"""Concepts open in order, chapters stay open, and only a teacher sets the class (2026-10-03).

No LLM calls. Proves:

  1. A fresh student: the first written concept of a chapter is open, the rest
     are locked with "Finish X first."; opening a locked one is refused.
  2. Right once ("cleared") opens the next one, and the row says partial: the
     roadmap's "Done" tick. Wrong doesn't open it.
  3. The starting check counts: a concept it says they know is passed, so the
     one after it is open (strong students aren't held back). A concept with a
     mix-up from the check is open (the plan sends them there).
  4. A student only opens their own class's chapters; the roadmap of another
     class's chapter is refused.
  5. Only a teacher moves a student between Class 11 and Class 12: through the
     boundary and over HTTP; a student can't, another teacher can't, and a
     bad level is refused. After the move the new class's chapters open.

Run: venv\\Scripts\\python.exe tests\\test_concept_locks.py
"""

from __future__ import annotations

import os
import sys
import tempfile
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(_ROOT / "apps"))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_locks_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "locks.db")
os.environ["LLM_MODEL"] = ""
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from ecolearn import platform_api as api  # noqa: E402
from ecolearn.content import lesson_service  # noqa: E402
from ecolearn.errors import EcoLearnError, NotFoundError  # noqa: E402
from ecolearn.path import engine  # noqa: E402
from ecolearn.progress import store  # noqa: E402

CHAPTER = "laws_of_motion"
CLASS_12_CHAPTER = "current_electricity"
INTEREST = "cricket"
_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


def raises(exc_type, fn, *args, **kwargs) -> Exception:
    try:
        fn(*args, **kwargs)
    except exc_type as exc:
        return exc
    raise AssertionError(f"FAIL: expected {exc_type.__name__} from {fn.__name__}")


def rows_of(student_id: str) -> dict[str, dict]:
    return {r["concept_id"]: r for r in api.get_roadmap(student_id, CHAPTER)}


def answer(student_id: str, concept_id: str, right: bool) -> None:
    authored = lesson_service.get_authored_lesson(concept_id, INTEREST)
    letter = authored.check.answer if right else next(
        o for o in authored.check.options if o != authored.check.answer)
    api._grade_multiple_choice(student_id, concept_id, letter, authored, INTEREST)


def new_student(name: str, username: str) -> str:
    return api.register_student(name, username, "kid-password-1", INTEREST, "Class 11")["student_id"]


def main() -> None:
    written = [c for c in engine.get_roadmap("nobody", CHAPTER)
               if lesson_service.has_lesson(c["concept_id"], INTEREST)]
    ids = [c["concept_id"] for c in written]
    assert len(ids) >= 4, "this test needs a chapter with four written concepts"
    first, second, third, fourth = ids[:4]

    print("\n[1] a fresh student")
    sid = new_student("Lock Kid", "lock.kid")
    rows = rows_of(sid)
    check(not rows[first]["locked"], f"{first} (first) is open")
    check(rows[second]["locked"] and rows[third]["locked"], "the next two are locked")
    check(rows[second]["locked_reason"].startswith("Finish ")
          and rows[second]["locked_reason"].endswith(" first."), rows[second]["locked_reason"])
    check(first in rows[third]["locked_reason"] or rows[second]["name"] in rows[third]["locked_reason"],
          "the reason names the concept just before")
    raises(EcoLearnError, api.get_next_lesson, sid, CHAPTER, concept_id=second)
    check(api.get_next_lesson(sid, CHAPTER, concept_id=first)["lesson"] is not None, "the open one opens")
    check(api.get_next_lesson(sid, CHAPTER)["concept_id"] == first, "Continue opens the first")

    print("\n[2] right once opens the next; wrong doesn't")
    answer(sid, first, right=False)
    check(rows_of(sid)[second]["locked"], "a wrong answer leaves the next one locked")
    answer(sid, first, right=True)
    rows = rows_of(sid)
    check(rows[first]["progress_status"] == "partial" and rows[first]["status"] == "available",
          "right once = cleared (partial): the roadmap's Done tick")
    check(not rows[second]["locked"] and rows[third]["locked"], "exactly one more opens")
    check(api.get_next_lesson(sid, CHAPTER)["concept_id"] == second, "Continue moves on")

    print("\n[3] the starting check counts")
    sid2 = new_student("Known Kid", "known.kid")
    own = lambda cid: lesson_service.get_authored_lesson(cid, "football")  # noqa: E731
    store.save_diagnostic(sid2, [], [
        {"concept_id": second, "source_interest": "football", "selected": own(second).check.answer,
         "correct": True},
        {"concept_id": fourth, "source_interest": "football", "selected": "A", "correct": False,
         "misconception": "Thinks something wrong."},
    ])
    rows = rows_of(sid2)
    check(not rows[second]["locked"], "a concept the check says they know is open")
    check(not rows[third]["locked"], "and so is the one after it (known counts as passed)")
    check(not rows[fourth]["locked"], "a concept with a mix-up from the check is open")

    print("\n[4] a student's own class only")
    err = raises(EcoLearnError, api.get_roadmap, sid, CLASS_12_CHAPTER)
    check("Class 12" in str(err) and "teacher" in str(err), str(err))
    raises(EcoLearnError, api.get_next_lesson, sid, CLASS_12_CHAPTER)

    print("\n[5] only a teacher sets the class")
    teacher = api.create_teacher("Ms. Lock", "lock.teacher", "teacher-password-1")
    other = api.create_teacher("Mr. Other", "other.teacher", "teacher-password-1")
    made = api.create_class(teacher["teacher_id"], "11-A", "Class 11", INTEREST, "Mia Roy")
    mia = made["credentials"][0]["student_id"]
    out = api.set_student_level(teacher["teacher_id"], mia, "Class 12")
    check(out["level"] == "Class 12" and store.get_student(mia)["level"] == "Class 12", "teacher moves a student")
    check(len(api.get_roadmap(mia, CLASS_12_CHAPTER)) > 0, "the new class's chapters open")
    raises(EcoLearnError, api.get_roadmap, mia, CHAPTER)
    raises(EcoLearnError, api.set_student_level, teacher["teacher_id"], mia, "Class 13")
    raises(NotFoundError, api.set_student_level, other["teacher_id"], mia, "Class 11")
    raises(NotFoundError, api.set_student_level, teacher["teacher_id"], sid, "Class 12")  # not in a class

    student_http = TestClient(app)
    r = student_http.post("/api/auth/login", json={"username": "lock.kid", "password": "kid-password-1"})
    check(r.status_code == 200, "student logs in")
    r = student_http.patch("/api/profile", json={"level": "Class 12"})
    check(r.status_code == 403, f"a student changing their own class → 403 (got {r.status_code})")
    check(store.get_student(sid)["level"] == "Class 11", "and it didn't change")
    r = student_http.patch("/api/profile", json={"name": "Lock Kid 2", "level": "Class 11"})
    check(r.status_code == 200 and r.json()["name"] == "Lock Kid 2",
          "re-sending the same class with a name change is fine")
    check(student_http.post(f"/api/teacher/students/{mia}/level", json={"level": "Class 11"}).status_code == 401,
          "a student session can't use the teacher endpoint")

    teacher_http = TestClient(app)
    r = teacher_http.post("/api/teacher/login",
                          json={"username": "lock.teacher", "password": "teacher-password-1"})
    check(r.status_code == 200, "teacher logs in")
    r = teacher_http.post(f"/api/teacher/students/{mia}/level", json={"level": "Class 11"})
    check(r.status_code == 200 and r.json()["level"] == "Class 11", "teacher moves a student back over HTTP")
    check(teacher_http.post(f"/api/teacher/students/{mia}/level", json={"level": "x"}).status_code == 400,
          "a bad level → 400")

    print(f"\nAll {_checks} concept-lock checks passed.")


if __name__ == "__main__":
    main()
