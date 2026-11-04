"""The end check: the pilot's "after", compared with the starting check.

No LLM calls. Proves:

  1. Parallel forms: for every in-scope interest and both classes, the two
     forms of every starting-check concept come from different interests,
     never the student's own, and the end check pairs every concept with a
     question the student hasn't seen in either check. Students split between
     the two forms.
  2. Who gets it: self-signup students never; a class student only once the
     teacher opens it, and only after the starting check. Submitting before
     that is refused and stores nothing.
  3. The browser gets questions without keys or misconceptions.
  4. Grading and comparison: right → right, mix-up → right (fixed), not sure →
     right (learned), right → wrong (slipped); studied concepts are those
     whose lesson was opened before the end check; taken once (409).
  5. The class view: before → after rates and counts, studied vs not
     studied, per concept and per student; closing keeps the answers; another
     teacher's class is not found.
  6. metrics.check_gains on hand-made rows.
  7. HTTP: student and teacher endpoints, auth, 400 / 409, and the pilot
     report carries the end check pseudonymised with the overall gains.
  8. The migration is additive: an older database gains the new columns.

Run: venv\\Scripts\\python.exe tests\\test_end_check.py
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import tempfile
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(_ROOT / "apps"))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_endcheck_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "endcheck.db")
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from ecolearn import platform_api as api  # noqa: E402
from ecolearn.content import lesson_service  # noqa: E402
from ecolearn.curriculum.scope import scope_interest_ids  # noqa: E402
from ecolearn.errors import ConflictError, EcoLearnError, NotFoundError  # noqa: E402
from ecolearn.learner import diagnostic  # noqa: E402
from ecolearn.progress import metrics, store  # noqa: E402

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


def key(concept_id: str, source: str) -> tuple[str, str]:
    """(right option, a wrong option) for this lesson's check."""
    c = lesson_service.get_authored_lesson(concept_id, source).check
    return c.answer, next(o for o in c.options if o != c.answer)


# ---------------------------------------------------------------------------
def test_forms() -> None:
    print("\n[1] parallel forms")
    config = diagnostic.load_config()
    for level, ids in config["questions"].items():
        for interest in scope_interest_ids():
            a = diagnostic.choose_questions(level, interest, 0)
            b = diagnostic.choose_questions(level, interest, 1)
            check([q["concept_id"] for q in a] == [q["concept_id"] for q in b]
                  and all(x["source_interest"] != y["source_interest"] for x, y in zip(a, b))
                  and all(q["source_interest"] != interest for q in a + b),
                  f"{level} × {interest}: two forms, same concepts, different interests, never their own")
            for form in (a, b):
                start_rows = [dict(q, correct=None) for q in form]
                end = diagnostic.choose_end_questions(interest, start_rows)
                starts = {q["concept_id"]: q["source_interest"] for q in form}
                check(len(end) == len(ids)
                      and all(q["source_interest"] not in (interest, starts[q["concept_id"]]) for q in end),
                      f"{level} × {interest}: the end check pairs all {len(ids)} with a new question")
    forms = [diagnostic.form_for(f"stu_{n:032x}") for n in range(200)]
    check(60 <= sum(forms) <= 140, f"students split between the forms ({sum(forms)} of 200 on form 1)")
    check(diagnostic.form_for("stu_x") == diagnostic.form_for("stu_x"), "a student's form is stable")


def setup() -> dict:
    rao = api.create_teacher("Ms. Rao", "rao.end", "teach-physics-1")
    sen = api.create_teacher("Mr. Sen", "sen.end", "teach-physics-2")
    made = api.create_class(rao["teacher_id"], "11-E", "Class 11", "cricket",
                            "Aarav Kumar\nMeera Iyer\nKabir Shah")
    creds = {c["name"]: c for c in made["credentials"]}
    return {"rao": rao, "sen": sen, "class_id": made["class"]["class_id"], "creds": creds}


def take_start(sid: str, plan: dict[str, str | None]) -> list[dict]:
    """Take the starting check: plan maps concept_id -> 'right' | 'wrong' | None (unsure)."""
    qs = diagnostic.choose_questions("Class 11", "cricket", diagnostic.form_for(sid))
    picks = {}
    for q in qs:
        right, wrong = key(q["concept_id"], q["source_interest"])
        want = plan.get(q["concept_id"])
        picks[q["concept_id"]] = right if want == "right" else (wrong if want == "wrong" else "unsure")
    api.submit_diagnostic(sid, picks)
    return qs


def end_picks(sid: str, plan: dict[str, str | None]) -> dict[str, str]:
    chosen = diagnostic.choose_end_questions("cricket", store.get_diagnostic_answers([sid]))
    picks = {}
    for q in chosen:
        right, wrong = key(q["concept_id"], q["source_interest"])
        want = plan.get(q["concept_id"])
        picks[q["concept_id"]] = right if want == "right" else (wrong if want == "wrong" else "unsure")
    return picks


def test_access(ctx: dict) -> None:
    print("\n[2] who gets it, and when")
    solo = api.register_student("Solo", "solo.end", "kid-password-1", "cricket", "Class 11")["student_id"]
    check(api.get_end_check(solo)["status"] == "not_open", "a self-signup student: not open")
    aarav = ctx["creds"]["Aarav Kumar"]["student_id"]
    kabir = ctx["creds"]["Kabir Shah"]["student_id"]
    check(api.get_end_check(aarav)["status"] == "not_open", "a class student before the teacher opens it")
    raises(EcoLearnError, api.submit_end_check, aarav, {})
    raises(NotFoundError, api.set_class_end_check, ctx["sen"]["teacher_id"], ctx["class_id"], True)
    out = api.set_class_end_check(ctx["rao"]["teacher_id"], ctx["class_id"], True)
    check(out["open"] and out["opened_at"], "the teacher opens it")
    check(api.get_end_check(kabir)["status"] == "needs_start", "no starting check → asked to take it first")
    raises(EcoLearnError, api.submit_end_check, kabir, {})
    check(store.get_end_check_answers([kabir]) == [], "refused submissions store nothing")


PLAN_BEFORE = {"displacement": "right", "acceleration": "wrong", "projectile_motion": None,
               "second_law": "right", "third_law": "wrong"}
PLAN_AFTER = {"displacement": "right", "acceleration": "right", "projectile_motion": "right",
              "second_law": "wrong", "third_law": "wrong"}


def test_take(ctx: dict) -> str:
    print("\n[3-4] questions, grading and the comparison")
    aarav = ctx["creds"]["Aarav Kumar"]["student_id"]
    start = take_start(aarav, PLAN_BEFORE)
    # Aarav studies acceleration (the mix-up he fixes) before the end check.
    api.start_lesson_view(aarav, "acceleration")
    got = api.get_end_check(aarav)
    check(got["status"] == "open" and len(got["questions"]) == len(start), "open: all the questions")
    text = json.dumps(got["questions"])
    end_q = diagnostic.choose_end_questions("cricket", store.get_diagnostic_answers([aarav]))
    c = lesson_service.get_authored_lesson(end_q[0]["concept_id"], end_q[0]["source_interest"]).check
    check(all(set(q) == {"concept_id", "concept_name", "chapter_name", "question", "options"}
              for q in got["questions"])
          and all(m.strip()[:30] not in text for m in c.misconceptions.values())
          and c.explanation.strip()[:30] not in text,
          "the browser gets question and options only")
    start_q = {q["concept_id"]: q["question"] for q in diagnostic.present(start)}
    check(all(q["question"] != start_q[q["concept_id"]] for q in got["questions"]),
          "every end question differs from the one asked at the start")

    raises(EcoLearnError, api.submit_end_check, aarav, {"ohms_law": "A"})
    out = api.submit_end_check(aarav, end_picks(aarav, PLAN_AFTER))
    comp = out["comparison"]
    check(out["status"] == "taken" and comp["paired"] == len(start), "taken: every concept paired")
    check(comp["before"] == {"right": 2, "mix_up": 2, "unsure": len(start) - 4}
          and comp["after"] == {"right": 3, "mix_up": 2, "unsure": len(start) - 5},
          "before and after tallies")
    check((comp["fixed"], comp["learned"], comp["slipped"]) == (1, 1, 1),
          "one mix-up fixed, one 'not sure' learned, one slipped")
    by = {c["concept_id"]: c for c in comp["concepts"]}
    check(by["acceleration"]["studied"] and not by["third_law"]["studied"],
          "studied = lesson opened before the end check")
    check(by["acceleration"]["concept_name"] == "Acceleration", "concept names for the page")
    api.start_lesson_view(aarav, "third_law")
    later = {c["concept_id"]: c for c in api.get_end_check(aarav)["comparison"]["concepts"]}
    check(not later["third_law"]["studied"], "a lesson opened after the end check doesn't count")
    raises(ConflictError, api.submit_end_check, aarav, {})
    check(api.get_learning_plan(aarav)["check"]["known"] == 2,
          "the starting check (the baseline) is unchanged")
    return aarav


def test_class_view(ctx: dict) -> None:
    print("\n[5] the class view")
    meera = ctx["creds"]["Meera Iyer"]["student_id"]
    take_start(meera, {"displacement": "wrong", "acceleration": "wrong"})
    view = api.get_class_checks(ctx["rao"]["teacher_id"], ctx["class_id"])
    s = view["summary"]
    check(s["students_started"] == 2 and s["students_finished"] == 1, "2 started, 1 finished")
    check(s["paired_answers"] == 8 and s["right_before"] == 0.25 and s["right_after"] == 0.375,
          "right answers 25% → 37.5% over paired answers only")
    check((s["fixed"], s["learned"], s["slipped"]) == (1, 1, 1), "fixed / learned / slipped totals")
    check(s["studied"] == {"pairs": 1, "right_before": 0.0, "right_after": 1.0}
          and s["not_studied"]["pairs"] == 7, "studied vs not studied")
    top = s["concepts"][0]
    check(top["concept_id"] in ("acceleration", "projectile_motion") and top["right_after"] == 1.0,
          "concepts: biggest gain first")
    rows = {r["name"]: r for r in view["students"]}
    check(rows["Aarav Kumar"]["finished"] and rows["Aarav Kumar"]["fixed"] == 1,
          "Aarav: finished, 1 fixed")
    check(rows["Meera Iyer"]["started"] and not rows["Meera Iyer"]["finished"]
          and rows["Meera Iyer"]["before"]["mix_up"] == 2 and rows["Meera Iyer"]["after"] is None,
          "Meera: her starting check only")
    check(not rows["Kabir Shah"]["started"] and rows["Kabir Shah"]["before"] is None, "Kabir: nothing yet")
    raises(NotFoundError, api.get_class_checks, ctx["sen"]["teacher_id"], ctx["class_id"])

    closed = api.set_class_end_check(ctx["rao"]["teacher_id"], ctx["class_id"], False)
    check(not closed["open"] and closed["summary"]["students_finished"] == 1, "closing keeps the answers")
    check(api.get_end_check(meera)["status"] == "not_open", "closed: Meera can't take it now")
    aarav = ctx["creds"]["Aarav Kumar"]["student_id"]
    check(api.get_end_check(aarav)["status"] == "taken", "but Aarav still sees his result")
    api.set_class_end_check(ctx["rao"]["teacher_id"], ctx["class_id"], True)


def test_metrics() -> None:
    print("\n[6] metrics.check_gains")
    comps = {
        "s1": {"fixed": 1, "learned": 0, "slipped": 0, "concepts": [
            {"concept_id": "x", "before": "mix_up", "after": "right", "studied": True},
            {"concept_id": "y", "before": "unsure", "after": "unsure", "studied": False}]},
        "s2": {"fixed": 0, "learned": 1, "slipped": 1, "concepts": [
            {"concept_id": "x", "before": "unsure", "after": "right", "studied": True},
            {"concept_id": "y", "before": "right", "after": "mix_up", "studied": False}]},
    }
    g = metrics.check_gains(comps, 3, lambda cid: {"name": cid.upper()})
    check(g["students_started"] == 3 and g["students_finished"] == 2 and g["paired_answers"] == 4,
          "counts")
    check(g["right_before"] == 0.25 and g["right_after"] == 0.5, "rates over paired answers")
    check(g["studied"] == {"pairs": 2, "right_before": 0.0, "right_after": 1.0}
          and g["not_studied"] == {"pairs": 2, "right_before": 0.5, "right_after": 0.0},
          "studied vs not studied split")
    check([c["concept_id"] for c in g["concepts"]] == ["x", "y"] and g["concepts"][0]["fixed"] == 1,
          "per concept, biggest gain first")
    empty = metrics.check_gains({}, 0, lambda cid: {})
    check(empty["right_before"] is None and empty["concepts"] == [], "no data: None, not a crash")


def test_http(ctx: dict) -> None:
    print("\n[7] HTTP and the pilot report")
    check(TestClient(app).get("/api/end-check").status_code == 401, "needs a student session")
    meera = ctx["creds"]["Meera Iyer"]
    student = TestClient(app)
    student.post("/api/auth/login", json={"username": meera["username"], "password": meera["password"]})
    r = student.get("/api/end-check")
    check(r.status_code == 200 and r.json()["status"] == "open", "GET → open")
    check(student.post("/api/end-check", json={"answers": {"x": "A"}}).status_code == 400,
          "an unknown concept → 400")
    r = student.post("/api/end-check", json={"answers": end_picks(meera["student_id"], {"displacement": "right"})})
    check(r.status_code == 200 and r.json()["comparison"]["fixed"] == 1, "POST → the comparison")
    check(student.post("/api/end-check", json={"answers": {}}).status_code == 409, "second go → 409")
    check(student.get(f"/api/teacher/classes/{ctx['class_id']}/checks").status_code == 401,
          "a student can't read the teacher view")

    teacher = TestClient(app)
    teacher.post("/api/teacher/login", json={"username": "rao.end", "password": "teach-physics-1"})
    r = teacher.get(f"/api/teacher/classes/{ctx['class_id']}/checks")
    check(r.status_code == 200 and r.json()["summary"]["students_finished"] == 2, "teacher view → 200")
    r = teacher.post(f"/api/teacher/classes/{ctx['class_id']}/end-check", json={"open": False})
    check(r.status_code == 200 and r.json()["open"] is False, "close over HTTP")

    report = api.pilot_report()
    names = {c["name"] for c in ctx["creds"].values()} | {c["username"] for c in ctx["creds"].values()}
    dumped = json.dumps(report["end_check"])
    check(len(report["end_check"]) == 16 and all(r["student_id"].startswith("S") for r in report["end_check"])
          and not any(n in dumped for n in names),
          "the pilot report has the end check, pseudonymised")
    check(report["check_gains"]["students_finished"] == 2, "and the overall before → after")


def test_migration() -> None:
    print("\n[8] the migration is additive")
    old = _TMP / "old.db"
    conn = sqlite3.connect(old)
    conn.execute("CREATE TABLE classes (class_id TEXT PRIMARY KEY, teacher_id TEXT NOT NULL, "
                 "name TEXT NOT NULL, level TEXT NOT NULL, created_at TEXT NOT NULL)")
    conn.execute("INSERT INTO classes VALUES ('c1', 't1', 'Old', 'Class 11', '2026-09-01')")
    conn.execute("CREATE TABLE learner_profiles (student_id TEXT PRIMARY KEY, "
                 "hobbies TEXT NOT NULL DEFAULT '[]', diagnostic_completed_at TEXT)")
    conn.execute("INSERT INTO learner_profiles VALUES ('s1', '[\"chess\"]', '2026-09-02')")
    conn.commit()
    conn.close()
    current = os.environ["ECOLEARN_PROGRESS_DB"]
    os.environ["ECOLEARN_PROGRESS_DB"] = str(old)
    try:
        klass = store.get_class("c1")
        profile = store.get_learner_profile("s1")
    finally:
        os.environ["ECOLEARN_PROGRESS_DB"] = current
    check(klass["name"] == "Old" and klass["end_check_opened_at"] is None, "old class: closed")
    check(profile["hobbies"] == ["chess"] and profile["end_check_completed_at"] is None,
          "old profile keeps its data, end check not taken")


def main() -> int:
    test_forms()
    ctx = setup()
    test_access(ctx)
    test_take(ctx)
    test_class_view(ctx)
    test_metrics()
    test_http(ctx)
    test_migration()
    print(f"\nAll {_checks} end-check checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
