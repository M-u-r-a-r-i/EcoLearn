"""EcoLearn — Streamlit front-end.

Two views, switched by whether `st.session_state.profile` is set:

    Onboarding — collects student name, interest, class level, and subject.
    Chat       — header with the student's identity, scrolling history of
                 messages, sticky input at the bottom, profile sidebar.

The chat handler routes the user's message through the multi-agent pipeline:
RAG retrieval → analogy generator → pedagogical critic → (on FAIL) retry.
"""

from __future__ import annotations

import os
import re

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

from src.pipeline import explain_with_review


# Markers used to extract the clean answer when the model follows format.
_SCENARIO_RE = re.compile(r"^\s*1\.\s*SCENARIO\b", re.MULTILINE | re.IGNORECASE)
_QUALITY_RE = re.compile(r"\[ANALOGY[_\s]QUALITY:\s*\d+\]", re.IGNORECASE)

# Paragraph-level scratchpad detector. Any paragraph where most lines start
# with a known meta-label or planning marker is treated as scratchpad and
# dropped. Used as a fallback when the model leaks reasoning instead of
# emitting the canonical 1./2./3. headers.
_META_LABEL_RE = re.compile(
    r"^\s*\*?\s*(?:"
    r"Concept|Student\s+Interest|Level|Subject|Constraints|"
    r"Curriculum\s+Context|Interest\s+Context|Formal\s+Elements?|"
    r"Scenario\s+Mapping|Length\s+Check|Word\s+count|"
    r"Element\s+Correspondence|Relation\s+Preservation|Honest\s+Breakdown|"
    r"Drafting|Refining|Expanding|Revised|Final\s+Polish|"
    r"Wait,|Self-Correction|Self-rating|Checking|"
    r"One\s+final\s+check|Correctness|Formatting|SI\s+Units|"
    r"No\s+emojis|No\s+filler|No\s+preamble|Bold\s+key\s+terms"
    r")\b",
    re.IGNORECASE,
)


def _is_scratchpad_paragraph(paragraph: str) -> bool:
    """True if the paragraph looks like model planning notes."""
    lines = [ln for ln in paragraph.splitlines() if ln.strip()]
    if not lines:
        return True
    meta_count = sum(1 for ln in lines if _META_LABEL_RE.match(ln))
    return meta_count / len(lines) >= 0.5


def _strip_scratchpad_paragraphs(text: str) -> str:
    """Drop scratchpad-looking paragraphs from the model output."""
    paragraphs = re.split(r"\n\s*\n", text)
    kept = [p for p in paragraphs if not _is_scratchpad_paragraph(p)]
    return "\n\n".join(kept).strip()


def _sanitize_explanation(raw: str) -> str:
    """Strip scratchpad noise; keep just the three-section student answer.

    Strategy in order:
      1. If the model emitted the canonical "1. SCENARIO" header and the
         "[ANALOGY_QUALITY: N]" tag, slice between them — this is the clean
         case and gives the cleanest output.
      2. If the markers are missing (chain-of-thought leakage), fall back to
         paragraph-level scratchpad stripping: drop any paragraph dominated
         by meta-labels like "Drafting", "Constraints:", "Length Check", etc.
    """
    if not raw:
        return raw
    text = raw.strip()

    # Strategy 1: marker-anchored extraction.
    scenario_match = _SCENARIO_RE.search(text)
    quality_match = _QUALITY_RE.search(text)
    if scenario_match and quality_match:
        return text[scenario_match.start():quality_match.end()].strip()

    # Strategy 2: paragraph-level scratchpad stripping.
    cleaned = _strip_scratchpad_paragraphs(text)

    # Last belt-and-suspenders: if 1. SCENARIO appeared but no quality tag,
    # still slice from there (the trailing scratchpad will already have been
    # stripped by the paragraph filter, but better safe).
    scenario_match = _SCENARIO_RE.search(cleaned)
    if scenario_match:
        cleaned = cleaned[scenario_match.start():].strip()

    return cleaned


# ---------------------------------------------------------------------------
# Polisher — a small, deterministic LLM pass that extracts the final answer.
# ---------------------------------------------------------------------------

_POLISHER_MODEL_DEFAULT = "gemini-2.5-flash-lite"
_POLISHER_SYSTEM = (
    "You are a strict text extractor and math formatter. You are given a "
    "draft explanation from a tutoring AI that sometimes leaks planning "
    "notes, multiple drafts, and length checks, and that writes math "
    "inconsistently (sometimes Unicode, sometimes LaTeX, sometimes plain "
    "text). Your only job is to emit the FINAL student-facing answer in "
    "this exact format:\n\n"
    "1. SCENARIO\n"
    "[the final scenario prose. Then a short mapping table — one mapping per "
    "line in the form `formal element  →  scenario element`. Then one sentence "
    "naming where the analogy breaks down.]\n\n"
    "2. FORMAL RESTATEMENT\n"
    "[the final formal definition prose, with equations and bolded key terms.]\n\n"
    "3. SELF-CHECK QUESTION\n"
    "[the final question. Then a line starting with `Hint:` and the hint.]\n\n"
    "[ANALOGY_QUALITY: N]\n\n"
    "EXTRACTION RULES:\n"
    "- Output ONLY the three numbered sections and the quality tag. No "
    "preamble. No commentary.\n"
    "- If the draft has multiple versions ('Revised', 'Drafting', 'Final "
    "Polish'), use the LAST version of each section.\n"
    "- Drop every meta line ('Length Check', 'Word count', 'Wait,', "
    "'No emojis? Yes.', bullet-list field/value pairs, etc.).\n"
    "- Do NOT invent content. If a section is genuinely missing, write the "
    "header and then `(not provided)` and move on.\n"
    "- If the draft contains '[ANALOGY_QUALITY: N]' anywhere, use that N. "
    "Otherwise use 3.\n\n"
    "MATH FORMATTING (CRITICAL — the page renders LaTeX via KaTeX):\n"
    "- Wrap every variable, symbol, expression, and equation in proper "
    "LaTeX. Inline math uses $...$. A standalone equation on its own line "
    "uses $$...$$.\n"
    "- Convert ALL Unicode math to LaTeX commands. Examples:\n"
    "    θ -> \\theta,  Θ -> \\Theta,  Δ -> \\Delta,  μ -> \\mu,  π -> \\pi\n"
    "    ≈ -> \\approx,  ≤ -> \\leq,  ≥ -> \\geq,  ≠ -> \\neq,  ± -> \\pm\n"
    "    × -> \\times,  · -> \\cdot,  √ -> \\sqrt{},  ∞ -> \\infty\n"
    "    x² -> x^2,  x³ -> x^3,  x_n -> x_{n}\n"
    "    sin, cos, tan -> \\sin, \\cos, \\tan\n"
    "    vectors: bold v -> \\vec{v} or \\mathbf{v}\n"
    "- Units inside math go in \\text{}: write $g \\approx 9.8 \\text{ m/s}^2$ "
    "not $g \\approx 9.8 m/s^2$.\n"
    "- A standalone defining equation should be on its OWN line and use "
    "$$...$$, e.g. $$v_{AB} = v_A - v_B$$.\n"
    "- Variables inside prose use inline $...$. Example: 'the velocity "
    "$v$ at angle $\\theta$ from the horizontal'.\n"
    "- EXCEPTION: in the mapping table, KEEP the Unicode arrow → exactly "
    "as is — it is a layout marker, not math.\n"
    "- Bold **key terms** on first mention using markdown bold; do NOT "
    "bold math symbols (let LaTeX render them)."
)


def _polish_explanation(messy_text: str) -> str:
    """Run a fast extractor LLM pass over messy generator output.

    Uses gemini-2.5-flash-lite by default (cheap, on a separate quota bucket
    from the generator). Returns the cleaned text on success, or the input
    unchanged on any failure (fail-open so the user always sees *something*).
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


# Onboarding option lists. Keeping them at module scope makes them easy to
# extend later (a new interest corpus, a new class level, a new subject)
# without touching the rendering code.
INTERESTS: list[str] = ["Football", "Gaming"]
LEVELS: list[str] = ["Class 11", "Class 12"]
SUBJECTS: list[str] = [
    "Physics — Kinematics",
    "Physics — Work-Energy-Power",
]


def _init_state() -> None:
    """Ensure the session keys we read elsewhere always exist."""
    if "profile" not in st.session_state:
        st.session_state.profile = None
    if "messages" not in st.session_state:
        st.session_state.messages = []


# ---------------------------------------------------------------------------
# Onboarding view
# ---------------------------------------------------------------------------

def _render_onboarding() -> None:
    st.title("Welcome to EcoLearn")
    st.write(
        "EcoLearn is a personalized AI tutor. It explains physics by grounding "
        "every example in something you already care about — your favourite "
        "sport, your favourite game, your daily life. Tell us a little about "
        "yourself and we will teach the rest accordingly."
    )

    # st.form batches the inputs so a single submit click triggers ONE rerun,
    # instead of one rerun per keystroke in the text input.
    with st.form("onboarding_form", clear_on_submit=False):
        name = st.text_input("Your name", placeholder="e.g., Aarav")
        interest = st.selectbox("Primary interest", INTERESTS, index=0)
        level = st.selectbox("Class level", LEVELS, index=0)
        subject = st.selectbox("Subject", SUBJECTS, index=0)
        submitted = st.form_submit_button("Start Learning")

    if not submitted:
        return

    if not name.strip():
        st.error("Please enter your name to continue.")
        return

    st.session_state.profile = {
        "name": name.strip(),
        "interest": interest,
        # Key intentionally named "class" (matching the project spec). The
        # local variable is named `level` to avoid shadowing Python's `class`
        # keyword in the form scope.
        "class": level,
        "subject": subject,
    }
    st.session_state.messages = []
    # Force an immediate rerun so the chat view is rendered on this cycle
    # rather than after the next user interaction.
    st.rerun()


# ---------------------------------------------------------------------------
# Chat view
# ---------------------------------------------------------------------------

def _render_sidebar(profile: dict) -> None:
    """Right-rail with profile summary, session progress, and a reset button."""
    # User messages submitted this session. A simple, defensible proxy for
    # "concepts the student has explored" — every chat turn the student starts
    # is one question/concept.
    concepts_explored = sum(
        1 for m in st.session_state.messages if m["role"] == "user"
    )

    with st.sidebar:
        st.markdown(f"### {profile['name']}")
        st.write(f"**Interest:** {profile['interest']}")
        st.write(f"**Subject:** {profile['subject']}")
        st.write(f"**Level:** {profile['class']}")

        st.divider()
        st.markdown("### Session progress")
        st.metric("Concepts explored", concepts_explored)

        st.divider()
        if st.button("Reset Profile", use_container_width=True):
            st.session_state.profile = None
            st.session_state.messages = []
            st.rerun()


# Tiny CSS shim so user messages float to the right of the chat column while
# assistant messages stay on the left. Streamlit's stock st.chat_message
# left-aligns both; we override the user variant only.
_RIGHT_ALIGN_USER_CSS = """
<style>
div[data-testid="stChatMessage"]:has(span[data-testid="stChatMessageAvatarUser"]) {
    flex-direction: row-reverse;
    text-align: right;
}
</style>
"""


def _generate_reply(
    user_text: str,
    profile: dict,
    on_status=None,
) -> str:
    """Run the multi-agent pipeline and return the cleaned student-facing answer.

    Returns a clean three-section explanation on success. On any pipeline error,
    returns a friendly fallback string so the chat keeps working and the user
    can simply ask again.
    """
    try:
        result = explain_with_review(
            concept=user_text,
            # Corpus metadata stores interest as lowercase ("football",
            # "gaming") — the selectbox value is title-case, so we normalise
            # before the retrieve_interest metadata filter runs.
            interest=profile["interest"].lower(),
            level=profile["class"],
            # max_retries=1 keeps interactive latency manageable; the benchmark
            # script uses 2 because it can afford to wait.
            max_retries=1,
            on_status=on_status,
        )
    except Exception as exc:  # noqa: BLE001 — any failure is shown to user.
        return (
            "_Sorry, something went wrong while generating that explanation._\n\n"
            f"Error: `{type(exc).__name__}`. "
            "Please try asking again — most failures are transient (rate "
            "limits, network blips, or temporary model errors)."
        )

    raw = result.get("explanation") or ""
    # Two passes: a fast regex pre-clean to give the polisher less garbage to
    # chew on, then the polisher LLM to extract the final three-section
    # answer regardless of how the generator dumped its scratchpad.
    pre_cleaned = _sanitize_explanation(raw)

    if on_status is not None:
        try:
            on_status("polishing the answer")
        except Exception:  # noqa: BLE001
            pass

    polished = _polish_explanation(pre_cleaned or raw)

    if not polished or not polished.strip():
        return (
            "_I could not produce a clean explanation this time. "
            "Try rephrasing your question — e.g., a concept name like "
            "'kinetic energy' or 'projectile motion'._"
        )
    return polished


def _render_chat() -> None:
    profile = st.session_state.profile
    _render_sidebar(profile)

    st.header(
        f"Hi {profile['name']} — let's learn "
        f"{profile['subject']} through {profile['interest']}."
    )

    st.markdown(_RIGHT_ALIGN_USER_CSS, unsafe_allow_html=True)

    # Render history. Streamlit handles vertical scrolling automatically when
    # the page exceeds viewport height.
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # st.chat_input sticks to the bottom of the viewport and yields the user's
    # text only on submit (Enter or send button). Returns None otherwise.
    user_text = st.chat_input("Ask about a concept (e.g., 'projectile motion').")
    if not user_text:
        return

    # 1) Append the user message to history and render the bubble immediately
    #    so the page does not look frozen while the pipeline runs.
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    # 2) Run the pipeline. A live status line inside the assistant bubble
    #    shows which agent is currently working (retrieving, generating,
    #    critiquing, polishing). The status placeholder is cleared once the
    #    final reply is ready.
    with st.chat_message("assistant"):
        status_slot = st.empty()
        status_slot.markdown("_EcoLearn is starting up..._")

        def _on_status(message: str) -> None:
            status_slot.markdown(f"_EcoLearn is {message}..._")

        reply = _generate_reply(user_text, profile, on_status=_on_status)
        status_slot.empty()
        st.markdown(reply)

    # 3) Persist the assistant reply to history so the next rerun keeps it.
    st.session_state.messages.append({"role": "assistant", "content": reply})

    # 4) Trigger an explicit rerun so the page redraws cleanly from history,
    #    leaving the chat_input ready for the next message.
    st.rerun()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    st.set_page_config(page_title="EcoLearn", layout="centered")
    _init_state()
    if st.session_state.profile is None:
        _render_onboarding()
    else:
        _render_chat()


if __name__ == "__main__":
    main()
