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
  ECOLEARN_JWT_SECRET  signing secret. Unset in development → a fixed dev secret
                       and a warning. Unset or short in production → the app
                       refuses to start.
  ECOLEARN_ENV         "production" turns on the strict checks and Secure cookies.
"""

from __future__ import annotations

import os
import warnings
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import HTTPException, Request, Response, status

from src import platform_api as api
from src.errors import AuthError, NotFoundError

COOKIE_NAME = "ecolearn_session"
TOKEN_TTL = timedelta(days=7)
ALGORITHM = "HS256"
MIN_SECRET_CHARS = 32
_DEV_SECRET = "ecolearn-development-only-secret-do-not-use-in-production"


def _is_production() -> bool:
    return os.getenv("ECOLEARN_ENV", "development").strip().lower() == "production"


def _load_secret() -> str:
    secret = os.getenv("ECOLEARN_JWT_SECRET", "").strip()
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
            "ECOLEARN_JWT_SECRET is not set — using the development secret. "
            "Anyone with the source code could forge sessions; set it before deploying.",
            stacklevel=2,
        )
        return _DEV_SECRET
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

def get_current_student_id(request: Request) -> str:
    """FastAPI dependency: the logged-in student's id, or a 401.

    Reads the session cookie (or an `Authorization: Bearer` header, handy for
    curl and tests), verifies it, and confirms the account still exists — a
    valid token for a deleted account must not keep working.
    """
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
