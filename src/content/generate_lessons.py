"""Offline lesson factory.

Pre-generates one Lesson per (concept, interest) pair for a chapter, using the
existing analogy-generator → critic pipeline from src/pipeline.py.

Output layout:
  data/lessons/{concept_id}__{interest}.json   — one lesson per file
  data/lessons/flagged.jsonl                   — append-only log of non-PASSed lessons

Usage (from project root):
  python -m src.content.generate_lessons
or import and call generate_all_lessons() directly.
"""

from __future__ import annotations

import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.agents.polisher import polish_explanation
from src.content.lesson_schema import Lesson, LessonMetadata
from src.curriculum.loader import load_subject
from src.curriculum.schema import Chapter
from src.pipeline import explain_with_review


_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_CURRICULUM_PATH = _PROJECT_ROOT / "data" / "curriculum" / "physics.yaml"
_LESSONS_DIR = _PROJECT_ROOT / "data" / "lessons"

# Extra gap between consecutive pipeline runs to avoid burst rate-limiting.
# The pipeline itself already sleeps 13 s between generate and critique calls.
_INTER_LESSON_DELAY_SECONDS = 5

# Strips the trailing "[ANALOGY_QUALITY: N]" self-rating line.
_QUALITY_LINE_RE = re.compile(
    r'\[ANALOGY_QUALITY:\s*\d+\].*$',
    re.IGNORECASE | re.MULTILINE,
)


# ---------------------------------------------------------------------------
# Section parser
# ---------------------------------------------------------------------------

def _parse_sections(raw: str) -> tuple[str, str, str]:
    """Split raw generator output into (body, worked_example, check_question).

    Recognises both the raw numbered format ("1. SCENARIO") and the polished
    markdown format ("### Scenario"). Falls back to body=full_text if the
    three-section structure isn't found — better to save imperfect content
    than to silently drop a lesson.
    """
    text = _QUALITY_LINE_RE.sub("", raw).strip()

    patterns = [
        re.compile(
            r"^(?:1\.\s*SCENARIO|#{1,3}\s*Scenario)\s*$",
            re.IGNORECASE | re.MULTILINE,
        ),
        re.compile(
            r"^(?:2\.\s*FORMAL\s+RESTATEMENT|#{1,3}\s*Formal\s+Restatement)\s*$",
            re.IGNORECASE | re.MULTILINE,
        ),
        re.compile(
            r"^(?:3\.\s*SELF-?CHECK\s+QUESTION|#{1,3}\s*Self-?Check\s+Question)\s*$",
            re.IGNORECASE | re.MULTILINE,
        ),
    ]

    spans: list[tuple[int, int]] = []
    for p in patterns:
        m = p.search(text)
        if m:
            spans.append((m.start(), m.end()))

    if len(spans) == 3:
        body = _strip_trailing_rule(text[spans[0][1] : spans[1][0]])
        worked = _strip_trailing_rule(text[spans[1][1] : spans[2][0]])
        check = _strip_trailing_rule(text[spans[2][1] :])
        return body, worked, check

    # Structure not found — keep everything in body so no content is lost.
    return text, "", ""


def _strip_trailing_rule(section: str) -> str:
    """Drop a trailing markdown horizontal rule (`---`) left by the section split.

    The polisher separates sections with `---`; when we slice between headers
    that divider lands at the end of the preceding section. Remove it so each
    stored field is clean content with no dangling separator.
    """
    return re.sub(r"\n+-{3,}\s*$", "", section.strip()).strip()


# ---------------------------------------------------------------------------
# Lesson builder
# ---------------------------------------------------------------------------

def _build_lesson(concept_id: str, interest: str, result: dict[str, Any]) -> Lesson:
    # Polish BEFORE parsing: the raw generator output is full of scratchpad and
    # uses inconsistent section labels, so the section parser can't split it.
    # The polisher emits clean "### Scenario / ### Formal Restatement /
    # ### Self-Check Question" markdown that _parse_sections recognises.
    polished = polish_explanation(result["explanation"])
    body, worked_example, check_question = _parse_sections(polished)
    verdict = result["critique"]

    # A soft-PASS caused by a quota-exhausted critic carries an "error" key.
    # Offline generation can afford to be strict: treat unreviewed as not passed.
    critic_passed = verdict.get("verdict") == "PASS" and "error" not in verdict

    return Lesson(
        concept_id=concept_id,
        interest=interest,
        body=body,
        worked_example=worked_example,
        check_question=check_question,
        metadata=LessonMetadata(
            generated_at=datetime.now(tz=timezone.utc),
            critic_passed=critic_passed,
            critic_verdict=verdict.get("verdict", "ERROR"),
            attempts=result["attempts"],
            critic_feedback=verdict.get("feedback", ""),
        ),
    )


def _looks_unpolished(lesson: Lesson) -> bool:
    """True if the structured split never happened (raw body, empty sections).

    Lessons generated before the polisher was wired in stored the full raw
    generator output in `body` with empty worked_example/check_question. That
    empty-section signature is how we detect them for a re-polish pass.
    """
    return not (lesson.worked_example.strip() and lesson.check_question.strip())


def repolish_existing(interests: list[str] | None = None) -> dict[str, Any]:
    """Polish lessons that were saved with raw, unsplit bodies, in place.

    Earlier factory runs stored raw generator output (scratchpad and all) in
    `body`, because the polisher wasn't wired in yet. This pass repairs them
    without regenerating: polish the raw body, re-split into the three
    sections, rewrite the JSON.

    Idempotent and resumable:
      - a lesson whose sections are already populated is skipped;
      - if the polish fails open (e.g. quota), the raw body is left untouched
        so the next run can retry — we never half-write a lesson.
    """
    _LESSONS_DIR.mkdir(parents=True, exist_ok=True)
    repolished = skipped = retry_later = 0

    tidied = 0
    for path in sorted(_LESSONS_DIR.glob("*__*.json")):
        lesson = Lesson.model_validate_json(path.read_text(encoding="utf-8"))
        if interests is not None and lesson.interest not in interests:
            continue
        if not _looks_unpolished(lesson):
            # Already split — but earlier ones may carry a dangling `---` from
            # before the parser stripped it. Tidy in place with no API call.
            new_body = _strip_trailing_rule(lesson.body)
            new_worked = _strip_trailing_rule(lesson.worked_example)
            new_check = _strip_trailing_rule(lesson.check_question)
            if (new_body, new_worked, new_check) != (
                lesson.body, lesson.worked_example, lesson.check_question
            ):
                lesson.body, lesson.worked_example, lesson.check_question = (
                    new_body, new_worked, new_check,
                )
                path.write_text(lesson.model_dump_json(indent=2), encoding="utf-8")
                tidied += 1
            skipped += 1
            continue

        print(f"  polishing {path.name} ...")
        polished = polish_explanation(lesson.body)
        body, worked, check = _parse_sections(polished)

        if not (worked.strip() and check.strip()):
            # Polish failed open or the markdown wasn't parseable — keep the
            # raw body intact so a later run retries it. Don't half-write.
            print("    still unpolished (fail-open) — will retry next run")
            retry_later += 1
            continue

        lesson.body = body
        lesson.worked_example = worked
        lesson.check_question = check
        path.write_text(lesson.model_dump_json(indent=2), encoding="utf-8")
        repolished += 1
        time.sleep(_INTER_LESSON_DELAY_SECONDS)

    print(
        f"\nRe-polish done: {repolished} fixed, {skipped} already clean "
        f"({tidied} tidied), {retry_later} to retry later."
    )
    return {
        "repolished": repolished,
        "skipped": skipped,
        "tidied": tidied,
        "retry_later": retry_later,
    }


# ---------------------------------------------------------------------------
# Save / flag helpers
# ---------------------------------------------------------------------------

def _save_lesson(lesson: Lesson) -> Path:
    _LESSONS_DIR.mkdir(parents=True, exist_ok=True)
    path = _LESSONS_DIR / f"{lesson.concept_id}__{lesson.interest}.json"
    path.write_text(lesson.model_dump_json(indent=2), encoding="utf-8")
    return path


def _rebuild_flagged_log() -> int:
    """Rewrite flagged.jsonl from scratch by scanning every saved lesson.

    Rebuilding from disk (rather than appending per-run) keeps the log
    consistent across resumed/partial runs — no duplicate entries, no stale
    lines for lessons that were later regenerated and passed.

    Returns the number of flagged lessons written.
    """
    _LESSONS_DIR.mkdir(parents=True, exist_ok=True)
    flagged_path = _LESSONS_DIR / "flagged.jsonl"

    entries: list[dict] = []
    for json_path in sorted(_LESSONS_DIR.glob("*__*.json")):
        try:
            lesson = Lesson.model_validate_json(
                json_path.read_text(encoding="utf-8")
            )
        except Exception:  # noqa: BLE001 — skip anything that isn't a valid lesson.
            continue
        if not lesson.metadata.critic_passed:
            entries.append(
                {
                    "concept_id": lesson.concept_id,
                    "interest": lesson.interest,
                    "critic_verdict": lesson.metadata.critic_verdict,
                    "attempts": lesson.metadata.attempts,
                    "critic_feedback": lesson.metadata.critic_feedback[:300],
                }
            )

    with flagged_path.open("w", encoding="utf-8") as fh:
        for entry in entries:
            fh.write(json.dumps(entry) + "\n")
    return len(entries)


# ---------------------------------------------------------------------------
# Chapter finder
# ---------------------------------------------------------------------------

def _find_chapter(subject, chapter_id: str) -> Chapter:
    for unit in subject.units:
        for chapter in unit.chapters:
            if chapter.id == chapter_id:
                return chapter
    raise ValueError(
        f"Chapter {chapter_id!r} not found in subject {subject.id!r}. "
        f"Available chapters: "
        + ", ".join(
            ch.id for unit in subject.units for ch in unit.chapters
        )
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def _summarize_from_disk(
    concepts, interests: list[str]
) -> dict[str, Any]:
    """Compute the run summary by scanning every saved lesson on disk.

    Reading from disk (rather than only this run's in-memory counters) means
    the summary reflects ALL completed lessons, even ones written by a prior
    partial/interrupted run that this resume skipped over.
    """
    passed = 0
    flagged: list[dict] = []
    saved: list[str] = []
    missing: list[str] = []

    for concept in concepts:
        for interest in interests:
            path = _LESSONS_DIR / f"{concept.id}__{interest}.json"
            if not path.exists():
                missing.append(f"{concept.id}__{interest}")
                continue
            saved.append(path.name)
            lesson = Lesson.model_validate_json(path.read_text(encoding="utf-8"))
            if lesson.metadata.critic_passed:
                passed += 1
            else:
                flagged.append(
                    {
                        "concept_id": lesson.concept_id,
                        "interest": lesson.interest,
                        "verdict": lesson.metadata.critic_verdict,
                        "feedback": lesson.metadata.critic_feedback[:200],
                    }
                )

    return {
        "total": len(concepts) * len(interests),
        "saved": len(saved),
        "passed": passed,
        "flagged": len(flagged),
        "missing": missing,
        "flagged_list": flagged,
        "saved_paths": saved,
    }


def generate_all_lessons(
    chapter_id: str,
    interests: list[str],
    level: str = "Class 11",
    max_retries: int = 2,
    skip_existing: bool = True,
) -> dict[str, Any]:
    """Generate and save lessons for every (concept, interest) pair in a chapter.

    Args:
        chapter_id:    The chapter's id slug (e.g. "motion_straight_line").
        interests:     List of interest names (e.g. ["football", "gaming"]).
        level:         Student level string passed to the generator.
        max_retries:   Generator retry budget on FAIL (same as pipeline default).
        skip_existing: If True (default), a pair whose JSON already exists on
                       disk is skipped — making the run resumable after an
                       interruption. Set False to force a full regenerate.

    Returns:
        Summary dict computed from disk: {total, saved, passed, flagged,
        missing, flagged_list, saved_paths}.
    """
    subject = load_subject(_CURRICULUM_PATH)
    chapter = _find_chapter(subject, chapter_id)
    concepts = chapter.concepts  # already in authored teaching order

    total = len(concepts) * len(interests)
    print(
        f"\nGenerating up to {total} lessons"
        f"  ({len(concepts)} concepts × {len(interests)} interests: {interests})"
    )
    print(f"Chapter  : {chapter.name}")
    print(f"Level    : {level}")
    print(f"Output   : {_LESSONS_DIR}")
    print(f"Resume   : skip_existing={skip_existing}\n")

    pairs = [(c, i) for c in concepts for i in interests]

    for idx, (concept, interest) in enumerate(pairs, start=1):
        path = _LESSONS_DIR / f"{concept.id}__{interest}.json"
        print(f"\n{'─' * 60}")
        print(f"[{idx}/{total}]  {concept.name!r}  ×  {interest!r}")

        if skip_existing and path.exists():
            print(f"  SKIP   already on disk → {path.name}")
            continue

        try:
            result = explain_with_review(
                concept=concept.name,
                interest=interest,
                level=level,
                max_retries=max_retries,
            )
        except Exception as exc:  # noqa: BLE001 — one bad pair shouldn't kill the batch.
            print(f"  PIPELINE ERROR: {exc}")
            continue

        lesson = _build_lesson(concept.id, interest, result)
        _save_lesson(lesson)

        if lesson.metadata.critic_passed:
            print(f"  PASS   attempts={lesson.metadata.attempts}  → {path.name}")
        else:
            print(
                f"  FLAGGED  verdict={lesson.metadata.critic_verdict}"
                f"  attempts={lesson.metadata.attempts}  → {path.name}"
            )

        # Only sleep after a real API call, not after a skip.
        if idx < total:
            time.sleep(_INTER_LESSON_DELAY_SECONDS)

    # Rebuild the flag log + summary from disk so both are consistent with
    # whatever is actually saved, regardless of how many runs it took.
    n_flagged = _rebuild_flagged_log()
    summary = _summarize_from_disk(concepts, interests)

    print(f"\n{'═' * 60}")
    print(
        f"DONE  target={summary['total']}  saved={summary['saved']}  "
        f"passed={summary['passed']}  flagged={summary['flagged']}  "
        f"missing={len(summary['missing'])}"
    )
    if summary["missing"]:
        print("Missing (no file on disk): " + ", ".join(summary["missing"]))
    if n_flagged:
        print(f"Flagged log rebuilt: {n_flagged} entries → data/lessons/flagged.jsonl")

    return summary


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "repolish":
        # Repair pass: polish + section-split lessons saved with raw bodies.
        result = repolish_existing(interests=["football", "gaming"])
        print("\nRe-polish summary JSON:")
        print(json.dumps(result, indent=2, default=str))
    else:
        summary = generate_all_lessons(
            chapter_id="motion_straight_line",
            interests=["football", "gaming"],
        )
        print("\nFinal summary JSON:")
        print(json.dumps(summary, indent=2, default=str))
