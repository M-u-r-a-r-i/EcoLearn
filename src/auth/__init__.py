"""Authentication primitives (password hashing today, more later).

Deliberately dependency-light and framework-free: nothing here knows about
HTTP, FastAPI, or JWTs. Session/token concerns live in the HTTP layer
(`api/security.py`); this package only answers "is this the right password?".
"""
