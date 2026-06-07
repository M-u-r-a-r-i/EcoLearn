"""Query the local Chroma index for concept passages and interest passages.

Used by the analogy pipeline to ground generation in real curriculum and
interest content. Both retrieval functions return a flat list of
{text, metadata, distance} dicts so callers don't need to know about
Chroma's nested response shape.
"""

from __future__ import annotations

from pathlib import Path

import chromadb


# Project root = .../EcoLearn/  (this file lives at .../EcoLearn/src/rag/).
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_CHROMA_PATH = _PROJECT_ROOT / "chroma_db"

_CURRICULUM_COLLECTION = "curriculum"
_INTERESTS_COLLECTION = "interests"


def _get_client() -> "chromadb.PersistentClient":
    return chromadb.PersistentClient(path=str(_CHROMA_PATH))


def _format_results(raw: dict) -> list[dict]:
    """Flatten Chroma's nested query response into [{text, metadata, distance}]."""
    docs = (raw.get("documents") or [[]])[0]
    metas = (raw.get("metadatas") or [[]])[0]
    dists = (raw.get("distances") or [[]])[0]
    results: list[dict] = []
    for doc, meta, dist in zip(docs, metas, dists):
        results.append({
            "text": doc,
            "metadata": meta or {},
            "distance": dist,
        })
    return results


def retrieve_concept(query: str, n_results: int = 3) -> list[dict]:
    """Return the top-n curriculum passages most semantically similar to `query`.

    Args:
        query: Natural-language question or concept name.
        n_results: How many passages to return.

    Returns:
        List of {text, metadata, distance} dicts, sorted by ascending distance
        (i.e., most similar first).
    """
    client = _get_client()
    collection = client.get_collection(name=_CURRICULUM_COLLECTION)
    raw = collection.query(query_texts=[query], n_results=n_results)
    return _format_results(raw)


def retrieve_interest(
    query: str,
    interest_name: str,
    n_results: int = 3,
) -> list[dict]:
    """Return the top-n interest passages, filtered to one interest.

    Uses Chroma's `where` metadata filter so only passages tagged with
    interest = <interest_name> are considered. This prevents football queries
    from accidentally returning gaming passages (or vice versa).

    Args:
        query: Natural-language question relevant to the student's interest.
        interest_name: Which interest corpus to search ("football", "gaming").
        n_results: How many passages to return.

    Returns:
        List of {text, metadata, distance} dicts, sorted by ascending distance.
    """
    client = _get_client()
    collection = client.get_collection(name=_INTERESTS_COLLECTION)
    raw = collection.query(
        query_texts=[query],
        n_results=n_results,
        where={"interest": interest_name},
    )
    return _format_results(raw)
