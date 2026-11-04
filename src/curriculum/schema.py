"""Curriculum schema — Pydantic models for the learning hierarchy.

Hierarchy: Subject -> Unit -> Chapter -> Concept.

A Concept is the atomic teachable thing. It declares what the student should
be able to do (learning_objective), at what cognitive level (bloom_target),
and what they need to know first (prerequisites). The `order` field records
the author's intended teaching sequence — GLOBAL across the whole subject,
not per chapter (see `Concept.order`).

Every model forbids unknown fields. At ~250 hand-authored concepts, a typo such
as `prerequisite:` (missing the "s") would otherwise be silently dropped and
the concept would load with no prerequisites at all.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


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


class Domain(str, Enum):
    """The broad area of physics a chapter belongs to.

    Used to match interests to chapters: each interest in
    `data/interests.yaml` lists the domains it grounds analogies in naturally.
    """

    GENERAL = "general"          # measurement, units, dimensions
    MECHANICS = "mechanics"
    THERMAL = "thermal"
    WAVES = "waves"              # oscillations and mechanical waves
    ELECTRICITY = "electricity"
    MAGNETISM = "magnetism"
    OPTICS = "optics"            # light and electromagnetic radiation
    MODERN = "modern"            # quantum, atomic, nuclear, semiconductors


class Board(str, Enum):
    """Exam boards whose syllabus includes a concept."""

    CBSE = "cbse"
    ISC = "isc"


class _Strict(BaseModel):
    """Base for curriculum models: reject unknown YAML keys (catches typos)."""

    model_config = ConfigDict(extra="forbid")


class Concept(_Strict):
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
            "Teaching order, GLOBAL across the whole subject (not per "
            "chapter). Convention: chapter_seq * 1000 + position * 10, e.g. "
            "2030 = chapter 2, third concept — the gaps leave room to insert "
            "concepts later without renumbering. The loader verifies the "
            "order respects prerequisites."
        ),
    )
    grade: int = Field(
        ...,
        description="Class (11 or 12). Stamped down from the parent Unit by the loader.",
    )
    boards: list[Board] = Field(
        default_factory=lambda: [Board.CBSE, Board.ISC],
        description=(
            "Exam boards whose syllabus includes this concept. Defaults to "
            "both. An empty list marks enrichment beyond both syllabuses "
            "(kept deliberately — say why in `syllabus_note`)."
        ),
    )
    syllabus_note: str | None = Field(
        default=None,
        description="Optional human note about the concept's syllabus status.",
    )


class Chapter(_Strict):
    """A coherent group of concepts within a unit."""

    id: str
    name: str
    unit_id: str
    grade: int = Field(..., description="Stamped down from the parent Unit by the loader.")
    domain: Domain = Field(..., description="Broad physics area, used to match interests.")
    concepts: list[Concept] = Field(default_factory=list)


class Unit(_Strict):
    """A high-level grouping of chapters within a subject.

    CBSE units never straddle classes, so `grade` lives here and the loader
    copies it onto every chapter and concept.
    """

    id: str
    name: str
    subject_id: str
    grade: int = Field(..., ge=11, le=12, description="Class 11 or 12.")
    chapters: list[Chapter] = Field(default_factory=list)


class Subject(_Strict):
    """The top-level container for a discipline."""

    id: str
    name: str
    description: str | None = None
    units: list[Unit] = Field(default_factory=list)
