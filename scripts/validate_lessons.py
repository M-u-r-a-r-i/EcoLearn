"""Validate authored lessons and report coverage.

    venv\\Scripts\\python.exe scripts\\validate_lessons.py                  # every lesson
    venv\\Scripts\\python.exe scripts\\validate_lessons.py --chapter laws_of_motion
    venv\\Scripts\\python.exe scripts\\validate_lessons.py --interest cricket --chapter laws_of_motion
    venv\\Scripts\\python.exe scripts\\validate_lessons.py path\\to\\file.md ...
    venv\\Scripts\\python.exe scripts\\validate_lessons.py --coverage       # counts per chapter

Exit code 1 if any lesson has an error, so an authoring session can't miss a
failure. Checks format only — see src/content/validate.py for what it can and
cannot catch.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

from src.content.lesson_service import lessons_dir  # noqa: E402
from src.content.validate import check_media_library, coverage, validate_files  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="*", type=Path, help="specific lesson files")
    parser.add_argument("--chapter", help="only this chapter id")
    parser.add_argument("--interest", help="only this interest id")
    parser.add_argument("--coverage", action="store_true", help="print per-chapter coverage")
    args = parser.parse_args()

    root = lessons_dir()
    if args.coverage:
        rows = coverage(root)
        total_p = sum(r["present"] for r in rows)
        total_e = sum(r["expected"] for r in rows)
        print(f"{'class':<6}{'chapter':<44}{'present':>9}{'expected':>10}")
        for r in rows:
            print(f"{r['grade']:<6}{r['chapter']:<44}{r['present']:>9}{r['expected']:>10}")
        print(f"{'':<6}{'TOTAL':<44}{total_p:>9}{total_e:>10}  ({100 * total_p / total_e:.1f}%)")
        return 0

    if args.paths:
        paths = [p.resolve() for p in args.paths]
    else:
        chapter = args.chapter or "*"
        interest = args.interest or "*"
        paths = sorted(root.glob(f"*/{chapter}/*/{interest}__*.md"))
    if not paths:
        print("No lesson files matched.")
        return 0

    report = validate_files(paths, root)
    report.issues.extend(check_media_library())  # famous-image licences, stale graphs
    by_file: dict[Path, list] = {}
    for issue in report.issues:
        by_file.setdefault(issue.path, []).append(issue)
    for path, issues in by_file.items():
        try:
            shown = path.relative_to(root)
        except ValueError:
            shown = path
        print(f"\n{shown}")
        for i in issues:
            print(f"  {i.level.upper():<8}{i.message}")

    print(f"\n{report.valid}/{report.files} lessons valid, {len(report.errors)} error(s)."
          + ("" if report.katex_checked else "  (maths NOT rendered — see warnings)"))
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
