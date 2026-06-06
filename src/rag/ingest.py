"""Ingest curriculum and interest corpora into Chroma collections.

Splits markdown corpora into chunks (preferring section boundaries marked by
`## ` headings), attaches metadata, and persists them into a local Chroma
collection that the rest of the pipeline can query. Uses Chroma's default
embedding function (all-MiniLM-L6-v2 via onnxruntime, fully local — no API
calls needed).
"""

from __future__ import annotations

import re
from pathlib import Path

import chromadb


# Project root = .../EcoLearn/  (this file lives at .../EcoLearn/src/rag/).
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_CHROMA_PATH = _PROJECT_ROOT / "chroma_db"

# Chunk-size targets. We measure in characters using a rough 1 token ≈ 4 chars
# heuristic for English markdown so we don't depend on a tokenizer library.
_TARGET_CHUNK_TOKENS = 250
_OVERLAP_TOKENS = 50
_CHARS_PER_TOKEN = 4
_TARGET_CHUNK_CHARS = _TARGET_CHUNK_TOKENS * _CHARS_PER_TOKEN  # 1000
_OVERLAP_CHARS = _OVERLAP_TOKENS * _CHARS_PER_TOKEN            # 200

# Headings at level 2 (## Heading) delimit passages in our curriculum and
# interest markdown files. Level-1 headings are the document title.
_SECTION_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)


def _split_sections(text: str) -> list[tuple[str, str]]:
    """Return [(heading, body), ...] from a markdown file."""
    matches = list(_SECTION_RE.finditer(text))
    if not matches:
        return [("(no heading)", text.strip())]
    sections: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        heading = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        sections.append((heading, body))
    return sections


def _split_body_into_chunks(body: str) -> list[str]:
    """Fallback splitter for sections too large for one chunk.

    Slides a window of TARGET chars across the body, stepping by
    (TARGET − OVERLAP) so consecutive chunks share OVERLAP chars of context.
    """
    if len(body) <= _TARGET_CHUNK_CHARS:
        return [body]
    chunks: list[str] = []
    step = _TARGET_CHUNK_CHARS - _OVERLAP_CHARS
    start = 0
    while start < len(body):
        end = start + _TARGET_CHUNK_CHARS
        chunk = body[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(body):
            break
        start += step
    return chunks


def _corpus_type_from_dir(corpus_dir: Path) -> str:
    """Infer corpus_type from directory name. Falls back to 'unknown'."""
    name = corpus_dir.name.lower()
    if "curriculum" in name:
        return "curriculum"
    if "interest" in name:
        return "interest"
    return "unknown"


def _safe_id(text: str) -> str:
    """Make a heading safe for use as part of a Chroma ID."""
    cleaned = re.sub(r"\W+", "_", text).strip("_")
    return cleaned[:60] or "section"


def ingest_corpus(corpus_dir: str | Path, collection_name: str) -> int:
    """Ingest all .md files under corpus_dir into a Chroma collection.

    The collection is dropped and recreated each call so re-ingestion is
    deterministic — useful when prompt-tuning the curriculum content.

    Args:
        corpus_dir: Directory containing .md files. The directory name
            determines `corpus_type` metadata ("curriculum" or "interest").
        collection_name: Chroma collection name to (re)create.

    Returns:
        Number of chunks ingested.
    """
    corpus_dir = Path(corpus_dir).resolve()
    if not corpus_dir.is_dir():
        raise FileNotFoundError(f"{corpus_dir} is not a directory.")
    corpus_type = _corpus_type_from_dir(corpus_dir)

    client = chromadb.PersistentClient(path=str(_CHROMA_PATH))
    try:
        client.delete_collection(collection_name)
    except Exception:
        # Collection didn't exist yet — that's fine.
        pass
    collection = client.create_collection(name=collection_name)

    chunk_ids: list[str] = []
    chunk_docs: list[str] = []
    chunk_metas: list[dict] = []

    for md_path in sorted(corpus_dir.rglob("*.md")):
        text = md_path.read_text(encoding="utf-8")
        sections = _split_sections(text)
        # For interest corpora, the interest name is the markdown filename
        # without extension (e.g. "football" from "football.md").
        interest_name = md_path.stem if corpus_type == "interest" else None

        for heading, body in sections:
            for i, chunk in enumerate(_split_body_into_chunks(body)):
                if not chunk:
                    continue
                meta: dict[str, str] = {
                    "source_file": md_path.name,
                    "heading": heading,
                    "corpus_type": corpus_type,
                }
                if interest_name:
                    meta["interest"] = interest_name
                chunk_ids.append(f"{md_path.stem}::{_safe_id(heading)}::{i}")
                chunk_docs.append(chunk)
                chunk_metas.append(meta)

    if chunk_docs:
        # Chroma's default embedding function turns each document string into
        # a vector at add-time. No external API required.
        collection.add(ids=chunk_ids, documents=chunk_docs, metadatas=chunk_metas)

    return len(chunk_docs)
