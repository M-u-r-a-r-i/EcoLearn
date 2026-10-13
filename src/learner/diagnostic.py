"""The starting check: which questions a student gets, and how they're graded.

The questions are existing lesson checks (see data/diagnostic.yaml for how
they're chosen), so grading is the same answer-key lookup as a lesson check,
and each wrong option already names the misconception it reveals. "Not sure"
is a first-class answer: a guess would plant a misconception the student
doesn't hold, so we'd rather know they don't know.

The END CHECK (2026-10-02) asks the same concepts again at the end of the
pilot, each with a PARALLEL question: the same concept's check from another
interest's lesson. Two forms are counterbalanced: half the students (by a hash
of their id) get form A at the start and B at the end, the other half the
reverse, so a before -> after gain can't just be one form being easier.
Neither form is ever the student's own interest, whose check they meet in
their lesson.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

import yaml

from src.content import lesson_service
from src.errors import EcoLearnError
from src.file_cache import cached_parse
from src.path import engine

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_CONFIG_PATH = _PROJECT_ROOT / "data" / "diagnostic.yaml"

UNSURE = "unsure"
# "How sure are you?" after picking an option (2026-10-02). Confident and wrong
# is the clearest sign of a real misconception; guessing and wrong may be noise.
CONFIDENCE_LEVELS = ("sure", "think", "guess")
MAX_HOBBIES = 8
MAX_OWN_HOBBIES = 2
# A hobby of the student's own: a short label, letters and a few separators
# only, so nothing that reads like a sentence about a child is stored.
_OWN_HOBBY_RE = re.compile(r"^[A-Za-z][A-Za-z &'\-]{1,23}$")
# A label that reaches the story AI and is shown to the student as "their hobby", so it must be
# suitable for school. A deterministic block, because a red-team run (scripts/redteam_stories.py,
# 2026-10-13) showed the writer and critic alone let "dating" through to a story and put "online casino"
# over a badminton one. This list is a floor, not a filter that can be complete: the critic is the
# second layer, and a teacher can hide any story.
_UNSUITABLE_HOBBY_RE = re.compile(
    r"(?<![a-z])(gambl|bet(s|ting)?(?![a-z])|casino|poker|lotter|vap(e|es|ing)(?![a-z])|smok|cigar|drug|weed(?![a-z])|"
    r"alcohol|beer|wine(?![a-z])|whisk|vodka|drunk|bomb|weapon|guns?(?![a-z])|sex|porn|nude|dating|kiss|"
    r"kill|suicid|self.?harm|hurt.?my|ignore|instruction|prompt|jailbreak)", re.IGNORECASE)


def load_config() -> dict[str, Any]:
    """data/diagnostic.yaml, parsed once per version of the file. Shared: read-only."""
    return cached_parse(_CONFIG_PATH, lambda p: yaml.safe_load(p.read_text(encoding="utf-8")),
                        "diagnostic")


def _grade_key(level: str, config: dict[str, Any]) -> str:
    """'Class 12' -> 'Class 12'; anything unknown falls back to Class 11."""
    return level if level in config["questions"] else "Class 11"


def form_for(student_id: str) -> int:
    """0 or 1: which question form this student gets at the start (the other at the end).

    A hash, not random(), so it is stable across requests and restarts and
    splits a class roughly in half.
    """
    return hashlib.sha256(student_id.encode("utf-8")).digest()[0] & 1


def _forms(concept_id: str, own: str) -> list[str]:
    """The interests whose lesson check can be asked for this concept, in
    `source_interests` order: never the student's own, and only written ones."""
    return [i for i in load_config()["source_interests"]
            if i != own and lesson_service.get_authored_lesson(concept_id, i) is not None]


def _in_teaching_order(chosen: list[dict[str, str]]) -> list[dict[str, str]]:
    order = {c["concept_id"]: engine.find_concept(c["concept_id"]).order for c in chosen}
    return sorted(chosen, key=lambda c: order[c["concept_id"]])


def choose_questions(level: str, interest: str, form: int = 0) -> list[dict[str, str]]:
    """[{concept_id, source_interest}] for the starting check, in teaching order.

    Each question comes from an interest that is not the student's own and has
    that lesson written: the first such in `source_interests` for form 0, the
    second for form 1 (or the first, when there is only one). A concept with no
    such lesson is skipped rather than failing the whole check.
    """
    config = load_config()
    own = (interest or "").lower()
    chosen = []
    for concept_id in config["questions"][_grade_key(level, config)]:
        forms = _forms(concept_id, own)
        if forms:
            chosen.append({"concept_id": concept_id, "source_interest": forms[form % len(forms)]})
    return _in_teaching_order(chosen)


def choose_end_questions(interest: str, start_rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    """The end check: every concept of the student's starting check, asked from
    an interest that is neither their own nor the one used at the start.

    Built from the stored starting-check rows (not the config), so the two
    checks pair up concept for concept even if the config changes later. A
    concept with no parallel question is left out: it can't be compared fairly.
    """
    own = (interest or "").lower()
    chosen = []
    for row in start_rows:
        forms = [i for i in _forms(row["concept_id"], own) if i != row["source_interest"]]
        if forms:
            chosen.append({"concept_id": row["concept_id"], "source_interest": forms[0]})
    return _in_teaching_order(chosen)


def present(chosen: list[dict[str, str]]) -> list[dict[str, Any]]:
    """The questions as the browser may see them: no answers, no misconceptions."""
    chapter_names = {c["id"]: c["name"] for c in engine.list_chapters()}
    out = []
    for q in chosen:
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


def student_questions(level: str, interest: str, form: int = 0) -> list[dict[str, Any]]:
    """The starting check as the browser may see it."""
    return present(choose_questions(level, interest, form))


def clean_confidence(value: str | None) -> str | None:
    """sure | think | guess, or None when not given.

    Raises:
        EcoLearnError: anything else.
    """
    if value is None or not str(value).strip():
        return None
    level = str(value).strip().lower()
    if level not in CONFIDENCE_LEVELS:
        raise EcoLearnError(f"How sure: one of {', '.join(CONFIDENCE_LEVELS)} — got {value!r}.")
    return level


def grade_chosen(
    chosen: list[dict[str, str]],
    picks: dict[str, str],
    confidence: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Grade answers to these questions. Unanswered questions count as "not sure".

    `confidence` maps concept_id -> sure | think | guess. It is kept only for a
    picked option: "not sure" already says how sure the student is.

    Raises:
        EcoLearnError: an answer (or confidence) for a concept that wasn't
                       asked, a pick that isn't an option or "unsure", or a
                       confidence that isn't one of the levels.
    """
    confidence = confidence or {}
    asked = {q["concept_id"] for q in chosen}
    extra = sorted((set(picks) | set(confidence)) - asked)
    if extra:
        raise EcoLearnError(f"These weren't in your check: {', '.join(extra)}.")

    graded = []
    for q in chosen:
        check = lesson_service.get_authored_lesson(q["concept_id"], q["source_interest"]).check
        raw = (picks.get(q["concept_id"]) or UNSURE).strip()
        pick = UNSURE if raw.lower() == UNSURE else raw.upper()
        if pick != UNSURE and pick not in check.options:
            raise EcoLearnError(f"Pick one of {', '.join(check.options)} or 'unsure' — got {raw!r}.")
        correct = None if pick == UNSURE else pick == check.answer
        sure = clean_confidence(confidence.get(q["concept_id"]))
        graded.append({
            "concept_id": q["concept_id"],
            "source_interest": q["source_interest"],
            "selected": pick,
            "correct": correct,
            "confidence": None if pick == UNSURE else sure,
            "misconception": (
                ((check.misconceptions.get(pick) or "").strip() or None)
                if correct is False else None
            ),
        })
    return graded


def grade(
    level: str,
    interest: str,
    picks: dict[str, str],
    form: int = 0,
    confidence: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Grade a whole starting check (see grade_chosen)."""
    return grade_chosen(choose_questions(level, interest, form), picks, confidence)


def _outcome(correct: bool | None) -> str:
    return "right" if correct else ("unsure" if correct is None else "mix_up")


def compare(
    start_rows: list[dict[str, Any]], end_rows: list[dict[str, Any]], studied: set[str]
) -> dict[str, Any]:
    """One student's before -> after, over the concepts asked in BOTH checks.

    `studied`: concepts whose lesson the student opened or answered. Concepts
    they didn't study are a rough control: if those improve as much as the
    studied ones, the gain isn't the lessons'.

    Returns {paired, before: {right, mix_up, unsure}, after: {...}, fixed
    (mix-up -> right), learned (not sure -> right), slipped (right -> not
    right), concepts: [{concept_id, before, after, studied}]}.
    """
    before = {r["concept_id"]: r for r in start_rows}
    concepts = []
    for row in end_rows:
        start = before.get(row["concept_id"])
        if start is None:
            continue
        concepts.append({"concept_id": row["concept_id"],
                         "before": _outcome(start["correct"]),
                         "after": _outcome(row["correct"]),
                         "studied": row["concept_id"] in studied})

    def tally(key: str) -> dict[str, int]:
        return {k: sum(1 for c in concepts if c[key] == k) for k in ("right", "mix_up", "unsure")}

    return {
        "paired": len(concepts),
        "before": tally("before"),
        "after": tally("after"),
        "fixed": sum(1 for c in concepts if c["before"] == "mix_up" and c["after"] == "right"),
        "learned": sum(1 for c in concepts if c["before"] == "unsure" and c["after"] == "right"),
        "slipped": sum(1 for c in concepts if c["before"] == "right" and c["after"] != "right"),
        "concepts": concepts,
    }


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
            if _UNSUITABLE_HOBBY_RE.search(value):
                raise EcoLearnError(
                    "That one can't be used for lessons. Pick a hobby from the list, or type a different one."
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
