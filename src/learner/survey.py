"""The "getting to know you" survey: questions, validation, and what the answers change.

The survey (data/survey.yaml) is the first thing a student does after a teacher creates
their account. It is not a test. From fixed-option answers (no free text about a child) this
module derives *traits*, and from traits it derives the few things the app adapts today:

* the lesson page: step-by-step or everything on one page, a "stretch your legs" nudge
  after the student's own stated span, "try an example first" for students who learn that way;
* the personal story: which hobby to build on (the one they know best), how much hobby jargon
  to use, and a gentler tone for students who are nervous about physics;
* the teacher: a plain-English profile per student and a class overview.

Everything here is deterministic. No model is called, and nothing here decides what is
*true* about a student: it records what they said and acts on it in small, visible ways.
Later content adaptation (difficulty, pacing of the path) reads the same traits.
"""

from __future__ import annotations

from pathlib import Path
from statistics import median
from typing import Any

import yaml

from src.errors import EcoLearnError
from src.file_cache import cached_parse
from src.learner import diagnostic

_CONFIG_PATH = Path(__file__).resolve().parents[2] / "data" / "survey.yaml"

HOBBY_LEVELS = ("novice", "fan", "player", "expert")
_SESSION_MINUTES = {"m5": 5, "m10": 10, "m20": 20, "m30": 30}


def load_config() -> dict[str, Any]:
    """data/survey.yaml, parsed once per version of the file. Shared: read-only."""
    return cached_parse(_CONFIG_PATH, lambda p: yaml.safe_load(p.read_text(encoding="utf-8")),
                        "survey")


def version() -> int:
    return int(load_config().get("version", 1))


def asked_hobbies() -> int:
    return int(load_config().get("asked_hobbies", 2))


def questions() -> list[dict[str, Any]]:
    """The questions as the browser needs them (all of it is public: no answer keys)."""
    return load_config()["questions"]


def sections() -> list[dict[str, Any]]:
    return load_config()["sections"]


def _by_id() -> dict[str, dict[str, Any]]:
    return {q["id"]: q for q in questions()}


def _option_ids(question: dict[str, Any]) -> set[str]:
    return {o["id"] for o in question.get("options", [])}


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def clean(answers: dict[str, Any] | None) -> dict[str, Any]:
    """Check a submission against the question bank and return only what is valid.

    Shape of the result: {"hobbies": [...], "hobby_depth": {hobby: option},
    "hobby_know": {hobby: [options]}, "<single>": option, "<multi>": [options]}.
    Every question may be skipped. Anything unknown is an error, never silently dropped:
    a mismatch between the page and the server should be loud.

    Raises:
        EcoLearnError: an unknown question or option, too many choices, or bad hobbies.
    """
    answers = answers or {}
    bank = _by_id()
    unknown = sorted(set(answers) - set(bank))
    if unknown:
        raise EcoLearnError(f"Unknown survey question(s): {', '.join(unknown)}.")

    out: dict[str, Any] = {}
    hobbies = diagnostic.clean_hobbies(answers.get("hobbies") if isinstance(answers.get("hobbies"), list) else [])
    if hobbies:
        out["hobbies"] = hobbies
    asked = hobbies[: asked_hobbies()]

    for qid, q in bank.items():
        if qid not in answers or qid == "hobbies":
            continue
        value = answers[qid]
        kind = q["type"]
        options = _option_ids(q)
        if kind == "single":
            if value in (None, ""):
                continue
            if value not in options:
                raise EcoLearnError(f"Not an option for {qid}: {value!r}.")
            out[qid] = value
        elif kind == "multi":
            picked = _as_list(value, qid)
            _check_options(qid, picked, options, q.get("max"))
            if picked:
                out[qid] = picked
        elif kind == "hobby_single":
            per = _as_dict(value, qid)
            cleaned = {}
            for hobby, option in per.items():
                _check_hobby(qid, hobby, asked)
                if option in (None, ""):
                    continue
                if option not in options:
                    raise EcoLearnError(f"Not an option for {qid}: {option!r}.")
                cleaned[hobby] = option
            if cleaned:
                out[qid] = cleaned
        elif kind == "hobby_multi":
            per = _as_dict(value, qid)
            cleaned_multi = {}
            for hobby, picked in per.items():
                _check_hobby(qid, hobby, asked)
                picked_list = _as_list(picked, qid)
                _check_options(qid, picked_list, options, q.get("max"))
                if picked_list:
                    cleaned_multi[hobby] = picked_list
            if cleaned_multi:
                out[qid] = cleaned_multi
    return out


def _as_list(value: Any, qid: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise EcoLearnError(f"{qid} should be a list.")
    return [str(v) for v in value]


def _as_dict(value: Any, qid: str) -> dict[str, Any]:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise EcoLearnError(f"{qid} should be one answer per hobby.")
    return value


def _check_options(qid: str, picked: list[str], options: set[str], limit: int | None) -> None:
    bad = [p for p in picked if p not in options]
    if bad:
        raise EcoLearnError(f"Not an option for {qid}: {bad[0]!r}.")
    if len(set(picked)) != len(picked):
        raise EcoLearnError(f"{qid} has a repeated choice.")
    if limit and len(picked) > int(limit):
        raise EcoLearnError(f"Pick at most {limit} for {qid}.")


def _check_hobby(qid: str, hobby: str, asked: list[str]) -> None:
    if hobby not in asked:
        raise EcoLearnError(f"{qid} is only asked about your first {asked_hobbies()} hobbies.")


# ---------------------------------------------------------------------------
# Traits: what the answers mean
# ---------------------------------------------------------------------------

_DEPTH = {"watch": 0, "follow": 1, "play_fun": 2, "play_regular": 3, "compete": 4}


def hobby_level(depth: int | None, knows: int) -> str:
    """novice | fan | player | expert, from how close they are and how much they can explain.

    Close-ness counts most (they do it, or only watch it), explaining counts as a tie-break:
    someone who plays regularly and can explain four things is an expert; someone who only
    watches and can explain one thing is a novice.
    """
    d = 1 if depth is None else depth
    if d >= 4 or (d >= 3 and knows >= 4):
        return "expert"
    if d >= 2:
        return "player"
    if d == 1 or knows >= 3:
        return "fan"
    return "novice"


def focus_span(session_minutes: int | None, drift: str | None) -> str:
    """short | medium | long, from the stated study span and how much the mind wanders."""
    if session_minutes is None and drift is None:
        return "medium"
    span_points = {5: 0, 10: 1, 20: 2, 30: 3}.get(session_minutes if session_minutes else 10, 1)
    drift_points = {"often": 0, "some": 1, "stays": 2}.get(drift or "some", 1)
    total = span_points + drift_points
    return "short" if total <= 1 else "long" if total >= 4 else "medium"


def derive_traits(answers: dict[str, Any]) -> dict[str, Any]:
    """Traits from cleaned answers. Missing answers fall back to neutral defaults."""
    hobbies = answers.get("hobbies", [])
    depth = answers.get("hobby_depth", {})
    know = answers.get("hobby_know", {})
    levels = {}
    for hobby in hobbies[: asked_hobbies()]:
        d = _DEPTH.get(depth.get(hobby, ""))
        k = len(know.get(hobby, []))
        levels[hobby] = {"level": hobby_level(d, k), "depth": d, "knows": k}

    minutes = _SESSION_MINUTES.get(answers.get("session_length", ""))
    span = focus_span(minutes, answers.get("focus_drift"))
    traits = {
        "hobbies": hobbies,
        "hobby_levels": levels,
        "focus": {
            "span": span,
            "session_minutes": minutes,
            "drift": answers.get("focus_drift"),
            "distractions": answers.get("distractions", []),
        },
        "learning": {"first_step": answers.get("first_step"), "pace": answers.get("pace")},
        "physics": {
            "feel": answers.get("physics_feel"),
            "maths": answers.get("maths_comfort"),
            "trips": answers.get("trips"),
            "goal": answers.get("goal"),
        },
    }
    traits["summary"] = describe(traits)
    return traits


_FEEL = {"love": "likes physics", "ok": "is fine with physics", "nervous": "is nervous about physics",
         "dread": "struggles with physics and dreads it"}
_MATHS = {"strong": "comfortable with the maths", "mostly": "mostly fine with the maths",
          "shaky": "shaky on the maths", "struggle": "finds the maths hard"}
_TRIPS = {"ideas": "understanding the ideas", "formulas": "choosing the formula",
          "numericals": "working out the numbers", "wording": "reading what a question asks"}
_STEP = {"story": "a story", "picture": "a picture", "try": "a problem to try first",
         "rule": "the rule first"}
_PACE = {"step_by_step": "step by step", "steady": "a steady pace", "fast": "fast"}
_GOAL = {"pass": "passing the boards", "marks": "top marks", "entrance": "an entrance exam",
         "curious": "curiosity"}


def describe(traits: dict[str, Any]) -> list[str]:
    """Plain-English lines for the teacher: what the student said, not what we conclude."""
    lines: list[str] = []
    table = {h["id"]: h["label"] for h in diagnostic.hobby_options()}
    for hobby, info in traits["hobby_levels"].items():
        label = table.get(hobby, hobby.capitalize())
        lines.append(f"{label}: {info['level']}")
    f = traits["focus"]
    if f["session_minutes"] or f["drift"]:
        bits = []
        if f["session_minutes"]:
            bits.append(f"studies about {f['session_minutes']} min at a time")
        if f["drift"] == "often":
            bits.append("mind wanders a lot")
        elif f["drift"] == "some":
            bits.append("mind wanders a little")
        elif f["drift"] == "stays":
            bits.append("stays focused")
        lines.append(f"Focus ({f['span']}): " + ", ".join(bits))
    p = traits["physics"]
    said = [t for t in (_FEEL.get(p["feel"] or ""), _MATHS.get(p["maths"] or "")) if t]
    if said:
        lines.append("Physics: " + "; ".join(said))
    if p["trips"]:
        lines.append(f"Usually trips up on {_TRIPS[p['trips']]}")
    lines_learn = []
    l = traits["learning"]
    if l["first_step"]:
        lines_learn.append(f"starts best with {_STEP[l['first_step']]}")
    if l["pace"]:
        lines_learn.append(f"likes {_PACE[l['pace']]}")
    if p["goal"]:
        lines_learn.append(f"aiming for {_GOAL[p['goal']]}")
    if lines_learn:
        lines.append("Learning: " + ", ".join(lines_learn))
    return lines


# ---------------------------------------------------------------------------
# What the traits change
# ---------------------------------------------------------------------------

DEFAULT_PREFS: dict[str, Any] = {
    "mode": "steps", "break_after_minutes": None, "example_first": False, "gentle": False,
}


def lesson_prefs(traits: dict[str, Any] | None) -> dict[str, Any]:
    """How the lesson page should behave for this student.

    mode                "steps" (one idea at a time) or "all" (one page: for fast readers)
    break_after_minutes a gentle stretch nudge after this much reading, or None
    example_first       put "Try an example" before "The idea" (they learn by trying)
    gentle              the student said physics makes them nervous: the page may say so kindly

    Nothing here locks or hides content: a student can always switch modes on the page.
    """
    if not traits:
        return dict(DEFAULT_PREFS)
    focus = traits["focus"]
    minutes = focus.get("session_minutes")
    break_after = None
    if focus["span"] in ("short", "medium") and minutes:
        break_after = minutes
    elif focus["span"] == "short":
        break_after = 8
    return {
        "mode": "all" if traits["learning"].get("pace") == "fast" else "steps",
        "break_after_minutes": break_after,
        "example_first": traits["learning"].get("first_step") == "try",
        "gentle": traits["physics"].get("feel") in ("nervous", "dread"),
    }


def order_hobbies(hobbies: list[str], traits: dict[str, Any] | None) -> list[str]:
    """The student's hobbies, closest-to-them first (stable: ties keep the order picked)."""
    if not traits:
        return list(hobbies)
    levels = traits.get("hobby_levels", {})
    rank = {lvl: i for i, lvl in enumerate(reversed(HOBBY_LEVELS))}  # expert=0 ... novice=3
    return sorted(hobbies, key=lambda h: rank.get(levels.get(h, {}).get("level", "fan"), 2))


def story_notes(traits: dict[str, Any] | None, hobby_id: str) -> list[str]:
    """Short guidance lines for the story writer. Coarse categories only: no raw answers."""
    if not traits:
        return []
    notes = []
    level = traits.get("hobby_levels", {}).get(hobby_id, {}).get("level")
    if level == "novice":
        notes.append("This student is new to the hobby: no hobby jargon, and explain any hobby "
                     "term in a few plain words.")
    elif level == "expert":
        notes.append("This student knows the hobby well: you may use its own terms, and skip "
                     "the basics of the hobby itself.")
    if traits["physics"].get("feel") in ("nervous", "dread"):
        notes.append("This student finds physics stressful: keep the tone warm and "
                     "encouraging, and keep the idea small.")
    if traits["focus"]["span"] == "short":
        notes.append("This student loses focus quickly: keep it at the short end of the limits.")
    return notes


# ---------------------------------------------------------------------------
# Observed behaviour, next to what they said
# ---------------------------------------------------------------------------

def observed_reading(views: list[dict[str, Any]]) -> dict[str, Any]:
    """What lesson views show: how long they actually read, and how often they skim.

    A view under 30 seconds of active reading is a skim. Needs at least three views to say
    anything (fewer is noise); otherwise the numbers are None.
    """
    seconds = [int(v.get("active_seconds") or 0) for v in views]
    if len(seconds) < 3:
        return {"views": len(seconds), "median_minutes": None, "skim_share": None}
    return {
        "views": len(seconds),
        "median_minutes": round(median(seconds) / 60, 1),
        "skim_share": round(sum(1 for s in seconds if s < 30) / len(seconds), 2),
    }
