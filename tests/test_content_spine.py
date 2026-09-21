"""Content-spine test: the full Class 11 + 12 curriculum and the interest registry.

What this verifies:
    1. The full curriculum loads: 29 chapters, both grades, every concept stamped
       with its unit's grade, every chapter carrying a domain.
    2. The original 17 concept ids still exist in their original chapters, in
       their original relative order (renaming or moving them would orphan
       lesson files, progress rows and tests).
    3. The loader REJECTS bad curricula: a duplicate concept id, a duplicate
       chapter id, an unknown key (typo), a missing grade, and a concept placed
       before its prerequisite.
    4. The interest registry loads 10 valid interests with football and gaming
       active, and rejects duplicate ids, bad slugs and unknown domains.

Runs purely locally — no LLM calls, no database.
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

from pydantic import ValidationError  # noqa: E402

from src.curriculum.interests import active_interests, load_interests  # noqa: E402
from src.curriculum.loader import all_concepts, load_subject, teaching_order  # noqa: E402

PHYSICS = _ROOT / "data" / "curriculum" / "physics.yaml"

_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


def expect_rejected(yaml_text: str, label: str, loader=load_subject) -> None:
    """Write a fixture to a temp file and assert the loader refuses it."""
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False, encoding="utf-8") as f:
        f.write(yaml_text)
        path = f.name
    try:
        loader(path)
    except (ValueError, ValidationError) as exc:
        first_line = str(exc).splitlines()[0]
        check(True, f"{label} -> rejected ({first_line[:70]})")
        return
    finally:
        Path(path).unlink(missing_ok=True)
    raise AssertionError(f"FAIL: {label} -> was accepted but should be rejected")


# A minimal valid curriculum that fixtures below break in exactly one way.
_VALID = """
subject:
  id: physics
  name: Physics
  units:
    - id: u1
      name: Unit 1
      grade: 11
      chapters:
        - id: ch1
          name: Chapter 1
          domain: mechanics
          concepts:
            - id: a
              name: A
              prerequisites: []
              learning_objective: "Do A."
              bloom_target: understand
              order: 1010
            - id: b
              name: B
              prerequisites: [a]
              learning_objective: "Do B."
              bloom_target: apply
              order: 1020
"""


def test_full_curriculum() -> None:
    print("\n[1] full curriculum")
    subject = load_subject(PHYSICS)
    chapters = [ch for u in subject.units for ch in u.chapters]
    concepts = all_concepts(subject)

    check(len(chapters) == 29, f"29 chapters (got {len(chapters)})")
    check({u.grade for u in subject.units} == {11, 12}, "units cover grades 11 and 12")
    check(sum(1 for ch in chapters if ch.grade == 11) == 14, "14 chapters in Class 11")
    check(sum(1 for ch in chapters if ch.grade == 12) == 15,
          "15 chapters in Class 12 (14 + ISC-only Communication Systems)")
    comms = next(ch for ch in chapters if ch.id == "communication_systems")
    check(all([b.value for b in c.boards] == ["isc"] for c in comms.concepts),
          "Communication Systems is tagged ISC-only")
    check(len(concepts) >= 200, f"at least 200 concepts (got {len(concepts)})")

    grade_ok = all(
        ch.grade == u.grade and all(c.grade == u.grade for c in ch.concepts)
        for u in subject.units for ch in u.chapters
    )
    check(grade_ok, "every chapter and concept carries its unit's grade")
    check(all(ch.concepts for ch in chapters), "no empty chapters")
    check(all(ch.domain for ch in chapters), "every chapter has a domain")

    # Every Class 11 concept precedes every Class 12 concept in teaching order.
    grades_in_order = [c.grade for c in teaching_order(subject)]
    check(grades_in_order == sorted(grades_in_order), "Class 11 is taught before Class 12")

    # Board tags: most concepts are on both boards; ISC-only and enrichment
    # concepts must explain themselves in a syllabus_note.
    boards = {c.id: sorted(b.value for b in c.boards) for c in concepts}
    check(sum(1 for b in boards.values() if b == ["cbse", "isc"]) >= 200,
          "most concepts are on both boards")
    check(boards["transistor_amplifier"] == ["isc"], "an ISC-only concept is tagged isc")
    check(boards["eddy_currents"] == [], "enrichment concepts have no board")
    check(all(c.syllabus_note for c in concepts if boards[c.id] != ["cbse", "isc"]),
          "every non-default board tag has a syllabus_note explaining it")

    # Topics the CBSE 2025-26 syllabus specifies, added on 2026-09-21.
    ids = set(boards)
    for cid in ("measurement_uncertainty", "motion_graphs", "calculus_for_motion",
                "unit_vectors", "motion_plane_constant_acceleration",
                "vertical_circle_motion", "elastic_potential_energy",
                "magnetic_field_oersted"):
        check(cid in ids and boards[cid] == ["cbse", "isc"], f"CBSE topic present: {cid}")
    ac = next(ch for ch in chapters if ch.id == "alternating_current")
    check("ac_generator" in [c.id for c in ac.concepts],
          "AC generator sits in Alternating Current, as CBSE 2025-26 lists it")


def test_legacy_ids_preserved() -> None:
    print("\n[2] original 17 concept ids preserved")
    ch1 = ["position", "distance", "displacement", "speed", "velocity",
           "average_vs_instantaneous", "acceleration", "equations_of_motion",
           "relative_velocity_1d"]
    ch2 = ["scalars_and_vectors", "vector_addition", "vector_components",
           "relative_velocity_2d", "projectile_motion", "projectile_trajectory",
           "uniform_circular_motion", "centripetal_acceleration"]
    subject = load_subject(PHYSICS)
    order = teaching_order(subject)
    for chapter_id, expected in (("motion_straight_line", ch1), ("motion_plane", ch2)):
        actual = [c.id for c in order if c.chapter_id == chapter_id]
        # New syllabus concepts may sit between them; the originals must all
        # still be here, in their original relative order.
        kept = [cid for cid in actual if cid in expected]
        check(kept == expected, f"{chapter_id}: all original ids present, same relative order")
    kin = next(u for u in subject.units if u.id == "kinematics")
    check([ch.id for ch in kin.chapters] == ["motion_straight_line", "motion_plane"],
          "unit 'kinematics' still holds both original chapters")


def test_bad_curricula_rejected() -> None:
    print("\n[3] bad curricula are rejected")
    # Sanity: the base fixture itself is valid, so each rejection below is
    # caused by exactly the one thing that fixture breaks.
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False, encoding="utf-8") as f:
        f.write(_VALID)
    try:
        check(len(all_concepts(load_subject(f.name))) == 2, "base fixture loads")
    finally:
        Path(f.name).unlink(missing_ok=True)

    dup_concept = _VALID.replace("            - id: b\n              name: B",
                                 "            - id: a\n              name: B")
    expect_rejected(dup_concept, "duplicate concept id")

    dup_chapter = _VALID + """
        - id: ch1
          name: Chapter 1 again
          domain: mechanics
          concepts: []
"""
    expect_rejected(dup_chapter, "duplicate chapter id")

    typo = _VALID.replace("prerequisites: [a]", "prerequisite: [a]")
    expect_rejected(typo, "unknown key 'prerequisite' (typo)")

    no_grade = _VALID.replace("      grade: 11\n", "")
    expect_rejected(no_grade, "unit without a grade")

    bad_order = _VALID.replace("order: 1020", "order: 1005")
    expect_rejected(bad_order, "concept ordered before its prerequisite")

    bad_domain = _VALID.replace("domain: mechanics", "domain: alchemy")
    expect_rejected(bad_domain, "unknown chapter domain")

    bad_board = _VALID.replace("              order: 1020\n",
                               "              order: 1020\n              boards: [icse]\n")
    expect_rejected(bad_board, "unknown exam board")


def test_interest_registry() -> None:
    print("\n[4] interest registry")
    interests = load_interests()
    ids = [i.id for i in interests]
    check(len(interests) == 10, f"10 interests (got {len(interests)})")
    check("football" in ids and "gaming" in ids, "football and gaming kept (never renamed)")
    check({i.id for i in active_interests(interests)} == {"football", "gaming"},
          "only football and gaming are active until their lessons exist")

    covered = {d.value for i in interests for d in i.strong_domains}
    check(covered >= {"mechanics", "thermal", "waves", "electricity",
                      "magnetism", "optics", "modern"},
          "every physics domain has at least one natural interest")

    entry = """
  - id: {id}
    label: X
    emoji: "x"
    description: x
    strong_domains: [{domain}]
    status: draft
"""
    two = "interests:" + entry.format(id="chess", domain="mechanics") * 2
    expect_rejected(two, "duplicate interest id", loader=load_interests)
    expect_rejected("interests:" + entry.format(id="Chess", domain="mechanics"),
                    "uppercase interest slug", loader=load_interests)
    expect_rejected("interests:" + entry.format(id="board__games", domain="mechanics"),
                    "double underscore in interest slug", loader=load_interests)
    expect_rejected("interests:" + entry.format(id="chess", domain="strategy"),
                    "unknown domain", loader=load_interests)


def main() -> None:
    test_full_curriculum()
    test_legacy_ids_preserved()
    test_bad_curricula_rejected()
    test_interest_registry()
    print(f"\nALL {_checks} CHECKS PASSED")


if __name__ == "__main__":
    main()
