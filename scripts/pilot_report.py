"""The whole pilot in one report: run on the server, by whoever runs EcoLearn.

Teachers see their own class in the web app (/teacher/class). This is the view
across every class, for the people evaluating the pilot and for the finals
pitch. It prints the headline numbers, the most common misconceptions, the
hardest concepts, and the same numbers per interest.

With --csv it also writes the raw rows (lesson views, answers, ratings,
students) for analysis in a spreadsheet or pandas. **No names or usernames are
ever written:** students become S001, S002…, classes C01, C02…, in the order
they were created. That's what makes the export safe to share with someone
analysing the data, which matters because the pilot students are minors.

Usage (from the project root):
    venv\\Scripts\\python.exe scripts\\pilot_report.py
    venv\\Scripts\\python.exe scripts\\pilot_report.py --csv pilot_export

Reads the same database as the API (ECOLEARN_PROGRESS_DB, default
data/progress.db). Read-only: it never changes anything.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

from src import platform_api as api  # noqa: E402


def pct(value: float | None) -> str:
    return "—" if value is None else f"{value * 100:.0f}%"


def print_report(report: dict, top: int) -> None:
    insights = report["insights"]
    s = insights["summary"]
    print("EcoLearn pilot report")
    print("=" * 60)
    print(f"Students            {s['students']}  ({s['active_students']} active)")
    print(f"Lessons opened      {s['lessons_opened']}  ({s['distinct_lessons']} distinct student × lesson)")
    print(f"Active reading      {s['active_minutes']} min  "
          f"(median {s['median_minutes_per_lesson'] or '—'} min per lesson)")
    print(f"Checks answered     {s['answers']}  ({s['first_try_answers']} first tries)")
    print(f"First-try accuracy  {pct(s['first_try_accuracy'])}")
    c = s["by_confidence"]
    print(f"How sure vs right   sure {pct(c['sure']['accuracy'])} ({c['sure']['answers']}) · "
          f"think {pct(c['think']['accuracy'])} ({c['think']['answers']}) · "
          f"guess {pct(c['guess']['accuracy'])} ({c['guess']['answers']}) · "
          f"sure but wrong {s['sure_but_wrong']}")
    print(f"Lesson ratings      👍 {s['thumbs_up']}  👎 {s['thumbs_down']}  "
          f"(approval {pct(s['approval'])})")
    stories = report["stories"]
    ready = [st for st in stories if st["status"] == "ready"]
    print(f"Personal stories    {len(ready)} written, "
          f"{sum(1 for st in ready if st['reported_at'])} reported by students, "
          f"{sum(1 for st in ready if st['hidden'] and st['hidden_by'] == 'teacher')} hidden by teachers, "
          f"{sum(1 for st in stories if st['status'] in ('failed', 'no_fit'))} not written (checks/fit)")

    g = report["check_gains"]
    print(f"\nStarting check → end check  ({g['students_finished']} of {g['students_started']} "
          f"students took both; {g['paired_answers']} paired answers)")
    if g["paired_answers"]:
        b, a = g["before"], g["after"]
        print(f"  Right answers     {pct(g['right_before'])} → {pct(g['right_after'])}")
        print(f"  Mix-ups           {b['mix_up']} → {a['mix_up']}   (not sure {b['unsure']} → {a['unsure']})")
        print(f"  Fixed {g['fixed']}  ·  learned from 'not sure' {g['learned']}  ·  slipped {g['slipped']}")
        for label, part in (("studied", g["studied"]), ("not studied", g["not_studied"])):
            print(f"  Concepts {label:<12} {pct(part['right_before'])} → {pct(part['right_after'])}"
                  f"  ({part['pairs']} pairs)")
        print("  (Not-studied concepts are a rough control: a gain there isn't the lessons'.)")

    print(f"\nBy interest")
    print(f"  {'interest':<13}{'students':>9}{'opens':>7}{'1st try':>9}{'👍':>5}{'👎':>5}{'approval':>10}")
    for i in insights["interests"]:
        print(f"  {i['interest']:<13}{i['students']:>9}{i['lessons_opened']:>7}"
              f"{pct(i['first_try_accuracy']):>9}{i['thumbs_up']:>5}{i['thumbs_down']:>5}"
              f"{pct(i['approval']):>10}")

    print(f"\nMost common misconceptions (top {top})")
    for m in insights["misconceptions"][:top]:
        print(f"  {m['students']} of {m['students_answered']} students ({pct(m['share'])}) — "
              f"{m['concept_name']} [{m['interest']}], chose {m['option']}")
        if m["misconception"]:
            print(f"      {m['misconception']}")

    print(f"\nHardest concepts by first-try accuracy (top {top})")
    for c in [c for c in insights["concepts"] if c["students_answered"]][:top]:
        print(f"  {pct(c['first_try_accuracy']):>5}  {c['concept_name']}  "
              f"({c['students_answered']} answered, chapter: {c['chapter_name'] or c['chapter_id']})")


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="EcoLearn pilot report (read-only).")
    parser.add_argument("--csv", metavar="DIR", help="also write pseudonymised CSVs to DIR")
    parser.add_argument("--top", type=int, default=10, help="rows per list (default 10)")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # the emoji, on a Windows console
    report = api.pilot_report()
    print_report(report, args.top)

    if args.csv:
        out = Path(args.csv)
        out.mkdir(parents=True, exist_ok=True)
        insights = report["insights"]
        for name, rows in (
            ("students", report["students"]),
            ("lesson_views", report["views"]),
            ("answers", report["answers"]),
            ("ratings", report["ratings"]),
            ("starting_check", report["diagnostic"]),
            ("end_check", report["end_check"]),
            ("check_gains_per_concept", report["check_gains"]["concepts"]),
            ("personal_stories", report["stories"]),
            ("per_student", insights["students"]),
            ("per_concept", insights["concepts"]),
            ("per_interest", insights["interests"]),
            ("misconceptions", insights["misconceptions"]),
        ):
            write_csv(out / f"{name}.csv", rows)
        print(f"\nCSV files written to {out.resolve()} (pseudonymised: no names or usernames).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
