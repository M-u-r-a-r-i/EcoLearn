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
    list_chapters()                               -> [{id, name, unit_id, unit_name, grade, ...}]
    list_interests(active_only=True)              -> [{id, label, emoji, ...}]
    get_roadmap(student_id, chapter_id)           -> list of concept statuses
    get_next_lesson(student_id, chapter_id)       -> next lesson envelope
    submit_assessment(student_id, concept_id, answer) -> grade + new mastery
    ask_help(student_id, concept_id, question)    -> live tutor answer

    PILOT METRICS (no model calls)
    start_lesson_view / record_lesson_time / rate_lesson  -> student-side logging
    get_class_insights(teacher_id, class_id)      -> a teacher's dashboard data
    pilot_report()                                -> every class, pseudonymised

    TEACHER AGENT (the one teacher-triggered live call; falls back to rules)
    get_class_plan / generate_class_plan(teacher_id, class_id) -> next-lesson plan

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

import os
import re
import sqlite3
import threading
import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from src.agents import coaching_agent, teacher_agent  # stdlib-only at import; the SDK loads lazily
from src.agents.assessor import grade_answer
from src.auth import credentials, passwords
from src.content import lesson_service
from src.curriculum.interests import load_interests
from src.curriculum.scope import scope_chapter_ids, scope_interest_ids
from src.errors import AuthError, ConflictError, EcoLearnError, NotFoundError, TooManyRequestsError
from src.learner import diagnostic, doubt_tutor, experiments, help_guard, personal_story, practice, profiler, survey
from src.learner import plan as learner_plan
from src.path import engine
from src.progress import metrics, store
from src import llm

# Every model call made through src/llm goes into the usage log (the cost per
# student for the pitch). Registered here, so src/llm needs no storage code.
llm.set_usage_sink(store.record_llm_call)


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
    # Teachers share the namespace, so a student can't take a teacher's username.
    if store.username_exists(username):
        raise ConflictError("That username is taken. Try another, or log in instead.")

    try:
        saved = store.save_student_with_credentials(
            student_id=_new_student_id(),
            name=name,
            interest=interest,
            level=level.strip(),
            username=username,
            password_hash=password_hash,
        )
        _enrol_experiments(saved["student_id"])
        return saved
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
# 1b. Teachers and classes (2026-10-02)
#
# The pilot's students have no email, so "forgot password" can't be a reset
# link. Instead the teacher who created a student's account can reset it. A
# teacher can also create a whole class from a list of names in one go and print
# the sign-in slips.
#
# The rules, all enforced here and nowhere else:
#   * Teacher accounts are created only by `create_teacher`, run from the
#     server's command line (scripts/create_teacher.py). There is no HTTP
#     endpoint for it, so nobody can make themselves a teacher from a browser.
#   * A teacher sees and changes only their own classes and the students in
#     them. Someone else's class answers NotFoundError, not "forbidden", so a
#     guessed id reveals nothing about whether it exists.
#   * Generated passwords are returned ONCE, in the response that created them,
#     and only their hash is stored. A lost slip means a reset, not a lookup.
# ---------------------------------------------------------------------------

# Limits that keep one request sane. A school class is ~30–45 students.
_MAX_ROSTER = 60
_MAX_NAME_LENGTH = 60


def _new_teacher_id() -> str:
    return f"tch_{uuid.uuid4().hex}"


def _new_class_id() -> str:
    return f"cls_{uuid.uuid4().hex}"


def create_teacher(name: str, username: str, password: str) -> dict[str, Any]:
    """Create a teacher account. Server-side only — see the section comment.

    Raises:
        EcoLearnError: blank name, invalid username, or a password that fails
                       the length rules.
        ConflictError: the username is taken (by a student or another teacher).
    """
    name = _require_name(name)
    username = _normalise_username(username)
    password_hash = passwords.hash_password(password)
    if store.username_exists(username):
        raise ConflictError("That username is taken.")
    try:
        return store.save_teacher(_new_teacher_id(), name, username, password_hash)
    except sqlite3.IntegrityError as exc:
        raise ConflictError("That username is taken.") from exc


def authenticate_teacher(username: str, password: str) -> dict[str, Any]:
    """Verify a teacher's credentials. Same constant-ish timing and single
    message as `authenticate_student`, for the same reasons."""
    try:
        username = _normalise_username(username)
    except EcoLearnError:
        passwords.dummy_verify()
        raise AuthError(_INVALID_CREDENTIALS) from None

    record = store.get_teacher_by_username(username)
    if record is None:
        passwords.dummy_verify()
        raise AuthError(_INVALID_CREDENTIALS)
    if not passwords.verify_password(password, record.get("password_hash")):
        raise AuthError(_INVALID_CREDENTIALS)
    return {k: v for k, v in record.items() if k != "password_hash"}


def get_teacher_profile(teacher_id: str) -> dict[str, Any]:
    """Raises NotFoundError for an unknown id (including any student id)."""
    profile = store.get_teacher(teacher_id)
    if profile is None:
        raise NotFoundError(f"Unknown teacher_id {teacher_id!r}.")
    return profile


def change_teacher_password(
    teacher_id: str, current_password: str, new_password: str
) -> dict[str, Any]:
    """Same rules as a student's `change_password`."""
    get_teacher_profile(teacher_id)
    if not passwords.verify_password(current_password, store.get_teacher_password_hash(teacher_id)):
        raise AuthError("Your current password is incorrect.")
    if new_password == current_password:
        raise EcoLearnError("Your new password must be different from the current one.")
    store.update_teacher_password(teacher_id, passwords.hash_password(new_password))
    return {"teacher_id": teacher_id, "changed": True}


def _own_class(teacher_id: str, class_id: str) -> dict[str, Any]:
    """The class, if it exists AND belongs to this teacher; otherwise NotFoundError."""
    klass = store.get_class(class_id) if class_id else None
    if klass is None or klass["teacher_id"] != teacher_id:
        raise NotFoundError("Class not found.")
    return klass


def _parse_roster(
    roster: str | list[str], default_interest: str
) -> list[tuple[str, str]]:
    """Turn pasted roster text into [(name, interest), ...].

    One student per line. A line may end with ", <interest>" to give that
    student a different interest from the class default ("Aarav Kumar, cricket").
    Blank lines are skipped, so a list pasted from a spreadsheet just works.

    Raises:
        EcoLearnError: no names, too many, a name that is too long, or an
                       unknown interest — naming the offending line.
    """
    lines = roster.splitlines() if isinstance(roster, str) else list(roster)
    entries: list[tuple[str, str]] = []
    for number, raw in enumerate(lines, start=1):
        line = (raw or "").strip()
        if not line:
            continue
        name, interest = line, default_interest
        if "," in line:
            name, _, maybe_interest = line.rpartition(",")
            name = name.strip()
            try:
                interest = _validate_interest(maybe_interest)
            except EcoLearnError as exc:
                raise EcoLearnError(f"Line {number} ({line!r}): {exc}") from None
        if not name:
            raise EcoLearnError(f"Line {number} has no name.")
        if len(name) > _MAX_NAME_LENGTH:
            raise EcoLearnError(
                f"Line {number}: names can be at most {_MAX_NAME_LENGTH} characters."
            )
        entries.append((name, interest))

    if not entries:
        raise EcoLearnError("Add at least one student name, one per line.")
    if len(entries) > _MAX_ROSTER:
        raise EcoLearnError(
            f"At most {_MAX_ROSTER} students at a time ({len(entries)} given). "
            "Split the list and add the rest to the same class."
        )
    return entries


def add_students_to_class(
    teacher_id: str,
    class_id: str,
    roster: str | list[str],
    interest: str,
) -> dict[str, Any]:
    """Create an account for every name in `roster`, inside one of the teacher's classes.

    Usernames come from the names ("Aarav Kumar" → "aarav.k", or "aarav.k2" if
    taken); each student gets a fresh typeable password. Everything is saved in
    one transaction — all students or none.

    Returns:
        {"class": {...}, "credentials": [{student_id, name, username, password,
        interest}, ...]} — the ONLY time these passwords exist in plaintext.

    Raises:
        NotFoundError: not this teacher's class.
        EcoLearnError: a bad roster or interest.
        ConflictError: a username was claimed by someone else mid-request
                       (nothing was saved; trying again picks fresh names).
    """
    get_teacher_profile(teacher_id)
    klass = _own_class(teacher_id, class_id)
    default_interest = _validate_interest(interest)
    entries = _parse_roster(roster, default_interest)

    chosen: set[str] = set()

    def is_taken(candidate: str) -> bool:
        return candidate in chosen or store.username_exists(candidate)

    rows: list[dict[str, Any]] = []
    plaintext: dict[str, str] = {}
    for name, student_interest in entries:
        username = credentials.unique_username(name, is_taken)
        chosen.add(username)
        student_id = _new_student_id()
        plaintext[student_id] = credentials.generate_password()
        rows.append({
            "student_id": student_id,
            "name": name,
            "interest": student_interest,
            "level": klass["level"],
            "username": username,
        })

    # bcrypt is slow on purpose (~0.35 s a hash here), so 45 hashes one after
    # another kept the teacher waiting ~16 s. bcrypt releases Python's GIL while
    # it works, so a thread pool really does hash in parallel: measured 2026-10-02
    # on a 16-core machine, 4 threads took 5.5 s and 8 or 16 were no faster. Four
    # also leaves CPU for the students using the app at the same moment.
    with ThreadPoolExecutor(max_workers=min(4, len(rows))) as pool:
        hashes = pool.map(passwords.hash_password, [plaintext[r["student_id"]] for r in rows])
        for row, password_hash in zip(rows, hashes):
            row["password_hash"] = password_hash

    try:
        saved = store.save_students_bulk(class_id, rows)
    except sqlite3.IntegrityError as exc:
        raise ConflictError(
            "Another account took one of these usernames just now. Nothing was "
            "saved — please try again."
        ) from exc
    for s in saved:  # pilot experiments: an arm per student, balanced within this class
        _enrol_experiments(s["student_id"])

    return {
        "class": store.get_class(class_id),
        "credentials": [
            {"student_id": s["student_id"], "name": s["name"], "username": s["username"],
             "password": plaintext[s["student_id"]], "interest": s["interest"]}
            for s in saved
        ],
    }


def create_class(
    teacher_id: str,
    name: str,
    level: str,
    interest: str,
    roster: str | list[str],
) -> dict[str, Any]:
    """Create a class and its students' accounts in one step.

    The roster is checked *before* the class row is written, so a typo in the
    list doesn't leave an empty class behind.

    Returns:
        Same shape as `add_students_to_class`.
    """
    get_teacher_profile(teacher_id)
    name = (name or "").strip()
    if not name:
        raise EcoLearnError("Class name is required.")
    if len(name) > _MAX_NAME_LENGTH:
        raise EcoLearnError(f"Class names can be at most {_MAX_NAME_LENGTH} characters.")
    level = (level or "").strip()
    if not level:
        raise EcoLearnError("Level is required.")
    _parse_roster(roster, _validate_interest(interest))  # fail early, write nothing

    klass = store.create_class(_new_class_id(), teacher_id, name, level)
    return add_students_to_class(teacher_id, klass["class_id"], roster, interest)


def list_teacher_classes(teacher_id: str) -> list[dict[str, Any]]:
    """The teacher's classes, newest first, with student counts."""
    get_teacher_profile(teacher_id)
    return store.list_classes(teacher_id)


def get_class_detail(teacher_id: str, class_id: str) -> dict[str, Any]:
    """One of the teacher's classes with every student's progress summary.

    Returns:
        {"class": {...}, "students": [{student_id, name, username, interest,
        level, created_at, attempted, mastered, last_active}, ...]}
    """
    get_teacher_profile(teacher_id)
    klass = _own_class(teacher_id, class_id)
    return {"class": klass, "students": store.list_class_students(class_id)}


def reset_student_password(teacher_id: str, student_id: str) -> dict[str, Any]:
    """Give a student in one of the teacher's classes a new password.

    Returns the new password once, for the teacher to hand over. The student's
    existing sessions stay valid — the cookie proves who they are, not their
    password — which is what a classroom wants: resetting a forgotten password
    shouldn't throw anyone else out.

    Raises:
        NotFoundError: the student doesn't exist or isn't in this teacher's
                       classes (one answer for both).
    """
    get_teacher_profile(teacher_id)
    class_id = store.get_student_class_id(student_id)
    if class_id is None:
        raise NotFoundError("Student not found in your classes.")
    try:
        _own_class(teacher_id, class_id)
    except NotFoundError:
        raise NotFoundError("Student not found in your classes.") from None

    password = credentials.generate_password()
    store.update_student_password(student_id, passwords.hash_password(password))
    profile = store.get_student(student_id) or {}
    return {
        "student_id": student_id,
        "name": profile.get("name"),
        "username": profile.get("username"),
        "password": password,
    }


_LEVELS = ("Class 11", "Class 12")


def set_student_level(teacher_id: str, student_id: str, level: str) -> dict[str, Any]:
    """Move a student in one of the teacher's classes to Class 11 or Class 12.

    Only a teacher can do this (2026-10-03): a student's level decides which
    chapters they see, so it isn't theirs to change. Their earlier answers and
    progress stay as they are; their lessons and roadmap follow the new level.

    Raises:
        NotFoundError: the student isn't in this teacher's classes.
        EcoLearnError: a level other than Class 11 or Class 12.
    """
    level = (level or "").strip()
    if level not in _LEVELS:
        raise EcoLearnError(f"Level must be one of: {', '.join(_LEVELS)}.")
    get_teacher_profile(teacher_id)
    class_id = store.get_student_class_id(student_id)
    if class_id is None:
        raise NotFoundError("Student not found in your classes.")
    try:
        _own_class(teacher_id, class_id)
    except NotFoundError:
        raise NotFoundError("Student not found in your classes.") from None
    store.update_student_profile(student_id, level=level)
    return {"student_id": student_id, "level": level}


def set_student_ai(teacher_id: str, student_id: str, enabled: bool) -> dict[str, Any]:
    """Turn the AI features on or off for one student in the teacher's classes (2026-10-14).

    For a family that says no to the AI parts. With the switch off, nothing about the student
    goes to a model: no personal story is written or shown (they see the lesson's own story),
    the help chat answers with the lesson's key idea instead of asking the AI, their coaching
    note is written by rules, and they are left out of what the teaching assistant sees. The
    lessons, checks and progress work exactly as before (none of them use AI).

    Raises:
        NotFoundError: the student isn't in this teacher's classes.
    """
    get_teacher_profile(teacher_id)
    class_id = store.get_student_class_id(student_id)
    if class_id is None:
        raise NotFoundError("Student not found in your classes.")
    try:
        _own_class(teacher_id, class_id)
    except NotFoundError:
        raise NotFoundError("Student not found in your classes.") from None
    store.set_student_ai(student_id, bool(enabled))
    return {"student_id": student_id, "ai_enabled": bool(enabled)}


def operator_set_student_ai(student_id: str, enabled: bool) -> dict[str, Any]:
    """The same switch for the operator (scripts/set_student_ai.py), when a family asks them directly.

    Never exposed over HTTP. Raises NotFoundError for an unknown student.
    """
    if not store.set_student_ai(student_id, bool(enabled)):
        raise NotFoundError(f"Unknown student_id {student_id!r}.")
    return {"student_id": student_id, "ai_enabled": bool(enabled)}


# ---------------------------------------------------------------------------
# 2. Chapters + roadmap
# ---------------------------------------------------------------------------

def list_chapters(interest: str | None = None) -> list[dict[str, Any]]:
    """Return all chapters in teaching order as
    [{id, name, unit_id, unit_name, grade, domain, concept_count}, ...].

    Lets a frontend render a chapter picker (grouped class → unit) without
    reaching into the curriculum directly.

    With `interest`, each chapter also carries `lessons_ready`: how many of its
    concepts have a lesson a student with that interest can be served. The
    picker uses it to mark chapters "coming soon" instead of letting a student
    walk into an empty one.

    Raises:
        EcoLearnError: `interest` is not a registered interest.
    """
    chapters = engine.list_chapters()
    if interest is None:
        return chapters
    ready = lesson_service.concepts_with_lessons(_validate_interest(interest))
    by_chapter = engine.concept_ids_by_chapter()
    for chapter in chapters:
        chapter["lessons_ready"] = sum(1 for c in by_chapter.get(chapter["id"], []) if c in ready)
    return chapters


def list_interests(active_only: bool = True) -> list[dict[str, Any]]:
    """Return the interests a student can choose.

    `active_only=True` (the default) offers the interests in
    `data/content_scope.yaml` — the set we are actually writing lessons for —
    in the order the scope lists them. Each one says how much of the syllabus it
    covers so far (`chapters_ready` of `chapters_total`), so the UI can be honest
    instead of hiding a half-written interest.

    Why not the registry's `active` flag: it marks an interest ready only once
    every chapter is written, which hid cricket (the largest set) while offering
    football and gaming, which were no more complete. Coverage is a number, not
    a yes/no, so we now show the number. `active_only=False` still returns the
    whole registry.

    Returns:
        [{id, label, emoji, description, status, chapters_ready, chapters_total}, ...]
    """
    registry = {i.id: i for i in load_interests()}
    scope_ids = [i for i in scope_interest_ids() if i in registry]
    chosen = scope_ids if (active_only and scope_ids) else list(registry)
    chapters_total = len(scope_chapter_ids())

    out: list[dict[str, Any]] = []
    for interest_id in chosen:
        i = registry[interest_id]
        ready = lesson_service.chapters_with_lessons(i.id) & set(scope_chapter_ids())
        out.append(
            {
                "id": i.id,
                "label": i.label,
                "emoji": i.emoji,
                "description": i.description,
                "status": i.status.value,
                "chapters_ready": len(ready),
                "chapters_total": chapters_total,
            }
        )
    return out


def _level_grade(level: str) -> int | None:
    digits = re.findall(r"\d+", level or "")
    return int(digits[0]) if digits else None


def _require_chapter_for_level(profile: dict[str, Any], chapter_id: str) -> None:
    """A student only works in their own class's chapters (the teacher sets the class)."""
    grade = _level_grade(profile.get("level", ""))
    chapter = next((c for c in engine.list_chapters() if c["id"] == chapter_id), None)
    if grade is None or chapter is None or chapter["grade"] == grade:
        return
    raise EcoLearnError(
        f"{chapter['name']} is a Class {chapter['grade']} chapter. You're in Class {grade}; "
        "your teacher can move you up."
    )


def _concept_locks(
    student_id: str, interest: str, rows: list[dict[str, Any]], state: dict[str, Any]
) -> dict[str, str | None]:
    """{concept_id: why it is locked, or None}: concepts open one after another.

    Chapters are never locked (2026-10-03: the user's call); the concepts inside
    one open in order, like levels. A concept is open when:
      * it is the first written one in the chapter, or the one before it is
        passed (right once = cleared, or mastered, or the starting check says
        the student knows it: so strong students aren't held back), or
      * the student already tried it, or the starting check showed a mix-up in
        it (the plan sends them there), or it is passed itself.
    A concept with no lesson yet ("coming soon") never blocks the one after it.
    """
    ready = lesson_service.concepts_with_lessons(interest)
    attempted = {a["concept_id"] for a in store.get_activity([student_id])["answers"]}
    open_anyway = attempted | set(state["mix_ups"])
    locks: dict[str, str | None] = {}
    previous: tuple[str, bool] | None = None  # (name, passed) of the last written concept
    for row in rows:
        cid = row["concept_id"]
        if cid not in ready:
            locks[cid] = None
            continue
        passed = (row["status"] == engine.ROADMAP_MASTERED
                  or row["progress_status"] in (store.STATUS_PARTIAL, store.STATUS_MASTERED)
                  or cid in state["likely_known"])
        if previous is None or previous[1] or passed or cid in open_anyway:
            locks[cid] = None
        else:
            locks[cid] = f"Finish {previous[0]} first."
        previous = (row["name"], passed)
    return locks


def get_roadmap(student_id: str, chapter_id: str) -> list[dict[str, Any]]:
    """Return every concept in a chapter tagged mastered / available.

    Thin pass-through to the path engine. Nothing is ever locked. Each entry is
    a plain dict carrying the concept id/name/order, its roadmap status, the
    underlying progress detail, and `missing_prerequisites` (uncleared
    prerequisites, shown as "brush up first" hints) — enough to render a
    roadmap view with no further calls.

    Each entry also has `has_lesson`: whether a lesson exists yet for the
    student's interest, so the UI can show "coming soon" instead of a link to
    an empty page. (Omitted for an unknown, legacy-only student id.)

    Personalisation (2026-10-02, layer 2): `personal` is "known" (the starting
    check says they know it), "focus" (they showed a misconception) or None,
    with a student-facing `personal_note`; `recommended` marks the concept
    "Continue learning" would open.

    Raises:
        ValueError: if the chapter has no concepts / doesn't exist.
    """
    roadmap = engine.get_roadmap(student_id, chapter_id)
    profile = store.get_student(student_id)
    if profile is not None:
        _require_chapter_for_level(profile, chapter_id)
        ready = lesson_service.concepts_with_lessons(profile["interest"])
        state = learner_plan.learner_state(student_id)
        learner_plan.annotate_roadmap(roadmap, state)
        locks = _concept_locks(student_id, profile["interest"], roadmap, state)
        for row in roadmap:
            row["locked"] = locks.get(row["concept_id"]) is not None
            row["locked_reason"] = locks.get(row["concept_id"])
        _, _, chosen = _recommend(student_id, chapter_id, profile["interest"], state)
        for row in roadmap:
            row["has_lesson"] = row["concept_id"] in ready
            row["recommended"] = chosen is not None and row["concept_id"] == chosen.id
    return roadmap


def _recommend(
    student_id: str, chapter_id: str, interest: str, state: dict[str, Any] | None = None
) -> tuple[str, str, Any]:
    """(status, reason, concept or None): what "Continue learning" opens.

    The path engine decides first. A spaced review it asks for stands. Otherwise
    the learner plan may personalise the pick (skip what the starting check
    says they know, brush up a misconception first). Finally, a concept with
    no lesson yet in this interest is skipped to the next one that has one.
    """
    rec = engine.next_concept(student_id, chapter_id)
    status, reason = rec.kind, rec.reason
    chosen = rec.concept if rec.kind in (engine.KIND_NEW, engine.KIND_REVIEW) else None

    if rec.kind != engine.KIND_REVIEW:
        personal = learner_plan.personal_next(student_id, chapter_id, interest, state)
        if personal is not None:
            return engine.KIND_NEW, personal["reason"], engine.find_concept(personal["concept_id"])

    # Lessons are still being written, interest by interest. If the pick has
    # none yet in this student's interest, recommend the next unmastered concept
    # in the chapter that does, rather than sending "Continue learning" into an
    # empty page.
    if chosen is not None and not lesson_service.has_lesson(chosen.id, interest):
        ready = lesson_service.concepts_with_lessons(interest)
        fallback = next(
            (row for row in engine.get_roadmap(student_id, chapter_id)
             if row["concept_id"] in ready and row["status"] != engine.ROADMAP_MASTERED),
            None,
        )
        if fallback is not None:
            chosen = engine.find_concept(fallback["concept_id"])
            status, reason = engine.KIND_NEW, f"Next up: {chosen.name}."
    return status, reason, chosen


# ---------------------------------------------------------------------------
# 2b. The starting check and the learning plan (2026-10-02, layers 1 and 2)
#
#   get_diagnostic(student_id)                    -> questions, or the result if taken
#   submit_diagnostic(student_id, picks, hobbies) -> the result
#   get_learning_plan(student_id)                 -> what to focus on, where to start
#
# No model calls: the questions are existing lesson checks and grading is the
# same answer-key lookup. See src/learner/.
# ---------------------------------------------------------------------------

def _diagnostic_result(student_id: str) -> dict[str, Any]:
    rows = store.get_diagnostic_answers([student_id])
    return {
        "asked": len(rows),
        "known": sum(1 for r in rows if r["correct"]),
        "mix_ups": sum(1 for r in rows if r["correct"] is False),
        "unsure": sum(1 for r in rows if r["correct"] is None),
    }


def get_diagnostic(student_id: str) -> dict[str, Any]:
    """The starting check for this student.

    Returns:
        {"taken": bool, "completed_at": iso|None, "hobbies": [...],
         "hobby_options": [{id, label, emoji}], "questions": [...] (only while
         not taken: {concept_id, concept_name, chapter_name, question, options}),
         "result": {asked, known, mix_ups, unsure} (only once taken)}
    """
    profile = _require_student(student_id)
    learner = store.get_learner_profile(student_id)
    taken = learner["diagnostic_completed_at"] is not None
    out: dict[str, Any] = {
        "taken": taken,
        "completed_at": learner["diagnostic_completed_at"],
        "hobbies": learner["hobbies"],
        "hobby_options": diagnostic.hobby_options(),
    }
    if taken:
        out["result"] = _diagnostic_result(student_id)
    else:
        out["questions"] = diagnostic.student_questions(
            profile["level"], profile["interest"], diagnostic.form_for(student_id))
    return out


def submit_diagnostic(
    student_id: str,
    picks: dict[str, str],
    hobbies: list[str] | None = None,
    confidence: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Grade and store the starting check (once per student).

    `picks` maps concept_id -> "A".."D" or "unsure"; anything left out counts as
    "unsure". `confidence` maps concept_id -> sure | think | guess (optional). It is taken once, because it is the pilot's baseline: a retake
    after the lessons would overwrite the "before" picture.

    Returns: {"result": {...}, "plan": get_learning_plan(...)}.

    Raises:
        ConflictError: already taken.
        EcoLearnError: a pick for a concept not in this check, a bad option, or
                       bad hobbies.
    """
    profile = _require_student(student_id)
    if store.get_learner_profile(student_id)["diagnostic_completed_at"] is not None:
        raise ConflictError("You've already taken the starting check.")
    clean = diagnostic.clean_hobbies(hobbies)
    graded = diagnostic.grade(profile["level"], profile["interest"], picks or {},
                              diagnostic.form_for(student_id), confidence)
    store.save_diagnostic(student_id, clean, graded)
    return {"result": _diagnostic_result(student_id), "plan": get_learning_plan(student_id)}


def get_learning_plan(student_id: str) -> dict[str, Any]:
    """What EcoLearn suggests for this student, from the starting check and lessons.

    Returns:
        {"check": {"taken", "completed_at", asked, known, mix_ups, unsure},
         "focus": [{concept_id, concept_name, chapter_id, chapter_name, note,
                    source: "check"|"lesson"}]  (open mix-ups, in teaching order),
         "known": [{concept_id, concept_name}]  (likely known, not yet confirmed),
         "start": {chapter_id, chapter_name, reason} | None,
         "hobbies": [...]}
    """
    profile = _require_student(student_id)
    learner = store.get_learner_profile(student_id)
    state = learner_plan.learner_state(student_id)
    ready = lesson_service.concepts_with_lessons(profile["interest"])
    chapters = {c["id"]: c for c in engine.list_chapters()}
    concepts = {cid: engine.find_concept(cid)
                for cid in set(state["mix_ups"]) | state["likely_known"]}

    def by_order(cid: str) -> int:
        return concepts[cid].order if concepts[cid] else 0

    focus = []
    for cid in sorted(state["mix_ups"], key=by_order):
        c = concepts[cid]
        if c is None:
            continue
        focus.append({
            "concept_id": cid, "concept_name": c.name, "chapter_id": c.chapter_id,
            "chapter_name": chapters.get(c.chapter_id, {}).get("name"),
            "note": learner_plan.you_might(state["mix_ups"][cid]["text"]),
            "source": state["mix_ups"][cid]["source"],
            "has_lesson": cid in ready,
        })
    known = [{"concept_id": cid, "concept_name": concepts[cid].name}
             for cid in sorted(state["likely_known"], key=by_order) if concepts[cid]]

    # Where to start: the chapter of the first mix-up that has a lesson, in the
    # student's own class if possible; otherwise their class's first chapter
    # that still has something to learn.
    grade = 12 if "12" in (profile["level"] or "") else 11
    start = None
    fixable = [f for f in focus if f["has_lesson"]]
    own_class = [f for f in fixable if chapters.get(f["chapter_id"], {}).get("grade") == grade]
    if own_class or fixable:
        f = (own_class or fixable)[0]
        start = {"chapter_id": f["chapter_id"], "chapter_name": f["chapter_name"],
                 "reason": f"Your starting check found a mix-up in {f['concept_name']}."}
    else:
        by_chapter = engine.concept_ids_by_chapter()
        for chapter_id in scope_chapter_ids():
            if chapters.get(chapter_id, {}).get("grade") != grade:
                continue
            left = [c for c in by_chapter.get(chapter_id, [])
                    if c in ready and c not in state["cleared"] and c not in state["likely_known"]]
            if left:
                start = {"chapter_id": chapter_id, "chapter_name": chapters[chapter_id]["name"],
                         "reason": "The first chapter with something new for you."}
                break

    return {
        "check": {"taken": learner["diagnostic_completed_at"] is not None,
                  "completed_at": learner["diagnostic_completed_at"],
                  **_diagnostic_result(student_id)},
        "focus": focus,
        "known": known,
        "start": start,
        "hobbies": learner["hobbies"],
    }


def _enrol_experiments(student_id: str) -> dict[str, str]:
    """Give the student an arm in every enabled pilot experiment they aren't in yet; returns {experiment: arm}.

    Called when an account is made, and from `_profile` for accounts made before an experiment started.
    Arms are balanced within the student's class (src/learner/experiments.py) and never change.
    """
    arms = store.get_experiment_arms(student_id)
    missing = [e for e in experiments.enabled() if e["id"] not in arms]
    if missing:
        class_key = store.get_student_class_id(student_id) or "none"
        for exp in missing:
            arms[exp["id"]] = store.assign_experiment_arm(
                student_id, exp["id"], class_key,
                lambda counts, eid=exp["id"]: experiments.choose_arm(eid, student_id, counts))
    return arms


def _profile(student_id: str, *, arms: dict[str, str] | None = None) -> dict[str, Any]:
    """profiler.build over this student's rows (see src/learner/profiler.py), minus any insight a pilot
    experiment's control arm switches off for them. `arms` given (the pilot report) means read-only: no
    new arm is assigned."""
    saved = store.get_survey(student_id)
    activity = store.get_activity([student_id])
    first = [a for a in activity["answers"] if a["attempt_no"] == 1]
    events = learner_plan._answer_events(
        store.get_diagnostic_answers([student_id]), activity["answers"],
        store.get_end_check_answers([student_id]), store.get_review_answers([student_id]))
    arms = _enrol_experiments(student_id) if arms is None else arms
    return profiler.build(saved["traits"] if saved else None, survey.observed_reading(activity["views"]),
                          (sum(1 for a in first if a["correct"]), len(first)), events,
                          store.get_insight_dismissals(student_id),
                          experiments.suppressed_insights(arms), experiments.pref_overrides(arms))


def get_learner_profile(student_id: str) -> dict[str, Any]:
    """What EcoLearn thinks about this student, why, and what it does about it (the open learner profile).

    Rules only, no AI. Each insight is something the student said (the survey) or did (reading, checks,
    how sure they were), with its evidence in plain words and its effect on the app. The student can say
    "that's not me" to any of them (`set_insight`), which switches its effect off.

    Returns: {"insights": [{id, kind: "said"|"shown", title, detail, evidence: [str], effect, active}],
              "survey_taken": bool, "signals": {views, skim_share, first_try_right, first_try_answered,
              sure, sure_wrong}}

    Raises:
        NotFoundError: unknown student.
    """
    _require_student(student_id)
    built = _profile(student_id)
    return {"insights": built["insights"], "survey_taken": store.get_survey(student_id) is not None,
            "signals": built["signals"]}


def set_insight(student_id: str, insight_id: str, dismissed: bool) -> dict[str, Any]:
    """The student says "that's not me" to an insight (dismissed=True), or takes it back.

    Raises:
        NotFoundError: unknown student.
        EcoLearnError: not an insight the profile can produce.
    """
    _require_student(student_id)
    if insight_id not in profiler.INSIGHT_IDS:
        raise EcoLearnError(f"Unknown insight {insight_id!r}.")
    store.set_insight_dismissed(student_id, insight_id, bool(dismissed))
    return get_learner_profile(student_id)


def get_mix_ups(student_id: str) -> dict[str, Any]:
    """Every misconception this student has shown, and whether it's fixed.

    See learner_plan.mix_up_history for the rule: "fixed" needs a right answer
    to a DIFFERENT question on the concept; right again on the same question
    (after the app explained it) is "recheck".

    Returns:
        {"summary": {"active", "recheck", "fixed"},
         "items": [{concept_id, concept_name, chapter_id, chapter_name, note,
                    status, sure, times, found_in, found_at, fixed_in,
                    fixed_at, has_lesson}]}
        Active first (in teaching order), then recheck, then fixed (newest first).
    """
    profile = _require_student(student_id)
    history = learner_plan.mix_up_history(
        store.get_diagnostic_answers([student_id]),
        store.get_activity([student_id])["answers"],
        store.get_end_check_answers([student_id]),
        store.get_review_answers([student_id]),
    )
    ready = lesson_service.concepts_with_lessons(profile["interest"])
    chapters = {c["id"]: c["name"] for c in engine.list_chapters()}
    items = []
    for concept_id, record in history.items():
        concept = engine.find_concept(concept_id)
        if concept is None:
            continue
        items.append({
            "concept_id": concept_id, "concept_name": concept.name,
            "chapter_id": concept.chapter_id, "chapter_name": chapters.get(concept.chapter_id),
            "note": learner_plan.you_might(record["text"]),
            "order": concept.order, "has_lesson": concept_id in ready,
            **{k: v for k, v in record.items() if k != "text"},
        })
    rank = {learner_plan.ACTIVE: 0, learner_plan.RECHECK: 1, learner_plan.FIXED: 2}
    items.sort(key=lambda i: (rank[i["status"]], i["order"]))
    fixed = sorted((i for i in items if i["status"] == learner_plan.FIXED),
                   key=lambda i: i["fixed_at"], reverse=True)
    items = [i for i in items if i["status"] != learner_plan.FIXED] + fixed
    for i in items:
        del i["order"]
    return {
        "summary": {status: sum(1 for i in items if i["status"] == status)
                    for status in (learner_plan.ACTIVE, learner_plan.RECHECK, learner_plan.FIXED)},
        "items": items,
    }


# ---------------------------------------------------------------------------
# 2c. The end check (2026-10-02): the pilot's "after"
#
#   get_end_check(student_id)                   -> status, questions or result
#   submit_end_check(student_id, picks)         -> the before -> after result
#   get_class_checks(teacher_id, class_id)      -> the class's before -> after
#   set_class_end_check(teacher_id, class_id, open) -> open or close it
#
# The same concepts as the starting check, each asked with a parallel question
# (see src/learner/diagnostic.py: two counterbalanced forms). The teacher opens
# it for the class, so everyone takes it at the same point of the pilot.
# Students without a class (self-signup) never get it: there is no one to open
# it, and they aren't part of a pilot class. No model calls.
# ---------------------------------------------------------------------------

def _end_check_status(student_id: str, learner: dict[str, Any]) -> str:
    """taken | open | needs_start | not_open."""
    if learner["end_check_completed_at"] is not None:
        return "taken"
    class_id = store.get_student_class_id(student_id)
    klass = store.get_class(class_id) if class_id else None
    if klass is None or not klass.get("end_check_opened_at"):
        return "not_open"
    if learner["diagnostic_completed_at"] is None:
        return "needs_start"
    return "open"


def _studied(student_ids: list[str], until: dict[str, str | None]) -> dict[str, set[str]]:
    return metrics.studied_concepts(store.get_activity(student_ids), until)


def _student_comparison(student_id: str, completed_at: str | None) -> dict[str, Any]:
    """diagnostic.compare for one student, with concept names for the page."""
    comparison = diagnostic.compare(
        store.get_diagnostic_answers([student_id]),
        store.get_end_check_answers([student_id]),
        _studied([student_id], {student_id: completed_at}).get(student_id, set()),
    )
    for c in comparison["concepts"]:
        concept = engine.find_concept(c["concept_id"])
        c["concept_name"] = concept.name if concept else c["concept_id"]
    return comparison


def get_end_check(student_id: str) -> dict[str, Any]:
    """The end check for this student.

    Returns:
        {"status": "not_open" | "needs_start" | "open" | "taken",
         "completed_at": iso | None,
         "questions": [...]  (only when open: same shape as the starting check's),
         "comparison": {...} (only when taken: diagnostic.compare + concept_name)}
    """
    profile = _require_student(student_id)
    learner = store.get_learner_profile(student_id)
    status = _end_check_status(student_id, learner)
    out: dict[str, Any] = {"status": status, "completed_at": learner["end_check_completed_at"]}
    if status == "open":
        out["questions"] = diagnostic.present(diagnostic.choose_end_questions(
            profile["interest"], store.get_diagnostic_answers([student_id])))
    elif status == "taken":
        out["comparison"] = _student_comparison(student_id, learner["end_check_completed_at"])
    return out


def submit_end_check(
    student_id: str, picks: dict[str, str], confidence: dict[str, str] | None = None
) -> dict[str, Any]:
    """Grade and store the end check (once). Anything left out counts as "unsure".
    `confidence` maps concept_id -> sure | think | guess (optional).

    Returns: get_end_check(student_id) after saving (status "taken", with the comparison).

    Raises:
        ConflictError: already taken.
        EcoLearnError: not open for this student, a pick for a concept not in
                       the check, or a bad option.
    """
    profile = _require_student(student_id)
    learner = store.get_learner_profile(student_id)
    status = _end_check_status(student_id, learner)
    if status == "taken":
        raise ConflictError("You've already taken the end check.")
    if status == "needs_start":
        raise EcoLearnError("Take the starting check first: the end check is compared with it.")
    if status != "open":
        raise EcoLearnError("The end check isn't open yet. Your teacher will open it.")
    chosen = diagnostic.choose_end_questions(
        profile["interest"], store.get_diagnostic_answers([student_id]))
    store.save_end_check(student_id, diagnostic.grade_chosen(chosen, picks or {}, confidence))
    return get_end_check(student_id)


# ---------------------------------------------------------------------------
# "Getting to know you" (2026-10-08): the first-login survey
# ---------------------------------------------------------------------------

def get_survey(student_id: str) -> dict[str, Any]:
    """The survey for this student.

    Returns:
        {"taken": bool, "completed_at": iso | None,
         "sections": [...], "questions": [...], "hobby_options": [...], "hobbies": [...],
         "traits": {...}, "answers": {...}, "updated_at": iso | None, "revision": int
                                   (once taken: their answers, so a form can be prefilled,
                                    and what those answers mean)}
    """
    _require_student(student_id)
    row = store.get_survey(student_id)
    # The questions are public content and are always sent: answering AND updating need them.
    out = {
        "sections": survey.sections(), "questions": survey.questions(),
        "hobby_options": diagnostic.hobby_options(),
    }
    if row is not None:
        return {**out, "taken": True, "completed_at": row["completed_at"],
                "updated_at": row["updated_at"], "revision": row["revision"],
                "traits": row["traits"], "answers": row["answers"], "hobbies": row["answers"].get("hobbies", [])}
    return {**out, "taken": False, "completed_at": None,
            "hobbies": store.get_learner_profile(student_id)["hobbies"]}


def submit_survey(student_id: str, answers: dict[str, Any]) -> dict[str, Any]:
    """Validate and store the survey (once), keep the hobbies, derive the traits.

    Every question may be skipped: an empty submission is allowed and stores neutral traits.

    Returns: get_survey(student_id) after saving ("taken": True, with the traits).

    Raises:
        ConflictError: already taken.
        EcoLearnError: an unknown question or option, too many choices, or bad hobbies.
    """
    _require_student(student_id)
    if store.get_survey(student_id) is not None:
        raise ConflictError("You've already answered these.")
    cleaned = survey.clean(answers)
    traits = survey.derive_traits(cleaned)
    store.save_survey(student_id, survey.version(), cleaned, traits, cleaned.get("hobbies", []))
    return get_survey(student_id)


def update_survey(student_id: str, answers: dict[str, Any]) -> dict[str, Any]:
    """Replace the student's survey answers (they changed their mind, or grew).

    The old set is kept in the history, never shown to the teacher. Validated exactly like
    the first time; if anything is wrong, nothing changes.

    Returns: get_survey(student_id) after saving.

    Raises:
        EcoLearnError: not answered yet (do that first), or an invalid submission.
    """
    _require_student(student_id)
    if store.get_survey(student_id) is None:
        raise EcoLearnError("Answer the first questions before you update them.")
    cleaned = survey.clean(answers)
    traits = survey.derive_traits(cleaned)
    store.update_survey(student_id, survey.version(), cleaned, traits, cleaned.get("hobbies", []))
    return get_survey(student_id)


def get_class_learner_profiles(teacher_id: str, class_id: str) -> dict[str, Any]:
    """The class's "getting to know you" results, for the teacher.

    Returns:
        {"summary": {taken, total, focus: {short, medium, long}, pace: {...},
                     physics_feel: {...}, hobby_level: {novice, fan, player, expert}},
         "students": [{student_id, name, taken, summary: [lines], focus_span, hobby_level,
                       observed: {views, median_minutes, skim_share}}]}
    Observed reading (from lesson views) sits next to what the student said, so a teacher can
    see when the two disagree. Students who haven't taken it yet are listed with taken False.

    Raises:
        NotFoundError: not this teacher's class.
    """
    get_teacher_profile(teacher_id)
    _own_class(teacher_id, class_id)
    students = store.list_class_students(class_id)
    ids = [s["student_id"] for s in students]
    surveys = store.list_surveys(ids)
    views = store.get_activity(ids)["views"]
    by_student: dict[str, list[dict[str, Any]]] = {}
    for v in views:
        by_student.setdefault(v["student_id"], []).append(v)

    focus: dict[str, int] = {"short": 0, "medium": 0, "long": 0}
    pace: dict[str, int] = {}
    feel: dict[str, int] = {}
    level: dict[str, int] = {lvl: 0 for lvl in survey.HOBBY_LEVELS}
    rows = []
    for s in students:
        row = surveys.get(s["student_id"])
        observed = survey.observed_reading(by_student.get(s["student_id"], []))
        if row is None:
            rows.append({"student_id": s["student_id"], "name": s["name"], "taken": False,
                         "summary": [], "focus_span": None, "hobby_level": None,
                         "observed": observed})
            continue
        t = row["traits"]
        focus[t["focus"]["span"]] += 1
        if t["learning"].get("pace"):
            pace[t["learning"]["pace"]] = pace.get(t["learning"]["pace"], 0) + 1
        if t["physics"].get("feel"):
            feel[t["physics"]["feel"]] = feel.get(t["physics"]["feel"], 0) + 1
        top = next(iter(t["hobby_levels"].values()), None)
        if top:
            level[top["level"]] += 1
        rows.append({"student_id": s["student_id"], "name": s["name"], "taken": True,
                     "summary": t["summary"], "focus_span": t["focus"]["span"],
                     "hobby_level": top["level"] if top else None, "observed": observed,
                     "updated_at": row["updated_at"]})
    return {
        "summary": {"taken": len(surveys), "total": len(students), "focus": focus,
                    "pace": pace, "physics_feel": feel, "hobby_level": level},
        "students": rows,
    }


def _class_gains(student_ids: list[str]) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    """(metrics.check_gains, {student_id: compare}) for these students."""
    start_rows = store.get_diagnostic_answers(student_ids)
    end_rows = store.get_end_check_answers(student_ids)
    finished_at = {r["student_id"]: r["answered_at"] for r in end_rows}
    studied = _studied(student_ids, finished_at) if finished_at else {}

    def rows_of(rows: list[dict[str, Any]], sid: str) -> list[dict[str, Any]]:
        return [r for r in rows if r["student_id"] == sid]

    comparisons = {
        sid: diagnostic.compare(rows_of(start_rows, sid), rows_of(end_rows, sid),
                                studied.get(sid, set()))
        for sid in finished_at
    }
    concept_info, _ = _insight_lookups()
    started = len({r["student_id"] for r in start_rows})
    return metrics.check_gains(comparisons, started, concept_info), comparisons


def get_class_checks(teacher_id: str, class_id: str) -> dict[str, Any]:
    """The class's starting check -> end check, for the teacher.

    Returns:
        {"class": {...}, "open": bool, "opened_at": iso | None,
         "summary": metrics.check_gains(...),
         "students": [{student_id, name, username, started: bool,
                       finished: bool, before: {right, mix_up, unsure} | None,
                       after: {...} | None, fixed, slipped}]}

    Raises:
        NotFoundError: not this teacher's class.
    """
    get_teacher_profile(teacher_id)
    klass = _own_class(teacher_id, class_id)
    students = store.list_class_students(class_id)
    ids = [s["student_id"] for s in students]
    summary, comparisons = _class_gains(ids)
    start_rows: dict[str, list[dict[str, Any]]] = {}
    for r in store.get_diagnostic_answers(ids):
        start_rows.setdefault(r["student_id"], []).append(r)

    def whole_check(sid: str) -> dict[str, int]:
        return {"right": sum(1 for r in start_rows[sid] if r["correct"]),
                "mix_up": sum(1 for r in start_rows[sid] if r["correct"] is False),
                "unsure": sum(1 for r in start_rows[sid] if r["correct"] is None)}

    rows = []
    for s in sorted(students, key=lambda s: (s["name"].lower(), s["username"] or "")):
        sid = s["student_id"]
        comp = comparisons.get(sid)
        rows.append({
            "student_id": sid, "name": s["name"], "username": s["username"],
            "started": sid in start_rows,
            "finished": comp is not None,
            # Before: the pairs compared once both are taken, else the whole starting check.
            "before": comp["before"] if comp else (whole_check(sid) if sid in start_rows else None),
            "after": comp["after"] if comp else None,
            "fixed": comp["fixed"] if comp else None,
            "slipped": comp["slipped"] if comp else None,
        })
    return {"class": klass, "open": bool(klass.get("end_check_opened_at")),
            "opened_at": klass.get("end_check_opened_at"), "summary": summary, "students": rows}


def set_class_end_check(teacher_id: str, class_id: str, open_: bool) -> dict[str, Any]:
    """Open the end check for the class (students see it on their roadmap), or
    close it again. Answers already given are kept either way.

    Returns: get_class_checks(...).
    """
    get_teacher_profile(teacher_id)
    _own_class(teacher_id, class_id)
    store.set_class_end_check(class_id, bool(open_))
    return get_class_checks(teacher_id, class_id)


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
        _require_chapter_for_level(profile, concept.chapter_id)
        state = learner_plan.learner_state(student_id)
        why_locked = _concept_locks(student_id, profile["interest"],
                                    engine.get_roadmap(student_id, concept.chapter_id),
                                    state).get(concept_id)
        if why_locked:
            raise EcoLearnError(why_locked)
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
        _require_chapter_for_level(profile, chapter_id)
        status, reason, chosen = _recommend(student_id, chapter_id, profile["interest"])
        envelope = {
            "status": status,
            "reason": reason,
            "concept_id": chosen.id if chosen else None,
            "concept_name": chosen.name if chosen else None,
            "lesson": None,
        }

    # Load the lesson body when there's a concept to actually teach.
    if chosen is not None:
        lesson = lesson_service.get_lesson(chosen.id, profile["interest"])
        if lesson is None:
            # Shown to the student, so it says what to do, not how it's built.
            envelope["status"] = "lesson_missing"
            envelope["reason"] = (
                f"The {profile['interest']} lesson for {chosen.name} is still being "
                "written. Pick a chapter that's marked ready, or come back soon."
            )
        else:
            envelope["lesson"] = lesson.model_dump()
            # How this student likes lessons shaped: what they said in the survey, corrected by
            # what they did, minus anything they said "that's not me" to (src/learner/profiler.py).
            # Presentation only: nothing is hidden or locked.
            envelope["prefs"] = _profile(student_id)["prefs"]
            # Authored lessons carry their own sections and a multiple-choice
            # check. Send those alongside the legacy fields: the web app renders
            # section by section (so it can collapse the worked example) and
            # shows real options. `student_view` never includes the answer key —
            # grading happens on the server in submit_assessment.
            authored = lesson_service.get_authored_lesson(chosen.id, profile["interest"])
            if authored is not None:
                view = lesson_service.student_view(authored)
                envelope["lesson"]["title"] = view["title"]
                envelope["lesson"]["sections"] = view["sections"]
                envelope["lesson"]["check"] = view["check"]
                # Layer 3: a story written for this student's hobby, shown above
                # the lesson's own story. Written in the background; the next two
                # concepts are started too, so they're usually ready on arrival.
                envelope["lesson"]["personal_story"] = personal_story.view(student_id, chosen.id)
                # Practice with AI: the button shows only when a question could be written for them.
                envelope["practice_available"] = _practice_available(profile)
                for upcoming in _upcoming_concepts(student_id, chosen, profile["interest"], 2):
                    personal_story.request(student_id, upcoming)

    return envelope


def _upcoming_concepts(student_id: str, concept: Any, interest: str, count: int) -> list[str]:
    """The next `count` unfinished, written concepts after `concept` in its chapter."""
    ready = lesson_service.concepts_with_lessons(interest)
    rows = engine.get_roadmap(student_id, concept.chapter_id)
    ids = [r["concept_id"] for r in rows]
    after = rows[ids.index(concept.id) + 1:] if concept.id in ids else []
    return [r["concept_id"] for r in after
            if r["concept_id"] in ready and r["status"] != engine.ROADMAP_MASTERED][:count]


def get_personal_story(student_id: str, concept_id: str) -> dict[str, Any]:
    """The personal story for one concept: ready, pending (poll again) or none.

    See src/learner/personal_story.py. Never raises for a missing story — "none"
    simply means the page shows the lesson's own story.
    """
    _require_student(student_id)
    if engine.find_concept(concept_id) is None:
        raise NotFoundError(f"Unknown concept_id {concept_id!r}.")
    return personal_story.view(student_id, concept_id)


# Why a student can report a story. Fixed choices, no free text: a child's
# typed comment is personal data we'd rather not hold, and a reason code is
# enough for a teacher to know what to look for.
STORY_REPORT_REASONS = {
    "wrong_physics": "The physics seems wrong",
    "confusing": "It's confusing",
    "not_appropriate": "It's not appropriate",
    "other": "Something else",
}


def report_personal_story(student_id: str, concept_id: str, reason: str) -> dict[str, Any]:
    """A student reports the story written for them. It is hidden from them at
    once (they see the lesson's own story) and shows up for their teacher.

    Raises:
        EcoLearnError: an unknown reason.
        NotFoundError: no story was shown to this student for this concept.
    """
    _require_student(student_id)
    if reason not in STORY_REPORT_REASONS:
        raise EcoLearnError(f"Reason must be one of: {', '.join(STORY_REPORT_REASONS)}.")
    row = store.get_personal_story(student_id, concept_id)
    if row is None or row["status"] != personal_story.READY:
        raise NotFoundError("There's no story to report here.")
    store.set_story_visibility(student_id, concept_id, hidden=True, hidden_by="student",
                               report_reason=reason)
    return {"concept_id": concept_id, "reported": True, "reason": reason}


def list_class_stories(teacher_id: str, class_id: str) -> dict[str, Any]:
    """Every personal story written for students in one of the teacher's classes.

    Reported ones first, then the newest. Each carries the full text, so a
    teacher reads exactly what the student saw.

    Returns:
        {"summary": {written, showing, reported, hidden_by_teacher, not_written},
         "stories": [{student_id, name, username, concept_id, concept_name,
                      chapter_name, hobby, emoji, story, analogy, limit, model,
                      created_at, hidden, hidden_by, report_reason,
                      report_label, reported_at}]}
        `not_written` counts attempts that failed the checks or found no fit
        (the student saw the reviewed story instead).

    Raises:
        NotFoundError: not this teacher's class.
    """
    get_teacher_profile(teacher_id)
    _own_class(teacher_id, class_id)
    students = {s["student_id"]: s for s in store.list_class_students(class_id)}
    rows = store.list_personal_stories(list(students))
    hobbies = personal_story._hobby_table()
    chapter_names = {c["id"]: c["name"] for c in engine.list_chapters()}

    stories = []
    for r in rows:
        if r["status"] != personal_story.READY:
            continue
        concept = engine.find_concept(r["concept_id"])
        hobby = hobbies.get(r["hobby"], {"label": r["hobby"].capitalize(), "emoji": "✨"})
        student = students[r["student_id"]]
        stories.append({
            "student_id": r["student_id"], "name": student["name"], "username": student["username"],
            "concept_id": r["concept_id"], "concept_name": concept.name if concept else r["concept_id"],
            "chapter_name": chapter_names.get(concept.chapter_id) if concept else None,
            "hobby": hobby["label"], "emoji": hobby.get("emoji", ""),
            "story": r["story"], "analogy": r["analogy"], "limit": r["limit_text"],
            "model": r["model"], "created_at": r["created_at"],
            "hidden": r["hidden"], "hidden_by": r["hidden_by"],
            "report_reason": r["report_reason"],
            "report_label": STORY_REPORT_REASONS.get(r["report_reason"] or ""),
            "reported_at": r["reported_at"],
        })
    # Reported first (newest report first), then everything else newest first.
    stories.sort(key=lambda s: s["created_at"], reverse=True)
    stories.sort(key=lambda s: (s["reported_at"] is None, -_epoch(s["reported_at"])))
    return {
        "summary": {
            "written": len(stories),
            "showing": sum(1 for s in stories if not s["hidden"]),
            "reported": sum(1 for s in stories if s["reported_at"]),
            "hidden_by_teacher": sum(1 for s in stories if s["hidden"] and s["hidden_by"] == "teacher"),
            "not_written": sum(1 for r in rows if r["status"] in (personal_story.FAILED,
                                                                  personal_story.NO_FIT)),
        },
        "stories": stories,
    }


# What each status means to a teacher, for the decision log.
_STORY_OUTCOME = {
    "ready": "Shown to the student",
    "failed": "Blocked: the student saw the reviewed lesson story",
    "no_fit": "Declined: no honest link to this hobby, so the reviewed story",
    "error": "Model unavailable: the student saw the reviewed lesson story",
}


def get_class_ai_decisions(teacher_id: str, class_id: str, limit: int = 30) -> dict[str, Any]:
    """"How the AI decided" for one of the teacher's classes: every guardrail at
    work, and the step-by-step record behind each personal story.

    Returns:
        {"stories": {attempted, shown, first_draft, rewritten, blocked, declined,
                     errors, reported, hidden_by_teacher, rules_rejections,
                     critic_checks, critic_rejections},
         "help": {asked, answered, failed, rate_limited, blocked: {reason: n}}  (doubt chat, counts only),
         "plans": {total, agent, rules, latest_note},
         "calls": {total, failed, by_feature: {feature: {calls, failed,
                   median_latency_ms}}},
         "log": [{student_id, name, concept_id, concept_name, hobby, emoji,
                  status, outcome, attempts, model, created_at, hidden,
                  reported, trail: [{attempt, step, passed, problems, model}]}]}
        `log` is newest first, at most `limit` stories. Stories written before
        the trail existed have an empty trail.

    Raises:
        NotFoundError: not this teacher's class.
    """
    get_teacher_profile(teacher_id)
    _own_class(teacher_id, class_id)
    students = {s["student_id"]: s for s in store.list_class_students(class_id)}
    rows = store.list_personal_stories(list(students))
    hobbies = personal_story._hobby_table()
    steps = [t for r in rows for t in r["trail"]]
    ready = [r for r in rows if r["status"] == personal_story.READY]
    stories = {
        "attempted": len(rows),
        "shown": sum(1 for r in ready if not r["hidden"]),
        "first_draft": sum(1 for r in ready if r["attempts"] == 1),
        "rewritten": sum(1 for r in ready if r["attempts"] > 1),
        "blocked": sum(1 for r in rows if r["status"] == personal_story.FAILED),
        "declined": sum(1 for r in rows if r["status"] == personal_story.NO_FIT),
        "errors": sum(1 for r in rows if r["status"] == personal_story.ERROR),
        "reported": sum(1 for r in rows if r["reported_at"]),
        "hidden_by_teacher": sum(1 for r in rows if r["hidden"] and r["hidden_by"] == "teacher"),
        "rules_rejections": sum(1 for t in steps if t["step"] in ("rules", "format") and not t["passed"]),
        "critic_checks": sum(1 for t in steps if t["step"] == "critic"),
        "critic_rejections": sum(1 for t in steps if t["step"] == "critic" and not t["passed"]),
    }

    plans = store.list_class_plans(class_id)
    calls = [c for c in store.get_llm_calls()
             if c["class_id"] == class_id or c["student_id"] in students]
    by_feature: dict[str, dict[str, Any]] = {}
    for feature in sorted({c["feature"] for c in calls}):
        mine = [c for c in calls if c["feature"] == feature]
        latencies = sorted(c["latency_ms"] for c in mine if c["latency_ms"] is not None)
        by_feature[feature] = {
            "calls": len(mine), "failed": sum(1 for c in mine if not c["ok"]),
            "median_latency_ms": latencies[len(latencies) // 2] if latencies else None,
        }

    log = []
    for r in rows[:limit]:
        concept = engine.find_concept(r["concept_id"])
        hobby = hobbies.get(r["hobby"], {"label": r["hobby"].capitalize(), "emoji": "✨"})
        log.append({
            "student_id": r["student_id"], "name": students[r["student_id"]]["name"],
            "concept_id": r["concept_id"], "concept_name": concept.name if concept else r["concept_id"],
            "hobby": hobby["label"], "emoji": hobby.get("emoji", ""),
            "status": r["status"],
            "outcome": ("Hidden by you: the student sees the reviewed story"
                        if r["hidden"] and r["hidden_by"] == "teacher"
                        else "Reported by the student, so hidden from them" if r["hidden"]
                        else _STORY_OUTCOME.get(r["status"], r["status"])),
            "attempts": r["attempts"], "model": r["model"], "created_at": r["created_at"],
            "hidden": r["hidden"], "reported": bool(r["reported_at"]), "trail": r["trail"],
        })
    return {
        "stories": stories,
        "help": store.help_event_counts(list(students)),
        # Practice with AI (2026-10-19): counts only; "thrown_away" = attempts the checks rejected.
        "practice": store.practice_counts(list(students)),
        "plans": {"total": len(plans),
                  "agent": sum(1 for p in plans if p["source"] == "agent"),
                  "rules": sum(1 for p in plans if p["source"] != "agent"),
                  "latest_note": plans[0]["note"] if plans else None},
        "calls": {"total": len(calls), "failed": sum(1 for c in calls if not c["ok"]),
                  "by_feature": by_feature},
        "log": log,
    }


def _epoch(iso: str | None) -> float:
    return datetime.fromisoformat(iso).timestamp() if iso else 0.0


def set_class_story_hidden(
    teacher_id: str, student_id: str, concept_id: str, hidden: bool
) -> dict[str, Any]:
    """A teacher hides a story (the student sees the reviewed one) or shows it
    again — including one the student reported, if the teacher judges it fine.
    The student's report stays on record either way.

    Raises:
        NotFoundError: the student isn't in this teacher's classes, or there's
                       no such story (one answer, like password resets).
    """
    get_teacher_profile(teacher_id)
    class_id = store.get_student_class_id(student_id)
    try:
        if class_id is None:
            raise NotFoundError("")
        _own_class(teacher_id, class_id)
    except NotFoundError:
        raise NotFoundError("Story not found in your classes.") from None
    if not store.set_story_visibility(student_id, concept_id, hidden=bool(hidden),
                                      hidden_by="teacher" if hidden else None):
        raise NotFoundError("Story not found in your classes.")
    return {"student_id": student_id, "concept_id": concept_id, "hidden": bool(hidden)}


# ---------------------------------------------------------------------------
# 4. Assessment
# ---------------------------------------------------------------------------

def _grade_multiple_choice(
    student_id: str,
    concept_id: str,
    answer: str,
    authored: Any,
    interest: str,
    confidence: str | None = None,
) -> dict[str, Any]:
    """Grade one multiple-choice pick against an authored lesson's answer key.

    No model call: the answer key and the per-option misconceptions are written
    into the lesson file, so this is pure lookup. `answer` is the option letter;
    anything else is the student's mistake to fix, not a server error, so it
    raises EcoLearnError (→ 400) without touching their progress.

    Every valid pick is also logged (store.record_answer) with the misconception
    it reveals, for the teacher's misconception view. `progress` keeps only the
    best score, which would hide what the student first got wrong.
    """
    check = authored.check
    picked = (answer or "").strip().upper()
    if picked not in check.options:
        raise EcoLearnError(
            f"Pick one of the options ({', '.join(check.options)}) — got {answer!r}."
        )

    sure = diagnostic.clean_confidence(confidence)
    correct = picked == check.answer

    if correct:
        feedback = f"Correct. {check.explanation.strip()}"
    else:
        why_wrong = (check.misconceptions.get(picked) or "").strip()
        feedback = (
            f"Not quite. {why_wrong}\n\n"
            f"The right answer is **{check.answer}**. {check.explanation.strip()}"
        ).strip()
    # How sure they were changes what the result means, so say it.
    if not correct and sure == "sure":
        feedback += ("\n\nYou were sure of this one, which makes it a mix-up worth fixing "
                     "properly. It's on your mix-ups list until you get a different question "
                     "on it right.")
    elif correct and sure == "guess":
        feedback += "\n\nYou guessed right. Read the explanation above so it sticks."

    logged = store.record_answer(
        student_id, concept_id, interest, picked, correct,
        None if correct else (check.misconceptions.get(picked) or "").strip() or None,
        sure,
    )
    # Scored AFTER recording, because this answer is part of the evidence.
    score, note = _mastery_score(student_id, concept_id, correct)
    updated = store.update_progress(student_id, concept_id, score)
    return {
        "concept_id": concept_id,
        "score": score,
        "attempt_no": logged["attempt_no"],
        "mastery_signal": _SIGNAL[score],
        "mastery_note": note,
        "feedback": feedback,
        "missing_concepts": [],
        "graded_question": check.question,
        "mastery": updated,
        # Multiple-choice extras the web app shows; absent for legacy grading.
        "correct": correct,
        "selected_option": picked,
        "correct_option": check.answer,
        "confidence": sure,
    }


# ---------------------------------------------------------------------------
# Mastery from evidence (2026-10-03)
#
# One right answer used to mean "mastered", and after a wrong pick the app
# shows the right answer, so a retry was nearly free. Now a concept is
# MASTERED only when the student has answered TWO DIFFERENT questions on it
# right (learner_plan.mastery_evidence): the starting check, a lesson check,
# the end check and revision questions all count, but not a question they got
# wrong first. One right answer is "cleared" (score 2): the path moves on, and
# the concept goes in the revision queue for a fresh question later.
# ---------------------------------------------------------------------------

_SIGNAL = {3: "mastered", 2: "partial", 0: "not_yet"}


def _concept_rows(student_id: str, concept_id: str) -> tuple[list, list, list, list]:
    """(starting check, lesson, end check, revision) answers for one concept."""
    return store.get_concept_answers(student_id, concept_id)


def _mastery_score(student_id: str, concept_id: str, correct: bool) -> tuple[int, str | None]:
    """(score to record, a sentence for the student) after an answer is stored."""
    if not correct:
        return 0, None
    events = learner_plan._answer_events(*_concept_rows(student_id, concept_id)).get(concept_id, [])
    evidence = learner_plan.mastery_evidence(events)
    if len(evidence) >= learner_plan.MASTERY_EVIDENCE:
        return 3, "That's two different questions on this idea answered right: mastered."
    if not evidence:
        return 2, ("Right, now that you've seen why. It's in your revision list: get a new "
                   "question on it right to show it's stuck.")
    return 2, ("One more right answer, on a different question, masters it. It's in your "
               "revision list for tomorrow.")


# Revision questions wait this long after the last answer: spacing helps it stick.
_DEFAULT_REVISION_HOURS = 20


def _revision_hours() -> float:
    raw = os.getenv("ECOLEARN_REVISION_HOURS")
    try:
        return max(0.0, float(raw)) if raw not in (None, "") else _DEFAULT_REVISION_HOURS
    except ValueError:
        return _DEFAULT_REVISION_HOURS


def _fresh_question(concept_id: str, rows: tuple[list, list, list, list]) -> str | None:
    """An interest whose check on this concept the student has never seen, or None."""
    start, lesson, end, review = rows
    seen = ({r["source_interest"] for r in start} | {r["interest"] for r in lesson}
            | {r["source_interest"] for r in end} | {r["interest"] for r in review})
    for interest in diagnostic.load_config()["source_interests"]:
        if interest not in seen and lesson_service.get_authored_lesson(concept_id, interest):
            return interest
    return None


# Mastered ideas come back to "keep it fresh" on a widening schedule: a week, then three weeks, then
# nine (each right revision answer widens it); a wrong one brings it back in two days (2026-10-14).
_REFRESH_DAYS = (7, 21, 63)
_REFRESH_AFTER_WRONG_DAYS = 2


def _refresh_days(review_rows: list[dict[str, Any]]) -> int:
    """How long a mastered concept waits before a keep-it-fresh question."""
    if review_rows and not sorted(review_rows, key=lambda r: r["answered_at"])[-1]["correct"]:
        return _REFRESH_AFTER_WRONG_DAYS
    right = sum(1 for r in review_rows if r["correct"])
    return _REFRESH_DAYS[min(right, len(_REFRESH_DAYS) - 1)]


def get_revision(student_id: str) -> dict[str, Any]:
    """The revision queue. Nothing is locked: a concept that isn't due yet can still be tried.

    Three kinds of item, each with a fresh question (another interest's lesson check it hasn't seen):
      * "teacher":  the student's teacher approved this from a coaching note; due now, listed first. If no
                    unseen question is left, the student's own lesson check is asked again;
      * "partial":  answered right but not yet mastered; due ECOLEARN_REVISION_HOURS (default 20) after
                    the last answer, HALF that when the student was sure of a wrong answer on it and the
                    profile's "sure but wrong" insight is on (src/learner/profiler.py);
      * "refresh":  mastered; comes back after 7, then 21, then 63 days (2 after a wrong answer).

    Returns:
        {"due": [...], "later": [...], "no_fresh_question": n}, each item {concept_id, concept_name,
         chapter_id, chapter_name, kind, reason, due_at, due}. Partial concepts with no unseen
         question left are left out and counted.
    """
    _require_student(student_id)
    progress = store.get_progress(student_id)
    chapters = {c["id"]: c["name"] for c in engine.list_chapters()}
    hours = _revision_hours()
    sooner = set(_profile(student_id)["sooner"])
    assigned = {a["concept_id"]: a for a in store.open_revise_actions(student_id)}
    now = datetime.now(timezone.utc)
    due, later, no_fresh = [], [], 0

    def item(concept: Any, kind: str, reason: str, due_at: datetime) -> dict[str, Any]:
        return {"concept_id": concept.id, "concept_name": concept.name, "chapter_id": concept.chapter_id,
                "chapter_name": chapters.get(concept.chapter_id), "kind": kind, "reason": reason,
                "due_at": due_at.isoformat(), "due": due_at <= now,
                "order": (0 if kind == "teacher" else 1 if concept.id in sooner else 2, concept.order)}

    items = []
    for concept_id, action in assigned.items():
        concept = engine.find_concept(concept_id)
        if concept is not None:
            items.append(item(concept, "teacher", "Your teacher asked you to have another go at this one.",
                              datetime.fromisoformat(action["created_at"])))
    for concept_id, row in progress.items():
        if concept_id in assigned or row["status"] not in (store.STATUS_PARTIAL, store.STATUS_MASTERED):
            continue
        concept = engine.find_concept(concept_id)
        if concept is None:
            continue
        rows = _concept_rows(student_id, concept_id)
        if _fresh_question(concept_id, rows) is None:
            no_fresh += int(row["status"] == store.STATUS_PARTIAL)
            continue
        last = datetime.fromisoformat(
            max((r["answered_at"] for group in rows for r in group), default=row["last_seen"]))
        if row["status"] == store.STATUS_MASTERED:
            days = _refresh_days(rows[3])
            items.append(item(concept, "refresh", "Mastered. A quick question to keep it fresh.",
                              last + timedelta(days=days)))
            continue
        events = learner_plan._answer_events(*rows).get(concept_id, [])
        if concept_id in sooner:
            reason, wait = "You were sure of a wrong answer here, so it comes back sooner.", hours / 2
        elif learner_plan.mastery_evidence(events):
            reason, wait = "Right once. One more, on a new question, masters it.", hours
        else:
            reason, wait = "Right after the explanation. Show it on a new question.", hours
        items.append(item(concept, "partial", reason, last + timedelta(hours=wait)))
    for it in items:
        (due if it["due"] else later).append(it)
    due.sort(key=lambda i: (i["order"], i["due_at"]))
    later.sort(key=lambda i: (i["due_at"], i["order"]))
    for it in due + later:
        del it["order"]
    return {"due": due, "later": later, "no_fresh_question": no_fresh}


def _revision_target(student_id: str, concept_id: str) -> tuple[Any, str]:
    """(the lesson to ask from, its interest) for a concept in the queue."""
    status = store.get_progress(student_id).get(concept_id, {}).get("status")
    assigned = any(a["concept_id"] == concept_id for a in store.open_revise_actions(student_id))
    if not assigned and status not in (store.STATUS_PARTIAL, store.STATUS_MASTERED):
        raise NotFoundError("That concept isn't in your revision list.")
    interest = _fresh_question(concept_id, _concept_rows(student_id, concept_id))
    if interest is None and assigned:
        # The teacher asked for another go and every question has been seen: ask their own lesson's again.
        own = (store.get_student(student_id) or {}).get("interest")
        if own and lesson_service.get_authored_lesson(concept_id, own):
            interest = own
    if interest is None:
        raise NotFoundError("There's no new question on that concept yet.")
    return lesson_service.get_authored_lesson(concept_id, interest), interest


def get_revision_question(student_id: str, concept_id: str) -> dict[str, Any]:
    """The fresh question for a concept in the revision queue (no answer key).

    Returns: {concept_id, concept_name, chapter_name, question, options}.

    Raises:
        NotFoundError: not in the queue, or no unseen question left.
    """
    _require_student(student_id)
    _, interest = _revision_target(student_id, concept_id)
    return diagnostic.present([{"concept_id": concept_id, "source_interest": interest}])[0]


def submit_revision(
    student_id: str, concept_id: str, answer: str, confidence: str | None = None
) -> dict[str, Any]:
    """Grade a revision answer, record it, and update mastery.

    Returns: {concept_id, correct, selected_option, correct_option, feedback,
              mastery_signal, mastery_note, mastery: the progress row}.

    Raises:
        NotFoundError: not in the queue / no fresh question.
        EcoLearnError: not one of the options, or a bad confidence.
    """
    _require_student(student_id)
    authored, interest = _revision_target(student_id, concept_id)
    check = authored.check
    picked = (answer or "").strip().upper()
    if picked not in check.options:
        raise EcoLearnError(f"Pick one of the options ({', '.join(check.options)}) — got {answer!r}.")
    sure = diagnostic.clean_confidence(confidence)
    correct = picked == check.answer
    misconception = None if correct else (check.misconceptions.get(picked) or "").strip() or None
    store.record_review_answer(student_id, concept_id, interest, picked, correct, misconception, sure)
    store.close_revise_actions(student_id, concept_id, correct)  # a teacher-assigned revision, if any
    score, note = _mastery_score(student_id, concept_id, correct)
    updated = store.update_progress(student_id, concept_id, score)
    if correct:
        feedback = f"Correct. {check.explanation.strip()}"
    else:
        feedback = (f"Not quite. {misconception or ''}\n\n"
                    f"The right answer is **{check.answer}**. {check.explanation.strip()}").strip()
        note = "It's back on your mix-ups list. Open the lesson again when you're ready."
    return {"concept_id": concept_id, "correct": correct, "selected_option": picked,
            "correct_option": check.answer, "feedback": feedback,
            "mastery_signal": _SIGNAL[score] if correct else "not_yet",
            "mastery_note": note, "mastery": updated}


def submit_assessment(
    student_id: str,
    concept_id: str,
    answer: str,
    confidence: str | None = None,
) -> dict[str, Any]:
    """Grade a student's answer to a concept's self-check and update mastery.

    Two paths, chosen by what the lesson is:

    * **Authored lessons (all new content): multiple choice, no LLM.** `answer`
      is the option letter the student picked ("A".."D"). It is checked against
      the answer key in the lesson file, which never leaves the server. Correct
      scores 3, wrong scores 0, and the feedback is the lesson's own written
      explanation plus, for a wrong pick, the misconception that option was
      designed to catch. This is instant, free and deterministic — the reason
      grading needs no model and no API key.
    * **Legacy JSON lessons: free text, graded by the Assessor.** Kept so older
      generated lessons and Streamlit keep working.

    Either way the 0-3 score is written to the progress store, advancing the
    student's mastery. `confidence` (sure | think | guess) is the student's
    "how sure are you?" for a multiple-choice pick; optional, ignored for
    legacy free-text grading.

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

    authored = lesson_service.get_authored_lesson(concept_id, profile["interest"])
    if authored is not None:
        return _grade_multiple_choice(
            student_id, concept_id, answer, authored, profile["interest"], confidence
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
# 4b. Pilot metrics (2026-10-02)
#
# The evidence for the pilot: which lessons students open, how long they
# actually read, what they get wrong first time (and which misconception that
# reveals), and whether the interest-based explanation worked for them (👍/👎).
#
#   start_lesson_view(student_id, concept_id)            -> {view_id, rating, ...}
#   record_lesson_time(student_id, view_id, seconds)     -> {view_id, active_seconds}
#   rate_lesson(student_id, concept_id, rating)          -> {concept_id, rating, ...}
#   get_class_insights(teacher_id, class_id)             -> dashboard data
#   pilot_report()                                       -> everything, pseudonymised
#
# Multiple-choice answers are logged by _grade_multiple_choice, not here.
# Nothing in this section calls a model.
# ---------------------------------------------------------------------------

# A view can't honestly hold more reading time than this. A tab left open over
# lunch shouldn't turn into an hour of "reading" in the pilot numbers.
_MAX_VIEW_SECONDS = 30 * 60
# Reported time may run slightly ahead of the server's clock (network delay).
_CLOCK_SLACK_SECONDS = 30


def _new_view_id() -> str:
    return f"view_{uuid.uuid4().hex}"


def _require_student(student_id: str) -> dict[str, Any]:
    profile = store.get_student(student_id)
    if profile is None:
        raise NotFoundError(f"Unknown student_id {student_id!r}.")
    return profile


def start_lesson_view(student_id: str, concept_id: str) -> dict[str, Any]:
    """Record that a student opened a lesson; return its view id and their rating.

    The web app calls this once when a lesson appears, then reports reading
    time against the view id. The student's current 👍/👎 for the lesson comes
    back too, so the page can show it without a second request.

    Raises:
        NotFoundError: unknown student or concept, or no lesson in their interest.
    """
    profile = _require_student(student_id)
    if engine.find_concept(concept_id) is None:
        raise NotFoundError(f"Unknown concept_id {concept_id!r}.")
    interest = profile["interest"]
    if not lesson_service.has_lesson(concept_id, interest):
        raise NotFoundError(f"No lesson for {concept_id!r} in {interest!r}.")
    view = store.create_lesson_view(_new_view_id(), student_id, concept_id, interest)
    return {
        "view_id": view["view_id"],
        "concept_id": concept_id,
        "interest": interest,
        "rating": store.get_lesson_rating(student_id, concept_id, interest),
    }


def record_lesson_time(student_id: str, view_id: str, active_seconds: int) -> dict[str, Any]:
    """Update how long a student has actively spent on one lesson view.

    `active_seconds` is the running total the browser measured: time with the
    tab visible and the student not idle. It is clamped to what is physically
    possible — never more than the time since the view opened, never more than
    30 minutes — and only ever raised, so repeated or late reports are harmless.

    Raises:
        NotFoundError: the view doesn't exist or isn't this student's (one
                       answer for both, so view ids can't be probed).
    """
    view = store.get_lesson_view(view_id) if view_id else None
    if view is None or view["student_id"] != student_id:
        raise NotFoundError("Lesson view not found.")
    try:
        seconds = int(active_seconds)
    except (TypeError, ValueError):
        raise EcoLearnError("active_seconds must be a whole number.") from None

    opened = datetime.fromisoformat(view["opened_at"])
    elapsed = (datetime.now(tz=timezone.utc) - opened).total_seconds()
    ceiling = min(_MAX_VIEW_SECONDS, int(elapsed) + _CLOCK_SLACK_SECONDS)
    seconds = max(0, min(seconds, ceiling))

    store.set_lesson_view_seconds(view_id, seconds)
    updated = store.get_lesson_view(view_id) or view
    return {"view_id": view_id, "active_seconds": updated["active_seconds"]}


def rate_lesson(student_id: str, concept_id: str, rating: int) -> dict[str, Any]:
    """Save a student's 👍 (1) or 👎 (-1) for a lesson in their interest; 0 clears it.

    Raises:
        EcoLearnError: a rating other than 1, -1 or 0.
        NotFoundError: unknown student or concept, or no lesson to rate.
    """
    if rating not in (1, -1, 0):
        raise EcoLearnError("Rating must be 1 (helpful), -1 (not helpful) or 0 (clear).")
    profile = _require_student(student_id)
    if engine.find_concept(concept_id) is None:
        raise NotFoundError(f"Unknown concept_id {concept_id!r}.")
    interest = profile["interest"]
    if not lesson_service.has_lesson(concept_id, interest):
        raise NotFoundError(f"No lesson for {concept_id!r} in {interest!r}.")
    store.set_lesson_rating(student_id, concept_id, interest, rating)
    return {"concept_id": concept_id, "interest": interest, "rating": rating}


def _insight_lookups():
    """The two lookups metrics.class_insights needs, memoised for one call.

    Reading a lesson file per misconception would re-parse the same file many
    times for a busy class; a dict per call is enough.
    """
    chapter_names = {c["id"]: c["name"] for c in engine.list_chapters()}
    concepts: dict[str, dict[str, Any]] = {}
    checks: dict[tuple[str, str], dict[str, Any] | None] = {}

    def concept_info(concept_id: str) -> dict[str, Any]:
        if concept_id not in concepts:
            concept = engine.find_concept(concept_id)
            concepts[concept_id] = (
                {"name": concept.name, "chapter_id": concept.chapter_id,
                 "chapter_name": chapter_names.get(concept.chapter_id)}
                if concept is not None else {"name": concept_id}
            )
        return concepts[concept_id]

    def check_info(concept_id: str, interest: str) -> dict[str, Any] | None:
        key = (concept_id, interest)
        if key not in checks:
            authored = lesson_service.get_authored_lesson(concept_id, interest)
            checks[key] = (
                {"question": authored.check.question, "options": dict(authored.check.options),
                 "answer": authored.check.answer}
                if authored is not None else None
            )
        return checks[key]

    return concept_info, check_info


def get_class_insights(teacher_id: str, class_id: str) -> dict[str, Any]:
    """Pilot metrics and the misconception view for one of the teacher's classes.

    Returns:
        {
          "class":          the class summary,
          "summary":        headline numbers (lessons opened, active minutes,
                            first-try accuracy, 👍/👎 ...),
          "misconceptions": wrong answers grouped by the misconception they
                            reveal, most common first, with the question and
                            option text so a teacher can discuss it in class,
          "concepts":       per concept, hardest (lowest first-try accuracy) first,
          "interests":      the same numbers per interest,
          "students":       per student, with name and username,
        }
        The answer key appears here (correct_option) — this is a teacher view.

    Raises:
        NotFoundError: not this teacher's class.
    """
    return _class_insights(teacher_id, class_id)


def _class_insights(teacher_id: str, class_id: str, exclude: set[str] | frozenset[str] = frozenset()
                    ) -> dict[str, Any]:
    """`get_class_insights`, leaving out the students in `exclude` (the teaching assistant uses this
    to leave out students whose AI switch is off: their data never reaches the model)."""
    get_teacher_profile(teacher_id)
    klass = _own_class(teacher_id, class_id)
    students = [s for s in store.list_class_students(class_id) if s["student_id"] not in exclude]
    activity = store.get_activity([s["student_id"] for s in students])
    concept_info, check_info = _insight_lookups()
    insights = metrics.class_insights(students, activity, concept_info, check_info)

    by_id = {s["student_id"]: s for s in students}
    for row in insights["students"]:
        student = by_id[row["student_id"]]
        row.update(name=student["name"], username=student["username"],
                   interest=student["interest"], mastered=student["mastered"],
                   last_active=student["last_active"])
    insights["students"].sort(key=lambda r: (r["name"].lower(), r["username"] or ""))
    return {"class": klass, **insights}


# ---------------------------------------------------------------------------
# 4c. The teacher agent (2026-10-02)
#
#   get_class_plan(teacher_id, class_id)       -> the latest plan, or None
#   generate_class_plan(teacher_id, class_id)  -> a new plan (agent, or rules)
#
# The ONE live model call a teacher can trigger. It is low-volume (a teacher
# clicks a button, a few times a day), read-only, and never on a student's
# path, so it doesn't touch the cached-lesson strategy. See
# src/agents/teacher_agent.py for the guardrails.
# ---------------------------------------------------------------------------

# A plan younger than this is returned instead of making a new one, so a
# double-click (or an impatient teacher) doesn't spend quota twice.
_PLAN_REUSE_SECONDS = 60


def _class_toolbox(teacher_id: str, class_id: str):
    """The agent's read-only tools for one of the teacher's classes.

    Returns (toolbox, aliases) where aliases is {"S1": student_id, ...}.
    Students are numbered by when their account was made, then username, so a
    label means the same student in every plan for this class.
    """
    roster = sorted(store.list_class_students(class_id),
                    key=lambda s: (s["created_at"], s["username"] or ""))
    # Students whose AI switch is off are left out of everything the agent can see (it calls a
    # model). Labels stay numbered over the whole class, so S3 is still S3 in every plan.
    off = {s["student_id"] for s in roster if not s.get("ai_enabled", True)}
    insights = _class_insights(teacher_id, class_id, exclude=off)  # checks ownership
    aliases = {f"S{n}": s["student_id"] for n, s in enumerate(roster, start=1)
               if s["student_id"] not in off}
    alias_of = {sid: alias for alias, sid in aliases.items()}
    chapter_names = {c["id"]: c["name"] for c in engine.list_chapters()}

    def concept_lookup(concept_id: str) -> dict[str, Any] | None:
        concept = engine.find_concept(concept_id)
        if concept is None:
            return None
        return {"name": concept.name, "chapter_name": chapter_names.get(concept.chapter_id),
                "learning_objective": concept.learning_objective,
                "prerequisites": list(concept.prerequisites)}

    def takeaway_lookup(concept_id: str, interest: str) -> str | None:
        authored = lesson_service.get_authored_lesson(concept_id, interest)
        if authored is None:
            return None
        sections = lesson_service.student_view(authored)["sections"]
        return next((s["markdown"] for s in sections if s["heading"] == "Key takeaway"), None)

    def days_since(iso: str | None) -> int | None:
        if not iso:
            return None
        return (datetime.now(tz=timezone.utc) - datetime.fromisoformat(iso)).days

    toolbox = teacher_agent.ClassToolbox(
        class_info=insights["class"], insights=insights, alias_of=alias_of,
        concept_lookup=concept_lookup, takeaway_lookup=takeaway_lookup, days_since=days_since,
    )
    return toolbox, aliases


def _render_plan(plan: dict[str, Any], class_id: str) -> dict[str, Any]:
    """A stored plan as the teacher sees it: aliases replaced by current names."""
    names_by_id = {s["student_id"]: s["name"] for s in store.list_class_students(class_id)}
    names = {alias: names_by_id[sid] for alias, sid in plan["aliases"].items() if sid in names_by_id}
    return {
        "plan_id": plan["plan_id"],
        "created_at": plan["created_at"],
        "source": plan["source"],
        "model": plan["model"],
        "note": plan["note"],
        "markdown": teacher_agent.fill_names(plan["markdown"], names),
        "steps": [{"summary": c["summary"], "ok": c.get("ok", True)} for c in plan["trace"]],
    }


def get_class_plan(teacher_id: str, class_id: str) -> dict[str, Any] | None:
    """The latest plan for one of the teacher's classes, or None if none yet."""
    get_teacher_profile(teacher_id)
    _own_class(teacher_id, class_id)
    plan = store.get_latest_class_plan(class_id)
    return _render_plan(plan, class_id) if plan else None


_PLAN_RUNS: dict[str, dict[str, Any]] = {}
_PLAN_RUNS_LOCK = threading.Lock()


def _plan_progress_start(class_id: str) -> dict[str, Any]:
    run: dict[str, Any] = {"running": True, "stage": "Getting the class data ready",
                           "steps": []}
    with _PLAN_RUNS_LOCK:
        _PLAN_RUNS[class_id] = run
    return run


def get_ai_status(teacher_id: str, *, force: bool = False) -> dict[str, Any]:
    """Is the live AI answering? For the teacher's status badge (cached a minute).

    Returns the `llm.health` dict. `configured: False` is normal (every AI feature
    then uses its non-AI fallback); `up: False` with `configured: True` means the
    gateway or every model in the chain is down right now.
    """
    get_teacher_profile(teacher_id)
    return llm.health(force=force)


def get_class_plan_progress(teacher_id: str, class_id: str) -> dict[str, Any]:
    """What the teaching assistant is doing right now for this class's plan.

    Polled by the page while `generate_class_plan` runs. Kept in this server's
    memory only (one process), and holds the last run until the next one starts.

    Returns: {running: bool, stage: str, steps: [{summary, ok}]}. Before any run
    since the server started: {running: False, stage: "", steps: []}.

    Raises:
        NotFoundError: not this teacher's class.
    """
    get_teacher_profile(teacher_id)
    _own_class(teacher_id, class_id)
    run = _PLAN_RUNS.get(class_id)
    if run is None:
        return {"running": False, "stage": "", "steps": []}
    return {"running": run["running"], "stage": run["stage"], "steps": list(run["steps"])}


def generate_class_plan(
    teacher_id: str, class_id: str, *, models: list[Any] | None = None
) -> dict[str, Any]:
    """Ask the teacher agent for a plan for the next lesson, and store it.

    Uses the configured Gemini models (or `models`, for tests); if none is
    configured or all fail, the plan is written by fixed rules and says so —
    the teacher always gets a plan. A plan made in the last minute is returned
    as-is instead of making another.

    Returns: the rendered plan (see `get_class_plan`), with "reused": bool.

    Raises:
        NotFoundError: not this teacher's class.
    """
    get_teacher_profile(teacher_id)
    _own_class(teacher_id, class_id)
    latest = store.get_latest_class_plan(class_id)
    if latest is not None:
        age = (datetime.now(tz=timezone.utc)
               - datetime.fromisoformat(latest["created_at"])).total_seconds()
        if age < _PLAN_REUSE_SECONDS:
            return {**_render_plan(latest, class_id), "reused": True}

    toolbox, aliases = _class_toolbox(teacher_id, class_id)
    # Live progress for the page to poll while this (slow) request runs: what the
    # agent has really done so far. Only concept names and counts, never students.
    run = _plan_progress_start(class_id)
    toolbox.on_step = lambda step: run["steps"].append(
        {"summary": step["summary"], "ok": step["ok"]})
    try:
        with llm.usage_context(feature="teacher_agent", class_id=class_id):
            result = teacher_agent.plan_class(
                toolbox, models, on_stage=lambda text: run.__setitem__("stage", text))
    finally:
        run["running"] = False
    note = result["note"]
    left_out = len(store.ai_disabled_ids([s["student_id"] for s in store.list_class_students(class_id)]))
    if left_out:
        extra = (f"{left_out} student{'s' if left_out != 1 else ''} with the AI switched off "
                 f"{'are' if left_out != 1 else 'is'} not included in this plan.")
        note = f"{note} {extra}" if note else extra
    saved = store.save_class_plan(
        class_id, teacher_id, result["source"], result["model"], result["markdown"],
        result["trace"], aliases, note,
    )
    return {**_render_plan(saved, class_id), "reused": False}


# ---------------------------------------------------------------------------
# Coaching notes (2026-10-13): a short note per student, for the teacher.
# A fourth live-AI feature, added at the user's request; the model sees only
# S1, S2... and coarse facts (src/agents/coaching_agent.py), and every student
# gets a rules note whenever the AI is off, fails or breaks a rule.
# ---------------------------------------------------------------------------

_COACHING_REUSE_SECONDS = 60


def _student_aliases(class_id: str) -> dict[str, str]:
    """{"S1": student_id, ...} numbered the same way as the teacher agent's plans."""
    roster = sorted(store.list_class_students(class_id),
                    key=lambda s: (s["created_at"], s["username"] or ""))
    return {f"S{n}": s["student_id"] for n, s in enumerate(roster, start=1)}


def _coaching_cases(teacher_id: str, class_id: str, aliases: dict[str, str]) -> dict[str, dict[str, Any]]:
    insights = get_class_insights(teacher_id, class_id)
    rows = {r["student_id"]: r for r in insights["students"]}
    ids = list(aliases.values())
    surveys = store.list_surveys(ids)
    activity = store.get_activity(ids)
    views: dict[str, list[dict[str, Any]]] = {}
    for v in activity["views"]:
        views.setdefault(v["student_id"], []).append(v)
    wrong: dict[str, dict[str, bool]] = {}   # student -> concept name -> was ever sure
    for a in activity["answers"]:
        if a["correct"]:
            continue
        concept = engine.find_concept(a["concept_id"])
        name = concept.name if concept else a["concept_id"]
        seen = wrong.setdefault(a["student_id"], {})
        seen[name] = seen.get(name, False) or a.get("confidence") == "sure"
    now = datetime.now(tz=timezone.utc)
    cases = {}
    for alias, sid in aliases.items():
        row = rows.get(sid) or {}
        last = row.get("last_active")
        days = (now - datetime.fromisoformat(last)).days if last else None
        mix_ups = sorted(({"concept": c, "sure": s} for c, s in wrong.get(sid, {}).items()),
                         key=lambda m: (not m["sure"], m["concept"]))
        survey_row = surveys.get(sid)
        cases[alias] = coaching_agent.build_case(
            row, survey_row["traits"] if survey_row else None,
            survey.observed_reading(views.get(sid, [])), mix_ups, days)
    return cases


def _concept_ids_by_name() -> dict[str, str]:
    return {c.name: c.id for ids in engine.concept_ids_by_chapter().values()
            for c in (engine.find_concept(i) for i in ids) if c is not None}


def _action_view(action: dict[str, Any], last_active: str | None) -> dict[str, Any]:
    """A stored coaching action with its outcome in words, for the teacher."""
    concept = engine.find_concept(action["concept_id"]) if action.get("concept_id") else None
    if action["kind"] == "revise":
        if action["done_at"] is None:
            outcome, status = "Waiting: it's at the top of their revision list.", "waiting"
        elif action["correct"]:
            outcome, status = "Done: they got the new question right.", "right"
        else:
            outcome, status = "Done, not yet right: it's back on their mix-ups list.", "wrong"
    else:
        came_back = bool(last_active and last_active > action["created_at"])
        outcome = "They've been active since." if came_back else "Not active since."
        status = "active_since" if came_back else "quiet_since"
    return {"action_id": action["action_id"], "kind": action["kind"], "concept_id": action.get("concept_id"),
            "concept_name": concept.name if concept else None, "created_at": action["created_at"],
            "done_at": action["done_at"], "correct": action["correct"], "status": status, "outcome": outcome}


def _render_coaching(run: dict[str, Any], class_id: str) -> dict[str, Any]:
    """A stored run as the teacher sees it: aliases replaced by current names, in S order, each note with
    its proposed action (concept resolved to an id) and what happened to any action the teacher approved."""
    roster = {s["student_id"]: s for s in store.list_class_students(class_id)}
    by_name = _concept_ids_by_name()
    actions: dict[str, list[dict[str, Any]]] = {}
    for a in store.list_coaching_actions(list(roster)):
        # Approved since these notes were written, or still waiting from an earlier set.
        if a["class_id"] == class_id and (a["created_at"] >= run["created_at"] or a["done_at"] is None):
            actions.setdefault(a["student_id"], []).append(a)
    students = []
    follow = {"approved": 0, "done": 0, "right": 0, "came_back": 0, "check_ins": 0}
    for alias in sorted(run["notes"], key=lambda a: int(a[1:])):
        sid = run["aliases"].get(alias)
        if sid not in roster:
            continue  # a student removed since the run
        note = dict(run["notes"][alias])
        proposed = note.pop("action", None)
        if proposed and proposed.get("type") == "revise":
            concept_id = by_name.get(proposed.get("concept"))
            proposed = {**proposed, "concept_id": concept_id} if concept_id else None
        taken = [_action_view(a, roster[sid]["last_active"]) for a in actions.get(sid, [])]
        for t in taken:
            follow["approved"] += 1
            if t["kind"] == "revise":
                follow["done"] += int(t["done_at"] is not None)
                follow["right"] += int(bool(t["correct"]))
            else:
                follow["check_ins"] += 1
                follow["came_back"] += int(t["status"] == "active_since")
        students.append({"student_id": sid, "name": roster[sid]["name"], "alias": alias, **note,
                         "action": proposed, "actions_taken": taken})
    return {"run_id": run["run_id"], "created_at": run["created_at"], "source": run["source"],
            "model": run["model"], "note": run["note"], "students": students, "follow_through": follow}


def apply_coaching_action(teacher_id: str, class_id: str, student_id: str, kind: str,
                          concept_id: str | None = None) -> dict[str, Any]:
    """The teacher approves one of a coaching note's suggestions; the system carries it out by rules.

    kind "revise": `concept_id` joins the student's revision list, due now and listed first, until they
    answer a new question on it (the outcome, right or not, is recorded). kind "check_in": recorded, so the
    page can show whether the student was active again afterwards. The AI only proposes; nothing happens
    to a student until a teacher approves it here.

    Returns: the action as the teacher sees it ({action_id, kind, concept_id, concept_name, created_at,
             done_at, correct, status, outcome}).

    Raises:
        NotFoundError: not this teacher's class, or the student isn't in it, or an unknown concept.
        EcoLearnError: an unknown kind, or "revise" without a concept.
    """
    get_teacher_profile(teacher_id)
    _own_class(teacher_id, class_id)
    roster = {s["student_id"]: s for s in store.list_class_students(class_id)}
    if student_id not in roster:
        raise NotFoundError("Student not found in this class.")
    if kind not in coaching_agent.ACTION_TYPES:
        raise EcoLearnError(f"Unknown action {kind!r}.")
    if kind == "revise":
        if not concept_id:
            raise EcoLearnError("Say which concept to revise.")
        if engine.find_concept(concept_id) is None:
            raise NotFoundError(f"Unknown concept_id {concept_id!r}.")
    else:
        concept_id = None
    action = store.add_coaching_action(student_id, class_id, teacher_id, kind, concept_id)
    return _action_view({**action, "correct": None if action.get("correct") is None else bool(action["correct"])},
                        roster[student_id]["last_active"])


def get_coaching_notes(teacher_id: str, class_id: str) -> dict[str, Any] | None:
    """The latest coaching notes for this class, or None if none were made yet.

    Returns: {run_id, created_at, source: "agent"|"mixed"|"rules", model, note,
              students: [{student_id, name, alias, note, evidence: [field], next_step,
                          source: "ai"|"rules"}]}

    Raises:
        NotFoundError: not this teacher's class.
    """
    get_teacher_profile(teacher_id)
    _own_class(teacher_id, class_id)
    run = store.get_latest_coaching_notes(class_id)
    return _render_coaching(run, class_id) if run else None


def generate_coaching_notes(teacher_id: str, class_id: str, *,
                            chat: Any = None) -> dict[str, Any]:
    """Write a note per student (AI first, rules for anything the AI misses) and store it.

    A run made in the last minute is returned as it is, with "reused": True. `chat` is for
    tests; by default the live model chain (src/llm) is used, or rules when it is off.

    Raises:
        NotFoundError: not this teacher's class.
    """
    get_teacher_profile(teacher_id)
    _own_class(teacher_id, class_id)
    latest = store.get_latest_coaching_notes(class_id)
    if latest is not None:
        age = (datetime.now(tz=timezone.utc) - datetime.fromisoformat(latest["created_at"])).total_seconds()
        if age < _COACHING_REUSE_SECONDS:
            return {**_render_coaching(latest, class_id), "reused": True}
    aliases = _student_aliases(class_id)
    cases = _coaching_cases(teacher_id, class_id, aliases)
    roster = store.list_class_students(class_id)
    forbidden = ([s["name"] for s in roster]
                 + [part for s in roster for part in s["name"].split() if len(part) > 2]
                 + [s["username"] for s in roster if s["username"]])
    use = chat if chat is not None else llm.chat
    off = store.ai_disabled_ids(list(aliases.values()))
    rules_only = {alias for alias, sid in aliases.items() if sid in off}
    with llm.usage_context(feature="coaching_agent", class_id=class_id):
        result = coaching_agent.coach_class(cases, forbidden, use, chat is not None or llm.is_configured(),
                                            rules_only=rules_only)
    saved = store.save_coaching_notes(class_id, teacher_id, result["source"], result["model"],
                                      result["notes"], aliases, result["trail"], result["note"])
    return {**_render_coaching(saved, class_id), "reused": False}


# ---------------------------------------------------------------------------
# A family's data requests (2026-10-13). For the operator, never exposed over HTTP: a person on the
# team checks who is asking, then runs scripts/export_student.py or scripts/delete_student.py.
# ---------------------------------------------------------------------------

def find_student_id(username: str) -> str:
    """The student id for a username (how a request from a family is turned into an id).

    Raises:
        NotFoundError: no such student.
    """
    record = store.get_student_by_username(username)
    if record is None:
        raise NotFoundError(f"No student with the username {username!r}.")
    return record["student_id"]


def export_student_data(student_id: str) -> dict[str, Any]:
    """Everything EcoLearn holds about one student, as plain data a person can read.

    Returns:
        {"account": {name, username, interest, level, class, created_at},
         "tables": {table: [rows]}   every row about them, by table, JSON parsed; no password hash,
         "readable": {...}           the same, in words: concept names instead of ids,
         "class_notes": [...]        any teacher-assistant coaching note about them,
         "plans_that_included_them": int}   class plans in which they were one of the labelled students

    Raises:
        NotFoundError: no such student.
    """
    profile = store.get_student(student_id)
    if profile is None:
        raise NotFoundError(f"Unknown student_id {student_id!r}.")
    class_id = store.get_student_class_id(student_id)
    klass = store.get_class(class_id) if class_id else None
    raw = store.export_student_rows(student_id)
    tables = raw["tables"]

    def concept_name(concept_id: str) -> str:
        concept = engine.find_concept(concept_id)
        return concept.name if concept else concept_id

    def named(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [{**r, "concept": concept_name(r["concept_id"])} if "concept_id" in r else r for r in rows]

    answers = tables.get("answers", [])
    survey_row = (tables.get("learner_survey") or [None])[0]
    readable = {
        "lessons_opened": sorted({concept_name(v["concept_id"]) for v in tables.get("lesson_views", [])}),
        "minutes_actively_read": round(sum(int(v.get("active_seconds") or 0)
                                           for v in tables.get("lesson_views", [])) / 60, 1),
        "lesson_check_answers": {"total": len(answers), "right": sum(1 for a in answers if a.get("correct"))},
        "progress": [{"concept": concept_name(p["concept_id"]), "status": p.get("status"),
                      "attempts": p.get("attempts")} for p in tables.get("progress", [])],
        "hobbies": ((tables.get("learner_profiles") or [{}])[0].get("hobbies")),
        "survey_summary": (survey_row or {}).get("traits", {}).get("summary") if survey_row else None,
        "survey_updates": len(tables.get("learner_survey_history", [])),
        "starting_check_questions_answered": len(tables.get("diagnostic_answers", [])),
        "end_check_questions_answered": len(tables.get("end_check_answers", [])),
        "revision_answers": len(tables.get("review_answers", [])),
        "personal_stories": [{"concept": concept_name(p["concept_id"]), "hobby": p.get("hobby"),
                              "status": p.get("status"), "story": p.get("story"),
                              "analogy": p.get("analogy"), "limit": p.get("limit_text")}
                             for p in tables.get("personal_stories", [])],
        "help_chat_outcomes": _count_by(tables.get("help_events", []), "outcome"),
        "ai_model_calls_logged": len(tables.get("llm_calls", [])),
    }
    return {
        "account": {"name": profile["name"], "username": profile["username"], "interest": profile["interest"],
                    "level": profile["level"], "class": klass["name"] if klass else None,
                    "created_at": profile["created_at"], "ai_enabled": profile.get("ai_enabled", True)},
        "tables": {name: named(rows) for name, rows in tables.items()},
        "readable": readable,
        "class_notes": raw["class_notes"],
        "plans_that_included_them": raw["plans_that_included_them"],
    }


def _count_by(rows: list[dict[str, Any]], key: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for r in rows:
        out[str(r.get(key))] = out.get(str(r.get(key)), 0) + 1
    return out


def delete_student(student_id: str) -> dict[str, Any]:
    """Permanently erase a student and everything about them. This cannot be undone.

    Removes the account and every row tied to it, in one transaction; the AI usage log keeps its token
    counts but loses the link to the child; the student's label and note in class plans and coaching
    notes are removed. Old copies of the database file (backups) are NOT touched: that is the
    operator's to handle.

    Returns:
        {"deleted": {table: rows}, "anonymised": {table: rows}, "edited": {...},
         "remaining": {"table.column": rows}}  `remaining` must be empty: it is a search of the whole
        database for the student's id after the erase.

    Raises:
        NotFoundError: no such student.
    """
    result = store.erase_student(student_id)
    if not result:
        raise NotFoundError(f"Unknown student_id {student_id!r}.")
    result["remaining"] = store.find_student_traces(student_id)
    return result


def llm_prices() -> dict[str, Any]:
    """data/llm_prices.yaml (Google's paid-tier list prices, checked 2026-10-13: re-check before quoting)."""
    import yaml

    from src.file_cache import cached_parse
    path = Path(__file__).resolve().parents[1] / "data" / "llm_prices.yaml"
    return cached_parse(path, lambda p: yaml.safe_load(p.read_text(encoding="utf-8")), "llm_prices")


def _pilot_survey(students: list[dict[str, Any]], student_alias: dict[str, str],
                  insights: dict[str, Any]) -> dict[str, Any]:
    """The survey section of `pilot_report`: pseudonymised, fixed-option answers only."""
    ids = [s["student_id"] for s in students]
    surveys = store.list_surveys(ids)
    stats = {r["student_id"]: r for r in insights["students"]}  # already re-keyed by alias
    views: dict[str, list[dict[str, Any]]] = {}
    for v in store.get_activity(None)["views"]:
        views.setdefault(v["student_id"], []).append(v)
    entries, history = [], {}
    for sid, row in surveys.items():
        if sid not in student_alias:
            continue
        a = student_alias[sid]
        entries.append({
            "student_id": a, "revision": row["revision"], "saved_at": row["updated_at"] or row["completed_at"],
            "traits": row["traits"], "observed": survey.observed_reading(views.get(sid, [])),
            "first_try_correct": (stats.get(a) or {}).get("first_try_correct"),
            "answered": (stats.get(a) or {}).get("answered")})
        history[a] = store.get_survey_history(sid)
    entries.sort(key=lambda e: e["student_id"])
    return metrics.survey_report(entries, history, len(students))


def pilot_report() -> dict[str, Any]:
    """Everything the pilot recorded, across all classes, with no names in it.

    For the server-side report (scripts/pilot_report.py) — the evidence for the
    pitch and for the school. Students and classes are replaced by stable
    pseudonyms (S001…, C01…) in order of creation, so the export can be shared
    for analysis without identifying a child. Never exposed over HTTP.

    Returns:
        {"insights": class_insights over every student,
         "students": [{student, class, interest, level, created_at}],
         "views": [...], "answers": [...], "ratings": [...],
         "diagnostic": [...], "end_check": [...], "check_gains": {...},
         "stories": [...], "survey": {taken, total, distributions, said_vs_shown, rows, history,
         changes, ...}}  — pseudonymised rows.
    """
    students = store.list_all_students()
    class_alias: dict[str | None, str | None] = {None: None}
    student_alias: dict[str, str] = {}
    for n, s in enumerate(students, start=1):
        student_alias[s["student_id"]] = f"S{n:03d}"
        if s["class_id"] not in class_alias:
            class_alias[s["class_id"]] = f"C{len(class_alias):02d}"

    activity = store.get_activity(None)
    concept_info, check_info = _insight_lookups()
    insights = metrics.class_insights(students, activity, concept_info, check_info)
    for row in insights["students"]:
        row["student_id"] = student_alias[row["student_id"]]
    insights["students"].sort(key=lambda r: r["student_id"])
    for m in insights["misconceptions"]:
        m["student_ids"] = [student_alias[s] for s in m["student_ids"] if s in student_alias]

    def alias(rows: list[dict[str, Any]], drop: tuple[str, ...] = ()) -> list[dict[str, Any]]:
        out = []
        for row in rows:
            if row["student_id"] not in student_alias:
                continue  # a deleted or legacy account
            clean = {k: v for k, v in row.items() if k not in drop}
            clean["student_id"] = student_alias[row["student_id"]]
            out.append(clean)
        return out

    return {
        "insights": insights,
        "students": [
            {"student_id": student_alias[s["student_id"]], "class_id": class_alias[s["class_id"]],
             "interest": s["interest"], "level": s["level"], "created_at": s["created_at"]}
            for s in students
        ],
        "views": alias(activity["views"], drop=("view_id",)),
        "answers": alias(activity["answers"], drop=("answer_id",)),
        "ratings": alias(activity["ratings"]),
        # The starting check: each student's baseline before any lesson.
        "diagnostic": alias(store.get_diagnostic_answers(None)),
        # The end check: the same concepts with parallel questions, at the end.
        "end_check": alias(store.get_end_check_answers(None)),
        # Before -> after over every student who took both checks.
        "check_gains": _class_gains(list(student_alias))[0],
        # Every model call, for the cost per student (ai_usage) and the raw rows.
        "ai_usage": metrics.ai_usage(store.get_llm_calls(), llm_prices(), len(students)),
        "llm_calls": [
            {**{k: v for k, v in c.items() if k not in ("student_id", "class_id", "call_id")},
             "student_id": student_alias.get(c["student_id"]) if c["student_id"] else None,
             "class_id": class_alias.get(c["class_id"]) if c["class_id"] else None}
            for c in store.get_llm_calls()
        ],
        # AI-written personal stories, with whether students reported them and
        # whether teachers hid them: the evidence on the AI layer's quality.
        "stories": alias(store.list_personal_stories(list(student_alias))),
        # The survey: what students said about themselves, how it changed when they updated
        # their answers, and how it lines up with how they actually read and answered.
        "survey": _pilot_survey(students, student_alias, insights),
        # Randomised comparisons (data/experiments.yaml, docs/pilot-experiment.md): control vs treatment.
        **_pilot_experiments(students, student_alias, class_alias),
    }


def _pilot_experiments(students: list[dict[str, Any]], student_alias: dict[str, str],
                       class_alias: dict[str | None, str | None]) -> dict[str, Any]:
    """The experiments section of `pilot_report`: per-student rows (pseudonymised) and each comparison.

    Read-only: students without an arm (accounts made before the experiment, never opened since) are
    counted as unassigned, not assigned here.
    """
    by_id = {s["student_id"]: s for s in students}
    stored = store.list_experiment_arms()
    arms_of: dict[str, dict[str, str]] = {}
    for a in stored:
        arms_of.setdefault(a["student_id"], {})[a["experiment_id"]] = a["arm"]
    _, comparisons = _class_gains([s["student_id"] for s in students])
    reports, all_rows = [], []
    for exp in experiments.load_config():
        rows = []
        for a in (x for x in stored if x["experiment_id"] == exp["id"]):
            sid = a["student_id"]
            if sid not in by_id:
                continue  # an erased student: their arm went with them, this is a leftover
            signals = _profile(sid, arms=arms_of.get(sid, {}))["signals"]
            comp = comparisons.get(sid)
            gain = (sum(1 for c in comp["concepts"] if c["after"] == "right")
                    - sum(1 for c in comp["concepts"] if c["before"] == "right")) if comp else None
            rows.append({
                "experiment_id": exp["id"], "student_id": student_alias[sid],
                "class_id": class_alias.get(by_id[sid]["class_id"]), "arm": a["arm"],
                "sure_wrong_rule": signals["sure_wrong_rule"], "sure_wrong_concepts": signals["sure_wrong_concepts"],
                "sure_wrong_fixed": signals["sure_wrong_fixed"], "first_try_right": signals["first_try_right"],
                "first_try_answered": signals["first_try_answered"], "sure": signals["sure"],
                "sure_wrong": signals["sure_wrong"], "end_gain": gain,
                "dismissed": "sure_wrong" in store.get_insight_dismissals(sid)})
        if not rows and not exp.get("enabled"):
            continue  # a stopped experiment nobody was ever put in: nothing to report
        rows.sort(key=lambda r: r["student_id"])
        report = metrics.experiment_report(exp, rows)
        report["enabled"] = bool(exp.get("enabled"))
        report["unassigned"] = len(students) - len(rows)
        reports.append(report)
        all_rows += rows
    return {"experiments": reports, "experiment_rows": all_rows}


# ---------------------------------------------------------------------------
# 5. Live help
# ---------------------------------------------------------------------------

def ask_help(student_id: str, concept_id: str, question: str) -> dict[str, Any]:
    """Answer a free-form question about the lesson the student is on (the doubt chat).

    The live path (distinct from the cached lessons): one model call through src/llm, grounded in
    the student's own lesson (src/learner/doubt_tutor.py), checked by rules before it is shown.
    When the AI is off (for this student, or on the server), fails, or its reply fails a check,
    the answer is the lesson's key idea and a nudge to the teacher: the chat never errors out.

    Args:
        student_id: Who is asking (used for their interest/level).
        concept_id: The concept the question is about (for context/logging).
        question:   The student's free-form question.

    Returns:
        {
          "concept_id", "concept_name",
          "answer":   markdown,
          "source":   "ai" | "rules",
          "verdict":  "PASS" (an AI answer that passed the checks) | "OFF_TOPIC" | "FALLBACK" | "AI_OFF",
          "attempts": model calls made (0 or 1),
        }
        A question stopped by the front door (src/learner/help_guard.py) is NOT sent to a model:
        it returns the same keys with "verdict": "BLOCKED", "attempts": 0, "blocked": True,
        "reason" (self_harm | personal_info | unsuitable | injection | too_short | too_long) and
        a kind message in "answer". Only the outcome is logged, never the question.

    Raises:
        NotFoundError: if the student is unknown.
        TooManyRequestsError: too many questions in a short time, a daily cap, or the last
            question is still being answered (HTTP 429). Never raised for a self-harm message.
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

    # The front door (src/learner/help_guard.py): nothing a student typed reaches a model until it
    # passes. Only the OUTCOME is logged, never the words. A self-harm message is answered kindly and
    # is never rate-limited away.
    def stopped(reason: str, message: str) -> dict[str, Any]:
        _log_help(student_id, "blocked", reason)
        return {"concept_id": concept_id, "concept_name": concept_label, "answer": message,
                "verdict": "BLOCKED", "attempts": 0, "blocked": True, "reason": reason}

    checked = help_guard.screen(question)
    if not checked.ok and checked.reason == "self_harm":
        return stopped(checked.reason, checked.message or "")
    allowed, retry_after, why = _help_limiter.try_start(student_id)
    if not allowed:
        _log_help(student_id, "rate_limited", why)
        raise TooManyRequestsError(help_guard.limit_message(why, retry_after))
    try:
        if not checked.ok:
            return stopped(checked.reason or "unsuitable", checked.message or "")
        try:
            return _answer_help(student_id, profile, concept, concept_id, concept_label,
                                " ".join(question.split()))
        except Exception:
            _log_help(student_id, "failed", None)  # the pipeline fell over: count it, then let the error through
            raise
    finally:
        _help_limiter.finish(student_id)


def _log_help(student_id: str, outcome: str, reason: str | None) -> None:
    try:
        store.record_help_event(student_id, outcome, reason)
    except Exception:  # noqa: BLE001 — a log line must never cost a student an answer
        pass


_help_limiter = help_guard.HelpLimiter()


# ---------------------------------------------------------------------------
# 6. Practice with AI (2026-10-19): the fifth live-AI place, approved by the user. An extra question on the
# idea just studied, written and independently solved by AI before a student sees it (src/learner/practice.py).
# It NEVER counts: nothing here touches progress, answers, mastery or the pilot metrics.
# ---------------------------------------------------------------------------

_practice_chat: Any = None  # tests swap in a stand-in for llm.chat; None means the live model chain
_practice_limiter = help_guard.HelpLimiter(
    per_window=int(os.getenv("ECOLEARN_PRACTICE_PER_WINDOW", "6")),
    window_seconds=int(os.getenv("ECOLEARN_PRACTICE_WINDOW_SECONDS", "600")),
    per_day=int(os.getenv("ECOLEARN_PRACTICE_PER_DAY", "40")))


def _practice_available(profile: dict[str, Any]) -> bool:
    """A practice question can be tried: the AI is on for the server and for this student."""
    return bool(profile.get("ai_enabled", True)) and (_practice_chat is not None or llm.is_configured())


def start_practice(student_id: str, concept_id: str) -> dict[str, Any]:
    """Write one checked practice question on this concept, in the student's interest.

    Returns {"available": True, "practice_id", "concept_id", "concept_name", "question", "options"} (no answer
    key), or {"available": False, "reason": "ai_off" | "not_configured" | "no_lesson" | "failed", "message"}
    when there is no question: the AI is switched off (for the student or the server), the lesson isn't
    written yet, or the AI's attempts failed the checks. A failed attempt is stored for the teacher's counts.

    Raises:
        NotFoundError: unknown student or concept.
        TooManyRequestsError: too many practice questions in a short time, or one already being written.
    """
    profile = _require_student(student_id)
    concept = engine.find_concept(concept_id)
    if concept is None:
        raise NotFoundError(f"Unknown concept_id {concept_id!r}.")

    def none(reason: str, message: str) -> dict[str, Any]:
        return {"available": False, "reason": reason, "message": message}

    if not profile.get("ai_enabled", True):
        return none("ai_off", "Practice with AI is switched off for your account.")
    if not _practice_available(profile):
        return none("not_configured", "Practice with AI isn't running right now.")
    authored = lesson_service.get_authored_lesson(concept_id, profile["interest"])
    if authored is None:
        return none("no_lesson", "There's no lesson to practise from yet.")
    allowed, retry_after, why = _practice_limiter.try_start(student_id)
    if not allowed:
        raise TooManyRequestsError(help_guard.limit_message(why, retry_after))
    try:
        material = practice.lesson_material(authored, doubt_tutor.lesson_context(concept, profile["interest"])["sections"])
        with llm.usage_context(feature="practice", student_id=student_id):
            made = practice.write(concept_name=concept.name, level=profile["level"], interest=profile["interest"],
                                  material=material, chat=_practice_chat if _practice_chat is not None else llm.chat)
    finally:
        _practice_limiter.finish(student_id)
    practice_id = store.save_practice(student_id, concept_id, made["ok"], made.get("question"),
                                      made.get("model"), made["trail"])
    if not made["ok"]:
        return none("failed", "Couldn't write a practice question that passed our checks just now. Try again later, "
                              "or open the revision list for another question.")
    q = made["question"]
    return {"available": True, "practice_id": practice_id, "concept_id": concept_id, "concept_name": concept.name,
            "question": q["question"], "options": q["options"]}


def answer_practice(student_id: str, practice_id: int, answer: str) -> dict[str, Any]:
    """Check a practice answer. Nothing is recorded anywhere but the practice table.

    Returns {"correct", "selected_option", "correct_option", "explanation", "why_wrong": str | None}.

    Raises:
        NotFoundError: not this student's practice question (or none was written).
        EcoLearnError: not one of A to D.
        ConflictError: already answered.
    """
    _require_student(student_id)
    row = store.get_practice(int(practice_id))
    if row is None or row["student_id"] != student_id or not row["ok"]:
        raise NotFoundError("That practice question isn't yours.")
    picked = (answer or "").strip().upper()
    if picked not in practice.LETTERS:
        raise EcoLearnError(f"Pick one of A, B, C or D — got {answer!r}.")
    q = row["question"]
    correct = picked == q["answer"]
    if not store.answer_practice(row["practice_id"], picked, correct):
        raise ConflictError("You've already answered this one. Ask for another!")
    return {"correct": correct, "selected_option": picked, "correct_option": q["answer"],
            "explanation": q["explanation"], "why_wrong": None if correct else q["why_wrong"].get(picked)}


_help_chat: Any = None  # tests swap in a stand-in for llm.chat; None means the live model chain

_HELP_VERDICTS = {"answered": "PASS", "off_topic": "OFF_TOPIC", "fallback": "FALLBACK", "ai_off": "AI_OFF"}


def _answer_help(student_id: str, profile: dict[str, Any], concept: Any, concept_id: str,
                 concept_label: str, question: str) -> dict[str, Any]:
    """The live part of the doubt chat, after the question has been screened.

    One call through src/llm (2026-10-14), grounded in the student's own lesson; it replaced the old
    generate -> critic -> polish pipeline and its chromadb index (see src/learner/doubt_tutor.py).
    """
    chat = _help_chat if _help_chat is not None else llm.chat
    with llm.usage_context(feature="doubt_chat", student_id=student_id):
        result = doubt_tutor.answer(
            concept=concept, concept_label=concept_label, interest=profile["interest"],
            level=profile["level"], question=question,
            # The model is never sent the name, so this only catches a leak. Single name parts are
            # left out on purpose: "Ray" or "Joule" would turn ordinary physics answers into fallbacks.
            forbidden=[w for w in (profile.get("username"),
                                   profile.get("name") if len((profile.get("name") or "").split()) > 1 else None)
                       if w],
            ai_allowed=profile.get("ai_enabled", True),
            models_on=_help_chat is not None or llm.is_configured(),
            chat=chat)
    # Only the outcome is logged (help_events), never the question or the answer. The model call
    # itself, with its tokens, is already in the usage log through src/llm.
    _log_help(student_id, result["outcome"], result["problem"][:60] if result["problem"] else None)
    return {
        "concept_id": concept_id,
        "concept_name": concept_label,
        "answer": result["answer"],
        "source": result["source"],
        "verdict": _HELP_VERDICTS[result["outcome"]],
        "attempts": 1 if result["called"] else 0,
    }
