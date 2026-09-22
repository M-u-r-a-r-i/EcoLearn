"""What content we have agreed to write, as data.

`data/content_scope.yaml` is the user's 2026-09-22 decision: which chapters and
which interests get lessons before the finals, in which phases. Until now only
`scripts/batch_status.py` read it. The boundary needs it too, so the signup page
can offer exactly the interests we are writing for — no more (an interest with
no lessons anywhere is a dead end) and no fewer (cricket has the most lessons
and was hidden, because the registry still called it a draft).

Kept deliberately tiny: read the file, hand back plain data.
"""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

_DEFAULT = Path(__file__).resolve().parents[2] / "data" / "content_scope.yaml"


def scope_path() -> Path:
    """The scope file, overridable with ECOLEARN_CONTENT_SCOPE (tests)."""
    return Path(os.environ.get("ECOLEARN_CONTENT_SCOPE", _DEFAULT))


@lru_cache(maxsize=4)
def _load(path: str) -> dict[str, Any]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    return {
        "chapters": list(data.get("chapters") or []),
        "interests": list(data.get("interests") or []),
        "phases": list(data.get("phases") or []),
        "decided": data.get("decided"),
    }


def load_scope() -> dict[str, Any]:
    """{chapters: [id], interests: [id], phases: [...], decided: date}."""
    return _load(str(scope_path()))


def scope_chapter_ids() -> list[str]:
    return load_scope()["chapters"]


def scope_interest_ids() -> list[str]:
    return load_scope()["interests"]
