"""Curriculum schema — Pydantic models for the learning hierarchy.

Hierarchy: Subject -> Unit -> Chapter -> Concept.

A Concept is the atomic teachable thing. It declares what the student should
be able to do (learning_objective), at what cognitive level (bloom_target),
and what they need to know first (prerequisites). The `order` field records
the author's intended teaching sequence within a chapter.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class BloomLevel(str, Enum):
    """Bloom's taxonomy levels, lowercased for clean YAML authoring.

    We treat this as a target — "what kind of mastery should the student
    reach for this concept" — not as a ceiling on the explanation.
    """

    REMEMBER = "remember"
    UNDERSTAND = "understand"
    APPLY = "apply"
    ANALYZE = "analyze"
    EVALUATE = "evaluate"
    CREATE = "create"


class Concept(BaseModel):
    """An atomic learnable unit inside a chapter."""

    id: str = Field(..., description="Stable slug, unique within the subject.")
    name: str = Field(..., description="Student-facing display name.")
    chapter_id: str = Field(
        ...,
        description=(
            "Parent chapter id. Filled in by the loader from YAML nesting "
            "so authors don't have to repeat it on every concept."
        ),
    )
    prerequisites: list[str] = Field(
        default_factory=list,
        description=(
            "Concept ids the student must have learned first. May re"
            "ference "
            "concepts in the same or earlier chapters."
        ),
    )
    learning_objective: str = Field(
        ...,
        description=(
            "One sentence stating what the student can do after learning this "
            "concept — phrased as an observable action."
        ),
    )
    bloom_target: BloomLevel = Field(
        ...,
        description="The cognitive level this concept aims to develop.",
    )
    order: int = Field(
        ...,
        ge=1,
        description=(
            "Intended teaching order within the chapter. Concepts are sorted "
            "by this; the loader verifies it respects prerequisites."
        ),
    )


class Chapter(BaseModel):
    """A coherent group of concepts within a unit."""

    id: str
    name: str
    unit_id: str
    concepts: list[Concept] = Field(default_factory=list)


class Unit(BaseModel):
    """A high-level grouping of chapters within a subject."""

    id: str
    name: str
    subject_id: str
    chapters: list[Chapter] = Field(default_factory=list)


class Subject(BaseModel):
    """The top-level container for a discipline."""

    id: str
    name: str
    description: str | None = None
    units: list[Unit] = Field(default_factory=list)
