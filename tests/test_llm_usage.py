"""The AI usage log and the cost-per-student numbers (2026-10-03).

No network: the LLM client talks to an httpx.MockTransport. Proves:

  1. The client reports every model call to the sink: tokens and model on
     success, ok=False and the error on failure (then the fallback answers);
     tags come from usage_context and nest; a sink that raises never breaks a
     call; no sink means nothing happens.
  2. The boundary's sink writes llm_calls rows.
  3. A real personal-story run (writer, then critic) is logged as
     story_writer and story_critic with the student's id and tokens.
  4. metrics.ai_usage: the longest price key wins (flash-lite isn't flash);
     unlisted models cost nothing actual but are priced at the reference
     model; calls without tokens are counted, not priced; per student and per
     month.
  5. The pilot report carries ai_usage and pseudonymised call rows.

Run: venv\\Scripts\\python.exe tests\\test_llm_usage.py
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

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_usage_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "usage.db")
os.environ["LLM_MODEL"] = "free/main-model"
os.environ["LLM_FALLBACK_MODELS"] = ""
os.environ["LLM_CRITIC_MODEL"] = ""
os.environ["LLM_BASE_URL"] = "http://llm.test/v1"
warnings.simplefilter("ignore")

import httpx  # noqa: E402

from src import llm  # noqa: E402
from src import platform_api as api  # noqa: E402
from src.learner import personal_story as ps  # noqa: E402
from src.llm import client  # noqa: E402
from src.progress import metrics, store  # noqa: E402

_checks = 0

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


def reply(text: str, model: str, prompt: int, completion: int) -> httpx.Response:
    return httpx.Response(200, json={
        "model": model,
        "choices": [{"message": {"role": "assistant", "content": text}}],
        "usage": {"prompt_tokens": prompt, "completion_tokens": completion,
                  "total_tokens": prompt + completion}})


def transport(*responses) -> httpx.MockTransport:
    queue = list(responses)

    def handler(request: httpx.Request) -> httpx.Response:
        return queue.pop(0)

    return httpx.MockTransport(handler)


# ---------------------------------------------------------------------------
def test_client() -> None:
    print("\n[1] the client reports every call")
    seen: list[dict] = []
    llm.set_usage_sink(seen.append)
    client._transport = transport(httpx.Response(500), reply("hi", "free/backup", 120, 30))
    with llm.usage_context(feature="outer", student_id="stu_1"):
        with llm.usage_context(feature="inner"):
            out = llm.chat([{"role": "user", "content": "x"}], models=["free/main", "free/backup"])
    check(out.text == "hi" and len(seen) == 2, "a failed model and the fallback: two records")
    failed, ok = seen
    check(not failed["ok"] and "HTTP 500" in failed["error"] and failed["prompt_tokens"] is None,
          "the failure: ok=False, the error, no tokens")
    check(ok["ok"] and ok["model"] == "free/backup" and ok["prompt_tokens"] == 120
          and ok["completion_tokens"] == 30 and ok["latency_ms"] >= 0, "the answer: model and tokens")
    check(ok["feature"] == "inner" and ok["student_id"] == "stu_1", "tags nest: inner feature, outer student")

    def broken(_):
        raise RuntimeError("disk full")

    llm.set_usage_sink(broken)
    client._transport = transport(reply("still fine", "m", 1, 1))
    check(llm.chat([{"role": "user", "content": "x"}], models=["m"]).text == "still fine",
          "a sink that raises never breaks the call")
    llm.set_usage_sink(None)
    client._transport = transport(reply("quiet", "m", 1, 1))
    check(llm.chat([{"role": "user", "content": "x"}], models=["m"]).text == "quiet", "no sink: nothing logged")
    check(not seen[2:], "and nothing was added")


def test_boundary_sink() -> None:
    print("\n[2] the boundary's sink")
    llm.set_usage_sink(store.record_llm_call)  # what platform_api registers at import
    client._transport = transport(reply("ok", "gemini-2.5-flash", 1000, 200))
    with llm.usage_context(feature="teacher_agent", class_id="cls_1"):
        llm.chat([{"role": "user", "content": "x"}], models=["gemini-2.5-flash"])
    rows = store.get_llm_calls()
    check(len(rows) == 1 and rows[0]["feature"] == "teacher_agent" and rows[0]["class_id"] == "cls_1"
          and rows[0]["prompt_tokens"] == 1000 and rows[0]["ok"] is True, "stored with its tags")


def test_story_run() -> str:
    print("\n[3] a personal story, writer then critic")
    sid = api.register_student("Tanvi K", "usage.kid", "kid-password-1", "cricket", "Class 11")["student_id"]
    store.save_diagnostic(sid, ["badminton"], [])
    draft = json.dumps({"fit": True, "story": STORY, "analogy": ANALOGY, "limit": LIMIT})
    client._transport = transport(reply(draft, "free/main-model", 900, 250),
                                  reply('{"verdict": "PASS", "problems": []}', "free/main-model", 700, 20))
    ps.chat = llm.chat
    ps._run(sid, "second_law")
    check(store.get_personal_story(sid, "second_law")["status"] == "ready", "the story was written")
    rows = [r for r in store.get_llm_calls() if r["student_id"] == sid]
    check([r["feature"] for r in rows] == ["story_writer", "story_critic"],
          "logged as story_writer, then story_critic")
    check(rows[0]["prompt_tokens"] == 900 and rows[1]["completion_tokens"] == 20, "with their tokens")
    return sid


def test_costs() -> None:
    print("\n[4] metrics.ai_usage")
    prices = {"usd_to_inr": 100, "reference_model": "gemini-2.5-flash",
              "models": {"gemini-2.5-flash": {"input": 0.30, "output": 2.50},
                         "gemini-2.5-flash-lite": {"input": 0.10, "output": 0.40}}}

    def call(feature, model, p, c, at, ok=True):
        return {"feature": feature, "model": model, "ok": ok, "prompt_tokens": p,
                "completion_tokens": c, "latency_ms": 1000, "at": at}

    calls = [
        call("story_writer", "google/gemini-2.5-flash-lite", 1_000_000, 0, "2026-10-01T00:00:00+00:00"),
        call("story_writer", "free/llama", 1_000_000, 100_000, "2026-10-04T00:00:00+00:00"),
        call("doubt_chat", "gemini pipeline", None, None, "2026-10-11T00:00:00+00:00"),
    ]
    u = metrics.ai_usage(calls, prices, students=4)
    w = u["by_feature"]["story_writer"]
    check(w["actual_inr"] == 10.0, "flash-lite priced as flash-lite (₹10), the free model at ₹0")
    check(w["reference_inr"] == 30.0 + 30.0 + 25.0,
          "reference: every call at flash prices (₹30 + ₹30 + ₹25)")
    check(u["total"]["calls_without_tokens"] == 1 and u["by_feature"]["doubt_chat"]["reference_inr"] == 0,
          "a call without tokens is counted, not priced")
    check(u["days"] == 10.0 and u["reference_inr_per_student"] == 21.25
          and u["reference_inr_per_student_month"] == 63.75,
          "per student ₹21.25 over 10 days ≈ ₹63.75 a month")
    empty = metrics.ai_usage([], prices, students=0)
    check(empty["total"]["calls"] == 0 and empty["reference_inr_per_student"] is None, "no calls, no students")


def test_report(sid: str) -> None:
    print("\n[5] the pilot report")
    report = api.pilot_report()
    u = report["ai_usage"]
    check(u["total"]["calls"] == 3 and set(u["by_feature"]) == {"teacher_agent", "story_writer", "story_critic"},
          "ai_usage over every logged call")
    real = api.llm_prices()
    check(real["reference_model"] in real["models"], "prices from data/llm_prices.yaml: the reference model is priced")
    from src.progress import metrics as _m
    check(_m._price_for("gemini/gemini-3.1-flash-lite", real) == {"input": 0.25, "output": 1.50},
          "the model in use (3.1 flash-lite) is priced at Google's published 0.25 / 1.50")
    check(_m._price_for("gemini/gemini-3.7-flash", real) == _m._price_for("gemini/gemini-3.8-flash", real) is not None,
          "the deprecated 3.7 flash is priced like 3.8 (Google routes it there)")
    check(_m._price_for("gemini/gemini-2.5-flash-lite", real)["input"] == 0.10,
          "the longest key wins: 2.5 flash-lite is not priced as 2.5 flash")
    rows = report["llm_calls"]
    dumped = json.dumps(rows)
    check(len(rows) == 3 and sid not in dumped and "cls_1" not in dumped
          and any(r["student_id"] and r["student_id"].startswith("S") for r in rows),
          "call rows are pseudonymised")


def main() -> int:
    try:
        test_client()
        test_boundary_sink()
        sid = test_story_run()
        test_costs()
        test_report(sid)
    finally:
        client._transport = None
    print(f"\nAll {_checks} usage-log checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
