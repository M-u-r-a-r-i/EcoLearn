"""The coaching-note agent: a short, privacy-safe note per student, for the teacher.

A teacher with 30 students can't read 30 dashboards. This turns each student's
numbers into a note a teacher can act on: what stands out, the evidence for it,
and one small thing to try. It is the third piece of the teacher loop: observe
(insights) -> plan the class (teacher agent) -> coach the individual (this).

HOW IT STAYS SAFE
  * The model never sees a name, username or id: students are S1, S2... and a
    "case file" holds only coarse facts (counts, fixed-option survey answers,
    the NAMES OF CONCEPTS they mixed up). No free text a child wrote.
  * Every note must cite its evidence: the case-file fields it rests on. A note
    that cites a field the student doesn't have is thrown away.
  * Notes describe behaviour, never the child: no diagnosis, no labels, no
    judgement. A note containing a name, a username or a labelling word is
    thrown away.
  * Anything thrown away, any failed call, and every student when no model is
    configured gets a deterministic RULES note instead. The page labels each
    note "AI" or "Rules", so a teacher always knows which they are reading.

The teacher is the audience and the decision-maker: these are suggestions to
check, not a verdict on a child.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Callable

_PROMPT_PATH = Path(__file__).resolve().parents[2] / "prompts" / "coaching_agent.txt"
BATCH = 8                    # students per model call: small JSON, fewer truncations
NOTE_WORDS = (5, 45)
STEP_WORDS = (4, 30)

# The only facts a case file may hold. A note's "evidence" must be a subset of
# the fields this student actually has.
FIELDS = ("lessons_opened", "minutes_read", "checks_answered", "first_try_right",
          "mastered_concepts", "days_since_active", "skim_share", "thumbs",
          "focus_span", "pace", "physics_feel", "maths_comfort", "top_hobby_level",
          "first_step", "mix_ups")

# Words that label a child instead of describing what they did. Not exhaustive: the
# prompt forbids them too; this is the backstop.
_LABELS = re.compile(
    r"\b(adhd|autis\w*|dyslex\w*|dyscalc\w*|depress\w*|anxiety|anxious disorder|disorder|"
    r"disabilit\w*|lazy|stupid|dumb|slow learner|weak student|low ability|gifted|"
    r"behaviou?r problem|diagnos\w*)\b", re.IGNORECASE)


def _words(text: str) -> int:
    return len(text.split())


def build_case(row: dict[str, Any], survey_traits: dict[str, Any] | None,
               observed: dict[str, Any], mix_ups: list[dict[str, Any]],
               days_since_active: int | None) -> dict[str, Any]:
    """One student's case file from numbers the dashboard already has. None values are
    dropped, so a missing fact is simply absent (never guessed)."""
    traits = survey_traits or {}
    top = next(iter((traits.get("hobby_levels") or {}).values()), None)
    case: dict[str, Any] = {
        "lessons_opened": row.get("lessons_opened"),
        "minutes_read": row.get("active_minutes"),
        "checks_answered": row.get("answered"),
        "first_try_right": (f"{row['first_try_correct']} of {row['answered']}"
                            if row.get("answered") else None),
        "mastered_concepts": row.get("mastered"),
        "days_since_active": days_since_active,
        "skim_share": (round(observed["skim_share"] * 100)
                       if observed.get("skim_share") is not None else None),
        "thumbs": (f"{row['thumbs_up']} up, {row['thumbs_down']} down"
                   if (row.get("thumbs_up") or row.get("thumbs_down")) else None),
        "focus_span": (traits.get("focus") or {}).get("span"),
        "pace": (traits.get("learning") or {}).get("pace"),
        "physics_feel": (traits.get("physics") or {}).get("feel"),
        "maths_comfort": (traits.get("physics") or {}).get("maths"),
        "top_hobby_level": top["level"] if top else None,
        "first_step": (traits.get("learning") or {}).get("first_step"),
        "mix_ups": [{"concept": m["concept"], "sure": bool(m.get("sure"))} for m in mix_ups[:3]] or None,
    }
    return {k: v for k, v in case.items() if v is not None}


# ---------------------------------------------------------------------------
# The rules fallback: same shape as a model note, built from the same case file.
# ---------------------------------------------------------------------------

def rules_note(case: dict[str, Any]) -> dict[str, Any]:
    findings: list[tuple[str, list[str], str]] = []  # (what we see, evidence, what to try)
    if not case.get("lessons_opened") and not case.get("checks_answered"):
        findings.append(("Hasn't opened a lesson yet.", ["lessons_opened"],
                         "Check the login slip works, and sit with them for a first lesson."))
    for m in case.get("mix_ups") or []:
        if m["sure"]:
            findings.append((f"Was sure of a wrong answer on {m['concept']}.", ["mix_ups"],
                             f"Ask them to explain {m['concept']} aloud before showing the answer."))
            break
    else:
        if case.get("mix_ups"):
            findings.append((f"Mixed something up on {case['mix_ups'][0]['concept']}.", ["mix_ups"],
                             "Revisit that idea with one worked example in class."))
    right = case.get("first_try_right")
    if right and case.get("checks_answered", 0) >= 3:
        good, total = (int(x) for x in right.split(" of "))
        if good / total < 0.5:
            findings.append((f"Right first time on {right} checks.", ["first_try_right", "checks_answered"],
                             "Go back one step: a short recap before the next concept."))
    if case.get("skim_share", 0) >= 50 and case.get("lessons_opened", 0) >= 3:
        findings.append((f"Skims lessons: {case['skim_share']}% were open under 30 seconds.",
                         ["skim_share", "lessons_opened"],
                         "Ask what they remember from the last lesson; slow down the rush to the check."))
    if (case.get("days_since_active") or 0) >= 7:
        findings.append((f"Quiet for {case['days_since_active']} days.", ["days_since_active"],
                         "A friendly nudge to pick up where they left off."))
    if case.get("physics_feel") in ("nervous", "dread"):
        findings.append(("Said physics makes them nervous or is a struggle.", ["physics_feel"],
                         "Start with a question they can get right, and praise the effort."))
    if not findings:
        steady = (f"Working steadily: right first time on {right}." if right
                  else "No concerns in the data so far.")
        return {"note": steady, "evidence": [k for k in ("first_try_right",) if k in case],
                "next_step": "Offer the next concept, or a stretch question if they are ready."}
    note = " ".join(f[0] for f in findings[:2])
    evidence = sorted({e for f in findings[:2] for e in f[1]})
    return {"note": note, "evidence": evidence, "next_step": findings[0][2]}


# ---------------------------------------------------------------------------
# The model path
# ---------------------------------------------------------------------------

def _validate(alias: str, value: Any, case: dict[str, Any], forbidden: list[str]) -> tuple[dict[str, Any] | None, str | None]:
    """(clean note, None) or (None, why it was rejected)."""
    if not isinstance(value, dict):
        return None, "not an object"
    note, step = value.get("note"), value.get("next_step")
    evidence = value.get("evidence")
    if not isinstance(note, str) or not isinstance(step, str) or not isinstance(evidence, list):
        return None, "missing note, next_step or evidence"
    note, step = note.strip(), step.strip()
    if not NOTE_WORDS[0] <= _words(note) <= NOTE_WORDS[1]:
        return None, f"note is {_words(note)} words"
    if not STEP_WORDS[0] <= _words(step) <= STEP_WORDS[1]:
        return None, f"next_step is {_words(step)} words"
    cited = [e for e in evidence if isinstance(e, str)]
    if not cited or any(e not in case for e in cited):
        return None, "evidence cites a fact this student doesn't have"
    text = f"{note} {step}"
    if _LABELS.search(text):
        return None, "labels the child"
    lowered = text.lower()
    if any(f and f.lower() in lowered for f in forbidden):
        return None, "contains a name or username"
    if re.search(r"https?://|www\.|@", text):
        return None, "contains a link"
    return {"note": note, "evidence": cited, "next_step": step}, None


def coach_class(cases: dict[str, dict[str, Any]], forbidden: list[str],
                chat: Callable[..., Any] | None, models_on: bool) -> dict[str, Any]:
    """Notes for every alias in `cases`.

    `chat` is llm.chat (or a test stand-in); `models_on` False skips the model at once.
    `forbidden` are strings no note may contain (the class's real names and usernames).

    Returns {"notes": {alias: {note, evidence, next_step, source: "ai"|"rules"}},
             "source": "agent"|"rules"|"mixed", "model": str|None,
             "trail": [{step, alias|batch, ok, detail}], "note": str|None}
    """
    notes: dict[str, dict[str, Any]] = {}
    trail: list[dict[str, Any]] = []
    model_used: str | None = None
    problem: str | None = None
    aliases = list(cases)
    if models_on and chat is not None:
        prompt = _PROMPT_PATH.read_text(encoding="utf-8")
        for start in range(0, len(aliases), BATCH):
            batch = aliases[start:start + BATCH]
            payload = {a: cases[a] for a in batch}
            message = (f"{prompt}\n\n---\nCASE FILES (JSON):\n"
                       f"{json.dumps(payload, ensure_ascii=False)}\n\nWrite the JSON now.")
            try:
                from src.llm.client import parse_json_object
                result = chat([{"role": "user", "content": message}], role="main",
                              temperature=0.3, max_tokens=min(4000, 260 * len(batch) + 300))
                model_used = getattr(result, "model", None) or model_used
                data = parse_json_object(result.text)
                if data is None:
                    raise ValueError("the reply wasn't a JSON object")
            except Exception as exc:  # noqa: BLE001 — any failure: rules for this batch
                problem = f"{type(exc).__name__}"
                trail.append({"step": "model", "batch": batch, "ok": False,
                              "detail": str(exc)[:200]})
                continue
            for alias in batch:
                clean, why = _validate(alias, data.get(alias), cases[alias], forbidden)
                if clean:
                    notes[alias] = {**clean, "source": "ai"}
                    trail.append({"step": "check", "alias": alias, "ok": True, "detail": ""})
                else:
                    trail.append({"step": "check", "alias": alias, "ok": False, "detail": why})
    for alias in aliases:
        if alias not in notes:
            notes[alias] = {**rules_note(cases[alias]), "source": "rules"}
    ai_count = sum(1 for n in notes.values() if n["source"] == "ai")
    source = "agent" if ai_count == len(notes) and notes else ("rules" if ai_count == 0 else "mixed")
    note = None
    if not models_on:
        note = "The AI assistant isn't configured on this server, so these notes were made by fixed rules."
    elif source == "rules":
        note = "The AI assistant couldn't be reached, so these notes were made by fixed rules."
    elif source == "mixed":
        note = (f"{len(notes) - ai_count} of {len(notes)} notes use fixed rules: the AI's note "
                "was missing or didn't pass the checks.")
    return {"notes": notes, "source": source, "model": model_used if ai_count else None,
            "trail": trail, "note": note, "failed": problem}
