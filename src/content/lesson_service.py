"""Lesson read-service — serve pre-generated lessons from disk.

The write side is the offline factory (generate_lessons.py); this is the read
side. It loads the cached `data/lessons/{concept_id}__{interest}.json` files
that the factory produced, so the live platform serves vetted lessons instantly
without touching an LLM.

Interest is lower-cased before building the filename, because the factory wrote
files as `position__football.json` while a student profile may carry "Football".
"""

from __future__ import annotations

from pathlib import Path

from src.content.lesson_schema import Lesson

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_LESSONS_DIR = _PROJECT_ROOT / "data" / "lessons"


def lesson_path(concept_id: str, interest: str) -> Path:
    """Return the on-disk path for a (concept, interest) lesson."""
    return _LESSONS_DIR / f"{concept_id}__{interest.lower()}.json"


def get_lesson(concept_id: str, interest: str) -> Lesson | None:
    """Load the pre-generated lesson for a concept + interest.

    Returns the validated Lesson, or None if no lesson file exists for this
    pair (e.g. the concept hasn't been generated for that interest yet).
    """
    path = lesson_path(concept_id, interest)
    if not path.exists():
        return None
    return Lesson.model_validate_json(path.read_text(encoding="utf-8"))


def has_lesson(concept_id: str, interest: str) -> bool:
    """True if a pre-generated lesson exists for this concept + interest."""
    return lesson_path(concept_id, interest).exists()
