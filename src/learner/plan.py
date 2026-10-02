"""Personal recommendations: "reorder, not regenerate" (ROADMAP §1).

Everything here works with lessons that already exist. It only changes what
EcoLearn *suggests*: nothing is ever locked, so a student can still open any
concept. Two signals feed it:

* the starting check (src/learner/diagnostic.py): a right answer marks a
  concept "likely known"; a wrong one records the misconception behind it;
* lesson checks: a wrong first answer records a misconception too.

A misconception stops counting once the student has cleared the concept.

The policy, on top of the path engine (which stays unchanged and tested):
1. a spaced review the engine wants still comes first;
2. otherwise the first unfinished concept in the chapter, skipping ones the
   starting check says the student already knows;
3. if that concept builds directly on one where the student showed a
   misconception, recommend brushing up that one first.
When none of this applies, the engine's own recommendation and wording stand,
so a student who skipped the check sees exactly what they saw before.
"""

from __future__ import annotations

import re
from typing import Any

from src.content import lesson_service
from src.path import engine
from src.progress import store

# How a misconception (written about "the student", in the third person) is
# turned to speak to the student. Others keep their wording, after a label.
_SECOND_PERSON = {
    "Thinks": "You might think",
    "Believes": "You might believe",
    "Assumes": "You might assume",
    "Expects": "You might expect",
    "Treats": "You might be treating",
    "Confuses": "You might be confusing",
    "Imagines": "You might imagine",
    "Mixes": "You might be mixing",
    "Reads": "You might be reading",
    "Forgets": "You might forget",
    "Ignores": "You might be ignoring",
}


_FIRST_SENTENCE = re.compile(r"^(.+?[.!?])(?=\s+[A-Z]|\s*$)", re.DOTALL)


def you_might(misconception: str) -> str:
    """'Thinks force is used up. It isn't…' -> 'You might think force is used up.'

    Only the first sentence: the rest of a misconception text is usually the
    correction, which is the lesson's job to teach, not the roadmap's to give away.
    """
    text = (misconception or "").strip()
    match = _FIRST_SENTENCE.match(text)
    if match:
        text = match.group(1)
    first, _, rest = text.partition(" ")
    if first in _SECOND_PERSON and rest:
        return f"{_SECOND_PERSON[first]} {rest}"
    return f"A mix-up to watch for: {text[:1].lower()}{text[1:]}"


def learner_state(student_id: str) -> dict[str, Any]:
    """What we know: likely-known concepts, open mix-ups, and what's cleared."""
    cleared = store.get_cleared_concepts(student_id)
    mastered = store.get_mastered_concepts(student_id)
    likely_known: set[str] = set()
    mix_ups: dict[str, dict[str, str]] = {}

    for row in store.get_diagnostic_answers([student_id]):
        if row["correct"] and row["concept_id"] not in mastered:
            likely_known.add(row["concept_id"])
        elif row["correct"] is False and row["misconception"]:
            mix_ups[row["concept_id"]] = {"text": row["misconception"], "source": "check"}
    # Lesson answers come later than the starting check, so they win.
    for row in store.get_activity([student_id])["answers"]:
        if not row["correct"] and row.get("misconception"):
            mix_ups[row["concept_id"]] = {"text": row["misconception"], "source": "lesson"}

    open_mix_ups = {c: m for c, m in mix_ups.items() if c not in cleared}
    return {"likely_known": likely_known - cleared, "mix_ups": open_mix_ups,
            "cleared": cleared, "mastered": mastered}


def _why(concept_name: str, mix_up: dict[str, str]) -> str:
    where = "Your starting check" if mix_up["source"] == "check" else "Your answer in this lesson"
    return f"{where} showed a mix-up in {concept_name}. {you_might(mix_up['text'])}"


def personal_next(
    student_id: str, chapter_id: str, interest: str, state: dict[str, Any] | None = None
) -> dict[str, Any] | None:
    """The personal next step in a chapter, or None to keep the engine's pick.

    Returns {"concept_id", "reason"} (always a new-learning step; reviews are
    left to the engine).
    """
    state = state or learner_state(student_id)
    if not state["likely_known"] and not state["mix_ups"]:
        return None  # nothing personal to go on

    ready = lesson_service.concepts_with_lessons(interest)
    rows = engine.get_roadmap(student_id, chapter_id)
    todo = [r for r in rows if r["concept_id"] in ready and r["concept_id"] not in state["cleared"]]
    if not todo:
        return None
    unknown = [r for r in todo if r["concept_id"] not in state["likely_known"]]
    first = (unknown or todo)[0]
    skipped = [r for r in todo[: todo.index(first)] if r["concept_id"] in state["likely_known"]]

    concept = engine.find_concept(first["concept_id"])
    for pid in concept.prerequisites:
        if pid in state["mix_ups"] and pid in ready and pid not in state["cleared"]:
            prerequisite = engine.find_concept(pid)
            return {
                "concept_id": pid,
                "reason": (f"Before {concept.name}, brush up on {prerequisite.name}: "
                           f"{concept.name} builds on it. "
                           + _why(prerequisite.name, state["mix_ups"][pid])),
            }

    if first["concept_id"] in state["mix_ups"]:
        return {"concept_id": first["concept_id"],
                "reason": _why(concept.name, state["mix_ups"][first["concept_id"]])}
    if skipped:
        names = ", ".join(r["name"] for r in skipped)
        return {"concept_id": first["concept_id"],
                "reason": (f"Next up: {concept.name}. Your starting check says you already "
                           f"know {names}, so we skipped ahead. You can still open "
                           f"{'it' if len(skipped) == 1 else 'them'} any time.")}
    return None


def annotate_roadmap(rows: list[dict[str, Any]], state: dict[str, Any]) -> None:
    """Add `personal` ("known" | "focus" | None) and `personal_note` to each row."""
    for row in rows:
        cid = row["concept_id"]
        if cid in state["mix_ups"]:
            row["personal"] = "focus"
            row["personal_note"] = you_might(state["mix_ups"][cid]["text"])
        elif cid in state["likely_known"]:
            row["personal"] = "known"
            row["personal_note"] = "Your starting check says you know this. Take its check to confirm."
        else:
            row["personal"] = None
            row["personal_note"] = None
