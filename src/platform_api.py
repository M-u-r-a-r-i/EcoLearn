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

import re
import sqlite3
import uuid
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from typing import Any

from src.agents import teacher_agent  # stdlib-only at import; the SDK loads lazily
from src.agents.assessor import grade_answer
from src.agents.polisher import polish_explanation
from src.auth import credentials, passwords
from src.content import lesson_service
from src.curriculum.interests import load_interests
from src.curriculum.scope import scope_chapter_ids, scope_interest_ids
from src.errors import AuthError, ConflictError, EcoLearnError, NotFoundError
from src.learner import diagnostic
from src.learner import plan as learner_plan
from src.path import engine
from src.progress import metrics, store
# src.pipeline (the doubt chat's generate→critic loop and its RAG index) is
# imported lazily inside ask_help — see the note there.

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
    # Teachers share the namespace, so a student can't take a teacher's username.
    if store.username_exists(username):
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
        ready = lesson_service.concepts_with_lessons(profile["interest"])
        state = learner_plan.learner_state(student_id)
        learner_plan.annotate_roadmap(roadmap, state)
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
        out["questions"] = diagnostic.student_questions(profile["level"], profile["interest"])
    return out


def submit_diagnostic(
    student_id: str, picks: dict[str, str], hobbies: list[str] | None = None
) -> dict[str, Any]:
    """Grade and store the starting check (once per student).

    `picks` maps concept_id -> "A".."D" or "unsure"; anything left out counts as
    "unsure". It is taken once, because it is the pilot's baseline: a retake
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
    graded = diagnostic.grade(profile["level"], profile["interest"], picks or {})
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

    return envelope


# ---------------------------------------------------------------------------
# 4. Assessment
# ---------------------------------------------------------------------------

def _grade_multiple_choice(
    student_id: str,
    concept_id: str,
    answer: str,
    authored: Any,
    interest: str,
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

    correct = picked == check.answer
    # 3 = mastered, 0 = not yet. The store's pass mark is 2, so a correct pick
    # masters the concept and a wrong one leaves it unmastered but attempted.
    score = 3 if correct else 0

    if correct:
        feedback = f"Correct. {check.explanation.strip()}"
    else:
        why_wrong = (check.misconceptions.get(picked) or "").strip()
        feedback = (
            f"Not quite. {why_wrong}\n\n"
            f"The right answer is **{check.answer}**. {check.explanation.strip()}"
        ).strip()

    updated = store.update_progress(student_id, concept_id, score)
    logged = store.record_answer(
        student_id, concept_id, interest, picked, correct,
        None if correct else (check.misconceptions.get(picked) or "").strip() or None,
    )
    return {
        "concept_id": concept_id,
        "score": score,
        "attempt_no": logged["attempt_no"],
        "mastery_signal": "mastered" if correct else "not_yet",
        "feedback": feedback,
        "missing_concepts": [],
        "graded_question": check.question,
        "mastery": updated,
        # Multiple-choice extras the web app shows; absent for legacy grading.
        "correct": correct,
        "selected_option": picked,
        "correct_option": check.answer,
    }


def submit_assessment(
    student_id: str,
    concept_id: str,
    answer: str,
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
    student's mastery.

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
            student_id, concept_id, answer, authored, profile["interest"]
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
    get_teacher_profile(teacher_id)
    klass = _own_class(teacher_id, class_id)
    students = store.list_class_students(class_id)
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
    insights = get_class_insights(teacher_id, class_id)  # checks ownership
    roster = sorted(store.list_class_students(class_id),
                    key=lambda s: (s["created_at"], s["username"] or ""))
    aliases = {f"S{n}": s["student_id"] for n, s in enumerate(roster, start=1)}
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
    result = teacher_agent.plan_class(toolbox, models)
    saved = store.save_class_plan(
        class_id, teacher_id, result["source"], result["model"], result["markdown"],
        result["trace"], aliases, result["note"],
    )
    return {**_render_plan(saved, class_id), "reused": False}


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
         "diagnostic": [...]}  — pseudonymised rows.
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

    # Imported here, not at the top of the module: the pipeline pulls in the RAG
    # index (chromadb → grpc → native DLLs). If any of that can't load — a missing
    # package, or Windows Application Control blocking a DLL, as happened on
    # 2026-10-02 — only the doubt chat should go down. A top-level import took
    # the whole API with it: login, lessons and grading included.
    try:
        from src.pipeline import explain_with_review
    except (ImportError, OSError) as exc:
        raise RuntimeError(
            "The doubt chat isn't available right now. Your lesson and progress are "
            "fine — ask your teacher, or try the chat again later."
        ) from exc

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
