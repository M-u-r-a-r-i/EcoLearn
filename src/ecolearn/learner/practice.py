"""Practice with AI (2026-10-19): an extra multiple-choice question on the idea a student just studied.

The FIFTH live-AI place, approved by the user on 2026-10-19 instead of letting AI run the graded checks. The graded
checks stay fixed, pre-written and pre-checked, because the pilot's numbers (first-try accuracy, mastery, the end
check, the randomised comparison) only mean something if everyone answers the same validated questions. Practice is
optional and NEVER counts: it writes nothing to progress, answers, mastery or the pilot metrics.

The real risk is a plausible question with a WRONG answer key (a loud failure is easy to catch; a confident wrong
one is not). So every question passes three gates before a student sees it:
  1. the WRITER (one call through src/ecolearn/llm) is grounded in the student's own lesson and its known mix-ups;
  2. RULES check the shape: four distinct options A-D, an answer among them, lengths, no links or emails, and not a
     copy of the lesson's own check;
  3. a SOLVER (a second call, the "critic" model role, which never sees the key) answers the question itself; the
     question is used only if its answer matches the writer's key.
If anything fails, there is no question ("couldn't write one just now"): never a half-checked one. The key and the
explanation stay on the server until the student answers. Two calls when both pass; at most three writer attempts.

A same-model solver is a weaker check than a different model: set LLM_CRITIC_MODEL to use another one. Even with
both gates a question can still be wrong, and the page says so.

Pure except the model calls, which come in as `chat` (llm.chat, or a test stand-in).
"""

from __future__ import annotations

from ecolearn.paths import PROJECT_ROOT
import re
from difflib import SequenceMatcher
from typing import Any, Callable

from ecolearn.llm.client import LLMError, parse_json_object

_PROMPTS = PROJECT_ROOT / "prompts"
LETTERS = ("A", "B", "C", "D")
MAX_ATTEMPTS = 3
_QUESTION_WORDS = (6, 90)
_OPTION_WORDS = (1, 30)
_EXPLANATION_WORDS = (8, 120)
_COPY_RATIO = 0.8  # more alike than this to the lesson's own check question = a copy


def lesson_material(authored: Any, sections: dict[str, str]) -> dict[str, Any]:
    """What the writer sees: the lesson text, its own check question (to avoid), and its known mix-ups."""
    check = authored.check
    return {"sections": sections, "own_question": check.question,
            "mix_ups": [m for m in check.misconceptions.values() if m]}


def writer_messages(concept_name: str, level: str, interest: str, material: dict[str, Any]) -> list[dict[str, str]]:
    lesson = "\n\n".join(f"## {h}\n{t}" for h, t in material["sections"].items())
    mix_ups = "\n".join(f"- {m}" for m in material["mix_ups"]) or "- (none listed)"
    return [{"role": "user", "content": (
        f"{(_PROMPTS / 'practice_writer.txt').read_text(encoding='utf-8')}\n\n---\n"
        f"Concept: {concept_name}\nLevel: {level}\nStudent's interest: {interest}\n\n"
        f"THE LESSON (source of truth):\n{lesson}\n\n"
        f"THE LESSON'S OWN CHECK QUESTION (do not repeat it):\n{material['own_question']}\n\n"
        f"COMMON MIX-UPS ABOUT THIS IDEA:\n{mix_ups}\n\nReply with the JSON object now.")}]


def solver_messages(concept_name: str, question: str, options: dict[str, str]) -> list[dict[str, str]]:
    listed = "\n".join(f"{k}. {v}" for k, v in options.items())
    return [{"role": "user", "content": (
        f"{(_PROMPTS / 'practice_solver.txt').read_text(encoding='utf-8')}\n\n---\n"
        f"Topic: {concept_name}\n\nQUESTION:\n{question}\n\nOPTIONS:\n{listed}\n\nReply with the JSON object now.")}]


def _words(text: str) -> int:
    return len(text.split())


def check_draft(data: Any, own_question: str) -> tuple[dict[str, Any] | None, str | None]:
    """(clean question, None) or (None, why it was rejected). Deterministic."""
    if not isinstance(data, dict):
        return None, "the reply wasn't a JSON object"
    question, options, answer = data.get("question"), data.get("options"), data.get("answer")
    explanation, why_wrong = data.get("explanation"), data.get("why_wrong") or {}
    if not isinstance(question, str) or not isinstance(options, dict) or not isinstance(explanation, str):
        return None, "missing question, options or explanation"
    if sorted(options) != list(LETTERS) or not all(isinstance(v, str) and v.strip() for v in options.values()):
        return None, "options must be exactly A, B, C and D, none empty"
    clean = {k: options[k].strip() for k in LETTERS}
    if len({v.lower() for v in clean.values()}) < 4:
        return None, "two options are the same"
    if not isinstance(answer, str) or answer.strip().upper() not in LETTERS:
        return None, "the answer isn't one of A to D"
    if not _QUESTION_WORDS[0] <= _words(question) <= _QUESTION_WORDS[1]:
        return None, f"the question has {_words(question)} words"
    if any(not _OPTION_WORDS[0] <= _words(v) <= _OPTION_WORDS[1] for v in clean.values()):
        return None, "an option is too long"
    if not _EXPLANATION_WORDS[0] <= _words(explanation) <= _EXPLANATION_WORDS[1]:
        return None, f"the explanation has {_words(explanation)} words"
    text = " ".join([question, explanation, *clean.values()])
    if re.search(r"https?://|www\.|\b[\w.+-]+@[\w-]+\.[\w.]+", text):
        return None, "contains a link or an email address"
    if SequenceMatcher(None, question.lower(), (own_question or "").lower()).ratio() > _COPY_RATIO:
        return None, "it copies the lesson's own check question"
    return {"question": question.strip(), "options": clean, "answer": answer.strip().upper(),
            "explanation": explanation.strip(),
            "why_wrong": {k: str(v).strip() for k, v in why_wrong.items() if k in LETTERS and str(v).strip()}}, None


def write(*, concept_name: str, level: str, interest: str, material: dict[str, Any],
          chat: Callable[..., Any]) -> dict[str, Any]:
    """Try to make one checked question.

    Returns {"ok": True, "question": {...}, "model": str, "trail": [...]} or {"ok": False, "trail": [...]}.
    The trail records every attempt and gate (no student data in it), for "How the AI decided".
    """
    trail: list[dict[str, Any]] = []
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            draft = chat(writer_messages(concept_name, level, interest, material), role="main",
                         temperature=0.7, max_tokens=900)
        except LLMError as exc:
            trail.append({"attempt": attempt, "step": "writer", "ok": False, "detail": str(exc)[:160]})
            break  # the model chain is down: more attempts won't help
        clean, why = check_draft(parse_json_object(getattr(draft, "text", "")), material["own_question"])
        if clean is None:
            trail.append({"attempt": attempt, "step": "rules", "ok": False, "detail": why})
            continue
        trail.append({"attempt": attempt, "step": "rules", "ok": True, "detail": ""})
        try:
            solved = chat(solver_messages(concept_name, clean["question"], clean["options"]), role="critic",
                          temperature=0.0, max_tokens=200)
        except LLMError as exc:
            trail.append({"attempt": attempt, "step": "solver", "ok": False, "detail": str(exc)[:160]})
            break
        verdict = parse_json_object(getattr(solved, "text", "")) or {}
        their = str(verdict.get("answer", "")).strip().upper()
        if their != clean["answer"]:
            trail.append({"attempt": attempt, "step": "solver", "ok": False,
                          "detail": f"the solver answered {their or 'nothing readable'}, the key says {clean['answer']}"})
            continue
        trail.append({"attempt": attempt, "step": "solver", "ok": True, "detail": ""})
        return {"ok": True, "question": clean, "model": getattr(draft, "model", None), "trail": trail}
    return {"ok": False, "trail": trail}
