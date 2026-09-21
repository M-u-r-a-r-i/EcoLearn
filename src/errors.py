"""Domain error types for EcoLearn.

WHY THESE EXIST
---------------
Before this module, everything the backend rejected was a bare `ValueError`
("Unknown student_id ...", "No lesson for concept ..."). That is fine in-process
— Streamlit just shows the message — but the HTTP layer needs to tell those
cases apart: an unknown student is a **404**, a duplicate username is a **409**,
a bad password is a **401**, and a malformed input is a **400**. A single
exception type cannot carry that distinction.

THE INHERITANCE TRICK (important)
---------------------------------
`EcoLearnError` subclasses **ValueError** on purpose. Every existing caller —
`except ValueError` in the Streamlit pages, the FastAPI handlers, the tests —
keeps catching these new errors exactly as before. So we gain precision in the
HTTP layer without a single regression in the callers that don't care.

Mapping used by api/main.py:
    NotFoundError  -> 404
    ConflictError  -> 409
    AuthError      -> 401
    EcoLearnError  -> 400   (and any other plain ValueError)
"""

from __future__ import annotations


class EcoLearnError(ValueError):
    """Base class for every expected, caller-facing EcoLearn failure.

    Subclasses ValueError so existing `except ValueError` code paths continue
    to work unchanged.
    """


class NotFoundError(EcoLearnError):
    """A requested entity (student, concept, chapter, lesson) does not exist."""


class ConflictError(EcoLearnError):
    """The request collides with existing state (e.g. username already taken)."""


class AuthError(EcoLearnError):
    """Authentication failed — bad credentials, or no/invalid session."""
