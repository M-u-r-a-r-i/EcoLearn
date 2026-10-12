r"""Write personal stories ahead of a demo or a lesson, so nobody waits for the AI.

    venv\Scripts\python.exe scripts\prewarm_stories.py --class "Class 11-B Physics" --concepts 3

For every student in the class, writes the stories for their next N concepts that
have a lesson in their interest (skipping any story that is already current), using
the same writer and critic as the live path. Run it with the same database the API
uses (ECOLEARN_PROGRESS_DB). Needs a working AI: check with scripts\ai_check.py.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import llm  # noqa: E402
from src import platform_api  # noqa: E402,F401  (importing it connects the AI usage log, so these calls are counted)
from src.content import lesson_service  # noqa: E402
from src.learner import personal_story as ps  # noqa: E402
from src.path import engine  # noqa: E402
from src.progress import store  # noqa: E402


def _classes(name: str) -> list[dict]:
    wanted = name.strip().lower()
    conn = store._connect()
    try:
        rows = conn.execute("SELECT class_id, name FROM classes").fetchall()
    finally:
        conn.close()
    ids = [r[0] for r in rows if wanted in (r[1].lower(), r[0].lower())]
    return [c for c in (store.get_class(i) for i in ids) if c]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--class", dest="cls", required=True, help="class name or id")
    ap.add_argument("--concepts", type=int, default=3, help="stories per student (default 3)")
    args = ap.parse_args()
    if not llm.is_configured():
        print("No AI configured (LLM_MODEL is empty): nothing to write.")
        return 1
    found = _classes(args.cls)
    if len(found) != 1:
        print(f"Expected one class matching {args.cls!r}, found {len(found)}.")
        return 1
    klass = found[0]
    grade = re.sub(r"\D", "", klass["level"])
    chapters = [c["id"] for c in engine.list_chapters() if str(c["grade"]) == grade or not grade]
    by_chapter = engine.concept_ids_by_chapter()
    ordered = [cid for ch in chapters for cid in by_chapter[ch]]
    made = have_already = no_fit = failed = 0
    for student in store.list_class_students(klass["class_id"]):
        have = lesson_service.concepts_with_lessons(student["interest"])
        wanted = 0  # concepts that can take a story, counted until --concepts is reached
        for concept_id in [c for c in ordered if c in have]:
            if wanted >= args.concepts:
                break
            ctx = ps._context(student["student_id"], concept_id)
            if ctx is None:
                continue  # no hobby of theirs fits this concept's domain, or no lesson text
            wanted += 1
            if ps._is_current(store.get_personal_story(student["student_id"], concept_id), ctx):
                have_already += 1
                continue
            with llm.usage_context(feature="story_writer", student_id=student["student_id"]):
                row = ps.generate(student["student_id"], concept_id)
            ok = row is not None and row["status"] == ps.READY
            made += ok
            failed += not ok
            print(f"  {'ready ' if ok else (row or {}).get('status', 'none'):6} {student['username']} · {concept_id}", flush=True)
        no_fit += args.concepts - wanted
    print(f"Done: {made} written, {have_already} already there, {no_fit} short (no concept with a fitting hobby), "
          f"{failed} not written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
