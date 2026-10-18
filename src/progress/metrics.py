"""Pilot metrics: turn raw activity rows into what a teacher (and the pitch) needs.

Pure functions, no database and no files: the boundary fetches the rows
(`store.get_activity`) and the lesson/concept details, and passes them in. That
keeps every number here testable with hand-made rows.

Two choices that shape every number below:

* **First-try accuracy, not "mastered".** After a wrong pick the app shows the
  right answer, so a second attempt is nearly free. Counting it would make
  every class look brilliant. Only a student's first pick on a concept says
  what they understood from the lesson.
* **Misconceptions are counted per student, not per click.** Five wrong clicks
  by one student is one confused student. The share is out of the students who
  answered that question, so a teacher reads "7 of 12 students think…".
"""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from statistics import median
from typing import Any, Callable

# A lesson view shorter than this is a bounce (opened by mistake, clicked
# through), not reading. It still counts as an open, but not toward reading time.
MIN_READING_SECONDS = 10


def _accuracy(correct: int, total: int) -> float | None:
    return round(correct / total, 3) if total else None


def _minutes(seconds: float) -> float:
    return round(seconds / 60, 1)


def class_insights(
    students: list[dict[str, Any]],
    activity: dict[str, list[dict[str, Any]]],
    concept_info: Callable[[str], dict[str, Any]],
    check_info: Callable[[str, str], dict[str, Any] | None],
) -> dict[str, Any]:
    """Aggregate a group of students' activity.

    Args:
        students:     [{student_id, name, ...}] — the group (a class).
        activity:     {"views": [...], "answers": [...], "ratings": [...]} as
                      returned by store.get_activity for those students.
        concept_info: concept_id -> {"name", "chapter_id", "chapter_name"}.
        check_info:   (concept_id, interest) -> {"question", "options", "answer"}
                      for that lesson's check, or None if it has none.

    Returns plain dicts and lists — see the keys built at the end.
    """
    ids = {s["student_id"] for s in students}
    views = [v for v in activity.get("views", []) if v["student_id"] in ids]
    answers = [a for a in activity.get("answers", []) if a["student_id"] in ids]
    ratings = [r for r in activity.get("ratings", []) if r["student_id"] in ids]
    first = [a for a in answers if a["attempt_no"] == 1]
    reading = [v for v in views if v["active_seconds"] >= MIN_READING_SECONDS]

    # ---- per student ------------------------------------------------------
    per_student: dict[str, dict[str, Any]] = {
        sid: {"student_id": sid, "lessons_opened": 0, "active_minutes": 0.0,
              "answered": 0, "first_try_correct": 0, "first_try_accuracy": None,
              "thumbs_up": 0, "thumbs_down": 0}
        for sid in ids
    }
    seconds_by_student: dict[str, int] = defaultdict(int)
    for v in views:
        per_student[v["student_id"]]["lessons_opened"] += 1
        seconds_by_student[v["student_id"]] += v["active_seconds"]
    for a in first:
        row = per_student[a["student_id"]]
        row["answered"] += 1
        row["first_try_correct"] += int(a["correct"])
    for r in ratings:
        per_student[r["student_id"]]["thumbs_up" if r["rating"] > 0 else "thumbs_down"] += 1
    for sid, row in per_student.items():
        row["active_minutes"] = _minutes(seconds_by_student[sid])
        row["first_try_accuracy"] = _accuracy(row["first_try_correct"], row["answered"])

    # ---- per concept ------------------------------------------------------
    concept_ids = ({v["concept_id"] for v in views} | {a["concept_id"] for a in answers}
                   | {r["concept_id"] for r in ratings})
    concepts = []
    for cid in concept_ids:
        c_first = [a for a in first if a["concept_id"] == cid]
        c_reading = [v["active_seconds"] for v in reading if v["concept_id"] == cid]
        c_ratings = [r["rating"] for r in ratings if r["concept_id"] == cid]
        info = concept_info(cid)
        concepts.append({
            "concept_id": cid,
            "concept_name": info.get("name", cid),
            "chapter_id": info.get("chapter_id"),
            "chapter_name": info.get("chapter_name"),
            "students_opened": len({v["student_id"] for v in views if v["concept_id"] == cid}),
            "students_answered": len(c_first),
            "first_try_correct": sum(a["correct"] for a in c_first),
            "first_try_accuracy": _accuracy(sum(a["correct"] for a in c_first), len(c_first)),
            "median_minutes": _minutes(median(c_reading)) if c_reading else None,
            "thumbs_up": sum(1 for x in c_ratings if x > 0),
            "thumbs_down": sum(1 for x in c_ratings if x < 0),
        })
    # Hardest first: lowest first-try accuracy; concepts nobody answered go last.
    concepts.sort(key=lambda c: (c["first_try_accuracy"] is None,
                                 c["first_try_accuracy"] if c["first_try_accuracy"] is not None else 0,
                                 -c["students_answered"], c["concept_name"]))

    # ---- misconceptions ---------------------------------------------------
    # Lessons differ per interest (different stories, different options), so a
    # wrong option is identified by (concept, interest, letter).
    answered_by: dict[tuple[str, str], set[str]] = defaultdict(set)
    for a in answers:
        answered_by[(a["concept_id"], a["interest"])].add(a["student_id"])
    wrong_by: dict[tuple[str, str, str], dict[str, Any]] = {}
    for a in answers:
        if a["correct"]:
            continue
        key = (a["concept_id"], a["interest"], a["selected"])
        entry = wrong_by.setdefault(key, {"students": set(), "sure": set(),
                                          "misconception": a.get("misconception")})
        entry["students"].add(a["student_id"])
        if a.get("confidence") == "sure":
            entry["sure"].add(a["student_id"])
        if a.get("misconception"):
            entry["misconception"] = a["misconception"]
    misconceptions = []
    for (cid, interest, letter), entry in wrong_by.items():
        check = check_info(cid, interest) or {}
        options = check.get("options") or {}
        answered = len(answered_by[(cid, interest)])
        misconceptions.append({
            "concept_id": cid,
            "concept_name": concept_info(cid).get("name", cid),
            "interest": interest,
            "question": check.get("question"),
            "option": letter,
            "option_text": options.get(letter),
            "correct_option": check.get("answer"),
            "correct_text": options.get(check.get("answer")) if check.get("answer") else None,
            "misconception": entry["misconception"],
            "students": len(entry["students"]),
            # Of those, how many were SURE: a firmly held misconception, not a slip.
            "sure": len(entry["sure"]),
            "student_ids": sorted(entry["students"]),
            "students_answered": answered,
            "share": _accuracy(len(entry["students"]), answered),
        })
    misconceptions.sort(key=lambda m: (-m["students"], -(m["share"] or 0), m["concept_name"]))

    # ---- per interest -----------------------------------------------------
    interests = []
    interest_ids = ({v["interest"] for v in views} | {a["interest"] for a in answers}
                    | {r["interest"] for r in ratings})
    for interest in sorted(interest_ids):
        i_first = [a for a in first if a["interest"] == interest]
        i_ratings = [r["rating"] for r in ratings if r["interest"] == interest]
        up = sum(1 for x in i_ratings if x > 0)
        interests.append({
            "interest": interest,
            "students": len({v["student_id"] for v in views if v["interest"] == interest}
                            | {a["student_id"] for a in answers if a["interest"] == interest}),
            "lessons_opened": sum(1 for v in views if v["interest"] == interest),
            "first_try_accuracy": _accuracy(sum(a["correct"] for a in i_first), len(i_first)),
            "thumbs_up": up,
            "thumbs_down": len(i_ratings) - up,
            "approval": _accuracy(up, len(i_ratings)),
        })

    # ---- how sure, against how right (first tries) ---------------------------
    # Well-calibrated students are right when sure and unsure when wrong. "Sure
    # and wrong" is the number a teacher should worry about.
    by_confidence = {}
    for level in ("sure", "think", "guess"):
        rows = [a for a in first if a.get("confidence") == level]
        by_confidence[level] = {"answers": len(rows),
                                "accuracy": _accuracy(sum(a["correct"] for a in rows), len(rows))}

    # ---- headline numbers -------------------------------------------------
    up_total = sum(1 for r in ratings if r["rating"] > 0)
    summary = {
        "students": len(ids),
        "active_students": len({v["student_id"] for v in views} | {a["student_id"] for a in answers}),
        "lessons_opened": len(views),
        "distinct_lessons": len({(v["student_id"], v["concept_id"]) for v in views}),
        "active_minutes": _minutes(sum(v["active_seconds"] for v in views)),
        "median_minutes_per_lesson": _minutes(median([v["active_seconds"] for v in reading]))
        if reading else None,
        "answers": len(answers),
        "first_try_answers": len(first),
        "first_try_correct": sum(a["correct"] for a in first),
        "first_try_accuracy": _accuracy(sum(a["correct"] for a in first), len(first)),
        "thumbs_up": up_total,
        "thumbs_down": len(ratings) - up_total,
        "approval": _accuracy(up_total, len(ratings)),
        "by_confidence": by_confidence,
        "sure_but_wrong": sum(1 for a in first if a.get("confidence") == "sure" and not a["correct"]),
    }

    return {
        "summary": summary,
        "misconceptions": misconceptions,
        "concepts": concepts,
        "interests": interests,
        "students": sorted(per_student.values(), key=lambda s: s["student_id"]),
    }


# ---------------------------------------------------------------------------
# Starting check -> end check (2026-10-02): the pilot's before and after.
# ---------------------------------------------------------------------------

def studied_concepts(
    activity: dict[str, list[dict[str, Any]]], until: dict[str, str | None]
) -> dict[str, set[str]]:
    """{student_id: concepts whose lesson they opened or answered}, counting
    only activity before their end check (`until`, an ISO time or None)."""
    out: dict[str, set[str]] = defaultdict(set)
    for kind, at in (("views", "opened_at"), ("answers", "answered_at")):
        for row in activity.get(kind, []):
            cutoff = until.get(row["student_id"])
            if cutoff is None or row[at] < cutoff:
                out[row["student_id"]].add(row["concept_id"])
    return out


def check_gains(
    comparisons: dict[str, dict[str, Any]],
    started: int,
    concept_info: Callable[[str], dict[str, Any]],
) -> dict[str, Any]:
    """A class's before -> after, from each student's `diagnostic.compare` result.

    `comparisons` holds only students who took BOTH checks; `started` counts
    those who took the starting check. Rates are 0-1 (None when nothing to
    divide). Every number is over paired answers: the same concept, before and
    after, so students who skipped one check don't distort it.

    Returns {students_started, students_finished, paired_answers,
             before: {right, mix_up, unsure}, after: {...},
             right_before, right_after (rates), fixed, learned, slipped,
             studied: {pairs, right_before, right_after},
             not_studied: {...},
             concepts: [{concept_id, concept_name, chapter_name, students,
                         right_before, right_after, fixed}] (biggest gain first)}
    """
    pairs = [c for comp in comparisons.values() for c in comp["concepts"]]

    def rate(rows: list[dict[str, Any]], key: str) -> float | None:
        return _accuracy(sum(1 for r in rows if r[key] == "right"), len(rows))

    def split(rows: list[dict[str, Any]]) -> dict[str, Any]:
        return {"pairs": len(rows), "right_before": rate(rows, "before"),
                "right_after": rate(rows, "after")}

    by_concept: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for c in pairs:
        by_concept[c["concept_id"]].append(c)
    concepts = []
    for concept_id, rows in by_concept.items():
        info = concept_info(concept_id)
        concepts.append({
            "concept_id": concept_id,
            "concept_name": info.get("name", concept_id),
            "chapter_name": info.get("chapter_name"),
            "students": len(rows),
            "right_before": rate(rows, "before"),
            "right_after": rate(rows, "after"),
            "fixed": sum(1 for r in rows if r["before"] == "mix_up" and r["after"] == "right"),
        })
    concepts.sort(key=lambda c: (-((c["right_after"] or 0) - (c["right_before"] or 0)),
                                 c["concept_name"]))

    def total(key: str) -> int:
        return sum(comp[key] for comp in comparisons.values())

    return {
        "students_started": started,
        "students_finished": len(comparisons),
        "paired_answers": len(pairs),
        "before": {k: sum(1 for c in pairs if c["before"] == k) for k in ("right", "mix_up", "unsure")},
        "after": {k: sum(1 for c in pairs if c["after"] == k) for k in ("right", "mix_up", "unsure")},
        "right_before": rate(pairs, "before"),
        "right_after": rate(pairs, "after"),
        "fixed": total("fixed"),
        "learned": total("learned"),
        "slipped": total("slipped"),
        "studied": split([c for c in pairs if c["studied"]]),
        "not_studied": split([c for c in pairs if not c["studied"]]),
        "concepts": concepts,
    }


# ---------------------------------------------------------------------------
# AI usage and cost (2026-10-03): the evidence behind "₹X per student".
# ---------------------------------------------------------------------------

def _price_for(model: str, prices: dict[str, Any]) -> dict[str, float] | None:
    """The longest price key the model name contains, or None (unpriced)."""
    name = (model or "").lower()
    matches = [k for k in (prices.get("models") or {}) if k.lower() in name]
    return prices["models"][max(matches, key=len)] if matches else None


def _usd(price: dict[str, float] | None, prompt: int | None, completion: int | None) -> float:
    if not price:
        return 0.0
    return ((prompt or 0) * price["input"] + (completion or 0) * price["output"]) / 1_000_000


def ai_usage(calls: list[dict[str, Any]], prices: dict[str, Any], students: int) -> dict[str, Any]:
    """Model calls, tokens and cost, per feature and per student.

    Two costs: `actual` prices each call at its own model (unlisted models,
    such as free ones, cost 0); `reference` prices every call at
    prices["reference_model"], i.e. what the same usage would cost on the paid
    key. Calls without token counts (the doubt chat's older pipeline) are
    counted but can't be priced; `calls_without_tokens` says how many.

    Per-student numbers divide by `students` (everyone in the pilot, not only
    those whose actions triggered a call) and, per month, scale by the days
    between the first and last call.
    """
    rate = float(prices.get("usd_to_inr") or 0)
    reference = (prices.get("models") or {}).get(prices.get("reference_model") or "")

    def summarise(rows: list[dict[str, Any]]) -> dict[str, Any]:
        with_tokens = [r for r in rows if r.get("prompt_tokens") is not None
                       or r.get("completion_tokens") is not None]
        latencies = [r["latency_ms"] for r in rows if r.get("latency_ms") is not None]
        actual = sum(_usd(_price_for(r["model"], prices), r.get("prompt_tokens"),
                          r.get("completion_tokens")) for r in rows)
        ref = sum(_usd(reference, r.get("prompt_tokens"), r.get("completion_tokens")) for r in rows)
        return {
            "calls": len(rows),
            "failed": sum(1 for r in rows if not r["ok"]),
            "calls_without_tokens": len(rows) - len(with_tokens),
            "prompt_tokens": sum(r.get("prompt_tokens") or 0 for r in rows),
            "completion_tokens": sum(r.get("completion_tokens") or 0 for r in rows),
            "median_latency_ms": int(median(latencies)) if latencies else None,
            "actual_inr": round(actual * rate, 2),
            "reference_inr": round(ref * rate, 2),
        }

    by_feature = {}
    for feature in sorted({c["feature"] for c in calls}):
        by_feature[feature] = summarise([c for c in calls if c["feature"] == feature])
    total = summarise(calls)
    days = 1.0
    if calls:
        first = min(c["at"] for c in calls)
        last = max(c["at"] for c in calls)
        span = (datetime.fromisoformat(last) - datetime.fromisoformat(first)).total_seconds() / 86400
        days = max(1.0, span)
    per_student = (total["reference_inr"] / students) if students else None
    return {
        "total": total,
        "by_feature": by_feature,
        "models": sorted({c["model"] for c in calls}),
        "reference_model": prices.get("reference_model"),
        "students": students,
        "days": round(days, 1),
        "reference_inr_per_student": round(per_student, 2) if per_student is not None else None,
        "reference_inr_per_student_month": (round(per_student / days * 30, 2)
                                            if per_student is not None else None),
    }


# ---------------------------------------------------------------------------
# The survey ("getting to know you") in the pilot report
# ---------------------------------------------------------------------------

# The trait fields exported and compared, flattened from the stored `traits` dict.
SURVEY_FIELDS = ("focus_span", "session_minutes", "focus_drift", "pace", "first_step",
                 "physics_feel", "maths_comfort", "trips", "goal", "top_hobby",
                 "top_hobby_level", "hobbies")


def survey_fields(traits: dict[str, Any]) -> dict[str, Any]:
    """A student's survey traits as one flat row (fixed-option answers only; no free text exists)."""
    focus, learning, physics = (traits.get("focus") or {}), (traits.get("learning") or {}), (traits.get("physics") or {})
    levels = traits.get("hobby_levels") or {}
    top = next(iter(levels), None)
    return {
        "focus_span": focus.get("span"), "session_minutes": focus.get("session_minutes"),
        "focus_drift": focus.get("drift"), "pace": learning.get("pace"),
        "first_step": learning.get("first_step"), "physics_feel": physics.get("feel"),
        "maths_comfort": physics.get("maths"), "trips": physics.get("trips"), "goal": physics.get("goal"),
        "top_hobby": top, "top_hobby_level": levels[top]["level"] if top else None,
        "hobbies": ",".join(traits.get("hobbies") or []) or None,
    }


def survey_changes(sets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """What changed between consecutive answer sets of ONE student.

    `sets` is oldest first: [{revision, saved_at, traits}, ...] with the current answers last.
    Returns [{revision (of the NEW set), saved_at (when the old set was replaced), field, from, to}].
    """
    out = []
    for before, after in zip(sets, sets[1:]):
        a, b = survey_fields(before["traits"]), survey_fields(after["traits"])
        for field in SURVEY_FIELDS:
            if a[field] != b[field]:
                out.append({"revision": after["revision"], "saved_at": after.get("saved_at"),
                            "field": field, "from": a[field], "to": b[field]})
    return out


def survey_report(entries: list[dict[str, Any]], history: dict[str, list[dict[str, Any]]],
                  total_students: int) -> dict[str, Any]:
    """The survey side of the pilot: who answered, what they said, how it changed, and how
    what they SAID lines up with what they DID.

    `entries`: one per student who took it: {student_id, revision, saved_at, traits,
    observed: {views, median_minutes, skim_share}, first_try_correct, answered}.
    `history`: {student_id: [{revision, saved_at, traits}, ...]} of the answer sets they
    REPLACED (oldest first); the current answers come from `entries`.

    "said_vs_shown" is an ASSOCIATION across a handful of students, never evidence that an
    adaptation works: it only shows whether what students say predicts how they read.
    """
    rows, hist_rows, changes = [], [], []
    for e in entries:
        flat = survey_fields(e["traits"])
        obs = e.get("observed") or {}
        rows.append({"student_id": e["student_id"], "revision": e["revision"], **flat,
                     "lessons_viewed": obs.get("views"), "median_minutes_per_lesson": obs.get("median_minutes"),
                     "skim_share": obs.get("skim_share"), "first_try_correct": e.get("first_try_correct"),
                     "first_try_answered": e.get("answered")})
        sets = list(history.get(e["student_id"], []))
        for h in sets:
            hist_rows.append({"student_id": e["student_id"], "revision": h["revision"],
                              "saved_at": h.get("saved_at"), "current": False, **survey_fields(h["traits"])})
        hist_rows.append({"student_id": e["student_id"], "revision": e["revision"],
                          "saved_at": e.get("saved_at"), "current": True, **flat})
        changes += [{"student_id": e["student_id"], **c}
                    for c in survey_changes(sets + [{"revision": e["revision"], "saved_at": e.get("saved_at"),
                                                     "traits": e["traits"]}])]

    def counts(field: str) -> dict[str, int]:
        tally: dict[str, int] = {}
        for r in rows:
            if r[field] is not None:
                tally[r[field]] = tally.get(r[field], 0) + 1
        return dict(sorted(tally.items(), key=lambda kv: (-kv[1], kv[0])))

    def group(field: str) -> list[dict[str, Any]]:
        out = []
        for value in counts(field):
            members = [r for r in rows if r[field] == value]
            mins = [r["median_minutes_per_lesson"] for r in members if r["median_minutes_per_lesson"] is not None]
            skims = [r["skim_share"] for r in members if r["skim_share"] is not None]
            answered = sum(r["first_try_answered"] or 0 for r in members)
            correct = sum(r["first_try_correct"] or 0 for r in members)
            out.append({"value": value, "students": len(members),
                        "median_minutes": round(median(mins), 1) if mins else None,
                        "mean_skim_share": round(sum(skims) / len(skims), 2) if skims else None,
                        "first_try_accuracy": _accuracy(correct, answered), "first_try_answers": answered})
        return out

    updated = {c["student_id"] for c in changes} | {e["student_id"] for e in entries if e["revision"]}
    return {
        "taken": len(entries), "total": total_students,
        "updated_students": len(updated), "revisions": sum(e["revision"] for e in entries),
        "changed_fields": counts_of([c["field"] for c in changes]),
        "distributions": {f: counts(f) for f in ("focus_span", "pace", "first_step", "physics_feel",
                                                 "maths_comfort", "trips", "goal", "top_hobby_level")},
        "said_vs_shown": {f: group(f) for f in ("focus_span", "pace", "physics_feel")},
        "rows": rows, "history": hist_rows, "changes": changes,
    }


def counts_of(values: list[str]) -> dict[str, int]:
    tally: dict[str, int] = {}
    for v in values:
        tally[v] = tally.get(v, 0) + 1
    return dict(sorted(tally.items(), key=lambda kv: (-kv[1], kv[0])))
