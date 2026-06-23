"""FastAPI web layer for EcoLearn.

This package is a *thin* HTTP wrapper around `src/platform_api.py`. It contains
no business logic of its own — it only translates web requests into calls to the
existing platform functions and translates their return values back into JSON.
"""
