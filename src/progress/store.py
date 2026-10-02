"""Persistent student-progress store (SQLite).

This is the durable version of the in-session mastery ledger that app.py keeps
in `st.session_state.mastery`. One row per (student, concept) records the
student's best score, attempt count, derived mastery status, and when they last
saw the concept. The Learning Path Engine (src/path/engine.py) reads this store
to decide what to teach next.

Status vocabulary and thresholds are identical to app.py's `_status_from_score`
(score 0-3 → mastered / partial / not_yet) so the live UI and the persisted
record never disagree.

The database path is resolved from the ECOLEARN_PROGRESS_DB env var at call
time (default: data/progress.db). Reading it lazily — not at import — lets
tests point at a temp file before the first call.
"""

from __future__ import annotations

import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Project root = .../EcoLearn/  (this file lives at .../EcoLearn/src/progress/).
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_DB_PATH = _PROJECT_ROOT / "data" / "progress.db"

# Mastery status labels. Kept in lockstep with app.py so the session ledger and
# the persisted store speak the same language.
STATUS_MASTERED = "mastered"
STATUS_PARTIAL = "partial"
STATUS_NOT_YET = "not_yet"


def status_from_score(score: int) -> str:
    """Map a 0-3 score to a mastery status label (mirrors app.py)."""
    if score >= 3:
        return STATUS_MASTERED
    if score >= 2:
        return STATUS_PARTIAL
    return STATUS_NOT_YET


def _db_path() -> Path:
    """Resolve the DB path lazily so tests can override via env var."""
    raw = os.getenv("ECOLEARN_PROGRESS_DB")
    return Path(raw) if raw else _DEFAULT_DB_PATH


def _connect() -> sqlite3.Connection:
    """Open the DB (creating the file and schema if needed)."""
    path = _db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS progress (
            student_id  TEXT    NOT NULL,
            concept_id  TEXT    NOT NULL,
            status      TEXT    NOT NULL,
            best_score  INTEGER NOT NULL,
            attempts    INTEGER NOT NULL,
            last_seen   TEXT    NOT NULL,
            PRIMARY KEY (student_id, concept_id)
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            student_id  TEXT PRIMARY KEY,
            name        TEXT NOT NULL,
            interest    TEXT NOT NULL,
            level       TEXT NOT NULL,
            created_at  TEXT NOT NULL
        )
        """
    )
    _migrate_students(conn)
    # Teachers and their classes (2026-10-02). New tables, so plain CREATE IF NOT
    # EXISTS is the whole migration; UNIQUE is allowed in a CREATE, just not in an
    # ALTER. Teachers live apart from students on purpose: a teacher's id
    # ("tch_...") is not a student id, so a teacher's session is refused by every
    # student endpoint without anyone having to remember an extra role check.
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id     TEXT PRIMARY KEY,
            name           TEXT NOT NULL,
            username       TEXT NOT NULL UNIQUE,
            password_hash  TEXT NOT NULL,
            created_at     TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS classes (
            class_id    TEXT PRIMARY KEY,
            teacher_id  TEXT NOT NULL,
            name        TEXT NOT NULL,
            level       TEXT NOT NULL,
            created_at  TEXT NOT NULL
        )
        """
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_classes_teacher ON classes(teacher_id)")
    _create_metrics_tables(conn)
    return conn


def _create_metrics_tables(conn: sqlite3.Connection) -> None:
    """Pilot metrics (2026-10-02): new tables only, so the migration is additive.

    * lesson_views   — one row per time a student opens a lesson, with the
                       seconds they actively spent on it (updated as they read).
    * answers        — every multiple-choice pick, kept forever. `progress` only
                       keeps the best score, which hides *what* a student got
                       wrong; this table is what the misconception view reads.
    * lesson_ratings — one 👍/👎 per student per lesson (re-rating replaces it).

    Each row records the interest the student had at the time, because a
    student can switch interest and the pilot compares interests.
    """
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS lesson_views (
            view_id         TEXT PRIMARY KEY,
            student_id      TEXT NOT NULL,
            concept_id      TEXT NOT NULL,
            interest        TEXT NOT NULL,
            opened_at       TEXT NOT NULL,
            active_seconds  INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS answers (
            answer_id      INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id     TEXT NOT NULL,
            concept_id     TEXT NOT NULL,
            interest       TEXT NOT NULL,
            selected       TEXT NOT NULL,
            correct        INTEGER NOT NULL,
            attempt_no     INTEGER NOT NULL,
            misconception  TEXT,
            answered_at    TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS lesson_ratings (
            student_id  TEXT NOT NULL,
            concept_id  TEXT NOT NULL,
            interest    TEXT NOT NULL,
            rating      INTEGER NOT NULL,
            rated_at    TEXT NOT NULL,
            PRIMARY KEY (student_id, concept_id, interest)
        )
        """
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_views_student ON lesson_views(student_id)")
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_answers_student ON answers(student_id, concept_id)"
    )


def _migrate_students(conn: sqlite3.Connection) -> None:
    """Add the account columns to `students` if this DB predates them.

    Idempotent and additive, in the same lazy spirit as the CREATE TABLE IF NOT
    EXISTS calls above: every connection checks, and only the first one on an
    old database actually changes anything. Existing rows keep working — the new
    columns are nullable, so a legacy name-only student simply has
    username = password_hash = NULL and can still be loaded by
    `create_or_load_student`.

    Accounts log in with a **username**, not an email (user decision,
    2026-09-21: the pilot is on minors, so collect as little personal data as
    possible). An earlier uncommitted draft added an `email` column; databases
    that already have it keep it, unused — migrations only ever add.

    Two SQLite specifics worth knowing:
      * there is no `ALTER TABLE ... ADD COLUMN IF NOT EXISTS`, so we read
        `PRAGMA table_info` and compare names ourselves;
      * `ADD COLUMN ... UNIQUE` is outright rejected by SQLite, so username
        uniqueness comes from a separate unique *index*. A unique index still
        permits many NULLs (SQLite treats NULLs as distinct), which is exactly
        what legacy rows need.
    """
    existing = {row["name"] for row in conn.execute("PRAGMA table_info(students)")}

    if "username" not in existing:
        conn.execute("ALTER TABLE students ADD COLUMN username TEXT")
    if "password_hash" not in existing:
        conn.execute("ALTER TABLE students ADD COLUMN password_hash TEXT")
    # The class a teacher created this account in; NULL for self-registered and
    # legacy students. A teacher may reset a password only within their own classes.
    if "class_id" not in existing:
        conn.execute("ALTER TABLE students ADD COLUMN class_id TEXT")

    conn.execute(
        "CREATE UNIQUE INDEX IF NOT EXISTS idx_students_username "
        "ON students(username)"
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_students_class ON students(class_id)")
    conn.commit()


def _now_iso() -> str:
    """Current UTC time as an ISO-8601 string that round-trips on Python 3.10."""
    return datetime.now(tz=timezone.utc).isoformat()


def _row_to_dict(row: sqlite3.Row) -> dict[str, Any]:
    return {
        "concept_id": row["concept_id"],
        "status": row["status"],
        "best_score": row["best_score"],
        "attempts": row["attempts"],
        "last_seen": row["last_seen"],
    }


def get_progress(student_id: str) -> dict[str, dict[str, Any]]:
    """Return all progress rows for a student, keyed by concept_id.

    Each value is {status, best_score, attempts, last_seen, concept_id}. An
    empty dict means the student has no recorded progress yet.
    """
    conn = _connect()
    try:
        rows = conn.execute(
            "SELECT * FROM progress WHERE student_id = ?",
            (student_id,),
        ).fetchall()
    finally:
        conn.close()
    return {row["concept_id"]: _row_to_dict(row) for row in rows}


def update_progress(
    student_id: str,
    concept_id: str,
    score: int,
    *,
    seen_at: datetime | None = None,
) -> dict[str, Any]:
    """Record an attempt on a concept and return the updated row.

    Mirrors app.py's `_update_mastery`: attempts increments by one, best_score
    takes the maximum over all attempts (a student who finally nails it has
    demonstrably learned), and status is derived from the best score. last_seen
    is set to now (or `seen_at` if given — used by tests to simulate the past).
    """
    score = int(score)
    last_seen = (seen_at.astimezone(timezone.utc).isoformat()
                 if seen_at is not None else _now_iso())

    conn = _connect()
    try:
        existing = conn.execute(
            "SELECT best_score, attempts FROM progress "
            "WHERE student_id = ? AND concept_id = ?",
            (student_id, concept_id),
        ).fetchone()

        prev_best = existing["best_score"] if existing else 0
        prev_attempts = existing["attempts"] if existing else 0

        best_score = max(prev_best, score)
        attempts = prev_attempts + 1
        status = status_from_score(best_score)

        conn.execute(
            """
            INSERT INTO progress
                (student_id, concept_id, status, best_score, attempts, last_seen)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(student_id, concept_id) DO UPDATE SET
                status     = excluded.status,
                best_score = excluded.best_score,
                attempts   = excluded.attempts,
                last_seen  = excluded.last_seen
            """,
            (student_id, concept_id, status, best_score, attempts, last_seen),
        )
        conn.commit()
    finally:
        conn.close()

    return {
        "concept_id": concept_id,
        "status": status,
        "best_score": best_score,
        "attempts": attempts,
        "last_seen": last_seen,
    }


def mark_reviewed(
    student_id: str,
    concept_id: str,
    *,
    seen_at: datetime | None = None,
) -> None:
    """Update only last_seen for a concept, without touching score or attempts.

    Used when a student revisits an already-mastered concept (spaced-repetition
    review): the review refreshes recency but isn't a fresh graded attempt.
    No-op if the concept has no row yet (nothing to review).
    """
    last_seen = (seen_at.astimezone(timezone.utc).isoformat()
                 if seen_at is not None else _now_iso())
    conn = _connect()
    try:
        conn.execute(
            "UPDATE progress SET last_seen = ? "
            "WHERE student_id = ? AND concept_id = ?",
            (last_seen, student_id, concept_id),
        )
        conn.commit()
    finally:
        conn.close()


def get_mastered_concepts(student_id: str) -> set[str]:
    """Return the set of concept_ids the student has mastered (status=mastered)."""
    conn = _connect()
    try:
        rows = conn.execute(
            "SELECT concept_id FROM progress "
            "WHERE student_id = ? AND status = ?",
            (student_id, STATUS_MASTERED),
        ).fetchall()
    finally:
        conn.close()
    return {row["concept_id"] for row in rows}


def get_cleared_concepts(student_id: str) -> set[str]:
    """Return concept_ids the student has *cleared* (best_score >= 2).

    "Cleared" is the progression bar: a partial pass (2/3) or full mastery
    (3/3). It's what the path engine uses to decide a concept no longer blocks
    forward progress and that its dependents may unlock — so a student who
    scored 2/3 can choose to move on. Mastery (3/3) remains the distinct gold
    status shown on the roadmap and used for spaced-repetition review.
    """
    conn = _connect()
    try:
        rows = conn.execute(
            "SELECT concept_id FROM progress "
            "WHERE student_id = ? AND best_score >= 2",
            (student_id,),
        ).fetchall()
    finally:
        conn.close()
    return {row["concept_id"] for row in rows}


# ---------------------------------------------------------------------------
# Student profiles
# ---------------------------------------------------------------------------

def get_student(student_id: str) -> dict[str, Any] | None:
    """Return a student's profile dict, or None if no such student exists.

    **Never** includes `password_hash` — the profile is the shape that crosses
    the service boundary and reaches a browser. Only
    `get_student_by_username` (the login path) sees the hash.
    """
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT * FROM students WHERE student_id = ?",
            (student_id,),
        ).fetchone()
    finally:
        conn.close()
    if row is None:
        return None
    return _student_to_dict(row)


def save_student(
    student_id: str,
    name: str,
    interest: str,
    level: str,
) -> dict[str, Any]:
    """Insert or update a student profile and return it.

    created_at is set once on first insert and preserved on later updates, so
    a returning student keeps their original join date even if they change
    interest or level.
    """
    conn = _connect()
    try:
        existing = conn.execute(
            "SELECT created_at FROM students WHERE student_id = ?",
            (student_id,),
        ).fetchone()
        created_at = existing["created_at"] if existing else _now_iso()

        conn.execute(
            """
            INSERT INTO students (student_id, name, interest, level, created_at)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(student_id) DO UPDATE SET
                name     = excluded.name,
                interest = excluded.interest,
                level    = excluded.level
            """,
            (student_id, name, interest, level, created_at),
        )
        conn.commit()
    finally:
        conn.close()

    return {
        "student_id": student_id,
        "name": name,
        "interest": interest,
        "level": level,
        "created_at": created_at,
    }


def _student_to_dict(row: sqlite3.Row) -> dict[str, Any]:
    """Map a `students` row to the public profile dict.

    Field-by-field on purpose (not `dict(row)`): the row also carries
    `password_hash`, and a secret must never leave this module by accident when
    someone later adds a column. Whitelist, don't blacklist.
    """
    return {
        "student_id": row["student_id"],
        "name": row["name"],
        "interest": row["interest"],
        "level": row["level"],
        "created_at": row["created_at"],
        # Nullable: legacy name-only students have no username.
        "username": row["username"],
    }


def get_student_by_username(username: str) -> dict[str, Any] | None:
    """Return the full student row **including `password_hash`**, or None.

    The one function that exposes the hash, because authentication needs to
    compare against it. Its result must stay inside the backend — pass the
    profile from `get_student` to anything that talks to a client.

    Username matching is case-insensitive: usernames are stored already
    normalised (lowercased + stripped by the boundary), and we normalise the
    lookup too so "Ada_K" finds the account registered as "ada_k".
    """
    normalised = username.strip().lower()
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT * FROM students WHERE username = ?",
            (normalised,),
        ).fetchone()
    finally:
        conn.close()
    if row is None:
        return None
    profile = _student_to_dict(row)
    profile["password_hash"] = row["password_hash"]
    return profile


def save_student_with_credentials(
    student_id: str,
    name: str,
    interest: str,
    level: str,
    username: str,
    password_hash: str,
) -> dict[str, Any]:
    """Insert a brand-new student that has real credentials.

    Unlike `save_student` this is a strict INSERT — no upsert. A caller that
    lands on a duplicate must decide what that means (the boundary turns it into
    a ConflictError), and silently overwriting an existing account's password
    would be a security hole.

    Raises:
        sqlite3.IntegrityError: if the student_id or username is already
                                taken (the unique index on `username`
                                enforces the latter). The boundary translates
                                this.
    """
    created_at = _now_iso()
    conn = _connect()
    try:
        conn.execute(
            """
            INSERT INTO students
                (student_id, name, interest, level, created_at, username, password_hash)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (student_id, name, interest, level, created_at,
             username.strip().lower(), password_hash),
        )
        conn.commit()
    finally:
        conn.close()

    return {
        "student_id": student_id,
        "name": name,
        "interest": interest,
        "level": level,
        "created_at": created_at,
        "username": username.strip().lower(),
    }


def update_student_profile(
    student_id: str,
    *,
    name: str | None = None,
    interest: str | None = None,
    level: str | None = None,
) -> dict[str, Any] | None:
    """Patch the editable profile fields, leaving the rest untouched.

    Every argument is optional: this is a PATCH, not a PUT, so passing only
    `interest` changes only the interest. Returns the updated profile, or None
    if the student does not exist (the caller decides whether that is a 404).
    """
    updates: list[str] = []
    values: list[Any] = []
    for column, value in (("name", name), ("interest", interest), ("level", level)):
        if value is not None:
            updates.append(f"{column} = ?")
            values.append(value)

    if updates:
        conn = _connect()
        try:
            cursor = conn.execute(
                f"UPDATE students SET {', '.join(updates)} WHERE student_id = ?",
                (*values, student_id),
            )
            conn.commit()
            if cursor.rowcount == 0:
                return None
        finally:
            conn.close()

    return get_student(student_id)


def update_student_password(student_id: str, password_hash: str) -> bool:
    """Replace a student's password hash. Returns False if no such student.

    Takes an already-hashed value — this module never sees a plaintext password;
    hashing belongs to `src/auth/passwords.py`.
    """
    conn = _connect()
    try:
        cursor = conn.execute(
            "UPDATE students SET password_hash = ? WHERE student_id = ?",
            (password_hash, student_id),
        )
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()


def get_password_hash(student_id: str) -> str | None:
    """Return a student's stored password hash, or None.

    None means one of two different things — no such student, or a legacy
    name-only student who never had a password. Neither can authenticate, so the
    caller treats them alike; when it needs to tell them apart it also calls
    `get_student`.
    """
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT password_hash FROM students WHERE student_id = ?",
            (student_id,),
        ).fetchone()
    finally:
        conn.close()
    return row["password_hash"] if row is not None else None


# ---------------------------------------------------------------------------
# Teachers and classes (2026-10-02)
#
# The pilot accounts belong to minors and carry no email, so a forgotten
# password can only be fixed by an adult with authority over the account: the
# teacher who created it. These functions are the storage half of that; the
# rules (who may do what) live in the boundary, src/platform_api.py.
# ---------------------------------------------------------------------------

def _teacher_to_dict(row: sqlite3.Row) -> dict[str, Any]:
    """Public teacher profile. Whitelisted for the same reason as students."""
    return {
        "teacher_id": row["teacher_id"],
        "name": row["name"],
        "username": row["username"],
        "created_at": row["created_at"],
    }


def _class_to_dict(row: sqlite3.Row) -> dict[str, Any]:
    out = {
        "class_id": row["class_id"],
        "teacher_id": row["teacher_id"],
        "name": row["name"],
        "level": row["level"],
        "created_at": row["created_at"],
    }
    if "student_count" in row.keys():
        out["student_count"] = row["student_count"]
    return out


def username_exists(username: str) -> bool:
    """True if a student OR a teacher already has this username.

    One login namespace for both: a username on a printed slip must point at
    exactly one account, whichever login page it is typed into.
    """
    normalised = username.strip().lower()
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT 1 FROM students WHERE username = ? "
            "UNION ALL SELECT 1 FROM teachers WHERE username = ? LIMIT 1",
            (normalised, normalised),
        ).fetchone()
    finally:
        conn.close()
    return row is not None


def save_teacher(
    teacher_id: str, name: str, username: str, password_hash: str
) -> dict[str, Any]:
    """Insert a teacher. Strict INSERT: raises sqlite3.IntegrityError on a duplicate."""
    created_at = _now_iso()
    conn = _connect()
    try:
        conn.execute(
            "INSERT INTO teachers (teacher_id, name, username, password_hash, created_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (teacher_id, name, username.strip().lower(), password_hash, created_at),
        )
        conn.commit()
    finally:
        conn.close()
    return {"teacher_id": teacher_id, "name": name,
            "username": username.strip().lower(), "created_at": created_at}


def get_teacher(teacher_id: str) -> dict[str, Any] | None:
    """Public profile of a teacher (no hash), or None."""
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT * FROM teachers WHERE teacher_id = ?", (teacher_id,)
        ).fetchone()
    finally:
        conn.close()
    return _teacher_to_dict(row) if row is not None else None


def get_teacher_by_username(username: str) -> dict[str, Any] | None:
    """Teacher row **including `password_hash`** — for authentication only."""
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT * FROM teachers WHERE username = ?", (username.strip().lower(),)
        ).fetchone()
    finally:
        conn.close()
    if row is None:
        return None
    profile = _teacher_to_dict(row)
    profile["password_hash"] = row["password_hash"]
    return profile


def get_teacher_password_hash(teacher_id: str) -> str | None:
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT password_hash FROM teachers WHERE teacher_id = ?", (teacher_id,)
        ).fetchone()
    finally:
        conn.close()
    return row["password_hash"] if row is not None else None


def update_teacher_password(teacher_id: str, password_hash: str) -> bool:
    conn = _connect()
    try:
        cursor = conn.execute(
            "UPDATE teachers SET password_hash = ? WHERE teacher_id = ?",
            (password_hash, teacher_id),
        )
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()


def create_class(class_id: str, teacher_id: str, name: str, level: str) -> dict[str, Any]:
    created_at = _now_iso()
    conn = _connect()
    try:
        conn.execute(
            "INSERT INTO classes (class_id, teacher_id, name, level, created_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (class_id, teacher_id, name, level, created_at),
        )
        conn.commit()
    finally:
        conn.close()
    return {"class_id": class_id, "teacher_id": teacher_id, "name": name,
            "level": level, "created_at": created_at, "student_count": 0}


_CLASS_WITH_COUNT = """
    SELECT c.*, (SELECT COUNT(*) FROM students s WHERE s.class_id = c.class_id)
               AS student_count
    FROM classes c
"""


def get_class(class_id: str) -> dict[str, Any] | None:
    conn = _connect()
    try:
        row = conn.execute(
            _CLASS_WITH_COUNT + " WHERE c.class_id = ?", (class_id,)
        ).fetchone()
    finally:
        conn.close()
    return _class_to_dict(row) if row is not None else None


def list_classes(teacher_id: str) -> list[dict[str, Any]]:
    """A teacher's classes, newest first, each with its student count."""
    conn = _connect()
    try:
        rows = conn.execute(
            _CLASS_WITH_COUNT + " WHERE c.teacher_id = ? ORDER BY c.created_at DESC",
            (teacher_id,),
        ).fetchall()
    finally:
        conn.close()
    return [_class_to_dict(r) for r in rows]


def save_students_bulk(class_id: str, students: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Insert several credentialed students into a class in ONE transaction.

    Each item: {student_id, name, interest, level, username, password_hash}.
    All or nothing: if any row fails (a username claimed a moment ago by someone
    else), the whole roster is rolled back, so a teacher never ends up with half
    a class and a slip sheet that doesn't match the database.

    Raises:
        sqlite3.IntegrityError: a duplicate username or id; nothing was saved.
    """
    created_at = _now_iso()
    conn = _connect()
    try:
        with conn:  # commits on success, rolls back on any exception
            conn.executemany(
                """
                INSERT INTO students (student_id, name, interest, level, created_at,
                                      username, password_hash, class_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (s["student_id"], s["name"], s["interest"], s["level"], created_at,
                     s["username"].strip().lower(), s["password_hash"], class_id)
                    for s in students
                ],
            )
    finally:
        conn.close()
    return [
        {"student_id": s["student_id"], "name": s["name"], "interest": s["interest"],
         "level": s["level"], "created_at": created_at,
         "username": s["username"].strip().lower()}
        for s in students
    ]


def get_student_class_id(student_id: str) -> str | None:
    """The class a student was created in, or None (self-registered / legacy / unknown)."""
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT class_id FROM students WHERE student_id = ?", (student_id,)
        ).fetchone()
    finally:
        conn.close()
    return row["class_id"] if row is not None else None


def list_class_students(class_id: str) -> list[dict[str, Any]]:
    """Students in a class, by name, each with a progress summary.

    The summary is aggregated in SQL from the `progress` table: how many concepts
    the student has mastered, how many they have attempted at all, and when they
    last did anything. Enough for a teacher to spot who hasn't started.
    """
    conn = _connect()
    try:
        rows = conn.execute(
            """
            SELECT s.student_id, s.name, s.username, s.interest, s.level, s.created_at,
                   COUNT(p.concept_id)                                   AS attempted,
                   COALESCE(SUM(CASE WHEN p.status = ? THEN 1 END), 0)   AS mastered,
                   MAX(p.last_seen)                                      AS last_active
            FROM students s
            LEFT JOIN progress p ON p.student_id = s.student_id
            WHERE s.class_id = ?
            GROUP BY s.student_id
            ORDER BY s.name COLLATE NOCASE, s.username
            """,
            (STATUS_MASTERED, class_id),
        ).fetchall()
    finally:
        conn.close()
    return [
        {"student_id": r["student_id"], "name": r["name"], "username": r["username"],
         "interest": r["interest"], "level": r["level"], "created_at": r["created_at"],
         "attempted": r["attempted"], "mastered": r["mastered"],
         "last_active": r["last_active"]}
        for r in rows
    ]


# ---------------------------------------------------------------------------
# Pilot metrics (2026-10-02)
#
# What the pilot needs to show: did students open lessons, how long did they
# actually read, what did they get wrong (and which misconception that
# reveals), and did the interest-based explanation work for them (👍/👎).
# The rules — caps, ownership, who may read what — live in the boundary; these
# functions only store and fetch.
# ---------------------------------------------------------------------------

def create_lesson_view(view_id: str, student_id: str, concept_id: str, interest: str) -> dict[str, Any]:
    opened_at = _now_iso()
    conn = _connect()
    try:
        conn.execute(
            "INSERT INTO lesson_views (view_id, student_id, concept_id, interest, opened_at, "
            "active_seconds) VALUES (?, ?, ?, ?, ?, 0)",
            (view_id, student_id, concept_id, interest, opened_at),
        )
        conn.commit()
    finally:
        conn.close()
    return {"view_id": view_id, "student_id": student_id, "concept_id": concept_id,
            "interest": interest, "opened_at": opened_at, "active_seconds": 0}


def get_lesson_view(view_id: str) -> dict[str, Any] | None:
    conn = _connect()
    try:
        row = conn.execute("SELECT * FROM lesson_views WHERE view_id = ?", (view_id,)).fetchone()
    finally:
        conn.close()
    return dict(row) if row is not None else None


def set_lesson_view_seconds(view_id: str, active_seconds: int) -> None:
    """Raise a view's active time to `active_seconds`, never lower it.

    The browser reports a running total, possibly more than once and out of
    order (a heartbeat and a page-hide can race). Keeping the maximum makes
    every report safe to repeat.
    """
    conn = _connect()
    try:
        conn.execute(
            "UPDATE lesson_views SET active_seconds = MAX(active_seconds, ?) WHERE view_id = ?",
            (int(active_seconds), view_id),
        )
        conn.commit()
    finally:
        conn.close()


def record_answer(
    student_id: str,
    concept_id: str,
    interest: str,
    selected: str,
    correct: bool,
    misconception: str | None,
) -> dict[str, Any]:
    """Store one multiple-choice pick and return it with its attempt number.

    attempt_no counts this student's picks on this concept, across interests:
    attempt 1 is the honest measurement, because after a wrong pick the app
    shows the right answer.
    """
    answered_at = _now_iso()
    conn = _connect()
    try:
        with conn:
            (previous,) = conn.execute(
                "SELECT COUNT(*) FROM answers WHERE student_id = ? AND concept_id = ?",
                (student_id, concept_id),
            ).fetchone()
            attempt_no = previous + 1
            conn.execute(
                "INSERT INTO answers (student_id, concept_id, interest, selected, correct, "
                "attempt_no, misconception, answered_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (student_id, concept_id, interest, selected, int(bool(correct)), attempt_no,
                 misconception, answered_at),
            )
    finally:
        conn.close()
    return {"student_id": student_id, "concept_id": concept_id, "interest": interest,
            "selected": selected, "correct": bool(correct), "attempt_no": attempt_no,
            "misconception": misconception, "answered_at": answered_at}


def set_lesson_rating(student_id: str, concept_id: str, interest: str, rating: int) -> None:
    """Save +1 / -1 for a lesson, replacing any earlier rating; 0 removes it."""
    conn = _connect()
    try:
        if rating == 0:
            conn.execute(
                "DELETE FROM lesson_ratings WHERE student_id = ? AND concept_id = ? AND interest = ?",
                (student_id, concept_id, interest),
            )
        else:
            conn.execute(
                """
                INSERT INTO lesson_ratings (student_id, concept_id, interest, rating, rated_at)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(student_id, concept_id, interest) DO UPDATE SET
                    rating = excluded.rating, rated_at = excluded.rated_at
                """,
                (student_id, concept_id, interest, int(rating), _now_iso()),
            )
        conn.commit()
    finally:
        conn.close()


def get_lesson_rating(student_id: str, concept_id: str, interest: str) -> int:
    """The student's rating of this lesson: 1, -1, or 0 for none."""
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT rating FROM lesson_ratings WHERE student_id = ? AND concept_id = ? "
            "AND interest = ?",
            (student_id, concept_id, interest),
        ).fetchone()
    finally:
        conn.close()
    return int(row["rating"]) if row is not None else 0


def get_activity(student_ids: list[str] | None = None) -> dict[str, list[dict[str, Any]]]:
    """Raw metric rows — views, answers, ratings — for some students, or everyone.

    Returned as plain lists so the aggregation (src/progress/metrics.py) stays a
    pure function that tests can feed directly. At pilot scale (a class of ~40,
    a few hundred events each) fetching the rows is cheaper to reason about
    than one SQL query per statistic.
    """
    conn = _connect()
    try:
        out: dict[str, list[dict[str, Any]]] = {}
        for key, table, order in (
            ("views", "lesson_views", "opened_at"),
            ("answers", "answers", "answer_id"),
            ("ratings", "lesson_ratings", "rated_at"),
        ):
            if student_ids is None:
                rows = conn.execute(f"SELECT * FROM {table} ORDER BY {order}").fetchall()
            elif not student_ids:
                rows = []
            else:
                marks = ",".join("?" * len(student_ids))
                rows = conn.execute(
                    f"SELECT * FROM {table} WHERE student_id IN ({marks}) ORDER BY {order}",
                    student_ids,
                ).fetchall()
            out[key] = [dict(r) for r in rows]
    finally:
        conn.close()
    for answer in out["answers"]:
        answer["correct"] = bool(answer["correct"])
    return out


def list_all_students() -> list[dict[str, Any]]:
    """Every student's public profile plus class_id — for the server-side pilot report."""
    conn = _connect()
    try:
        rows = conn.execute("SELECT * FROM students ORDER BY created_at").fetchall()
    finally:
        conn.close()
    out = []
    for row in rows:
        profile = _student_to_dict(row)
        profile["class_id"] = row["class_id"]
        out.append(profile)
    return out
