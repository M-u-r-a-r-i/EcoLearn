"""The starting check: which questions a student gets, and how they're graded.

The questions are existing lesson checks (see data/diagnostic.yaml for how
they're chosen), so grading is the same answer-key lookup as a lesson check,
and each wrong option already names the misconception it reveals. "Not sure"
is a first-class answer: a guess would plant a misconception the student
doesn't hold, so we'd rather know they don't know.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from src.content import lesson_service
from src.errors import EcoLearnError
from src.path import engine

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_CONFIG_PATH = _PROJECT_ROOT / "data" / "diagnostic.yaml"

UNSURE = "unsure"
MAX_HOBBIES = 8
MAX_OWN_HOBBIES = 2
# A hobby of the student's own: a short label, letters and a few separators
# only, so nothing that reads like a sentence about a child is stored.
_OWN_HOBBY_RE = re.compile(r"^[A-Za-z][A-Za-z &'\-]{1,23}$")


def load_config() -> dict[str, Any]:
    return yaml.safe_load(_CONFIG_PATH.read_text(encoding="utf-8"))


def _grade_key(level: str, config: dict[str, Any]) -> str:
    """'Class 12' -> 'Class 12'; anything unknown falls back to Class 11."""
    return level if level in config["questions"] else "Class 11"


def choose_questions(level: str, interest: str) -> list[dict[str, str]]:
    """[{concept_id, source_interest}] for this student, in teaching order.

    Each question comes from the first interest in `source_interests` that is
    not the student's own and has that lesson written. A concept with no such
    lesson is skipped rather than failing the whole check.
    """
    config = load_config()
    own = (interest or "").lower()
    chosen = []
    for concept_id in config["questions"][_grade_key(level, config)]:
        source = next(
            (i for i in config["source_interests"]
             if i != own and lesson_service.get_authored_lesson(concept_id, i) is not None),
            None,
        )
        if source is not None:
            chosen.append({"concept_id": concept_id, "source_interest": source})
    order = {c["concept_id"]: (engine.find_concept(c["concept_id"]).order) for c in chosen}
    return sorted(chosen, key=lambda c: order[c["concept_id"]])


def student_questions(level: str, interest: str) -> list[dict[str, Any]]:
    """The questions as the browser may see them: no answers, no misconceptions."""
    chapter_names = {c["id"]: c["name"] for c in engine.list_chapters()}
    out = []
    for q in choose_questions(level, interest):
        lesson = lesson_service.get_authored_lesson(q["concept_id"], q["source_interest"])
        view = lesson_service.student_view(lesson)["check"]
        concept = engine.find_concept(q["concept_id"])
        out.append({
            "concept_id": q["concept_id"],
            "concept_name": concept.name,
            "chapter_name": chapter_names.get(concept.chapter_id),
            "question": view["question"],
            "options": view["options"],
        })
    return out


def grade(level: str, interest: str, picks: dict[str, str]) -> list[dict[str, Any]]:
    """Grade a whole check. Unanswered questions count as "not sure".

    Raises:
        EcoLearnError: an answer for a concept that wasn't in this student's
                       check, or a pick that isn't an option or "unsure".
    """
    questions = choose_questions(level, interest)
    asked = {q["concept_id"] for q in questions}
    extra = sorted(set(picks) - asked)
    if extra:
        raise EcoLearnError(f"These weren't in your check: {', '.join(extra)}.")

    graded = []
    for q in questions:
        check = lesson_service.get_authored_lesson(q["concept_id"], q["source_interest"]).check
        raw = (picks.get(q["concept_id"]) or UNSURE).strip()
        pick = UNSURE if raw.lower() == UNSURE else raw.upper()
        if pick != UNSURE and pick not in check.options:
            raise EcoLearnError(f"Pick one of {', '.join(check.options)} or 'unsure' — got {raw!r}.")
        correct = None if pick == UNSURE else pick == check.answer
        graded.append({
            "concept_id": q["concept_id"],
            "source_interest": q["source_interest"],
            "selected": pick,
            "correct": correct,
            "misconception": (
                ((check.misconceptions.get(pick) or "").strip() or None)
                if correct is False else None
            ),
        })
    return graded


def hobby_options() -> list[dict[str, str]]:
    return load_config()["hobbies"]


def clean_hobbies(hobbies: list[str] | None) -> list[str]:
    """Validate hobbies: ids from the list, plus up to two short labels of the
    student's own (stored lower-case).

    Raises:
        EcoLearnError: too many, or an own label that isn't a short plain word.
    """
    known = {h["id"] for h in hobby_options()}
    picked: list[str] = []
    own = 0
    for raw in hobbies or []:
        value = (raw or "").strip()
        if not value:
            continue
        if value in known:
            item = value
        else:
            if not _OWN_HOBBY_RE.match(value):
                raise EcoLearnError(
                    "Hobbies of your own must be short: letters and spaces, up to 24 characters."
                )
            own += 1
            item = value.lower()
        if item not in picked:
            picked.append(item)
    if own > MAX_OWN_HOBBIES:
        raise EcoLearnError(f"Add at most {MAX_OWN_HOBBIES} hobbies of your own.")
    if len(picked) > MAX_HOBBIES:
        raise EcoLearnError(f"Pick at most {MAX_HOBBIES} hobbies.")
    return picked
