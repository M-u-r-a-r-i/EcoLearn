"""The coaching-note agent: a short note per student, for the teacher. No network calls.

A scripted stand-in replaces the model, so every path is deterministic.

  1. Rules notes: each situation (not started, sure-but-wrong, low accuracy, skimming,
     quiet, nervous about physics, steady) gets a note with evidence and a next step.
  2. The model path: valid notes are used ("ai"); everything the model gets wrong is
     replaced by a rules note for that student only: evidence the student doesn't have,
     labelling words, a name or username, wrong length, a missing student, non-JSON, a
     failing call. Classes are sent in batches of 8.
  3. Privacy: nothing sent to the model holds a name, username or id; stored runs hold
     aliases (S1...), and names are filled in only when a teacher views them.
  4. The boundary: reuse inside a minute, another teacher gets NotFound, GET before any
     run is null, and over HTTP a student session gets 401.

Run: venv\\Scripts\\python.exe tests\\test_coaching_agent.py
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import tempfile
import warnings
from pathlib import Path
from types import SimpleNamespace

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(_ROOT / "apps"))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_coach_"))
_DB = _TMP / "coach.db"
os.environ["ECOLEARN_PROGRESS_DB"] = str(_DB)
os.environ["LLM_MODEL"] = ""  # the AI is off unless a test passes its own chat
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from ecolearn import platform_api as api  # noqa: E402
from ecolearn.agents import coaching_agent as ca  # noqa: E402
from ecolearn.content import lesson_service  # noqa: E402
from ecolearn.errors import NotFoundError  # noqa: E402

CONCEPT = "second_law"
NAMES = ["Aarav Kumar", "Meera Iyer", "Kabir Shah", "Diya Rao", "Ishaan Das", "Zara Khan"]
_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


GOOD = {"note": "Got two of seven right first time and was sure of a wrong answer.",
        "evidence": ["first_try_right"], "next_step": "Ask them to explain the idea aloud first."}


def reply(obj) -> SimpleNamespace:
    return SimpleNamespace(text=obj if isinstance(obj, str) else json.dumps(obj), model="scripted")


def sent_cases(messages) -> dict:
    text = messages[0]["content"]
    start = text.index("CASE FILES (JSON):\n") + len("CASE FILES (JSON):\n")
    return json.loads(text[start:text.index("\n\nWrite the JSON now.")])


def echo_chat(log: list):
    """Answers every student in the request with a valid note citing a field they have."""
    def chat(messages, **kw):
        cases = sent_cases(messages)
        log.append({"aliases": list(cases), "raw": json.dumps(messages), "kw": kw})
        return reply({a: {"note": f"This student's data shows {len(c)} facts worth a look today.",
                          "evidence": [next(iter(c))], "next_step": "Check in with them briefly this week."}
                      for a, c in cases.items()})
    return chat


def test_rules() -> None:
    print("\n[1] rules notes")
    cases = {
        "not started": {"lessons_opened": 0, "checks_answered": 0},
        "sure but wrong": {"lessons_opened": 3, "checks_answered": 3, "first_try_right": "2 of 3",
                           "mix_ups": [{"concept": "Inertia", "sure": True}]},
        "low accuracy": {"lessons_opened": 4, "checks_answered": 4, "first_try_right": "1 of 4"},
        "skimmer": {"lessons_opened": 5, "checks_answered": 5, "first_try_right": "4 of 5", "skim_share": 80},
        "quiet": {"lessons_opened": 2, "checks_answered": 2, "first_try_right": "2 of 2", "days_since_active": 12},
        "nervous": {"lessons_opened": 1, "checks_answered": 1, "first_try_right": "1 of 1", "physics_feel": "dread"},
        "steady": {"lessons_opened": 4, "checks_answered": 4, "first_try_right": "4 of 4"},
    }
    notes = {k: ca.rules_note(c) for k, c in cases.items()}
    check("Hasn't opened" in notes["not started"]["note"] and "login slip" in notes["not started"]["next_step"],
          "not started: says so and suggests checking the login slip")
    check("sure of a wrong answer on Inertia" in notes["sure but wrong"]["note"],
          "sure but wrong: names the concept")
    check("1 of 4" in notes["low accuracy"]["note"], "low accuracy: states the numbers")
    check("80%" in notes["skimmer"]["note"], "skimmer: states the share")
    check("12 days" in notes["quiet"]["note"], "quiet: states the days")
    check("nervous" in notes["nervous"]["note"] and "quick win" not in notes["nervous"]["note"]
          and "question they can get right" in notes["nervous"]["next_step"],
          "nervous about physics: a gentle first step, no label")
    check("steadily" in notes["steady"]["note"], "nothing wrong: a steady note")
    for k, n in notes.items():
        check(all(e in cases[k] for e in n["evidence"]), f"{k}: evidence only cites facts the student has")
        check(not ca._LABELS.search(n["note"] + " " + n["next_step"]), f"{k}: no labelling words")


def test_model_path() -> None:
    print("\n[2] the model path and its checks")
    cases = {"S1": {"first_try_right": "2 of 7", "checks_answered": 7},
             "S2": {"lessons_opened": 0}, "S3": {"first_try_right": "5 of 5"},
             "S4": {"physics_feel": "nervous"}, "S5": {"lessons_opened": 2},
             "S6": {"days_since_active": 9}, "S7": {"lessons_opened": 1}}
    forbidden = ["Meera Iyer", "Meera", "meera.i"]

    def bad(note=None, evidence=None, step=None):
        return {"note": note or GOOD["note"], "evidence": ["first_try_right"] if evidence is None else evidence,
                "next_step": step or GOOD["next_step"]}

    def scripted(data):
        return lambda messages, **kw: reply(data)

    out = ca.coach_class({"S1": cases["S1"]}, forbidden, scripted({"S1": GOOD}), True)
    check(out["notes"]["S1"]["source"] == "ai" and out["source"] == "agent" and out["model"] == "scripted",
          "a valid note is accepted and labelled ai")

    attempts = {
        "evidence the student doesn't have": bad(evidence=["skim_share"]),
        "a labelling word": bad(note="This looks like ADHD to me, with too few checks answered so far."),
        "a student's name": bad(note="Meera got two of seven right first time and seems unsure."),
        "a username": bad(note="Perhaps meera.i got two of seven right first time and was unsure."),
        "a note that is too short": bad(note="Struggling."),
        "no evidence listed": bad(evidence=[]),
        "a link": bad(step="Send them to http://example.com for a long recap of the idea."),
    }
    for label, note in attempts.items():
        out = ca.coach_class({"S1": cases["S1"]}, forbidden, scripted({"S1": note}), True)
        check(out["notes"]["S1"]["source"] == "rules" and out["source"] == "rules",
              f"rejected → rules note: {label}")

    out = ca.coach_class({"S1": cases["S1"], "S3": cases["S3"]}, forbidden,
                         scripted({"S1": GOOD}), True)
    check(out["notes"]["S1"]["source"] == "ai" and out["notes"]["S3"]["source"] == "rules"
          and out["source"] == "mixed" and "1 of 2" in out["note"],
          "a missing student gets a rules note; the run is 'mixed' and says how many")

    out = ca.coach_class({"S1": cases["S1"]}, forbidden, scripted("Sorry, I can't do that."), True)
    check(out["source"] == "rules" and out["failed"], "a reply that isn't JSON → rules")

    def boom(messages, **kw):
        raise RuntimeError("gateway down")
    out = ca.coach_class({"S1": cases["S1"]}, forbidden, boom, True)
    check(out["source"] == "rules" and out["trail"][0]["ok"] is False and "gateway down" in out["trail"][0]["detail"],
          "a failing call → rules, and the trail says why")

    out = ca.coach_class({"S1": cases["S1"]}, forbidden, None, False)
    check(out["source"] == "rules" and "isn't configured" in out["note"], "AI off → rules, and says why")

    log: list = []
    out = ca.coach_class(cases, forbidden, echo_chat(log), True)
    check([len(c["aliases"]) for c in log] == [7] and out["source"] == "agent", "7 students → one call")
    big = {f"S{n}": {"lessons_opened": n} for n in range(1, 20)}
    log.clear()
    out = ca.coach_class(big, forbidden, echo_chat(log), True)
    check([len(c["aliases"]) for c in log] == [8, 8, 3] and len(out["notes"]) == 19,
          "19 students → batches of 8, 8 and 3")
    check(log[0]["kw"]["temperature"] <= 0.5, "a low temperature: notes should be steady, not creative")


def setup_class() -> tuple[dict, dict, str, dict]:
    teacher = api.create_teacher("Ms. Rao", "rao.coach", "teach-physics-1")
    other = api.create_teacher("Mr. Sen", "sen.coach", "teach-physics-2")
    made = api.create_class(teacher["teacher_id"], "11-B", "Class 11", "cricket", "\n".join(NAMES))
    ids = {c["name"]: c["student_id"] for c in made["credentials"]}
    usernames = [c["username"] for c in made["credentials"]]
    key = lesson_service.get_authored_lesson(CONCEPT, "cricket").check
    wrong = next(o for o in key.options if o != key.answer)
    for i, name in enumerate(NAMES):
        if name == "Zara Khan":
            continue  # never starts
        api.start_lesson_view(ids[name], CONCEPT)
        api.submit_assessment(ids[name], CONCEPT, wrong if i < 3 else key.answer)
    return teacher, other, made["class"]["class_id"], {"ids": ids, "usernames": usernames}


def test_boundary(teacher, other, class_id, info) -> None:
    print("\n[3-4] the boundary: privacy, storage, reuse, access")
    tid = teacher["teacher_id"]
    check(api.get_coaching_notes(tid, class_id) is None, "GET before any run → None")

    log: list = []
    run = api.generate_coaching_notes(tid, class_id, chat=echo_chat(log))
    check(run["source"] == "agent" and run["reused"] is False and len(run["students"]) == 6
          and {s["name"] for s in run["students"]} == set(NAMES), "a run covers the whole class, with names")
    sent = " ".join(c["raw"] for c in log)
    private = NAMES + [n.split()[0] for n in NAMES] + info["usernames"] + list(info["ids"].values())
    check(not [p for p in private if p in sent], "no name, username or id was sent to the model")
    check("S1" in sent and "S6" in sent and "S7" not in sent, "students reach it as S1…S6")
    for key in ("lessons_opened", "first_try_right"):
        check(key in sent, f"the case file carries '{key}'")
    check("mix_ups" in sent, "the case file carries the concepts they mixed up")

    stored = sqlite3.connect(_DB).execute("SELECT notes, aliases FROM coaching_notes").fetchone()
    check(not [n for n in NAMES if n in stored[0]] and set(json.loads(stored[1])) == {f"S{n}" for n in range(1, 7)},
          "the stored run keeps aliases, not names")
    zara = next(s for s in run["students"] if s["name"] == "Zara Khan")
    check(zara["source"] == "ai" and zara["evidence"], "each note cites its evidence")

    again = api.generate_coaching_notes(tid, class_id, chat=echo_chat([]))
    check(again["reused"] is True and again["run_id"] == run["run_id"], "a second request within a minute reuses the run")
    check(api.get_coaching_notes(tid, class_id)["run_id"] == run["run_id"], "GET returns the latest run")

    sqlite3.connect(_DB).execute("UPDATE coaching_notes SET created_at = '2026-01-01T00:00:00+00:00'").connection.commit()
    rules = api.generate_coaching_notes(tid, class_id)  # the AI is off (LLM_MODEL empty)
    check(rules["source"] == "rules" and "isn't configured" in rules["note"]
          and "Hasn't opened a lesson" in next(s for s in rules["students"] if s["name"] == "Zara Khan")["note"],
          "AI off → a rules run; the student who never started is flagged")
    chose = next(s for s in rules["students"] if s["name"] == "Aarav Kumar")
    check("mix_ups" in chose["evidence"] or "first_try_right" in chose["evidence"],
          "a student with a wrong first try gets a note grounded in it")

    for fn in (api.get_coaching_notes, api.generate_coaching_notes):
        try:
            fn(other["teacher_id"], class_id)
            check(False, f"{fn.__name__}: another teacher → NotFound")
        except NotFoundError:
            check(True, f"{fn.__name__}: another teacher → NotFound")

    client = TestClient(app)
    client.post("/api/teacher/login", json={"username": "rao.coach", "password": "teach-physics-1"})
    sqlite3.connect(_DB).execute("UPDATE coaching_notes SET created_at = '2026-01-01T00:00:00+00:00'").connection.commit()
    r = client.post(f"/api/teacher/classes/{class_id}/coaching")
    check(r.status_code == 200 and r.json()["source"] == "rules" and len(r.json()["students"]) == 6,
          "POST over HTTP works (rules, since the AI is off)")
    r = client.get(f"/api/teacher/classes/{class_id}/coaching")
    check(r.status_code == 200 and r.json()["students"][0]["alias"] == "S1", "GET over HTTP returns it in S order")
    check(client.get("/api/teacher/classes/cls_nope/coaching").status_code == 404, "unknown class → 404")

    student = TestClient(app)
    api.register_student("Kid", "coach.kid", "kid-password-1", "cricket", "Class 11")
    student.post("/api/auth/login", json={"username": "coach.kid", "password": "kid-password-1"})
    check(student.post(f"/api/teacher/classes/{class_id}/coaching").status_code == 401,
          "a student session can't ask for coaching notes")
    check(TestClient(app).get(f"/api/teacher/classes/{class_id}/coaching").status_code == 401, "no session → 401")


def main() -> None:
    test_rules()
    test_model_path()
    teacher, other, class_id, info = setup_class()
    test_boundary(teacher, other, class_id, info)
    print(f"\nAll {_checks} coaching-agent checks passed.")


if __name__ == "__main__":
    main()
