"""Fill a SEPARATE database with a realistic demo class, so the dashboards are full on stage.

Usage (from the project root):
    venv\\Scripts\\python.exe scripts\\seed_demo.py --reset
    set ECOLEARN_PROGRESS_DB=data\\demo.db      (PowerShell: $env:ECOLEARN_PROGRESS_DB = "data\\demo.db")
    venv\\Scripts\\python.exe -m uvicorn api.main:app --port 8000

It writes to data/demo.db, never to data/progress.db, so the pilot's numbers stay clean.
It refuses to touch the pilot database even if you point it there.

What it makes: one teacher, one Class 11 class of 25 students (cricket / football /
gaming), each with a "getting to know you" survey and a starting check, lessons read and checked, mix-ups with
"how sure are you?", 👍/👎, revision answers, and (for most of the class) the end
check; plus personal stories with decision trails and a teaching-assistant plan.

It goes through the same code the app uses (grading, mastery, the revision queue), then
moves the timestamps back over three weeks, so the numbers are consistent with the real
rules rather than painted on.

HONESTY: everything here is invented. The students are fictional; each answer is drawn
from a simple ability model with a fixed random seed; the personal-story texts are
placeholders and carry the model name "demo-seed". No AI usage (tokens, cost) is
invented: the usage log stays empty. Never quote these numbers as pilot results.
Re-running with the same seed gives the same class.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import random
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_DEMO_DB = _ROOT / "data" / "demo.db"
_PILOT_DB = _ROOT / "data" / "progress.db"

# The demo accounts' shared password (a throwaway for a local demo database).
DEMO_PASSWORD = "demo-class-2026"
TEACHER_USERNAME = "demo.teacher"
SEED = 2026

NAMES = [
    "Aarav Kumar", "Meera Iyer", "Kabir Singh", "Ananya Reddy", "Rohan Mehta",
    "Isha Patel", "Vihaan Sharma", "Diya Nair", "Arjun Rao", "Saanvi Gupta",
    "Aditya Verma", "Kiara Menon", "Dev Malhotra", "Tara Banerjee", "Yash Joshi",
    "Riya Kapoor", "Ishaan Das", "Navya Pillai", "Karthik Subramanian", "Zoya Khan",
    "Neel Desai", "Pooja Hegde", "Sahil Chopra", "Lakshmi Naidu", "Omar Siddiqui",
]
# --south-indian: a second sample class in its own database (data/sample.db), South Indian names. Most students
# were last active in the last RECENT_DAYS days; QUIET_STUDENTS went quiet 8 to 12 days ago, so the teacher's
# "gone quiet" card has someone to show.
SOUTH_INDIAN_NAMES = [
    "Arjun Krishnan", "Lakshmi Narayanan", "Karthik Raghavan", "Divya Subramaniam", "Vignesh Rajan",
    "Priya Venkatesh", "Harish Reddy", "Sneha Nair", "Pranav Menon", "Keerthana Murugan",
    "Surya Prakash", "Anjali Pillai", "Rahul Chandran", "Meenakshi Sundaram", "Siddharth Rao",
    "Kavya Shetty", "Naveen Gowda", "Swathi Iyer", "Aditya Varma", "Nandini Hegde",
    "Gokul Krishna", "Revathi Balakrishnan", "Vishnu Namboodiri", "Harini Srinivasan", "Manoj Kumar",
]
_SAMPLE_DB = _ROOT / "data" / "sample.db"
SAMPLE_TEACHER_USERNAME = "sample.teacher"
ACTIVE_WINDOW_DAYS = 14   # the end check opened this many days ago (plus one)
RECENT_DAYS = 3
QUIET_STUDENTS = 3
QUIET_DAYS = (8, 12)
INTERESTS = ["cricket"] * 9 + ["football"] * 8 + ["gaming"] * 8
NOT_STARTED = 2          # signed up, haven't taken the starting check
NO_END_CHECK = 3         # took the starting check, not the end check yet
HOBBY_IDS = ["cricket", "football", "badminton", "basketball", "kabaddi", "athletics",
             "swimming", "cycling", "gaming", "phones", "cars", "music"]


def _resolve_db(sample: bool, explicit: str | None) -> Path:
    if sample:
        # Ignores ECOLEARN_PROGRESS_DB on purpose: it is often still set to data\demo.db in the same window,
        # and --reset would wipe the demo's pre-warmed stories.
        raw = explicit or str(_SAMPLE_DB)
    else:
        raw = explicit or os.environ.get("ECOLEARN_PROGRESS_DB")
    path = Path(raw) if raw else _DEMO_DB
    path = path if path.is_absolute() else (Path.cwd() / path)
    if path.resolve() == _PILOT_DB.resolve():
        sys.exit("Refusing to seed data/progress.db: that is the pilot database. "
                 "Leave ECOLEARN_PROGRESS_DB unset (the default is data/demo.db).")
    if sample and path.resolve() == _DEMO_DB.resolve():
        sys.exit("Refusing to put the --south-indian class into data/demo.db (it holds the demo's stories). "
                 "The default is data/sample.db.")
    return path


def _iso(moment: datetime) -> str:
    return moment.isoformat()


_IST = timezone(timedelta(hours=5, minutes=30))


def _daytime(moment: datetime, rng: random.Random) -> datetime:
    """The same Indian date as `moment`, at a random time a student might be studying (07:00 to 22:00 IST)."""
    local = moment.astimezone(_IST)
    minute = rng.randint(7 * 60, 22 * 60 - 1)
    return local.replace(hour=minute // 60, minute=minute % 60, second=rng.randint(0, 59),
                         microsecond=0).astimezone(timezone.utc)


def main() -> int:
    parser = argparse.ArgumentParser(description="Seed a demo class into data/demo.db.")
    parser.add_argument("--reset", action="store_true", help="delete the demo database first")
    parser.add_argument("--south-indian", action="store_true",
                        help="a second sample class (South Indian names, most students active in the last few "
                             "days) in data/sample.db; teacher login sample.teacher")
    parser.add_argument("--db", help="database file to write (default data/demo.db, or data/sample.db)")
    args = parser.parse_args()
    sample = args.south_indian

    db_path = _resolve_db(sample, args.db)
    if db_path.exists():
        if not args.reset:
            sys.exit(f"{db_path} already exists. Run with --reset to rebuild it.")
        db_path.unlink()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    os.environ["ECOLEARN_PROGRESS_DB"] = str(db_path)  # BEFORE importing the app

    from src import platform_api as api  # noqa: E402
    from src.auth import passwords  # noqa: E402
    from src.content import lesson_service  # noqa: E402
    from src.learner import diagnostic, personal_story, survey as survey_mod  # noqa: E402
    from src.path import engine  # noqa: E402
    from src.progress import store  # noqa: E402

    rng = random.Random(SEED)
    # The survey draws from its OWN stream, so adding it didn't change the class's checks.
    srng = random.Random(SEED + 1)
    now = datetime.now(tz=timezone.utc)
    conn = store._connect()

    def run_sql(sql: str, params: tuple = ()) -> None:
        with conn:
            conn.execute(sql, params)

    # ---- accounts ----------------------------------------------------------
    if sample:
        teacher_name, teacher_username, class_name, names = (
            "Mrs. Sangeetha Raman", SAMPLE_TEACHER_USERNAME, "Class 11-A Physics", SOUTH_INDIAN_NAMES)
    else:
        teacher_name, teacher_username, class_name, names = (
            "Ms. Priya Nair", TEACHER_USERNAME, "Class 11-B Physics", NAMES)
    teacher = api.create_teacher(teacher_name, teacher_username, DEMO_PASSWORD)
    teacher_id = teacher["teacher_id"]
    roster = [f"{n}, {i}" for n, i in zip(names, INTERESTS)]
    made = api.create_class(teacher_id, class_name, "Class 11", "cricket", roster)
    class_id = made["class"]["class_id"]
    shared_hash = passwords.hash_password(DEMO_PASSWORD)
    students = made["credentials"]
    for s in students:
        store.update_student_password(s["student_id"], shared_hash)
    run_sql("UPDATE classes SET created_at = ? WHERE class_id = ?",
            (_iso(now - timedelta(days=23)), class_id))
    # In the sample class every student who started has one last moment of activity, a random day and time:
    # most in the last few days, a few 8 to 12 days ago; everything they did comes before it (fixed at the end,
    # in "last activity").
    arng = random.Random(SEED + 2)   # its own stream, so the default demo class is unchanged

    # ---- who each student is ------------------------------------------------
    not_started = set(rng.sample(range(len(students)), NOT_STARTED))
    quiet = set(arng.sample([i for i in range(len(students)) if i not in not_started], QUIET_STUDENTS))
    people = []
    for index, s in enumerate(students):
        ability = min(0.92, max(0.25, rng.gauss(0.6, 0.15)))
        if index in (6, 17):
            ability = 0.3          # two students who really struggle
        own_hobby = {"cricket": "cricket", "football": "football", "gaming": "gaming"}[s["interest"]]
        others = [h for h in HOBBY_IDS if h != own_hobby]
        hobbies = rng.sample(others, 2) + ([own_hobby] if rng.random() < 0.5 else [])
        people.append({
            **s, "ability": ability, "hobbies": hobbies[:3],
            "started_days_ago": 20 - rng.random() * 5,
            "check_taken": index not in not_started,
        })
        if sample:
            days_ago = arng.uniform(*QUIET_DAYS) if index in quiet else arng.uniform(0, RECENT_DAYS)
            last = _daytime(now - timedelta(days=days_ago), arng)
            if last > now:
                last -= timedelta(days=1)
            people[-1]["last_active"] = last
    takers = [p for p in people if p["check_taken"]]
    no_end = {p["student_id"] for p in rng.sample(takers, NO_END_CHECK)}

    def difficulty(concept_id: str) -> float:
        return (hashlib.sha256(concept_id.encode()).digest()[0] / 255 - 0.5) * 0.3

    def favourite_wrong(concept_id: str, source: str, wrong: list[str]) -> str:
        pick = hashlib.sha256(f"{concept_id}:{source}".encode()).digest()[0]
        return wrong[pick % len(wrong)]

    def pick_for(chosen: dict, p_right: float, ability: float,
                 unsure_scale: float = 1.0) -> tuple[str, str | None]:
        """(option letter or 'unsure', confidence) for one question."""
        check = lesson_service.get_authored_lesson(
            chosen["concept_id"], chosen["source_interest"]).check
        if rng.random() < unsure_scale * max(0.03, 0.22 - 0.2 * ability):
            return "unsure", None
        options = list(check.options)
        if rng.random() < p_right:
            sure = rng.choices(["sure", "think", "guess"], [0.5, 0.3, 0.2])[0]
            return check.answer, sure
        wrong = [o for o in options if o != check.answer]
        letter = (favourite_wrong(chosen["concept_id"], chosen["source_interest"], wrong)
                  if rng.random() < 0.65 else rng.choice(wrong))
        sure = rng.choices(["sure", "think", "guess"], [0.35 - 0.2 * ability + 0.2, 0.35, 0.3])[0]
        return letter, sure

    def take_check(p: dict, chosen: list[dict], fixed: dict[str, float] | None = None,
                   unsure_scale: float = 1.0) -> tuple[dict, dict]:
        """`fixed` maps concept_id -> the chance of a right answer; otherwise ability decides."""
        picks, confs = {}, {}
        for q in chosen:
            p_right = (fixed or {}).get(q["concept_id"])
            if p_right is None:
                p_right = min(0.97, max(0.05, p["ability"] + difficulty(q["concept_id"])))
            letter, sure = pick_for(q, p_right, p["ability"], unsure_scale)
            picks[q["concept_id"]] = letter
            if sure:
                confs[q["concept_id"]] = sure
        return picks, confs


    def survey_answers(p: dict) -> dict:
        """What this fictional student says about themselves (leans on their ability)."""
        a = p["ability"]
        out: dict = {"hobbies": p["hobbies"]}
        depth = {}
        know = {}
        for h in p["hobbies"][:2]:
            depth[h] = srng.choices(["watch", "follow", "play_fun", "play_regular", "compete"],
                                    [2, 3, 4, 3, 1])[0]
            know[h] = srng.sample(["rules", "tactics", "equipment", "numbers", "history"],
                                  srng.randint(0, 4))
        if depth:
            out["hobby_depth"], out["hobby_know"] = depth, {h: k for h, k in know.items() if k}
        out["first_step"] = srng.choice(["story", "picture", "try", "rule"])
        out["pace"] = srng.choices(["step_by_step", "steady", "fast"], [3, 4, 2])[0]
        out["session_length"] = srng.choices(["m5", "m10", "m20", "m30"], [2, 4, 3, 1])[0]
        out["focus_drift"] = srng.choices(["stays", "some", "often"], [2, 4, 3])[0]
        out["distractions"] = srng.sample(["phone", "noise", "thoughts", "tired", "bored"],
                                          srng.randint(1, 3))
        feel = ["love", "ok"] if a > 0.7 else ["nervous", "dread"] if a < 0.45 else ["ok", "nervous", "love"]
        out["physics_feel"] = srng.choice(feel)
        out["maths_comfort"] = srng.choice(["strong", "mostly"] if a > 0.6 else ["shaky", "struggle", "mostly"])
        out["trips"] = srng.choice(["ideas", "formulas", "numericals", "wording"])
        out["goal"] = srng.choice(["pass", "marks", "entrance", "curious"])
        return out

    # ---- starting checks ----------------------------------------------------
    hobby_ids_valid = {h["id"] for h in diagnostic.hobby_options()}
    for p in people:
        t0 = now - timedelta(days=p["started_days_ago"])
        if sample:
            t0 = min(_daytime(t0, arng), p["last_active"] - timedelta(days=1))
        run_sql("UPDATE students SET created_at = ? WHERE student_id = ?",
                (_iso(t0 - timedelta(minutes=6)), p["student_id"]))
        p["t0"] = t0
        if not p["check_taken"]:
            continue
        p["hobbies"] = [h for h in p["hobbies"] if h in hobby_ids_valid]
        sid = p["student_id"]
        profile = store.get_student(sid)
        chosen = diagnostic.choose_questions(profile["level"], profile["interest"],
                                             diagnostic.form_for(sid))
        picks, confs = take_check(p, chosen, {})
        rng_minutes = 1  # the survey, a minute after the account was made
        # "Getting to know you" came first, as it does for a real student.
        api.submit_survey(sid, survey_answers(p))
        run_sql("UPDATE learner_survey SET completed_at = ? WHERE student_id = ?",
                (_iso(t0 + timedelta(minutes=rng_minutes)), sid))
        api.submit_diagnostic(sid, picks, p["hobbies"], confs)
        at = _iso(t0 + timedelta(minutes=rng.randint(4, 9)))
        run_sql("UPDATE diagnostic_answers SET answered_at = ? WHERE student_id = ?", (at, sid))
        run_sql("UPDATE learner_profiles SET diagnostic_completed_at = ? WHERE student_id = ?",
                (at, sid))
        p["start_rows"] = store.get_diagnostic_answers([sid])

    # ---- lessons, lesson checks, ratings ---------------------------------------
    lessons_done = 0
    for p in people:
        if not p["check_taken"]:
            continue
        sid, interest = p["student_id"], p["interest"]
        ready = sorted(lesson_service.concepts_with_lessons(interest),
                       key=lambda c: engine.find_concept(c).order)
        # first the ideas the check flagged (that is what the plan tells them to do),
        # then the teaching order
        flagged = [r["concept_id"] for r in p["start_rows"]
                   if r["correct"] is not True and r["concept_id"] in ready]
        rng.shuffle(flagged)
        wanted = max(3, min(len(ready), int(3 + p["ability"] * 9 + rng.randint(-2, 4))))
        if p["ability"] <= 0.3:
            wanted = rng.randint(2, 4)
        order = [c for c in flagged if rng.random() < 0.75]
        order += [c for c in ready if c not in order]
        studied = order[:wanted]
        p["studied"] = studied
        last_study = now - timedelta(days=2.6)
        if sample:
            last_study = max(p["t0"] + timedelta(hours=2), p["last_active"] - timedelta(hours=3))
        span = (last_study - p["t0"]).total_seconds()
        for i, concept_id in enumerate(studied):
            moment = p["t0"] + timedelta(seconds=span * (i + 1) / (len(studied) + 1)
                                         + rng.randint(0, 3600))
            if sample:
                moment = min(max(_daytime(moment, arng), p["t0"] + timedelta(minutes=15)), last_study)
            view = api.start_lesson_view(sid, concept_id)
            seconds = rng.choice([rng.randint(8, 30), rng.randint(60, 420), rng.randint(120, 540)])
            store.set_lesson_view_seconds(view["view_id"], seconds)
            run_sql("UPDATE lesson_views SET opened_at = ? WHERE view_id = ?",
                    (_iso(moment), view["view_id"]))
            authored = lesson_service.get_authored_lesson(concept_id, interest)
            chosen = {"concept_id": concept_id, "source_interest": interest}
            # reading the lesson first lifts the odds
            p_right = min(0.97, p["ability"] + difficulty(concept_id) + 0.18)
            attempt_moment = moment + timedelta(minutes=rng.randint(3, 12))
            for attempt in range(3):
                letter, sure = pick_for(chosen, p_right, p["ability"])
                if letter == "unsure":
                    letter = rng.choice(list(authored.check.options))
                if attempt > 0:
                    letter = authored.check.answer      # the right answer was shown
                api._grade_multiple_choice(sid, concept_id, letter, authored, interest, sure)
                if letter == authored.check.answer or rng.random() > 0.75:
                    break
            run_sql("UPDATE answers SET answered_at = ? WHERE student_id = ? AND concept_id = ?",
                    (_iso(attempt_moment), sid, concept_id))
            run_sql("UPDATE progress SET last_seen = ? WHERE student_id = ? AND concept_id = ?",
                    (_iso(attempt_moment), sid, concept_id))
            if rng.random() < 0.7:
                good = rng.random() < 0.86 - max(0, 0.15 - p["ability"] / 6)
                store.set_lesson_rating(sid, concept_id, interest, 1 if good else -1)
                run_sql("UPDATE lesson_ratings SET rated_at = ? WHERE student_id = ? AND concept_id = ?",
                        (_iso(attempt_moment + timedelta(seconds=40)), sid, concept_id))
            lessons_done += 1

    # ---- revision (a fresh question about a day later) ------------------------------
    revised = 0
    for p in people:
        if not p["check_taken"]:
            continue
        sid = p["student_id"]
        for item in api.get_revision(sid)["due"]:
            if rng.random() > 0.45:
                continue
            letter_pool = None
            q = api.get_revision_question(sid, item["concept_id"])
            letter_pool = list(q["options"])
            _, interest = api._revision_target(sid, item["concept_id"])
            check = lesson_service.get_authored_lesson(item["concept_id"], interest).check
            right = rng.random() < min(0.95, p["ability"] + 0.2)
            letter = check.answer if right else rng.choice([o for o in letter_pool if o != check.answer])
            api.submit_revision(sid, item["concept_id"], letter,
                                rng.choice(["sure", "think", "guess"]))
            moment = now - timedelta(days=rng.uniform(0.2, 1.8))
            if sample:
                moment = p["last_active"] - timedelta(minutes=arng.uniform(1, 150))
            run_sql("UPDATE review_answers SET answered_at = ? WHERE student_id = ? AND concept_id = ?",
                    (_iso(moment), sid, item["concept_id"]))
            run_sql("UPDATE progress SET last_seen = ? WHERE student_id = ? AND concept_id = ?",
                    (_iso(moment), sid, item["concept_id"]))
            revised += 1

    # ---- the end check ------------------------------------------------------------
    opened = now - timedelta(days=ACTIVE_WINDOW_DAYS + 1 if sample else 3)
    api.set_class_end_check(teacher_id, class_id, True)
    run_sql("UPDATE classes SET end_check_opened_at = ? WHERE class_id = ?", (_iso(opened), class_id))
    ended = 0
    for p in people:
        sid = p["student_id"]
        if not p["check_taken"] or sid in no_end:
            continue
        profile = store.get_student(sid)
        chosen = diagnostic.choose_end_questions(profile["interest"], p["start_rows"])
        studied = set(p["studied"])
        # What they knew before mostly carries over; a studied idea they got wrong
        # mostly gets fixed; an unstudied one they got wrong mostly doesn't.
        before = {r["concept_id"]: r["correct"] for r in p["start_rows"]}
        tilt = 0.12 * (p["ability"] - 0.6)
        fixed = {}
        for q in chosen:
            cid = q["concept_id"]
            base = 0.94 if before.get(cid) is True else 0.78 if cid in studied else 0.3
            fixed[cid] = min(0.97, max(0.05, base + tilt))
        picks, confs = take_check(p, chosen, fixed, unsure_scale=0.4)  # fewer "not sure" by now
        api.submit_end_check(sid, picks, confs)
        at = _iso(now - timedelta(days=rng.uniform(0.2, 2.5)))
        if sample:
            at = _iso(max(opened + timedelta(hours=1), p["last_active"] - timedelta(minutes=arng.uniform(5, 60))))
        run_sql("UPDATE end_check_answers SET answered_at = ? WHERE student_id = ?", (at, sid))
        run_sql("UPDATE learner_profiles SET end_check_completed_at = ? WHERE student_id = ?", (at, sid))
        ended += 1

    # ---- personal stories + their decision trails (placeholder text) -----------------
    table = {h["id"]: h for h in diagnostic.hobby_options()}
    outcomes = (["first"] * 12 + ["rules"] * 4 + ["critic"] * 3 + ["failed"] * 1 + ["no_fit"] * 2)
    stories = 0
    for p in people:
        if not p["check_taken"] or rng.random() > 0.6:
            continue
        for concept_id in p["studied"][:rng.randint(1, 3)]:
            ctx = personal_story._context(p["student_id"], concept_id)
            if ctx is None:
                continue
            kind = rng.choice(outcomes)
            hobby = ctx["hobby"]
            trail, status, attempts = [], "ready", 1
            model = "demo-seed"
            if kind == "first":
                trail = [(1, "rules", True, []), (1, "critic", True, [])]
            elif kind == "rules":
                trail = [(1, "rules", False, ["Uses a number that isn't in the lesson."]),
                         (2, "rules", True, []), (2, "critic", True, [])]
                attempts = 2
            elif kind == "critic":
                trail = [(1, "rules", True, []),
                         (1, "critic", False, ["The analogy implies the wrong direction of force."]),
                         (2, "rules", True, []), (2, "critic", True, [])]
                attempts = 2
            elif kind == "failed":
                trail = [(1, "rules", True, []),
                         (1, "critic", False, ["The analogy treats force as 'used up'."]),
                         (2, "rules", False, ["Still states the common mix-up as fact."])]
                status, attempts = "failed", 2
            else:
                trail = [(1, "fit", False, ["The writer found no honest link to this hobby."])]
                status = "no_fit"
            concept = engine.find_concept(concept_id)
            row = {
                "student_id": p["student_id"], "concept_id": concept_id,
                "hobby": hobby["id"], "lesson_hash": ctx["source"]["hash"],
                "status": status, "model": model, "attempts": attempts,
                "trail": [{"attempt": a, "step": s, "passed": ok, "problems": pr, "model": model}
                          for a, s, ok, pr in trail],
            }
            if status == "ready":
                label = table.get(hobby["id"], {"label": hobby["id"]})["label"]
                row.update(
                    story=f"[Demo placeholder] Think of a moment in {label.lower()} you know well: "
                          f"{concept.name.lower()} is quietly deciding what happens next.",
                    analogy=f"[Demo placeholder] {label} gives a picture of {concept.name.lower()}.",
                    limit_text="[Demo placeholder] Where the picture stops matching the physics.")
            elif status == "failed":
                row["problems"] = ["Still states the common mix-up as fact."]
            store.save_personal_story(row)
            moment = now - timedelta(days=rng.uniform(0.3, 15))
            if sample:
                moment = p["t0"] + (p["last_active"] - p["t0"]) * arng.random()
            run_sql("UPDATE personal_stories SET created_at = ? WHERE student_id = ? AND concept_id = ?",
                    (_iso(moment), p["student_id"], concept_id))
            stories += 1
    ready_rows = [r for r in store.list_personal_stories([p["student_id"] for p in people])
                  if r["status"] == "ready"]
    if ready_rows:
        store.set_story_visibility(ready_rows[0]["student_id"], ready_rows[0]["concept_id"], True,
                                   "student", "It said something that didn't match my textbook.")
    if len(ready_rows) > 1:
        store.set_story_visibility(ready_rows[1]["student_id"], ready_rows[1]["concept_id"],
                                   True, "teacher")

    # ---- last activity (sample class only) -----------------------------------------------------
    # The teacher's "last active" is the newest progress.last_seen. Nothing may come after the student's
    # chosen moment, and the newest row is set to exactly that moment.
    if sample:
        for p in people:
            if not p["check_taken"]:
                continue
            sid, last = p["student_id"], _iso(p["last_active"])
            run_sql("UPDATE progress SET last_seen = ? WHERE student_id = ? AND last_seen > ?", (last, sid, last))
            for table, column in (("answers", "answered_at"), ("review_answers", "answered_at"),
                                  ("end_check_answers", "answered_at"), ("lesson_views", "opened_at")):
                run_sql(f"UPDATE {table} SET {column} = ? WHERE student_id = ? AND {column} > ?", (last, sid, last))
            newest = conn.execute("SELECT concept_id FROM progress WHERE student_id = ? "
                                  "ORDER BY last_seen DESC LIMIT 1", (sid,)).fetchone()
            if newest:
                run_sql("UPDATE progress SET last_seen = ? WHERE student_id = ? AND concept_id = ?",
                        (last, sid, newest[0]))

    # ---- a teaching-assistant plan (the rules plan: no model call is made) ----------------
    api.generate_class_plan(teacher_id, class_id, models=[])

    # ---- the pilot experiment (data/experiments.yaml) --------------------------------------
    # Arms were given when the class was made, balanced, ties by a hash of the (random) student id. The
    # stage demo shows aarav.k's "Before you pick" line, so keep him in the treatment arm of every running
    # experiment: swap with a treatment classmate if needed, which keeps the class balanced. Demo data only;
    # never do this in a pilot.
    from src.learner import experiments  # noqa: E402
    aarav = students[0]["student_id"]   # aarav.k in the demo class, the first name in the sample class
    for exp in experiments.enabled():
        arm_row = conn.execute("SELECT arm FROM experiment_arms WHERE student_id = ? AND experiment_id = ?",
                               (aarav, exp["id"])).fetchone()
        if arm_row is None or arm_row[0] != "control":
            continue
        other = conn.execute("SELECT student_id FROM experiment_arms WHERE experiment_id = ? "
                             "AND arm = 'treatment' AND student_id != ? LIMIT 1", (exp["id"], aarav)).fetchone()
        if other:
            conn.execute("UPDATE experiment_arms SET arm = 'control' WHERE student_id = ? AND experiment_id = ?",
                         (other[0], exp["id"]))
            conn.execute("UPDATE experiment_arms SET arm = 'treatment' WHERE student_id = ? AND experiment_id = ?",
                         (aarav, exp["id"]))
            conn.commit()

    conn.close()
    print(f"Demo database: {db_path}")
    print(f"  teacher login : {teacher_username}  (password in scripts/seed_demo.py)")
    print(f"  class         : {class_name}, {len(people)} students, "
          f"{len(takers)} took the starting check, {ended} the end check")
    print(f"  activity      : {lessons_done} lessons checked, {revised} revision answers, "
          f"{stories} personal stories")
    print("  student logins: " + ", ".join(s["username"] for s in students[:4]) + ", ...  "
          "(same password)")
    print(f"Run the API against it with (Command Prompt):  set ECOLEARN_PROGRESS_DB={db_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
