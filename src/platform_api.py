"""EcoLearn platform API — the single service boundary for any frontend.

Every frontend (today Streamlit, tomorrow Next.js, a mobile app, a CLI) talks
to the platform through exactly these five functions and nothing else:

    ACCOUNTS
    register_student(name, username, password, interest, level) -> profile
    authenticate_student(username, password)      -> profile (raises AuthError)
    get_student_profile(student_id)               -> profile
    update_student_profile(student_id, ...)       -> updated profile
    change_password(student_id, current, new)     -> {student_id, changed}

    LEARNING
    create_or_load_student(name, interest, level) -> profile  (legacy, no password)
    list_chapters()                               -> [{id, name}, ...]
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
import sqlite3
import uuid
from typing import Any

from src.agents.assessor import grade_answer
from src.agents.polisher import polish_explanation
from src.auth import passwords
from src.content import lesson_service
from src.curriculum.interests import load_interests
from src.errors import AuthError, ConflictError, EcoLearnError, NotFoundError
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
# 1b. Accounts (username + password)
#
# Username, not email: the pilot runs on school students, most of them minors,
# so the platform collects as little personal data as it can (user decision,
# 2026-09-21). The trade-off: there is no email to send a reset link to, so a
# forgotten password is reset by a teacher/admin tool instead.
#
# `create_or_load_student` above treats a *name* as the credential: type "Ada"
# and you are Ada, forever, on any device. That was fine for a demo and is kept
# working (Streamlit and the pinned contract test depend on it), but it is not an
# account. These functions add real ones.
#
# Two id schemes now coexist, and they are provably disjoint:
#   * legacy ids are slugs        -> "ada-lovelace"   (letters, digits, hyphens)
#   * account ids are uuid-based  -> "stu_9f8a...c1"  (contains an underscore)
# `_slugify` can never emit "_", so no new account can ever collide with a
# legacy student's progress rows.
# ---------------------------------------------------------------------------

# 3–20 characters: lowercase letters, digits, "_" and ".", starting with a
# letter or digit. Stored lowercased, so "Ada_K" and "ada_k" are one account.
_USERNAME_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_.]{2,19}$")

# ONE message for every login failure. Saying "no such account" vs "wrong
# password" hands an attacker a free username-enumeration oracle.
_INVALID_CREDENTIALS = "Incorrect username or password."


def _new_student_id() -> str:
    """Mint an opaque id for a real account ("stu_" + 32 hex chars).

    Random, not derived from the name or username: an id ends up in URLs and
    logs, and it must stay stable when the student changes their name.
    """
    return f"stu_{uuid.uuid4().hex}"


def _normalise_username(username: str) -> str:
    """Trim + lowercase a username and check it against the allowed pattern.

    Normalising on the way in is what makes the unique index meaningful:
    "Ada_K " and "ada_k" must be the same account, and the database compares
    bytes, not intentions.

    Raises:
        EcoLearnError: if the username is empty or breaks the rules.
    """
    cleaned = (username or "").strip().lower()
    if not cleaned:
        raise EcoLearnError("Username is required.")
    if not _USERNAME_PATTERN.match(cleaned):
        raise EcoLearnError(
            "Usernames are 3–20 characters: letters, numbers, '_' and '.', "
            "starting with a letter or number."
        )
    return cleaned


def _validate_interest(interest: str) -> str:
    """Normalise an interest and check it exists in `data/interests.yaml`.

    Before the registry, any non-blank text was accepted — and an interest with
    no lessons silently got "lesson missing" on every concept.
    """
    cleaned = (interest or "").strip().lower()
    if not cleaned:
        raise EcoLearnError("Interest is required.")
    known = {i.id for i in load_interests()}
    if cleaned not in known:
        raise EcoLearnError(
            f"Unknown interest {interest!r}. Choose one of: {', '.join(sorted(known))}."
        )
    return cleaned


def _require_name(name: str) -> str:
    """Trim a display name, rejecting blank input."""
    cleaned = (name or "").strip()
    if not cleaned:
        raise EcoLearnError("Name is required.")
    return cleaned


def register_student(
    name: str,
    username: str,
    password: str,
    interest: str,
    level: str = "Class 11",
) -> dict[str, Any]:
    """Create a brand-new account and return its profile (never the hash).

    Args:
        name:     Display name (not an identifier — two students may share one).
        username: Login identifier; normalised and unique across the platform.
        password: Plaintext, hashed here and never stored or logged as-is.
        interest: An id from data/interests.yaml — drives which lessons are served.
        level:    Academic level, e.g. "Class 11".

    Returns:
        Profile dict {student_id, name, interest, level, created_at, username}.

    Raises:
        EcoLearnError:  blank name, an invalid username, an unknown interest,
                        or a password that fails the length rules.
        ConflictError:  that username is already taken.
    """
    name = _require_name(name)
    username = _normalise_username(username)
    interest = _validate_interest(interest)
    if not (level or "").strip():
        raise EcoLearnError("Level is required.")

    # Hash first: a weak/over-long password should fail before we touch the DB.
    password_hash = passwords.hash_password(password)

    # Friendly pre-check, then rely on the unique index as the real guarantee —
    # between this SELECT and the INSERT another request could claim the name.
    if store.get_student_by_username(username) is not None:
        raise ConflictError("That username is taken. Try another, or log in instead.")

    try:
        return store.save_student_with_credentials(
            student_id=_new_student_id(),
            name=name,
            interest=interest,
            level=level.strip(),
            username=username,
            password_hash=password_hash,
        )
    except sqlite3.IntegrityError as exc:
        # The index caught a race (or, vanishingly unlikely, a uuid4 collision).
        raise ConflictError("That username is taken. Try another, or log in instead.") from exc


def authenticate_student(username: str, password: str) -> dict[str, Any]:
    """Verify credentials and return the student's profile.

    Constant-ish time on purpose. Both failure branches — unknown username and
    wrong password — do one bcrypt comparison and raise the *same* message, so
    neither timing nor wording reveals whether a username is registered.

    Returns:
        Profile dict (no password_hash).

    Raises:
        AuthError: on any failure, always with the same generic message.
    """
    # A malformed username can't match any account; fail like a wrong password
    # rather than explaining the format (this is the login form, not signup).
    try:
        username = _normalise_username(username)
    except EcoLearnError:
        passwords.dummy_verify()
        raise AuthError(_INVALID_CREDENTIALS) from None

    record = store.get_student_by_username(username)
    if record is None:
        passwords.dummy_verify()  # spend the same ~100ms as a real check
        raise AuthError(_INVALID_CREDENTIALS)

    if not passwords.verify_password(password, record.get("password_hash")):
        raise AuthError(_INVALID_CREDENTIALS)

    # Strip the hash before the profile escapes the boundary.
    return {k: v for k, v in record.items() if k != "password_hash"}


def get_student_profile(student_id: str) -> dict[str, Any]:
    """Return a student's profile, raising if they don't exist.

    The read behind `GET /api/auth/me`: the browser holds an httpOnly cookie it
    cannot read, so it asks the server who it is on every page load.

    Raises:
        NotFoundError: if no such student (e.g. a token for a deleted account).
    """
    profile = store.get_student(student_id)
    if profile is None:
        raise NotFoundError(f"Unknown student_id {student_id!r}.")
    return profile


def update_student_profile(
    student_id: str,
    *,
    name: str | None = None,
    interest: str | None = None,
    level: str | None = None,
) -> dict[str, Any]:
    """Patch name / interest / level; omitted fields are left alone.

    Note what is *not* here: username and password. Changing a login identifier or
    a secret needs its own re-authentication flow, so it doesn't ride along with
    "pick a different interest".

    Returns:
        The updated profile dict.

    Raises:
        EcoLearnError:  nothing to update, a blank value passed explicitly, or
                        an interest that isn't in the registry.
        NotFoundError:  no such student.
    """
    if name is None and interest is None and level is None:
        raise EcoLearnError("Nothing to update.")

    if name is not None:
        name = _require_name(name)
    if interest is not None:
        if not interest.strip():
            raise EcoLearnError("Interest cannot be blank.")
        interest = _validate_interest(interest)
    if level is not None:
        level = level.strip()
        if not level:
            raise EcoLearnError("Level cannot be blank.")

    updated = store.update_student_profile(
        student_id, name=name, interest=interest, level=level
    )
    if updated is None:
        raise NotFoundError(f"Unknown student_id {student_id!r}.")
    return updated


def change_password(
    student_id: str,
    current_password: str,
    new_password: str,
) -> dict[str, Any]:
    """Re-authenticate with the current password, then set a new one.

    Requiring the current password matters even though the caller already holds
    a valid session: it stops a borrowed or stolen session from locking the real
    owner out of their own account.

    Returns:
        {"student_id": ..., "changed": True}

    Raises:
        NotFoundError: no such student.
        AuthError:     the current password is wrong (or the account has none).
        EcoLearnError: the new password fails the length rules, or repeats the
                       current one.
    """
    if store.get_student(student_id) is None:
        raise NotFoundError(f"Unknown student_id {student_id!r}.")

    existing_hash = store.get_password_hash(student_id)
    if not passwords.verify_password(current_password, existing_hash):
        raise AuthError("Your current password is incorrect.")

    if new_password == current_password:
        raise EcoLearnError("Your new password must be different from the current one.")

    store.update_student_password(student_id, passwords.hash_password(new_password))
    return {"student_id": student_id, "changed": True}


# ---------------------------------------------------------------------------
# 2. Chapters + roadmap
# ---------------------------------------------------------------------------

def list_chapters() -> list[dict[str, Any]]:
    """Return all chapters in the curriculum as [{id, name}, ...].

    Lets a frontend render a chapter picker without reaching into the
    curriculum directly.
    """
    return engine.list_chapters()


def get_roadmap(student_id: str, chapter_id: str) -> list[dict[str, Any]]:
    """Return every concept in a chapter tagged mastered / available.

    Thin pass-through to the path engine. Nothing is ever locked. Each entry is
    a plain dict carrying the concept id/name/order, its roadmap status, the
    underlying progress detail, and `missing_prerequisites` (uncleared
    prerequisites, shown as "brush up first" hints) — enough to render a
    roadmap view with no further calls.

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
          "status":       "new" | "review" | "done" | "lesson_missing",
                          ("blocked" is no longer produced — nothing is locked)
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
        raise NotFoundError(
            f"Unknown student_id {student_id!r}. Call create_or_load_student first."
        )

    if concept_id is not None:
        # Explicit re-practise of a specific concept.
        concept = engine.find_concept(concept_id)
        if concept is None:
            raise NotFoundError(f"Unknown concept_id {concept_id!r}.")
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
        raise NotFoundError(
            f"Unknown student_id {student_id!r}. Call create_or_load_student first."
        )

    lesson = lesson_service.get_lesson(concept_id, profile["interest"])
    if lesson is None:
        raise NotFoundError(
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
        raise NotFoundError(
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
