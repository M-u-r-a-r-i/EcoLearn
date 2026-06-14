"""Simulate a student working through a chapter, step by step.

At each step we ask the engine what to learn next, assert that its
recommendation never violates prerequisites, print the choice and the engine's
reason, then "master" that concept and repeat — until the chapter is done.

Then a second scenario back-dates one mastered concept's last_seen to prove the
spaced-repetition path surfaces it for review.

Run from the project root:
    venv\\Scripts\\python.exe tests\\test_path_engine.py
No API calls; pure logic against a throwaway SQLite DB.
"""

from __future__ import annotations

import os
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PROJECT_ROOT))

# Point the store at a throwaway DB BEFORE importing it, so the real
# data/progress.db is never touched. store._db_path() reads this lazily.
_TMP_DB = os.path.join(tempfile.gettempdir(), "ecolearn_test_progress.db")
if os.path.exists(_TMP_DB):
    os.remove(_TMP_DB)
os.environ["ECOLEARN_PROGRESS_DB"] = _TMP_DB

from src.curriculum.loader import load_subject, resolve_prerequisites  # noqa: E402
from src.path import engine  # noqa: E402
from src.progress import store  # noqa: E402

CHAPTER = "motion_straight_line"
STUDENT = "sim_student"


def _subject():
    return load_subject(engine._curriculum_path())


def _chapter_concept_ids() -> set[str]:
    subject = _subject()
    return {c.id for c in engine._chapter_concepts(subject, CHAPTER)}


def simulate_full_chapter() -> None:
    print("=" * 70)
    print("SCENARIO 1 — master the chapter one concept at a time")
    print("=" * 70)

    subject = _subject()
    mastered_so_far: set[str] = set()
    step = 0
    max_steps = 50  # safety net against an accidental infinite loop

    while step < max_steps:
        rec = engine.next_concept(STUDENT, CHAPTER)

        if rec.kind == engine.KIND_DONE:
            print(f"\n[done] {rec.reason}")
            break

        assert rec.kind == engine.KIND_NEW, (
            f"Expected a NEW recommendation while learning, got {rec.kind!r} "
            f"({rec.reason})"
        )
        c = rec.concept
        assert c is not None

        # THE INVARIANT: every (transitive) prerequisite must already be
        # mastered at the moment this concept is recommended.
        prereqs = resolve_prerequisites(c.id, subject, transitive=True)
        unmet = [p.id for p in prereqs if p.id not in mastered_so_far]
        assert not unmet, (
            f"PREREQUISITE VIOLATION: engine recommended {c.id!r} but these "
            f"prerequisites are not yet mastered: {unmet}"
        )

        print(f"\nStep {step + 1}: learn '{c.name}'  (id={c.id})")
        print(f"  reason: {rec.reason}")
        if prereqs:
            print(f"  prereqs satisfied: {[p.id for p in prereqs]}")

        # Master it (top score) and move on.
        store.update_progress(STUDENT, c.id, score=3)
        mastered_so_far.add(c.id)
        step += 1

    # The engine should have walked us through the entire chapter.
    expected = _chapter_concept_ids()
    assert mastered_so_far == expected, (
        f"Did not master every concept. Missing: {expected - mastered_so_far}"
    )
    print(f"\nOK — mastered all {len(expected)} concepts with zero prerequisite "
          f"violations.")


def show_roadmap_midway() -> None:
    print("\n" + "=" * 70)
    print("SCENARIO 2 — roadmap with a partial-progress student")
    print("=" * 70)

    fresh = "roadmap_student"
    # Master only the first two foundational concepts.
    store.update_progress(fresh, "position", score=3)
    store.update_progress(fresh, "distance", score=3)

    print(f"\nRoadmap for {fresh!r} (mastered: position, distance):\n")
    print(f"  {'concept':<28} {'status':<12} prereqs-missing")
    print(f"  {'-' * 28} {'-' * 12} {'-' * 20}")
    for row in engine.get_roadmap(fresh, CHAPTER):
        missing = ", ".join(row["missing_prerequisites"]) or "—"
        print(f"  {row['name']:<28} {row['status']:<12} {missing}")

    rec = engine.next_concept(fresh, CHAPTER)
    print(f"\n  next_concept -> {rec.kind}: "
          f"{rec.concept.name if rec.concept else '(none)'}")
    print(f"  reason: {rec.reason}")


def show_spaced_repetition() -> None:
    print("\n" + "=" * 70)
    print("SCENARIO 3 — spaced repetition surfaces a stale mastered concept")
    print("=" * 70)

    rev = "review_student"
    # Master two concepts, then back-date 'position' so it looks long-neglected.
    store.update_progress(rev, "position", score=3)
    store.update_progress(rev, "distance", score=3)
    stale_time = datetime.now(tz=timezone.utc) - timedelta(days=10)
    store.mark_reviewed(rev, "position", seen_at=stale_time)

    rec = engine.next_concept(rev, CHAPTER)
    print(f"\n  position last seen 10 days ago; review threshold = "
          f"{engine._review_interval_days()} days")
    print(f"  next_concept -> {rec.kind}: "
          f"{rec.concept.name if rec.concept else '(none)'}")
    print(f"  reason: {rec.reason}")

    assert rec.kind == engine.KIND_REVIEW, (
        f"Expected a REVIEW recommendation for the stale concept, got {rec.kind}"
    )
    assert rec.concept is not None and rec.concept.id == "position", (
        "Expected the stale concept 'position' to be surfaced for review"
    )
    print("\nOK — engine correctly prioritised review over new material.")


if __name__ == "__main__":
    simulate_full_chapter()
    show_roadmap_midway()
    show_spaced_repetition()
    print("\nAll scenarios passed.")
