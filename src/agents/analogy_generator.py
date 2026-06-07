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


def _format_context_block(label: str, intro: str, passages: list[str]) -> list[str]:
    """Render a list of retrieved passages as a labelled block."""
    out = ["", f"{label} ({intro}):"]
    for i, p in enumerate(passages, start=1):
        out.append(f"--- passage {i} ---")
        out.append(p.strip())
    out.append(f"--- end {label.lower()} ---")
    return out


def _build_user_message(
    concept: str,
    interest: str,
    level: str,
    sub_interest_facts: Iterable[str] | None,
    prior_feedback: str | None,
    curriculum_context: Iterable[str] | None = None,
) -> str:
    """Render the per-request inputs into a single user message."""
    lines = [
        f"Concept: {concept}",
        f"Student interest: {interest}",
        f"Level: {level}",
    ]
    if curriculum_context:
        passages = [p for p in curriculum_context if p and p.strip()]
        if passages:
            lines.extend(_format_context_block(
                "CURRICULUM CONTEXT",
                "authoritative for formal definitions, equations, and notation",
                passages,
            ))
    if sub_interest_facts:
        passages = [p for p in sub_interest_facts if p and p.strip()]
        if passages:
            lines.extend(_format_context_block(
                "INTEREST CONTEXT",
                "authoritative for concrete numbers, real examples, and names from the student's interest",
                passages,
            ))
    if prior_feedback and prior_feedback.strip():
        lines.append("")
        lines.append("REVISION NOTE — your previous answer was rejected by the")
        lines.append("Pedagogical Critic. Rewrite the explanation in full and")
        lines.append("address this feedback specifically:")
        lines.append(prior_feedback.strip())
    lines.append("")
    lines.append("=== FORMAT GUARDRAILS — read last, enforce strictly ===")
    lines.append("")
    lines.append(
        "Your response MUST begin with the literal text \"1. SCENARIO\" on its "
        "own line. Nothing before it. No preamble, no bullet point, no header, "
        "no label, no acknowledgement."
    )
    lines.append("")
    lines.append("You MUST NOT output ANY of the following anywhere in your reply:")
    lines.append("  - Planning notes, drafts, or revisions (no \"Revised Scenario\","
                 " \"Expanding...\", \"Refining...\").")
    lines.append("  - Length checks (no \"Word count: ~330. I need to expand.\").")
    lines.append("  - Labels echoing the input (no \"Concept:\", \"Student Interest:\","
                 " \"Constraints:\", \"Curriculum Context:\", \"Interest Context:\").")
    lines.append("  - Self-correction commentary (no \"Wait, I need to...\","
                 " \"Self-Correction during drafting...\").")
    lines.append("  - Bullet-point scratchpad with asterisks and italic asides.")
    lines.append("")
    lines.append(
        "If you would normally think out loud, think silently and emit only the "
        "final three-section answer plus the [ANALOGY_QUALITY: N] line."
    )
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


def _response_debug_summary(response: object) -> str:
    """Return compact model metadata for diagnosing empty responses."""
    candidates = getattr(response, "candidates", None) or []
    summaries: list[str] = []
    for candidate in candidates:
        finish_reason = getattr(candidate, "finish_reason", None)
        safety_ratings = getattr(candidate, "safety_ratings", None)
        summaries.append(
            f"finish_reason={finish_reason!r}, safety_ratings={safety_ratings!r}"
        )
    return "; ".join(summaries) or "no candidate metadata available"


def _extract_response_text(response: object) -> str:
    """Extract text from a Gemini/Gemma response, raising clearly if absent."""
    text = getattr(response, "text", None)
    if text and text.strip():
        return text

    parts_text: list[str] = []
    for candidate in getattr(response, "candidates", None) or []:
        content = getattr(candidate, "content", None)
        for part in getattr(content, "parts", None) or []:
            part_text = getattr(part, "text", None)
            if part_text:
                parts_text.append(part_text)
    if parts_text:
        return "\n".join(parts_text)

    raise RuntimeError(
        "Generator model returned no text. "
        f"Response metadata: {_response_debug_summary(response)}"
    )


def generate_explanation(
    concept: str,
    interest: str,
    level: str,
    sub_interest_facts: Iterable[str] | None = None,
    prior_feedback: str | None = None,
    curriculum_context: Iterable[str] | None = None,
) -> str:
    """Generate an interest-grounded explanation of `concept` for the student.

    Args:
        concept: The academic concept to explain (e.g., "relative velocity").
        interest: The student's primary interest (e.g., "football").
        level: The student's academic level (e.g., "Class 11").
        sub_interest_facts: Optional list of interest-domain passages (real
            facts, numbers, named examples) the model should prefer over its
            own knowledge. Typically supplied by the RAG retriever.
        prior_feedback: Optional critic feedback from a previous attempt. When
            present, the model is told to rewrite in full while addressing it.
        curriculum_context: Optional list of curriculum passages (formal
            definitions, equations, notation) the model must treat as the
            source of truth. Typically supplied by the RAG retriever.

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
        curriculum_context=curriculum_context,
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
    return _extract_response_text(response)
