"""Multiple-choice grading: deterministic, server-side, no LLM.

Run:  venv\\Scripts\\python.exe tests\\test_mcq_grading.py

Why this test matters: grading used to call a cloud model, which cost money,
needed an API key and took seconds. Authored lessons carry their own answer key
and per-option misconceptions, so grading is now a lookup. This pins that:

  * the right letter masters the concept, the wrong one doesn't;
  * the answer key never reaches the browser (get_next_lesson);
  * a wrong pick gets the misconception that option was written to catch;
  * rubbish input is a 400-style error, not a silent score of 0.

Like every other test here it is a standalone script, not pytest, and it points
ECOLEARN_PROGRESS_DB at a temp file BEFORE importing the modules under test.
"""

from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

_DB = Path(tempfile.gettempdir()) / "ecolearn_test_mcq.db"
_DB.unlink(missing_ok=True)
os.environ["ECOLEARN_PROGRESS_DB"] = str(_DB)

from src.content import lesson_service  # noqa: E402
from src.errors import EcoLearnError  # noqa: E402
from src import platform_api as api  # noqa: E402

_checks = 0
_failed = 0


def check(condition: bool, label: str) -> None:
    global _checks, _failed
    _checks += 1
    if condition:
        print(f"  ok  {label}")
    else:
        _failed += 1
        print(f"  FAIL {label}")


# A concept that has an authored football lesson (Units and Measurement).
CONCEPT = "si_units"
INTEREST = "football"


def main() -> None:
    lesson = lesson_service.get_authored_lesson(CONCEPT, INTEREST)
    if lesson is None:
        print(f"SKIP: no authored lesson for {CONCEPT} x {INTEREST}")
        sys.exit(0)

    key = lesson.check.answer
    wrong = next(k for k in lesson.check.options if k != key)

    student = api.register_student(
        name="MCQ Tester", username="mcq_tester", password="hunter2hunter2",
        interest=INTEREST, level="Class 11",
    )
    sid = student["student_id"]

    print("\n[1] the answer key stays on the server")
    env = api.get_next_lesson(sid, "units_measurement", concept_id=CONCEPT)
    served = env["lesson"]
    check("check" in served and "options" in served["check"], "the lesson carries its options")
    check(set(served["check"]["options"]) == set(lesson.check.options), "all options are sent")
    blob = repr(served)
    check("answer" not in served["check"], "no answer key in the check")
    check("misconception" not in blob.lower(), "no misconceptions leak to the browser")
    check(
        isinstance(served.get("sections"), list) and len(served["sections"]) >= 3,
        "sections are sent separately so the UI can collapse them",
    )
    headings = [s["heading"] for s in served["sections"]]
    check("The story" in headings, f"the story is the first section (got {headings[:1]})")

    print("\n[2] a wrong pick: score 0, and the misconception it reveals")
    bad = api.submit_assessment(sid, CONCEPT, wrong)
    check(bad["score"] == 0, f"wrong pick scores 0 (got {bad['score']})")
    check(bad["correct"] is False, "correct flag is False")
    check(bad["mastery_signal"] == "not_yet", "mastery_signal is not_yet")
    check(bad["correct_option"] == key, "the right letter is returned for the review screen")
    expected_snippet = lesson.check.misconceptions[wrong].strip()[:40]
    check(expected_snippet in bad["feedback"], "feedback quotes that option's misconception")
    check(lesson.check.explanation.strip()[:40] in bad["feedback"], "feedback also explains the right answer")
    check(bad["mastery"]["attempts"] == 1, "the attempt is recorded")
    check(bad["mastery"]["status"] != "mastered", "a wrong answer does not master the concept")

    print("\n[3] the right pick: score 3, concept mastered")
    good = api.submit_assessment(sid, CONCEPT, key.lower())  # lowercase accepted
    check(good["score"] == 3, f"right pick scores 3 (got {good['score']})")
    check(good["correct"] is True, "correct flag is True")
    check(good["selected_option"] == key, "the picked letter is normalised to upper case")
    check(good["feedback"].startswith("Correct."), "feedback opens with Correct.")
    check(good["mastery"]["status"] == "mastered", "the concept is now mastered")
    check(good["mastery"]["best_score"] == 3, "best score is kept")

    print("\n[4] rubbish input is rejected, progress untouched")
    before = good["mastery"]["attempts"]
    for bad_input in ("", "Z", "the second one"):
        try:
            api.submit_assessment(sid, CONCEPT, bad_input)
            check(False, f"{bad_input!r} should be refused")
        except EcoLearnError:
            check(True, f"{bad_input!r} → EcoLearnError (400), not a score of 0")
    roadmap = {c["concept_id"]: c for c in api.get_roadmap(sid, "units_measurement")}
    check(roadmap[CONCEPT]["attempts"] == before, "no extra attempt was recorded")

    print(f"\n{'ALL' if not _failed else _failed} {_checks} CHECKS "
          f"{'PASSED' if not _failed else 'RUN — SOME FAILED'}")
    sys.exit(1 if _failed else 0)


if __name__ == "__main__":
    main()
