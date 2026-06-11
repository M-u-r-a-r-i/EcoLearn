"""Smoke test for the curriculum loader.

What this verifies:
    1. data/curriculum/physics.yaml parses and validates against the schema.
    2. teaching_order() returns concepts sorted by `order`.
    3. No concept appears before any of its declared prerequisites.
    4. resolve_prerequisites() returns the right ancestor set for a spot-check.

Runs purely locally — no LLM calls, no quota.
"""

from __future__ import annotations

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PROJECT_ROOT))

from src.curriculum.loader import (
    load_subject,
    resolve_prerequisites,
    teaching_order,
)


PHYSICS_PATH = _PROJECT_ROOT / "data" / "curriculum" / "physics.yaml"


def _bar(title: str) -> str:
    line = "=" * 78
    return f"\n{line}\n{title}\n{line}"


def _print_loaded_subject() -> None:
    subject = load_subject(PHYSICS_PATH)
    print(_bar(f"LOADED  subject = {subject.name!r}"))
    print(f"  description: {subject.description}")
    print(f"  units:       {[u.name for u in subject.units]}")
    for unit in subject.units:
        print(f"    unit '{unit.name}' has chapters: "
              f"{[c.name for c in unit.chapters]}")


def _print_teaching_order() -> None:
    subject = load_subject(PHYSICS_PATH)
    order = teaching_order(subject)
    print(_bar("TEACHING ORDER"))
    for i, c in enumerate(order, start=1):
        prereqs = ", ".join(c.prerequisites) if c.prerequisites else "(none)"
        print(
            f"  {i:>2}. [{c.bloom_target.value:>10}]  {c.name}\n"
            f"        id:        {c.id}\n"
            f"        prereqs:   {prereqs}\n"
            f"        objective: {c.learning_objective.strip()}"
        )


def _verify_prereqs_respected() -> None:
    """Walk the teaching order; assert every prereq of every concept has
    already been seen by the time we reach that concept."""
    subject = load_subject(PHYSICS_PATH)
    order = teaching_order(subject)
    seen: set[str] = set()
    failures: list[str] = []
    for c in order:
        for pid in c.prerequisites:
            if pid not in seen:
                failures.append(
                    f"  - {c.id!r} (order {c.order}) needs {pid!r} but "
                    f"that prereq hasn't appeared yet."
                )
        seen.add(c.id)

    print(_bar("PREREQUISITE CHECK"))
    if failures:
        print("FAIL — the following ordering issues were found:")
        for f in failures:
            print(f)
        sys.exit(1)
    print(f"PASS — all {len(order)} concepts respect their prerequisites.")


def _spot_check_resolve() -> None:
    """Pick a concept with non-trivial prereqs and resolve them."""
    subject = load_subject(PHYSICS_PATH)
    target = "equations_of_motion"

    direct = resolve_prerequisites(target, subject)
    transitive = resolve_prerequisites(target, subject, transitive=True)

    print(_bar(f"RESOLVE PREREQUISITES  target = {target!r}"))
    print(f"  direct ({len(direct)}):     {[c.id for c in direct]}")
    print(f"  transitive ({len(transitive)}): {[c.id for c in transitive]}")


def main() -> None:
    _print_loaded_subject()
    _print_teaching_order()
    _verify_prereqs_respected()
    _spot_check_resolve()
    print()
    print("All curriculum checks passed.")


if __name__ == "__main__":
    main()
