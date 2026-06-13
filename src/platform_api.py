"""EcoLearn platform API — the single service boundary for any frontend.

Every frontend (today Streamlit, tomorrow Next.js, a mobile app, a CLI) talks
to the platform through exactly these five functions and nothing else:

    create_or_load_student(name, interest, level) -> profile
    get_roadmap(student_id, chapter_id)           -> list of concept statuses
    get_next_lesson(student_id, chapter_id)       -> next lesson envelope
    submit_assessment(student_id, concept_id, answer) -> grade + new mastery
    ask_help(student_id, concept_id, question)    -> live tutor answer

These functions orchestrate the internal subsystems — the path engine
(src/path), the lesson read-service (src/content), the progress store
(src/progress), the assessor, and the live generate→critic→polish pipeline.
The frontend never imports those modules directly; it imports only this one.

Design rule: every return value is plain, JSON-serializable data (dict / list
of dicts / primitives). No Pydantic models, dataclasses, or domain objects
cross the boundary. That is what lets a non-Python frontend consume the exact
same results over HTTP without translation.
"""

from __future__ import annotations

import re
from typing import Any

from src.agents.assessor import grade_answer
from src.agents.polisher import polish_explanation
from src.content import lesson_service
from src.path import engine
from src.pipeline import explain_with_review
from src.progress import store

# Live help runs the full multi-agent pipeline; cap regeneration so a help
# request stays reasonably responsive (one critic-driven retry at most).
_HELP_MAX_RETRIES = 1


def _slugify(name: str) -> str:
    """Turn a display name into a stable student_id slug ('Ada Lovelace' -> 'ada-lovelace')."""
    slug = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    return slug or "student"


# ---------------------------------------------------------------------------
# 1. Students
# ---------------------------------------------------------------------------

def create_or_load_student(name: str, interest: str, level: str) -> dict[str, Any]:
    """Create a student, or load (and refresh) one that already exists.

    The student_id is derived deterministically from `name`, so calling this
    again with the same name returns the same student — the "load" path —
    while updating their interest/level to whatever was just passed (a student
    may switch interests between sessions).

    Args:
        name:     Student display name (e.g. "Ada").
        interest: Primary interest used to personalise lessons ("football" /
                  "gaming").
        level:    Academic level (e.g. "Class 11").

    Returns:
        Profile dict: {student_id, name, interest, level, created_at}.
    """
    student_id = _slugify(name)
    return store.save_student(student_id, name, interest, level)


# ---------------------------------------------------------------------------
# 2. Roadmap
# ---------------------------------------------------------------------------

def get_roadmap(student_id: str, chapter_id: str) -> list[dict[str, Any]]:
    """Return every concept in a chapter tagged mastered / available / locked.

    Thin pass-through to the path engine. Each entry is a plain dict carrying
    the concept id/name/order, its roadmap status, the underlying progress
    detail, and (for locked concepts) the missing prerequisite ids — enough to
    render a roadmap view with no further calls.

    Raises:
        ValueError: if the chapter has no concepts / doesn't exist.
    """
    return engine.get_roadmap(student_id, chapter_id)


# ---------------------------------------------------------------------------
# 3. Next lesson
# ---------------------------------------------------------------------------

def get_next_lesson(
    student_id: str,
    chapter_id: str,
    concept_id: str | None = None,
) -> dict[str, Any]:
    """Return the personalised lesson for the student's next concept.

    Orchestrates: ask the path engine what to learn next, then fetch the
    pre-generated lesson for that concept in the student's interest.

    If `concept_id` is given, that specific concept is served instead of the
    engine's pick — used when the student chooses to *re-practise* a concept
    they only partly passed (the engine would otherwise advance past it).

    Returns an envelope dict so the frontend can handle every outcome:
        {
          "status":       "new" | "review" | "done" | "blocked" | "lesson_missing",
          "reason":       why this was chosen (human-readable),
          "concept_id":   the chosen concept id (None when status == "done"),
          "concept_name": the chosen concept name (None when status == "done"),
          "lesson":       the Lesson as a plain dict, or None,
        }

    Raises:
        ValueError: if the student is unknown (create them first).
    """
    profile = store.get_student(student_id)
    if profile is None:
        raise ValueError(
            f"Unknown student_id {student_id!r}. Call create_or_load_student first."
        )

    if concept_id is not None:
        # Explicit re-practise of a specific concept.
        concept = engine.find_concept(concept_id)
        if concept is None:
            raise ValueError(f"Unknown concept_id {concept_id!r}.")
        is_mastered = concept_id in store.get_mastered_concepts(student_id)
        envelope: dict[str, Any] = {
            "status": engine.KIND_REVIEW if is_mastered else engine.KIND_NEW,
            "reason": f"Practising {concept.name} again to strengthen it.",
            "concept_id": concept.id,
            "concept_name": concept.name,
            "lesson": None,
        }
        chosen = concept
    else:
        rec = engine.next_concept(student_id, chapter_id)
        envelope = {
            "status": rec.kind,
            "reason": rec.reason,
            "concept_id": rec.concept.id if rec.concept else None,
            "concept_name": rec.concept.name if rec.concept else None,
            "lesson": None,
        }
        chosen = rec.concept if rec.kind in (engine.KIND_NEW, engine.KIND_REVIEW) else None

    # Load the lesson body when there's a concept to actually teach.
    if chosen is not None:
        lesson = lesson_service.get_lesson(chosen.id, profile["interest"])
        if lesson is None:
            envelope["status"] = "lesson_missing"
            envelope["reason"] = (
                f"No pre-generated lesson exists for {chosen.name} in "
                f"interest {profile['interest']!r} yet. "
                "Generate it with the lesson factory."
            )
        else:
            envelope["lesson"] = lesson.model_dump()

    return envelope


# ---------------------------------------------------------------------------
# 4. Assessment
# ---------------------------------------------------------------------------

def submit_assessment(
    student_id: str,
    concept_id: str,
    answer: str,
) -> dict[str, Any]:
    """Grade a student's answer to a concept's self-check and update mastery.

    The question graded against is the concept's pre-generated lesson
    `check_question` (the assessment *is* the lesson's self-check). The grade
    is run through the existing Assessor, then the 0-3 score is written to the
    progress store, advancing the student's mastery.

    Returns:
        {
          "concept_id":      the graded concept,
          "score":           0-3,
          "mastery_signal":  "mastered" | "partial" | "not_yet" (assessor's view),
          "feedback":        teacher-style feedback string,
          "missing_concepts": list of concepts the answer missed,
          "graded_question": the question the answer was scored against,
          "mastery":         the updated progress row {status, best_score, attempts, ...},
        }

    Raises:
        ValueError: if the student is unknown, or no lesson exists to assess
                    against for this concept + interest.
    """
    profile = store.get_student(student_id)
    if profile is None:
        raise ValueError(
            f"Unknown student_id {student_id!r}. Call create_or_load_student first."
        )

    lesson = lesson_service.get_lesson(concept_id, profile["interest"])
    if lesson is None:
        raise ValueError(
            f"No lesson for concept {concept_id!r} in interest "
            f"{profile['interest']!r}; cannot assess."
        )

    # Anchor the grader with the concept's name and learning objective so it
    # knows what a correct answer should demonstrate.
    concept = engine.find_concept(concept_id)
    expected_concepts = []
    if concept is not None:
        expected_concepts = [concept.name, concept.learning_objective]

    grade = grade_answer(
        question=lesson.check_question,
        expected_concepts=expected_concepts,
        student_answer=answer,
    )

    # If the grader failed (all models errored / unparseable), it returns a
    # sentinel with an `error` key. Do NOT write a fake score-0 to mastery —
    # that would punish the student for an API outage. Surface it instead so
    # the UI can show a "try again" message, leaving progress untouched.
    if grade.get("error"):
        raise RuntimeError(
            "The grader is temporarily unavailable. Your progress was not "
            "changed — please try submitting again in a moment."
        )

    score = int(grade.get("score", 0))
    updated = store.update_progress(student_id, concept_id, score)

    return {
        "concept_id": concept_id,
        "score": score,
        "mastery_signal": grade.get("mastery_signal", "not_yet"),
        "feedback": grade.get("feedback", ""),
        "missing_concepts": grade.get("missing_concepts", []),
        "graded_question": lesson.check_question,
        "mastery": updated,
    }


# ---------------------------------------------------------------------------
# 5. Live help
# ---------------------------------------------------------------------------

def ask_help(student_id: str, concept_id: str, question: str) -> dict[str, Any]:
    """Answer a free-form question via the live generate→critic→polish pipeline.

    This is the expensive, real-time path (distinct from the cached lessons):
    it runs the full multi-agent pipeline on the student's question, grounded
    in their interest, then polishes the result into clean markdown.

    Args:
        student_id: Who is asking (used for their interest/level).
        concept_id: The concept the question is about (for context/logging).
        question:   The student's free-form question.

    Returns:
        {
          "concept_id": the concept context,
          "answer":     polished markdown answer,
          "verdict":    the critic's verdict on the underlying explanation,
          "attempts":   how many generator attempts the pipeline made,
        }

    Raises:
        ValueError: if the student is unknown.
    """
    profile = store.get_student(student_id)
    if profile is None:
        raise ValueError(
            f"Unknown student_id {student_id!r}. Call create_or_load_student first."
        )

    # Ground the help in the concept the student is actually on. Leading with
    # the concept name steers RAG retrieval to the right curriculum passages,
    # and tells the generator the topic — so the answer is contextual to the
    # lesson, not just a free-floating reply to the raw question text.
    concept = engine.find_concept(concept_id)
    concept_label = concept.name if concept is not None else concept_id
    framed_query = f"{concept_label} — student asks: {question}"

    result = explain_with_review(
        concept=framed_query,
        interest=profile["interest"],
        level=profile["level"],
        max_retries=_HELP_MAX_RETRIES,
    )
    answer = polish_explanation(result.get("explanation", ""))

    return {
        "concept_id": concept_id,
        "concept_name": concept_label,
        "answer": answer,
        "verdict": result.get("verdict", "ERROR"),
        "attempts": result.get("attempts", 0),
    }
