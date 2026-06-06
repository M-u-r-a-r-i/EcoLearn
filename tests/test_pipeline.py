"""End-to-end pipeline test across 5 concepts.

Runs explain_with_review on five (concept, interest) pairs and saves the final
explanation, verdict, and retry count for each to tests/pipeline_output.md.

This is the canonical demonstration that Generator + Critic + retry-loop work
together — running it should show the agents collaborating in real time.

Cost note: each pipeline run is at least one generator call + one critic call,
and up to three of each on a FAIL → retry → retry sequence. With 5 cases this
can mean ~30 API calls in the worst case. The pipeline spaces calls at >12 s
to stay under free-tier rate limits, so a full run takes several minutes.
"""

from __future__ import annotations

import sys
import time
from datetime import datetime
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PROJECT_ROOT))

from src.pipeline import explain_with_review


CASES = [
    ("Relative velocity",      "football"),
    ("Projectile motion",      "football"),
    ("Work-energy theorem",    "gaming"),
    ("Conservation of energy", "football"),
    ("Free fall",              "gaming"),
]

LEVEL = "Class 11"
MAX_RETRIES = 2
INTER_CASE_DELAY_SECONDS = 13

OUTPUT_PATH = _PROJECT_ROOT / "tests" / "pipeline_output.md"


def _render_section(
    index: int,
    total: int,
    concept: str,
    interest: str,
    result: dict,
) -> str:
    verdict = result.get("verdict", "ERROR")
    attempts = result.get("attempts", "?")
    critique_dict = result.get("critique", {})
    feedback = critique_dict.get("feedback", "")
    explanation = result.get("explanation", "").strip()

    lines = [
        f"## {index}. {concept} — {interest}",
        "",
        f"**Concept:** {concept}  ",
        f"**Interest:** {interest}  ",
        f"**Level:** {LEVEL}  ",
        f"**Final verdict:** `{verdict}`  ",
        f"**Attempts:** {attempts} of {1 + MAX_RETRIES} allowed",
        "",
        "**Critic axes (final attempt):**",
        f"- scientific_correctness: `{critique_dict.get('scientific_correctness')}`",
        f"- pedagogical_fit: `{critique_dict.get('pedagogical_fit')}`",
        f"- analogical_integrity: `{critique_dict.get('analogical_integrity')}`",
        "",
    ]
    if feedback:
        lines.extend(["**Final critic feedback:**", "", f"> {feedback}", ""])
    lines.extend(["---", "", "**Final explanation:**", "", explanation, "", ""])
    return "\n".join(lines)


def main() -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sections: list[str] = [
        "# Pipeline Output — Generator + Critic Loop\n\n"
        f"_Run at {timestamp}. Max retries per case: {MAX_RETRIES}._\n\n"
        "---\n\n"
    ]
    total = len(CASES)
    for i, (concept, interest) in enumerate(CASES, start=1):
        print()
        print("#" * 78)
        print(f"### CASE {i}/{total}: {concept} — {interest}")
        print("#" * 78)
        try:
            result = explain_with_review(
                concept=concept,
                interest=interest,
                level=LEVEL,
                max_retries=MAX_RETRIES,
            )
        except Exception as exc:
            print(f"[CASE {i}] crashed: {type(exc).__name__}: {exc}")
            result = {
                "explanation": f"[ERROR] {type(exc).__name__}: {exc}",
                "verdict": "ERROR",
                "attempts": 0,
                "critique": {},
                "history": [],
            }
        sections.append(_render_section(i, total, concept, interest, result))

        if i < total:
            time.sleep(INTER_CASE_DELAY_SECONDS)

    OUTPUT_PATH.write_text("".join(sections), encoding="utf-8")
    print(f"\nWrote {total} cases to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
