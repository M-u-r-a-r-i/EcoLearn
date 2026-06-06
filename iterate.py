"""Single-case pipeline runner for prompt iteration.

Run one concept through the generator+critic loop and print the result. Use
this while editing prompts/analogy_generator.txt or prompts/critic.txt: tweak,
run, read, repeat. Cheaper than the full 5-case test_pipeline.py.

Usage:
    python iterate.py "relative velocity" football
    python iterate.py "projectile motion" football --retries 1
    python iterate.py "kinetic energy" gaming --level "Class 12"
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(_PROJECT_ROOT))

from src.pipeline import explain_with_review


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("concept", help="e.g. 'relative velocity'")
    parser.add_argument("interest", help="e.g. 'football'")
    parser.add_argument("--level", default="Class 11")
    parser.add_argument("--retries", type=int, default=2)
    args = parser.parse_args()

    result = explain_with_review(
        concept=args.concept,
        interest=args.interest,
        level=args.level,
        max_retries=args.retries,
    )

    print()
    print("=" * 78)
    print("FINAL EXPLANATION")
    print("=" * 78)
    print(result["explanation"].strip())

    print()
    print("=" * 78)
    print("METADATA")
    print("=" * 78)
    print(f"verdict:  {result['verdict']}")
    print(f"attempts: {result['attempts']}")
    print("critique:")
    print(json.dumps(result["critique"], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
