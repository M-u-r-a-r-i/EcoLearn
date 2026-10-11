"""Layer 3: personal stories, and the src/llm provider layer. No network.

The writer and critic are scripted stand-ins for `personal_story.chat`, and
the HTTP client is tested against httpx.MockTransport playing OmniRoute.

Proves:
  1. Hobby choice: only a hobby whose `fits` covers the concept's domain; never
     the student's own lesson interest; an own hobby goes to the writer.
  2. The happy path: writer → guards → critic PASS → stored and served; the
     lesson page gets it, and the next two concepts are started too.
  3. Privacy: no name, username or id in anything sent to a model; the
     student's open mix-up IS sent (first sentence only).
  4. Guards and the critic: digits, lengths and links are caught before the
     critic; one retry with the problems fed back; a second failure → none
     (the page shows the pre-written story); an unreadable critic verdict is a
     FAIL (fail closed); the writer may decline ("fit": false).
  5. Errors: a dead gateway stores an error and doesn't retry for 30 min; no
     model configured → no calls at all.
  6. Cache: a story is reused, and retired when the lesson text changes.
  7. The llm client: OpenAI request shape, Bearer key, fallback down the chain,
     tool calls parsed; JSON pulled out of chatty replies.
  8. The teacher agent over the OpenAI-compatible route: a tool call goes out,
     its result comes back with the matching id, and a plan is produced.
  9. HTTP: GET /api/personal-story needs a student session.

Run: venv\\Scripts\\python.exe tests\\test_personal_story.py
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
sys.path.insert(0, str(_ROOT))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_story_"))
_DB = _TMP / "story.db"
os.environ["ECOLEARN_PROGRESS_DB"] = str(_DB)
os.environ["LLM_MODEL"] = "free/main-model"
os.environ["LLM_FALLBACK_MODELS"] = "free/backup-model"
os.environ["LLM_BASE_URL"] = "http://gateway.test/v1"
os.environ["LLM_API_KEY"] = "test-key"
warnings.simplefilter("ignore")

import httpx  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from src import llm, platform_api as api  # noqa: E402
from src.agents import teacher_agent  # noqa: E402
from src.learner import personal_story as ps  # noqa: E402
from src.llm import client as llm_client  # noqa: E402
from src.progress import store  # noqa: E402

ps.SYNC = True
_checks = 0
_n = 0

STORY = ("Riya stands at the back of the court, waiting for a smash. Her friend hits the light "
         "shuttle and the heavy practice ball with the same swing. One shoots off, one barely moves. "
         "Same hit, so why such different results? Riya frowns at the net and wonders what the "
         "racquet really changes.")
ANALOGY = ("The racquet's push is the net force, the shuttle and the ball are the masses, and how "
           "quickly each speeds up is the acceleration. The lighter one speeds up far more.")
LIMIT = "Real shuttles feel strong air drag, which the simple picture ignores."


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


class Script:
    """Stand-in for llm.chat: plays writer and critic replies in order."""

    def __init__(self, *replies):
        self.replies = list(replies)
        self.sent: list[tuple[str, str]] = []

    def __call__(self, messages, role="main", **_):
        self.sent.append((role, json.dumps(messages)))
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        return llm.ChatResult(text=reply, model=f"{role}-model")


def draft(**over) -> str:
    return json.dumps({"fit": True, "story": STORY, "analogy": ANALOGY, "limit": LIMIT, **over})


PASS = '{"verdict": "PASS", "problems": []}'


def student(hobbies, interest="cricket", mixup=None) -> tuple[str, str]:
    global _n
    _n += 1
    username = f"story.kid{_n}"
    sid = api.register_student(f"Tanvi Kulkarni {_n}", username, "kid-password-1", interest,
                               "Class 11")["student_id"]
    rows = []
    if mixup:
        rows = [{"concept_id": "second_law", "source_interest": "football", "selected": "B",
                 "correct": False, "misconception": mixup}]
    store.save_diagnostic(sid, hobbies, rows)
    return sid, username


def test_hobby_choice() -> None:
    print("\n[1] hobby choice")
    check(ps.choose_hobby(["reading", "badminton"], "football", "mechanics")["id"] == "badminton",
          "reading doesn't fit mechanics; badminton does")
    check(ps.choose_hobby(["cricket", "badminton"], "cricket", "mechanics")["id"] == "badminton",
          "the student's own lesson interest is skipped")
    check(ps.choose_hobby(["badminton"], "cricket", "electricity") is None,
          "badminton isn't forced onto electricity")
    check(ps.choose_hobby(["badminton", "kite flying"], "cricket", "optics")["id"] == "kite flying",
          "an own hobby goes to the writer, which may decline")


def test_happy_path() -> None:
    print("\n[2-3] writer → guards → critic, and privacy")
    sid, username = student(["badminton"],
                            mixup="Thinks a bigger force always means a bigger speed. It doesn't.")
    script = Script(draft(), PASS, draft(), PASS, draft(), PASS)
    ps.chat = script
    lesson = api.get_next_lesson(sid, "laws_of_motion", concept_id="second_law")
    story = lesson["lesson"]["personal_story"]
    check(story["status"] == "ready" and story["hobby"] == "Badminton" and story["story"] == STORY
          and story["analogy"] == ANALOGY and story["limit"] == LIMIT,
          "the lesson arrives with a ready badminton story")
    row = store.get_personal_story(sid, "second_law")
    check(row["status"] == "ready" and row["attempts"] == 1, "stored after one attempt")
    upcoming = sqlite3.connect(_DB).execute(
        "SELECT COUNT(*) FROM personal_stories WHERE student_id = ?", (sid,)).fetchone()[0]
    check(upcoming == 3, "the next two concepts were written too")
    everything = "\n".join(text for _, text in script.sent)
    for private in ("Tanvi", "Kulkarni", username, sid):
        check(private not in everything, f"{private!r} never reaches a model")
    first_writer = script.sent[0][1]
    check("Thinks a bigger force always means a bigger speed." in first_writer
          and "It doesn't." not in first_writer, "the student's mix-up is sent (first sentence)")
    check("THE LESSON'S KEY TAKEAWAY" in first_writer and "Badminton" in first_writer,
          "the writer gets the lesson's own text and the hobby")
    check([r for r, _ in script.sent[:2]] == ["main", "critic"], "a separate critic call")

    calls = len(script.sent)
    again = api.get_personal_story(sid, "second_law")
    check(again["status"] == "ready" and len(script.sent) == calls, "served from cache: no new calls")


def test_guards_and_critic() -> None:
    print("\n[4] guards, critic, retry, fail closed, decline")
    sid, _ = student(["badminton"])
    ps.chat = Script(draft(story=STORY + " It reaches 30 metres per second."), draft(), PASS)
    out = ps.generate(sid, "second_law")
    check(out["status"] == "ready" and out["attempts"] == 2, "digits caught; fixed on the retry")
    sid, _ = student(["badminton"])
    script = Script(draft(), '{"verdict": "FAIL", "problems": ["Says force is used up."]}',
                    draft(), '{"verdict": "FAIL", "problems": ["Still wrong."]}')
    ps.chat = script
    out = ps.generate(sid, "second_law")
    check(out["status"] == "failed" and out["problems"] == ["Still wrong."],
          "two critic failures → failed, with the reasons kept")
    check("Says force is used up." in script.sent[2][1], "the first critique was fed back to the writer")
    check(api.get_personal_story(sid, "second_law")["status"] == "none",
          "a failed story means the page shows the pre-written one")
    sid, _ = student(["badminton"])
    ps.chat = Script(draft(), "I think it's mostly fine!", draft(), "{}")
    check(ps.generate(sid, "second_law")["status"] == "failed",
          "an unreadable critic verdict is a FAIL (fail closed)")
    sid, _ = student(["badminton"])
    ps.chat = Script('{"fit": false}')
    check(ps.generate(sid, "second_law")["status"] == "no_fit"
          and api.get_personal_story(sid, "second_law")["status"] == "none",
          "the writer may decline; no story is shown")
    check(ps.guard_problems({"story": "Short.", "analogy": ANALOGY, "limit": "See http://x.com now"})
          and any("link" in p for p in ps.guard_problems({"story": STORY, "analogy": ANALOGY,
                                                           "limit": "See www.x.com for more on this."})),
          "lengths and links are guarded")


def test_errors_and_cache() -> None:
    print("\n[5-6] errors and the cache")
    sid, _ = student(["badminton"])
    script = Script(llm.LLMError("All models failed: HTTP 503"))
    ps.chat = script
    ps.request(sid, "second_law")
    check(store.get_personal_story(sid, "second_law")["status"] == "error", "a dead gateway → error row")
    ps.request(sid, "second_law")
    check(len(script.sent) == 1, "and no retry within 30 minutes")

    sid, _ = student(["badminton"])
    ps.chat = Script(draft(), PASS, draft(), PASS)
    ps.generate(sid, "second_law")
    conn = sqlite3.connect(_DB)
    conn.execute("UPDATE personal_stories SET lesson_hash = 'old' WHERE student_id = ?", (sid,))
    conn.commit()
    conn.close()
    view = api.get_personal_story(sid, "second_law")
    check(view["status"] == "ready" and store.get_personal_story(sid, "second_law")["lesson_hash"] != "old",
          "a changed lesson retires the old story and a new one is written")

    os.environ["LLM_MODEL"] = ""
    sid, _ = student(["badminton"])
    script = Script()
    ps.chat = script
    view = api.get_personal_story(sid, "second_law")
    check(view["status"] == "none" and not script.sent, "no model configured → no calls, no story")
    os.environ["LLM_MODEL"] = "free/main-model"


def test_llm_client() -> None:
    print("\n[7] the llm client")
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content)
        seen.append((str(request.url), request.headers.get("authorization"), body["model"]))
        if body["model"] == "free/main-model":
            return httpx.Response(429, json={"error": "rate limited"})
        return httpx.Response(200, json={"model": body["model"], "choices": [{"message": {
            "role": "assistant", "content": None,
            "tool_calls": [{"id": "call_1", "type": "function",
                            "function": {"name": "get_class_overview", "arguments": "{}"}}]}}]})

    llm_client._transport = httpx.MockTransport(handler)
    result = llm.chat([{"role": "user", "content": "hi"}],
                      tools=[{"type": "function", "function": {"name": "x", "parameters": {}}}])
    check(seen[0][0] == "http://gateway.test/v1/chat/completions" and seen[0][1] == "Bearer test-key",
          "POST {base}/chat/completions with the Bearer key")
    check([m for _, _, m in seen] == ["free/main-model", "free/backup-model"]
          and result.model == "free/backup-model", "a 429 falls through to the next model")
    check(result.tool_calls == [{"id": "call_1", "name": "get_class_overview", "args": {}}],
          "tool calls parsed")
    # [7b] "is the AI up?": probes the chain in order, reports a backup, caches a minute
    def health_handler(request: httpx.Request) -> httpx.Response:
        model = json.loads(request.content)["model"]
        if model == "free/main-model":
            return httpx.Response(503, json={"error": "down"})
        return httpx.Response(200, json={"model": model, "choices": [{"message": {"content": "OK"}}]})

    llm_client._transport = httpx.MockTransport(health_handler)
    h = llm.health(force=True)
    check(h["up"] and h["on_fallback"] and h["model"] == "free/backup-model"
          and [t["ok"] for t in h["tried"]] == [False, True], "health: main down, backup answers")
    llm_client._transport = httpx.MockTransport(lambda r: httpx.Response(500))
    check(llm.health()["model"] == "free/backup-model", "health: the answer is cached for a minute")
    h = llm.health(force=True)
    check(h["configured"] and not h["up"] and h["model"] is None, "health: every model down → up is False")
    llm_client._transport = httpx.MockTransport(handler)
    check(ps.guard_problems({"story": "x", "analogy": "y"})[-1] == "'limit' is missing."
          and "'limit' is missing." in ps.guard_problems({"story": "x", "analogy": "y", "limit": "  "}),
          "a missing or blank 'limit' is rejected")
    check(llm_client.parse_json_object('Sure! ```json\n{"a": {"b": 1}}\n``` hope that helps')
          == {"a": {"b": 1}}, "JSON pulled out of a chatty reply")

    # [8] the teacher agent over the same route
    print("\n[8] the teacher agent over an OpenAI-compatible endpoint")
    turns = []

    def agent_handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content)
        turns.append(body)
        if len(turns) == 1:
            return httpx.Response(200, json={"choices": [{"message": {
                "role": "assistant", "content": None,
                "tool_calls": [{"id": "call_7", "type": "function",
                                "function": {"name": "get_class_overview", "arguments": "{}"}}]}}]})
        plan = "\n\n".join(f"## {s}\nText." for s in teacher_agent.SECTIONS)
        return httpx.Response(200, json={"choices": [{"message": {"role": "assistant", "content": plan}}]})

    llm_client._transport = httpx.MockTransport(agent_handler)
    teacher = api.create_teacher("Ms. Rao", "rao.story", "teach-physics-1")
    klass = api.create_class(teacher["teacher_id"], "11-C", "Class 11", "cricket", "Asha Verma")
    original = teacher_agent._gemini_models
    teacher_agent._gemini_models = lambda: []
    plan = api.generate_class_plan(teacher["teacher_id"], klass["class"]["class_id"])
    teacher_agent._gemini_models = original
    check(plan["source"] == "agent" and plan["model"] == "free/main-model",
          "the plan comes from the gateway model")
    check("tools" in turns[0] and turns[0]["tools"][0]["type"] == "function", "tools sent in OpenAI form")
    tool_msg = next(m for m in turns[1]["messages"] if m["role"] == "tool")
    check(tool_msg["tool_call_id"] == "call_7" and json.loads(tool_msg["content"])["students"] == 1,
          "the tool result goes back with the matching call id")
    check("Asha" not in json.dumps(turns), "no student name reaches the gateway")
    llm_client._transport = None


def test_http() -> None:
    print("\n[9] HTTP")
    client = TestClient(app)
    check(client.get("/api/personal-story", params={"concept_id": "second_law"}).status_code == 401,
          "no session → 401")


def main() -> None:
    test_hobby_choice()
    test_happy_path()
    test_guards_and_critic()
    test_errors_and_cache()
    test_llm_client()
    test_http()
    print(f"\nAll {_checks} personal-story checks passed.")


if __name__ == "__main__":
    main()
