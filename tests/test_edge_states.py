"""Edge/empty-state checks through the platform API (no LLM calls).

Confirms get_next_lesson reports the right status at each boundary:
  - fresh student         -> "new" on the root concept (empty roadmap)
  - all concepts mastered -> "done" (end of chapter)
  - a stale mastered one  -> "review" (spaced repetition), so the UI can show
                             the "Quick review before we move on" banner
"""

from __future__ import annotations

import os
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_TMP_DB = os.path.join(tempfile.gettempdir(), "ecolearn_edge_states.db")
if os.path.exists(_TMP_DB):
    os.remove(_TMP_DB)
os.environ["ECOLEARN_PROGRESS_DB"] = _TMP_DB

from src import platform_api as api  # noqa: E402
from src.progress import store  # noqa: E402

CHAPTER = "motion_straight_line"


def main() -> None:
    profile = api.create_or_load_student("Edge Tester", "gaming", "Class 11")
    sid = profile["student_id"]

    # 1. EMPTY: nothing mastered -> first lesson is the root concept.
    nxt = api.get_next_lesson(sid, CHAPTER)
    print(f"[empty]  status={nxt['status']} concept={nxt['concept_id']}")
    assert nxt["status"] == "new" and nxt["concept_id"] == "position"

    roadmap = api.get_roadmap(sid, CHAPTER)
    assert all(r["status"] != "mastered" for r in roadmap), "nothing mastered yet"
    print(f"[empty]  roadmap mastered count = "
          f"{sum(1 for r in roadmap if r['status'] == 'mastered')}/{len(roadmap)}")

    # 2. END OF CHAPTER: master every concept -> "done".
    for r in roadmap:
        store.update_progress(sid, r["concept_id"], score=3)
    nxt = api.get_next_lesson(sid, CHAPTER)
    print(f"[done]   status={nxt['status']} concept={nxt['concept_id']}")
    assert nxt["status"] == "done" and nxt["concept_id"] is None
    roadmap = api.get_roadmap(sid, CHAPTER)
    assert all(r["status"] == "mastered" for r in roadmap), "all mastered now"
    print(f"[done]   roadmap mastered count = {len(roadmap)}/{len(roadmap)}")

    # 3. REVIEW: backdate one concept so spaced repetition surfaces it.
    stale = datetime.now(tz=timezone.utc) - timedelta(days=14)
    store.mark_reviewed(sid, "speed", seen_at=stale)
    nxt = api.get_next_lesson(sid, CHAPTER)
    print(f"[review] status={nxt['status']} concept={nxt['concept_id']}")
    print(f"[review] reason: {nxt['reason']}")
    assert nxt["status"] == "review" and nxt["concept_id"] == "speed"
    # A review still serves the lesson to revisit.
    assert nxt["lesson"] is not None, "review should carry the lesson to revisit"

    print("\nAll edge states correct (empty / done / review).")


def partial_advance() -> None:
    """A 2/3 pass clears a concept: the student can move on, or re-practise it."""
    sid = api.create_or_load_student("Partial Tester", "football", "Class 11")["student_id"]
    store.update_progress(sid, "position", score=2)  # partial pass

    nxt = api.get_next_lesson(sid, CHAPTER)
    print(f"[partial] after 2/3 on position -> status={nxt['status']} "
          f"concept={nxt['concept_id']}")
    assert nxt["concept_id"] in {"distance", "displacement"}, (
        "a 2/3 pass should clear position and let the engine advance"
    )

    status = {r["concept_id"]: r["status"] for r in api.get_roadmap(sid, CHAPTER)}
    assert status["position"] == "available", (
        "a 2/3 concept is 'available' (revisit to master), not 'mastered'"
    )
    assert status["distance"] == "available", "distance unlocks after position cleared"

    # The re-practise override re-serves the same concept on demand.
    again = api.get_next_lesson(sid, CHAPTER, concept_id="position")
    assert again["concept_id"] == "position" and again["lesson"] is not None

    print("[partial] PASS — 2/3 advances, downstream unlocks, re-practise works.")


if __name__ == "__main__":
    main()
    print()
    partial_advance()
