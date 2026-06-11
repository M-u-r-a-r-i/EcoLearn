"""Curriculum loader — read YAML, validate against the schema, expose queries.

The YAML file is the source of truth. This module is the single front door
through which the rest of the platform reads curriculum data, so callers
never touch raw YAML or worry about validation errors mid-flight.

Functions:
    load_subject(path)            -> Subject
    all_concepts(subject)         -> list[Concept]
    teaching_order(subject)       -> list[Concept]    # sorted by `order`
    resolve_prerequisites(...)    -> list[Concept]    # walk the prereq graph
    validate_ordering(subject)    -> None             # raises if order vs prereqs disagree
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from src.curriculum.schema import Chapter, Concept, Subject, Unit


# ---------------------------------------------------------------------------
# Loading and parent-id wiring
# ---------------------------------------------------------------------------

def _inject_parent_ids(raw_subject: dict[str, Any]) -> dict[str, Any]:
    """Walk the nested YAML dict and copy parent ids onto child nodes.

    YAML authoring stays clean (no repeating chapter_id on every concept);
    the loader then populates the fields the Pydantic schema requires.
    """
    subject_id = raw_subject["id"]
    for unit in raw_subject.get("units", []) or []:
        unit["subject_id"] = subject_id
        for chapter in unit.get("chapters", []) or []:
            chapter["unit_id"] = unit["id"]
            for concept in chapter.get("concepts", []) or []:
                concept["chapter_id"] = chapter["id"]
    return raw_subject


def load_subject(path: str | Path) -> Subject:
    """Read a curriculum YAML file and return a fully-validated Subject.

    Raises:
        FileNotFoundError: if `path` doesn't exist.
        yaml.YAMLError:    if the file isn't valid YAML.
        ValidationError:   if the data doesn't match the schema.
        ValueError:        if the teaching order violates prerequisites.
    """
    yaml_path = Path(path)
    raw = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or "subject" not in raw:
        raise ValueError(
            f"{yaml_path} must contain a top-level `subject:` mapping."
        )

    subject_dict = _inject_parent_ids(raw["subject"])
    subject = Subject.model_validate(subject_dict)
    # Fail fast if the author's declared `order` contradicts their declared
    # prereqs. Better to crash at load time than to surface confusion later.
    validate_ordering(subject)
    return subject


# ---------------------------------------------------------------------------
# Queries
# ---------------------------------------------------------------------------

def all_concepts(subject: Subject) -> list[Concept]:
    """Flatten every Concept under the Subject, preserving authored order."""
    out: list[Concept] = []
    for unit in subject.units:
        for chapter in unit.chapters:
            out.extend(chapter.concepts)
    return out


def teaching_order(subject: Subject) -> list[Concept]:
    """Return all concepts sorted by their declared `order` field.

    `order` is set per-concept by the author. Within a chapter the field is
    1, 2, 3, …; across chapters and units we sort by (unit_order_implicit,
    chapter_order_implicit, order) using the document's natural sequence.
    """
    flat = all_concepts(subject)
    # Sort by `order` but break ties by the original document position so
    # that two concepts at order=1 in different chapters keep the author's
    # intended sequence.
    return sorted(flat, key=lambda c: (c.order, c.id))


def _by_id(subject: Subject) -> dict[str, Concept]:
    """Build a flat id -> Concept index for fast prereq lookups."""
    return {c.id: c for c in all_concepts(subject)}


def resolve_prerequisites(
    concept_id: str,
    subject: Subject,
    *,
    transitive: bool = False,
) -> list[Concept]:
    """Return the Concept objects that `concept_id` depends on.

    Args:
        concept_id:  The id to resolve.
        subject:     The curriculum to look up against.
        transitive:  If False (default), return only the direct prerequisites.
                     If True, walk the prereq graph recursively and return
                     EVERY ancestor concept (deduplicated, depth-first order).

    Raises:
        KeyError: if `concept_id` or any prereq id isn't present in the subject.
    """
    index = _by_id(subject)
    if concept_id not in index:
        raise KeyError(f"Unknown concept id: {concept_id!r}")

    if not transitive:
        return [index[pid] for pid in index[concept_id].prerequisites]

    visited: set[str] = set()
    ordered: list[Concept] = []

    def _walk(cid: str) -> None:
        for pid in index[cid].prerequisites:
            if pid in visited:
                continue
            if pid not in index:
                raise KeyError(
                    f"Concept {cid!r} lists unknown prerequisite {pid!r}."
                )
            visited.add(pid)
            _walk(pid)
            ordered.append(index[pid])

    _walk(concept_id)
    return ordered


def validate_ordering(subject: Subject) -> None:
    """Raise ValueError if any concept appears before one of its prerequisites
    in the declared teaching order. Also catches unknown prerequisite ids and
    cycles in the prereq graph.
    """
    index = _by_id(subject)

    # 1. Every prereq id must reference a real concept in this subject.
    for c in index.values():
        for pid in c.prerequisites:
            if pid not in index:
                raise ValueError(
                    f"Concept {c.id!r} lists unknown prerequisite {pid!r}."
                )

    # 2. No concept may come earlier in the declared order than any of its
    #    prerequisites. Single pass through the sorted list, accumulating
    #    concept ids seen so far. This also catches prereq cycles: in any
    #    cycle, at least one node will be reached before its prereq is seen.
    seen_so_far: set[str] = set()
    for c in teaching_order(subject):
        for pid in c.prerequisites:
            if pid not in seen_so_far:
                raise ValueError(
                    f"Concept {c.id!r} (order {c.order}) appears before its "
                    f"prerequisite {pid!r}. Fix the `order` fields or the "
                    "prerequisite list. (This also fires if the prerequisite "
                    "graph contains a cycle.)"
                )
        seen_so_far.add(c.id)
