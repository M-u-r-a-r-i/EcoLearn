"""The open learner profile, behaviour-aware adaptations, and teacher-approved coaching actions (2026-10-14). No network.

  1. The profiler's rules (src/ecolearn/learner/profiler.py), pure: quiet without data; survey insights with their effects;
     "one page may be fast" overrides a fast reader who skims and gets checks wrong; "sure but wrong" turns on the
     slow-down nudge; "doing better than you think"; every threshold respected; a dismissal switches the effect off.
  2. Through the boundary: the profile, "that's not me" and undo, an unknown insight refused; the lesson envelope's
     prefs follow the profile.
  3. The revision queue: a concept answered wrong while sure comes back sooner (and not when that insight is
     dismissed); a mastered concept waits as a keep-it-fresh question on a widening schedule.
  4. Coaching actions: rules notes propose an action; a model's action is kept only if it names a concept from that
     student's own mix-ups; the teacher approves; "revise" puts the concept at the top of the student's revision list,
     answering it records the outcome; "check_in" is recorded; follow-through counts; only the class's own teacher.
  5. HTTP: the profile routes (student only) and the action route (teacher only).

Run: venv\\Scripts\\python.exe tests\\test_learner_profile.py
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import types
import warnings
from datetime import datetime, timedelta, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(_ROOT / "apps"))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_profile_"))
_DB = _TMP / "profile.db"
os.environ["ECOLEARN_PROGRESS_DB"] = str(_DB)
os.environ["LLM_MODEL"] = ""
os.environ["ECOLEARN_REVISION_HOURS"] = "20"
os.environ["ECOLEARN_EXPERIMENTS"] = "off"  # the profile rules are tested here; experiments in test_pilot_experiment
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from ecolearn import platform_api as api  # noqa: E402
from ecolearn.agents import coaching_agent  # noqa: E402
from ecolearn.content import lesson_service  # noqa: E402
from ecolearn.errors import EcoLearnError, NotFoundError  # noqa: E402
from ecolearn.learner import diagnostic, profiler, survey  # noqa: E402
from ecolearn.progress import store  # noqa: E402

_checks = 0
_n = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


def raises(exc, fn, *args) -> None:
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"FAIL: expected {exc.__name__} from {fn.__name__}")


def key(concept_id: str, interest: str) -> tuple[str, str]:
    c = lesson_service.get_authored_lesson(concept_id, interest).check
    return c.answer, next(o for o in c.options if o != c.answer)


def ev(correct: bool, confidence: str | None, at: str = "2026-10-01T00:00:00+00:00") -> dict:
    return {"source": "lesson", "at": at, "correct": correct, "question": "cricket", "text": None,
            "confidence": confidence}


FAST_TRY_NERVOUS = {"pace": "fast", "first_step": "try", "physics_feel": "nervous",
                    "session_length": "m5", "focus_drift": "often", "hobbies": ["badminton"]}


def traits(answers: dict) -> dict:
    return survey.derive_traits(survey.clean(answers))


def ids(profile: dict) -> dict:
    return {i["id"]: i for i in profile["insights"]}


# ---------------------------------------------------------------------------
def test_rules() -> None:
    print("\n[1] the profiler's rules")
    quiet = profiler.build(None, {"views": 0, "skim_share": None}, (0, 0), {}, set())
    check(quiet["insights"] == [] and quiet["prefs"] == {**survey.DEFAULT_PREFS, "slow_down": False}
          and quiet["sooner"] == [], "no survey and no data: no insights, default prefs")

    t = traits(FAST_TRY_NERVOUS)
    said = profiler.build(t, {"views": 0, "skim_share": None}, (0, 0), {}, set())
    got = ids(said)
    check({"pace_fast", "example_first", "break_nudge", "gentle"} <= set(got)
          and all(i["kind"] == "said" for i in said["insights"]), "the survey's adaptations are insights, marked 'said'")
    check(said["prefs"]["mode"] == "all" and said["prefs"]["example_first"] and said["prefs"]["gentle"]
          and said["prefs"]["break_after_minutes"], "and their effects are on")
    check(all(i["detail"] and i["effect"] and i["evidence"] for i in said["insights"]),
          "every insight says what we saw, the evidence, and what changes")

    off = profiler.build(t, {"views": 0, "skim_share": None}, (0, 0), {}, {"pace_fast", "example_first", "gentle"})
    check(off["prefs"]["mode"] == "steps" and not off["prefs"]["example_first"] and not off["prefs"]["gentle"]
          and not ids(off)["pace_fast"]["active"], "'that's not me' switches each effect off")

    skimmer = {"views": 6, "skim_share": 0.67}
    corrected = profiler.build(t, skimmer, (1, 5), {}, set())
    check("pace_check" in ids(corrected) and corrected["prefs"]["mode"] == "steps"
          and ids(corrected)["pace_check"]["kind"] == "shown",
          "said fast, but skims and gets checks wrong: lessons go one step at a time")
    check(any("67%" in e for e in ids(corrected)["pace_check"]["evidence"])
          and any("1 of 5" in e for e in ids(corrected)["pace_check"]["evidence"]), "with the numbers as evidence")
    kept = profiler.build(t, skimmer, (1, 5), {}, {"pace_check"})
    check(kept["prefs"]["mode"] == "all", "dismissing the correction keeps one page")
    doing_fine = profiler.build(t, skimmer, (4, 5), {}, set())
    check("pace_check" not in ids(doing_fine) and "skimming" in ids(doing_fine) and doing_fine["prefs"]["mode"] == "all",
          "a skimmer whose checks go well is told, and nothing changes")
    check("pace_check" not in ids(profiler.build(t, skimmer, (1, 3), {}, set())),
          f"fewer than {profiler.MIN_FIRST_TRIES} first tries: no correction")
    check(not ids(profiler.build(None, {"views": 2, "skim_share": 1.0}, (0, 0), {}, set())),
          f"fewer than {profiler.MIN_VIEWS} views: nothing about reading")

    events = {"velocity": [ev(False, "sure")], "acceleration": [ev(False, "sure"), ev(True, "sure", "2026-10-02T00:00:00+00:00")],
              "displacement": [ev(True, "sure")], "position": [ev(False, "guess")]}
    cal = profiler.build(None, {"views": 0, "skim_share": None}, (0, 0), events, set())
    check("sure_wrong" in ids(cal) and cal["prefs"]["slow_down"], "sure but wrong 2 of 4 times: the slow-down nudge is on")
    check(cal["sooner"] == ["acceleration", "velocity"],
          "sure-but-wrong concepts come back sooner, even after a right answer to the SAME question")
    moved = profiler.build(None, {"views": 0, "skim_share": None}, (0, 0),
                           {**events, "acceleration": [ev(False, "sure"),
                                                       {**ev(True, "sure", "2026-10-02T00:00:00+00:00"), "question": "football"}]}, set())
    check(moved["sooner"] == ["velocity"], "right on a different question counts as fixed")
    check(cal["signals"]["sure"] == 4 and cal["signals"]["sure_wrong"] == 2, "a guess doesn't count as sure")
    calm = profiler.build(None, {"views": 0, "skim_share": None}, (0, 0),
                          {"a": [ev(False, "sure")], "b": [ev(True, "sure")], "c": [ev(True, "sure")], "d": [ev(True, "sure")]}, set())
    check("sure_wrong" not in ids(calm), f"one wrong of four sure answers stays under the threshold")
    hushed = profiler.build(None, {"views": 0, "skim_share": None}, (0, 0), events, {"sure_wrong"})
    check(not hushed["prefs"]["slow_down"] and hushed["sooner"] == [], "dismissed: no nudge and nothing sooner")

    happy = profiler.build(t, {"views": 0, "skim_share": None}, (5, 6), {}, set())
    check("doing_well" in ids(happy), "said physics is stressful, checks going well: 'doing better than you think'")
    check(profiler.INSIGHT_IDS >= {i["id"] for p in (said, corrected, doing_fine, cal, happy) for i in p["insights"]},
          "every insight id is in the list a dismissal is checked against")


# ---------------------------------------------------------------------------
def new_student(name: str | None = None) -> str:
    global _n
    _n += 1
    return api.register_student(name or f"Kid {_n}", f"prof.{_n}", "kid-password-1", "cricket", "Class 11")["student_id"]


def test_boundary() -> None:
    print("\n[2] the profile through the boundary")
    sid = new_student()
    check(api.get_learner_profile(sid) == {"insights": [], "survey_taken": False, "signals": api.get_learner_profile(sid)["signals"]},
          "a new student: nothing to say yet")
    api.submit_survey(sid, FAST_TRY_NERVOUS)
    prof = api.get_learner_profile(sid)
    check(prof["survey_taken"] and "pace_fast" in ids(prof), "after the survey: what they said, as insights")
    lesson = api.get_next_lesson(sid, "motion_straight_line")
    check(lesson["prefs"]["mode"] == "all" and lesson["prefs"]["slow_down"] is False, "the lesson follows the profile")
    after = api.set_insight(sid, "pace_fast", True)
    check(not ids(after)["pace_fast"]["active"], "'that's not me' is saved")
    check(api.get_next_lesson(sid, "motion_straight_line")["prefs"]["mode"] == "steps",
          "and the lesson opens one step at a time")
    api.set_insight(sid, "pace_fast", False)
    check(api.get_next_lesson(sid, "motion_straight_line")["prefs"]["mode"] == "all", "undo brings it back")
    raises(EcoLearnError, api.set_insight, sid, "be_more_like_your_sister", True)
    raises(NotFoundError, api.get_learner_profile, "stu_nobody")


# ---------------------------------------------------------------------------
def test_revision() -> tuple[str, str]:
    print("\n[3] the revision queue")
    sid = new_student()
    qs = diagnostic.choose_questions("Class 11", "cricket", diagnostic.form_for(sid))
    api.submit_diagnostic(sid, {q["concept_id"]: key(q["concept_id"], q["source_interest"])[1] for q in qs})
    # Sure and wrong, then right after the explanation: "partial", and a firm mix-up.
    for concept in ("velocity", "acceleration"):
        api.submit_assessment(sid, concept, key(concept, "cricket")[1], "sure")
        api.submit_assessment(sid, concept, key(concept, "cricket")[0], "sure")
    api.submit_assessment(sid, "displacement", key("displacement", "cricket")[0], "think")
    prof = api.get_learner_profile(sid)
    check("sure_wrong" in ids(prof), "two sure-but-wrong answers: the insight appears")
    queue = api.get_revision(sid)
    items = {i["concept_id"]: i for i in queue["later"] + queue["due"]}
    now = datetime.now(timezone.utc)
    vel = datetime.fromisoformat(items["velocity"]["due_at"]) - now
    dis = datetime.fromisoformat(items["displacement"]["due_at"]) - now
    check(timedelta(hours=9) < vel < timedelta(hours=11) and timedelta(hours=19) < dis < timedelta(hours=21),
          "a concept they were sure about but got wrong comes back in half the time")
    check("sure" in items["velocity"]["reason"] and items["velocity"]["kind"] == "partial", "and says why")
    api.set_insight(sid, "sure_wrong", True)
    queue = api.get_revision(sid)
    vel2 = datetime.fromisoformat(next(i for i in queue["later"] if i["concept_id"] == "velocity")["due_at"]) - now
    check(vel2 > timedelta(hours=19), "with the insight dismissed, it waits the usual time")
    api.set_insight(sid, "sure_wrong", False)

    other = new_student()
    qs = diagnostic.choose_questions("Class 11", "cricket", diagnostic.form_for(other))
    api.submit_diagnostic(other, {q["concept_id"]: key(q["concept_id"], q["source_interest"])[1] for q in qs})
    fresh = [i for i in diagnostic.load_config()["source_interests"] if i != "cricket"]
    api.submit_assessment(other, "position", key("position", "cricket")[0])
    out = api.submit_revision(other, "position", key("position", fresh[0])[0])
    check(out["mastery"]["status"] == "mastered", "two different questions right: mastered")
    item = next(i for i in api.get_revision(other)["later"] if i["concept_id"] == "position")
    wait = datetime.fromisoformat(item["due_at"]) - now
    check(item["kind"] == "refresh" and timedelta(days=20) < wait < timedelta(days=22),
          "mastered after a right revision answer: back in about three weeks to keep it fresh")
    api.submit_revision(other, "position", key("position", fresh[1])[1])
    item = next(i for i in api.get_revision(other)["later"] if i["concept_id"] == "position")
    wait = datetime.fromisoformat(item["due_at"]) - now
    check(timedelta(days=1) < wait < timedelta(days=3) and store.get_progress(other)["position"]["status"] == "mastered",
          "a wrong keep-it-fresh answer brings it back in two days (mastery isn't taken away)")
    return sid, other


# ---------------------------------------------------------------------------
def test_coaching_actions() -> None:
    print("\n[4] coaching actions")
    case = {"lessons_opened": 3, "mix_ups": [{"concept": "Velocity", "sure": False}, {"concept": "Acceleration", "sure": True}]}
    check(coaching_agent.rules_note(case)["action"] == {"type": "revise", "concept": "Acceleration"},
          "a rules note proposes revising the mix-up they were sure about")
    check(coaching_agent.rules_note({"lessons_opened": 0})["action"] == {"type": "check_in"},
          "and a check-in for a student who hasn't started")
    check(coaching_agent.clean_action({"type": "revise", "concept": "Optics"}, case) is None
          and coaching_agent.clean_action({"type": "email_parents"}, case) is None
          and coaching_agent.clean_action({"type": "revise", "concept": "Velocity"}, case)["concept"] == "Velocity",
          "a model's action is kept only if it is a known kind and names a concept from this student's mix-ups")

    teacher = api.create_teacher("Ms. Rao", "rao.prof", "teach-physics-1")
    other = api.create_teacher("Mr. Sen", "sen.prof", "teach-physics-2")
    made = api.create_class(teacher["teacher_id"], "11-P", "Class 11", "cricket", "Aarav Kumar\nMeera Iyer")
    tid, class_id = teacher["teacher_id"], made["class"]["class_id"]
    a, b = (c["student_id"] for c in made["credentials"])
    for sid in (a,):
        qs = diagnostic.choose_questions("Class 11", "cricket", diagnostic.form_for(sid))
        api.submit_diagnostic(sid, {q["concept_id"]: key(q["concept_id"], q["source_interest"])[1] for q in qs})
        api.submit_assessment(sid, "velocity", key("velocity", "cricket")[1], "sure")

    def chat(messages, **_kw):
        text = messages[-1]["content"]
        cases = json.loads(text[text.index("CASE FILES (JSON):\n") + 19:text.index("\n\nWrite the JSON now.")])
        out = {}
        for alias, c in cases.items():
            mix = (c.get("mix_ups") or [{}])[0].get("concept")
            out[alias] = {"note": "Mixed up one idea and was sure about it on the check.",
                          "evidence": [next(iter(c))], "next_step": "Ask them to explain it aloud first.",
                          "action": {"type": "revise", "concept": mix} if mix else {"type": "revise", "concept": "Optics"}}
        return types.SimpleNamespace(text=json.dumps(out), model="stand-in")

    run = api.generate_coaching_notes(tid, class_id, chat=chat)
    notes = {s["student_id"]: s for s in run["students"]}
    check(notes[a]["action"]["type"] == "revise" and notes[a]["action"]["concept_id"] == "velocity",
          "the AI's proposal for a student with a mix-up is kept, with the concept resolved")
    check(notes[b]["action"] is None, "an invented concept is dropped (the note stays)")
    check(run["follow_through"] == {"approved": 0, "done": 0, "right": 0, "came_back": 0, "check_ins": 0},
          "nothing happens until the teacher approves")
    check(not api.get_revision(a)["due"] or all(i["kind"] != "teacher" for i in api.get_revision(a)["due"]),
          "the student's list is untouched before approval")

    raises(NotFoundError, api.apply_coaching_action, other["teacher_id"], class_id, a, "revise", "velocity")
    raises(EcoLearnError, api.apply_coaching_action, tid, class_id, a, "send_email", None)
    raises(EcoLearnError, api.apply_coaching_action, tid, class_id, a, "revise", None)
    raises(NotFoundError, api.apply_coaching_action, tid, class_id, "stu_nobody", "check_in", None)

    done = api.apply_coaching_action(tid, class_id, a, "revise", "velocity")
    check(done["status"] == "waiting" and done["concept_name"], "approved: waiting on the student")
    again = api.apply_coaching_action(tid, class_id, a, "revise", "velocity")
    check(again["action_id"] == done["action_id"], "approving twice doesn't add it twice")
    due = api.get_revision(a)["due"]
    check(due and due[0]["concept_id"] == "velocity" and due[0]["kind"] == "teacher" and "teacher" in due[0]["reason"],
          "it is at the top of the student's revision list, due now, saying the teacher asked")
    q = api.get_revision_question(a, "velocity")
    check(q["question"], "the student gets a question on it")
    interest = api._revision_target(a, "velocity")[1]
    api.submit_revision(a, "velocity", key("velocity", interest)[0])
    view = api.get_coaching_notes(tid, class_id)
    taken = next(s for s in view["students"] if s["student_id"] == a)["actions_taken"]
    check(taken and taken[0]["status"] == "right" and "right" in taken[0]["outcome"], "the outcome is recorded: right")
    check(all(i["kind"] != "teacher" for i in api.get_revision(a)["due"]), "and it leaves the teacher's slot")

    api.apply_coaching_action(tid, class_id, b, "check_in")
    view = api.get_coaching_notes(tid, class_id)
    check(view["follow_through"] == {"approved": 2, "done": 1, "right": 1, "came_back": 0, "check_ins": 1},
          f"follow-through counts (got {view['follow_through']})")
    sb = next(s for s in view["students"] if s["student_id"] == b)
    check(sb["actions_taken"][0]["status"] == "quiet_since", "a check-in shows whether they were active since")

    # HTTP
    c = TestClient(app)
    url = f"/api/teacher/classes/{class_id}/coaching/actions"
    check(c.post(url, json={"student_id": b, "kind": "check_in"}).status_code == 401, "no session -> 401")
    c.post("/api/teacher/login", json={"username": "sen.prof", "password": "teach-physics-2"})
    check(c.post(url, json={"student_id": b, "kind": "check_in"}).status_code == 404, "another teacher -> 404")
    t = TestClient(app)
    t.post("/api/teacher/login", json={"username": "rao.prof", "password": "teach-physics-1"})
    r = t.post(url, json={"student_id": a, "kind": "revise", "concept_id": "acceleration"})
    check(r.status_code == 200 and r.json()["status"] == "waiting", "the class's teacher -> 200")
    check(t.post(url, json={"student_id": a, "kind": "nope"}).status_code == 400, "an unknown kind -> 400")


def test_http() -> None:
    print("\n[5] HTTP: the student's profile")
    api.register_student("Http Kid", "prof.http", "kid-password-1", "cricket", "Class 11")
    c = TestClient(app)
    check(c.get("/api/profile/insights").status_code == 401, "no session -> 401")
    c.post("/api/auth/login", json={"username": "prof.http", "password": "kid-password-1"})
    check(c.get("/api/profile/insights").json()["insights"] == [], "the profile comes back")
    sid = store.get_student_by_username("prof.http")["student_id"]
    api.submit_survey(sid, FAST_TRY_NERVOUS)
    r = c.post("/api/profile/insights/gentle", json={"dismissed": True})
    check(r.status_code == 200 and not ids(r.json())["gentle"]["active"], "'that's not me' over HTTP")
    check(c.post("/api/profile/insights/made_up", json={"dismissed": True}).status_code == 400, "an unknown insight -> 400")


def main() -> None:
    test_rules()
    test_boundary()
    test_revision()
    test_coaching_actions()
    test_http()
    print(f"\nAll {_checks} learner-profile checks passed.")


if __name__ == "__main__":
    main()
