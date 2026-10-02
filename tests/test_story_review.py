"""Reviewing personal stories: the student's report button and the teacher's view.

No LLM calls: stories are stored directly, as the story agent would store them.
Proves:

  1. Report: only fixed reasons (no free text); only a story that was shown;
     the story disappears for the student at once (they get the reviewed one)
     and is never rewritten for the same lesson.
  2. Teacher view: every story in the class with its full text, reported ones
     first with their reason; failed or no-fit attempts are only counted; a
     student outside the class never appears; another teacher gets NotFound.
  3. Hide / restore: a teacher can hide a story (the student sees the reviewed
     one) and restore one, even a reported one; the report stays on record;
     ownership is enforced, including on a self-registered student.
  4. HTTP: the right role for each endpoint; bad reasons are 400.
  5. The pilot report carries the stories, pseudonymised.

Run: venv\\Scripts\\python.exe tests\\test_story_review.py
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_review_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "review.db")
os.environ["LLM_MODEL"] = ""  # the story agent stays off: nothing is generated here
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from src import platform_api as api  # noqa: E402
from src.errors import EcoLearnError, NotFoundError  # noqa: E402
from src.learner import personal_story as ps  # noqa: E402
from src.progress import store  # noqa: E402

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


def seed_story(student_id: str, concept_id: str = "second_law", status: str = "ready") -> None:
    """Store a story exactly as the agent would, for the student's current lesson."""
    profile = store.get_student(student_id)
    source = ps.lesson_source(concept_id, profile["interest"])
    store.save_personal_story({
        "student_id": student_id, "concept_id": concept_id, "hobby": "badminton",
        "lesson_hash": source["hash"], "status": status, "model": "seeded", "attempts": 1,
        "story": f"A badminton story about {concept_id}." if status == "ready" else None,
        "analogy": "The racquet's push is the force." if status == "ready" else None,
        "limit_text": "Air drag is left out." if status == "ready" else None,
    })


def setup():
    teacher = api.create_teacher("Ms. Rao", "rao.review", "teach-physics-1")
    other = api.create_teacher("Mr. Sen", "sen.review", "teach-physics-2")
    made = api.create_class(teacher["teacher_id"], "11-D", "Class 11", "cricket",
                            "Aarav Kumar\nMeera Iyer")
    ids = {c["name"]: c["student_id"] for c in made["credentials"]}
    logins = {c["name"]: (c["username"], c["password"]) for c in made["credentials"]}
    for sid in ids.values():
        store.save_diagnostic(sid, ["badminton"], [])
    return teacher, other, made["class"]["class_id"], ids, logins


def test_report(ids) -> None:
    print("\n[1] the student's report button")
    aarav = ids["Aarav Kumar"]
    seed_story(aarav)
    check(api.get_personal_story(aarav, "second_law")["status"] == "ready", "the story is showing")
    raises(EcoLearnError, api.report_personal_story, aarav, "second_law", "I hate it, my name is Aarav")
    raises(NotFoundError, api.report_personal_story, aarav, "third_law", "confusing")
    out = api.report_personal_story(aarav, "second_law", "wrong_physics")
    check(out["reported"] and out["reason"] == "wrong_physics", "a fixed reason is accepted")
    check(api.get_personal_story(aarav, "second_law")["status"] == "none",
          "hidden from the student at once: they get the reviewed story")
    lesson = api.get_next_lesson(aarav, "laws_of_motion", concept_id="second_law")
    check(lesson["lesson"]["personal_story"]["status"] == "none", "on the lesson page too")
    row = store.get_personal_story(aarav, "second_law")
    check(row["hidden"] and row["hidden_by"] == "student" and row["reported_at"],
          "stored as reported, with the time")
    check(ps._is_current(row, ps._context(aarav, "second_law")),
          "still 'current', so the same lesson never rewrites it")


def test_teacher_view(teacher, other, class_id, ids) -> None:
    print("\n[2] the teacher's view")
    meera = ids["Meera Iyer"]
    seed_story(meera, "third_law")
    seed_story(meera, "inertia_first_law", status="failed")
    outsider = api.register_student("Out Sider", "out.sider", "kid-password-1", "cricket", "Class 11")
    store.save_diagnostic(outsider["student_id"], ["badminton"], [])
    seed_story(outsider["student_id"])

    view = api.list_class_stories(teacher["teacher_id"], class_id)
    check(view["summary"] == {"written": 2, "showing": 1, "reported": 1, "hidden_by_teacher": 0,
                              "not_written": 1},
          "counts: 2 written, 1 showing, 1 reported, 1 failed attempt")
    first = view["stories"][0]
    check(first["name"] == "Aarav Kumar" and first["report_label"] == "The physics seems wrong"
          and first["hidden"], "the reported story comes first, with its reason")
    check(first["story"] and first["analogy"] and first["limit"] and first["hobby"] == "Badminton"
          and first["concept_name"] == "Newton's second law" and first["chapter_name"] == "Laws of Motion",
          "with the full text the student saw, and where it belongs")
    check(all(s["name"] != "Out Sider" for s in view["stories"]), "a student outside the class never appears")
    raises(NotFoundError, api.list_class_stories, other["teacher_id"], class_id)


def test_hide_restore(teacher, other, ids) -> dict:
    print("\n[3] hide and restore")
    meera, aarav = ids["Meera Iyer"], ids["Aarav Kumar"]
    t = teacher["teacher_id"]
    api.set_class_story_hidden(t, meera, "third_law", True)
    check(api.get_personal_story(meera, "third_law")["status"] == "none", "hidden by the teacher")
    check(store.get_personal_story(meera, "third_law")["hidden_by"] == "teacher", "recorded as the teacher's")
    api.set_class_story_hidden(t, meera, "third_law", False)
    check(api.get_personal_story(meera, "third_law")["status"] == "ready", "restored")
    api.set_class_story_hidden(t, aarav, "second_law", False)
    row = store.get_personal_story(aarav, "second_law")
    check(not row["hidden"] and row["report_reason"] == "wrong_physics" and row["reported_at"],
          "a reported story can be restored, and the report stays on record")
    raises(NotFoundError, api.set_class_story_hidden, other["teacher_id"], meera, "third_law", True)
    outsider = store.get_student_by_username("out.sider")["student_id"]
    raises(NotFoundError, api.set_class_story_hidden, t, outsider, "second_law", True)
    raises(NotFoundError, api.set_class_story_hidden, t, meera, "ohms_law", True)
    return {"meera": meera}


def test_http(class_id, logins, ids) -> None:
    print("\n[4] HTTP")
    student = TestClient(app)
    user, pw = logins["Meera Iyer"]
    student.post("/api/auth/login", json={"username": user, "password": pw})
    check(student.post("/api/personal-story/report",
                       json={"concept_id": "third_law", "reason": "rude"}).status_code == 400,
          "a made-up reason → 400")
    r = student.post("/api/personal-story/report", json={"concept_id": "third_law", "reason": "confusing"})
    check(r.status_code == 200 and r.json()["reported"], "report → 200")
    check(student.get(f"/api/teacher/classes/{class_id}/stories").status_code == 401,
          "a student can't read the teacher view")

    teacher = TestClient(app)
    teacher.post("/api/teacher/login", json={"username": "rao.review", "password": "teach-physics-1"})
    r = teacher.get(f"/api/teacher/classes/{class_id}/stories")
    check(r.status_code == 200 and r.json()["summary"]["reported"] == 2, "teacher view → 200, 2 reported")
    r = teacher.post(f"/api/teacher/stories/{ids['Meera Iyer']}/third_law/visibility", json={"hidden": False})
    check(r.status_code == 200 and r.json()["hidden"] is False, "restore over HTTP")
    check(teacher.post("/api/personal-story/report",
                       json={"concept_id": "third_law", "reason": "other"}).status_code == 401,
          "a teacher can't use the student's report button")


def test_pilot_report() -> None:
    print("\n[5] the pilot report")
    report = api.pilot_report()
    text = json.dumps(report["stories"])
    check(len(report["stories"]) == 4 and "stu_" not in text and "Aarav" not in text,
          "stories included, pseudonymised")


def main() -> None:
    teacher, other, class_id, ids, logins = setup()
    test_report(ids)
    test_teacher_view(teacher, other, class_id, ids)
    test_hide_restore(teacher, other, ids)
    test_http(class_id, logins, ids)
    test_pilot_report()
    print(f"\nAll {_checks} story-review checks passed.")


if __name__ == "__main__":
    main()
