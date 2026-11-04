"""The teacher agent: a tool-using model loop with guardrails. No network calls.

A scripted stand-in replaces Gemini (it implements the same `Model.step`
interface), so every path is tested deterministically:

  1. The loop: the model calls tools, gets real class data back, and writes a
     plan; every tool call is recorded as a step the teacher can see.
  2. Privacy: nothing sent to the model contains a student's name, username or
     id. Students are S1, S2…; names are filled in only for their teacher.
  3. Grounding: tools return the lesson's own key takeaway and the class's
     real misconceptions and numbers.
  4. Robustness: an unknown tool or bad arguments come back as an error the
     model can recover from; a model that keeps calling tools is stopped
     (the last turn has tools off); a plan missing its sections is rejected.
  5. Fallbacks: a failing model → the next model → the rules-based plan, which
     says it was made by rules. No models configured → rules, saying so.
  6. Storage and access: a plan younger than a minute is reused; another
     teacher gets NotFound; a student session gets 401; GET before any plan
     returns null.

Run: venv\\Scripts\\python.exe tests\\test_teacher_agent.py
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

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_agent_"))
_DB = _TMP / "agent.db"
os.environ["ECOLEARN_PROGRESS_DB"] = str(_DB)
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from ecolearn import platform_api as api  # noqa: E402
from ecolearn.agents import teacher_agent  # noqa: E402
from ecolearn.agents.teacher_agent import ModelTurn  # noqa: E402
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


GOOD_PLAN = """## In one line
Most of the class [S1] [S2] think force alone sets acceleration.

## Tomorrow's 10-minute starter
Ask which ball speeds up more.

## Who to check in with
- [S1] chose the misconception.
- [S2] chose it too.

## What to do next
Revisit Newton's second law.

## How sure is this?
Six first-try answers."""


class ScriptedModel:
    """Plays back a fixed list of turns and records everything it was sent."""

    def __init__(self, name: str, turns: list, fail_with: Exception | None = None):
        self.name = name
        self.turns = list(turns)
        self.fail_with = fail_with
        self.seen: list[str] = []
        self.allow_tools_log: list[bool] = []

    def step(self, messages, allow_tools):
        self.seen.append(json.dumps(messages, default=str))
        self.allow_tools_log.append(allow_tools)
        if self.fail_with:
            raise self.fail_with
        turn = self.turns.pop(0) if self.turns else ModelTurn(text=GOOD_PLAN, calls=[])
        if callable(turn):
            turn = turn(messages, allow_tools)
        return turn


def calls(*pairs) -> ModelTurn:
    return ModelTurn(text="", calls=[{"name": n, "args": a} for n, a in pairs])


def setup_class() -> tuple[dict, dict, str, dict]:
    teacher = api.create_teacher("Ms. Rao", "rao.agent", "teach-physics-1")
    other = api.create_teacher("Mr. Sen", "sen.agent", "teach-physics-2")
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
    return teacher, other, made["class"]["class_id"], {"ids": ids, "usernames": usernames,
                                                        "wrong": wrong}


def private_strings(info: dict) -> list[str]:
    return NAMES + [n.split()[0] for n in NAMES] + info["usernames"] + list(info["ids"].values())


def test_loop_and_privacy(teacher, class_id, info) -> None:
    print("\n[1-3] the loop, privacy and grounding")
    model = ScriptedModel("scripted", [
        calls(("get_class_overview", {})),
        calls(("list_misconceptions", {"limit": 3})),
        calls(("get_concept", {"concept_id": CONCEPT}),
              ("get_lesson_takeaway", {"concept_id": CONCEPT})),
        calls(("list_students", {})),
        ModelTurn(text=GOOD_PLAN, calls=[]),
    ])
    plan = api.generate_class_plan(teacher["teacher_id"], class_id, models=[model])
    check(plan["source"] == "agent" and plan["model"] == "scripted" and plan["reused"] is False,
          "the agent's plan is accepted and stored")
    check([s["summary"] for s in plan["steps"]] == [
        "Looked at the class overview",
        "Read the most common misconceptions",
        "Looked up a concept and its prerequisites: Newton's second law",
        "Read the lesson's key takeaway: Newton's second law",
        "Reviewed each student's activity",
    ], "every tool call is a visible step")

    everything_sent = "\n".join(model.seen)
    leaked = [s for s in private_strings(info) if s in everything_sent]
    check(not leaked, f"no name, username or id was sent to the model (leaked: {leaked})")
    check('"S1"' in everything_sent and '"S6"' in everything_sent, "students reach it as S1…S6")

    tool_results = json.loads(model.seen[-1])
    by_tool = {r["name"]: r["response"] for m in tool_results if m["role"] == "tool"
               for r in m["results"]}
    takeaway = by_tool["get_lesson_takeaway"]["key_takeaway"]
    lesson = lesson_service.student_view(lesson_service.get_authored_lesson(CONCEPT, "cricket"))
    real = next(s["markdown"] for s in lesson["sections"] if s["heading"] == "Key takeaway")
    check(takeaway == real, "the takeaway is the lesson's own text")
    top = by_tool["list_misconceptions"]["misconceptions"][0]
    # Students made in one batch share a timestamp, so aliases follow username
    # order: aarav.k=S1, diya.r=S2, ishaan.d=S3, kabir.s=S4, meera.i=S5, zara.k=S6.
    # The wrong pickers were Aarav, Meera and Kabir.
    check(top["students"].startswith("3 of 5") and top["chosen_by"] == ["S1", "S4", "S5"],
          "the misconception data is the class's real numbers, by alias, in order")
    overview = by_tool["get_class_overview"]
    check(overview["active_students"] == 5 and overview["students"] == 6
          and overview["enough_data"] is True, "overview: 5 of 6 active, 5 first tries = enough data")

    check("**Aarav Kumar**" in plan["markdown"] and "[S1]" not in plan["markdown"],
          "the teacher sees names filled in")
    stored = sqlite3.connect(_DB).execute("SELECT markdown FROM class_plans").fetchone()[0]
    check("[S1]" in stored and "Aarav" not in stored, "the stored plan keeps aliases, not names")

    live = api.get_class_plan_progress(teacher["teacher_id"], class_id)
    check(live["running"] is False and live["stage"].startswith("Asking scripted")
          and [s["summary"] for s in live["steps"]] == [s["summary"] for s in plan["steps"]],
          "the progress feed holds the run's real steps and stage")
    check(not [s for s in private_strings(info) if s in json.dumps(live)],
          "the progress feed has no names")

    again = api.generate_class_plan(teacher["teacher_id"], class_id, models=[ScriptedModel("x", [])])
    check(again["reused"] is True and again["plan_id"] == plan["plan_id"],
          "a second request within a minute reuses the plan")
    check(api.get_class_plan(teacher["teacher_id"], class_id)["plan_id"] == plan["plan_id"],
          "GET returns the latest plan")


def _age_plans() -> None:
    conn = sqlite3.connect(_DB)
    conn.execute("UPDATE class_plans SET created_at = '2026-01-01T00:00:00+00:00'")
    conn.commit()
    conn.close()


def test_robustness(teacher, class_id) -> None:
    print("\n[4] robustness")
    _age_plans()
    model = ScriptedModel("scripted", [
        calls(("delete_everything", {})),
        calls(("get_concept", {"wrong_arg": 1})),
        calls(("get_concept", {"concept_id": "no_such_concept"})),
    ])
    plan = api.generate_class_plan(teacher["teacher_id"], class_id, models=[model])
    check(plan["source"] == "agent", "bad tool calls don't crash the run")
    check([s["ok"] for s in plan["steps"]] == [False, False, False],
          "each bad call is recorded as a failed step")
    replies = json.loads(model.seen[-1])
    errors = [r["response"].get("error", "") for m in replies if m["role"] == "tool"
              for r in m["results"]]
    check("Unknown tool" in errors[0] and "Bad arguments" in errors[1] and "No concept" in errors[2],
          "and the model is told what went wrong")

    _age_plans()
    endless = ScriptedModel("endless", [
        (lambda msgs, allow: calls(("get_class_overview", {})) if allow
         else ModelTurn(text=GOOD_PLAN, calls=[]))
    ] * 20)
    plan = api.generate_class_plan(teacher["teacher_id"], class_id, models=[endless])
    check(len(endless.allow_tools_log) == teacher_agent.MAX_STEPS
          and endless.allow_tools_log[-1] is False and plan["source"] == "agent",
          f"a model that never stops is cut off after {teacher_agent.MAX_STEPS} turns, tools off last")
    check("That's enough investigating" in endless.seen[-1], "and told to write the plan")


def test_fallbacks(teacher, class_id) -> None:
    print("\n[5] fallbacks")
    _age_plans()
    broken = ScriptedModel("broken", [], fail_with=RuntimeError("401 UNAUTHENTICATED"))
    sloppy = ScriptedModel("sloppy", [ModelTurn(text="Here's a plan: do better.", calls=[])])
    plan = api.generate_class_plan(teacher["teacher_id"], class_id, models=[broken, sloppy])
    check(plan["source"] == "rules" and plan["model"] is None and "couldn't be reached" in plan["note"],
          "a failing model, then one missing the sections → the rules plan, which says so")
    md = plan["markdown"]
    check(all(f"## {s}" in md for s in teacher_agent.SECTIONS), "the rules plan has all five sections")
    check("Newton's second law" in md and "3 of 5" in md, "it leads with the real top misconception")
    check("> " in md, "and quotes the lesson's takeaway")
    check("**Aarav Kumar**" in md and "**Zara Khan** hasn't started" in md.replace("- ", ""),
          "it names who chose the misconception and who hasn't started")

    _age_plans()
    plan = api.generate_class_plan(teacher["teacher_id"], class_id, models=[])
    check(plan["source"] == "rules" and "isn't configured" in plan["note"],
          "no model configured → rules, and the note says why")


def test_access(teacher, other, class_id) -> None:
    print("\n[6] access")
    for fn in (api.get_class_plan, api.generate_class_plan):
        try:
            fn(other["teacher_id"], class_id)
            check(False, f"{fn.__name__}: another teacher → NotFound")
        except NotFoundError:
            check(True, f"{fn.__name__}: another teacher → NotFound")

    teacher_agent.default_models = lambda: []  # keep HTTP tests offline
    fresh = api.create_class(teacher["teacher_id"], "12-A", "Class 12", "football", "Solo Student")
    fresh_id = fresh["class"]["class_id"]
    client = TestClient(app)
    client.post("/api/teacher/login", json={"username": "rao.agent", "password": "teach-physics-1"})
    r = client.get(f"/api/teacher/classes/{fresh_id}/plan")
    check(r.status_code == 200 and r.json() is None, "GET before any plan → null")
    r = client.post(f"/api/teacher/classes/{fresh_id}/plan")
    check(r.status_code == 200 and r.json()["source"] == "rules"
          and "Not enough data yet" in r.json()["markdown"],
          "POST on an empty class → a rules plan that says there's not enough data")
    check(client.get("/api/teacher/classes/cls_nope/plan").status_code == 404, "unknown class → 404")

    student = TestClient(app)
    api.register_student("Kid", "agent.kid", "kid-password-1", "cricket", "Class 11")
    student.post("/api/auth/login", json={"username": "agent.kid", "password": "kid-password-1"})
    check(student.post(f"/api/teacher/classes/{fresh_id}/plan").status_code == 401,
          "a student session can't ask for a plan")


def main() -> None:
    teacher, other, class_id, info = setup_class()
    test_loop_and_privacy(teacher, class_id, info)
    test_robustness(teacher, class_id)
    test_fallbacks(teacher, class_id)
    test_access(teacher, other, class_id)
    print(f"\nAll {_checks} teacher-agent checks passed.")


if __name__ == "__main__":
    main()
