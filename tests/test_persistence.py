"""Confirm progress persists across app restarts.

Real close/reopen test: run as TWO separate process invocations sharing the
same ECOLEARN_PROGRESS_DB file. Because they're different processes, the only
thing connecting them is the on-disk SQLite database — exactly what a user
closing and reopening the app relies on.

    python tests/test_persistence.py seed     # process 1: write, then exit
    python tests/test_persistence.py verify   # process 2: fresh — read it back

'seed' masters two concepts via the same store call submit_assessment uses
internally (no LLM, so the persistence check is deterministic). 'verify' loads
the student through the API exactly as onboarding would on reopen, then reads
get_roadmap and asserts the mastery — and the prereq unlocks it implies — were
restored.
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

from src import platform_api as api  # noqa: E402
from src.progress import store  # noqa: E402

CHAPTER = "motion_straight_line"
NAME = "Persist Test"


def seed() -> None:
    profile = api.create_or_load_student(NAME, "football", "Class 11")
    sid = profile["student_id"]
    # update_progress is exactly what submit_assessment writes on a pass.
    store.update_progress(sid, "position", score=3)
    store.update_progress(sid, "distance", score=3)
    print(f"[seed] student={sid!r} mastered position + distance.")
    print("[seed] process exiting — nothing kept in memory.")


def verify() -> None:
    # On reopen the app re-onboards, which loads (not recreates) the student.
    sid = api.create_or_load_student(NAME, "football", "Class 11")["student_id"]
    roadmap = api.get_roadmap(sid, CHAPTER)
    status = {r["concept_id"]: r["status"] for r in roadmap}

    print(f"[verify] FRESH process read roadmap for {sid!r}:")
    for r in roadmap:
        print(f"    {r['name']:<34} {r['status']}")

    assert status["position"] == "mastered", "position should persist as mastered"
    assert status["distance"] == "mastered", "distance should persist as mastered"
    # The restored mastery must also drive the derived state correctly:
    assert status["displacement"] == "available", "displacement unlocks after position"
    assert status["speed"] == "available", "speed unlocks after distance"
    assert status["velocity"] == "locked", "velocity still locked (needs displacement+speed)"
    print("[verify] PASS — roadmap state fully restored from SQLite across processes.")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "verify"
    if mode == "seed":
        seed()
    else:
        verify()
