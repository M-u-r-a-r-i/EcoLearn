"""Scale test: a second chapter routes correctly with NO code changes.

Proves the architectural claims for 'Motion in a Plane' purely through the
platform API + path engine (no LLM):
  - the curriculum loads (global ordering + cross-chapter prereqs validate);
  - get_roadmap surfaces the new chapter's concepts;
  - cross-chapter prerequisites gate correctly (a Chapter-2 concept stays
    locked until its Chapter-1 prerequisites are cleared);
  - next_concept routes through the new chapter respecting those prereqs.
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

    # 1. The new chapter exists and has its 8 concepts.
    roadmap = api.get_roadmap(sid, CH2)
    names = [r["concept_id"] for r in roadmap]
    print(f"[chapter] motion_plane has {len(roadmap)} concepts: {names}")
    assert len(roadmap) == 8
    assert "projectile_motion" in names and "scalars_and_vectors" in names

    # 2. Cross-chapter gating: with nothing done, the entry concept is locked
    #    on CHAPTER-1 prerequisites (distance, displacement).
    by_id = {r["concept_id"]: r for r in roadmap}
    sv = by_id["scalars_and_vectors"]
    print(f"[cross]  scalars_and_vectors status={sv['status']} "
          f"missing={sv['missing_prerequisites']}")
    assert sv["status"] == "locked"
    assert set(sv["missing_prerequisites"]) == {"distance", "displacement"}, (
        "entry concept must be locked on its Chapter-1 prerequisites"
    )

    # projectile_motion depends on equations_of_motion (Ch1) + vector_components (Ch2).
    pm = by_id["projectile_motion"]
    assert "equations_of_motion" in pm["missing_prerequisites"], (
        "projectile_motion must cite its cross-chapter prereq equations_of_motion"
    )

    # 3. Clear the Chapter-1 prerequisites → the Chapter-2 entry unlocks.
    store.update_progress(sid, "distance", score=3)
    store.update_progress(sid, "displacement", score=3)
    roadmap = api.get_roadmap(sid, CH2)
    by_id = {r["concept_id"]: r for r in roadmap}
    print(f"[unlock] after clearing distance+displacement, "
          f"scalars_and_vectors status={by_id['scalars_and_vectors']['status']}")
    assert by_id["scalars_and_vectors"]["status"] == "available"

    nxt = api.get_next_lesson(sid, CH2)
    print(f"[route]  next in motion_plane -> {nxt['concept_id']} ({nxt['status']})")
    assert nxt["concept_id"] == "scalars_and_vectors"

    # 4. Deeper cross-chapter unlock: clear the Ch2 vector chain + the Ch1
    #    prereq equations_of_motion → projectile_motion unlocks.
    for cid in ("scalars_and_vectors", "vector_addition", "vector_components"):
        store.update_progress(sid, cid, score=3)
    # equations_of_motion needs its own Ch1 chain; clear everything it needs.
    for cid in ("position", "speed", "velocity", "acceleration", "equations_of_motion"):
        store.update_progress(sid, cid, score=3)
    roadmap = api.get_roadmap(sid, CH2)
    pm = next(r for r in roadmap if r["concept_id"] == "projectile_motion")
    print(f"[deep]   projectile_motion status={pm['status']} "
          f"missing={pm['missing_prerequisites']}")
    assert pm["status"] == "available", (
        "projectile_motion should unlock once vector_components (Ch2) and "
        "equations_of_motion (Ch1) are cleared"
    )

    print("\nPASS — Chapter 2 routes with correct cross-chapter prerequisites, "
          "no code changes.")


if __name__ == "__main__":
    main()
