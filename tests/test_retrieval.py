"""Smoke test for the RAG retrieval functions.

Runs four sample queries — two against the curriculum collection, two against
the interest collection (filtered) — and prints the top passages with their
distances. Use this to sanity-check that semantic search is surfacing the
passages a human would expect.

Lower distance = more semantically similar. The all-MiniLM-L6-v2 default is
cosine-based, so distances roughly span 0 (identical) to 2 (orthogonal).
"""

from __future__ import annotations

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PROJECT_ROOT))

from src.rag.retrieve import retrieve_concept, retrieve_interest


_BAR = "=" * 78


def _print_results(title: str, results: list[dict]) -> None:
    print(_BAR)
    print(title)
    print(_BAR)
    if not results:
        print("(no results)\n")
        return
    for i, r in enumerate(results, start=1):
        meta = r["metadata"]
        heading = meta.get("heading", "(no heading)")
        source = meta.get("source_file", "(no file)")
        distance = r["distance"]
        snippet = r["text"][:280] + ("..." if len(r["text"]) > 280 else "")
        print()
        print(f"[{i}] distance={distance:.4f}  |  {source}  ::  {heading}")
        print(snippet)
    print()


def main() -> None:
    q1 = "how to calculate relative velocity"
    _print_results(f"CONCEPT QUERY: {q1!r}", retrieve_concept(q1))

    q2 = "what is kinetic energy"
    _print_results(f"CONCEPT QUERY: {q2!r}", retrieve_concept(q2))

    q3 = "defender chasing attacker speed"
    _print_results(
        f"INTEREST QUERY [football]: {q3!r}",
        retrieve_interest(q3, "football"),
    )

    q4 = "racing game acceleration physics"
    _print_results(
        f"INTEREST QUERY [gaming]: {q4!r}",
        retrieve_interest(q4, "gaming"),
    )


if __name__ == "__main__":
    main()
