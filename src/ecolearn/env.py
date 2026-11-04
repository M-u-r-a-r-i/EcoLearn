"""Configuration from the environment, then the project's .env, plus local secrets that never enter git.

`get` is the one way the package reads a setting:

  * A variable that is SET in the environment wins even when it is empty: `LLM_MODEL=` means "off",
    which is how tests and the load test switch the AI off without editing .env (the load test once
    found an empty value falling through to .env and calling a real provider).
  * Otherwise the project's .env, parsed once per version (ecolearn/file_cache.py), so a value added
    while the server runs is still picked up without a restart.

`local_secret` is for development secrets that must stay stable across restarts but must never be
written into the code: before 2026-11-04 the JWT signing secret and the demo password were string
literals in the repo, so anyone who read GitHub had them (GitGuardian flagged both).
"""

from __future__ import annotations

import os
import secrets
from pathlib import Path

from ecolearn.paths import PROJECT_ROOT


def get(name: str, default: str | None = None) -> str | None:
    """The environment first, then the project's .env; `default` when neither has a value."""
    if name in os.environ:
        return os.environ[name] or default
    path = PROJECT_ROOT / ".env"
    try:
        from dotenv import dotenv_values

        from ecolearn.file_cache import cached_parse
        value = cached_parse(path, lambda p: dict(dotenv_values(p)), "dotenv").get(name)
    except Exception:  # noqa: BLE001 — no .env, or unreadable: use the default
        value = None
    return value or default


def local_secret(relative_path: str, nbytes: int = 48) -> str:
    """A random secret kept in a gitignored file under the project, created on first use.

    Stable across restarts (a dev server with --reload would otherwise log everyone out on every
    code edit). If the file can't be written, a secret for this process only is returned.
    """
    path = PROJECT_ROOT / relative_path
    try:
        existing = path.read_text(encoding="utf-8").strip()
        if existing:
            return existing
    except FileNotFoundError:
        pass
    value = secrets.token_urlsafe(nbytes)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "x", encoding="utf-8") as f:  # "x": two processes starting at once can't both write
            f.write(value + "\n")
    except FileExistsError:
        return path.read_text(encoding="utf-8").strip() or value
    except OSError:
        return value
    return value


def secret_file(relative_path: str) -> Path:
    """Where `local_secret` keeps a secret (for messages that tell a person where to look)."""
    return PROJECT_ROOT / relative_path
