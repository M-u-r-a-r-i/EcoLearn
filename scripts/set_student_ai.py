r"""Switch the AI features off (or back on) for one student.

    venv\Scripts\python.exe scripts\set_student_ai.py --username aarav.k --off
    venv\Scripts\python.exe scripts\set_student_ai.py --username aarav.k --on

For the operator, when a family asks them directly to keep their child out of the AI parts (after checking
who is asking). A teacher can do the same from the Students tab of their class. With the switch off, nothing
about the student goes to a model: no personal story, the help chat shows the lesson's key idea, the coaching
note is written by rules, and the teaching assistant does not see them. Lessons, checks and progress are
unchanged (none of them use AI).

It changes the same database as the API (ECOLEARN_PROGRESS_DB, default data/progress.db).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import platform_api as api  # noqa: E402
from src.errors import NotFoundError  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--username", required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--off", action="store_true", help="switch the AI features off for this student")
    group.add_argument("--on", action="store_true", help="switch them back on")
    args = parser.parse_args()
    try:
        student_id = api.find_student_id(args.username)
    except NotFoundError as exc:
        print(exc)
        return 1
    api.operator_set_student_ai(student_id, enabled=args.on)
    print(f"AI features for {args.username}: {'on' if args.on else 'off'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
