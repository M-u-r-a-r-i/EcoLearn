"""Generate-and-review pipeline.

Coordinates the Analogy Generator and the Pedagogical Critic in a feedback
loop. Produces a draft, critiques it, and — on FAIL — regenerates with the
critic's feedback folded in as a revision instruction. This is the
multi-agent collaboration the rest of the system is built on.
"""

from __future__ import annotations

import time
from typing import Any

from src.agents.analogy_generator import generate_explanation
from src.agents.critic import critique
from src.rag.retrieve import retrieve_concept, retrieve_interest


# Brief pause between API calls inside one pipeline run. The Gemini free tier
# caps gemini-2.5-flash at 5 req/min, so we space generator calls at >12 s.
_INTER_STEP_DELAY_SECONDS = 13

# How many passages to pull from each RAG collection per pipeline run.
_RETRIEVE_TOP_K = 3


def _retrieve_context(concept: str, interest: str) -> tuple[list[str], list[str]]:
    """Pull the top curriculum and interest passages for this request.

    Returns (curriculum_passages, interest_passages) as plain text lists.
    """
    curriculum_hits = retrieve_concept(concept, n_results=_RETRIEVE_TOP_K)
    curriculum_passages = [h["text"] for h in curriculum_hits if h.get("text")]

    # Concatenating concept + interest as the interest-collection query gives
    # the embedding model both hooks — "kinetic energy" alone matches gaming
    # passages weakly, but "kinetic energy gaming" steers toward physics-heavy
    # gaming passages.
    interest_query = f"{concept} {interest}".strip()
    interest_hits = retrieve_interest(
        interest_query, interest, n_results=_RETRIEVE_TOP_K,
    )
    interest_passages = [h["text"] for h in interest_hits if h.get("text")]

    return curriculum_passages, interest_passages


def _format_verdict_for_log(verdict: dict[str, Any]) -> str:
    label = verdict.get("verdict", "UNKNOWN")
    flags = (
        f"sci={verdict.get('scientific_correctness')} "
        f"ped={verdict.get('pedagogical_fit')} "
        f"int={verdict.get('analogical_integrity')}"
    )
    return f"{label} ({flags})"


def explain_with_review(
    concept: str,
    interest: str,
    level: str,
    max_retries: int = 2,
) -> dict[str, Any]:
    """Generate an explanation, have it reviewed, retry on FAIL.

    Args:
        concept: The academic concept (e.g., "relative velocity").
        interest: The student's primary interest (e.g., "football").
        level: The student's academic level (e.g., "Class 11").
        max_retries: Maximum number of regeneration attempts after the
            initial draft. Total attempts = 1 + max_retries.

    Returns:
        A dict with keys:
            explanation: The final explanation text (PASS or last attempt).
            verdict: "PASS" / "FAIL" / "ERROR" from the final critique.
            attempts: How many generator calls were made.
            critique: The final verdict dict from the critic.
            history: A list of per-attempt verdict snapshots for inspection.
            curriculum_context: Curriculum passages fed to the generator.
            interest_context: Interest passages fed to the generator.
    """
    # Retrieve grounding context once up front; the same passages are reused
    # across regenerations because the concept and interest do not change.
    print(f"[RAG] retrieving for concept={concept!r}, interest={interest!r} ...")
    curriculum_passages, interest_passages = _retrieve_context(concept, interest)
    print(
        f"[RAG] got {len(curriculum_passages)} curriculum + "
        f"{len(interest_passages)} interest passages"
    )

    feedback_for_next: str | None = None
    final_explanation = ""
    final_verdict: dict[str, Any] = {}
    history: list[dict[str, Any]] = []
    total_attempts = 1 + max(0, max_retries)

    for attempt in range(1, total_attempts + 1):
        is_first = attempt == 1
        if is_first:
            print(f"[Attempt {attempt}] generating draft...")
        else:
            print(f"[Attempt {attempt}] regenerating with critic feedback...")

        final_explanation = generate_explanation(
            concept=concept,
            interest=interest,
            level=level,
            sub_interest_facts=interest_passages,
            curriculum_context=curriculum_passages,
            prior_feedback=feedback_for_next,
        )
        time.sleep(_INTER_STEP_DELAY_SECONDS)

        print(f"[Attempt {attempt}] critiquing...")
        final_verdict = critique(final_explanation, concept=concept)
        history.append(final_verdict)
        print(f"[Attempt {attempt}] verdict: {_format_verdict_for_log(final_verdict)}")

        if final_verdict.get("verdict") == "PASS":
            print(f"[Attempt {attempt}] PASS — stopping.")
            return {
                "explanation": final_explanation,
                "verdict": "PASS",
                "attempts": attempt,
                "critique": final_verdict,
                "history": history,
                "curriculum_context": curriculum_passages,
                "interest_context": interest_passages,
            }

        # On FAIL or ERROR, prepare feedback for the next attempt (if any).
        feedback_for_next = final_verdict.get("feedback") or ""
        if attempt < total_attempts:
            print(f"[Attempt {attempt}] feedback: {feedback_for_next[:200]}")
            time.sleep(_INTER_STEP_DELAY_SECONDS)

    print(f"[Final] exhausted {total_attempts} attempts without PASS.")
    return {
        "explanation": final_explanation,
        "verdict": final_verdict.get("verdict", "ERROR"),
        "attempts": total_attempts,
        "critique": final_verdict,
        "history": history,
        "curriculum_context": curriculum_passages,
        "interest_context": interest_passages,
    }
