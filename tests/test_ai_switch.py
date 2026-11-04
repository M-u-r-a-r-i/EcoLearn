"""The per-student AI switch and the doubt chat's new tutor (2026-10-14). No network.

  1. The switch: on by default; a teacher turns it off only for their own students; the operator can too;
     it shows in the profile, the class list and a family's export.
  2. Off means nothing about the student reaches a model:
     - no personal story is written or shown (the lesson's own story instead);
     - the help chat answers with the lesson's key idea and makes no model call;
     - their coaching note is written by rules and their case is never in the model's message;
     - the teaching assistant's tools never show them, and its plan says how many were left out.
  3. The doubt tutor (src/learner/doubt_tutor.py): one call, grounded in the student's own lesson;
     off-topic replies are refused; a reply that fails a check (not JSON, too short, a link, the student's
     name) or a model failure falls back to the lesson's key idea; no model configured falls back too;
     the call is in the usage log as "doubt_chat" with its tokens; the outcome is counted, never the words.
  4. HTTP: POST /api/teacher/students/{id}/ai (teacher only, own class).

Run: venv\\Scripts\\python.exe tests\\test_ai_switch.py
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import types
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_aiswitch_"))
_DB = _TMP / "aiswitch.db"
os.environ["ECOLEARN_PROGRESS_DB"] = str(_DB)
os.environ["LLM_MODEL"] = ""
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from src import platform_api as api  # noqa: E402
from src.errors import NotFoundError  # noqa: E402
from src.learner import doubt_tutor, help_guard  # noqa: E402
from src.learner import personal_story as ps  # noqa: E402
from src.llm.client import LLMError  # noqa: E402
from src.path import engine  # noqa: E402
from src.progress import store  # noqa: E402

ps.SYNC = True
_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


ANSWER = ("Newton's second law says the net force equals mass times acceleration, F = m a. "
          "With the same push, a heavier cart speeds up more slowly, because the same force is shared "
          "over more mass. Think of a bowler's run-up: a heavier ball needs a stronger arm for the same pace.")


class Recorder:
    """A stand-in for llm.chat that records every message and plays back a fixed reply."""

    def __init__(self, reply: str | Exception = "") -> None:
        self.reply = reply
        self.messages: list[str] = []

    def __call__(self, messages, **_kwargs):
        self.messages.append(messages[-1]["content"])
        if isinstance(self.reply, Exception):
            raise self.reply
        return types.SimpleNamespace(text=self.reply, model="stand-in/model")


def setup() -> dict:
    teacher = api.create_teacher("Ms. Rao", "rao.switch", "teach-physics-1")
    other = api.create_teacher("Mr. Sen", "sen.switch", "teach-physics-2")
    made = api.create_class(teacher["teacher_id"], "11-C", "Class 11", "cricket",
                            "Aarav Kumar\nMeera Iyer\nKabir Shah")
    ids = [c["student_id"] for c in made["credentials"]]
    for sid in ids:
        store.save_diagnostic(sid, ["badminton"], [])
    return {"teacher": teacher["teacher_id"], "other": other["teacher_id"],
            "class_id": made["class"]["class_id"], "ids": ids,
            "usernames": [c["username"] for c in made["credentials"]]}


def test_switch(ctx: dict) -> None:
    print("\n[1] the switch")
    a, b, c = ctx["ids"]
    check(api.get_student_profile(a)["ai_enabled"] is True, "on by default")
    try:
        api.set_student_ai(ctx["other"], a, False)
        check(False, "another teacher cannot switch it")
    except NotFoundError:
        check(api.get_student_profile(a)["ai_enabled"] is True, "another teacher cannot switch it")
    out = api.set_student_ai(ctx["teacher"], a, False)
    check(out == {"student_id": a, "ai_enabled": False} and api.get_student_profile(a)["ai_enabled"] is False,
          "the student's own teacher can switch it off")
    rows = {s["student_id"]: s for s in api.get_class_detail(ctx["teacher"], ctx["class_id"])["students"]}
    check(rows[a]["ai_enabled"] is False and rows[b]["ai_enabled"] is True, "the class list shows it")
    check(api.export_student_data(a)["account"]["ai_enabled"] is False, "a family's export shows it")
    api.operator_set_student_ai(c, False)
    check(api.get_student_profile(c)["ai_enabled"] is False, "the operator can switch it off")
    api.operator_set_student_ai(c, True)
    check(api.get_student_profile(c)["ai_enabled"] is True, "and back on")
    try:
        api.operator_set_student_ai("stu_nobody", False)
        check(False, "an unknown student is refused")
    except NotFoundError:
        check(True, "an unknown student is refused")


def test_stories(ctx: dict) -> None:
    print("\n[2a] personal stories")
    a, b, _ = ctx["ids"]
    concept = "second_law"
    check(ps._context(b, concept) is not None, "a student with AI on has a story to write")
    check(ps._context(a, concept) is None and api.get_personal_story(a, concept)["status"] == "none",
          "with AI off there is nothing to write and the lesson's own story is shown")
    os.environ["LLM_MODEL"] = "stand-in/model"
    calls = []
    real = ps.generate
    ps.generate = lambda sid, cid: calls.append(sid)
    try:
        ps.request(a, concept)
        ps.request(b, concept)
    finally:
        ps.generate = real
        os.environ["LLM_MODEL"] = ""
    check(calls == [b], "a story is only started for the student whose AI is on")


def test_help_chat(ctx: dict) -> None:
    print("\n[2b, 3] the help chat")
    a, b, _ = ctx["ids"]
    api._help_limiter = help_guard.HelpLimiter(per_window=100, window_seconds=600, per_day=100)
    rec = Recorder(json.dumps({"on_topic": True, "answer": ANSWER}))
    api._help_chat = rec
    q = "Why does a heavier cart speed up more slowly with the same push?"

    off = api.ask_help(a, "second_law", q)
    check(off["verdict"] == "AI_OFF" and off["source"] == "rules" and off["attempts"] == 0 and not rec.messages,
          "AI off: no model call, the answer says the AI is off")
    check("key idea" in off["answer"] and "teacher" in off["answer"], "and gives the lesson's key idea and the teacher")

    out = api.ask_help(b, "second_law", q)
    check(out["verdict"] == "PASS" and out["source"] == "ai" and out["answer"] == ANSWER and out["attempts"] == 1,
          "AI on: the checked answer is returned")
    msg = rec.messages[-1]
    takeaway = doubt_tutor.lesson_context(engine.find_concept("second_law"), "cricket")["takeaway"]
    check(takeaway and takeaway[:80] in msg and "## The physics" in msg and "## Worked example" in msg,
          "the model is grounded in the student's own lesson")
    check("Meera" not in msg and ctx["usernames"][1] not in msg, "the student's name and username are never sent")
    check(msg.rstrip().endswith("Reply with the JSON object now.") and q in msg,
          "the question goes in once, after the lesson")

    cases = [
        ('{"on_topic": false, "answer": ""}', "OFF_TOPIC", "only help with physics"),
        ("Sure! F = m a.", "FALLBACK", "key idea"),
        (json.dumps({"on_topic": True, "answer": "F = m a."}), "FALLBACK", "key idea"),
        (json.dumps({"on_topic": True, "answer": ANSWER + " See https://example.com"}), "FALLBACK", "key idea"),
        (json.dumps({"on_topic": True, "answer": ANSWER + " Well done, Meera Iyer!"}), "FALLBACK", "key idea"),
        (LLMError("All models failed"), "FALLBACK", "key idea"),
    ]
    for reply, verdict, phrase in cases:
        rec.reply = reply
        r = api.ask_help(b, "second_law", q)
        check(r["verdict"] == verdict and phrase in r["answer"] and r["source"] == "rules",
              f"{str(reply)[:40]!r} -> {verdict}")
    rec.reply = json.dumps({"on_topic": True, "answer": ANSWER.replace("bowler", "ray of light and a bowler")})
    check(api.ask_help(b, "second_law", q)["verdict"] == "PASS",
          "an ordinary word that is part of no full name is fine")

    api._help_chat = None  # the live chain, with no model configured
    r = api.ask_help(b, "second_law", q)
    check(r["verdict"] == "FALLBACK" and r["attempts"] == 0 and "isn't running" in r["answer"],
          "no model configured: the lesson's key idea, no error")

    counts = store.help_event_counts([a, b])
    check(counts["ai_off"] == 1 and counts["answered"] == 2 and counts["off_topic"] == 1 and counts["fallback"] == 6,
          f"outcomes are counted (got {counts})")
    everything = " ".join(str(v) for t in ("help_events", "llm_calls")
                          for row in store._connect().execute(f"SELECT * FROM {t}") for v in row)
    check("heavier cart" not in everything and "bowler" not in everything, "the words are never stored")


def test_usage_log(ctx: dict) -> None:
    print("\n[3b] the usage log")
    import httpx
    from src.llm import client as llm_client
    b = ctx["ids"][1]
    api._help_chat = None
    os.environ["LLM_MODEL"] = "free/main-model"

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={
            "model": "free/main-model",
            "choices": [{"message": {"content": json.dumps({"on_topic": True, "answer": ANSWER})}}],
            "usage": {"prompt_tokens": 1500, "completion_tokens": 120}})

    llm_client._transport = httpx.MockTransport(handler)
    try:
        r = api.ask_help(b, "second_law", "What does net force mean in this lesson?")
    finally:
        llm_client._transport = None
        os.environ["LLM_MODEL"] = ""
    rows = [c for c in store.get_llm_calls() if c["feature"] == "doubt_chat"]
    check(r["verdict"] == "PASS" and rows and rows[-1]["prompt_tokens"] == 1500
          and rows[-1]["completion_tokens"] == 120 and rows[-1]["student_id"] == b,
          "the doubt chat's call is logged with its tokens and the student")


def test_coaching(ctx: dict) -> None:
    print("\n[2c] coaching notes")
    a = ctx["ids"][0]
    payloads = []

    def chat(messages, **_kwargs):
        content = messages[-1]["content"]
        payloads.append(content)
        cases = json.loads(content.split("CASE FILES (JSON):\n", 1)[1].split("\n\nWrite the JSON now.")[0])
        return types.SimpleNamespace(text=json.dumps({k: {} for k in cases}), model="stand-in/model")

    run = api.generate_coaching_notes(ctx["teacher"], ctx["class_id"], chat=chat)
    sent = set()
    for p in payloads:
        sent |= set(json.loads(p.split("CASE FILES (JSON):\n", 1)[1].split("\n\nWrite the JSON now.")[0]))
    alias_a = next(s["alias"] for s in run["students"] if s["student_id"] == a)
    check(alias_a not in sent and len(sent) == 2, "the AI-off student's case never goes to the model")
    check(next(s for s in run["students"] if s["student_id"] == a)["source"] == "rules",
          "and their note is written by rules")
    check(len(run["students"]) == 3, "every student still gets a note")


def test_teacher_agent(ctx: dict) -> None:
    print("\n[2d] the teaching assistant")
    a = ctx["ids"][0]
    toolbox, aliases = api._class_toolbox(ctx["teacher"], ctx["class_id"])
    check(a not in aliases.values() and len(aliases) == 2, "the AI-off student has no label for the agent")
    results = [toolbox.call(n, {}) for n in ("get_class_overview", "list_misconceptions", "list_students")]
    check(all("error" not in r for r in results), "the agent's tools answer")
    seen = json.dumps(results)
    check(len(results[2]["students"]) == 2, "it sees two students, not three")
    check(a not in seen and "S1" not in seen, "and never the AI-off one in what its tools return")
    check(sorted(aliases) == ["S2", "S3"], "labels stay numbered over the whole class")
    plan = api.generate_class_plan(ctx["teacher"], ctx["class_id"], models=[])
    check("1 student with the AI switched off is not included" in (plan.get("note") or ""),
          "the plan says how many students were left out")


def test_http(ctx: dict) -> None:
    print("\n[4] HTTP")
    b = ctx["ids"][1]
    c = TestClient(app)
    check(c.post(f"/api/teacher/students/{b}/ai", json={"enabled": False}).status_code == 401, "no session -> 401")
    c.post("/api/teacher/login", json={"username": "sen.switch", "password": "teach-physics-2"})
    check(c.post(f"/api/teacher/students/{b}/ai", json={"enabled": False}).status_code == 404,
          "another teacher -> 404")
    c2 = TestClient(app)
    c2.post("/api/teacher/login", json={"username": "rao.switch", "password": "teach-physics-1"})
    r = c2.post(f"/api/teacher/students/{b}/ai", json={"enabled": False})
    check(r.status_code == 200 and r.json()["ai_enabled"] is False and not api.get_student_profile(b)["ai_enabled"],
          "the student's teacher -> 200, switched off")
    c2.post(f"/api/teacher/students/{b}/ai", json={"enabled": True})
    check(api.get_student_profile(b)["ai_enabled"], "and back on")


def main() -> None:
    ctx = setup()
    test_switch(ctx)
    test_stories(ctx)
    test_help_chat(ctx)
    test_usage_log(ctx)
    test_coaching(ctx)
    test_teacher_agent(ctx)
    test_http(ctx)
    print(f"\nAll {_checks} AI-switch and doubt-tutor checks passed.")


if __name__ == "__main__":
    main()
