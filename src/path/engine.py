"""Learning Path Engine — decide what a student should learn next.

This is the proactive brain of the platform. Given a student and a chapter, it
reads the student's persisted progress and the chapter's prerequisite-ordered
concepts, and answers two questions:

    next_concept(student_id, chapter_id)  -> the single best next step + why
    get_roadmap(student_id, chapter_id)   -> every concept tagged
                                             mastered / available

The engine never invents pedagogy of its own: ordering and prerequisites come
from the curriculum spine (src/curriculum), mastery comes from the progress
store (src/progress). The engine is the rule that combines them.

NOTHING IS EVER LOCKED (user decision, 2026-09-21). Prerequisites are advice,
not gates: a student may open any concept in any chapter. With 28 chapters, hard
gating would lock a Class 12 student out of Class 12 chapters behind Class 11
concepts they never studied in the app. Uncleared prerequisites are still
reported — as "brush up first" suggestions — in both the recommendation reason
and the roadmap's `missing_prerequisites` field.

`next_concept` policy, in order:
  1. Spaced repetition — if a mastered concept in this chapter hasn't been
     revisited in REVIEW_INTERVAL_DAYS, surface it for review first. A forgotten
     prerequisite quietly undermines everything built on top of it.
  2. Forward progress — otherwise recommend the first not-yet-cleared concept
     in teaching order. Teaching order already puts prerequisites first, so a
     student following the recommendations meets them in a sensible sequence.
  3. Done — every concept in the chapter is cleared.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from src.curriculum.loader import (
    load_subject,
    resolve_prerequisites,
    teaching_order,
)
from src.curriculum.schema import Concept, Subject
# NotFoundError subclasses ValueError, so callers that already do
# `except ValueError` keep working — the HTTP layer just gains the precision to
# answer 404 instead of 400 for an unknown chapter.
from src.errors import NotFoundError
from src.progress import store

# Project root = .../EcoLearn/  (this file lives at .../EcoLearn/src/path/).
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_CURRICULUM = _PROJECT_ROOT / "data" / "curriculum" / "physics.yaml"

# How long a mastered concept may go unrevisited before the engine suggests a
# review. Deliberately simple — one threshold, not a full SM-2 schedule.
_DEFAULT_REVIEW_INTERVAL_DAYS = 7


# Recommendation kinds.
KIND_NEW = "new"        # learn this for the first time
KIND_REVIEW = "review"  # revisit a mastered concept (spaced repetition)
KIND_DONE = "done"      # whole chapter mastered, nothing due
# No longer returned — nothing is locked. Kept because UIs and older clients
# still branch on the string "blocked".
KIND_BLOCKED = "blocked"


@dataclass
class Recommendation:
    """What the engine thinks the student should do next, and why."""

    kind: str                 # one of KIND_*
    concept: Concept | None   # None only when kind == KIND_DONE
    reason: str               # human-readable justification


def _curriculum_path() -> Path:
    raw = os.getenv("ECOLEARN_CURRICULUM")
    return Path(raw) if raw else _DEFAULT_CURRICULUM


def _review_interval_days() -> int:
    raw = os.getenv("ECOLEARN_REVIEW_DAYS")
    if raw and raw.strip():
        try:
            return int(raw)
        except ValueError:
            pass
    return _DEFAULT_REVIEW_INTERVAL_DAYS


def _load_subject() -> Subject:
    return load_subject(_curriculum_path())


def _chapter_concepts(subject: Subject, chapter_id: str) -> list[Concept]:
    """Return this chapter's concepts in teaching order.

    `teaching_order` sorts the whole subject by (order, id); filtering to one
    chapter preserves the author's intended within-chapter sequence.
    """
    concepts = [c for c in teaching_order(subject) if c.chapter_id == chapter_id]
    if not concepts:
        known = sorted({c.chapter_id for c in teaching_order(subject)})
        raise NotFoundError(
            f"Chapter {chapter_id!r} has no concepts (or doesn't exist). "
            f"Known chapters: {', '.join(known)}"
        )
    return concepts


def list_chapters() -> list[dict]:
    """Return every chapter in the subject, in teaching (document) order.

    Each entry: {id, name, unit_id, unit_name, grade, domain, concept_count}.
    The unit and grade fields let a UI group 29 chapters as class → unit →
    chapter instead of one long flat list; `id` and `name` are unchanged, so
    older callers (the Streamlit chapter selector) keep working.
    """
    subject = _load_subject()
    return [
        {
            "id": ch.id,
            "name": ch.name,
            "unit_id": unit.id,
            "unit_name": unit.name,
            "grade": ch.grade,
            "domain": ch.domain.value,
            "concept_count": len(ch.concepts),
        }
        for unit in subject.units
        for ch in unit.chapters
    ]


def find_concept(concept_id: str) -> Concept | None:
    """Look up a single concept by id across the whole curriculum.

    Public helper for callers (e.g. the service layer) that have a concept_id
    and need its name / learning_objective without re-loading the subject
    themselves. Returns None if the id isn't found.
    """
    subject = _load_subject()
    for c in teaching_order(subject):
        if c.id == concept_id:
            return c
    return None


def _parse_ts(raw: str | None) -> datetime | None:
    if not raw:
        return None
    try:
        dt = datetime.fromisoformat(raw)
    except ValueError:
        return None
    # Treat naive timestamps as UTC so comparisons never raise.
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def next_concept(
    student_id: str,
    chapter_id: str,
    *,
    now: datetime | None = None,
) -> Recommendation:
    """Return the single best next step for this student in this chapter.

    `now` is injectable so tests can exercise the spaced-repetition path
    deterministically; it defaults to the current UTC time.
    """
    now = now or datetime.now(tz=timezone.utc)
    subject = _load_subject()
    concepts = _chapter_concepts(subject, chapter_id)
    progress = store.get_progress(student_id)
    mastered = store.get_mastered_concepts(student_id)  # gold (3/3), for review
    cleared = store.get_cleared_concepts(student_id)    # passed (>=2/3), for progress

    review_days = _review_interval_days()

    # 1. Spaced repetition: the most-overdue *mastered* concept in this chapter.
    #    We only schedule review for concepts the student truly mastered (3/3),
    #    not ones they merely scraped a pass on.
    overdue: list[tuple[datetime, int, Concept]] = []
    for c in concepts:
        if c.id not in mastered:
            continue
        last_seen = _parse_ts(progress.get(c.id, {}).get("last_seen"))
        if last_seen is None:
            continue
        age_days = (now - last_seen).days
        if age_days >= review_days:
            overdue.append((last_seen, age_days, c))
    if overdue:
        overdue.sort(key=lambda t: t[0])  # oldest last_seen first
        _, age_days, c = overdue[0]
        return Recommendation(
            kind=KIND_REVIEW,
            concept=c,
            reason=(
                f"You mastered {c.name} but last practised it {age_days} days "
                f"ago. A quick review keeps it solid before you build further."
            ),
        )

    # 2. Forward progress: the first not-yet-cleared concept in teaching order.
    #    A 2/3 pass "clears" a concept, so a student who chose to move on past a
    #    partial pass keeps advancing. Uncleared prerequisites never block — they
    #    become a suggestion in the reason.
    for c in concepts:
        if c.id in cleared:
            continue
        prereqs = resolve_prerequisites(c.id, subject)  # direct prerequisites
        missing = [p for p in prereqs if p.id not in cleared]
        if not prereqs:
            reason = f"Starting point: {c.name} doesn't build on anything earlier."
        elif not missing:
            reason = (
                f"Next in sequence: you've cleared what it builds on "
                f"({', '.join(p.name for p in prereqs)}), so {c.name} is a "
                f"natural next step."
            )
        else:
            reason = (
                f"Next in sequence: {c.name}. It builds on "
                f"{', '.join(p.name for p in missing)} — a quick brush-up on "
                f"those first will make it easier, but you can start right away."
            )
        return Recommendation(kind=KIND_NEW, concept=c, reason=reason)

    # 3. Everything in the chapter is cleared.
    return Recommendation(
        kind=KIND_DONE,
        concept=None,
        reason=(
            "You've worked through every concept in this chapter. There's "
            "nothing due for review right now either — well done."
        ),
    )


# Roadmap status labels (drive the roadmap UI).
ROADMAP_MASTERED = "mastered"
ROADMAP_AVAILABLE = "available"
# "locked" is no longer produced — nothing is locked. Kept for older clients.
ROADMAP_LOCKED = "locked"


def get_roadmap(student_id: str, chapter_id: str) -> list[dict]:
    """Return every concept in the chapter tagged with its roadmap status.

    Status is one of:
      - "mastered"  : the student has mastered it (3/3) — the gold badge
      - "available" : everything else. Nothing is ever locked.

    Each entry also carries the underlying progress detail (progress_status,
    best_score, attempts) and `missing_prerequisites`: the ids of prerequisites
    not yet cleared (>=2/3), for the UI to show as "brush up first" hints.
    """
    subject = _load_subject()
    concepts = _chapter_concepts(subject, chapter_id)
    progress = store.get_progress(student_id)
    mastered = store.get_mastered_concepts(student_id)
    cleared = store.get_cleared_concepts(student_id)

    roadmap: list[dict] = []
    for c in concepts:
        prereqs = resolve_prerequisites(c.id, subject)
        missing = [p.id for p in prereqs if p.id not in cleared]

        status = ROADMAP_MASTERED if c.id in mastered else ROADMAP_AVAILABLE

        row = progress.get(c.id, {})
        roadmap.append({
            "concept_id": c.id,
            "name": c.name,
            "order": c.order,
            "status": status,
            "progress_status": row.get("status", store.STATUS_NOT_YET),
            "best_score": row.get("best_score", 0),
            "attempts": row.get("attempts", 0),
            "missing_prerequisites": missing,
        })
    return roadmap
