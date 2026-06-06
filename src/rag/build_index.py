"""Build the local Chroma index from the curriculum and interest corpora.

Run this once after the corpora are written or modified. The index is
persisted under ./chroma_db so subsequent processes can query it without
re-embedding.
"""

from __future__ import annotations

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_PROJECT_ROOT))

from src.rag.ingest import ingest_corpus


def main() -> None:
    curriculum_dir = _PROJECT_ROOT / "src" / "data" / "curriculum"
    interest_dir = _PROJECT_ROOT / "src" / "data" / "interests"

    print(f"Ingesting curriculum from {curriculum_dir} ...")
    curriculum_count = ingest_corpus(curriculum_dir, "curriculum")
    print(f"  ingested {curriculum_count} chunks into 'curriculum' collection")

    print(f"Ingesting interests from {interest_dir} ...")
    interest_count = ingest_corpus(interest_dir, "interests")
    print(f"  ingested {interest_count} chunks into 'interests' collection")

    print()
    print(f"Total chunks indexed: {curriculum_count + interest_count}")
    print(f"Persisted to: {_PROJECT_ROOT / 'chroma_db'}")


if __name__ == "__main__":
    main()
