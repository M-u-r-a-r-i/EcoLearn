r"""Permanently erase one student and everything EcoLearn holds about them.

    venv\Scripts\python.exe scripts\delete_student.py --username aarav.k                      # dry run: shows what would go
    venv\Scripts\python.exe scripts\delete_student.py --username aarav.k --export exports --confirm

For the operator, on a request from a parent or guardian (check who is asking first). It CANNOT BE UNDONE.

  * Without --confirm nothing is changed: it lists what would be removed.
  * With --confirm it erases the account and every row tied to it in one transaction, then searches the whole
    database for the student's id to prove nothing is left. If anything is found it says so and exits with 2.
  * --export DIR writes the family's copy (see scripts/export_student.py) BEFORE erasing, so they can keep it.
    Recommended: after the erase there is nothing left to export.

What it does not touch, and you must handle: **backups** and any copy of the database file made earlier
(the data is still in them until they are deleted or age out under your retention rule), and the class-level
plans written for the teacher, from which only this student's label and note are removed.
The AI usage log keeps its token counts and times but loses the link to the child.

Reads and writes the database the API uses (ECOLEARN_PROGRESS_DB, default data/progress.db). Stop the API first
if it is running against the same file, or at least make sure nobody is using it.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import platform_api as api  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import export_student  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--username", required=True, help="the student's username")
    ap.add_argument("--export", metavar="DIR", help="write the family's copy here before erasing")
    ap.add_argument("--confirm", action="store_true", help="actually erase (without it: a dry run)")
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        student_id = api.find_student_id(args.username)
        data = api.export_student_data(student_id)
    except ValueError as exc:
        print(exc)
        return 1
    a = data["account"]
    print(f"Student: {a['name']} ({a['username']}), {a['level']}" + (f", class {a['class']}" if a["class"] else ""))
    print("Rows that would be removed:")
    for table, rows in data["tables"].items():
        print(f"  {table:<24}{len(rows):>6}" + ("   (kept as an anonymous usage count)" if table == "llm_calls" else ""))
    print(f"  coaching notes about them: {len(data['class_notes'])}; class plans that include them: "
          f"{data['plans_that_included_them']} (their label is removed)")
    if not args.confirm:
        print("\nDRY RUN: nothing was changed. Add --confirm to erase. This cannot be undone.")
        return 0
    if args.export:
        sys.argv = ["export_student.py", "--username", args.username, "--out", args.export]
        if export_student.main() != 0:
            print("The export failed, so nothing was erased.")
            return 1
    result = api.delete_student(student_id)
    print("\nErased.")
    for table, n in result["deleted"].items():
        print(f"  deleted    {table:<24}{n:>6}")
    for table, n in result["anonymised"].items():
        print(f"  unlinked   {table:<24}{n:>6}")
    print(f"  edited     coaching notes: {result['edited']['coaching_notes']}, class plans: {result['edited']['class_plans']}")
    if result["remaining"]:
        print("\nWARNING: the student's id still appears in the database:")
        for where, n in result["remaining"].items():
            print(f"  {where}: {n}")
        return 2
    print("\nVerified: a search of the whole database finds no trace of this student.")
    print("Remember: backups and earlier copies of the database still hold the data until they are deleted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
