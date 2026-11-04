r"""Is the live AI answering? Run this before a demo or a pilot day.

    venv\Scripts\python.exe scripts\ai_check.py

Probes the configured model chain (LLM_MODEL, then LLM_FALLBACK_MODELS) with a tiny
call and prints which model answers and how fast. Exit code 0 = a model answered,
1 = the AI is off or down (the app still works: every AI feature has a fallback).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import llm  # noqa: E402


def main() -> int:
    status = llm.health(force=True)
    if not status["configured"]:
        print("AI is not configured (LLM_MODEL is empty). Plans and stories use their fallbacks.")
        return 1
    for t in status["tried"]:
        print(f"  {'ok  ' if t['ok'] else 'FAIL'} {t['model']}  {t['latency_ms'] / 1000:.1f} s"
              + ("" if t["ok"] else f"  ({t['error']})"))
    if not status["up"]:
        print("AI is DOWN: every model in the chain failed.")
        return 1
    note = " (on a BACKUP model)" if status["on_fallback"] else ""
    print(f"AI is up: {status['model']}{note}, {status['latency_ms'] / 1000:.1f} s.")
    if status["slow"]:
        print(f"  SLOW: over {llm.SLOW_MS // 1000} s for one word. Students would wait; pre-warm stories "
              "(scripts\\prewarm_stories.py) before a demo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
