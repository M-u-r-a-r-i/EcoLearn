"""Chapter coverage: students never walk into a chapter or concept with no lesson.

Lessons are written interest by interest, so at any moment some chapters have
no lessons for a student's interest, and some are part-written. Proves:

  1. list_chapters(interest) counts the lessons each chapter has ready, using
     the same rule as serving (an "explain" lesson); an unknown interest is
     refused (it would otherwise be a glob pattern).
  2. The roadmap marks each concept has_lesson for the student's interest.
  3. "Continue learning" skips a concept whose lesson isn't written yet and
     recommends the next one that is.
  4. A chapter with nothing written answers lesson_missing with a message meant
     for a student (no "lesson factory").
  5. GET /api/chapters?interest= exposes the counts.

Uses a temporary lessons directory: one real chapter for one interest, with
its first concept's lesson removed.

Run: venv\\Scripts\\python.exe tests\\test_chapter_coverage.py
"""

from __future__ import annotations

import os
import shutil
import sys
import tempfile
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(_ROOT / "apps"))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_coverage_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "coverage.db")
os.environ["ECOLEARN_LESSONS_DIR"] = str(_TMP / "lessons")
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from ecolearn import platform_api as api  # noqa: E402
from ecolearn.errors import EcoLearnError  # noqa: E402
from ecolearn.path import engine  # noqa: E402

CHAPTER = "motion_straight_line"
INTEREST = "cricket"
EMPTY_CHAPTER = "gravitation"  # a Class 11 chapter: students only open their own class's chapters

_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


def build_lessons() -> tuple[list[str], str]:
    """Copy CHAPTER's cricket explain lessons, minus the first concept's."""
    concepts = engine.concept_ids_by_chapter()[CHAPTER]
    src = _ROOT / "data" / "lessons" / "11" / CHAPTER
    for concept in concepts[1:]:
        target = _TMP / "lessons" / "11" / CHAPTER / concept
        target.mkdir(parents=True)
        shutil.copy(src / concept / f"{INTEREST}__explain.md", target)
    # A challenge-format file alone must NOT count as a servable lesson.
    stray = _TMP / "lessons" / "11" / CHAPTER / concepts[0]
    stray.mkdir(parents=True)
    (stray / f"{INTEREST}__challenge.md").write_text("not served", encoding="utf-8")
    return concepts, concepts[0]


def main() -> None:
    concepts, missing = build_lessons()
    student = api.register_student("Cov Kid", "cov.kid", "kid-password-1", INTEREST, "Class 11")
    sid = student["student_id"]

    print("\n[1] chapter counts")
    chapters = {c["id"]: c for c in api.list_chapters(INTEREST)}
    check(chapters[CHAPTER]["lessons_ready"] == len(concepts) - 1,
          f"{CHAPTER}: {len(concepts) - 1} of {len(concepts)} ready (a challenge file alone doesn't count)")
    check(chapters[EMPTY_CHAPTER]["lessons_ready"] == 0, f"{EMPTY_CHAPTER}: 0 ready")
    check("lessons_ready" not in api.list_chapters()[0], "no interest → no counts (old shape)")
    try:
        api.list_chapters("*")
        check(False, "a glob pattern as interest is refused")
    except EcoLearnError:
        check(True, "a glob pattern as interest is refused")

    print("\n[2] roadmap flags")
    roadmap = {r["concept_id"]: r for r in api.get_roadmap(sid, CHAPTER)}
    check(roadmap[missing]["has_lesson"] is False, f"{missing}: has_lesson False")
    check(all(roadmap[c]["has_lesson"] for c in concepts[1:]), "every other concept: has_lesson True")

    print("\n[3] continue learning skips the unwritten concept")
    nxt = api.get_next_lesson(sid, CHAPTER)
    check(nxt["status"] == "new" and nxt["concept_id"] == concepts[1] and nxt["lesson"] is not None,
          f"recommends {concepts[1]} instead of {missing}")
    explicit = api.get_next_lesson(sid, CHAPTER, concept_id=missing)
    check(explicit["status"] == "lesson_missing", "opening the unwritten concept directly → lesson_missing")

    print("\n[4] an empty chapter speaks to the student")
    empty = api.get_next_lesson(sid, EMPTY_CHAPTER)
    check(empty["status"] == "lesson_missing" and empty["lesson"] is None, "lesson_missing")
    check("factory" not in empty["reason"] and "still being written" in empty["reason"],
          f"student-facing reason: {empty['reason']!r}")

    print("\n[5] HTTP")
    client = TestClient(app)
    r = client.get("/api/chapters", params={"interest": INTEREST})
    by_id = {c["id"]: c for c in r.json()}
    check(r.status_code == 200 and by_id[EMPTY_CHAPTER]["lessons_ready"] == 0,
          "GET /api/chapters?interest= → counts")
    check(client.get("/api/chapters", params={"interest": "knitting"}).status_code == 400,
          "unknown interest → 400")
    check(client.get("/api/chapters").status_code == 200, "no interest still works (public)")

    print(f"\nAll {_checks} chapter-coverage checks passed.")


if __name__ == "__main__":
    main()
