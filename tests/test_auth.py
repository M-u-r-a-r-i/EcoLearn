"""Deterministic tests for the accounts/auth core (Milestone 0). No LLM calls.

Covers the three layers added for real accounts:

  1. MIGRATION  — an old-shape `students` table (no email/password_hash) is
                  upgraded in place, idempotently, without disturbing its rows.
  2. PASSWORDS  — bcrypt hashing, the 72-BYTE limit, and the guarantee that
                  `verify_password` never raises.
  3. BOUNDARY   — register / authenticate / get_profile / update_profile /
                  change_password, including every error branch and the
                  promise that a password hash never crosses the boundary.

It also pins the two backwards-compatibility contracts: the legacy slug id
still works, and account ids are provably disjoint from slug ids.

Run it (no API key needed):
    venv\\Scripts\\python.exe tests\\test_auth.py
"""

from __future__ import annotations

import os
import sqlite3
import sys
import tempfile
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

# Point the store at a throwaway DB BEFORE importing anything that opens it.
# (The store resolves this env var lazily inside _connect(), which is exactly
# what makes this redirect possible.)
_TMP_DIR = Path(tempfile.mkdtemp(prefix="ecolearn_auth_test_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP_DIR / "auth_test.db")

from src import platform_api as api  # noqa: E402
from src.auth import passwords  # noqa: E402
from src.errors import (  # noqa: E402
    AuthError,
    ConflictError,
    EcoLearnError,
    NotFoundError,
)
from src.progress import store  # noqa: E402

_CHECKS = 0


def check(label: str, condition: bool) -> None:
    """Assert and report one expectation."""
    global _CHECKS
    _CHECKS += 1
    print(f"  {'PASS' if condition else 'FAIL'}  {label}")
    assert condition, label


def check_raises(label: str, exc: type[Exception], fn, *args, **kwargs) -> None:
    """Assert that `fn` raises exactly `exc` (or a subclass)."""
    global _CHECKS
    _CHECKS += 1
    try:
        fn(*args, **kwargs)
    except exc as err:
        print(f"  PASS  {label}  →  {type(err).__name__}: {err}")
        return
    except Exception as err:  # noqa: BLE001 - we want the wrong type reported
        print(f"  FAIL  {label}  →  expected {exc.__name__}, got {type(err).__name__}: {err}")
        raise AssertionError(label) from err
    print(f"  FAIL  {label}  →  expected {exc.__name__}, nothing raised")
    raise AssertionError(label)


# ---------------------------------------------------------------------------
# 1. Migration — an old database must upgrade in place
# ---------------------------------------------------------------------------

def test_migration() -> None:
    """A pre-auth `students` table gains the account columns, idempotently."""
    print("\n[1] MIGRATION from an old-shape database")

    old_db = _TMP_DIR / "old_shape.db"
    conn = sqlite3.connect(old_db)
    conn.execute(
        """
        CREATE TABLE students (
            student_id  TEXT PRIMARY KEY,
            name        TEXT NOT NULL,
            interest    TEXT NOT NULL,
            level       TEXT NOT NULL,
            created_at  TEXT NOT NULL
        )
        """
    )
    conn.execute(
        "INSERT INTO students VALUES "
        "('legacy-kid', 'Legacy Kid', 'football', 'Class 11', '2026-01-01T00:00:00+00:00')"
    )
    conn.commit()
    conn.close()

    # Redirect the store at the old DB; the first _connect() migrates it.
    original = os.environ["ECOLEARN_PROGRESS_DB"]
    os.environ["ECOLEARN_PROGRESS_DB"] = str(old_db)
    try:
        profile = store.get_student("legacy-kid")
        check("legacy row still loads", profile is not None)
        check("legacy name preserved", profile["name"] == "Legacy Kid")
        check("legacy created_at preserved", profile["created_at"].startswith("2026-01-01"))
        check("legacy email is NULL", profile["email"] is None)
        check("password_hash never in a profile dict", "password_hash" not in profile)

        columns = {row[1] for row in sqlite3.connect(old_db).execute("PRAGMA table_info(students)")}
        check("email column added", "email" in columns)
        check("password_hash column added", "password_hash" in columns)

        # Second connect must be a no-op, not an error.
        store.get_student("legacy-kid")
        check("migration is idempotent (second connect ok)", True)

        # A unique index on a nullable column still allows many NULLs — which is
        # what every legacy, password-less student relies on.
        store.save_student("legacy-two", "Legacy Two", "gaming", "Class 11")
        store.save_student("legacy-three", "Legacy Three", "gaming", "Class 11")
        check("multiple NULL emails coexist", len(store.get_student("legacy-two")) > 0)
    finally:
        os.environ["ECOLEARN_PROGRESS_DB"] = original


# ---------------------------------------------------------------------------
# 2. Passwords — hashing and the 72-byte cliff
# ---------------------------------------------------------------------------

def test_passwords() -> None:
    """bcrypt round-trips, and every bad input fails closed instead of raising."""
    print("\n[2] PASSWORD hashing")

    digest = passwords.hash_password("correct horse battery")
    check("hash is bcrypt-formatted", digest.startswith("$2b$"))
    check("hash does not contain the plaintext", "correct horse battery" not in digest)
    check("correct password verifies", passwords.verify_password("correct horse battery", digest))
    check("wrong password rejected", not passwords.verify_password("wrong", digest))

    # bcrypt hashes at most 72 BYTES. bcrypt>=5 raises where bcrypt 4 silently
    # truncated; either way it must never surface as a 500 on a login attempt.
    check_raises("over-long password rejected at hash time", EcoLearnError,
                 passwords.hash_password, "x" * 100)
    check("over-long password fails verification without raising",
          not passwords.verify_password("x" * 100, digest))
    check("emoji count as multiple bytes (30 emoji > 72 bytes)",
          not passwords.is_hashable("\U0001f600" * 30))

    check_raises("too-short password rejected", EcoLearnError, passwords.hash_password, "short")
    check_raises("empty password rejected", EcoLearnError, passwords.hash_password, "")

    check("no stored hash fails verification", not passwords.verify_password("anything", None))
    check("corrupt stored hash fails verification",
          not passwords.verify_password("anything", "not-a-bcrypt-hash"))

    passwords.dummy_verify()  # must not raise; used on the unknown-email path
    check("dummy_verify runs (constant-time login path)", True)


# ---------------------------------------------------------------------------
# 3. Boundary — the five account functions
# ---------------------------------------------------------------------------

def test_register() -> None:
    """Registration normalises input, rejects bad input, and hides the hash."""
    print("\n[3] REGISTER")

    profile = api.register_student(
        name="Ada Lovelace",
        email="  Ada@Example.COM ",
        password="hunter2hunter2",
        interest="football",
        level="Class 11",
    )
    check("account id uses the stu_ scheme", profile["student_id"].startswith("stu_"))
    check("account id contains '_' (disjoint from any slug)", "_" in profile["student_id"])
    check("email normalised to lowercase + trimmed", profile["email"] == "ada@example.com")
    check("password_hash absent from the returned profile", "password_hash" not in profile)
    check("name trimmed", profile["name"] == "Ada Lovelace")

    check_raises("duplicate email (case-insensitive) conflicts", ConflictError,
                 api.register_student, "Impostor", "ADA@EXAMPLE.COM", "another12345", "gaming")
    check_raises("malformed email rejected", EcoLearnError,
                 api.register_student, "X", "not-an-email", "another12345", "gaming")
    check_raises("short password rejected", EcoLearnError,
                 api.register_student, "X", "new@example.com", "short", "gaming")
    check_raises("blank name rejected", EcoLearnError,
                 api.register_student, "   ", "new@example.com", "another12345", "gaming")
    check_raises("blank interest rejected", EcoLearnError,
                 api.register_student, "X", "new@example.com", "another12345", "  ")

    return profile


def test_authenticate(registered: dict) -> None:
    """Login succeeds on the right password and is uniform on every failure."""
    print("\n[4] AUTHENTICATE")

    signed_in = api.authenticate_student("  ADA@Example.com", "hunter2hunter2")
    check("login returns the same account", signed_in["student_id"] == registered["student_id"])
    check("login result carries no password_hash", "password_hash" not in signed_in)

    # All three failure branches must be indistinguishable to a caller: same
    # exception type, same message. Anything else is an enumeration oracle.
    messages = []
    for label, email, password in (
        ("wrong password", "ada@example.com", "wrongwrongwrong"),
        ("unknown email", "nobody@example.com", "hunter2hunter2"),
        ("malformed email", "junk", "hunter2hunter2"),
    ):
        try:
            api.authenticate_student(email, password)
            raise AssertionError(f"{label} should not authenticate")
        except AuthError as err:
            messages.append(str(err))
            print(f"  PASS  {label} rejected  →  {err}")
            global _CHECKS
            _CHECKS += 1

    check("all login failures share one message (no email enumeration)",
          len(set(messages)) == 1)


def test_profile(registered: dict) -> None:
    """Profile reads and patches behave, and unknown ids 404 rather than crash."""
    print("\n[5] PROFILE read + patch")

    student_id = registered["student_id"]
    check("profile readable by id", api.get_student_profile(student_id)["name"] == "Ada Lovelace")
    check_raises("unknown student id is NotFound", NotFoundError,
                 api.get_student_profile, "stu_does_not_exist")

    patched = api.update_student_profile(student_id, interest="gaming")
    check("interest patched", patched["interest"] == "gaming")
    check("untouched fields preserved", patched["name"] == "Ada Lovelace")
    check("created_at preserved across a patch",
          patched["created_at"] == registered["created_at"])

    renamed = api.update_student_profile(student_id, name="Ada L.", level="Class 12")
    check("multi-field patch applied", renamed["name"] == "Ada L." and renamed["level"] == "Class 12")
    check("patch did not disturb the email", renamed["email"] == "ada@example.com")

    check_raises("empty patch rejected", EcoLearnError, api.update_student_profile, student_id)
    check_raises("blank interest rejected", EcoLearnError,
                 api.update_student_profile, student_id, interest="   ")
    check_raises("patching an unknown id is NotFound", NotFoundError,
                 api.update_student_profile, "stu_does_not_exist", interest="gaming")


def test_change_password(registered: dict) -> None:
    """Changing a password requires the current one and invalidates it."""
    print("\n[6] CHANGE PASSWORD")

    student_id = registered["student_id"]
    result = api.change_password(student_id, "hunter2hunter2", "brandnewpassword")
    check("change reported", result == {"student_id": student_id, "changed": True})

    check_raises("the old password no longer works", AuthError,
                 api.authenticate_student, "ada@example.com", "hunter2hunter2")
    check("the new password works",
          api.authenticate_student("ada@example.com", "brandnewpassword")["student_id"] == student_id)

    check_raises("wrong current password rejected", AuthError,
                 api.change_password, student_id, "notmypassword", "yetanotherpw1")
    check_raises("reusing the current password rejected", EcoLearnError,
                 api.change_password, student_id, "brandnewpassword", "brandnewpassword")
    check_raises("too-short new password rejected", EcoLearnError,
                 api.change_password, student_id, "brandnewpassword", "tiny")
    check_raises("changing an unknown id is NotFound", NotFoundError,
                 api.change_password, "stu_does_not_exist", "whatever12345", "another123456")


def test_legacy_contract() -> None:
    """The pre-auth, name-as-identity path must be completely unaffected."""
    print("\n[7] LEGACY contract (Streamlit + the pinned journey test)")

    legacy = api.create_or_load_student("Journey Student", "football", "Class 11")
    check("legacy slug id unchanged", legacy["student_id"] == "journey-student")
    check("legacy ids contain no '_' (disjoint from stu_ ids)", "_" not in legacy["student_id"])

    again = api.create_or_load_student("Journey Student", "gaming", "Class 12")
    check("create_or_load is still idempotent", again["student_id"] == legacy["student_id"])
    check("legacy interest still refreshes on load", again["interest"] == "gaming")
    check("legacy student has no email", again.get("email") is None)

    # A legacy student cannot authenticate — there is no password to check —
    # and that must surface as an auth failure, never a crash.
    check("a password-less legacy account cannot log in",
          not passwords.verify_password("anything", store.get_password_hash("journey-student")))


def main() -> None:
    print("=" * 70)
    print("EcoLearn — accounts/auth core (deterministic, no LLM)")
    print(f"temp DB: {os.environ['ECOLEARN_PROGRESS_DB']}")
    print("=" * 70)

    test_migration()
    test_passwords()
    registered = test_register()
    test_authenticate(registered)
    test_profile(registered)
    test_change_password(registered)
    test_legacy_contract()

    print("\n" + "=" * 70)
    print(f"ALL {_CHECKS} CHECKS PASSED")
    print("=" * 70)


if __name__ == "__main__":
    main()
