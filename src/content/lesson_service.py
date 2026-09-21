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
from pathlib import Path

from src.content.authored import parse_lesson_file, to_legacy_lesson
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


def find_authored_lesson(concept_id: str, interest: str, fmt: LessonFormat | str) -> Path | None:
    fmt = LessonFormat(fmt).value
    matches = sorted(lessons_dir().glob(f"*/*/{concept_id}/{interest.lower()}__{fmt}.md"))
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


def has_lesson(concept_id: str, interest: str) -> bool:
    """True if any servable lesson exists for this concept + interest."""
    return (
        find_authored_lesson(concept_id, interest, LessonFormat.EXPLAIN) is not None
        or lesson_path(concept_id, interest).exists()
    )
