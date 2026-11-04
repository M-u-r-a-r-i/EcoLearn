"""The randomised pilot comparison (2026-10-18). No network.

  1. Arms: balanced within a class (the smaller arm first), a tie broken by a re-checkable hash that splits about
     evenly; given when the account is made, never changed; balanced even when accounts are made at the same moment.
  2. Effect (check_prompt): the "Before you pick" line is on for every treatment student and never in control; a
     flagged control student's About me card doesn't promise it; sooner revision is the same in both arms. An
     insight-type experiment hides its insight in control only.
  3. Switches: an older account gets its arm the first time its profile is built; a disabled experiment, or
     ECOLEARN_EXPERIMENTS=off, suppresses nothing.
  4. Analysis: the bootstrap is deterministic, needs 2+ students per arm, and its interval brackets the estimate;
     the pilot report's experiment section is pseudonymised, read-only, and counts the unassigned.

Run: venv\\Scripts\\python.exe tests\\test_pilot_experiment.py
"""

from __future__ import annotations

import os
import sqlite3
import sys
import tempfile
import threading
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_experiment_"))
_DB = _TMP / "experiment.db"
os.environ["ECOLEARN_PROGRESS_DB"] = str(_DB)
os.environ["LLM_MODEL"] = ""
os.environ.pop("ECOLEARN_EXPERIMENTS", None)
warnings.simplefilter("ignore")

from src import platform_api as api  # noqa: E402
from src.content import lesson_service  # noqa: E402
from src.learner import diagnostic, experiments  # noqa: E402
from src.progress import metrics, store  # noqa: E402

EXP = "check_prompt"
_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


def key(concept_id: str, interest: str) -> tuple[str, str]:
    c = lesson_service.get_authored_lesson(concept_id, interest).check
    return c.answer, next(o for o in c.options if o != c.answer)


def arms_in(class_id: str) -> dict[str, int]:
    out = {"control": 0, "treatment": 0}
    for s in store.list_class_students(class_id):
        out[store.get_experiment_arms(s["student_id"])[EXP]] += 1
    return out


def test_assignment() -> dict:
    print("\n[1] arms")
    check(experiments.choose_arm(EXP, "x", {"control": 3, "treatment": 2}) == "treatment"
          and experiments.choose_arm(EXP, "x", {"control": 1}) == "treatment",
          "the smaller arm in the class goes first")
    check(experiments.choose_arm(EXP, "abc", {}) == experiments.tie_break(EXP, "abc")
          == experiments.tie_break(EXP, "abc"), "a tie is the hash, the same every time (re-checkable)")
    ties = [experiments.tie_break(EXP, f"stu_{i:04d}") for i in range(1000)]
    check(430 < ties.count("control") < 570, f"the hash splits about evenly ({ties.count('control')}/1000 control)")

    teacher = api.create_teacher("Ms. Rao", "rao.exp", "teach-physics-1")
    tid = teacher["teacher_id"]
    names = "\n".join(f"Student {chr(65 + i)}" for i in range(10))
    a = api.create_class(tid, "11-A", "Class 11", "cricket", names)["class"]["class_id"]
    b = api.create_class(tid, "11-B", "Class 11", "cricket", "\n".join(f"Pupil {chr(65 + i)}" for i in range(7)))["class"]["class_id"]
    check(arms_in(a) == {"control": 5, "treatment": 5}, f"a class of 10 splits 5/5 (got {arms_in(a)})")
    check(sorted(arms_in(b).values()) == [3, 4], f"a class of 7 splits 4/3 (got {arms_in(b)})")
    solo = api.register_student("Self Signup", "exp.solo", "kid-password-1", "cricket", "Class 11")["student_id"]
    check(store.get_experiment_arms(solo).get(EXP) in experiments.ARMS, "a self-signup student gets an arm too")
    first = store.get_experiment_arms(solo)[EXP]
    api._enrol_experiments(solo)
    api.get_learner_profile(solo)
    check(store.get_experiment_arms(solo)[EXP] == first, "an arm never changes")

    c = api.create_class(tid, "11-C", "Class 11", "cricket", "Only One")["class"]["class_id"]
    ids = [f"stu_race{i:02d}" for i in range(20)]
    conn = sqlite3.connect(_DB)
    conn.executemany("INSERT INTO students (student_id, name, interest, level, created_at, class_id) VALUES (?,?,?,?,?,?)",
                     [(i, i, "cricket", "Class 11", "2026-10-18T00:00:00+00:00", c) for i in ids])
    conn.commit()
    conn.close()
    threads = [threading.Thread(target=api._enrol_experiments, args=(i,)) for i in ids]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    got = arms_in(c)
    check(abs(got["control"] - got["treatment"]) <= 1, f"21 accounts at the same moment still balance (got {got})")
    return {"tid": tid, "class_a": a}


def make_sure_wrong(sid: str) -> None:
    """Answer the starting check wrong, then be sure and wrong twice and sure and right once."""
    qs = diagnostic.choose_questions("Class 11", "cricket", diagnostic.form_for(sid))
    api.submit_diagnostic(sid, {q["concept_id"]: key(q["concept_id"], q["source_interest"])[1] for q in qs})
    for concept in ("velocity", "acceleration"):
        api.submit_assessment(sid, concept, key(concept, "cricket")[1], "sure")
    api.submit_assessment(sid, "displacement", key("displacement", "cricket")[0], "sure")


def test_effect(ctx: dict) -> None:
    print("\n[2] what the arms change")
    by_arm = {"control": [], "treatment": []}
    for s in store.list_class_students(ctx["class_a"]):
        by_arm[store.get_experiment_arms(s["student_id"])[EXP]].append(s["student_id"])
    ctrl, treat, treat_plain = by_arm["control"][0], by_arm["treatment"][0], by_arm["treatment"][1]
    for sid in (ctrl, treat):
        make_sure_wrong(sid)
    p_ctrl, p_treat, p_plain = api._profile(ctrl), api._profile(treat), api._profile(treat_plain)
    check(not p_ctrl["prefs"]["slow_down"] and p_treat["prefs"]["slow_down"] and p_plain["prefs"]["slow_down"],
          "the line: never in control, on for EVERY treatment student (flagged or not)")
    insight = next(i for i in p_ctrl["insights"] if i["id"] == "sure_wrong")
    check(insight["effect"] == "Those ideas come back for revision sooner." and "reminder" not in insight["effect"],
          "a flagged control student's About me card doesn't promise the line they won't see")
    check(p_ctrl["sooner"] and p_treat["sooner"], "sooner revision is the same in both arms (only the line differs)")
    check(api.get_next_lesson(ctrl, "motion_straight_line")["prefs"]["slow_down"] is False
          and api.get_next_lesson(treat_plain, "motion_straight_line")["prefs"]["slow_down"] is True,
          "and the lesson envelope follows the arm")

    # The other kind of experiment: one that switches an insight off in its control arm.
    real = experiments.load_config
    experiments.load_config = lambda: [
        {**e, "enabled": e["id"] == "sure_wrong_nudge"} for e in real()]
    try:
        api._enrol_experiments(ctrl)
        nudge_arm = store.get_experiment_arms(ctrl)["sure_wrong_nudge"]
        has = any(i["id"] == "sure_wrong" for i in api._profile(ctrl)["insights"])
        check(has == (nudge_arm == "treatment"), f"an insight experiment hides the insight in control only ({nudge_arm})")
    finally:
        experiments.load_config = real

    experiments.load_config = lambda: [{**e, "enabled": False} for e in real()]
    try:
        check(api._profile(ctrl)["prefs"]["slow_down"] is True,
              "a disabled experiment changes nothing (a flagged student gets the normal product)")
    finally:
        experiments.load_config = real
    os.environ["ECOLEARN_EXPERIMENTS"] = "off"
    try:
        check(api._profile(ctrl)["prefs"]["slow_down"] is True and api._profile(treat_plain)["prefs"]["slow_down"] is False,
              "ECOLEARN_EXPERIMENTS=off: the normal product for everyone")
        old = api.register_student("Before Start", "exp.old", "kid-password-1", "cricket", "Class 11")["student_id"]
        check(store.get_experiment_arms(old) == {}, "and no arm is given while it is off")
    finally:
        os.environ.pop("ECOLEARN_EXPERIMENTS")
    api.get_learner_profile(old)
    check(EXP in store.get_experiment_arms(old), "an older account gets its arm the first time its profile is built")
    ctx.update(ctrl=ctrl, treat=treat, by_arm=by_arm)


def answer_checks(sid: str, right: int, wrong: int) -> None:
    concepts = ["position", "displacement", "velocity", "acceleration"]
    concepts = [c for c in concepts if lesson_service.get_authored_lesson(c, "cricket")]
    for i in range(right + wrong):
        c = concepts[i]
        api.submit_assessment(sid, c, key(c, "cricket")[0 if i < right else 1], "think")


def test_analysis(ctx: dict) -> None:
    print("\n[3] the analysis")
    d1 = metrics.bootstrap_difference([1, 1, 0.5, 1], [0, 0.5, 0, 0])
    d2 = metrics.bootstrap_difference([1, 1, 0.5, 1], [0, 0.5, 0, 0])
    check(d1 == d2 and d1["estimate"] == 0.75, "deterministic, and the estimate is the difference of means")
    check(d1["ci95"][0] <= d1["estimate"] <= d1["ci95"][1] and d1["ci95"][0] > 0,
          f"the interval brackets the estimate (here it excludes 0: {d1['ci95']})")
    check(metrics.bootstrap_difference([1], [0, 1])["estimate"] is None, "fewer than 2 in an arm: no estimate")

    # Fresh students with known first tries: treatment 4/4 and 3/4, control 2/4 and 1/4; one with only 2 checks.
    teacher = api.create_teacher("Mr. Das", "das.exp", "teach-physics-3")
    made = api.create_class(teacher["teacher_id"], "11-D", "Class 11", "cricket", "\n".join(f"Kid {c}" for c in "PQRSTU"))
    arms = {"control": [], "treatment": []}
    for cr in made["credentials"]:
        arms[store.get_experiment_arms(cr["student_id"])[EXP]].append(cr["student_id"])
    for sid, (r, w) in zip(arms["treatment"], [(4, 0), (3, 1), (1, 1)]):
        answer_checks(sid, r, w)
    for sid, (r, w) in zip(arms["control"], [(2, 2), (1, 3), (2, 0)]):
        answer_checks(sid, r, w)

    before = sqlite3.connect(_DB).execute("SELECT COUNT(*) FROM experiment_arms").fetchone()[0]
    report = api.pilot_report()
    after = sqlite3.connect(_DB).execute("SELECT COUNT(*) FROM experiment_arms").fetchone()[0]
    check(before == after, "the report is read-only: it assigns no arms")
    check(all(e["id"] != "sure_wrong_nudge" or e["enabled"] or e["arms"]["control"]["students"] + e["arms"]["treatment"]["students"]
              for e in report["experiments"]), "a stopped experiment nobody was in is left out")
    e = next(x for x in report["experiments"] if x["id"] == EXP)
    rows = [r for r in report["experiment_rows"] if r["experiment_id"] == EXP]
    check(e["primary_metric"] == "first_try_accuracy", "the primary measure comes from the config")
    # Only class 11-D's six students and the two sure-but-wrong students answered checks; compute the expected
    # means from the rows themselves (eligible = 3+ first tries) and compare with the report.
    expect = {}
    for arm in ("control", "treatment"):
        vals = [r["first_try_right"] / r["first_try_answered"] for r in rows
                if r["arm"] == arm and r["first_try_answered"] >= 3]
        expect[arm] = round(sum(vals) / len(vals), 3)
        check(e["arms"][arm]["primary_mean"] == expect[arm] and e["arms"][arm]["eligible"] == len(vals),
              f"{arm}: mean right-first-time over eligible students = {expect[arm]} ({len(vals)} students)")
    check(e["primary"]["estimate"] == round(expect["treatment"] - expect["control"], 3) and e["primary"]["ci95"],
          "the difference and its interval")
    check(any(r["first_try_answered"] == 2 for r in rows) and e["arms"]["control"]["first_try_students"] >
          e["arms"]["control"]["eligible"] - 1, "a student with only 2 checks is counted, but not eligible")
    check("far too few" in e["caution"], "with this few, the report says it is far too few to tell")
    check(e["unassigned"] == 0 and sum(sum(v.values()) for v in e["balance"].values()) == len(report["students"]),
          "everyone is assigned, and the balance table adds up")
    blob = str(report["experiment_rows"])
    check(all(r["student_id"].startswith("S") for r in report["experiment_rows"]) and "stu_" not in blob
          and "Kid P" not in blob and "das" not in blob, "rows are pseudonymised: no ids, names or usernames")


def main() -> None:
    ctx = test_assignment()
    test_effect(ctx)
    test_analysis(ctx)
    print(f"\nAll {_checks} pilot-experiment checks passed.")


if __name__ == "__main__":
    main()
