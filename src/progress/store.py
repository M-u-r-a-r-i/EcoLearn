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
    return conn


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


# ---------------------------------------------------------------------------
# Student profiles
# ---------------------------------------------------------------------------

def get_student(student_id: str) -> dict[str, Any] | None:
    """Return a student's profile dict, or None if no such student exists."""
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
    return {
        "student_id": row["student_id"],
        "name": row["name"],
        "interest": row["interest"],
        "level": row["level"],
        "created_at": row["created_at"],
    }


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
