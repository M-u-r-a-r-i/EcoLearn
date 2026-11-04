"""Scale test: a second chapter routes correctly with NO code changes.

Proves the architectural claims for 'Motion in a Plane' purely through the
platform API + path engine (no LLM):
  - the curriculum loads (global ordering + cross-chapter prereqs validate);
  - get_roadmap surfaces the new chapter's concepts;
  - NOTHING IS LOCKED (user decision, 2026-09-21): a Chapter-2 concept is
    available even when its Chapter-1 prerequisites aren't cleared, and those
    prerequisites are reported as "brush up first" hints instead;
  - the hints disappear as the prerequisites are cleared;
  - next_concept routes through the new chapter in teaching order.
"""

from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_TMP_DB = os.path.join(tempfile.gettempdir(), "ecolearn_scale.db")
if os.path.exists(_TMP_DB):
    os.remove(_TMP_DB)
os.environ["ECOLEARN_PROGRESS_DB"] = _TMP_DB

from src import platform_api as api  # noqa: E402
from src.progress import store  # noqa: E402

CH2 = "motion_plane"


def main() -> None:
    sid = api.create_or_load_student("Scale Tester", "football", "Class 11")["student_id"]

    # 1. The chapter exists: the original 8 concepts plus the 2 added from the
    #    CBSE 2025-26 syllabus (unit vectors, constant acceleration in a plane).
    roadmap = api.get_roadmap(sid, CH2)
    names = [r["concept_id"] for r in roadmap]
    print(f"[chapter] motion_plane has {len(roadmap)} concepts: {names}")
    assert len(roadmap) == 10
    assert "projectile_motion" in names and "scalars_and_vectors" in names

    # 2. Nothing is locked: with nothing done, every concept is available —
    #    but the Chapter-1 prerequisites still show up as hints.
    by_id = {r["concept_id"]: r for r in roadmap}
    assert all(r["status"] == "available" for r in roadmap), "nothing may be locked"
    sv = by_id["scalars_and_vectors"]
    print(f"[hint]   scalars_and_vectors status={sv['status']} "
          f"brush-up={sv['missing_prerequisites']}")
    assert set(sv["missing_prerequisites"]) == {"distance", "displacement"}, (
        "entry concept must cite its Chapter-1 prerequisites as hints"
    )
    pm = by_id["projectile_motion"]
    assert "equations_of_motion" in pm["missing_prerequisites"], (
        "projectile_motion must cite its cross-chapter prereq equations_of_motion"
    )

    # The engine recommends the chapter's first concept straight away, with the
    # brush-up suggestion in its reason rather than a "blocked" status.
    nxt = api.get_next_lesson(sid, CH2)
    print(f"[route]  fresh student, next in motion_plane -> "
          f"{nxt['concept_id']} ({nxt['status']})")
    assert nxt["concept_id"] == "scalars_and_vectors"
    assert nxt["status"] in ("new", "lesson_missing"), nxt["status"]
    assert "brush-up" in nxt["reason"] or nxt["status"] == "lesson_missing"

    # 3. Clear the Chapter-1 prerequisites → the hint disappears.
    store.update_progress(sid, "distance", score=3)
    store.update_progress(sid, "displacement", score=3)
    by_id = {r["concept_id"]: r for r in api.get_roadmap(sid, CH2)}
    print(f"[clear]  after clearing distance+displacement, scalars_and_vectors "
          f"brush-up={by_id['scalars_and_vectors']['missing_prerequisites']}")
    assert by_id["scalars_and_vectors"]["missing_prerequisites"] == []

    # 4. Deeper cross-chapter prerequisites: clear the Ch2 vector chain + the Ch1
    #    prerequisite equations_of_motion → projectile_motion has no hints left.
    for cid in ("scalars_and_vectors", "vector_addition", "vector_components"):
        store.update_progress(sid, cid, score=3)
    for cid in ("position", "speed", "velocity", "acceleration", "equations_of_motion"):
        store.update_progress(sid, cid, score=3)
    pm = next(r for r in api.get_roadmap(sid, CH2) if r["concept_id"] == "projectile_motion")
    print(f"[deep]   projectile_motion status={pm['status']} "
          f"brush-up={pm['missing_prerequisites']}")
    assert pm["status"] == "available"
    assert pm["missing_prerequisites"] == [], (
        "no hints once vector_components (Ch2) and equations_of_motion (Ch1) are cleared"
    )

    # 5. Routing follows teaching order: with the vector chain cleared, the next
    #    concept is the first uncleared one in the chapter.
    nxt = api.get_next_lesson(sid, CH2)
    print(f"[route]  next in motion_plane -> {nxt['concept_id']} ({nxt['status']})")
    assert nxt["concept_id"] == "unit_vectors", nxt["concept_id"]

    print("\nPASS — Chapter 2 routes in teaching order with cross-chapter "
          "prerequisites as hints, nothing locked, no code changes.")


if __name__ == "__main__":
    main()
