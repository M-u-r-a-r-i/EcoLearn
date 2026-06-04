"""Benchmark the analogy generator across 10 concept/interest pairs.

Writes a single Markdown report to tests/benchmark_output.md. A short delay
between calls keeps us under the Gemini free-tier per-minute rate limit.
"""

from __future__ import annotations

import sys
import time
from datetime import datetime
from pathlib import Path

# Make `src` importable when running this script directly.
_PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PROJECT_ROOT))

from google.genai import errors

from src.agents.analogy_generator import generate_explanation


BENCHMARK_CASES = [
    ("Relative velocity",                       "football"),
    ("Relative velocity",                       "gaming"),
    ("Average vs instantaneous velocity",       "football"),
    ("Projectile motion",                       "football"),
    ("Free fall",                               "gaming"),
    ("Work done by a force",                    "football"),
    ("Kinetic energy",                          "gaming"),
    ("Work-energy theorem",                     "football"),
    ("Power",                                   "gaming"),
    ("Conservation of energy",                  "football"),
]

LEVEL = "Class 11"

# Gemini free tier for gemini-2.5-flash caps at 5 requests/minute, so we need
# at least 12 s between calls. 13 s gives a small safety margin.
DELAY_SECONDS = 13

# On a 429 (RESOURCE_EXHAUSTED), back off and retry. The waits escalate so a
# transient minute-window collision recovers quickly, but a hard daily-quota
# wall surfaces after three tries instead of looping forever.
RETRY_WAITS_SECONDS = (30, 60, 90)

OUTPUT_PATH = _PROJECT_ROOT / "tests" / "benchmark_output.md"


def _generate_with_retry(concept: str, interest: str, level: str) -> str:
    """Call the agent; on 429, back off and retry. Reraise any other error."""
    for attempt, wait in enumerate(RETRY_WAITS_SECONDS, start=1):
        try:
            return generate_explanation(concept, interest, level)
        except errors.ClientError as exc:
            if getattr(exc, "code", None) != 429:
                raise
            print(
                f"  [rate-limited, retry {attempt}/{len(RETRY_WAITS_SECONDS)} "
                f"in {wait}s] ",
                end="",
                flush=True,
            )
            time.sleep(wait)
    # Final attempt — let any error propagate.
    return generate_explanation(concept, interest, level)


def _render_case(index: int, total: int, concept: str, interest: str, body: str) -> str:
    return (
        f"## {index}. {concept} — {interest}\n\n"
        f"**Concept:** {concept}  \n"
        f"**Interest:** {interest}  \n"
        f"**Level:** {LEVEL}\n\n"
        f"---\n\n"
        f"{body.strip()}\n\n"
    )


def main() -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sections: list[str] = [
        f"# Analogy Generator Benchmark\n\n"
        f"_Run at {timestamp}. Model: gemini-2.5-flash. Level: {LEVEL}._\n\n"
        f"---\n\n"
    ]

    total = len(BENCHMARK_CASES)
    for i, (concept, interest) in enumerate(BENCHMARK_CASES, start=1):
        print(f"[{i}/{total}] {concept} — {interest} ... ", end="", flush=True)
        try:
            output = _generate_with_retry(concept, interest, LEVEL)
            print("ok")
        except Exception as exc:
            output = f"**[ERROR]** `{type(exc).__name__}`: {exc}"
            print(f"FAILED ({type(exc).__name__})")

        sections.append(_render_case(i, total, concept, interest, output))

        # Don't sleep after the last case.
        if i < total:
            time.sleep(DELAY_SECONDS)

    OUTPUT_PATH.write_text("".join(sections), encoding="utf-8")
    print(f"\nWrote {total} cases to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
