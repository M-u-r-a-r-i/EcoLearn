"""Interest registry — the second axis of the content matrix.

`data/interests.yaml` is the single source of truth for which interests exist.
Before this registry, interests were hardcoded separately in the web app,
Streamlit and the lesson factory, so an interest that existed in one place but
not another silently got "lesson missing" on every concept.

Functions:
    load_interests(path=None)          -> list[Interest]
    active_interests(interests)        -> list[Interest]
    interest_ids(interests)            -> set[str]
"""

from __future__ import annotations

from enum import Enum
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field

from src.curriculum.schema import Domain


_PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INTERESTS_PATH = _PROJECT_ROOT / "data" / "interests.yaml"


class InterestStatus(str, Enum):
    ACTIVE = "active"   # offered to students
    DRAFT = "draft"     # lessons still being written; not offered yet


class Interest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # Lowercase words joined by single underscores. Lesson files are named
    # `{concept_id}__{interest}...`, so a double underscore here would make
    # filenames ambiguous to split.
    id: str = Field(..., pattern=r"^[a-z]+(_[a-z]+)*$")
    label: str
    emoji: str
    description: str
    strong_domains: list[Domain] = Field(..., min_length=1)
    status: InterestStatus
    # General, checkable facts lesson authors may use (rules, standard sizes,
    # specifications) — so every batch draws on the same verified numbers
    # instead of each session recalling its own. Never statistics about real
    # people, teams or products.
    facts: list[str] = Field(default_factory=list)


def load_interests(path: str | Path | None = None) -> list[Interest]:
    """Read and validate the interest registry.

    Raises:
        ValueError:      if the file lacks an `interests:` list or ids repeat.
        ValidationError: if an entry is malformed (bad slug, unknown domain,
                         unknown key, missing field).
    """
    yaml_path = Path(path) if path else DEFAULT_INTERESTS_PATH
    raw = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("interests"), list):
        raise ValueError(f"{yaml_path} must contain a top-level `interests:` list.")

    interests = [Interest.model_validate(entry) for entry in raw["interests"]]

    seen: set[str] = set()
    for interest in interests:
        if interest.id in seen:
            raise ValueError(f"Duplicate interest id {interest.id!r} in {yaml_path}.")
        seen.add(interest.id)
    return interests


def active_interests(interests: list[Interest]) -> list[Interest]:
    """Only the interests students may choose right now."""
    return [i for i in interests if i.status is InterestStatus.ACTIVE]


def interest_ids(interests: list[Interest]) -> set[str]:
    return {i.id for i in interests}
