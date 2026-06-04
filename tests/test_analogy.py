"""Smoke test for the analogy generator agent.

Runs three (concept, interest, level) cases and prints each response with a
clear separator so the outputs are easy to scan.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make `src` importable when running this script directly (no package install).
_PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PROJECT_ROOT))

from src.agents.analogy_generator import generate_explanation


TEST_CASES = [
    ("relative velocity", "football", "Class 11"),
    ("work-energy theorem", "gaming", "Class 11"),
    ("kinematic equations", "football", "Class 11"),
]


def _banner(title: str) -> str:
    bar = "=" * 78
    return f"\n{bar}\n{title}\n{bar}"


def main() -> None:
    for i, (concept, interest, level) in enumerate(TEST_CASES, start=1):
        header = f"TEST {i}/{len(TEST_CASES)}  |  concept='{concept}'  interest='{interest}'  level='{level}'"
        print(_banner(header))
        try:
            output = generate_explanation(concept, interest, level)
        except Exception as exc:
            print(f"[ERROR] {type(exc).__name__}: {exc}")
            continue
        print(output.strip())
    print()


if __name__ == "__main__":
    main()
