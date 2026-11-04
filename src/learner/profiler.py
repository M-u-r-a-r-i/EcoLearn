"""The learner profile, in the open (2026-10-14): what EcoLearn thinks about a student, why, and what it does about it.

Before this, the profile was what the student SAID in the first-login survey (survey.lesson_prefs), fixed at that
moment; what they DID was recorded and shown to the teacher but changed nothing for them, and they never saw any of it.
This module joins the two:

  * every adaptation is an INSIGHT with its evidence in plain words, and what the app does because of it;
  * behaviour can correct what was said ("you said you read fast, but most lessons were open under 30 seconds and the
    checks went wrong: lessons open one step at a time for now");
  * confidence is used, not just stored: a student who is often SURE of a wrong answer holds a firm mix-up, which needs
    a nudge to check before picking, and those ideas come back for revision sooner;
  * the student can say "that's not me" to any insight, and its effect is switched off for them.

Showing a learner their own model is an "open learner model" in the education literature. Here it is also the
transparency a profile of a child should have: nothing is inferred out of sight.

All of it is rules, no AI: the numbers come from the database, the thresholds are below, and the same input always gives
the same profile. NOTHING here is evidence that the adaptations help; the pilot has to show that.

Pure: the caller (platform_api.get_learner_profile) loads the rows and passes them in.
"""

from __future__ import annotations

from typing import Any

from src.learner import survey

# Behaviour needs enough data before it says anything: below these, the profile stays quiet.
MIN_VIEWS = 3                 # lesson views before reading habits count (same as survey.observed_reading)
MIN_FIRST_TRIES = 4           # first tries at lesson checks before accuracy counts
MIN_SURE = 3                  # answers marked "sure" before calibration counts
SKIM_SHARE = 0.5              # half the lessons open under 30 seconds
LOW_FIRST_TRY = 0.5           # under half right first time
SURE_WRONG_SHARE = 0.34       # a third or more of "sure" answers were wrong
SURE_WRONG_MIN = 2            # and at least two of them
GOOD_FIRST_TRY = 0.7          # "doing better than you think"
GOOD_MIN_FIRST_TRIES = 5

SAID, SHOWN = "said", "shown"


def _pct(part: int, whole: int) -> str:
    return f"{part} of {whole}"


def calibration(events_by_concept: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    """How often "sure" was right. Events are learner_plan._answer_events output (every check, oldest first).

    Returns {"sure": n, "sure_wrong": n, "sure_wrong_concepts": [...]}: the concepts with a sure-but-wrong answer
    that isn't fixed yet. Fixed means right later on a DIFFERENT question (as in learner_plan.mix_up_history): a
    right answer to the same question just after the explanation was shown proves little.
    """
    sure = sure_wrong = 0
    concepts: list[str] = []
    ever: list[str] = []
    for concept_id, items in events_by_concept.items():
        last_sure_wrong = None
        for i, e in enumerate(items):
            if e.get("confidence") != "sure":
                continue
            sure += 1
            if not e["correct"]:
                sure_wrong += 1
                last_sure_wrong = i
        if last_sure_wrong is not None:
            ever.append(concept_id)
            question = items[last_sure_wrong]["question"]
            if not any(e["correct"] and e["question"] != question for e in items[last_sure_wrong + 1:]):
                concepts.append(concept_id)
    return {"sure": sure, "sure_wrong": sure_wrong, "sure_wrong_concepts": sorted(concepts),
            "sure_wrong_ever": sorted(ever)}


def build(traits: dict[str, Any] | None, observed: dict[str, Any], first_tries: tuple[int, int],
          events_by_concept: dict[str, list[dict[str, Any]]], dismissed: set[str],
          suppressed: set[str] | frozenset[str] = frozenset(),
          overrides: dict[str, Any] | None = None) -> dict[str, Any]:
    """The profile.

    traits:      survey traits (survey.derive_traits) or None when the survey wasn't answered
    observed:    survey.observed_reading(views)
    first_tries: (right, answered) over first tries at lesson checks
    dismissed:   insight ids the student said "that's not me" to
    suppressed:  insight ids switched off for this student by a pilot experiment's control arm
                 (src/learner/experiments.py): never produced, never shown, no effect
    overrides:   lesson prefs fixed by a pilot experiment's arm (e.g. {"slow_down": False}), applied last; an
                 insight's effect text is corrected so the About me page never promises what the arm removed

    Returns {"insights": [{id, kind: said|shown, title, detail, evidence, effect, active}],
             "prefs": the lesson prefs after every active insight (survey.lesson_prefs keys + "slow_down"),
             "sooner": concept ids that come back for revision sooner (empty if that insight is off),
             "signals": the raw numbers, for the teacher and the tests}.
    """
    traits = traits or None
    base = survey.lesson_prefs(traits)
    prefs = {**base, "slow_down": False}
    insights: list[dict[str, Any]] = []
    right, answered = first_tries
    accuracy = right / answered if answered else None
    cal = calibration(events_by_concept)

    def add(insight_id: str, kind: str, title: str, detail: str, evidence: list[str], effect: str) -> bool:
        if insight_id in suppressed:
            return False  # a pilot experiment's control arm: not shown, no effect
        active = insight_id not in dismissed
        insights.append({"id": insight_id, "kind": kind, "title": title, "detail": detail,
                         "evidence": evidence, "effect": effect, "active": active})
        return active

    # ---- what they said (the survey) ----------------------------------------------------------
    if traits:
        if base["mode"] == "all":
            if not add("pace_fast", SAID, "You like to read fast",
                       "You told us you like to get through things quickly.", ["Your 'getting to know you' answers"],
                       "Lessons open as one page instead of one step at a time."):
                prefs["mode"] = "steps"
        if base["example_first"]:
            if not add("example_first", SAID, "You like to start by trying",
                       "You told us you'd rather try an example before reading the idea.",
                       ["Your 'getting to know you' answers"],
                       "'Try an example' comes before 'The idea' in each lesson."):
                prefs["example_first"] = False
        if base["break_after_minutes"]:
            if not add("break_nudge", SAID, "You focus best in shorter stretches",
                       f"You told us about {base['break_after_minutes']} minutes is a good stretch for you.",
                       ["Your 'getting to know you' answers"],
                       f"A gentle 'time for a stretch?' after {base['break_after_minutes']} minutes of reading."):
                prefs["break_after_minutes"] = None
        if base["gentle"]:
            if not add("gentle", SAID, "Physics can feel stressful",
                       "You told us physics makes you nervous, or feels like a struggle.",
                       ["Your 'getting to know you' answers"],
                       "Lessons start with a calm line, and your personal story keeps a warm tone."):
                prefs["gentle"] = False

    # ---- what they did (behaviour) ------------------------------------------------------------
    skim = observed.get("skim_share")
    skimming = skim is not None and observed.get("views", 0) >= MIN_VIEWS and skim >= SKIM_SHARE
    struggling = answered >= MIN_FIRST_TRIES and accuracy is not None and accuracy < LOW_FIRST_TRY
    skim_evidence = f"{round(skim * 100)}% of your {observed.get('views', 0)} lessons were open under 30 seconds" \
        if skim is not None else ""
    if skimming and struggling and base["mode"] == "all" and prefs["mode"] == "all":
        if add("pace_check", SHOWN, "One page may be a bit fast for now",
               "You said you like to read fast, but most lessons went by quickly and the checks were hard.",
               [skim_evidence, f"Right first time on {_pct(right, answered)} checks"],
               "Lessons open one step at a time for now. You can still switch to one page on any lesson."):
            prefs["mode"] = "steps"
    elif skimming:
        add("skimming", SHOWN, "You often move on quickly",
            "Many lessons were open for less than half a minute before you moved on.",
            [skim_evidence],
            "Nothing changes for you. If the check goes wrong, the lesson is still there to read.")

    sure_wrong_rule = cal["sure"] >= MIN_SURE and cal["sure_wrong"] >= SURE_WRONG_MIN \
        and cal["sure_wrong"] / cal["sure"] >= SURE_WRONG_SHARE
    if sure_wrong_rule:
        if add("sure_wrong", SHOWN, "Sometimes you're sure, but it's a mix-up",
               "When you pick 'I'm sure', the answer is usually right, but not always. Those are the mix-ups "
               "worth catching, because they feel true.",
               [f"{_pct(cal['sure_wrong'], cal['sure'])} answers you were sure about were wrong"],
               "A short reminder to check your answer before you pick, and those ideas come back for "
               "revision sooner."):
            prefs["slow_down"] = True

    if base["gentle"] and answered >= GOOD_MIN_FIRST_TRIES and accuracy is not None and accuracy >= GOOD_FIRST_TRY:
        add("doing_well", SHOWN, "You're doing better than you think",
            "You said physics can feel stressful, and your checks are going well.",
            [f"Right first time on {_pct(right, answered)} checks"],
            "Nothing changes. Just so you know.")

    sooner = cal["sure_wrong_concepts"] if any(i["id"] == "sure_wrong" and i["active"] for i in insights) else []
    if overrides:
        prefs.update(overrides)
        if overrides.get("slow_down") is False:
            for i in insights:  # the arm removed the reminder: say only what still happens
                if i["id"] == "sure_wrong":
                    i["effect"] = "Those ideas come back for revision sooner."
    return {
        "insights": insights,
        "prefs": prefs,
        "sooner": sooner,
        "signals": {"views": observed.get("views", 0), "skim_share": skim, "first_try_right": right,
                    "first_try_answered": answered, "sure": cal["sure"], "sure_wrong": cal["sure_wrong"],
                    # For the pilot experiment: whether the rule is met (in either arm), and the mix-ups behind it.
                    "sure_wrong_rule": sure_wrong_rule,
                    "sure_wrong_concepts": len(cal["sure_wrong_ever"]),
                    "sure_wrong_fixed": len(cal["sure_wrong_ever"]) - len(cal["sure_wrong_concepts"])},
    }


# Every insight id the profile can produce: a dismissal for anything else is refused.
INSIGHT_IDS = frozenset({"pace_fast", "example_first", "break_nudge", "gentle",
                         "pace_check", "skimming", "sure_wrong", "doing_well"})
