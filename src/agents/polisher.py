"""Polisher agent — extract the final answer from messy generator output.

Reasoning-trained models (notably Gemma 4) leak planning notes, drafts, length
checks, and self-corrections into their replies, and write math inconsistently
(mixed Unicode/LaTeX). This module runs a cheap extractor LLM over that mess and
returns clean, scannable markdown with consistent KaTeX-ready math.

This is the single source of truth for polishing. Both the live Streamlit app
(app.py) and the offline lesson factory (src/content/generate_lessons.py) import
`polish_explanation` from here so the two paths produce identical formatting.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Polisher uses a cheap model on a separate quota bucket from the generator.
# Override via POLISHER_MODEL. gemini-2.5-flash-lite is the proven default.
_POLISHER_MODEL_DEFAULT = "gemini-2.5-flash-lite"
_POLISHER_SYSTEM = (
    "You are a strict text extractor and markdown formatter. You receive a "
    "draft explanation from a tutoring AI that sometimes leaks planning "
    "notes, drafts, and length checks, and that writes math inconsistently. "
    "Your job: emit the FINAL student-facing answer using the visually "
    "scannable markdown layout described below. Do NOT invent content; "
    "extract and reformat what the draft already says.\n\n"
    "═══════════════════════════════════════════════════════════════\n"
    "OUTPUT FORMAT (use this exact markdown layout)\n"
    "═══════════════════════════════════════════════════════════════\n\n"
    "### Scenario\n\n"
    "[2-4 short sentences setting up the analogy in the student's interest. "
    "Keep paragraphs short — one idea per paragraph, blank line between "
    "paragraphs.]\n\n"
    "**Mapping:**\n\n"
    "- formal element → scenario element\n"
    "- formal element → scenario element\n"
    "- (one bullet per mapping; preserve the → arrow)\n\n"
    "> **Where the analogy breaks down:** [one sentence naming the limit]\n\n"
    "---\n\n"
    "### Formal Restatement\n\n"
    "[2-3 short sentences defining the concept in standard academic "
    "language. Bold **key terms** on first mention.]\n\n"
    "$$\\text{the defining equation on its own line}$$\n\n"
    "**Where:**\n\n"
    "- $\\text{symbol}$ — what it means (with SI units)\n"
    "- $\\text{symbol}$ — what it means (with SI units)\n\n"
    "---\n\n"
    "### Self-Check Question\n\n"
    "[the question, 1-2 sentences]\n\n"
    "> **Hint:** [the hint]\n\n"
    "═══════════════════════════════════════════════════════════════\n"
    "EXTRACTION RULES\n"
    "═══════════════════════════════════════════════════════════════\n\n"
    "- Output ONLY the three sections in the layout above. No preamble, no "
    "commentary, no [ANALOGY_QUALITY] tag at the end.\n"
    "- If the draft has multiple versions ('Revised', 'Drafting', 'Final "
    "Polish'), use the LAST version of each section.\n"
    "- Drop every meta line ('Length Check', 'Word count', 'Wait,', "
    "'No emojis? Yes.', bullet-list field/value pairs).\n"
    "- If a section is genuinely missing in the draft, write the header and "
    "then `(not provided)` and move on. NEVER invent.\n"
    "- Keep paragraphs SHORT. Break long paragraphs at natural seams. The "
    "student should be able to scan the bubble in 10 seconds.\n\n"
    "═══════════════════════════════════════════════════════════════\n"
    "MATH FORMATTING (CRITICAL — the page renders LaTeX via KaTeX)\n"
    "═══════════════════════════════════════════════════════════════\n\n"
    "- Inline math: $...$. Standalone equation: $$...$$ on its own line.\n"
    "- Convert ALL Unicode math to LaTeX:\n"
    "    θ → \\theta,  Δ → \\Delta,  μ → \\mu,  π → \\pi\n"
    "    ≈ → \\approx,  ≤ → \\leq,  ≥ → \\geq,  ± → \\pm\n"
    "    × → \\times,  · → \\cdot,  √x → \\sqrt{x},  ∞ → \\infty\n"
    "    x² → x^2,  x_n → x_{n}\n"
    "    sin/cos/tan → \\sin/\\cos/\\tan\n"
    "    vectors: \\vec{v} or \\mathbf{v}\n"
    "- Units inside math use \\text{}: $g \\approx 9.8 \\text{ m/s}^2$ "
    "(not $g \\approx 9.8 m/s^2$).\n"
    "- EXCEPTION: in the **Mapping** bullet list, KEEP the → as Unicode "
    "(it's a layout marker, not math).\n"
    "- Bold **key terms** with markdown; do NOT bold math symbols."
)


def polish_explanation(messy_text: str) -> str:
    """Run a fast extractor LLM pass over messy generator output.

    Uses gemini-2.5-flash-lite by default (cheap, on a separate quota bucket
    from the generator). Returns the cleaned text on success, or the input
    unchanged on any failure (fail-open so the caller always has *something*).
    """
    if not messy_text or not messy_text.strip():
        return messy_text

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return messy_text

    model = os.getenv("POLISHER_MODEL", _POLISHER_MODEL_DEFAULT).strip()

    contents = (
        f"{_POLISHER_SYSTEM}\n\n"
        f"DRAFT (begin):\n---\n{messy_text}\n---\n(end of draft)\n\n"
        "Emit the cleaned final answer now."
    )

    config_kwargs: dict = {
        "temperature": 0.0,
        "max_output_tokens": 2048,
    }
    # gemini-2.5-* enables thinking by default; disable it so all tokens go
    # to the visible extraction.
    if model.startswith("gemini-2.5"):
        config_kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=0)

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=types.GenerateContentConfig(**config_kwargs),
        )
        polished = (response.text or "").strip()
    except Exception:  # noqa: BLE001 — fail open on any polisher failure.
        return messy_text

    return polished or messy_text
