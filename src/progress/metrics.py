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
        entry = wrong_by.setdefault(key, {"students": set(), "misconception": a.get("misconception")})
        entry["students"].add(a["student_id"])
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
