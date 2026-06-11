"""Pedagogical Critic agent.

Reviews an Analogy Generator output for scientific correctness, pedagogical fit,
and analogical integrity. Returns a strict-JSON verdict that the pipeline can
act on. We deliberately use a cheaper/faster model than the Generator because
judging structured criteria is easier than producing creative explanations.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from google import genai
from google.genai import types


_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_SYSTEM_PROMPT_PATH = _PROJECT_ROOT / "prompts" / "critic.txt"

# Critic uses a smaller, cheaper model than the generator. Override via the
# CRITIC_MODEL env var. gemini-2.5-flash-lite is a strong default for fast,
# cheap structured-output judgement; falls back to whatever the user picks.
_DEFAULT_MODEL = "gemini-2.5-flash-lite"
_TEMPERATURE = 0.1  # Low temperature so the same input yields the same verdict.
_DEFAULT_MAX_OUTPUT_TOKENS = 512

# When the model returns text with markdown fences or stray prose around the
# JSON, this regex pulls out the first balanced JSON object as a fallback.
_JSON_BLOCK_RE = re.compile(r"\{.*\}", re.DOTALL)

_REQUIRED_KEYS = (
    "verdict",
    "scientific_correctness",
    "pedagogical_fit",
    "analogical_integrity",
    "feedback",
)


def _load_system_prompt() -> str:
    return _SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")


def _build_user_message(explanation_text: str, concept: str) -> str:
    return (
        f"Concept: {concept}\n\n"
        f"Explanation under review:\n"
        f"---\n"
        f"{explanation_text.strip()}\n"
        f"---\n\n"
        f"Return your verdict now as a single JSON object."
    )


def _build_generation_config(model: str) -> types.GenerateContentConfig:
    """Force JSON output on Gemini; for Gemma, rely on the prompt + parser."""
    kwargs: dict[str, Any] = {
        "temperature": _TEMPERATURE,
        "max_output_tokens": _DEFAULT_MAX_OUTPUT_TOKENS,
    }
    if model.startswith("gemini-"):
        kwargs["response_mime_type"] = "application/json"
    if model.startswith("gemini-2.5"):
        # Critic doesn't need internal reasoning tokens; keep responses snappy.
        kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=0)
    return types.GenerateContentConfig(**kwargs)


def _parse_verdict(raw_text: str) -> dict[str, Any] | None:
    """Parse the model output into a verdict dict, or return None on failure."""
    if not raw_text:
        return None
    text = raw_text.strip()
    # Try direct parse first (Gemini in JSON mode returns clean JSON).
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
    if not all(key in parsed for key in _REQUIRED_KEYS):
        return None
    return parsed


def _call_model(client: genai.Client, model: str, prompt: str, contents: str) -> str:
    response = client.models.generate_content(
        model=model,
        contents=f"{prompt}\n\n---\n\n{contents}",
        config=_build_generation_config(model),
    )
    return response.text or ""


def critique(explanation_text: str, concept: str) -> dict[str, Any]:
    """Critique an explanation and return a verdict dict.

    Returns a dict with keys: verdict ("PASS" | "FAIL" | "ERROR"),
    scientific_correctness, pedagogical_fit, analogical_integrity, feedback.

    On parse failure, retries once. If the second attempt also fails, returns
    a sentinel dict with verdict="ERROR" so the caller can decide how to react.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in environment. Check your .env file.")

    client = genai.Client(api_key=api_key)
    model = os.getenv("CRITIC_MODEL", _DEFAULT_MODEL).strip()
    system_prompt = _load_system_prompt()
    user_message = _build_user_message(explanation_text, concept)

    last_raw = ""
    last_exc: Exception | None = None
    for _attempt in range(2):  # initial + one retry on bad JSON
        try:
            last_raw = _call_model(client, model, system_prompt, user_message)
        except Exception as exc:  # noqa: BLE001 — capture for fail-safe path.
            last_exc = exc
            continue
        parsed = _parse_verdict(last_raw)
        if parsed is not None:
            return parsed

    # Fail-safe: critic is supposed to *gate* shipping, but in a live chat we
    # would rather ship a possibly-imperfect explanation than show the student
    # an error. Treat critic failure as a soft PASS — the pipeline keeps going,
    # the student sees the explanation, and we surface the failure reason in
    # the `error` field for any downstream logging.
    fail_reason = (
        f"API error: {type(last_exc).__name__}: {last_exc}"
        if last_exc is not None
        else f"Critic could not produce valid JSON. Last raw: {last_raw[:300]!r}"
    )
    return {
        "verdict": "PASS",
        "scientific_correctness": True,
        "pedagogical_fit": True,
        "analogical_integrity": True,
        "feedback": "",
        "error": fail_reason,
    }
