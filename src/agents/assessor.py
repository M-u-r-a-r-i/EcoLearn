"""Assessor agent — generates interest-themed questions and grades answers.

Two public functions share a single system prompt (`prompts/assessor.txt`)
that dispatches on a `Mode:` line in the user message:

    generate_question(concept, interest, level) -> dict
    grade_answer(question, expected_concepts, student_answer) -> dict

Both return parsed JSON dicts. On any JSON parse failure we retry once;
if the second attempt still fails, we return a sentinel dict with a clear
error key so callers can fall back gracefully.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, Iterable

from dotenv import load_dotenv
from google import genai
from google.genai import types


_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_SYSTEM_PROMPT_PATH = _PROJECT_ROOT / "prompts" / "assessor.txt"

# Defaults — Gemma 4 31B for both modes. Gemma sits on a separate, much
# more generous free-tier quota bucket than the Gemini Flash family (which
# is capped at 20 req/day). Gemma does not have native JSON mime mode, but
# the prompt's strict examples plus the regex fallback parser handle that.
# Override via env vars if you want different models for the two modes.
_DEFAULT_QUESTION_MODEL = "gemma-4-31b-it"
_DEFAULT_GRADE_MODEL = "gemma-4-31b-it"

# Fallback models tried, in order, when the primary model fails with an API
# error (e.g. a 500 INTERNAL outage on one model, or a 429 quota cap). This is
# the "portfolio of models" reliability pattern: a single model going down on
# the provider's side must not take grading/questioning offline. Override the
# primary via the env vars above; these are the safety net behind it.
_FALLBACK_MODELS = ("gemini-2.5-flash-lite", "gemini-flash-latest")

# Mild variety on questions; near-deterministic on grading.
_QUESTION_TEMPERATURE = 0.4
_GRADE_TEMPERATURE = 0.1

_DEFAULT_MAX_OUTPUT_TOKENS = 2048

# Fallback parser if the model wraps the JSON in prose or markdown fences.
_JSON_BLOCK_RE = re.compile(r"\{.*\}", re.DOTALL)

_QUESTION_REQUIRED_KEYS = ("question", "expected_concepts", "difficulty_level")
_GRADE_REQUIRED_KEYS = ("score", "mastery_signal", "feedback", "missing_concepts")


def _load_system_prompt() -> str:
    return _SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")


def _parse_json(raw_text: str, required_keys: tuple[str, ...]) -> dict | None:
    """Parse the model output as JSON; verify required keys are present."""
    if not raw_text:
        return None
    text = raw_text.strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        match = _JSON_BLOCK_RE.search(text)
        if not match:
            return None
        try:
            parsed = json.loads(match.group(0))
        except json.JSONDecodeError:
            return None
    if not isinstance(parsed, dict):
        return None
    if not all(k in parsed for k in required_keys):
        return None
    return parsed


def _build_config(model: str, temperature: float) -> types.GenerateContentConfig:
    """Generation config — enforce JSON output on Gemini; turn off thinking."""
    kwargs: dict[str, Any] = {
        "temperature": temperature,
        "max_output_tokens": _DEFAULT_MAX_OUTPUT_TOKENS,
    }
    if model.startswith("gemini-"):
        # Gemini models support response_mime_type to force valid JSON.
        kwargs["response_mime_type"] = "application/json"
    if model.startswith("gemini-2.5"):
        # Thinking tokens would eat our small max_output_tokens budget.
        kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=0)
    return types.GenerateContentConfig(**kwargs)


def _call_assessor(model: str, user_message: str, temperature: float) -> str:
    """Send the system prompt + user message; return the raw text response."""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY not found in environment. Check your .env file."
        )

    client = genai.Client(api_key=api_key)
    system_prompt = _load_system_prompt()
    # Gemma models don't accept a separate system_instruction, so we always
    # prepend the prompt — works on both Gemini and Gemma.
    contents = f"{system_prompt}\n\n---\n\n{user_message}"
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=_build_config(model, temperature),
    )
    text = response.text or ""
    if not text.strip():
        # Print finish_reason and safety ratings so empty responses are
        # debuggable. Common causes: MAX_TOKENS (raise max_output_tokens),
        # SAFETY (rewrite the prompt), RECITATION (rewrite the prompt).
        for cand in getattr(response, "candidates", None) or []:
            print(
                f"[assessor] empty response — finish_reason="
                f"{getattr(cand, 'finish_reason', None)!r} safety="
                f"{getattr(cand, 'safety_ratings', None)!r}"
            )
    return text


def _model_chain(primary: str) -> list[str]:
    """Build the ordered model list: primary first, then distinct fallbacks."""
    chain = [primary]
    for model in _FALLBACK_MODELS:
        if model not in chain:
            chain.append(model)
    return chain


def _attempt_with_retry(
    primary_model: str,
    user_message: str,
    temperature: float,
    required_keys: tuple[str, ...],
) -> tuple[dict | None, str]:
    """Call the assessor, returning the first parseable JSON verdict.

    Resilience strategy:
      - try each model in the fallback chain (primary first);
      - within a model, retry once on a JSON *parse* failure;
      - on an API *error* (500 outage, 429 quota, network), skip straight to
        the next model rather than crashing — the provider client has already
        retried the same model internally, so re-hitting it is pointless.

    Returns (parsed_or_None, last_raw_text). Never raises on API errors; an
    all-models-failed run returns (None, last_raw) so the caller emits its
    sentinel dict.
    """
    last_raw = ""
    for model in _model_chain(primary_model):
        for _attempt in range(2):  # one parse-retry within a healthy model
            try:
                last_raw = _call_assessor(model, user_message, temperature)
            except Exception as exc:  # noqa: BLE001 — API/network error, try next model.
                print(
                    f"[assessor] model {model!r} failed "
                    f"({type(exc).__name__}: {str(exc)[:100]}); trying next model."
                )
                last_raw = f"{type(exc).__name__}: {exc}"
                break  # don't retry the same model on an API error
            parsed = _parse_json(last_raw, required_keys)
            if parsed is not None:
                if model != primary_model:
                    print(f"[assessor] succeeded on fallback model {model!r}.")
                return parsed, last_raw
    return None, last_raw


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def generate_question(concept: str, interest: str, level: str) -> dict[str, Any]:
    """Generate one interest-themed question about `concept` for the student.

    Returns a dict with keys: question, expected_concepts, difficulty_level.
    On parse failure after one retry, returns a fallback dict containing an
    `error` key so callers can detect the failure.
    """
    model = os.getenv("ASSESSOR_QUESTION_MODEL", _DEFAULT_QUESTION_MODEL).strip()
    user_message = (
        f"Mode: generate_question\n"
        f"Concept: {concept}\n"
        f"Student interest: {interest}\n"
        f"Student level: {level}\n\n"
        f"Generate the question now as a single JSON object."
    )
    parsed, last_raw = _attempt_with_retry(
        model, user_message, _QUESTION_TEMPERATURE, _QUESTION_REQUIRED_KEYS,
    )
    if parsed is not None:
        return parsed

    return {
        "question": "(failed to generate a valid question)",
        "expected_concepts": [],
        "difficulty_level": "recall",
        "error": (
            "Assessor could not produce valid JSON from any model "
            "(primary + fallbacks). "
            f"Last response/error: {last_raw[:300]!r}"
        ),
    }


def grade_answer(
    question: str,
    expected_concepts: Iterable[str],
    student_answer: str,
) -> dict[str, Any]:
    """Grade a student's answer against the expected concepts.

    Returns a dict with keys: score, mastery_signal, feedback, missing_concepts.
    On parse failure after one retry, returns a sentinel "not_yet" dict
    containing an `error` key.
    """
    model = os.getenv("ASSESSOR_GRADE_MODEL", _DEFAULT_GRADE_MODEL).strip()
    expected_lines = [f"  - {c}" for c in expected_concepts]
    expected_str = "\n".join(expected_lines) if expected_lines else "  (none provided)"
    user_message = (
        f"Mode: grade_answer\n"
        f"Question: {question}\n"
        f"Expected concepts:\n{expected_str}\n"
        f"Student's answer:\n---\n{student_answer.strip()}\n---\n\n"
        f"Grade the answer now as a single JSON object."
    )
    parsed, last_raw = _attempt_with_retry(
        model, user_message, _GRADE_TEMPERATURE, _GRADE_REQUIRED_KEYS,
    )
    if parsed is not None:
        return parsed

    return {
        "score": 0,
        "mastery_signal": "not_yet",
        "feedback": "(grader could not parse a valid response)",
        "missing_concepts": [],
        "error": (
            "Assessor could not produce valid JSON from any model "
            "(primary + fallbacks). "
            f"Last response/error: {last_raw[:300]!r}"
        ),
    }
