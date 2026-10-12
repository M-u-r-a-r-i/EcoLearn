"""Personal stories (layer 3, option b): a lesson opening written for one student.

WHAT A STUDENT GETS
A short story and one analogy framed through one of their hobbies, shown above
the reviewed lesson, with the lesson's own pre-written story one click away.
The lesson below (physics, worked example, takeaway, check) never changes.

HOW IT IS MADE — two agents and four guards
1. Pick a hobby that FITS the concept's physics domain (data/diagnostic.yaml).
   No fit, no story: the student just gets the pre-written lesson.
2. The writer agent gets the lesson's own physics text and takeaway (the only
   facts it may use), the hobby, and this student's open mix-up on the concept
   if there is one. It never gets a name, username or id.
3. Automatic guards, before any model judges it: valid JSON, lengths, and NO
   DIGITS at all — a number the lesson didn't state is the easiest way for a
   model to invent physics, so the prompt bans them and the code checks.
4. The critic agent (a second call, strict, low temperature) checks physics
   against the lesson, the analogy's mapping, the limit sentence, safety, and
   that a staged mix-up gets resolved.
5. One retry with the problems fed back; then give up and fall back.
6. Fail CLOSED: an unreadable critic verdict is a FAIL. The older judges fail
   open (availability first); for content minors read before a lesson,
   correctness comes first, and the fallback is the reviewed story anyway.

WHEN
Generation runs in the background (a small thread pool in the API process),
for the lesson being opened and the next two in the chapter, so a student
normally finds their story ready. The page polls while one is being written.
A story is cached per student × concept and retired when the lesson text it
was based on changes.

Models come from src/llm (OmniRoute / any OpenAI-compatible endpoint). With no
model configured, nothing is generated and every lesson shows as before.
"""

from __future__ import annotations

import hashlib
import re
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable

from src import llm
from src.content import lesson_service
from src.learner import diagnostic, plan, survey
from src.llm.client import parse_json_object
from src.path import engine
from src.progress import store

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_WRITER_PROMPT = _PROJECT_ROOT / "prompts" / "personal_story_writer.txt"
_CRITIC_PROMPT = _PROJECT_ROOT / "prompts" / "personal_story_critic.txt"

READY, NO_FIT, FAILED, ERROR = "ready", "no_fit", "failed", "error"
MAX_ATTEMPTS = 2
_FORMAT_RETRIES = 2  # extra calls when the reply isn't JSON (they don't count as attempts)
# After a connection error (gateway down, rate limit), wait before trying again.
RETRY_AFTER_ERROR = timedelta(minutes=30)
# Word limits, a little looser than the prompt's, so near-misses aren't wasted.
_LIMITS = {"story": (40, 160), "analogy": (15, 100), "limit": (5, 50)}
_SECTION_CHARS = 2500  # how much of "The physics" the writer sees

# Swappable in tests: (messages, role=..., temperature=..., max_tokens=...) -> ChatResult
chat: Callable[..., Any] = llm.chat
# Tests set this to run generation inline instead of on the thread pool.
SYNC = False

_pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="story")
_inflight: set[tuple[str, str]] = set()
_lock = threading.Lock()


# ---------------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------------

def _hobby_table() -> dict[str, dict[str, Any]]:
    return {h["id"]: h for h in diagnostic.hobby_options()}


def choose_hobby(hobbies: list[str], interest: str, domain: str | None) -> dict[str, str] | None:
    """The first of the student's hobbies that fits this physics domain.

    Listed hobbies need `domain` in their `fits` and must not be the student's
    own lesson interest (the lesson is already written for that). A hobby of
    their own has no list, so it's offered to the writer, which may decline.
    Returns {"id", "label", "emoji"} or None.
    """
    table = _hobby_table()
    for h in hobbies:
        option = table.get(h)
        if option and option.get("interest") != interest and domain in (option.get("fits") or []):
            return {"id": h, "label": option["label"], "emoji": option.get("emoji", "")}
    for h in hobbies:
        if h not in table:
            return {"id": h, "label": h.capitalize(), "emoji": "✨"}
    return None


def lesson_source(concept_id: str, interest: str) -> dict[str, str] | None:
    """The reviewed lesson text the writer must stay inside, plus its hash."""
    authored = lesson_service.get_authored_lesson(concept_id, interest)
    if authored is None:
        return None
    sections = {s["heading"]: s["markdown"] for s in lesson_service.student_view(authored)["sections"]}
    physics = (sections.get("The physics") or "")[:_SECTION_CHARS]
    takeaway = sections.get("Key takeaway") or ""
    if not physics and not takeaway:
        return None
    digest = hashlib.sha256(f"{physics}\n{takeaway}".encode("utf-8")).hexdigest()[:16]
    return {"physics": physics, "takeaway": takeaway, "hash": digest}


def _first_sentence(text: str) -> str:
    match = re.match(r"^(.+?[.!?])(?=\s+[A-Z]|\s*$)", (text or "").strip(), re.DOTALL)
    return match.group(1) if match else (text or "").strip()


def _context(student_id: str, concept_id: str) -> dict[str, Any] | None:
    """Everything needed to write one story, or None if there's nothing to write."""
    profile = store.get_student(student_id)
    concept = engine.find_concept(concept_id)
    if profile is None or concept is None:
        return None
    chapters = {c["id"]: c for c in engine.list_chapters()}
    domain = chapters.get(concept.chapter_id, {}).get("domain")
    saved = store.get_survey(student_id)
    traits = saved["traits"] if saved else None
    # The hobby they know best goes first (survey.order_hobbies; unchanged when no survey).
    hobbies = survey.order_hobbies(store.get_learner_profile(student_id)["hobbies"], traits)
    hobby = choose_hobby(hobbies, profile["interest"], domain)
    source = lesson_source(concept_id, profile["interest"])
    if hobby is None or source is None:
        return None
    mix_up = plan.learner_state(student_id)["mix_ups"].get(concept_id)
    return {"concept": concept, "hobby": hobby, "source": source,
            "level": profile["level"],
            "notes": survey.story_notes(traits, hobby["id"]) if hobby else [],
            "mix_up": _first_sentence(mix_up["text"]) if mix_up else None}


# ---------------------------------------------------------------------------
# The agents
# ---------------------------------------------------------------------------

def _facts(ctx: dict[str, Any]) -> str:
    c = ctx["concept"]
    return (f"Concept: {c.name}\nLevel: {ctx['level']}\n"
            f"The student should be able to: {c.learning_objective}\n\n"
            f"THE LESSON'S PHYSICS TEXT (source of truth):\n{ctx['source']['physics']}\n\n"
            f"THE LESSON'S KEY TAKEAWAY:\n{ctx['source']['takeaway']}\n")


def writer_messages(ctx: dict[str, Any]) -> list[dict[str, str]]:
    prompt = _WRITER_PROMPT.read_text(encoding="utf-8")
    mix_up = (f"This student's mix-up on this concept: {ctx['mix_up']}\n" if ctx["mix_up"]
              else "No mix-up recorded for this concept.\n")
    # What the student said about themselves (coarse categories only, never raw answers).
    notes = "".join(f"Note: {n}\n" for n in ctx.get("notes", []))
    notes = f"{notes}\n" if notes else ""
    # The instructions travel in the user message: every model accepts that
    # (Gemma has no system role; free gateway models vary).
    return [{"role": "user", "content": (
        f"{prompt}\n\n---\n{_facts(ctx)}\nHobby: {ctx['hobby']['label']}\n{mix_up}\n"
        f"{notes}Write the JSON now.")}]


def guard_problems(draft: dict[str, Any]) -> list[str]:
    """Deterministic checks, run before the critic sees anything."""
    problems = []
    for key, (low, high) in _LIMITS.items():
        text = draft.get(key)
        if not isinstance(text, str) or not text.strip():
            problems.append(f"'{key}' is missing.")
            continue
        words = len(text.split())
        if not low <= words <= high:
            problems.append(f"'{key}' has {words} words; keep it between {low} and {high}.")
        if re.search(r"\d", text):
            problems.append(f"'{key}' contains digits. Write no numbers at all; use words.")
        if re.search(r"https?://|www\.|@|\$", text):
            problems.append(f"'{key}' contains a link, an @ or maths notation; plain words only.")
    return problems


def critic_verdict(ctx: dict[str, Any], draft: dict[str, Any]) -> tuple[bool, list[str], str]:
    """(passed, problems, model). An unreadable verdict counts as a FAIL."""
    prompt = _CRITIC_PROMPT.read_text(encoding="utf-8")
    message = (f"{prompt}\n\n---\n{_facts(ctx)}\nHobby: {ctx['hobby']['label']}\n\n"
               f"THE DRAFT\nStory: {draft['story']}\n\nAnalogy: {draft['analogy']}\n\n"
               f"Limit: {draft['limit']}\n\nGive your verdict as JSON now.")
    with llm.usage_context(feature="story_critic"):  # the usage log's label
        result = chat([{"role": "user", "content": message}], role="critic",
                      temperature=0.0, max_tokens=400)
    verdict = parse_json_object(result.text)
    if not verdict or verdict.get("verdict") not in ("PASS", "FAIL"):
        return False, ["The checker's answer couldn't be read."], result.model
    problems = [str(p) for p in (verdict.get("problems") or []) if str(p).strip()]
    return verdict["verdict"] == "PASS", problems, result.model


def generate(student_id: str, concept_id: str) -> dict[str, Any] | None:
    """Write, check and store one story. Returns the stored row (None: nothing to write)."""
    ctx = _context(student_id, concept_id)
    if ctx is None:
        return None
    row: dict[str, Any] = {"student_id": student_id, "concept_id": concept_id,
                           "hobby": ctx["hobby"]["id"], "lesson_hash": ctx["source"]["hash"]}
    messages = writer_messages(ctx)
    problems: list[str] = []
    model = None
    # The decision trail (2026-10-03): every step's verdict, so a teacher can see
    # how a story was checked ("How the AI decided"). Steps: format (was the
    # draft readable JSON), fit (the writer declined), rules (guard_problems),
    # critic (the second model's verdict), model (a call failed).
    trail: list[dict[str, Any]] = []

    def step(attempt: int, name: str, passed: bool, found: list[str] | None = None,
             by: str | None = None) -> None:
        trail.append({"attempt": attempt, "step": name, "passed": passed,
                      "problems": list(found or [])[:5], "model": by})

    attempt = 0
    try:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            # A reply that isn't JSON at all is a transport hiccup more than a bad draft (seen live:
            # 3 of 25 demo stories died on it, yet the same prompt parsed 3 of 3 a day later), so it
            # gets up to two more tries without using up a real attempt, and the start of the reply is
            # kept in the trail so the cause can be diagnosed next time.
            for _try in range(1 + _FORMAT_RETRIES):
                result = chat(messages, role="main", temperature=0.7, max_tokens=900)
                model = result.model
                draft = parse_json_object(result.text)
                if draft is not None:
                    break
                snippet = " ".join((result.text or "").split())[:120]
                step(attempt, "format", False,
                     [f"Not a JSON object ({len(result.text or '')} characters): {snippet!r}"], model)
            if draft is not None and draft.get("fit") is False:
                step(attempt, "fit", False, ["The writer found no honest link to this hobby."], model)
                store.save_personal_story({**row, "status": NO_FIT, "model": model,
                                           "attempts": attempt, "trail": trail})
                return store.get_personal_story(student_id, concept_id)
            if draft is None:
                problems = ["The answer wasn't a JSON object."]
            else:
                problems = guard_problems(draft)
                step(attempt, "rules", not problems, problems, model)
                if not problems:
                    passed, problems, critic_model = critic_verdict(ctx, draft)
                    step(attempt, "critic", passed, problems, critic_model)
                    if passed:
                        store.save_personal_story({
                            **row, "status": READY, "model": model, "attempts": attempt,
                            "story": draft["story"].strip(), "analogy": draft["analogy"].strip(),
                            "limit_text": draft["limit"].strip(), "trail": trail})
                        return store.get_personal_story(student_id, concept_id)
            messages = messages + [
                {"role": "assistant", "content": result.text or ""},
                {"role": "user", "content": "A checker found these problems:\n- "
                 + "\n- ".join(problems or ["unspecified"])
                 + "\nRewrite it to fix every one, following all the rules. JSON only."},
            ]
        store.save_personal_story({**row, "status": FAILED, "model": model,
                                   "attempts": MAX_ATTEMPTS, "problems": problems, "trail": trail})
    except llm.LLMError as exc:
        step(max(attempt, 1), "model", False, [str(exc)[:300]], model)
        store.save_personal_story({**row, "status": ERROR, "model": model,
                                   "problems": [str(exc)[:300]], "trail": trail})
    return store.get_personal_story(student_id, concept_id)


# ---------------------------------------------------------------------------
# Scheduling and serving
# ---------------------------------------------------------------------------

def _is_current(row: dict[str, Any] | None, ctx: dict[str, Any]) -> bool:
    """Does a stored row still answer for this lesson text and this hobby?"""
    if row is None or row["lesson_hash"] != ctx["source"]["hash"] or row["hobby"] != ctx["hobby"]["id"]:
        return False
    if row["status"] == ERROR:
        made = datetime.fromisoformat(row["created_at"])
        return datetime.now(tz=timezone.utc) - made < RETRY_AFTER_ERROR
    return True


def _run(student_id: str, concept_id: str) -> None:
    try:
        # Labels every model call in the usage log (the critic relabels its own).
        with llm.usage_context(feature="story_writer", student_id=student_id):
            generate(student_id, concept_id)
    except Exception:  # noqa: BLE001 — a background failure must never surface
        pass
    finally:
        with _lock:
            _inflight.discard((student_id, concept_id))


def request(student_id: str, concept_id: str) -> None:
    """Start writing this story in the background if it's needed and not under way."""
    if not llm.is_configured():
        return
    ctx = _context(student_id, concept_id)
    if ctx is None or _is_current(store.get_personal_story(student_id, concept_id), ctx):
        return
    key = (student_id, concept_id)
    with _lock:
        if key in _inflight:
            return
        _inflight.add(key)
    if SYNC:
        _run(student_id, concept_id)
    else:
        _pool.submit(_run, student_id, concept_id)


def view(student_id: str, concept_id: str) -> dict[str, Any]:
    """What the lesson page shows, and kicks off writing if needed.

    {"status": "ready", "hobby", "emoji", "story", "analogy", "limit"}
    {"status": "pending", "hobby", "emoji"}   — being written; poll again
    {"status": "none"}                        — show the pre-written story
    """
    ctx = _context(student_id, concept_id)
    if ctx is None:
        return {"status": "none"}
    request(student_id, concept_id)
    row = store.get_personal_story(student_id, concept_id)
    hobby = {"hobby": ctx["hobby"]["label"], "emoji": ctx["hobby"]["emoji"]}
    if row is not None and _is_current(row, ctx):
        # Reported by the student or hidden by a teacher: the reviewed story
        # only. It stays "current", so the same lesson never rewrites it.
        if row["status"] == READY and not row.get("hidden"):
            return {"status": "ready", **hobby, "story": row["story"],
                    "analogy": row["analogy"], "limit": row["limit_text"]}
        return {"status": "none"}
    with _lock:
        writing = (student_id, concept_id) in _inflight
    return {"status": "pending", **hobby} if writing else {"status": "none"}
