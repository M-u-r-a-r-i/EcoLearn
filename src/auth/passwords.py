"""Password hashing and verification (bcrypt).

WHY BCRYPT DIRECTLY (not passlib)
---------------------------------
passlib is unmaintained and its bcrypt backend breaks against modern bcrypt
releases (it reads a private `__about__` attribute that no longer exists). The
`bcrypt` package is the actual implementation underneath anyway, so we call it
directly — one dependency, no compatibility layer.

THE 72-BYTE LIMIT (the gotcha that bites)
-----------------------------------------
bcrypt hashes at most **72 bytes** of input. bcrypt < 5 silently truncated
anything longer; bcrypt >= 5 raises `ValueError` instead. Either behaviour is a
trap: silent truncation makes two different long passwords equivalent, and the
raise turns a login attempt into an unhandled 500. So we handle it explicitly:

  * `validate_password` rejects over-long passwords **up front** (at register
    and at change-password) with a clear, actionable message;
  * `verify_password` never raises — an over-long or malformed input simply
    fails to verify, because it cannot possibly match a stored hash.

Note the limit is in **bytes, not characters**: one emoji is 4 bytes, so we
measure the UTF-8 encoding, not `len(password)`.
"""

from __future__ import annotations

import bcrypt

from src.errors import EcoLearnError

# bcrypt's hard algorithmic limit. Anything longer cannot be hashed.
MAX_PASSWORD_BYTES = 72

# Our own floor. Short enough not to annoy students, long enough to be worth
# hashing. (Deliberately not a complexity rule — length beats character classes.)
MIN_PASSWORD_LENGTH = 8

# A real bcrypt hash of a throwaway value, used only by `dummy_verify` to burn
# the same ~100ms an actual verification costs when the email is unknown. Built
# once at import so the cost isn't paid twice on that path.
_DUMMY_HASH = bcrypt.hashpw(b"ecolearn-dummy-password", bcrypt.gensalt()).decode("utf-8")


def validate_password(password: str) -> None:
    """Raise EcoLearnError unless `password` is a hashable, long-enough secret.

    Call this wherever a *new* password is being set (register, change-password)
    so the user gets a specific message instead of a generic failure.

    Raises:
        EcoLearnError: if the password is too short, or longer than bcrypt can
                       hash (72 bytes of UTF-8).
    """
    if not isinstance(password, str) or not password:
        raise EcoLearnError("Password is required.")
    if len(password) < MIN_PASSWORD_LENGTH:
        raise EcoLearnError(
            f"Password must be at least {MIN_PASSWORD_LENGTH} characters."
        )
    if len(password.encode("utf-8")) > MAX_PASSWORD_BYTES:
        raise EcoLearnError(
            f"Password must be at most {MAX_PASSWORD_BYTES} bytes "
            "(about 72 characters; emoji and accents count for more than one)."
        )


def is_hashable(password: str) -> bool:
    """Return True if bcrypt could hash this input at all (length-wise).

    Used on the *login* path, where we must not leak which half of the
    credentials was wrong: an over-long password is simply "incorrect", handled
    with the same generic message as a wrong one.
    """
    return (
        isinstance(password, str)
        and bool(password)
        and len(password.encode("utf-8")) <= MAX_PASSWORD_BYTES
    )


def hash_password(password: str) -> str:
    """Validate then hash a password, returning the hash as a str for SQLite.

    The returned string carries its own salt and cost factor (bcrypt's
    `$2b$12$...` format), so nothing else needs storing alongside it.

    Raises:
        EcoLearnError: if the password fails `validate_password`.
    """
    validate_password(password)
    digest = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return digest.decode("utf-8")


def verify_password(password: str, password_hash: str | None) -> bool:
    """Return True if `password` matches `password_hash`. Never raises.

    Every failure mode collapses to False: no hash stored (a legacy
    name-only student), an over-long password, a corrupt or non-bcrypt hash.
    Callers get a plain boolean and turn it into one generic auth error.
    """
    if not password_hash or not is_hashable(password):
        return False
    try:
        return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))
    except (ValueError, TypeError):
        # Malformed/truncated hash in the DB, or a non-UTF-8-encodable input.
        return False


def dummy_verify() -> None:
    """Burn one bcrypt verification against a throwaway hash.

    Called on the unknown-email login path so that "no such account" and "wrong
    password" take ~the same wall-clock time. Without it, a fast rejection is a
    side channel that tells an attacker which emails are registered.
    """
    bcrypt.checkpw(b"ecolearn-dummy-password-probe", _DUMMY_HASH.encode("utf-8"))
