"""Analogy-driven explanation agent.

Generates structurally honest, interest-grounded explanations of academic concepts
using Gemini 2.5 Flash. The system prompt is loaded from prompts/analogy_generator.txt
so the prompt can be tuned without touching code.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Project root = .../EcoLearn/  (this file lives at .../EcoLearn/src/agents/)
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_SYSTEM_PROMPT_PATH = _PROJECT_ROOT / "prompts" / "analogy_generator.txt"

# Model is controlled by the GEMINI_MODEL env var so we can swap between
# Gemini and Gemma models without code changes. Gemma is recommended while
# free-tier Gemini quotas are tight — it has a separate, more generous quota.
_DEFAULT_MODEL = "gemma-3-27b-it"
_TEMPERATURE = 0.7
_DEFAULT_MAX_OUTPUT_TOKENS = 2048
_DEFAULT_THINKING_BUDGET = 0


def _load_system_prompt() -> str:
    """Read the analogy-generator system prompt from disk."""
    return _SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")


def _build_user_message(
    concept: str,
    interest: str,
    level: str,
    sub_interest_facts: Iterable[str] | None,
    prior_feedback: str | None,
) -> str:
    """Render the per-request inputs into a single user message."""
    lines = [
        f"Concept: {concept}",
        f"Student interest: {interest}",
        f"Level: {level}",
    ]
    if sub_interest_facts:
        facts = list(sub_interest_facts)
        if facts:
            lines.append("Additional facts about the student's interest:")
            lines.extend(f"  - {fact}" for fact in facts)
    if prior_feedback and prior_feedback.strip():
        lines.append("")
        lines.append("REVISION NOTE — your previous answer was rejected by the")
        lines.append("Pedagogical Critic. Rewrite the explanation in full and")
        lines.append("address this feedback specifically:")
        lines.append(prior_feedback.strip())
    lines.append("")
    lines.append("Generate the explanation now, following the output format exactly.")
    return "\n".join(lines)


def _env_int(name: str, default: int) -> int:
    """Read a positive integer setting from the environment."""
    raw_value = os.getenv(name)
    if raw_value is None or not raw_value.strip():
        return default
    try:
        value = int(raw_value)
    except ValueError as exc:
        raise RuntimeError(f"{name} must be an integer, got {raw_value!r}.") from exc
    if value <= 0:
        raise RuntimeError(f"{name} must be greater than 0, got {value}.")
    return value


def _env_non_negative_int(name: str, default: int) -> int:
    """Read a zero-or-greater integer setting from the environment."""
    raw_value = os.getenv(name)
    if raw_value is None or not raw_value.strip():
        return default
    try:
        value = int(raw_value)
    except ValueError as exc:
        raise RuntimeError(f"{name} must be an integer, got {raw_value!r}.") from exc
    if value < 0:
        raise RuntimeError(f"{name} must be 0 or greater, got {value}.")
    return value


def _build_generation_config(model: str) -> types.GenerateContentConfig:
    """Build generation settings, including Gemini 2.5 Flash thinking control."""
    max_output_tokens = _env_int("GEMINI_MAX_OUTPUT_TOKENS", _DEFAULT_MAX_OUTPUT_TOKENS)
    config_kwargs = {
        "temperature": _TEMPERATURE,
        "max_output_tokens": max_output_tokens,
    }

    # Gemini 2.5 Flash enables thinking by default. For this tutoring agent we
    # prefer longer visible explanations, so keep the thinking budget explicit.
    if model.startswith("gemini-2.5-flash"):
        thinking_budget = _env_non_negative_int(
            "GEMINI_THINKING_BUDGET",
            _DEFAULT_THINKING_BUDGET,
        )
        config_kwargs["thinking_config"] = types.ThinkingConfig(
            thinking_budget=thinking_budget,
        )

    return types.GenerateContentConfig(**config_kwargs)


def generate_explanation(
    concept: str,
    interest: str,
    level: str,
    sub_interest_facts: Iterable[str] | None = None,
    prior_feedback: str | None = None,
) -> str:
    """Generate an interest-grounded explanation of `concept` for the student.

    Args:
        concept: The academic concept to explain (e.g., "relative velocity").
        interest: The student's primary interest (e.g., "football").
        level: The student's academic level (e.g., "Class 11").
        sub_interest_facts: Optional list of specific facts about the student's
            interest, used to make the analogy more personal.
        prior_feedback: Optional critic feedback from a previous attempt. When
            present, the model is told to rewrite in full while addressing it.

    Returns:
        The model's response text, formatted per the system prompt.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not found in environment. Check your .env file.")

    client = genai.Client(api_key=api_key)
    model = os.getenv("GEMINI_MODEL", _DEFAULT_MODEL).strip()
    system_prompt = _load_system_prompt()
    user_message = _build_user_message(
        concept, interest, level, sub_interest_facts, prior_feedback,
    )

    # Gemma models do not support a separate `system_instruction` field, so we
    # prepend the system prompt to the user message. This works for both
    # Gemma and Gemini.
    contents = f"{system_prompt}\n\n---\n\n{user_message}"

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=_build_generation_config(model),
    )
    return response.text
