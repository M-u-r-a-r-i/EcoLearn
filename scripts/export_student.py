r"""Show a family everything EcoLearn holds about one student.

    venv\Scripts\python.exe scripts\export_student.py --username aarav.k
    venv\Scripts\python.exe scripts\export_student.py --username aarav.k --out exports

For the operator, on a request from a parent or guardian (after checking who is asking). Without --out it
prints a plain-language summary. With --out DIR it writes two files there: `<username>.md` (the summary, to
hand to the family) and `<username>.json` (every row, complete, for anyone who wants the detail).

It reads the same database as the API (ECOLEARN_PROGRESS_DB, default data/progress.db) and changes nothing.
The password is never included: only a scrambled copy is stored and it is not exported.
Old copies of the database (backups) are not searched.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import platform_api as api  # noqa: E402


def render_markdown(data: dict) -> str:
    a, r = data["account"], data["readable"]
    lines = [f"# What EcoLearn holds about {a['name']}", "",
             "This is everything stored about this student, in plain words. The full detail, row by row, is in the"
             " matching `.json` file. The password is never shown: only a scrambled copy is kept.", "",
             "## Account", f"- Name: {a['name']}", f"- Username: {a['username']}", f"- Class: {a['level']}"
             + (f", group {a['class']}" if a["class"] else ""), f"- Lesson topic: {a['interest']}",
             f"- Account made: {a['created_at']}", ""]
    lines += ["## Hobbies and survey", f"- Hobbies: {', '.join(r['hobbies']) if r['hobbies'] else 'none given'}"]
    if r["survey_summary"]:
        lines += [f"- {s}" for s in r["survey_summary"]]
    else:
        lines.append("- The 'getting to know you' survey has not been answered.")
    if r["survey_updates"]:
        lines.append(f"- Answers were updated {r['survey_updates']} time(s); the earlier sets are kept as history.")
    lines += ["", "## Activity",
              f"- Lessons opened: {len(r['lessons_opened'])}" + (f" ({', '.join(r['lessons_opened'])})" if r["lessons_opened"] else ""),
              f"- Minutes actively reading: {r['minutes_actively_read']}",
              f"- Quiz answers: {r['lesson_check_answers']['total']} ({r['lesson_check_answers']['right']} right)",
              f"- Starting-check questions answered: {r['starting_check_questions_answered']}",
              f"- End-check questions answered: {r['end_check_questions_answered']}",
              f"- Revision answers: {r['revision_answers']}", ""]
    if r["progress"]:
        lines += ["## Progress"] + [f"- {p['concept']}: {p['status']} ({p['attempts']} attempt(s))" for p in r["progress"]] + [""]
    if r["personal_stories"]:
        lines.append("## AI-written personal stories")
        for s in r["personal_stories"]:
            lines.append(f"- **{s['concept']}** (hobby: {s['hobby']}, {s['status']})")
            if s["story"]:
                lines += [f"  > {s['story']}", f"  > Analogy: {s['analogy']}", f"  > Where it stops: {s['limit']}"]
        lines.append("")
    lines += ["## Help chat", "- What was typed is **not stored**. Only what happened to each question is: "
              + (", ".join(f"{k}: {v}" for k, v in r["help_chat_outcomes"].items()) or "no questions asked") + ".", ""]
    if data["class_notes"]:
        lines.append("## Notes written for the teacher about this student")
        for n in data["class_notes"]:
            lines += [f"- ({n['made']}) {n['note'].get('note', '')}  Suggested step: {n['note'].get('next_step', '')}"]
        lines.append("")
    lines += ["## Other", f"- AI model calls logged for this student: {r['ai_model_calls_logged']} (counts and times only, never the text).",
              f"- Class plans for the teacher that included this student among their labelled students: {data['plans_that_included_them']}"
              " (those plans are about the whole class and are not listed here).", ""]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--username", required=True, help="the student's username")
    ap.add_argument("--out", help="write <username>.md and <username>.json into this folder")
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        data = api.export_student_data(api.find_student_id(args.username))
    except ValueError as exc:
        print(exc)
        return 1
    text = render_markdown(data)
    if not args.out:
        print(text)
        return 0
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{args.username}.md").write_text(text, encoding="utf-8")
    (out / f"{args.username}.json").write_text(json.dumps(data, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print(f"Wrote {out / (args.username + '.md')} and {out / (args.username + '.json')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
