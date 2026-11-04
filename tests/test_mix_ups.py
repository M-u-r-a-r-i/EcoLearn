"""'My mix-ups' and 'How sure are you?' (2026-10-02).

No LLM calls. Proves:

  1. mix_up_history: a wrong answer with a misconception opens a mix-up; right
     on a DIFFERENT question fixes it; right only on the same question (after
     the explanation) is "recheck"; "not sure" changes nothing; a mix-up that
     comes back is active again and counted twice; a wrong answer without a
     misconception text isn't listed; `sure` comes from the latest wrong one.
  2. Confidence validation: sure | think | guess or nothing; kept for a picked
     option, dropped for "not sure"; refused for a concept not asked.
  3. Lesson checks store confidence and say something when it matters (sure
     and wrong, guessed and right); a bad level is refused and stores nothing;
     no confidence still works (Streamlit, older clients).
  4. The starting and end checks store confidence.
  5. get_mix_ups: summary, order (active, recheck, fixed newest first), names,
     the second-person note, and a lesson link flag.
  6. Class insights: per-misconception "sure" counts, first-try accuracy by
     confidence, and "sure but wrong".
  7. HTTP: GET /api/mix-ups needs a session; a bad confidence is a 400.
  8. The migration adds `confidence` to an older answers table.

Run: venv\\Scripts\\python.exe tests\\test_mix_ups.py
"""

from __future__ import annotations

import os
import sqlite3
import sys
import tempfile
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_mixups_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "mixups.db")
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from src import platform_api as api  # noqa: E402
from src.content import lesson_service  # noqa: E402
from src.errors import EcoLearnError  # noqa: E402
from src.learner import diagnostic, plan  # noqa: E402
from src.progress import store  # noqa: E402

_checks = 0
_n = 0


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


def new_student(interest: str = "cricket", level: str = "Class 11") -> str:
    global _n
    _n += 1
    return api.register_student(f"Kid {_n}", f"mix.{_n}", "kid-password-1", interest, level)["student_id"]


def key(concept_id: str, interest: str) -> tuple[str, str]:
    c = lesson_service.get_authored_lesson(concept_id, interest).check
    return c.answer, next(o for o in c.options if o != c.answer)


def row(concept_id: str, interest: str, correct: bool | None, at: str,
        text: str | None = "Thinks X. Not so.", confidence: str | None = None,
        field: str = "source_interest") -> dict:
    return {"concept_id": concept_id, field: interest, "correct": correct, "answered_at": at,
            "misconception": None if correct else text, "confidence": confidence}


def lesson(concept_id: str, interest: str, correct: bool, at: str, **kw) -> dict:
    return row(concept_id, interest, correct, at, field="interest", **kw)


# ---------------------------------------------------------------------------
def test_history() -> None:
    print("\n[1] mix_up_history")
    h = plan.mix_up_history(
        [row("a", "football", False, "t1"), row("b", "football", None, "t1"),
         row("e", "football", False, "t1", text=None)],
        [lesson("a", "cricket", True, "t2"),
         lesson("c", "cricket", False, "t3", confidence="sure"), lesson("c", "cricket", True, "t4"),
         lesson("d", "cricket", False, "t3"), lesson("d", "cricket", True, "t4"),
         lesson("f", "cricket", False, "t2", confidence="guess"),
         lesson("g", "cricket", False, "t2"), lesson("g", "cricket", True, "t3"),
         lesson("g", "cricket", False, "t6", confidence="sure")],
        [row("d", "gaming", True, "t5"), row("f", "gaming", None, "t5")],
    )
    check(h["a"]["status"] == "fixed" and h["a"]["found_in"] == "start" and h["a"]["fixed_in"] == "lesson",
          "start wrong → right in the lesson (another question): fixed")
    check(h["c"]["status"] == "recheck" and h["c"]["sure"],
          "wrong then right on the SAME question: recheck, and it was a sure one")
    check(h["d"]["status"] == "fixed" and h["d"]["fixed_in"] == "end",
          "recheck → right in the end check (another question): fixed")
    check(h["f"]["status"] == "active" and not h["f"]["sure"], "wrong, then 'not sure': still active")
    check(h["g"]["status"] == "active" and h["g"]["times"] == 2 and h["g"]["sure"]
          and h["g"]["fixed_at"] is None,
          "came back after a right answer: active again, counted twice, latest confidence")
    check("b" not in h and "e" not in h, "'not sure' and a wrong answer with no misconception: not listed")
    check(h["a"]["text"] == "Thinks X. Not so." and h["a"]["times"] == 1, "text and count kept")


def test_confidence_validation() -> None:
    print("\n[2] confidence validation")
    check(diagnostic.clean_confidence(" Sure ") == "sure" and diagnostic.clean_confidence(None) is None
          and diagnostic.clean_confidence("") is None, "levels normalised; empty means not given")
    raises(EcoLearnError, diagnostic.clean_confidence, "maybe")
    chosen = diagnostic.choose_questions("Class 11", "cricket", 0)
    a, b = chosen[0], chosen[1]
    right, _ = key(a["concept_id"], a["source_interest"])
    graded = {g["concept_id"]: g for g in diagnostic.grade_chosen(
        chosen, {a["concept_id"]: right, b["concept_id"]: "unsure"},
        {a["concept_id"]: "think", b["concept_id"]: "sure"})}
    check(graded[a["concept_id"]]["confidence"] == "think", "kept for a picked option")
    check(graded[b["concept_id"]]["confidence"] is None, "dropped for 'not sure'")
    raises(EcoLearnError, diagnostic.grade_chosen, chosen, {}, {"ohms_law": "sure"})
    raises(EcoLearnError, diagnostic.grade_chosen, chosen, {a["concept_id"]: right},
           {a["concept_id"]: "very"})


def test_lesson_checks() -> str:
    print("\n[3] lesson checks")
    sid = new_student()
    right, wrong = key("acceleration", "cricket")
    raises(EcoLearnError, api.submit_assessment, sid, "acceleration", wrong, "certain")
    check(store.get_activity([sid])["answers"] == [], "a bad confidence stores nothing")
    out = api.submit_assessment(sid, "acceleration", wrong, "sure")
    check(out["confidence"] == "sure" and "You were sure" in out["feedback"],
          "sure and wrong: stored, and the feedback says why it matters")
    out = api.submit_assessment(sid, "acceleration", right, "guess")
    check("You guessed right" in out["feedback"], "guessed and right: a nudge to read the explanation")
    out = api.submit_assessment(sid, "displacement", key("displacement", "cricket")[0])
    check(out["correct"] and out["confidence"] is None
          and "You were sure" not in out["feedback"] and "You guessed" not in out["feedback"],
          "no confidence still works, with no confidence note")
    rows = store.get_activity([sid])["answers"]
    check([r["confidence"] for r in rows] == ["sure", "guess", None], "stored per answer")
    return sid


def test_checks_store_confidence() -> None:
    print("\n[4] starting and end checks")
    teacher = api.create_teacher("Ms. Rao", "rao.mix", "teach-physics-1")
    made = api.create_class(teacher["teacher_id"], "11-M", "Class 11", "cricket", "Asha Rao")
    sid = made["credentials"][0]["student_id"]
    chosen = diagnostic.choose_questions("Class 11", "cricket", diagnostic.form_for(sid))
    first = chosen[0]
    _, wrong = key(first["concept_id"], first["source_interest"])
    api.submit_diagnostic(sid, {first["concept_id"]: wrong}, [], {first["concept_id"]: "sure"})
    start = {r["concept_id"]: r for r in store.get_diagnostic_answers([sid])}
    check(start[first["concept_id"]]["confidence"] == "sure", "the starting check stores it")
    api.set_class_end_check(teacher["teacher_id"], made["class"]["class_id"], True)
    end_q = diagnostic.choose_end_questions("cricket", store.get_diagnostic_answers([sid]))[0]
    r, _ = key(end_q["concept_id"], end_q["source_interest"])
    api.submit_end_check(sid, {end_q["concept_id"]: r}, {end_q["concept_id"]: "think"})
    end = {x["concept_id"]: x for x in store.get_end_check_answers([sid])}
    check(end[end_q["concept_id"]]["confidence"] == "think", "the end check stores it")
    mix = api.get_mix_ups(sid)
    item = next(i for i in mix["items"] if i["concept_id"] == first["concept_id"])
    check(item["sure"] and item["found_in"] == "start", "a sure mix-up from the starting check")


def test_get_mix_ups(sid: str) -> None:
    print("\n[5] get_mix_ups")
    # acceleration: wrong (sure) then right on the same question → recheck.
    # velocity: wrong → active. position: wrong, then right in another interest's lesson → fixed.
    api.submit_assessment(sid, "velocity", key("velocity", "cricket")[1])
    api.submit_assessment(sid, "position", key("position", "cricket")[1])
    api.update_student_profile(sid, interest="football")
    api.submit_assessment(sid, "position", key("position", "football")[0])
    api.update_student_profile(sid, interest="cricket")
    mix = api.get_mix_ups(sid)
    check(mix["summary"] == {"active": 1, "recheck": 1, "fixed": 1}, "summary counts")
    check([i["concept_id"] for i in mix["items"]] == ["velocity", "acceleration", "position"],
          "order: active, recheck, fixed")
    acc = mix["items"][1]
    check(acc["concept_name"] == "Acceleration" and acc["chapter_name"] and acc["has_lesson"]
          and acc["note"].startswith(("You might", "A mix-up to watch for")) and acc["sure"],
          "names, the second-person note, the lesson flag and 'sure'")
    check(set(acc) == {"concept_id", "concept_name", "chapter_id", "chapter_name", "note", "status",
                       "sure", "times", "found_in", "found_at", "fixed_in", "fixed_at", "has_lesson"},
          "exactly the documented fields")
    check(api.get_mix_ups(new_student())["items"] == [], "a new student has none")


def test_insights(sid: str) -> None:
    print("\n[6] class insights")
    students = [{"student_id": "s1", "name": "A"}, {"student_id": "s2", "name": "B"}]

    def ans(student, letter, correct, confidence, attempt=1):
        return {"student_id": student, "concept_id": "c", "interest": "cricket", "selected": letter,
                "correct": correct, "attempt_no": attempt, "misconception": None if correct else "Thinks Y.",
                "answered_at": "t", "confidence": confidence}

    activity = {"views": [], "ratings": [], "answers": [
        ans("s1", "B", False, "sure"), ans("s2", "B", False, "guess"),
        ans("s1", "A", True, "sure", attempt=2), ans("s2", "A", True, None, attempt=2)]}
    from src.progress import metrics
    out = metrics.class_insights(students, activity, lambda c: {"name": c}, lambda c, i: None)
    m = out["misconceptions"][0]
    check(m["students"] == 2 and m["sure"] == 1, "a misconception: 2 students, 1 of them sure")
    by = out["summary"]["by_confidence"]
    check(by["sure"] == {"answers": 1, "accuracy": 0.0} and by["guess"] == {"answers": 1, "accuracy": 0.0}
          and by["think"] == {"answers": 0, "accuracy": None},
          "first-try accuracy by confidence (retries don't count)")
    check(out["summary"]["sure_but_wrong"] == 1, "sure but wrong")


def test_http() -> None:
    print("\n[7] HTTP")
    check(TestClient(app).get("/api/mix-ups").status_code == 401, "needs a student session")
    sid = new_student()
    client = TestClient(app)
    client.post("/api/auth/login", json={"username": f"mix.{_n}", "password": "kid-password-1"})
    _, wrong = key("acceleration", "cricket")
    r = client.post("/api/assessment", json={"concept_id": "acceleration", "answer": wrong,
                                             "confidence": "maybe"})
    check(r.status_code == 400, "a bad confidence → 400")
    r = client.post("/api/assessment", json={"concept_id": "acceleration", "answer": wrong,
                                             "confidence": "sure"})
    check(r.status_code == 200 and r.json()["confidence"] == "sure", "confidence over HTTP")
    r = client.get("/api/mix-ups")
    check(r.status_code == 200 and r.json()["summary"]["active"] == 1, "GET /api/mix-ups")
    check(store.get_activity([sid])["answers"][0]["confidence"] == "sure", "stored for the right student")


def test_migration() -> None:
    print("\n[8] the migration is additive")
    old = _TMP / "old.db"
    conn = sqlite3.connect(old)
    conn.execute("CREATE TABLE answers (answer_id INTEGER PRIMARY KEY AUTOINCREMENT, student_id TEXT NOT NULL, "
                 "concept_id TEXT NOT NULL, interest TEXT NOT NULL, selected TEXT NOT NULL, "
                 "correct INTEGER NOT NULL, attempt_no INTEGER NOT NULL, misconception TEXT, "
                 "answered_at TEXT NOT NULL)")
    conn.execute("INSERT INTO answers (student_id, concept_id, interest, selected, correct, attempt_no, "
                 "misconception, answered_at) VALUES ('s1', 'c', 'cricket', 'B', 0, 1, 'Thinks Z.', 't')")
    conn.commit()
    conn.close()
    current = os.environ["ECOLEARN_PROGRESS_DB"]
    os.environ["ECOLEARN_PROGRESS_DB"] = str(old)
    try:
        rows = store.get_activity(["s1"])["answers"]
    finally:
        os.environ["ECOLEARN_PROGRESS_DB"] = current
    check(len(rows) == 1 and rows[0]["confidence"] is None and rows[0]["misconception"] == "Thinks Z.",
          "an old answer keeps its data, confidence empty")


def main() -> int:
    test_history()
    test_confidence_validation()
    sid = test_lesson_checks()
    test_checks_store_confidence()
    test_get_mix_ups(sid)
    test_insights(sid)
    test_http()
    test_migration()
    print(f"\nAll {_checks} mix-up and confidence checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
