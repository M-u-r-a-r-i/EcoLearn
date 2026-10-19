"""A family's data requests: export everything about a student, erase everything about a student. No network.

The point is COMPLETENESS, so the test works from the live schema, not from a list it keeps itself:

  * One student ("Aarav") is given a row in EVERY table that holds a student id (account, survey and its history,
    starting and end checks, lessons, ratings, quiz and revision answers, progress, a personal story, a help-chat
    event, a model-call log row) plus a note in a class coaching run and a mention in a class plan. If a new table
    is added later, this test fails until it is covered here too, which is the intended alarm.
  1. Export: every one of those tables appears, no password hash, none of a classmate's data, concept names in words.
  2. Erase: the account and every row go; a search of the WHOLE database, run independently of the code under test,
     finds neither the student's id, name nor username; sign-in and an old session stop working.
  3. Nobody else is touched: a classmate's rows are identical before and after; the class's coaching notes and plans
     still read; the model-call log keeps its rows but loses the link to the child.
  4. The scripts: a dry run changes nothing, --confirm exports first and then erases, unknown users are refused.

Run: venv\\Scripts\\python.exe tests\\test_student_data_rights.py
"""

from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import warnings
from pathlib import Path
from types import SimpleNamespace

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_rights_"))
_DB = _TMP / "rights.db"
os.environ["ECOLEARN_PROGRESS_DB"] = str(_DB)
os.environ["LLM_MODEL"] = "free/main-model"  # on, so a personal story is written (by the scripted stand-in below)
os.environ["LLM_BASE_URL"] = "http://gateway.test/v1"
os.environ["ECOLEARN_REVISION_HOURS"] = "0"  # a revision question is due straight away
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api import security  # noqa: E402
from api.main import app  # noqa: E402
from src import llm, platform_api as api  # noqa: E402
from src.content import lesson_service  # noqa: E402
from src.errors import NotFoundError  # noqa: E402
from src.learner import diagnostic, personal_story as ps  # noqa: E402
from src.progress import store  # noqa: E402

_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


def key(concept_id: str, source: str) -> tuple[str, str]:
    c = lesson_service.get_authored_lesson(concept_id, source).check
    return c.answer, next(o for o in c.options if o != c.answer)


STORY = ("Riya stands at the back of the court, waiting for a smash. Her friend hits the light shuttle and the heavy "
         "practice ball with the same swing. One shoots off, one barely moves. Same hit, so why such different results? "
         "Riya frowns at the net and wonders what the racquet really changes.")
ANALOGY = ("The racquet's push is the net force, the shuttle and the ball are the masses, and how quickly each speeds "
           "up is the acceleration. The lighter one speeds up far more.")
LIMIT = "Real shuttles feel strong air drag, which the simple picture ignores."


class Script:
    def __init__(self, *replies):
        self.replies = list(replies)

    def __call__(self, messages, role="main", **_):
        return llm.ChatResult(text=self.replies.pop(0), model=f"{role}-model")


def draft() -> str:
    return json.dumps({"fit": True, "story": STORY, "analogy": ANALOGY, "limit": LIMIT})


def coaching_chat(messages, **kw):
    text = messages[0]["content"]
    start = text.index("CASE FILES (JSON):\n") + len("CASE FILES (JSON):\n")
    cases = json.loads(text[start:text.index("\n\nWrite the JSON now.")])
    return SimpleNamespace(model="scripted", text=json.dumps({
        a: {"note": "This student's record shows a few facts worth a short look this week.",
            "evidence": [next(iter(c))], "next_step": "Check in with them briefly this week."} for a, c in cases.items()}))


def all_student_tables() -> list[str]:
    conn = sqlite3.connect(_DB)
    names = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
    return [n for n in names if "student_id" in [c[1] for c in conn.execute(f'PRAGMA table_info("{n}")')]]


def scan_database(needle: str) -> dict[str, int]:
    """Independent of the code under test: every column of every table, as text."""
    conn = sqlite3.connect(_DB)
    found = {}
    for (name,) in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall():
        for col in conn.execute(f'PRAGMA table_info("{name}")').fetchall():
            n = conn.execute(f'SELECT COUNT(*) FROM "{name}" WHERE CAST("{col[1]}" AS TEXT) LIKE ?', (f"%{needle}%",)).fetchone()[0]
            if n:
                found[f"{name}.{col[1]}"] = n
    return found


def row_counts(student_id: str) -> dict[str, int]:
    conn = sqlite3.connect(_DB)
    return {t: conn.execute(f'SELECT COUNT(*) FROM "{t}" WHERE student_id = ?', (student_id,)).fetchone()[0]
            for t in all_student_tables()}


def build() -> dict:
    rao = api.create_teacher("Ms. Rao", "rao.rights", "teach-physics-1")
    made = api.create_class(rao["teacher_id"], "11-R", "Class 11", "cricket", "Aarav Kumar\nMeera Iyer\nKabir Shah")
    cred = {c["name"]: c for c in made["credentials"]}
    class_id = made["class"]["class_id"]
    tid = rao["teacher_id"]
    a = cred["Aarav Kumar"]["student_id"]
    b = cred["Meera Iyer"]["student_id"]

    api.submit_survey(a, {"hobbies": ["badminton"], "session_length": "m5", "focus_drift": "often", "physics_feel": "nervous"})
    api.update_survey(a, {"hobbies": ["badminton", "music"], "session_length": "m30", "focus_drift": "stays"})
    for sid in (a, b):
        qs = diagnostic.choose_questions("Class 11", "cricket", diagnostic.form_for(sid))
        # wrong on purpose: an idea the starting check marks as known skips revision
        picks = {q["concept_id"]: key(q["concept_id"], q["source_interest"])[1] for q in qs}
        api.submit_diagnostic(sid, picks, hobbies=["badminton", "music"])
    api.set_class_end_check(tid, class_id, True)
    for sid in (a, b):
        chosen = diagnostic.choose_end_questions("cricket", store.get_diagnostic_answers([sid]))
        api.submit_end_check(sid, {q["concept_id"]: key(q["concept_id"], q["source_interest"])[0] for q in chosen})
    fresh = next(i for i in diagnostic.load_config()["source_interests"] if i != "cricket")
    for sid in (a, b):
        view = api.start_lesson_view(sid, "displacement")
        api.record_lesson_time(sid, view["view_id"], 95)
        api.submit_assessment(sid, "velocity", key("velocity", "cricket")[0], "sure")  # cleared, so due for revision
        api.rate_lesson(sid, "displacement", 1)
        api.submit_revision(sid, "velocity", key("velocity", fresh)[0], "sure")
        api.ask_help(sid, "second_law", "show me porn")  # stopped at the front door: leaves one help event
        store.record_llm_call({"feature": "story_writer", "model": "m", "ok": True, "student_id": sid,
                               "prompt_tokens": 10, "completion_tokens": 5, "latency_ms": 1})
    ps.SYNC = True
    ps.chat = Script(draft(), '{"verdict": "PASS", "problems": []}')
    api.get_personal_story(a, "second_law")
    api.generate_coaching_notes(tid, class_id, chat=coaching_chat)
    api.generate_class_plan(tid, class_id, models=[])
    for sid in (a, b):  # the open learner profile and teacher-approved coaching actions (2026-10-14)
        api.set_insight(sid, "sure_wrong", True)
        api.apply_coaching_action(tid, class_id, sid, "revise", "velocity")
        store.save_practice(sid, "velocity", False, None, None, [])  # a practice attempt (2026-10-19)
    return {"tid": tid, "class_id": class_id, "a": a, "b": b, "c": cred["Kabir Shah"]["student_id"], "cred": cred}


def test_export(ctx: dict) -> None:
    print("\n[1] export")
    a = ctx["a"]
    data = api.export_student_data(a)
    check(set(data["tables"]) == set(all_student_tables()),
          f"every table that holds a student id has rows for the test student (missing: "
          f"{sorted(set(all_student_tables()) - set(data['tables']))})")
    blob = json.dumps(data, default=str)
    check("password_hash" not in blob and "$2b$" not in blob, "no password hash anywhere in the export")
    check(ctx["b"] not in blob and "Meera" not in blob and "Kabir" not in blob, "none of a classmate's data or names")
    r = data["readable"]
    seconds = sum(v["active_seconds"] for v in data["tables"]["lesson_views"])
    check("Displacement" in r["lessons_opened"] and 0 < r["minutes_actively_read"] == round(seconds / 60, 1)
          and r["lesson_check_answers"]["total"] == 1, "the readable part uses concept names and real numbers")
    check(len(r["personal_stories"]) == 1 and r["personal_stories"][0]["story"] == STORY, "the personal story is included in full")
    check(r["help_chat_outcomes"] == {"blocked": 1}, "help chat: outcomes only")
    check("show me porn" not in blob, "and the typed words were never stored, so they cannot be exported")
    check(len(data["class_notes"]) == 1 and data["plans_that_included_them"] >= 1,
          "their coaching note and the class plans that included them are found")
    check(data["account"]["class"] == "11-R" and data["account"]["username"], "the account block names the class")
    try:
        api.export_student_data("stu_nobody")
        check(False, "unknown student → NotFoundError")
    except NotFoundError:
        check(True, "unknown student → NotFoundError")
    try:
        api.find_student_id("nobody.here")
        check(False, "unknown username → NotFoundError")
    except NotFoundError:
        check(True, "unknown username → NotFoundError")


def test_erase(ctx: dict) -> None:
    print("\n[2-3] erase")
    a, b, tid, class_id = ctx["a"], ctx["b"], ctx["tid"], ctx["class_id"]
    a_name, a_user = "Aarav Kumar", ctx["cred"]["Aarav Kumar"]["username"]
    b_before = json.dumps(store.export_student_rows(b), sort_keys=True, default=str)
    calls_before = sqlite3.connect(_DB).execute("SELECT COUNT(*) FROM llm_calls").fetchone()[0]
    token = security.create_token(a)

    result = api.delete_student(a)
    check(result["remaining"] == {}, "the function's own search finds no trace left")
    check(set(result["deleted"]) | set(result["anonymised"]) == set(all_student_tables()),
          "every table was handled: deleted, or (the usage log) unlinked")
    check(result["deleted"]["students"] == 1 and result["anonymised"]["llm_calls"] == 1, "the account is gone; the usage row is unlinked")
    check(scan_database(a) == {}, "an independent scan of every column of every table finds no trace of the student id")
    check(scan_database(a_name) == {} and scan_database(a_user) == {}, "nor their name, nor their username, anywhere")
    check(store.get_student(a) is None, "the account no longer exists")

    client = TestClient(app)
    r = client.post("/api/auth/login", json={"username": a_user, "password": ctx["cred"]["Aarav Kumar"]["password"]})
    check(r.status_code == 401, "they can no longer sign in")
    old = TestClient(app)
    old.cookies.set(security.COOKIE_NAME, token)
    check(old.get("/api/auth/me").status_code == 401, "an old session cookie stops working")

    check(json.dumps(store.export_student_rows(b), sort_keys=True, default=str) == b_before,
          "a classmate's data is byte-for-byte unchanged")
    check(sqlite3.connect(_DB).execute("SELECT COUNT(*) FROM llm_calls").fetchone()[0] == calls_before,
          "the usage log keeps every row (token counts stay true)")
    check(sqlite3.connect(_DB).execute("SELECT COUNT(*) FROM llm_calls WHERE student_id IS NULL").fetchone()[0] >= 1,
          "but one row lost its link to the child")
    notes = api.get_coaching_notes(tid, class_id)
    check(notes is not None and {s["name"] for s in notes["students"]} == {"Meera Iyer", "Kabir Shah"},
          "the class's coaching notes still read, without the erased student")
    check(api.get_class_plan(tid, class_id)["markdown"], "the class plan still reads")
    check(a not in {s["student_id"] for s in api.get_class_detail(tid, class_id)["students"]}, "the class list no longer shows them")
    try:
        api.delete_student(a)
        check(False, "erasing twice → NotFoundError")
    except NotFoundError:
        check(True, "erasing twice → NotFoundError")


def test_all_or_nothing() -> None:
    print("\n[3b] all or nothing")
    sid = api.register_student("Half Way", "half.way", "kid-password-1", "cricket", "Class 11")["student_id"]
    view = api.start_lesson_view(sid, "displacement")
    api.record_lesson_time(sid, view["view_id"], 20)
    api.rate_lesson(sid, "displacement", 1)
    before = row_counts(sid)
    assert sum(before.values()) >= 3  # the account, a lesson view, a rating
    conn = sqlite3.connect(_DB)
    # A corrupt row makes the erase fail AFTER it has already deleted the student's own rows.
    conn.execute("INSERT INTO coaching_notes (class_id, teacher_id, created_at, source, notes, aliases, trail) "
                 f"VALUES ('c', 't', 'now', 'rules', '{{}}', '{{\"S1\": \"{sid}\", broken', '[]')")
    conn.commit()
    conn.close()
    try:
        api.delete_student(sid)
        check(False, "a failure part-way raises")
    except Exception:
        check(True, "a failure part-way raises")
    check(store.get_student(sid) is not None, "the account is still there")
    check(row_counts(sid) == before, "and every table still has the same number of rows for them: nothing was half-deleted")
    conn = sqlite3.connect(_DB)
    conn.execute("DELETE FROM coaching_notes WHERE class_id = 'c'")
    conn.commit()
    conn.close()
    check(api.delete_student(sid)["remaining"] == {}, "with the corrupt row gone, the erase completes cleanly")


def run_script(name: str, *args: str) -> subprocess.CompletedProcess:
    env = {**os.environ, "PYTHONUTF8": "1", "ECOLEARN_PROGRESS_DB": str(_DB), "LLM_MODEL": ""}
    return subprocess.run([sys.executable, str(_ROOT / "scripts" / name), *args], capture_output=True, text=True,
                          encoding="utf-8", env=env, timeout=120)


def test_scripts(ctx: dict) -> None:
    print("\n[4] the scripts")
    user = ctx["cred"]["Kabir Shah"]["username"]
    c = ctx["c"]
    out = _TMP / "exports"
    shown = run_script("export_student.py", "--username", user)
    check(shown.returncode == 0 and "What EcoLearn holds about Kabir Shah" in shown.stdout and "$2b$" not in shown.stdout,
          "export prints a plain-language summary and no password")
    dry = run_script("delete_student.py", "--username", user)
    check(dry.returncode == 0 and "DRY RUN" in dry.stdout and store.get_student(c) is not None,
          "a dry run lists what would go and changes nothing")
    check(run_script("delete_student.py", "--username", "nobody.here", "--confirm").returncode == 1, "an unknown username is refused")
    done = run_script("delete_student.py", "--username", user, "--export", str(out), "--confirm")
    check(done.returncode == 0 and "Verified" in done.stdout and store.get_student(c) is None, "--confirm erases and verifies")
    check((out / f"{user}.md").exists() and (out / f"{user}.json").exists(), "and the family's copy was written first")
    check("password_hash" not in (out / f"{user}.json").read_text(encoding="utf-8"), "the JSON copy has no password hash")
    check(scan_database(c) == {}, "nothing about the second student remains either")


def main() -> None:
    ctx = build()
    test_export(ctx)
    test_erase(ctx)
    test_all_or_nothing()
    test_scripts(ctx)
    print(f"\nAll {_checks} student-data-rights checks passed.")


if __name__ == "__main__":
    main()
