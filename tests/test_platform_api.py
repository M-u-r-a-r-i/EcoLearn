"""Full student journey through ONLY the platform API boundary.

This test imports `src.platform_api` and nothing else from the domain — no
engine, store, lesson service, or pipeline imports. If the boundary is well
designed, a complete journey (sign up → see roadmap → get a lesson → answer →
ask for help → get the next lesson) is expressible through these five
functions alone. That is exactly what a real frontend would do.

Steps 4 (submit_assessment) and 5 (ask_help) call live LLMs (Gemma assessor +
the generate→critic→polish pipeline), so this is a slow, quota-using test. The
underlying agents fail open, so we assert on the response *contract* and print
the content rather than hard-failing on a transient API hiccup.

Run from the project root:
    venv\\Scripts\\python.exe tests\\test_platform_api.py
"""

from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PROJECT_ROOT))

# Throwaway DB so the real data/progress.db is untouched. Set before import.
_TMP_DB = os.path.join(tempfile.gettempdir(), "ecolearn_test_platform.db")
if os.path.exists(_TMP_DB):
    os.remove(_TMP_DB)
os.environ["ECOLEARN_PROGRESS_DB"] = _TMP_DB

from src import platform_api as api  # noqa: E402  (the ONLY domain import)

CHAPTER = "motion_straight_line"


def _rule(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main() -> None:
    # --- 1. create_or_load_student --------------------------------------
    _rule("STEP 1 — create_or_load_student")
    profile = api.create_or_load_student("Journey Student", "football", "Class 11")
    print(profile)
    assert profile["student_id"] == "journey-student"
    assert profile["interest"] == "football"
    sid = profile["student_id"]

    # Idempotency: loading again returns the same student.
    again = api.create_or_load_student("Journey Student", "football", "Class 11")
    assert again["student_id"] == sid
    assert again["created_at"] == profile["created_at"], "created_at must persist"
    print("  (re-load returns same student_id and created_at — OK)")

    # --- 2. get_roadmap (fresh student) ---------------------------------
    _rule("STEP 2 — get_roadmap (nothing mastered yet)")
    roadmap = api.get_roadmap(sid, CHAPTER)
    for row in roadmap:
        missing = ", ".join(row["missing_prerequisites"]) or "—"
        print(f"  {row['name']:<34} {row['status']:<10} missing: {missing}")
    statuses = {r["concept_id"]: r["status"] for r in roadmap}
    assert statuses["position"] == "available", "position has no prereqs → available"
    assert statuses["velocity"] == "locked", "velocity should be locked initially"

    # --- 3. get_next_lesson ---------------------------------------------
    _rule("STEP 3 — get_next_lesson")
    nxt = api.get_next_lesson(sid, CHAPTER)
    print(f"  status      : {nxt['status']}")
    print(f"  concept     : {nxt['concept_name']} ({nxt['concept_id']})")
    print(f"  reason      : {nxt['reason']}")
    assert nxt["status"] == "new"
    assert nxt["concept_id"] == "position", "first lesson should be the root concept"
    assert nxt["lesson"] is not None, "a pre-generated lesson should be served"
    lesson = nxt["lesson"]
    assert lesson["check_question"].strip(), "lesson must carry a check question"
    print(f"  lesson body : {lesson['body'][:90]}...")
    print(f"  check Q     : {lesson['check_question'][:90]}...")

    # --- 4. submit_assessment (LIVE — Gemma grader) ---------------------
    _rule("STEP 4 — submit_assessment (live grade)")
    answer = (
        "The total displacement is zero, because the striker starts and ends at "
        "the same point (the center spot), so the start-to-finish vector has zero "
        "magnitude. The total distance is large and positive — the full arc out to "
        "the penalty spot plus the path back — because distance adds up over the "
        "whole path regardless of direction."
    )
    graded = api.submit_assessment(sid, "position", answer)
    print(f"  score          : {graded['score']}")
    print(f"  mastery_signal : {graded['mastery_signal']}")
    print(f"  feedback       : {graded['feedback'][:140]}")
    print(f"  new mastery    : {graded['mastery']}")
    for key in ("score", "mastery_signal", "feedback", "mastery", "graded_question"):
        assert key in graded, f"assessment result missing {key!r}"
    assert graded["mastery"]["attempts"] >= 1, "an attempt should be recorded"

    # --- 5. ask_help (LIVE — full pipeline) -----------------------------
    _rule("STEP 5 — ask_help (live tutor pipeline)")
    help_resp = api.ask_help(
        sid, "position",
        "Why is displacement a vector but distance is not?",
    )
    print(f"  verdict  : {help_resp['verdict']}  (attempts={help_resp['attempts']})")
    print(f"  answer   :\n{help_resp['answer'][:400]}")
    for key in ("concept_id", "answer", "verdict", "attempts"):
        assert key in help_resp, f"help result missing {key!r}"
    assert isinstance(help_resp["answer"], str) and help_resp["answer"].strip()

    # --- 6. get_next_lesson again ---------------------------------------
    _rule("STEP 6 — get_next_lesson (after assessment)")
    nxt2 = api.get_next_lesson(sid, CHAPTER)
    print(f"  status   : {nxt2['status']}")
    print(f"  concept  : {nxt2['concept_name']} ({nxt2['concept_id']})")
    print(f"  reason   : {nxt2['reason']}")

    # The recommendation must stay prerequisite-correct regardless of the grade:
    #  - if 'position' was mastered (score 3), the engine advances to 'distance'
    #    or 'displacement' (both depend only on position);
    #  - otherwise it re-recommends 'position'.
    mastered_position = graded["mastery"]["status"] == "mastered"
    if mastered_position:
        assert nxt2["concept_id"] in {"distance", "displacement"}, (
            f"after mastering position, expected distance/displacement, "
            f"got {nxt2['concept_id']}"
        )
        print("  -> position mastered, engine advanced correctly.")
    else:
        assert nxt2["concept_id"] == "position", (
            "position not mastered, engine should re-recommend it"
        )
        print("  -> position not yet mastered, engine re-recommends it (correct).")

    print("\nFull journey passed — all six steps went through the API boundary "
          "only.")


if __name__ == "__main__":
    main()
