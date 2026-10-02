"""Personalisation layers 1 and 2: the starting check and the learning plan.

No LLM calls. Proves:

  1. The question set (data/diagnostic.yaml) is valid for every in-scope
     interest and both classes: every concept exists, every question comes
     from a DIFFERENT interest's lesson, and the browser never sees an answer
     key or a misconception.
  2. Grading: right, wrong (with its misconception), "not sure", and a
     missing answer counts as not sure; answers for concepts not in the check
     and invalid options are refused; the check can be taken once.
  3. Hobbies: listed ones, up to two short ones of the student's own; a
     sentence, too many of their own, or too many overall are refused.
  4. The plan: likely-known concepts, open mix-ups (first sentence only, in
     the second person), and a starting chapter, preferring the student's own
     class.
  5. Recommendations: skip what the check says they know; brush up a
     prerequisite with a mix-up first; flag a mix-up on the concept itself; a
     cleared concept's mix-up is closed; and a student with no check gets
     exactly the engine's recommendation, wording included.
  6. The roadmap marks known / focus concepts and exactly one recommended one.
  7. HTTP: the endpoints need a student session, a second submit is 409, and
     the pilot report carries the starting check pseudonymised.

Run: venv\\Scripts\\python.exe tests\\test_learner_plan.py
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_learner_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "learner.db")
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from src import platform_api as api  # noqa: E402
from src.content import lesson_service  # noqa: E402
from src.curriculum.scope import scope_interest_ids  # noqa: E402
from src.errors import ConflictError, EcoLearnError  # noqa: E402
from src.learner import diagnostic, plan  # noqa: E402
from src.path import engine  # noqa: E402
from src.progress import store  # noqa: E402

_checks = 0
_n = 0


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


def new_student(interest: str = "cricket", level: str = "Class 11") -> str:
    global _n
    _n += 1
    return api.register_student(f"Kid {_n}", f"kid.{_n}", "kid-password-1", interest, level)["student_id"]


def key(concept_id: str, source: str):
    c = lesson_service.get_authored_lesson(concept_id, source).check
    return c.answer, next(o for o in c.options if o != c.answer), c


def diag_row(concept_id: str, correct: bool | None, misconception: str | None = None) -> dict:
    return {"concept_id": concept_id, "source_interest": "football",
            "selected": "unsure" if correct is None else ("A" if correct else "B"),
            "correct": correct, "misconception": misconception}


# ---------------------------------------------------------------------------
def test_question_set() -> None:
    print("\n[1] the question set")
    config = diagnostic.load_config()
    for level, ids in config["questions"].items():
        check(all(engine.find_concept(c) is not None for c in ids), f"{level}: every concept exists")
        for interest in scope_interest_ids():
            for form in (0, 1):
                chosen = diagnostic.choose_questions(level, interest, form)
                check(len(chosen) == len(ids) and all(q["source_interest"] != interest for q in chosen),
                      f"{level} × {interest} form {form}: all {len(ids)} questions, each from another interest")
    qs = diagnostic.student_questions("Class 11", "cricket")
    text = json.dumps(qs)
    _, _, c = key(qs[0]["concept_id"], "football")
    check(all(set(q) == {"concept_id", "concept_name", "chapter_name", "question", "options"} for q in qs)
          and c.explanation.strip()[:30] not in text
          and all(m.strip()[:30] not in text for m in c.misconceptions.values()),
          "the browser gets question and options only: no key, explanation or misconception")
    orders = [engine.find_concept(q["concept_id"]).order for q in qs]
    check(orders == sorted(orders), "questions come in teaching order")


def test_grading_and_once() -> None:
    print("\n[2] grading")
    sid = new_student()
    qs = diagnostic.choose_questions("Class 11", "cricket", diagnostic.form_for(sid))
    a, b, c3 = qs[0], qs[1], qs[2]
    right, _, _ = key(a["concept_id"], a["source_interest"])
    _, wrong, check_b = key(b["concept_id"], b["source_interest"])
    raises(EcoLearnError, api.submit_diagnostic, sid, {"ohms_law": "A"})
    raises(EcoLearnError, api.submit_diagnostic, sid, {a["concept_id"]: "Z"})
    check(store.get_learner_profile(sid)["diagnostic_completed_at"] is None,
          "refused submissions store nothing")
    out = api.submit_diagnostic(sid, {a["concept_id"]: right, b["concept_id"]: wrong,
                                      c3["concept_id"]: "unsure"})
    rows = {r["concept_id"]: r for r in store.get_diagnostic_answers([sid])}
    check(rows[a["concept_id"]]["correct"] is True, "right → correct")
    check(rows[b["concept_id"]]["correct"] is False
          and rows[b["concept_id"]]["misconception"] == check_b.misconceptions[wrong].strip(),
          "wrong → its option's misconception")
    check(rows[c3["concept_id"]]["correct"] is None and rows[c3["concept_id"]]["selected"] == "unsure",
          "'not sure' is stored as such")
    check(out["result"] == {"asked": len(qs), "known": 1, "mix_ups": 1, "unsure": len(qs) - 2},
          "unanswered questions count as not sure")
    raises(ConflictError, api.submit_diagnostic, sid, {})
    taken = api.get_diagnostic(sid)
    check(taken["taken"] and "questions" not in taken and taken["result"]["known"] == 1,
          "once taken: the result, no questions, and no second go")


def test_hobbies() -> None:
    print("\n[3] hobbies")
    check(diagnostic.clean_hobbies(["cricket", "badminton", " Kite flying ", "cricket"])
          == ["cricket", "badminton", "kite flying"], "listed ones + an own label, deduplicated")
    raises(EcoLearnError, diagnostic.clean_hobbies, ["I live at 12 Park Street, Pune"])
    raises(EcoLearnError, diagnostic.clean_hobbies, ["chess", "kites", "origami"])
    raises(EcoLearnError, diagnostic.clean_hobbies,
           ["cricket", "football", "badminton", "basketball", "kabaddi", "athletics",
            "swimming", "cycling", "gaming"])


def test_plan() -> None:
    print("\n[4] the learning plan")
    sid = new_student()
    qs = diagnostic.choose_questions("Class 11", "cricket", diagnostic.form_for(sid))
    picks = {}
    for i, q in enumerate(qs):
        right, wrong, _ = key(q["concept_id"], q["source_interest"])
        picks[q["concept_id"]] = right if i < 2 else (wrong if q["concept_id"] in
                                                       ("projectile_motion", "third_law") else "unsure")
    result = api.submit_diagnostic(sid, picks, ["cricket"])
    p = result["plan"]
    check([k["concept_id"] for k in p["known"]] == [qs[0]["concept_id"], qs[1]["concept_id"]],
          "the two right answers are 'likely known'")
    check([f["concept_id"] for f in p["focus"]] == ["projectile_motion", "third_law"],
          "the two wrong answers are focus items, in teaching order")
    note = p["focus"][0]["note"]
    check(note.startswith("You might") and note.count(". ") == 0,
          f"notes speak to the student and stop at the mix-up: {note!r}")
    check(p["start"]["chapter_id"] == "motion_plane", "start where the first mix-up is")
    check(p["hobbies"] == ["cricket"] and p["check"]["taken"], "hobbies and check status included")

    sid12 = new_student("football", "Class 12")
    qs12 = diagnostic.choose_questions("Class 12", "football", diagnostic.form_for(sid12))
    picks = {}
    for q in qs12:
        right, wrong, _ = key(q["concept_id"], q["source_interest"])
        picks[q["concept_id"]] = wrong if q["concept_id"] in ("second_law", "lenzs_law") else right
    p12 = api.submit_diagnostic(sid12, picks)["plan"]
    check({f["concept_id"] for f in p12["focus"]} == {"second_law", "lenzs_law"},
          "a Class 12 student's Class 11 foundation mix-up is a focus item too")
    check(p12["start"]["chapter_id"] == "electromagnetic_induction",
          "but the suggested start stays in their own class")

    fresh = api.get_learning_plan(new_student())
    check(not fresh["check"]["taken"] and fresh["focus"] == [] and fresh["start"]["chapter_id"]
          == "units_measurement", "no check yet: no focus, start at the first chapter")


def test_recommendations() -> None:
    print("\n[5] recommendations")
    sid = new_student()
    engine_says = engine.next_concept(sid, "laws_of_motion")
    got = api.get_next_lesson(sid, "laws_of_motion")
    check(got["concept_id"] == engine_says.concept.id and got["reason"] == engine_says.reason,
          "no check: exactly the engine's pick and wording")

    store.save_diagnostic(sid, [], [diag_row("position", True), diag_row("distance", True)])
    got = api.get_next_lesson(sid, "motion_straight_line")
    check(got["concept_id"] == "displacement" and "already know Position, Distance" in got["reason"],
          "skips the two concepts the check says they know, and says so")

    sid = new_student()
    first_law = engine.find_concept("inertia_first_law")
    check("velocity" in first_law.prerequisites, "(fixture: inertia_first_law builds on velocity)")
    store.save_diagnostic(sid, [], [diag_row("velocity", False, "Thinks velocity is just speed. It has a direction.")])
    got = api.get_next_lesson(sid, "laws_of_motion")
    check(got["concept_id"] == "velocity" and got["reason"].startswith("Before Inertia")
          and "You might think velocity is just speed." in got["reason"]
          and "It has a direction" not in got["reason"],
          "a prerequisite with a mix-up is brushed up first, across chapters")
    check(got["lesson"] is not None, "and its lesson is served")

    store.update_progress(sid, "velocity", 3)
    got = api.get_next_lesson(sid, "laws_of_motion")
    check(got["concept_id"] == "inertia_first_law", "once velocity is cleared, the mix-up is closed")

    sid = new_student()
    right, wrong, c = key("inertia_first_law", "cricket")
    api.submit_assessment(sid, "inertia_first_law", wrong)
    state = plan.learner_state(sid)
    check(state["mix_ups"]["inertia_first_law"]["source"] == "lesson",
          "a wrong lesson answer opens a mix-up too")
    got = api.get_next_lesson(sid, "laws_of_motion")
    check(got["concept_id"] == "inertia_first_law" and "Your answer in this lesson" in got["reason"],
          "and the recommendation names it")
    api.submit_assessment(sid, "inertia_first_law", right)
    check("inertia_first_law" not in plan.learner_state(sid)["mix_ups"], "answering right closes it")


def test_roadmap() -> None:
    print("\n[6] roadmap annotations")
    sid = new_student()
    store.save_diagnostic(sid, [], [diag_row("position", True),
                                    diag_row("displacement", False, "Thinks displacement is distance.")])
    rows = {r["concept_id"]: r for r in api.get_roadmap(sid, "motion_straight_line")}
    check(rows["position"]["personal"] == "known" and rows["displacement"]["personal"] == "focus",
          "known and focus concepts are marked")
    check(rows["displacement"]["personal_note"] == "You might think displacement is distance.",
          "with a student-facing note")
    recommended = [c for c, r in rows.items() if r["recommended"]]
    check(recommended == ["distance"], f"exactly one recommended concept (got {recommended})")


def test_http() -> None:
    print("\n[7] HTTP and the pilot report")
    client = TestClient(app)
    check(client.get("/api/diagnostic").status_code == 401, "no session → 401")
    api.register_student("Web Kid", "web.learner", "kid-password-1", "gaming", "Class 11")
    client.post("/api/auth/login", json={"username": "web.learner", "password": "kid-password-1"})
    r = client.get("/api/diagnostic")
    body = r.json()
    check(r.status_code == 200 and len(body["questions"]) == 8 and len(body["hobby_options"]) >= 10,
          "GET → 8 questions and the hobby list")
    check('"answer"' not in r.text and "misconception" not in r.text, "no key in the response")
    first = body["questions"][0]["concept_id"]
    r = client.post("/api/diagnostic", json={"answers": {first: "unsure"}, "hobbies": ["gaming"]})
    check(r.status_code == 200 and r.json()["result"]["unsure"] == 8 and "plan" in r.json(),
          "POST → result and plan")
    check(client.post("/api/diagnostic", json={"answers": {}}).status_code == 409, "again → 409")
    check(client.get("/api/learning-plan").json()["check"]["taken"] is True, "GET /api/learning-plan")

    report = api.pilot_report()
    check(len(report["diagnostic"]) > 0 and all(r["student_id"].startswith("S")
                                                for r in report["diagnostic"])
          and "stu_" not in json.dumps(report["diagnostic"]),
          "the pilot report carries the starting check, pseudonymised")


def main() -> None:
    test_question_set()
    test_grading_and_once()
    test_hobbies()
    test_plan()
    test_recommendations()
    test_roadmap()
    test_http()
    print(f"\nAll {_checks} learner-plan checks passed.")


if __name__ == "__main__":
    main()
