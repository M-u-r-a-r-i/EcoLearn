"""Learning Path Engine — decide what a student should learn next.

This is the proactive brain of the platform. Given a student and a chapter, it
reads the student's persisted progress and the chapter's prerequisite-ordered
concepts, and answers two questions:

    next_concept(student_id, chapter_id)  -> the single best next step + why
    get_roadmap(student_id, chapter_id)   -> every concept tagged
                                             mastered / available / locked

The engine never invents pedagogy of its own: ordering and prerequisites come
from the curriculum spine (src/curriculum), mastery comes from the progress
store (src/progress). The engine is the rule that combines them.

`next_concept` policy, in order:
  1. Spaced repetition — if a mastered concept in this chapter hasn't been
     revisited in REVIEW_INTERVAL_DAYS, surface it for review first. A forgotten
     prerequisite quietly undermines everything built on top of it.
  2. Forward progress — otherwise recommend the first not-yet-mastered concept
     (in teaching order) whose prerequisites are ALL mastered.
  3. Done / blocked — if nothing is learnable, say whether the chapter is fully
     mastered or blocked on a prerequisite from elsewhere.
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
KIND_BLOCKED = "blocked"  # next concept locked by an unmet prerequisite


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
        raise ValueError(
            f"Chapter {chapter_id!r} has no concepts (or doesn't exist). "
            f"Known chapters: {', '.join(known)}"
        )
    return concepts


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

    # 2. Forward progress: first not-yet-cleared concept whose prerequisites are
    #    all cleared. A 2/3 pass "clears" a concept, so a student who chose to
    #    move on past a partial pass keeps advancing.
    for c in concepts:
        if c.id in cleared:
            continue
        prereqs = resolve_prerequisites(c.id, subject)  # direct prerequisites
        missing = [p for p in prereqs if p.id not in cleared]
        if not missing:
            if prereqs:
                reason = (
                    f"Next in sequence: you've cleared its prerequisites "
                    f"({', '.join(p.name for p in prereqs)}), so {c.name} is "
                    f"now unlocked and you haven't cleared it yet."
                )
            else:
                reason = (
                    f"Starting point: {c.name} has no prerequisites and you "
                    f"haven't cleared it yet."
                )
            return Recommendation(kind=KIND_NEW, concept=c, reason=reason)

    # 3. Nothing learnable: either the chapter is done, or it's blocked.
    uncleared = [c for c in concepts if c.id not in cleared]
    if not uncleared:
        return Recommendation(
            kind=KIND_DONE,
            concept=None,
            reason=(
                "You've worked through every concept in this chapter. There's "
                "nothing due for review right now either — well done."
            ),
        )

    first = uncleared[0]
    missing = [p for p in resolve_prerequisites(first.id, subject)
               if p.id not in cleared]
    return Recommendation(
        kind=KIND_BLOCKED,
        concept=first,
        reason=(
            f"{first.name} is next, but it's locked until you clear its "
            f"prerequisite(s): {', '.join(p.name for p in missing)}. "
            f"Those live earlier in the curriculum — work through them first."
        ),
    )


# Roadmap status labels (drive the roadmap UI).
ROADMAP_MASTERED = "mastered"
ROADMAP_AVAILABLE = "available"
ROADMAP_LOCKED = "locked"


def get_roadmap(student_id: str, chapter_id: str) -> list[dict]:
    """Return every concept in the chapter tagged with its roadmap status.

    Status is one of:
      - "mastered"  : the student has mastered it (3/3) — the gold badge
      - "available" : not mastered, but all prerequisites are cleared (>=2/3);
                      includes concepts the student passed at 2/3 and can
                      revisit to fully master
      - "locked"    : not mastered, and at least one prerequisite is not cleared

    Each entry also carries the underlying progress detail (progress_status,
    best_score, attempts) and, for locked concepts, the missing prerequisite
    ids — everything a roadmap view needs to render without re-querying.
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

        if c.id in mastered:
            status = ROADMAP_MASTERED
        elif not missing:
            status = ROADMAP_AVAILABLE
        else:
            status = ROADMAP_LOCKED

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
