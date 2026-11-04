"""Create a teacher account (run on the server, by whoever runs EcoLearn).

Teacher accounts can't be made from the website on purpose: a teacher can reset
students' passwords, so "become a teacher" must not be a button anyone can press.
Whoever has access to this machine creates them here instead.

Usage (from the project root):
    venv\\Scripts\\python.exe scripts\\create_teacher.py --name "Ms. Rao" --username rao.physics

The password is asked for twice and never echoed or passed on the command line,
where it would end up in the shell history. The teacher then logs in at
/teacher/login and can change it in the teacher pages.

The account goes into the same database as the API (ECOLEARN_PROGRESS_DB, default
data/progress.db), so run this on the machine the API runs on.
"""

from __future__ import annotations

import argparse
import getpass
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(_ROOT / "apps"))

from ecolearn import platform_api as api  # noqa: E402
from ecolearn.errors import EcoLearnError  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an EcoLearn teacher account.")
    parser.add_argument("--name", required=True, help='Display name, e.g. "Ms. Rao"')
    parser.add_argument("--username", required=True, help="Login name, e.g. rao.physics")
    args = parser.parse_args()

    password = getpass.getpass("Password (at least 8 characters): ")
    if password != getpass.getpass("Repeat password: "):
        print("The two passwords don't match. Nothing was created.", file=sys.stderr)
        return 1

    try:
        teacher = api.create_teacher(args.name, args.username, password)
    except EcoLearnError as exc:  # also covers ConflictError
        print(f"Not created: {exc}", file=sys.stderr)
        return 1

    print(f"Created teacher {teacher['name']!r} with username {teacher['username']!r}.")
    print("They can log in at /teacher/login.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
