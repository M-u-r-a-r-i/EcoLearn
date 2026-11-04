"""Pilot metrics and the misconception view. No LLM calls.

Proves:

  1. The aggregation (src/ecolearn/progress/metrics.py), on hand-made rows: first-try
     accuracy ignores retries, misconceptions count students not clicks, the
     share is out of the students who answered, bounces don't count as reading,
     and every number is split by interest.
  2. Lesson views: opening a lesson needs a real concept with a lesson; reading
     time is clamped to what is possible (time since opening, 30 min max), only
     ever goes up, and nobody can report time on someone else's view.
  3. Answers: every multiple-choice pick is logged with its attempt number and,
     when wrong, the misconception its option was written to catch.
  4. Ratings: 👍/👎 replace each other, 0 clears, anything else is refused, and
     the current rating comes back when the lesson is opened again.
  5. Class insights: the teacher sees the real numbers for their own class —
     including the question and option text behind each misconception — and
     another teacher's class answers NotFound.
  6. HTTP: the endpoints are tied to the session's role, the reading-time
     report works as text/plain (what a closing page sends), and nothing a
     student receives contains the answer key.
  7. The pilot report has no names or usernames in it.

Run: venv\\Scripts\\python.exe tests\\test_pilot_metrics.py
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import tempfile
import warnings
from datetime import datetime, timedelta, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(_ROOT / "apps"))

_TMP_DIR = Path(tempfile.mkdtemp(prefix="ecolearn_metrics_"))
_DB = _TMP_DIR / "metrics.db"
os.environ["ECOLEARN_PROGRESS_DB"] = str(_DB)
warnings.simplefilter("ignore")  # the dev-secret warning and a TestClient notice

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from ecolearn import platform_api as api  # noqa: E402
from ecolearn.content import lesson_service  # noqa: E402
from ecolearn.errors import EcoLearnError, NotFoundError  # noqa: E402
from ecolearn.progress import metrics, store  # noqa: E402

# A concept with a cricket and a football lesson (both written in phase 1).
CONCEPT = "second_law"

_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


def raises(exc_type: type[Exception], fn, *args, **kwargs) -> Exception:
    try:
        fn(*args, **kwargs)
    except exc_type as exc:
        return exc
    raise AssertionError(f"FAIL: expected {exc_type.__name__} from {fn.__name__}")


def key_for(concept_id: str, interest: str):
    """(right letter, a wrong letter, that wrong letter's misconception)."""
    check_ = lesson_service.get_authored_lesson(concept_id, interest).check
    wrong = next(letter for letter in check_.options if letter != check_.answer)
    return check_.answer, wrong, check_.misconceptions[wrong].strip()


def _age_view(view_id: str, minutes: int) -> None:
    """Pretend a view was opened `minutes` ago."""
    opened = (datetime.now(tz=timezone.utc) - timedelta(minutes=minutes)).isoformat()
    conn = sqlite3.connect(_DB)
    conn.execute("UPDATE lesson_views SET opened_at = ? WHERE view_id = ?", (opened, view_id))
    conn.commit()
    conn.close()


# ---------------------------------------------------------------------------
def test_aggregation() -> None:
    print("\n[1] aggregation on hand-made rows")
    students = [{"student_id": s} for s in ("a", "b", "c", "outsider-not-in-class")]
    students = students[:3]
    view = lambda sid, cid, secs, interest="cricket": {  # noqa: E731
        "student_id": sid, "concept_id": cid, "interest": interest, "active_seconds": secs}
    ans = lambda sid, cid, opt, ok, n, mis=None, interest="cricket": {  # noqa: E731
        "student_id": sid, "concept_id": cid, "interest": interest, "selected": opt,
        "correct": ok, "attempt_no": n, "misconception": mis}
    activity = {
        "views": [view("a", "x", 300), view("b", "x", 120), view("c", "x", 4),
                  view("c", "y", 60, "football"), view("zz", "x", 999)],
        "answers": [
            # a: wrong (B) twice, then right — one confused student, not three
            ans("a", "x", "B", False, 1, "thinks B"), ans("a", "x", "B", False, 2, "thinks B"),
            ans("a", "x", "A", True, 3),
            # b: wrong (B) then right; c: right first time
            ans("b", "x", "B", False, 1, "thinks B"), ans("b", "x", "A", True, 2),
            ans("c", "x", "A", True, 1),
            ans("c", "y", "D", False, 1, "thinks D", "football"),
            ans("zz", "x", "C", False, 1, "outsider"),
        ],
        "ratings": [{"student_id": "a", "concept_id": "x", "interest": "cricket", "rating": 1},
                    {"student_id": "b", "concept_id": "x", "interest": "cricket", "rating": -1},
                    {"student_id": "c", "concept_id": "y", "interest": "football", "rating": 1}],
    }
    names = {"x": "Concept X", "y": "Concept Y"}
    out = metrics.class_insights(
        students, activity,
        lambda cid: {"name": names[cid], "chapter_id": "ch", "chapter_name": "Chapter"},
        lambda cid, i: {"question": f"Q {cid}", "options": {"A": "a", "B": "b", "C": "c", "D": "d"},
                        "answer": "A"},
    )
    s = out["summary"]
    check(s["students"] == 3 and s["active_students"] == 3, "outsider rows are ignored")
    check(s["lessons_opened"] == 4 and s["active_minutes"] == round(484 / 60, 1),
          "opens and total minutes count every view")
    check(s["median_minutes_per_lesson"] == 2.0,
          "median reading time skips the 4-second bounce (median of 300, 120, 60 s = 2 min)")
    check(s["first_try_answers"] == 4 and s["first_try_correct"] == 1
          and s["first_try_accuracy"] == 0.25, "first-try accuracy ignores retries: 1 of 4")
    check(s["thumbs_up"] == 2 and s["thumbs_down"] == 1 and s["approval"] == 0.667,
          "👍/👎 totals and approval")

    top = out["misconceptions"][0]
    check(top["concept_id"] == "x" and top["option"] == "B" and top["students"] == 2,
          "top misconception: option B on X, by 2 students (a's three clicks count once)")
    check(top["students_answered"] == 3 and top["share"] == 0.667,
          "share is out of the 3 students who answered X")
    check(top["misconception"] == "thinks B" and top["option_text"] == "b"
          and top["correct_option"] == "A" and top["question"] == "Q x",
          "misconception carries its text, the question, and the right answer")
    check(all(m["misconception"] != "outsider" for m in out["misconceptions"]),
          "an outsider's misconception never shows up")

    hardest = out["concepts"][0]
    check(hardest["concept_id"] == "y" and hardest["first_try_accuracy"] == 0.0,
          "concepts sorted hardest first (Y: 0% first try)")
    x = next(c for c in out["concepts"] if c["concept_id"] == "x")
    check(x["first_try_accuracy"] == 0.333 and x["students_opened"] == 3
          and x["median_minutes"] == 3.5, "per-concept accuracy, opens and median reading time")

    by_interest = {i["interest"]: i for i in out["interests"]}
    check(by_interest["cricket"]["first_try_accuracy"] == 0.333
          and by_interest["football"]["first_try_accuracy"] == 0.0
          and by_interest["football"]["approval"] == 1.0, "numbers split by interest")

    a = next(r for r in out["students"] if r["student_id"] == "a")
    check(a["answered"] == 1 and a["first_try_correct"] == 0 and a["active_minutes"] == 5.0,
          "per-student row: one first try (wrong), 5 minutes")

    empty = metrics.class_insights(students, {"views": [], "answers": [], "ratings": []},
                                   lambda c: {}, lambda c, i: None)
    check(empty["summary"]["first_try_accuracy"] is None
          and empty["summary"]["median_minutes_per_lesson"] is None
          and empty["misconceptions"] == [], "an empty class gives None, not a divide-by-zero")


# ---------------------------------------------------------------------------
def test_views(cricket_id: str, football_id: str) -> None:
    print("\n[2] lesson views and reading time")
    raises(NotFoundError, api.start_lesson_view, cricket_id, "no_such_concept")
    raises(NotFoundError, api.start_lesson_view, "stu_nobody", CONCEPT)
    view = api.start_lesson_view(cricket_id, CONCEPT)
    check(view["view_id"].startswith("view_") and view["interest"] == "cricket"
          and view["rating"] == 0, "opening a lesson gives a view id, the interest, no rating yet")

    got = api.record_lesson_time(cricket_id, view["view_id"], 10_000)
    check(got["active_seconds"] <= 31,
          f"a just-opened view can't hold 10,000 s (clamped to {got['active_seconds']})")
    _age_view(view["view_id"], 120)
    got = api.record_lesson_time(cricket_id, view["view_id"], 10_000)
    check(got["active_seconds"] == 1800, "even a 2-hour-old view caps at 30 minutes")
    got = api.record_lesson_time(cricket_id, view["view_id"], 50)
    check(got["active_seconds"] == 1800, "a lower, late report never lowers the total")
    raises(NotFoundError, api.record_lesson_time, football_id, view["view_id"], 5)
    raises(NotFoundError, api.record_lesson_time, cricket_id, "view_doesnotexist", 5)
    raises(EcoLearnError, api.record_lesson_time, cricket_id, view["view_id"], "lots")
    check(store.get_lesson_view(view["view_id"])["active_seconds"] == 1800,
          "someone else's report changed nothing")


def test_answers(cricket_id: str) -> None:
    print("\n[3] every multiple-choice pick is logged")
    right, wrong, misconception = key_for(CONCEPT, "cricket")
    r1 = api.submit_assessment(cricket_id, CONCEPT, wrong)
    r2 = api.submit_assessment(cricket_id, CONCEPT, right)
    check(r1["attempt_no"] == 1 and r2["attempt_no"] == 2, "attempt numbers 1 then 2")
    rows = store.get_activity([cricket_id])["answers"]
    check(len(rows) == 2 and rows[0]["selected"] == wrong and rows[0]["correct"] is False
          and rows[0]["misconception"] == misconception and rows[0]["interest"] == "cricket",
          "the wrong pick is stored with the misconception its option was written for")
    check(rows[1]["correct"] is True and rows[1]["misconception"] is None,
          "a right pick carries no misconception")
    raises(EcoLearnError, api.submit_assessment, cricket_id, CONCEPT, "Z")
    check(len(store.get_activity([cricket_id])["answers"]) == 2, "a rubbish pick logs nothing")


def test_ratings(cricket_id: str) -> None:
    print("\n[4] 👍 / 👎")
    api.rate_lesson(cricket_id, CONCEPT, 1)
    check(api.start_lesson_view(cricket_id, CONCEPT)["rating"] == 1, "👍 saved and shown on reopen")
    api.rate_lesson(cricket_id, CONCEPT, -1)
    check(store.get_lesson_rating(cricket_id, CONCEPT, "cricket") == -1, "👎 replaces 👍")
    check(len(store.get_activity([cricket_id])["ratings"]) == 1, "still one rating row")
    api.rate_lesson(cricket_id, CONCEPT, 0)
    check(store.get_lesson_rating(cricket_id, CONCEPT, "cricket") == 0, "0 clears it")
    raises(EcoLearnError, api.rate_lesson, cricket_id, CONCEPT, 5)
    raises(NotFoundError, api.rate_lesson, cricket_id, "no_such_concept", 1)


def test_class_insights() -> dict:
    print("\n[5] class insights for the teacher")
    teacher = api.create_teacher("Ms. Rao", "rao.metrics", "teach-physics-1")
    other = api.create_teacher("Mr. Sen", "sen.metrics", "teach-physics-2")
    made = api.create_class(teacher["teacher_id"], "11-B", "Class 11", "cricket",
                            "Aarav Kumar\nMeera Iyer\nKabir Shah, football")
    ids = {c["name"]: c["student_id"] for c in made["credentials"]}
    class_id = made["class"]["class_id"]

    right, wrong, misconception = key_for(CONCEPT, "cricket")
    for name in ("Aarav Kumar", "Meera Iyer"):
        v = api.start_lesson_view(ids[name], CONCEPT)
        _age_view(v["view_id"], 10)
        api.record_lesson_time(ids[name], v["view_id"], 240)
        api.submit_assessment(ids[name], CONCEPT, wrong)
        api.submit_assessment(ids[name], CONCEPT, right)
    api.rate_lesson(ids["Aarav Kumar"], CONCEPT, 1)
    f_right, _, _ = key_for(CONCEPT, "football")
    api.start_lesson_view(ids["Kabir Shah"], CONCEPT)
    api.submit_assessment(ids["Kabir Shah"], CONCEPT, f_right)

    out = api.get_class_insights(teacher["teacher_id"], class_id)
    s = out["summary"]
    check(out["class"]["class_id"] == class_id and s["students"] == 3
          and s["active_students"] == 3, "the class and its three active students")
    check(s["lessons_opened"] == 3 and s["active_minutes"] == 8.0, "3 opens, 8 minutes read")
    check(s["first_try_answers"] == 3 and s["first_try_correct"] == 1,
          "first try: 1 of 3 right (the two retries don't count)")
    top = out["misconceptions"][0]
    check(top["students"] == 2 and top["students_answered"] == 2 and top["share"] == 1.0
          and top["misconception"] == misconception and top["interest"] == "cricket",
          "top misconception: both cricket students, with its text")
    check(bool(top["question"]) and bool(top["option_text"]) and top["correct_option"] == right,
          "the teacher sees the question, the wrong option and the right answer")
    names = [r["name"] for r in out["students"]]
    check(names == sorted(names) and all("username" in r for r in out["students"]),
          "student rows carry names and usernames, sorted by name")
    check({i["interest"] for i in out["interests"]} == {"cricket", "football"},
          "numbers split by the two interests in the class")
    check(json.dumps(out) is not None, "the whole result is JSON-serializable")
    raises(NotFoundError, api.get_class_insights, other["teacher_id"], class_id)
    return {"teacher": teacher, "class_id": class_id}


def test_http(cricket_id: str, teacher_class: dict) -> None:
    print("\n[6] HTTP")
    student = TestClient(app)
    check(student.post("/api/lesson-views", json={"concept_id": CONCEPT}).status_code == 401,
          "no session → 401")
    api.register_student("Web Kid", "web.kid", "kid-password-1", "cricket", "Class 11")
    student.post("/api/auth/login", json={"username": "web.kid", "password": "kid-password-1"})
    r = student.post("/api/lesson-views", json={"concept_id": CONCEPT})
    check(r.status_code == 201 and r.json()["view_id"].startswith("view_"), "open a lesson → 201")
    view_id = r.json()["view_id"]
    _age_view(view_id, 5)
    r = student.post(f"/api/lesson-views/{view_id}/time", content='{"active_seconds": 75}',
                     headers={"Content-Type": "text/plain;charset=UTF-8"})
    check(r.status_code == 200 and r.json()["active_seconds"] == 75,
          "reading time accepted as text/plain (what keepalive sends)")
    r = student.post(f"/api/lesson-views/{view_id}/time", content="not json",
                     headers={"Content-Type": "text/plain"})
    check(r.status_code == 400, "a garbled report → 400")
    r = student.post("/api/lesson-ratings", json={"concept_id": CONCEPT, "rating": 1})
    check(r.status_code == 200 and r.json()["rating"] == 1, "rate → 200")
    check(student.post("/api/lesson-ratings", json={"concept_id": CONCEPT, "rating": 3})
          .status_code == 400, "bad rating → 400")

    right, wrong, _ = key_for(CONCEPT, "cricket")
    texts = [student.post("/api/lesson-views", json={"concept_id": CONCEPT}).text,
             student.get("/api/next-lesson",
                         params={"chapter_id": "laws_of_motion", "concept_id": CONCEPT}).text]
    lesson = lesson_service.get_authored_lesson(CONCEPT, "cricket").check
    check(all(m.strip()[:40] not in t for t in texts for m in lesson.misconceptions.values())
          and all('"answer"' not in t for t in texts),
          "no answer key or misconception reaches the student")
    check(student.get(f"/api/teacher/classes/{teacher_class['class_id']}/insights")
          .status_code == 401, "a student can't read class insights")

    teacher = TestClient(app)
    teacher.post("/api/teacher/login", json={"username": "rao.metrics", "password": "teach-physics-1"})
    r = teacher.get(f"/api/teacher/classes/{teacher_class['class_id']}/insights")
    check(r.status_code == 200 and r.json()["summary"]["students"] == 3, "teacher insights → 200")
    check(teacher.get("/api/teacher/classes/cls_nope/insights").status_code == 404,
          "unknown class → 404")
    check(teacher.post("/api/lesson-views", json={"concept_id": CONCEPT}).status_code == 401,
          "a teacher session can't log student views")


def test_pilot_report() -> None:
    print("\n[7] the pilot report is pseudonymised")
    report = api.pilot_report()
    text = json.dumps(report)
    for secret in ("Aarav", "Meera", "Kabir", "aarav.k", "web.kid", "stu_", "cls_", "view_"):
        check(secret not in text, f"no {secret!r} in the report")
    check(all(r["student_id"].startswith("S") for r in report["answers"]),
          "rows use S001-style pseudonyms")
    check(report["insights"]["summary"]["first_try_answers"] >= 4, "the totals cover everyone")


def main() -> None:
    cricket = api.register_student("Cricket Kid", "cricket.kid", "kid-password-1", "cricket", "Class 11")
    football = api.register_student("Football Kid", "football.kid", "kid-password-1", "football",
                                    "Class 11")
    test_aggregation()
    test_views(cricket["student_id"], football["student_id"])
    test_answers(cricket["student_id"])
    test_ratings(cricket["student_id"])
    teacher_class = test_class_insights()
    test_http(cricket["student_id"], teacher_class)
    test_pilot_report()
    print(f"\nAll {_checks} pilot-metrics checks passed.")


if __name__ == "__main__":
    main()
