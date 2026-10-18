"""Mastery from evidence, and the revision queue (2026-10-03).

No LLM calls. Proves:

  1. mastery_evidence: a right answer to a question not failed first counts;
     right after being shown the answer doesn't; two different questions make
     two pieces of evidence.
  2. Lesson checks: a first right answer clears the concept (score 2, the path
     moves on) but doesn't master it; right after a wrong pick on the same
     question is cleared too, with a different note; the starting check plus a
     first-try lesson answer (two different questions) masters it.
  3. The revision queue: cleared concepts, due after ECOLEARN_REVISION_HOURS,
     each with a question the student has never seen (no answer key sent).
  4. A right revision answer masters the concept and empties the queue; a
     wrong one keeps it cleared, opens a mix-up "found in review", and the next
     revision question is a different one again; when no unseen question is
     left the concept is counted, not offered.
  5. Revision answers stay out of the lesson metrics (first-try accuracy).
  6. HTTP: the endpoints need a session; 404 for a concept not in the queue;
     400 for a bad option or confidence.

Run: venv\\Scripts\\python.exe tests\\test_mastery.py
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

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_mastery_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "mastery.db")
os.environ["ECOLEARN_REVISION_HOURS"] = "20"
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api.main import app  # noqa: E402
from src import platform_api as api  # noqa: E402
from src.content import lesson_service  # noqa: E402
from src.errors import EcoLearnError, NotFoundError  # noqa: E402
from src.learner import diagnostic, plan  # noqa: E402
from src.progress import metrics, store  # noqa: E402

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


def new_student(interest: str = "cricket") -> str:
    global _n
    _n += 1
    return api.register_student(f"Kid {_n}", f"mast.{_n}", "kid-password-1", interest,
                                "Class 11")["student_id"]


def key(concept_id: str, interest: str) -> tuple[str, str]:
    c = lesson_service.get_authored_lesson(concept_id, interest).check
    return c.answer, next(o for o in c.options if o != c.answer)


def ev(question: str, correct: bool, at: str) -> dict:
    return {"question": question, "correct": correct, "at": at}


# ---------------------------------------------------------------------------
def test_evidence() -> None:
    print("\n[1] mastery_evidence")
    check(plan.mastery_evidence([ev("cricket", True, "t1")]) == {"cricket"}, "a fresh right answer counts")
    check(plan.mastery_evidence([ev("cricket", False, "t1"), ev("cricket", True, "t2")]) == set(),
          "right after being shown the answer doesn't")
    check(plan.mastery_evidence([ev("football", True, "t1"), ev("cricket", True, "t2")])
          == {"football", "cricket"}, "two different questions: two pieces")
    check(plan.mastery_evidence([ev("a", False, "t1"), ev("b", True, "t2"), ev("a", True, "t3")]) == {"b"},
          "only the question not failed first counts")
    check(plan.MASTERY_EVIDENCE == 2, "two pieces make 'mastered'")


def test_lesson_checks() -> tuple[str, str]:
    print("\n[2] lesson checks")
    sid = new_student()
    right, wrong = key("displacement", "cricket")
    out = api.submit_assessment(sid, "displacement", right)
    check(out["score"] == 2 and out["mastery_signal"] == "partial" and out["mastery"]["status"] == "partial",
          "a first right answer clears the concept, but doesn't master it")
    check("One more right answer" in out["mastery_note"], "the note says how to master it")
    check("displacement" in store.get_cleared_concepts(sid), "cleared: the path engine moves on")

    right2, wrong2 = key("velocity", "cricket")
    api.submit_assessment(sid, "velocity", wrong2)
    out = api.submit_assessment(sid, "velocity", right2)
    check(out["score"] == 2 and "now that you've seen why" in out["mastery_note"],
          "right after a wrong pick: cleared, with a different note")

    other = new_student()
    chosen = diagnostic.choose_questions("Class 11", "cricket", diagnostic.form_for(other))
    q = next(c for c in chosen if c["concept_id"] == "acceleration")
    api.submit_diagnostic(other, {q["concept_id"]: key("acceleration", q["source_interest"])[0]})
    out = api.submit_assessment(other, "acceleration", key("acceleration", "cricket")[0])
    check(out["score"] == 3 and out["mastery"]["status"] == "mastered" and "mastered" in out["mastery_note"],
          "starting check + lesson check (two different questions) = mastered")
    queue = api.get_revision(other)
    check(all(i["concept_id"] != "acceleration" for i in queue["due"]),
          "a mastered concept isn't due for revision")
    fresh = [i for i in queue["later"] if i["concept_id"] == "acceleration"]
    check(len(fresh) == 1 and fresh[0]["kind"] == "refresh",
          "it comes back later only as a keep-it-fresh question (2026-10-14)")
    return sid, other


def test_queue(sid: str) -> None:
    print("\n[3] the revision queue")
    queue = api.get_revision(sid)
    ids = {i["concept_id"] for i in queue["later"]}
    check(queue["due"] == [] and ids == {"displacement", "velocity"},
          "both cleared concepts are queued, not due yet (20 h)")
    item = next(i for i in queue["later"] if i["concept_id"] == "displacement")
    check(item["concept_name"] == "Displacement" and item["chapter_name"] and not item["due"]
          and "One more" in item["reason"], "names, a reason and a due time")
    os.environ["ECOLEARN_REVISION_HOURS"] = "0"
    check({i["concept_id"] for i in api.get_revision(sid)["due"]} == {"displacement", "velocity"},
          "after the wait, they're due")
    q = api.get_revision_question(sid, "displacement")
    served = json.dumps(q)
    first_fresh = next(i for i in diagnostic.load_config()["source_interests"] if i != "cricket")
    lesson = lesson_service.get_authored_lesson("displacement", first_fresh)
    check(q["question"] == lesson_service.student_view(lesson)["check"]["question"],
          "the question is another interest's check, never seen before")
    check(set(q) == {"concept_id", "concept_name", "chapter_name", "question", "options"}
          and lesson.check.explanation.strip()[:30] not in served, "no answer key or explanation sent")


def test_revision_answers(sid: str) -> None:
    print("\n[4] answering revision questions")
    first_fresh = next(i for i in diagnostic.load_config()["source_interests"] if i != "cricket")
    right, _ = key("displacement", first_fresh)
    out = api.submit_revision(sid, "displacement", right, "sure")
    check(out["correct"] and out["mastery"]["status"] == "mastered" and out["mastery_signal"] == "mastered",
          "right on a fresh question: mastered")
    check(all(i["concept_id"] != "displacement" for i in api.get_revision(sid)["due"]),
          "and it leaves the due list")
    later = [i for i in api.get_revision(sid)["later"] if i["concept_id"] == "displacement"]
    check(later and later[0]["kind"] == "refresh" and api.get_revision_question(sid, "displacement")["question"],
          "it waits as a keep-it-fresh question, which can still be tried early (nothing is locked)")

    fresh = []
    for _ in range(5):
        try:
            q = api.get_revision_question(sid, "velocity")
        except NotFoundError:
            break
        interest = next(i for i in diagnostic.load_config()["source_interests"]
                        if lesson_service.student_view(lesson_service.get_authored_lesson("velocity", i))
                        ["check"]["question"] == q["question"])
        fresh.append(interest)
        _, wrong = key("velocity", interest)
        out = api.submit_revision(sid, "velocity", wrong)
        check(not out["correct"] and out["mastery"]["status"] == "partial" and "mix-ups" in out["mastery_note"],
              f"wrong on {interest}: still cleared, and a note about mix-ups")
    check(len(fresh) == len(set(fresh)) and "cricket" not in fresh,
          f"every revision question was new ({', '.join(fresh)})")
    queue = api.get_revision(sid)
    check(all(i["concept_id"] != "velocity" for i in queue["due"] + queue["later"])
          and queue["no_fresh_question"] == 1, "no unseen question left: counted, not offered")
    mix = {m["concept_id"]: m for m in api.get_mix_ups(sid)["items"]}
    check(mix["velocity"]["status"] == "active" and mix["velocity"]["times"] == 1 + len(fresh),
          "the wrong revision answers show on the mix-ups page")



def test_metrics_untouched(sid: str) -> None:
    print("\n[5] revision answers stay out of the lesson metrics")
    students = [{"student_id": sid, "name": "Kid"}]
    out = metrics.class_insights(students, store.get_activity([sid]), lambda c: {"name": c},
                                 lambda c, i: None)
    check(out["summary"]["answers"] == 3 and out["summary"]["first_try_answers"] == 2,
          "lesson answers: 3 (1 + 2), first tries: 2; revision answers not mixed in")


def test_http() -> None:
    print("\n[6] HTTP")
    check(TestClient(app).get("/api/revision").status_code == 401, "needs a student session")
    sid = new_student()
    client = TestClient(app)
    client.post("/api/auth/login", json={"username": f"mast.{_n}", "password": "kid-password-1"})
    api.submit_assessment(sid, "position", key("position", "cricket")[0])
    r = client.get("/api/revision")
    check(r.status_code == 200 and r.json()["due"][0]["concept_id"] == "position", "GET /api/revision")
    check(client.get("/api/revision/question", params={"concept_id": "acceleration"}).status_code == 404,
          "a concept not in the queue → 404")
    r = client.get("/api/revision/question", params={"concept_id": "position"})
    check(r.status_code == 200 and r.json()["options"], "GET the question")
    check(client.post("/api/revision", json={"concept_id": "position", "answer": "Z"}).status_code == 400,
          "a bad option → 400")
    check(client.post("/api/revision", json={"concept_id": "position", "answer": "A",
                                             "confidence": "maybe"}).status_code == 400,
          "a bad confidence → 400")
    fresh = next(i for i in diagnostic.load_config()["source_interests"] if i != "cricket")
    r = client.post("/api/revision", json={"concept_id": "position",
                                           "answer": key("position", fresh)[0], "confidence": "think"})
    check(r.status_code == 200 and r.json()["mastery_signal"] == "mastered", "POST: mastered")


def main() -> int:
    test_evidence()
    sid, _ = test_lesson_checks()
    test_queue(sid)
    test_revision_answers(sid)
    test_metrics_untouched(sid)
    test_http()
    print(f"\nAll {_checks} mastery and revision checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
