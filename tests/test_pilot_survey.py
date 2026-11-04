"""The survey in the pilot report: who answered, what changed, said vs shown. No network.

Proves:
  1. survey_changes: only fields that really differ are reported, between consecutive sets.
  2. The report counts who answered, tallies what they said, and counts students who updated.
  3. History: every replaced set plus the current one, oldest first, the current one flagged.
  4. Said vs shown: groups students by what they said and reports how they read and answered.
  5. Privacy: pseudonyms only (S001...), never a name, username or student id, anywhere.
  6. The printed report and the CSV files carry the section.

Run: venv\\Scripts\\python.exe tests\\test_pilot_survey.py
"""

from __future__ import annotations

import io
import json
import os
import sys
import tempfile
import warnings
from contextlib import redirect_stdout
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(_ROOT / "apps"))
sys.path.insert(0, str(_ROOT / "scripts"))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_pilotsurvey_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "pilotsurvey.db")
os.environ["LLM_MODEL"] = ""
warnings.simplefilter("ignore")

import pilot_report as script  # noqa: E402
from ecolearn import platform_api as api  # noqa: E402
from ecolearn.progress import metrics, store  # noqa: E402

_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


def student(name: str, username: str) -> str:
    return api.register_student(name, username, "kid-password-1", "cricket", "Class 11")["student_id"]


def test_pure() -> None:
    print("\n[1] survey_changes")
    base = {"focus": {"span": "short", "session_minutes": 10, "drift": "often"},
            "learning": {"pace": "fast", "first_step": "try"}, "physics": {"feel": "nervous"},
            "hobby_levels": {"badminton": {"level": "fan"}}, "hobbies": ["badminton"]}
    later = json.loads(json.dumps(base))
    later["focus"]["span"] = "long"
    later["physics"]["feel"] = "ok"
    sets = [{"revision": 0, "saved_at": "t0", "traits": base}, {"revision": 1, "saved_at": "t1", "traits": later}]
    changes = metrics.survey_changes(sets)
    check({(c["field"], c["from"], c["to"]) for c in changes} == {("focus_span", "short", "long"),
                                                                    ("physics_feel", "nervous", "ok")},
          "only the fields that differ are reported, with from and to")
    check(all(c["revision"] == 1 for c in changes), "each change is attributed to the new revision")
    check(metrics.survey_changes(sets[:1]) == [], "one set alone has no changes")


def test_report() -> None:
    print("\n[2-6] the report")
    first = student("Ava Nair", "ava.n")
    second = student("Ben Das", "ben.d")
    third = student("Cia Roy", "cia.r")
    student("Dev Pal", "dev.p")  # never answers
    api.submit_survey(first, {"hobbies": ["badminton"], "session_length": "m5", "focus_drift": "often",
                              "pace": "fast", "physics_feel": "nervous"})
    api.submit_survey(second, {"hobbies": ["music"], "session_length": "m30", "focus_drift": "stays",
                               "pace": "steady", "physics_feel": "love"})
    api.submit_survey(third, {"pace": "fast", "physics_feel": "nervous"})
    api.update_survey(first, {"hobbies": ["badminton", "music"], "session_length": "m30",
                              "focus_drift": "stays", "pace": "fast", "physics_feel": "ok"})
    # How they actually read: Ava skims, Ben reads properly (>= 3 views are needed to say anything).
    for sid, seconds in ((first, 5), (second, 120)):
        for concept in ("second_law", "third_law", "inertia_first_law"):
            view = api.start_lesson_view(sid, concept)
            api.record_lesson_time(sid, view["view_id"], seconds)

    sv = api.pilot_report()["survey"]
    check(sv["taken"] == 3 and sv["total"] == 4, "3 of 4 students answered")
    check(sv["distributions"]["pace"] == {"fast": 2, "steady": 1}, "what they said is tallied")
    check(sv["distributions"]["physics_feel"] == {"nervous": 1, "love": 1, "ok": 1},
          "the CURRENT answer counts (Ava's update replaced 'nervous')")
    check(sv["updated_students"] == 1 and sv["revisions"] == 1, "one student updated, once")

    fields = {c["field"]: (c["from"], c["to"]) for c in sv["changes"]}
    check(fields.get("focus_span") == ("short", "long") and fields.get("physics_feel") == ("nervous", "ok"),
          "the changes name what moved, from and to")
    check("pace" not in fields, "an unchanged answer isn't a change")
    check(sv["changed_fields"]["focus_span"] == 1, "changed fields are counted")

    ava = [h for h in sv["history"] if h["student_id"] == "S001"]
    check([h["revision"] for h in ava] == [0, 1] and [h["current"] for h in ava] == [False, True],
          "history holds the replaced set then the current one, flagged")
    check(len([h for h in sv["history"] if h["student_id"] == "S002"]) == 1, "a student who never updated has one row")

    groups = {g["value"]: g for g in sv["said_vs_shown"]["pace"]}
    check(groups["fast"]["students"] == 2 and groups["steady"]["students"] == 1, "said-vs-shown groups by what they said")
    check(set(sv["said_vs_shown"]) == {"focus_span", "pace", "physics_feel"}, "three groupings are reported")

    blob = json.dumps(sv, default=str)
    private = ["Ava", "Nair", "ava.n", "Ben", "Das", "ben.d", "Cia", "cia.r", "Dev", "dev.p", first, second, third]
    check(not [p for p in private if p in blob], "no name, username or student id anywhere in the survey section")
    check({r["student_id"] for r in sv["rows"]} == {"S001", "S002", "S003"}, "students are S001...")

    out = io.StringIO()
    with redirect_stdout(out):
        script.print_survey(sv)
    text = out.getvalue()
    check("3 of 4 students answered" in text and "Updated their answers: 1 students, 1 updates" in text
          and "NOT evidence" in text, "the printed section says who answered, who updated, and the caveat")

    empty = metrics.survey_report([], {}, 5)
    out = io.StringIO()
    with redirect_stdout(out):
        script.print_survey(empty)
    check("Nobody has answered yet" in out.getvalue(), "an empty pilot prints a plain sentence, not a crash")

    csv_dir = _TMP / "csv"
    argv = sys.argv
    sys.argv = ["pilot_report.py", "--csv", str(csv_dir)]
    try:
        with redirect_stdout(io.StringIO()):
            script.main()
    finally:
        sys.argv = argv
    for name in ("survey", "survey_history", "survey_changes"):
        check((csv_dir / f"{name}.csv").exists(), f"{name}.csv is written")
    check("ava" not in (csv_dir / "survey.csv").read_text(encoding="utf-8").lower(), "the survey CSV has no names")


def main() -> None:
    test_pure()
    test_report()
    print(f"\nAll {_checks} pilot-survey checks passed.")


if __name__ == "__main__":
    main()
