"""Benchmark v3 — same 10 cases as v2, this time with RAG context fed in.

For each (concept, interest):
  1. Retrieve top curriculum passages with retrieve_concept(concept).
  2. Retrieve top interest passages with retrieve_interest(concept + interest).
  3. Call generate_explanation with both context lists passed in.
  4. Save the retrieved passages AND the generated explanation to the report.

The output file deliberately includes the retrieved context next to each
explanation so we can audit which numbers and examples came from the corpora
versus the model's general knowledge.
"""

from __future__ import annotations

import sys
import time
from datetime import datetime
from pathlib import Path

# Make `src` importable when running directly.
_PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PROJECT_ROOT))

from google.genai import errors  # noqa: E402

from src.agents.analogy_generator import generate_explanation  # noqa: E402
from src.rag.retrieve import retrieve_concept, retrieve_interest  # noqa: E402


BENCHMARK_CASES = [
    ("Relative velocity",                  "football"),
    ("Relative velocity",                  "gaming"),
    ("Average vs instantaneous velocity",  "football"),
    ("Projectile motion",                  "football"),
    ("Free fall",                          "gaming"),
    ("Work done by a force",               "football"),
    ("Kinetic energy",                     "gaming"),
    ("Work-energy theorem",                "football"),
    ("Power",                              "gaming"),
    ("Conservation of energy",             "football"),
]

LEVEL = "Class 11"
TOP_K = 3
DELAY_SECONDS = 13            # Stay under generator's per-minute quota.
RETRY_WAITS_SECONDS = (30, 60, 90)

OUTPUT_PATH = _PROJECT_ROOT / "tests" / "benchmark_v3_output.md"


def _generate_with_retry(
    concept: str,
    interest: str,
    level: str,
    curriculum_passages: list[str],
    interest_passages: list[str],
) -> str:
    """Call the generator; on 429, back off and retry. Reraise other errors."""
    for attempt, wait in enumerate(RETRY_WAITS_SECONDS, start=1):
        try:
            return generate_explanation(
                concept=concept,
                interest=interest,
                level=level,
                sub_interest_facts=interest_passages,
                curriculum_context=curriculum_passages,
            )
        except errors.ClientError as exc:
            if getattr(exc, "code", None) != 429:
                raise
            print(
                f"  [rate-limited, retry {attempt}/{len(RETRY_WAITS_SECONDS)} "
                f"in {wait}s]",
                flush=True,
            )
            time.sleep(wait)
    return generate_explanation(
        concept=concept,
        interest=interest,
        level=level,
        sub_interest_facts=interest_passages,
        curriculum_context=curriculum_passages,
    )


def _retrieve_for(concept: str, interest: str) -> tuple[list[dict], list[dict]]:
    curriculum_hits = retrieve_concept(concept, n_results=TOP_K)
    interest_query = f"{concept} {interest}".strip()
    interest_hits = retrieve_interest(interest_query, interest, n_results=TOP_K)
    return curriculum_hits, interest_hits


def _render_hits(label: str, hits: list[dict]) -> list[str]:
    lines = [f"**Retrieved {label} (top {TOP_K}):**", ""]
    for i, h in enumerate(hits, start=1):
        meta = h.get("metadata", {})
        source = meta.get("source_file", "?")
        heading = meta.get("heading", "?")
        dist = h.get("distance")
        dist_s = f"{dist:.3f}" if isinstance(dist, (int, float)) else "?"
        lines.append(f"{i}. `{source} :: {heading}` (distance {dist_s})")
    lines.append("")
    return lines


def _render_case(
    index: int,
    concept: str,
    interest: str,
    curriculum_hits: list[dict],
    interest_hits: list[dict],
    output: str,
) -> str:
    lines = [
        f"## {index}. {concept} — {interest}",
        "",
        f"**Concept:** {concept}  ",
        f"**Interest:** {interest}  ",
        f"**Level:** {LEVEL}",
        "",
        "---",
        "",
    ]
    lines.extend(_render_hits("curriculum context", curriculum_hits))
    lines.extend(_render_hits("interest context", interest_hits))
    lines.extend(["---", "", "**Generated explanation:**", "", output.strip(), "", ""])
    return "\n".join(lines)


def main() -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sections: list[str] = [
        "# Analogy Generator Benchmark — v3 (with RAG context)\n\n"
        f"_Run at {timestamp}. Each case is fed the top {TOP_K} curriculum "
        f"passages plus the top {TOP_K} interest passages as context, then "
        "asked to generate the explanation. Critic loop is intentionally "
        "disabled here so the diff against v2 isolates the RAG effect._\n\n"
        "---\n\n",
    ]

    total = len(BENCHMARK_CASES)
    for i, (concept, interest) in enumerate(BENCHMARK_CASES, start=1):
        print(f"[{i}/{total}] {concept} — {interest}")
        try:
            curriculum_hits, interest_hits = _retrieve_for(concept, interest)
            curriculum_passages = [h["text"] for h in curriculum_hits if h.get("text")]
            interest_passages = [h["text"] for h in interest_hits if h.get("text")]
            print(
                f"  RAG: {len(curriculum_passages)} curriculum + "
                f"{len(interest_passages)} interest passages"
            )
            output = _generate_with_retry(
                concept, interest, LEVEL, curriculum_passages, interest_passages,
            )
            print("  ok")
        except Exception as exc:
            print(f"  FAILED ({type(exc).__name__}): {exc}")
            curriculum_hits, interest_hits = [], []
            output = f"**[ERROR]** `{type(exc).__name__}`: {exc}"

        sections.append(
            _render_case(i, concept, interest, curriculum_hits, interest_hits, output)
        )

        if i < total:
            time.sleep(DELAY_SECONDS)

    OUTPUT_PATH.write_text("".join(sections), encoding="utf-8")
    print(f"\nWrote {total} cases to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
