"""Practice with AI (2026-10-19): the fifth live-AI place. No network: a stand-in plays the writer and the solver.

  1. The rules gate: a good draft passes; wrong option letters, duplicate options, an answer outside A-D, a copy of
     the lesson's own check, a link, a too-short explanation are each rejected.
  2. The solver gate: shown only when the solver's answer matches the key; a disagreement or a rules failure tries
     again (at most 3 attempts); a model outage stops at once. The writer sees the lesson, its own check (to avoid)
     and its mix-ups, never the student's name, username or id.
  3. The boundary: no question when the student's AI switch is off or no model runs (and no model call); the
     lesson envelope says whether to show the button; the answer key never leaves the server before an answer;
     right/wrong with the mix-up behind a wrong pick; one answer only; only the student's own question; a failed
     attempt is stored for the teacher's counts; NOTHING changes progress, lesson answers or mastery; a rate limit.
  4. HTTP: 401 without a session, the whole flow, 409 on a second answer.

Run: venv\\Scripts\\python.exe tests\\test_ai_practice.py
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import tempfile
import types
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_practice_"))
_DB = _TMP / "practice.db"
os.environ["ECOLEARN_PROGRESS_DB"] = str(_DB)
os.environ["LLM_MODEL"] = ""
os.environ["ECOLEARN_EXPERIMENTS"] = "off"
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from src import platform_api as api  # noqa: E402
from src.errors import ConflictError, EcoLearnError, NotFoundError, TooManyRequestsError  # noqa: E402
from src.learner import help_guard, practice  # noqa: E402
from src.llm.client import LLMError  # noqa: E402
from src.progress import store  # noqa: E402

_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


def raises(exc, fn, *args) -> None:
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"FAIL: expected {exc.__name__} from {fn.__name__}")


GOOD = {
    "question": "A bowler pushes a heavier ball and a lighter ball with the same force. Which speeds up faster?",
    "options": {"A": "The heavier ball", "B": "The lighter ball", "C": "Both the same", "D": "Neither moves"},
    "answer": "B",
    "explanation": "With the same net force, acceleration is force divided by mass, so the smaller mass speeds up more.",
    "why_wrong": {"A": "Thinks heavier things respond more to a push.", "C": "Forgets that mass matters.",
                  "D": "Thinks a force is needed just to keep things moving."},
}


class StandIn:
    """Plays both roles: replies come from two queues (writer drafts, solver answers); records every call."""

    def __init__(self, drafts: list, answers: list) -> None:
        self.drafts, self.answers, self.calls = list(drafts), list(answers), []

    def __call__(self, messages, role="main", **_kw):
        content = messages[-1]["content"]
        self.calls.append((role, content))
        queue = self.answers if "You are checking a physics practice question" in content else self.drafts
        reply = queue.pop(0)
        if isinstance(reply, Exception):
            raise reply
        return types.SimpleNamespace(text=reply if isinstance(reply, str) else json.dumps(reply), model="stand-in")


def test_rules() -> None:
    print("\n[1] the rules gate")
    own = "A cricket ball of mass 0.16 kg is hit with a net force of 8 N. What is its acceleration?"
    ok, why = practice.check_draft(GOOD, own)
    check(ok is not None and why is None and ok["answer"] == "B", "a good draft passes")
    bad = [
        ({**GOOD, "options": {"A": "x", "B": "y", "C": "z"}}, "exactly A, B, C and D"),
        ({**GOOD, "options": {**GOOD["options"], "D": "The lighter ball"}}, "the same"),
        ({**GOOD, "answer": "E"}, "isn't one of A to D"),
        ({**GOOD, "question": own}, "copies the lesson's own check"),
        ({**GOOD, "explanation": "Because. See https://example.com for more on this topic today."}, "link"),
        ({**GOOD, "explanation": "Lighter."}, "explanation has"),
        ("not json at all", "wasn't a JSON object"),
    ]
    for draft, expect in bad:
        clean, why = practice.check_draft(draft if isinstance(draft, dict) else None, own)
        check(clean is None and expect in (why or ""), f"rejected: {expect}")


def material() -> dict:
    return {"sections": {"The physics": "Net force equals mass times acceleration.", "Key takeaway": "F = m a."},
            "own_question": "What is F?", "mix_ups": ["Thinks heavier things fall faster."]}


def test_gates() -> None:
    print("\n[2] the solver gate and retries")
    s = StandIn([GOOD], [{"answer": "B"}])
    out = practice.write(concept_name="Newton's second law", level="Class 11", interest="cricket", material=material(), chat=s)
    check(out["ok"] and len(s.calls) == 2 and s.calls[1][0] == "critic", "writer then solver (the critic role): shown")
    solver_msg = s.calls[1][1]
    check("lighter ball" in solver_msg.lower() and GOOD["explanation"] not in solver_msg
          and GOOD["why_wrong"]["A"] not in solver_msg and '"B"' not in solver_msg.split("QUESTION:")[1],
          "the solver sees the question and options, never the key, explanation or mix-up notes")
    w = s.calls[0][1]
    check("Net force equals mass" in w and "What is F?" in w and "heavier things fall faster" in w,
          "the writer sees the lesson, its own check (to avoid) and its mix-ups")

    s = StandIn([GOOD, GOOD], [{"answer": "A"}, {"answer": "B"}])
    out = practice.write(concept_name="x", level="Class 11", interest="cricket", material=material(), chat=s)
    check(out["ok"] and [t["step"] for t in out["trail"]] == ["rules", "solver", "rules", "solver"]
          and not out["trail"][1]["ok"], "the solver disagreed once: tried again, then shown")
    s = StandIn([GOOD] * 3, [{"answer": "C"}] * 3)
    out = practice.write(concept_name="x", level="Class 11", interest="cricket", material=material(), chat=s)
    check(not out["ok"] and len(s.calls) == 6, "three disagreements: no question (never a half-checked one)")
    s = StandIn(["garbage", GOOD], [{"answer": "B"}])
    out = practice.write(concept_name="x", level="Class 11", interest="cricket", material=material(), chat=s)
    check(out["ok"] and out["trail"][0]["step"] == "rules" and not out["trail"][0]["ok"], "a bad draft is retried")
    s = StandIn([LLMError("All models failed")], [])
    out = practice.write(concept_name="x", level="Class 11", interest="cricket", material=material(), chat=s)
    check(not out["ok"] and len(s.calls) == 1, "a model outage stops at once")
    s = StandIn([GOOD], [{"answer": "NONE"}])
    s.drafts += [GOOD, GOOD]
    s.answers += [{"answer": "NONE"}, {"answer": "NONE"}]
    check(not practice.write(concept_name="x", level="Class 11", interest="cricket", material=material(), chat=s)["ok"],
          "the solver finding no single right answer counts as a disagreement")


def counts(sid: str) -> tuple:
    conn = sqlite3.connect(_DB)
    return tuple(conn.execute(f"SELECT COUNT(*) FROM {t} WHERE student_id = ?", (sid,)).fetchone()[0]
                 for t in ("progress", "answers", "review_answers"))


def test_boundary() -> None:
    print("\n[3] the boundary")
    teacher = api.create_teacher("Ms. Rao", "rao.practice", "teach-physics-1")
    made = api.create_class(teacher["teacher_id"], "11-P", "Class 11", "cricket", "Aarav Kumar\nMeera Iyer")
    a, b = (c["student_id"] for c in made["credentials"])
    usernames = [c["username"] for c in made["credentials"]]

    api._practice_chat = None
    out = api.start_practice(a, "second_law")
    check(out == {"available": False, "reason": "not_configured", "message": out["message"]},
          "no model running: no question, no error")
    check(api.get_next_lesson(a, "laws_of_motion").get("practice_available") is False,
          "and the lesson tells the page not to show the button")

    s = StandIn([GOOD] * 20, [{"answer": "B"}] * 20)
    api._practice_chat = s
    check(api.get_next_lesson(a, "laws_of_motion")["practice_available"] is True,
          "with a model: the button shows")
    api.set_student_ai(teacher["teacher_id"], b, False)
    check(api.start_practice(b, "second_law")["reason"] == "ai_off" and not s.calls,
          "the student's AI switch off: no question and no model call")
    check(api.get_next_lesson(b, "laws_of_motion")["practice_available"] is False,
          "and no button for them")

    before = counts(a)
    q = api.start_practice(a, "second_law")
    check(q["available"] and set(q) == {"available", "practice_id", "concept_id", "concept_name", "question", "options"},
          "a question comes back with no answer key and no explanation")
    sent = " ".join(c for _, c in s.calls)
    check("Aarav" not in sent and usernames[0] not in sent and a not in sent, "no name, username or id is sent")
    wrong = api.answer_practice(a, q["practice_id"], "A")
    check(not wrong["correct"] and wrong["correct_option"] == "B" and wrong["why_wrong"] == GOOD["why_wrong"]["A"]
          and wrong["explanation"], "a wrong pick: the right option, why it's right, and the mix-up behind theirs")
    raises(ConflictError, api.answer_practice, a, q["practice_id"], "B")
    q2 = api.start_practice(a, "second_law")
    right = api.answer_practice(a, q2["practice_id"], "b")
    check(right["correct"] and right["why_wrong"] is None, "a right pick (lower case is fine)")
    raises(NotFoundError, api.answer_practice, b, q2["practice_id"], "B")
    raises(EcoLearnError, api.answer_practice, a, api.start_practice(a, "second_law")["practice_id"], "Z")
    check(counts(a) == before, "nothing was added to progress, lesson answers or revision answers")

    s.drafts[:0] = [GOOD] * 3
    s.answers[:0] = [{"answer": "D"}] * 3
    failed = api.start_practice(a, "second_law")
    check(not failed["available"] and failed["reason"] == "failed", "the checks threw every attempt away: no question")
    c = store.practice_counts([a, b])
    check(c["thrown_away"] == 1 and c["written"] == 3 and c["answered"] == 2 and c["right"] == 1,
          f"the teacher's counts (got {c})")
    check(api.get_class_ai_decisions(teacher["teacher_id"], made["class"]["class_id"])["practice"] == c,
          "and they show in 'How the AI decided'")

    api._practice_limiter = help_guard.HelpLimiter(per_window=1, window_seconds=600, per_day=10)
    api.start_practice(a, "second_law")
    raises(TooManyRequestsError, api.start_practice, a, "second_law")
    api._practice_limiter = help_guard.HelpLimiter(per_window=100, window_seconds=600, per_day=100)


def test_http() -> None:
    print("\n[4] HTTP")
    api.register_student("Http Kid", "practice.http", "kid-password-1", "cricket", "Class 11")
    api._practice_chat = StandIn([GOOD] * 5, [{"answer": "B"}] * 5)
    c = TestClient(app)
    check(c.post("/api/practice", json={"concept_id": "second_law"}).status_code == 401, "no session -> 401")
    c.post("/api/auth/login", json={"username": "practice.http", "password": "kid-password-1"})
    r = c.post("/api/practice", json={"concept_id": "second_law"})
    check(r.status_code == 200 and r.json()["available"] and "answer" not in r.json(), "200, no key")
    pid = r.json()["practice_id"]
    r = c.post(f"/api/practice/{pid}/answer", json={"answer": "B"})
    check(r.status_code == 200 and r.json()["correct"], "the answer is checked")
    check(c.post(f"/api/practice/{pid}/answer", json={"answer": "B"}).status_code == 409, "a second answer -> 409")


def main() -> None:
    test_rules()
    test_gates()
    test_boundary()
    test_http()
    print(f"\nAll {_checks} AI-practice checks passed.")


if __name__ == "__main__":
    main()
