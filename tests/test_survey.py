"""The "getting to know you" survey (2026-10-08).

No LLM calls. Proves:

  1. The question bank is well formed (unique ids, every section used, unique option ids).
  2. Validation: every question skippable and an empty submission is fine; unknown questions,
     unknown options, too many choices and per-hobby answers for a hobby outside the first two
     are errors, never silently dropped.
  3. Traits: hobby level (novice/fan/player/expert), focus span, and the lesson preferences
     and story notes they lead to.
  4. Storage: taken once (second submit is a conflict), the hobbies it collected reach the
     learner profile, and the starting check still keeps them.
  5. Where it shows: the lesson envelope carries the preferences (defaults before the survey),
     the story writer's prompt carries coarse notes, the closest hobby is tried first.
  7. Updating: replaces the answers (and hobbies and traits), keeps the old set in a history the
     teacher never sees, refuses bad input without changing anything, and needs a first survey.
  6. HTTP: needs a student session; bad answers are 400; a repeat is 409; the teacher endpoint
     needs a teacher who owns the class and shows observed reading next to what was said.

Run: venv\\Scripts\\python.exe tests\\test_survey.py
"""

from __future__ import annotations

import os
import sys
import tempfile
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(_ROOT / "apps"))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_survey_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "survey.db")
# The survey's own preferences are tested here. With the pilot experiment on, each new student gets a random
# arm that can turn slow_down on, and the "default preferences" check failed about 1 run in 3.
# Experiments are tested in test_pilot_experiment.py.
os.environ["ECOLEARN_EXPERIMENTS"] = "off"
os.environ["LLM_MODEL"] = ""
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from ecolearn import platform_api as api  # noqa: E402
from ecolearn.errors import ConflictError, EcoLearnError, NotFoundError  # noqa: E402
from ecolearn.learner import personal_story as ps  # noqa: E402
from ecolearn.learner import survey  # noqa: E402
from ecolearn.path import engine  # noqa: E402
from ecolearn.progress import store  # noqa: E402

_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


def raises(exc_type, fn, *args, **kwargs) -> Exception:
    try:
        fn(*args, **kwargs)
    except exc_type as exc:
        return exc
    raise AssertionError(f"FAIL: expected {exc_type.__name__} from {fn.__name__}")


def new_student(name: str, username: str) -> str:
    return api.register_student(name, username, "kid-password-1", "cricket", "Class 11")["student_id"]


FULL = {
    "hobbies": ["badminton", "music"],
    "hobby_depth": {"badminton": "watch"},
    "hobby_know": {"badminton": ["rules"]},
    "first_step": "try", "pace": "fast", "session_length": "m5", "focus_drift": "often",
    "distractions": ["phone", "tired"], "physics_feel": "nervous", "maths_comfort": "shaky",
    "trips": "formulas", "goal": "pass",
}


def test_bank() -> None:
    print("\n[1] the question bank")
    qs = survey.questions()
    ids = [q["id"] for q in qs]
    check(len(ids) == len(set(ids)), "question ids are unique")
    check({q["section"] for q in qs} == {s["id"] for s in survey.sections()}, "every section has a question")
    check(all(len({o["id"] for o in q.get("options", [])}) == len(q.get("options", [])) for q in qs),
          "option ids are unique within a question")
    check(all(q["type"] in {"hobbies", "hobby_single", "hobby_multi", "single", "multi"} for q in qs),
          "only types the web app can draw")


def test_validation() -> None:
    print("\n[2] validation")
    check(survey.clean({}) == {} and survey.clean(None) == {}, "an empty submission is allowed")
    cleaned = survey.clean(FULL)
    check(cleaned["hobbies"] == ["badminton", "music"] and cleaned["pace"] == "fast", "a full submission is kept")
    check(survey.clean({"pace": ""}) == {}, "an empty answer counts as skipped")
    raises(EcoLearnError, survey.clean, {"favourite_colour": "red"})
    raises(EcoLearnError, survey.clean, {"pace": "warp"})
    raises(EcoLearnError, survey.clean, {"distractions": ["phone", "noise", "tired", "bored"]})  # max 3
    raises(EcoLearnError, survey.clean, {"distractions": ["phone", "phone"]})
    raises(EcoLearnError, survey.clean, {"hobbies": ["badminton"], "hobby_depth": {"music": "watch"}})
    raises(EcoLearnError, survey.clean, {"hobbies": ["a hobby that is far too long to be a label"]})
    raises(EcoLearnError, survey.clean, {"distractions": "phone"})  # a list is required


def test_traits() -> None:
    print("\n[3] traits and what they change")
    check(survey.hobby_level(0, 0) == "novice" and survey.hobby_level(0, 1) == "novice", "watching, explains little: novice")
    check(survey.hobby_level(1, 0) == "fan" and survey.hobby_level(0, 3) == "fan", "follows it or can explain a lot: fan")
    check(survey.hobby_level(2, 0) == "player" and survey.hobby_level(3, 1) == "player", "plays: player")
    check(survey.hobby_level(4, 0) == "expert" and survey.hobby_level(3, 4) == "expert", "competes, or plays and explains: expert")
    check(survey.focus_span(5, "often") == "short" and survey.focus_span(10, "often") == "short", "short span, wandering: short")
    check(survey.focus_span(30, "stays") == "long" and survey.focus_span(20, "stays") == "long", "long span, focused: long")
    check(survey.focus_span(10, "some") == "medium" and survey.focus_span(None, None) == "medium", "in between / unknown: medium")

    traits = survey.derive_traits(survey.clean(FULL))
    check(traits["hobby_levels"]["badminton"]["level"] == "novice", "badminton: novice")
    check(traits["focus"]["span"] == "short", "focus: short")
    prefs = survey.lesson_prefs(traits)
    check(prefs == {"mode": "all", "break_after_minutes": 5, "example_first": True, "gentle": True}, f"prefs: {prefs}")
    check(survey.lesson_prefs(None) == survey.DEFAULT_PREFS, "no survey: the lesson page is exactly as before")
    check(survey.lesson_prefs(survey.derive_traits(survey.clean({"session_length": "m30", "focus_drift": "stays"})))
          ["break_after_minutes"] is None, "a long focuser gets no break nudge")
    check(any("Badminton" in line for line in traits["summary"]), "the teacher's summary names the hobby")

    notes = survey.story_notes(traits, "badminton")
    check(any("new to the hobby" in n for n in notes) and any("stressful" in n for n in notes)
          and any("loses focus" in n for n in notes), f"story notes: {notes}")
    check(survey.story_notes(None, "badminton") == [], "no survey: no notes")
    expert = survey.derive_traits(survey.clean({"hobbies": ["music", "badminton"],
                                                "hobby_depth": {"music": "watch", "badminton": "compete"}}))
    check(survey.order_hobbies(["music", "badminton"], expert) == ["badminton", "music"], "the closest hobby goes first")
    check(survey.order_hobbies(["a", "b"], None) == ["a", "b"], "no survey: order unchanged")
    check(survey.observed_reading([{"active_seconds": 100}]) ["median_minutes"] is None, "under three views: no verdict")
    seen = survey.observed_reading([{"active_seconds": 10}, {"active_seconds": 20}, {"active_seconds": 300}])
    check(seen["median_minutes"] == 0.3 and seen["skim_share"] == 0.67, f"observed reading: {seen}")


def test_storage_and_surfaces() -> None:
    print("\n[4][5] storage and where it shows")
    sid = new_student("Sv Kid", "sv.kid")
    first = engine.get_roadmap(sid, "laws_of_motion")[0]["concept_id"]
    before = api.get_next_lesson(sid, "laws_of_motion")
    check(before["prefs"] == {**survey.DEFAULT_PREFS, "slow_down": False},
          "before the survey: default preferences (plus the profile's slow_down, off)")
    check(api.get_survey(sid)["taken"] is False and len(api.get_survey(sid)["questions"]) == len(survey.questions()),
          "not taken: the questions come back")

    out = api.submit_survey(sid, FULL)
    check(out["taken"] and out["traits"]["focus"]["span"] == "short", "taken, with traits")
    check(store.get_learner_profile(sid)["hobbies"] == ["badminton", "music"], "the hobbies reached the learner profile")
    raises(ConflictError, api.submit_survey, sid, {})
    after = api.get_next_lesson(sid, "laws_of_motion")
    check(after["prefs"]["mode"] == "all" and after["prefs"]["gentle"], "the lesson envelope carries the preferences")

    # the starting check keeps the hobbies the survey collected
    check(store.get_survey(sid)["answers"]["pace"] == "fast", "answers stored")
    ctx = ps._context(sid, first)
    check(ctx is not None and ctx["hobby"]["id"] == "badminton", "the story is built on a hobby that fits")
    check(any("new to the hobby" in n for n in ctx["notes"]), "with notes for the writer")
    prompt = ps.writer_messages(ctx)[0]["content"]
    check("Note: This student is new to the hobby" in prompt, "the writer's prompt carries the note")
    check("fast" not in prompt.split("Note:")[1], "and only coarse notes, never the raw answers")
    plain = new_student("Plain Kid", "plain.kid")
    store.save_diagnostic(plain, ["badminton"], [])
    check(ps._context(plain, first)["notes"] == [], "no survey: no notes, the prompt is as before")

    raises(NotFoundError, api.get_survey, "stu_nope")


def test_http() -> None:
    print("\n[6] HTTP")
    check(TestClient(app).get("/api/survey").status_code == 401, "needs a student session")
    teacher = api.create_teacher("Ms. Sv", "sv.teacher", "teacher-password-1")
    other = api.create_teacher("Mr. Other", "other.sv", "teacher-password-1")
    made = api.create_class(teacher["teacher_id"], "11-S", "Class 11", "cricket", "Mia Roy\nNeil Das")
    class_id = made["class"]["class_id"]
    mia = next(c for c in made["credentials"] if c["name"] == "Mia Roy")

    client = TestClient(app)
    r = client.post("/api/auth/login", json={"username": mia["username"], "password": mia["password"]})
    check(r.status_code == 200, "a class student logs in")
    r = client.get("/api/survey")
    check(r.status_code == 200 and r.json()["taken"] is False and r.json()["questions"], "GET: the questions")
    check(client.post("/api/survey", json={"answers": {"pace": "warp"}}).status_code == 400, "a bad option is a 400")
    r = client.post("/api/survey", json={"answers": FULL})
    check(r.status_code == 200 and r.json()["taken"] and r.json()["traits"]["summary"], "POST stores it")
    check(client.post("/api/survey", json={"answers": {}}).status_code == 409, "a repeat is a 409")

    # observed reading beside what they said: three short views
    for i in range(3):
        view = store.create_lesson_view(f"view_t{i}", mia["student_id"], "second_law", "cricket")
        store.set_lesson_view_seconds(view["view_id"], 12 + i)

    t_http = TestClient(app)
    check(t_http.post("/api/teacher/login", json={"username": "sv.teacher", "password": "teacher-password-1"}).status_code == 200,
          "teacher logs in")
    r = t_http.get(f"/api/teacher/classes/{class_id}/profiles")
    body = r.json()
    check(r.status_code == 200 and body["summary"]["taken"] == 1 and body["summary"]["total"] == 2, "class summary: 1 of 2 answered")
    rows = {s["name"]: s for s in body["students"]}
    check(rows["Mia Roy"]["taken"] and rows["Mia Roy"]["focus_span"] == "short", "Mia's profile is there")
    check(rows["Mia Roy"]["observed"]["skim_share"] == 1.0, "and what her views show: all three skimmed")
    check(rows["Neil Das"]["taken"] is False and rows["Neil Das"]["summary"] == [], "Neil hasn't answered")
    check("traits" not in rows["Mia Roy"] and "answers" not in rows["Mia Roy"], "the teacher gets summary lines, not raw answers")
    check(client.get(f"/api/teacher/classes/{class_id}/profiles").status_code == 401, "a student can't read it")
    raises(NotFoundError, api.get_class_learner_profiles, other["teacher_id"], class_id)


def test_update() -> None:
    print("\n[7] updating your answers")
    sid = new_student("Up Kid", "up.kid")
    raises(EcoLearnError, api.update_survey, sid, {"pace": "fast"})  # answer first
    api.submit_survey(sid, {"hobbies": ["badminton"], "session_length": "m5", "focus_drift": "often",
                            "physics_feel": "nervous"})
    first = store.get_survey(sid)
    check(first["revision"] == 0 and first["updated_at"] is None, "a fresh survey is revision 0, never updated")

    out = api.update_survey(sid, {"hobbies": ["music", "cricket"], "hobby_depth": {"music": "compete"},
                                  "session_length": "m30", "focus_drift": "stays"})
    check(out["revision"] == 1 and out["updated_at"], "the update bumps the revision and stamps the time")
    check(out["traits"]["focus"]["span"] == "long", "the traits follow the new answers")
    check(out["answers"]["hobbies"] == ["music", "cricket"] and "physics_feel" not in out["answers"],
          "the new set REPLACES the old (skipped now means skipped)")
    check(store.get_learner_profile(sid)["hobbies"] == ["music", "cricket"], "the hobbies follow")
    check(store.get_survey(sid)["completed_at"] == first["completed_at"], "completed_at stays the first time")
    history = store.get_survey_history(sid)
    check(len(history) == 1 and history[0]["answers"]["hobbies"] == ["badminton"]
          and history[0]["traits"]["focus"]["span"] == "short", "the old answers are kept in the history")

    raises(EcoLearnError, api.update_survey, sid, {"pace": "warp"})
    raises(EcoLearnError, api.update_survey, sid, {"hobbies": ["music"], "hobby_depth": {"cricket": "watch"}})
    check(api.get_survey(sid)["revision"] == 1 and len(store.get_survey_history(sid)) == 1,
          "a refused update changes nothing")
    api.update_survey(sid, {})
    check(store.get_learner_profile(sid)["hobbies"] == [] and api.get_survey(sid)["revision"] == 2,
          "an empty update clears the hobbies (their choice) and is recorded as another revision")
    check(len(store.get_survey_history(sid)) == 2, "two earlier sets are in the history")
    check(api.get_survey(sid)["questions"], "the questions are still sent once taken (the edit form needs them)")

    # HTTP
    client = TestClient(app)
    check(client.put("/api/survey", json={"answers": {}}).status_code == 401, "PUT needs a session")
    made = api.create_class(api.create_teacher("Ms. Up", "up.teacher", "teacher-password-1")["teacher_id"],
                            "11-U", "Class 11", "cricket", "Zed Ali")
    zed = made["credentials"][0]
    check(client.post("/api/auth/login", json={"username": zed["username"], "password": zed["password"]}).status_code == 200,
          "a class student logs in")
    check(client.put("/api/survey", json={"answers": {"pace": "fast"}}).status_code == 400, "PUT before the first answers is a 400")
    check(client.post("/api/survey", json={"answers": {"pace": "steady"}}).status_code == 200, "first answers")
    r = client.put("/api/survey", json={"answers": {"pace": "fast", "session_length": "m10"}})
    check(r.status_code == 200 and r.json()["revision"] == 1 and r.json()["answers"]["pace"] == "fast", "PUT replaces them")
    check(client.put("/api/survey", json={"answers": {"pace": "warp"}}).status_code == 400, "a bad option is a 400")
    r = client.get("/api/survey")
    check(r.json()["answers"]["pace"] == "fast", "GET returns the answers to prefill a form")

    t_http = TestClient(app)
    t_http.post("/api/teacher/login", json={"username": "up.teacher", "password": "teacher-password-1"})
    rows = {x["name"]: x for x in t_http.get(f"/api/teacher/classes/{made['class']['class_id']}/profiles").json()["students"]}
    check(rows["Zed Ali"]["updated_at"], "the teacher sees THAT they updated, and the current answers only")
    check("history" not in str(rows["Zed Ali"]).lower(), "never the history")


def main() -> None:
    test_bank()
    test_validation()
    test_traits()
    test_storage_and_surfaces()
    test_http()
    test_update()
    print(f"\nAll {_checks} survey checks passed.")


if __name__ == "__main__":
    main()
