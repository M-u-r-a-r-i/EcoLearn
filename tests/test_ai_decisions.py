"""'How the AI decided' (2026-10-03): the decision trail and the teacher's view.

No network: the story agent's model is a scripted stand-in. Proves:

  1. The trail records every step of a story's run: the rule checks, the
     critic's verdict with its problems, a rewrite, and the final pass.
  2. A story the critic keeps rejecting is blocked (the reviewed story is
     shown) with every rejection in its trail; a writer that finds no honest
     fit is recorded as declined; a model failure is recorded as such.
  3. get_class_ai_decisions: the guardrail counts (shown, first draft,
     rewritten, blocked, declined, errors, rule and critic rejections),
     teacher-hidden and reported outcomes, teaching-assistant plans by source
     (a rules fallback with its note), model calls for this class only, and
     the log newest first with names; another teacher's class is not found.
  4. HTTP: teachers only.

Run: venv\\Scripts\\python.exe tests\\test_ai_decisions.py
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

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_decisions_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "decisions.db")
os.environ["LLM_MODEL"] = "free/main-model"
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from src import llm  # noqa: E402
from src import platform_api as api  # noqa: E402
from src.errors import NotFoundError  # noqa: E402
from src.learner import personal_story as ps  # noqa: E402
from src.progress import store  # noqa: E402

_checks = 0

STORY = ("Riya stands at the back of the court, waiting for a smash. Her friend hits the light "
         "shuttle and the heavy practice ball with the same swing. One shoots off, one barely moves. "
         "Same hit, so why such different results? Riya frowns at the net and wonders what the "
         "racquet really changes.")
ANALOGY = ("The racquet's push is the net force, the shuttle and the ball are the masses, and how "
           "quickly each speeds up is the acceleration. The lighter one speeds up far more.")
LIMIT = "Real shuttles feel strong air drag, which the simple picture ignores."
PASS = '{"verdict": "PASS", "problems": []}'


def FAIL(problem: str) -> str:
    return json.dumps({"verdict": "FAIL", "problems": [problem]})


def draft(**over) -> str:
    return json.dumps({"fit": True, "story": STORY, "analogy": ANALOGY, "limit": LIMIT, **over})


class Script:
    """Stand-in for llm.chat: plays writer and critic replies in order."""

    def __init__(self, *replies):
        self.replies = list(replies)

    def __call__(self, messages, role="main", **_):
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        return llm.ChatResult(text=reply, model=f"{role}-model")


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


def setup() -> dict:
    rao = api.create_teacher("Ms. Rao", "rao.ai", "teach-physics-1")
    sen = api.create_teacher("Mr. Sen", "sen.ai", "teach-physics-2")
    made = api.create_class(rao["teacher_id"], "11-AI", "Class 11", "cricket",
                            "Asha Rao\nBilal Khan\nChitra Nair\nDev Shah\nEsha Iyer")
    ids = {c["name"]: c["student_id"] for c in made["credentials"]}
    for sid in ids.values():
        store.save_diagnostic(sid, ["badminton"], [])
    return {"rao": rao, "sen": sen, "class_id": made["class"]["class_id"], "ids": ids}


def run(sid: str, *replies) -> dict:
    ps.chat = Script(*replies)
    return ps.generate(sid, "second_law")


# ---------------------------------------------------------------------------
def test_trails(ctx: dict) -> None:
    print("\n[1-2] the decision trail")
    ids = ctx["ids"]
    row = run(ids["Asha Rao"], draft(story=STORY + " She is 16."), draft(), PASS)
    steps = [(t["attempt"], t["step"], t["passed"]) for t in row["trail"]]
    check(row["status"] == "ready" and row["attempts"] == 2, "shown on the second draft")
    check(steps == [(1, "rules", False), (2, "rules", True), (2, "critic", True)],
          "rule checks fail (digits) → rewrite → rules pass → critic passes")
    check(any("digits" in p for p in row["trail"][0]["problems"]), "the rule check keeps its reason")

    row = run(ids["Esha Iyer"], draft(), FAIL("The analogy says force is used up."), draft(), PASS)
    steps = [(t["attempt"], t["step"], t["passed"]) for t in row["trail"]]
    check(steps == [(1, "rules", True), (1, "critic", False), (2, "rules", True), (2, "critic", True)],
          "critic rejects draft 1 → rewrite → critic passes")
    check(row["trail"][1]["problems"] == ["The analogy says force is used up."]
          and row["trail"][1]["model"] == "critic-model", "the critic's reason, and which model decided")

    blocked = run(ids["Bilal Khan"], *[r for _ in range(ps.MAX_ATTEMPTS)
                                      for r in (draft(), FAIL("Too much like the lesson."))])
    check(blocked["status"] == "failed"
          and sum(1 for t in blocked["trail"] if t["step"] == "critic" and not t["passed"]) == ps.MAX_ATTEMPTS,
          f"critic rejects all {ps.MAX_ATTEMPTS} drafts: blocked, every rejection recorded")
    declined = run(ids["Chitra Nair"], json.dumps({"fit": False}))
    check(declined["status"] == "no_fit" and declined["trail"][0]["step"] == "fit", "the writer declines")
    error = run(ids["Dev Shah"], llm.LLMError("All models failed: HTTP 503"))
    check(error["status"] == "error" and error["trail"][0]["step"] == "model"
          and "503" in error["trail"][0]["problems"][0], "a model failure is recorded")


def test_class_view(ctx: dict) -> None:
    print("\n[3] the teacher's view")
    rao, ids, class_id = ctx["rao"]["teacher_id"], ctx["ids"], ctx["class_id"]
    api.generate_class_plan(rao, class_id, models=[])  # no model: the rules fallback
    store.record_llm_call({"feature": "story_writer", "model": "m", "ok": False,
                           "student_id": ids["Asha Rao"], "latency_ms": 900, "error": "HTTP 500"})
    store.record_llm_call({"feature": "story_writer", "model": "m", "ok": True,
                           "student_id": ids["Asha Rao"], "latency_ms": 1200})
    store.record_llm_call({"feature": "story_writer", "model": "m", "ok": True,
                           "student_id": "stu_someone_else", "latency_ms": 100})
    api.set_class_story_hidden(rao, ids["Asha Rao"], "second_law", True)

    out = api.get_class_ai_decisions(rao, class_id)
    s = out["stories"]
    check((s["attempted"], s["shown"], s["first_draft"], s["rewritten"]) == (5, 1, 0, 2),
          "5 runs; 2 stories, both rewritten; Asha's is hidden, so 1 shown")
    check((s["blocked"], s["declined"], s["errors"], s["hidden_by_teacher"]) == (1, 1, 1, 1),
          "1 blocked, 1 declined, 1 model error, 1 hidden by the teacher")
    check((s["rules_rejections"], s["critic_checks"], s["critic_rejections"])
          == (1, 3 + ps.MAX_ATTEMPTS, 1 + ps.MAX_ATTEMPTS), "rule and critic rejections counted")
    check(out["plans"]["total"] == 1 and out["plans"]["rules"] == 1 and out["plans"]["latest_note"],
          "the teaching assistant fell back to rules, with its note")
    check(out["calls"]["total"] == 2 and out["calls"]["failed"] == 1
          and out["calls"]["by_feature"]["story_writer"]["calls"] == 2,
          "model calls for this class only (another student's call isn't counted)")
    by_name = {e["name"]: e for e in out["log"]}
    check(set(by_name) == {"Asha Rao", "Bilal Khan", "Chitra Nair", "Dev Shah", "Esha Iyer"}
          and by_name["Asha Rao"]["outcome"].startswith("Hidden by you")
          and by_name["Bilal Khan"]["outcome"].startswith("Blocked")
          and by_name["Chitra Nair"]["outcome"].startswith("Declined")
          and len(by_name["Esha Iyer"]["trail"]) == 4 and by_name["Asha Rao"]["emoji"],
          "the log: names, outcomes in plain words, and each trail")
    try:
        api.get_class_ai_decisions(ctx["sen"]["teacher_id"], class_id)
        check(False, "another teacher must not see it")
    except NotFoundError:
        check(True, "another teacher's class: not found")


def test_http(ctx: dict) -> None:
    print("\n[4] HTTP")
    url = f"/api/teacher/classes/{ctx['class_id']}/ai-decisions"
    check(TestClient(app).get(url).status_code == 401, "needs a teacher session")
    teacher = TestClient(app)
    teacher.post("/api/teacher/login", json={"username": "rao.ai", "password": "teach-physics-1"})
    r = teacher.get(url)
    check(r.status_code == 200 and r.json()["stories"]["attempted"] == 5, "teacher → 200")


def main() -> int:
    ctx = setup()
    test_trails(ctx)
    test_class_view(ctx)
    test_http(ctx)
    print(f"\nAll {_checks} AI-decision checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
