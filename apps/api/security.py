"""Sessions for the HTTP layer: signed tokens in an httpOnly cookie.

How a session works:
  1. On register / login the API signs a small JSON Web Token (JWT) with a
     server-only secret: {"sub": student_id, "iat": issued-at, "exp": expiry}.
  2. It is sent back in a cookie the browser stores and returns automatically on
     every request to the API. The cookie is:
       - httpOnly  — page JavaScript (including any injected script) cannot read it;
       - SameSite=lax — the browser won't attach it to cross-site POSTs, which
         blocks the classic cross-site request forgery attack;
       - Secure in production — only ever sent over HTTPS.
  3. `get_current_student_id` (a FastAPI dependency) reads the cookie, checks
     the signature and expiry, and answers **401** if anything is wrong.

Why a signed token and not a session table: the signature proves the server
issued it, so there is nothing to look up or clean up — the one database read
per request is the check that the account still exists.

Configuration (read once, at import):
  ECOLEARN_JWT_SECRET  signing secret (environment or .env). Unset in development →
                       a random secret made once and kept in data/.dev_jwt_secret
                       (gitignored), so sessions survive a restart. Unset or short
                       in production → the app refuses to start.
  ECOLEARN_ENV         "production" turns on the strict checks and Secure cookies.

Before 2026-11-04 the development secret was a string in this file, so anyone who
read the public repo could sign a session for a server running without the variable.
"""

from __future__ import annotations

import warnings
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import HTTPException, Request, Response, status

from ecolearn import env
from ecolearn import platform_api as api
from ecolearn.errors import AuthError, NotFoundError

COOKIE_NAME = "ecolearn_session"
TOKEN_TTL = timedelta(days=7)
ALGORITHM = "HS256"
MIN_SECRET_CHARS = 32
_DEV_SECRET_FILE = "data/.dev_jwt_secret"


def _is_production() -> bool:
    return (env.get("ECOLEARN_ENV", "development") or "").strip().lower() == "production"


def _load_secret() -> str:
    secret = (env.get("ECOLEARN_JWT_SECRET") or "").strip()
    if _is_production():
        if len(secret) < MIN_SECRET_CHARS:
            raise RuntimeError(
                f"ECOLEARN_JWT_SECRET must be set to at least {MIN_SECRET_CHARS} characters "
                "in production. Generate one with: "
                'python -c "import secrets; print(secrets.token_urlsafe(32))"'
            )
        return secret
    if not secret:
        warnings.warn(
            "ECOLEARN_JWT_SECRET is not set — using a local development secret kept in "
            f"{_DEV_SECRET_FILE} (made on first run, gitignored). Set the variable before deploying.",
            stacklevel=2,
        )
        return env.local_secret(_DEV_SECRET_FILE)
    return secret


_SECRET = _load_secret()


# ---------------------------------------------------------------------------
# Tokens
# ---------------------------------------------------------------------------

def create_token(student_id: str, *, now: datetime | None = None) -> str:
    """Sign a session token for this student. `now` is injectable for tests."""
    issued = now or datetime.now(tz=timezone.utc)
    payload = {"sub": student_id, "iat": issued, "exp": issued + TOKEN_TTL}
    return jwt.encode(payload, _SECRET, algorithm=ALGORITHM)


def decode_token(token: str) -> str:
    """Return the student id in a valid token.

    Raises:
        AuthError: bad signature, expired, malformed, or missing claims. One
                   message for all of them — the caller only needs "log in again".
    """
    try:
        claims = jwt.decode(
            token,
            _SECRET,
            algorithms=[ALGORITHM],  # pinned: never let the token choose its algorithm
            options={"require": ["sub", "iat", "exp"]},
        )
    except jwt.PyJWTError as exc:
        raise AuthError("Your session has expired or is invalid. Please log in again.") from exc
    return str(claims["sub"])


# ---------------------------------------------------------------------------
# Cookies
# ---------------------------------------------------------------------------

def set_session_cookie(response: Response, student_id: str) -> None:
    response.set_cookie(
        key=COOKIE_NAME,
        value=create_token(student_id),
        max_age=int(TOKEN_TTL.total_seconds()),
        httponly=True,
        samesite="lax",
        secure=_is_production(),
        path="/",
    )


def clear_session_cookie(response: Response) -> None:
    response.delete_cookie(
        key=COOKIE_NAME,
        httponly=True,
        samesite="lax",
        secure=_is_production(),
        path="/",
    )


# ---------------------------------------------------------------------------
# The dependency
# ---------------------------------------------------------------------------

def _read_token(request: Request) -> str:
    """The session token from the cookie or a Bearer header, or a 401."""
    token = request.cookies.get(COOKIE_NAME)
    header = request.headers.get("authorization", "")
    if not token and header.lower().startswith("bearer "):
        token = header[7:].strip()
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You need to log in.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token


def get_current_teacher_id(request: Request) -> str:
    """FastAPI dependency: the logged-in teacher's id, or a 401.

    The mirror of `get_current_student_id`. A student's token fails here and a
    teacher's token fails there, because each looks the id up in its own table:
    the two roles can't reach each other's endpoints even by accident.
    """
    token = _read_token(request)
    try:
        teacher_id = decode_token(token)
        api.get_teacher_profile(teacher_id)
    except (AuthError, NotFoundError) as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please log in with a teacher account.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
    return teacher_id


def get_current_account(request: Request) -> tuple[str, dict]:
    """FastAPI dependency: ("student" | "teacher", profile) for whoever is logged in.

    Lets the web app ask one question on page load — who is this, and which
    kind of account — instead of probing two endpoints.
    """
    token = _read_token(request)
    try:
        account_id = decode_token(token)
    except AuthError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Your session has expired or is invalid. Please log in again.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
    for role, lookup in (("student", api.get_student_profile),
                         ("teacher", api.get_teacher_profile)):
        try:
            return role, lookup(account_id)
        except NotFoundError:
            continue
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Your session has expired or is invalid. Please log in again.",
        headers={"WWW-Authenticate": "Bearer"},
    )


def get_current_student_id(request: Request) -> str:
    """FastAPI dependency: the logged-in student's id, or a 401.

    Reads the session cookie (or an `Authorization: Bearer` header, handy for
    curl and tests), verifies it, and confirms the account still exists — a
    valid token for a deleted account must not keep working.
    """
    token = _read_token(request)
    try:
        student_id = decode_token(token)
        api.get_student_profile(student_id)
    except (AuthError, NotFoundError) as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Your session has expired or is invalid. Please log in again.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
    return student_id
