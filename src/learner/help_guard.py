"""The doubt chat's front door: screen what a student types, and slow down floods.

WHY THIS EXISTS
The doubt chat is the one place where words a student typed go straight to a live model
(the other AI features only ever see our own text and fixed-option answers). That makes it
the weakest point of the AI safety card, so it gets its own guard, in two parts, neither of
which costs a model call:

  1. `screen(question)`: deterministic checks before anything is sent. A question that
     matches is NOT sent to a model; the student gets a short, kind reply instead.
       * self_harm     a warm message pointing to a trusted adult and a free helpline. It
                       is never rate-limited away: a student in distress must not be told
                       to "slow down".
       * personal_info a phone number, email, link, or home address. We don't want it, and a
                       model must never receive it.
       * unsuitable    sexual content, how-to requests for weapons or drugs, wanting to hurt
                       someone, gambling.
       * injection     "ignore your instructions", "show your prompt", "pretend you are...".
       * too_short / too_long   not a question yet, or an essay.
  2. `HelpLimiter`: per student, a few questions in a short window, a daily cap, and one
     question being answered at a time (an answer takes up to a couple of minutes of model
     time, so a flood is expensive and can starve everyone else).

WHAT IT DOES NOT DO (written down so nobody mistakes it for more)
  * It is a floor, not a classifier. Regular expressions catch clear cases in English only;
    misspellings, other languages and creative phrasing pass. The model's own safety
    settings and the critic are the next layers, and a teacher can see how many questions
    were stopped (counts only).
  * It does not decide whether a question is about physics. It stops harmful or unsafe
    text, not off-topic text.
  * The question text is never stored. Only the outcome (answered, blocked and why, slowed
    down, failed) is recorded, so a teacher sees counts and never a child's words.
  * What happens after a self-harm message (does the school's counsellor get told?) is a
    decision for the school and is deliberately not automated here. See docs/ai-safety-card.html.
  * The limiter is in memory and per process, like the login limiter (api/ratelimit.py).
"""

from __future__ import annotations

import os
import re
import threading
import time
import unicodedata
from collections import defaultdict, deque
from dataclasses import dataclass

MAX_QUESTION_CHARS = 600
MIN_LETTERS = 3

# Verified 2026-10-13: Tele-MANAS is India's free, 24/7 national tele-mental-health helpline
# (14416, also 1-800-891-4416); 112 is the national emergency number. Re-check before the pilot.
HELPLINE = "Tele-MANAS, a free helpline that is open any time, on 14416"
EMERGENCY = "112"


def _flags(*patterns: str) -> re.Pattern[str]:
    return re.compile("|".join(f"(?:{p})" for p in patterns), re.IGNORECASE | re.DOTALL)


_SELF_HARM = _flags(
    r"\bkill(ing)? my ?self\b", r"\bend(ing)? my (own )?life\b", r"\bend it all\b",
    r"\btake my (own )?life\b", r"\bsuicid\w*", r"\bwant(ed)? to die\b", r"\bwanna die\b",
    r"\b(hurt|harm|cut|cutting|hurting|harming) my ?self\b", r"\bself[- ]?harm\w*",
    r"\bdon'?t want to (live|be alive|exist|be here)\b", r"\bno (reason|point) (to|in) (live|living)\b",
    r"\bbetter off dead\b", r"\bkill me\b",
)
_PERSONAL = _flags(
    r"[\w.+-]+@[\w-]+\.[\w.-]+",                                   # an email address
    r"https?://", r"\bwww\.", r"\b[\w-]+\.(com|in|org|net|io|me)\b",  # a link or a website
    r"(?<![\d.])(?:\+?\d[\s-]?){10,13}(?![\d.])",                   # a phone number
    r"\bmy (home |full |house )?address\b", r"\bi live (at|on)\b",
    r"\bmy (phone|mobile|contact|whatsapp) (number|no)\b", r"\bwhats ?app\b", r"\bcall me (on|at)\b",
)
_UNSUITABLE = _flags(
    r"\b(porn\w*|nude\w*|naked|sexting|onlyfans|hentai)\b", r"\bsex(ual)? (video|chat|story|pictures?|photos?)\b",
    r"\b(how (do i|to|can i|would i)|ways to|steps (to|for)|teach me to|instructions (to|for))\b.{0,30}"
    r"\b(make|build|create|cook|synthesi[sz]e|get|buy)\b.{0,30}"
    r"\b(bombs?|explosives?|weapons?|guns?|poison|meth|cocaine|drugs?|napalm|thermite|grenades?)\b",
    r"\b(kill|hurt|harm|poison|stab|shoot|beat up)\b (him|her|them|someone|somebody|my (teacher|friend|classmate|"
    r"brother|sister|parents?|mom|dad))\b",
    r"\b(online casino|sports betting|betting (app|site|tips)|place a bet)\b",
)
_INJECTION = _flags(
    r"\b(ignore|disregard|forget|override|bypass)\b.{0,25}\b(previous|prior|above|all|any|your|the|these)\b.{0,25}"
    r"\b(instructions?|rules?|prompts?|guidelines?|restrictions?)\b",
    r"\b(system|hidden|secret|original) prompt\b",
    r"\b(reveal|show|print|repeat|tell me)\b.{0,20}\b(your|the) (prompt|instructions|rules)\b",
    r"\byou are now\b", r"\bpretend (to be|you are|you're)\b", r"\bjailbreak\w*", r"\b(dan|developer) mode\b",
    r"\bfrom now on,? you\b",
)


def _school_line() -> str:
    extra = (os.getenv("ECOLEARN_SCHOOL_SUPPORT") or "").strip()
    return f" {extra}" if extra else ""


def _messages() -> dict[str, str]:
    return {
        "self_harm": (
            "I'm really glad you said something, and I'm sorry things feel this heavy. This isn't something "
            "I can help with in a physics chat, but you don't have to carry it alone. Please talk to someone "
            "you trust today: a parent, a teacher or your school counsellor. You can also call "
            f"{HELPLINE}. If you are in danger right now, call {EMERGENCY}.{_school_line()}"),
        "personal_info": (
            "Please don't share personal details here, such as a phone number, an email, a link or where you "
            "live. Ask your physics question without them and I'll help."),
        "unsuitable": (
            "That isn't something I can help with here. If you're stuck on this lesson, ask it as a physics "
            "question and I'll explain it."),
        "injection": "I can only answer physics questions about this lesson. What would you like to understand?",
        "too_short": "Ask me a full question about this lesson, for example \"Why does the ball keep moving?\"",
        "too_long": (f"That's a bit long for a question. Try asking it in a sentence or two "
                     f"(up to {MAX_QUESTION_CHARS} characters)."),
    }


@dataclass(frozen=True)
class Screen:
    ok: bool
    reason: str | None = None     # self_harm | personal_info | unsuitable | injection | too_short | too_long
    message: str | None = None    # what to show the student when not ok


def _normalise(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "").replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", text).strip()


def screen(question: str) -> Screen:
    """Decide whether a question may go to a model. Order matters: safety first."""
    text = _normalise(question)
    messages = _messages()
    if len(text) > MAX_QUESTION_CHARS:
        return Screen(False, "too_long", messages["too_long"])
    # Self-harm is checked first and on its own: it wins over every other category.
    for reason, pattern in (("self_harm", _SELF_HARM), ("personal_info", _PERSONAL),
                            ("unsuitable", _UNSUITABLE), ("injection", _INJECTION)):
        if pattern.search(text):
            return Screen(False, reason, messages[reason])
    if sum(c.isalpha() for c in text) < MIN_LETTERS:
        return Screen(False, "too_short", messages["too_short"])
    return Screen(True)


# ---------------------------------------------------------------------------
# Rate limit
# ---------------------------------------------------------------------------

def _env_int(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, "") or default)
    except ValueError:
        return default


class HelpLimiter:
    """Per student: N questions per short window, a daily cap, one answer in flight at a time."""

    def __init__(self, per_window: int | None = None, window_seconds: int | None = None,
                 per_day: int | None = None, clock=time.monotonic):
        self.per_window = per_window or _env_int("ECOLEARN_HELP_PER_WINDOW", 5)
        self.window = window_seconds or _env_int("ECOLEARN_HELP_WINDOW_SECONDS", 10 * 60)
        self.per_day = per_day or _env_int("ECOLEARN_HELP_PER_DAY", 30)
        self._clock = clock
        self._lock = threading.Lock()
        self._asked: dict[str, deque[float]] = defaultdict(deque)
        self._busy: set[str] = set()

    def try_start(self, student_id: str) -> tuple[bool, int, str | None]:
        """(allowed, retry_after_seconds, reason). Reason: busy | slow_down | daily | None.

        An allowed call counts as a question and marks the student busy: pair it with `finish`.
        """
        now = self._clock()
        with self._lock:
            if student_id in self._busy:
                return False, 15, "busy"
            asked = self._asked[student_id]
            while asked and now - asked[0] > 86400:
                asked.popleft()
            if len(asked) >= self.per_day:
                return False, int(86400 - (now - asked[0])) + 1, "daily"
            recent = [t for t in asked if now - t <= self.window]
            if len(recent) >= self.per_window:
                return False, int(self.window - (now - recent[0])) + 1, "slow_down"
            asked.append(now)
            self._busy.add(student_id)
            return True, 0, None

    def finish(self, student_id: str) -> None:
        with self._lock:
            self._busy.discard(student_id)


def limit_message(reason: str | None, retry_after: int) -> str:
    minutes = max(1, round(retry_after / 60))
    if reason == "busy":
        return "I'm still answering your last question. Give me a moment, then ask again."
    if reason == "daily":
        return "That's a lot of questions for one day. Take a break, and ask your teacher if you're still stuck."
    return (f"You've asked a few questions in a row. Take a short break, re-read the lesson, and try again in "
            f"about {minutes} minute{'s' if minutes != 1 else ''}.")
