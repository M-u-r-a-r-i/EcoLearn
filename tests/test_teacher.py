"""Teacher tools: accounts, classes from a roster, password resets. No LLM calls.

Proves the rules the pilot depends on, at the boundary and over HTTP:

  1. Teacher accounts: created server-side only; usernames are one namespace
     shared with students (neither can take the other's).
  2. Teacher login: right password works, anything else gets the one generic
     401; a student's credentials don't log in as a teacher, and vice versa.
  3. Create a class from pasted names: blank lines skipped, "Name, interest"
     honoured, clashing names get unique usernames, every generated password
     logs that student in, no hash ever leaves the boundary.
  4. A bad roster (unknown interest, too many names) is rejected with the line
     number and writes NOTHING — not even an empty class.
  5. A class view shows each student's progress summary.
  6. Ownership: another teacher's class or student answers NotFound — for
     viewing, adding students and resetting passwords alike. Self-registered
     students can't be reset by any teacher.
  7. Reset: the new password works and the old one stops working.
  8. HTTP: the two roles can't reach each other's endpoints; /api/auth/session
     reports the role; responses carrying passwords are Cache-Control: no-store.
  9. A 45-student class is created in a few seconds (bcrypt hashes in parallel).

Run: venv\\Scripts\\python.exe tests\\test_teacher.py
"""

from __future__ import annotations

import os
import sys
import tempfile
import time
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_TMP_DIR = Path(tempfile.mkdtemp(prefix="ecolearn_teacher_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP_DIR / "teacher.db")
warnings.simplefilter("ignore")  # the dev-secret warning and a TestClient notice

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from src import platform_api as api  # noqa: E402
from src.errors import AuthError, ConflictError, EcoLearnError, NotFoundError  # noqa: E402
from src.progress import store  # noqa: E402

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


ROSTER = """Aarav Kumar
Aarav Khanna

José Álvarez, cricket
Li
"""


def test_teacher_accounts() -> tuple[dict, dict]:
    print("\n[1] teacher accounts and the shared username namespace")
    rao = api.create_teacher("Ms. Rao", "Rao.Physics", "teach-physics-1")
    check(rao["username"] == "rao.physics" and rao["teacher_id"].startswith("tch_"),
          "teacher created, username normalised, id is tch_…")
    check("password_hash" not in rao, "no hash in the returned profile")
    raises(ConflictError, api.create_teacher, "Someone", "rao.physics", "another-pass-1")
    check(True, "duplicate teacher username → ConflictError")

    raises(ConflictError, api.register_student,
           name="Kid", username="rao.physics", password="kidpassword1", interest="football")
    check(True, "a student can't register a teacher's username")

    api.register_student(name="Self Signup", username="self.signup",
                         password="selfsignup1", interest="gaming")
    raises(ConflictError, api.create_teacher, "Mr. X", "self.signup", "teacher-pass-1")
    check(True, "a teacher can't take a student's username")

    raises(EcoLearnError, api.create_teacher, "Short", "short.pw", "abc")
    check(True, "short teacher password rejected")

    mehta = api.create_teacher("Mr. Mehta", "mehta", "mehta-pass-123")
    return rao, mehta


def test_teacher_login(rao: dict) -> None:
    print("\n[2] teacher login")
    profile = api.authenticate_teacher("RAO.physics", "teach-physics-1")
    check(profile["teacher_id"] == rao["teacher_id"] and "password_hash" not in profile,
          "right password logs in (case-insensitive username), no hash")
    wrong = raises(AuthError, api.authenticate_teacher, "rao.physics", "nope-nope-nope")
    unknown = raises(AuthError, api.authenticate_teacher, "nobody.here", "nope-nope-nope")
    check(str(wrong) == str(unknown), "wrong password and unknown user: one identical message")
    raises(AuthError, api.authenticate_teacher, "self.signup", "selfsignup1")
    check(True, "a student's credentials don't log in as a teacher")
    raises(AuthError, api.authenticate_student, "rao.physics", "teach-physics-1")
    check(True, "a teacher's credentials don't log in as a student")


def test_create_class(rao: dict) -> dict:
    print("\n[3] create a class from a roster")
    result = api.create_class(rao["teacher_id"], "11-B Physics", "Class 11", "football", ROSTER)
    klass, creds = result["class"], result["credentials"]
    check(klass["name"] == "11-B Physics" and klass["student_count"] == 4,
          "class created with 4 students (blank line skipped)")
    by_name = {c["name"]: c for c in creds}
    check(by_name["Aarav Kumar"]["username"] == "aarav.k", "Aarav Kumar → aarav.k")
    check(by_name["Aarav Khanna"]["username"] == "aarav.k2", "a clashing name gets aarav.k2")
    check(by_name["José Álvarez"]["username"] == "jose.a"
          and by_name["José Álvarez"]["interest"] == "cricket",
          "accents dropped from the username; per-line interest honoured")
    check(by_name["Li"]["username"] == "li.student", "a two-letter name still makes a valid username")
    check(by_name["Aarav Kumar"]["interest"] == "football", "others get the class default interest")
    check(all("password_hash" not in c for c in creds), "no hash in the credentials")
    check(len({c["password"] for c in creds}) == 4, "every student gets a different password")

    for c in creds:
        profile = api.authenticate_student(c["username"], c["password"])
        assert profile["student_id"] == c["student_id"]
    check(True, "every generated password logs its student in")
    check(api.get_student_profile(by_name["Li"]["student_id"])["level"] == "Class 11",
          "students take the class's level")
    return result


def test_bad_rosters(rao: dict) -> None:
    print("\n[4] bad rosters are rejected and write nothing")
    before = len(api.list_teacher_classes(rao["teacher_id"]))
    exc = raises(EcoLearnError, api.create_class, rao["teacher_id"], "Typo class",
                 "Class 11", "football", "Asha Patel\nRavi Shah, crikcet\n")
    check("Line 2" in str(exc), f"unknown interest names its line: {exc}")
    raises(EcoLearnError, api.create_class, rao["teacher_id"], "Big", "Class 11",
           "football", "\n".join(f"Student {i}" for i in range(61)))
    check(True, "more than 60 names rejected")
    raises(EcoLearnError, api.create_class, rao["teacher_id"], "Empty", "Class 11",
           "football", "\n  \n")
    check(True, "an empty roster rejected")
    raises(EcoLearnError, api.create_class, rao["teacher_id"], "  ", "Class 11",
           "football", "Asha")
    check(True, "a blank class name rejected")
    check(len(api.list_teacher_classes(rao["teacher_id"])) == before,
          "no class row was left behind by any failed attempt")
    check(not store.username_exists("asha.p"), "no student row was left behind either")


def test_class_detail(rao: dict, created: dict) -> None:
    print("\n[5] class view with progress")
    aarav = next(c for c in created["credentials"] if c["username"] == "aarav.k")
    store.update_progress(aarav["student_id"], "displacement_distance", 3)
    store.update_progress(aarav["student_id"], "speed_velocity", 1)
    detail = api.get_class_detail(rao["teacher_id"], created["class"]["class_id"])
    rows = {s["username"]: s for s in detail["students"]}
    check(len(rows) == 4, "all four students listed")
    check(rows["aarav.k"]["mastered"] == 1 and rows["aarav.k"]["attempted"] == 2
          and rows["aarav.k"]["last_active"], "progress summary: 1 mastered of 2 attempted")
    check(rows["li.student"]["attempted"] == 0 and rows["li.student"]["last_active"] is None,
          "a student who hasn't started shows zero")
    check(all("password_hash" not in s for s in detail["students"]), "no hashes in the class view")
    classes = api.list_teacher_classes(rao["teacher_id"])
    check(classes[0]["student_count"] == 4, "class list carries the student count")


def test_ownership(rao: dict, mehta: dict, created: dict) -> None:
    print("\n[6] a teacher only touches their own classes")
    class_id = created["class"]["class_id"]
    student_id = created["credentials"][0]["student_id"]
    raises(NotFoundError, api.get_class_detail, mehta["teacher_id"], class_id)
    check(True, "another teacher can't view the class")
    raises(NotFoundError, api.add_students_to_class, mehta["teacher_id"], class_id,
           "Intruder", "football")
    check(True, "another teacher can't add students to it")
    raises(NotFoundError, api.reset_student_password, mehta["teacher_id"], student_id)
    check(True, "another teacher can't reset its students' passwords")
    self_id = store.get_student_by_username("self.signup")["student_id"]
    raises(NotFoundError, api.reset_student_password, rao["teacher_id"], self_id)
    check(True, "a self-registered student can't be reset by any teacher")
    raises(NotFoundError, api.get_class_detail, rao["teacher_id"], "cls_doesnotexist")
    check(True, "an unknown class id → NotFound, same as someone else's")
    raises(NotFoundError, api.list_teacher_classes, student_id)
    check(True, "a student id is not a teacher id")


def test_reset_and_add(rao: dict, created: dict) -> None:
    print("\n[7] reset a password; add a latecomer")
    cred = created["credentials"][0]
    reset = api.reset_student_password(rao["teacher_id"], cred["student_id"])
    check(reset["username"] == cred["username"] and reset["password"] != cred["password"],
          "reset returns the username and a new password")
    check(api.authenticate_student(cred["username"], reset["password"])["student_id"]
          == cred["student_id"], "the new password works")
    raises(AuthError, api.authenticate_student, cred["username"], cred["password"])
    check(True, "the old password no longer works")

    added = api.add_students_to_class(rao["teacher_id"], created["class"]["class_id"],
                                      "Aarav Kapoor", "gaming")
    check(added["credentials"][0]["username"] == "aarav.k3", "latecomer gets the next free username")
    check(added["class"]["student_count"] == 5, "class now has five students")


def test_http(rao: dict) -> None:
    print("\n[8] HTTP: roles, session, no-store")
    teacher = TestClient(app)
    r = teacher.post("/api/teacher/login",
                     json={"username": "rao.physics", "password": "teach-physics-1"})
    check(r.status_code == 200 and "password_hash" not in r.json(), "teacher login → 200")
    r = teacher.get("/api/auth/session")
    check(r.status_code == 200 and r.json()["role"] == "teacher", "/api/auth/session → teacher")
    check(teacher.get("/api/auth/me").status_code == 401, "teacher session → student /me is 401")
    check(teacher.get("/api/roadmap", params={"chapter_id": "motion_straight_line"})
          .status_code == 401, "teacher session → student roadmap is 401")

    r = teacher.post("/api/teacher/classes", json={
        "name": "12-A", "level": "Class 12", "interest": "smartphones",
        "roster": "Meera Iyer\nKabir Singh"})
    check(r.status_code == 201 and len(r.json()["credentials"]) == 2, "create class over HTTP → 201")
    check(r.headers.get("cache-control") == "no-store", "credentials response is no-store")
    class_id = r.json()["class"]["class_id"]
    meera = r.json()["credentials"][0]

    r = teacher.get(f"/api/teacher/classes/{class_id}")
    check(r.status_code == 200 and len(r.json()["students"]) == 2, "class detail over HTTP")
    r = teacher.post(f"/api/teacher/students/{meera['student_id']}/reset-password")
    check(r.status_code == 200 and r.headers.get("cache-control") == "no-store",
          "reset over HTTP → 200, no-store")
    new_password = r.json()["password"]
    check(teacher.get("/api/teacher/classes/cls_nope").status_code == 404, "unknown class → 404")
    r = teacher.post("/api/teacher/classes", json={
        "name": "Bad", "interest": "football", "roster": "Ravi, crikcet"})
    check(r.status_code == 400 and "Line 1" in r.json()["detail"], "bad roster → 400 with the line")

    student = TestClient(app)
    r = student.post("/api/auth/login",
                     json={"username": meera["username"], "password": new_password})
    check(r.status_code == 200, "student logs in with the teacher-reset password")
    check(student.get("/api/auth/session").json()["role"] == "student",
          "/api/auth/session → student")
    check(student.get("/api/teacher/classes").status_code == 401,
          "student session → teacher endpoints are 401")
    check(TestClient(app).get("/api/auth/session").status_code == 401,
          "no cookie → /api/auth/session is 401")
    check(student.post("/api/teacher/login", json={
        "username": meera["username"], "password": "whatever-123"}).status_code == 401,
        "student username on teacher login → 401")


def test_speed(rao: dict) -> None:
    print("\n[9] a full class is quick")
    roster = "\n".join(f"Pupil Number{i}" for i in range(45))
    start = time.perf_counter()
    result = api.create_class(rao["teacher_id"], "Big class", "Class 11", "cricket", roster)
    elapsed = time.perf_counter() - start
    check(len(result["credentials"]) == 45, "45 students created")
    check(len({c["username"] for c in result["credentials"]}) == 45, "45 distinct usernames")
    check(elapsed < 8, f"in {elapsed:.1f} s (bcrypt hashed in parallel)")


if __name__ == "__main__":
    rao, mehta = test_teacher_accounts()
    test_teacher_login(rao)
    created = test_create_class(rao)
    test_bad_rosters(rao)
    test_class_detail(rao, created)
    test_ownership(rao, mehta, created)
    test_reset_and_add(rao, created)
    test_http(rao)
    test_speed(rao)
    print(f"\nALL {_checks} CHECKS PASSED")
