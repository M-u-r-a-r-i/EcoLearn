"""Lesson read-service — serve lessons from disk, never from an LLM.

Two sources, checked in this order:

1. **Authored lessons** (Markdown, one per concept × interest × format) at
   `data/lessons/{grade}/{chapter_id}/{concept_id}/{interest}__{format}.md`,
   written by Claude Code sessions. See `src/content/authored.py`.
2. **Legacy factory lessons** (JSON, one per concept × interest) at
   `data/lessons/{concept_id}__{interest}.json`, produced by the old
   generate → critique pipeline (generate_lessons.py).

`get_lesson` returns the legacy `Lesson` shape either way, so today's UIs keep
working; `get_authored_lesson` exposes the richer multi-format lesson.

Interest is lower-cased before building a filename, because files are written
as `position__football.json` while a student profile may carry "Football".
The lessons directory can be redirected with `ECOLEARN_LESSONS_DIR` (read
lazily, like the progress store's DB path) so tests never touch real content.
"""

from __future__ import annotations

import os
import time
from pathlib import Path

from src.content.authored import parse_lesson_file, student_view, to_legacy_lesson
from src.content.lesson_schema import AuthoredLesson, Lesson, LessonFormat

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_LESSONS_DIR = _PROJECT_ROOT / "data" / "lessons"


def lessons_dir() -> Path:
    raw = os.getenv("ECOLEARN_LESSONS_DIR")
    return Path(raw) if raw else _DEFAULT_LESSONS_DIR


# ---------------------------------------------------------------------------
# Legacy factory lessons (JSON)
# ---------------------------------------------------------------------------

def lesson_path(concept_id: str, interest: str) -> Path:
    """Return the on-disk path for a legacy (concept, interest) JSON lesson."""
    return lessons_dir() / f"{concept_id}__{interest.lower()}.json"


# ---------------------------------------------------------------------------
# Authored lessons (Markdown)
# ---------------------------------------------------------------------------

def authored_lesson_path(
    grade: int, chapter_id: str, concept_id: str, interest: str, fmt: LessonFormat | str
) -> Path:
    """Where an authored lesson must live. Concept ids are unique across the
    whole subject, so the grade/chapter directories are for humans browsing
    thousands of files — lookup only needs the concept id."""
    fmt = LessonFormat(fmt).value
    return lessons_dir() / str(grade) / chapter_id / concept_id / f"{interest.lower()}__{fmt}.md"


def _lesson_index() -> dict[tuple[str, str], Path]:
    """{(concept_id, "interest__format"): path} for every authored lesson.

    One directory walk instead of one glob per lookup (a student's journey did
    ~850 of those). Shares the short cache of the other scans, so a newly
    written lesson appears within seconds.
    """
    key = ("index", str(lessons_dir()), "")
    now = time.monotonic()
    hit = _scan_cache.get(key)
    if hit is not None and now - hit[0] < _SCAN_TTL_SECONDS:
        return hit[1]  # type: ignore[return-value]
    index: dict[tuple[str, str], Path] = {}
    for path in sorted(lessons_dir().glob("*/*/*/*.md")):
        index.setdefault((path.parent.name, path.stem), path)
    _scan_cache[key] = (now, index)  # type: ignore[assignment]
    return index


def find_authored_lesson(concept_id: str, interest: str, fmt: LessonFormat | str) -> Path | None:
    fmt = LessonFormat(fmt).value
    name = f"{interest.lower()}__{fmt}"
    hit = _lesson_index().get((concept_id, name))
    if hit is not None and hit.exists():
        return hit
    # A miss is never trusted from the cache: a writing session may have just
    # added this lesson. One direct look on disk; if it's there now, the index
    # is stale, so drop it.
    matches = sorted(lessons_dir().glob(f"*/*/{concept_id}/{name}.md"))
    if matches:
        _scan_cache.clear()
    return matches[0] if matches else None


def get_authored_lesson(
    concept_id: str, interest: str, fmt: LessonFormat | str = LessonFormat.EXPLAIN
) -> AuthoredLesson | None:
    """Load one authored lesson, or None if it hasn't been written yet."""
    path = find_authored_lesson(concept_id, interest, fmt)
    return parse_lesson_file(path) if path else None


def available_formats(concept_id: str, interest: str) -> list[str]:
    """Which formats exist on disk for this concept × interest, in canonical order."""
    return [f.value for f in LessonFormat if find_authored_lesson(concept_id, interest, f)]


# ---------------------------------------------------------------------------
# The serving entry points
# ---------------------------------------------------------------------------

def get_lesson(concept_id: str, interest: str) -> Lesson | None:
    """Load the lesson for a concept + interest in the legacy `Lesson` shape.

    Prefers the authored "explain" lesson, falls back to the legacy JSON, and
    returns None if neither exists yet.
    """
    authored = get_authored_lesson(concept_id, interest, LessonFormat.EXPLAIN)
    if authored is not None:
        return to_legacy_lesson(authored)
    path = lesson_path(concept_id, interest)
    if not path.exists():
        return None
    return Lesson.model_validate_json(path.read_text(encoding="utf-8"))


def chapters_with_lessons(interest: str) -> set[str]:
    """Which chapter ids have at least one authored lesson for this interest.

    One glob over `data/lessons/{grade}/{chapter}/{concept}/{interest}__*.md`,
    so it stays cheap as the corpus grows. Used to tell a student how much of
    the syllabus their interest covers before they pick it.
    """
    pattern = f"*/*/*/{interest.lower()}__*.md"
    return _scanned("chapters", interest,
                    lambda: {path.parents[1].name for path in lessons_dir().glob(pattern)})


# Directory scans are cached briefly: the load test (2026-10-02) found ~900
# globs in one student's journey. Lessons are added by writing sessions, not by
# students, so a new lesson showing up within 30 seconds is plenty.
_SCAN_TTL_SECONDS = 30.0
_scan_cache: dict[tuple[str, str, str], tuple[float, set[str]]] = {}


def _scanned(kind: str, interest: str, scan) -> set[str]:
    key = (kind, str(lessons_dir()), interest.lower())
    now = time.monotonic()
    hit = _scan_cache.get(key)
    if hit is not None and now - hit[0] < _SCAN_TTL_SECONDS:
        return set(hit[1])
    value = scan()
    _scan_cache[key] = (now, value)
    return set(value)


def concepts_with_lessons(interest: str) -> set[str]:
    """Every concept id a student with this interest can actually be served.

    The same rule as `has_lesson` (an authored "explain" lesson, or a legacy
    JSON one), but for the whole syllabus in two globs instead of one lookup
    per concept — the chapter picker needs all 249 answers at once. Cached for
    a few seconds (see `_scanned`).
    """
    return _scanned("concepts", interest, lambda: _scan_concepts(interest))


def _scan_concepts(interest: str) -> set[str]:
    interest = interest.lower()
    authored = {p.parent.name for p in lessons_dir().glob(f"*/*/*/{interest}__explain.md")}
    suffix = f"__{interest}"
    legacy = {p.stem[: -len(suffix)] for p in lessons_dir().glob(f"*{suffix}.json")}
    return authored | legacy


def has_lesson(concept_id: str, interest: str) -> bool:
    """True if any servable lesson exists for this concept + interest."""
    return (
        find_authored_lesson(concept_id, interest, LessonFormat.EXPLAIN) is not None
        or lesson_path(concept_id, interest).exists()
    )
