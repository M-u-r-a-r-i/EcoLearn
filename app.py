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

from src.agents.assessor import generate_question, grade_answer
from src.agents.polisher import polish_explanation
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
# Router — decides whether a message needs the full pipeline or just a chat.
# ---------------------------------------------------------------------------

_ROUTER_MODEL_DEFAULT = "gemma-4-31b-it"
_ROUTER_PROMPT = (
    "You are an intent router for an AI physics tutor for Class 11 students. "
    "Decide which of three modes the student's message belongs to:\n"
    "- TUTOR: the student wants a physics concept explained.\n"
    "- ASSESS: the student wants to be tested. Includes explicit requests "
    "(quiz me, test me, ask a question) AND implicit signals after an "
    "explanation (I understood, got it, makes sense, I'm ready).\n"
    "- CHAT: anything else — greetings, thanks, off-topic, requests to move "
    "on without a new concept named, vague clarifications.\n\n"
    "Output STRICT JSON only — no prose before or after, no markdown fences:\n"
    "{\n"
    '  "mode": "TUTOR" or "ASSESS" or "CHAT",\n'
    '  "concept": "<for TUTOR: the concept to explain in 1-5 words. For '
    'ASSESS: the concept to be quizzed on, OR empty string to quiz on the '
    'concept the student most recently studied. For CHAT: empty string.>",\n'
    '  "chat_reply": "<for CHAT: a short, warm reply. For TUTOR and ASSESS: '
    'empty string.>"\n'
    "}\n\n"
    "CHAT REPLY RULES (only when mode is CHAT):\n"
    "- Maximum 2 sentences.\n"
    "- Warm but not sycophantic. Do NOT say things like 'Great question!'.\n"
    "- Gently steer back to learning. If appropriate, suggest the student "
    "name a concept to explore.\n"
    "- If the message is an off-topic question (not physics), politely say "
    "you focus on physics and invite a physics topic.\n\n"
    "EXAMPLES (the student's interest area is shown in [brackets] for context):\n"
    "[football] 'hello' → "
    '{"mode":"CHAT","concept":"","chat_reply":"Hi! What physics concept '
    'would you like to explore today?"}\n'
    "[football] 'thanks' → "
    '{"mode":"CHAT","concept":"","chat_reply":"You are welcome. Ready for '
    'a new concept, or want a practice question to test yourself?"}\n'
    "[football] 'I understood' → "
    '{"mode":"ASSESS","concept":"","chat_reply":""}\n'
    "[football] 'got it' → "
    '{"mode":"ASSESS","concept":"","chat_reply":""}\n'
    "[football] 'makes sense' → "
    '{"mode":"ASSESS","concept":"","chat_reply":""}\n'
    "[football] 'quiz me' → "
    '{"mode":"ASSESS","concept":"","chat_reply":""}\n'
    "[football] 'test me on momentum' → "
    '{"mode":"ASSESS","concept":"momentum","chat_reply":""}\n'
    "[football] 'give me a practice question' → "
    '{"mode":"ASSESS","concept":"","chat_reply":""}\n'
    "[football] 'what is kinetic energy' → "
    '{"mode":"TUTOR","concept":"kinetic energy","chat_reply":""}\n'
    "[gaming] 'explain projectile motion' → "
    '{"mode":"TUTOR","concept":"projectile motion","chat_reply":""}\n'
    "[football] 'I am confused about acceleration' → "
    '{"mode":"TUTOR","concept":"acceleration","chat_reply":""}\n'
    "[football] 'next concept' → "
    '{"mode":"CHAT","concept":"","chat_reply":"Sure — which concept would '
    'you like to learn next?"}\n'
    "[football] 'who won the world cup' → "
    '{"mode":"CHAT","concept":"","chat_reply":"I focus on Class 11 physics, '
    'not match scores. Which physics topic would you like to explore?"}\n'
)


def _classify_intent(user_text: str, profile: dict) -> dict:
    """Decide whether the user message needs the pipeline or just a quick reply.

    Returns a dict with keys: mode ("TUTOR" or "CHAT"), concept (str), and
    chat_reply (str). On any classifier failure we fail OPEN — i.e. treat the
    message as a tutor request — so a buggy router never silences a real
    learning question. Worst case behaviour matches the previous code.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"mode": "TUTOR", "concept": user_text, "chat_reply": ""}

    model = os.getenv("ROUTER_MODEL", _ROUTER_MODEL_DEFAULT).strip()

    contents = (
        f"{_ROUTER_PROMPT}\n\n"
        f"---\n"
        f"Student interest: {profile.get('interest', 'unknown')}\n"
        f"Student level:    {profile.get('class', 'Class 11')}\n"
        f"Student message:  {user_text}\n\n"
        f"Emit the JSON now."
    )

    config_kwargs: dict = {
        "temperature": 0.0,
        "max_output_tokens": 512,
    }
    if model.startswith("gemini-"):
        config_kwargs["response_mime_type"] = "application/json"
    if model.startswith("gemini-2.5"):
        config_kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=0)

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=types.GenerateContentConfig(**config_kwargs),
        )
        raw = (response.text or "").strip()
    except Exception:  # noqa: BLE001 — fail open on any router error.
        return {"mode": "TUTOR", "concept": user_text, "chat_reply": ""}

    if not raw:
        return {"mode": "TUTOR", "concept": user_text, "chat_reply": ""}

    # Best-effort JSON parse: try direct first, then the first JSON-shaped
    # block in the raw text (handles models that wrap output in fences).
    import json
    parsed: dict | None = None
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if match:
            try:
                parsed = json.loads(match.group(0))
            except json.JSONDecodeError:
                parsed = None

    if not isinstance(parsed, dict) or "mode" not in parsed:
        return {"mode": "TUTOR", "concept": user_text, "chat_reply": ""}

    mode = parsed.get("mode", "TUTOR")
    if mode not in {"TUTOR", "ASSESS", "CHAT"}:
        mode = "TUTOR"
    return {
        "mode": mode,
        # Empty-string-on-ASSESS is intentional — handler will fall back to
        # session_state.last_concept. For TUTOR we keep the raw text as a
        # last resort if the router returns an empty concept.
        "concept": (parsed.get("concept") or "").strip(),
        "chat_reply": (parsed.get("chat_reply") or "").strip(),
    }


# ---------------------------------------------------------------------------
# Polisher — a small, deterministic LLM pass that extracts the final answer.
# The implementation lives in src/agents/polisher.py so the offline lesson
# factory can share it. The thin alias keeps the existing call sites here.
# ---------------------------------------------------------------------------

_polish_explanation = polish_explanation


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
    # Tracks the most-recent concept the student was tutored on; used as the
    # default topic when the student asks to be quizzed.
    if "last_concept" not in st.session_state:
        st.session_state.last_concept = None
    # When the assessor has asked a question, the question dict is stashed
    # here so the next user message can be graded against it.
    if "last_question" not in st.session_state:
        st.session_state.last_question = None
    # State flag: True when we are mid-quiz waiting for the student's answer.
    if "awaiting_answer" not in st.session_state:
        st.session_state.awaiting_answer = False
    # Transient UI affordance to show below the chat history:
    #   None         — nothing pending
    #   "offer_quiz" — explanation just shown; offer Yes/Not-yet buttons
    #   "post_grade" — answer just graded; offer Try-another/Move-on buttons
    if "pending_action" not in st.session_state:
        st.session_state.pending_action = None
    # Marks an in-flight action being executed on this render.
    # While set, NO buttons render — preventing the user from accidentally
    # interrupting a long-running operation with a stray click on a stale
    # button. Cleared by the worker after it finishes.
    if "processing_action" not in st.session_state:
        st.session_state.processing_action = None
    # Mastery ledger per concept.
    #   { concept_name: {"attempts": int, "best_score": int, "status": str} }
    if "mastery" not in st.session_state:
        st.session_state.mastery = {}


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
    # Distinct concepts that triggered a real tutoring turn.
    concepts_explored = len({
        (m.get("concept") or "").strip().lower()
        for m in st.session_state.messages
        if m.get("role") == "user"
        and m.get("mode") == "TUTOR"
        and (m.get("concept") or "").strip()
    })
    # Number of practice questions the student has answered.
    quizzes_taken = sum(
        1 for m in st.session_state.messages
        if m.get("role") == "user" and m.get("mode") == "ANSWER"
    )

    with st.sidebar:
        st.markdown(f"### {profile['name']}")
        st.write(f"**Interest:** {profile['interest']}")
        st.write(f"**Subject:** {profile['subject']}")
        st.write(f"**Level:** {profile['class']}")

        st.divider()
        st.markdown("### Session progress")
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Concepts explored", concepts_explored)
        with col_b:
            st.metric("Quizzes taken", quizzes_taken)

        # Mastery panel: one coloured pill per concept the student has been
        # quizzed on. Sorted with mastered → partial → not_yet so the most
        # progress shows first.
        if st.session_state.mastery:
            st.divider()
            st.markdown("### Mastery")
            order = {"mastered": 0, "partial": 1, "not_yet": 2}
            sorted_items = sorted(
                st.session_state.mastery.items(),
                key=lambda kv: (order.get(kv[1].get("status", "not_yet"), 3),
                                kv[0]),
            )
            for concept, data in sorted_items:
                badge = _mastery_badge(data.get("status", "not_yet"))
                best = data.get("best_score", 0)
                attempts = data.get("attempts", 0)
                st.markdown(
                    f"{badge} **{concept}** "
                    f"<span style='color:#9e9e9e; font-size:0.85em;'>"
                    f"(best {best}/3 · {attempts} attempt"
                    f"{'s' if attempts != 1 else ''})</span>",
                    unsafe_allow_html=True,
                )

        st.divider()
        if st.button("Reset Profile", use_container_width=True):
            st.session_state.profile = None
            st.session_state.messages = []
            st.session_state.last_concept = None
            st.session_state.last_question = None
            st.session_state.awaiting_answer = False
            st.session_state.pending_action = None
            st.session_state.processing_action = None
            st.session_state.mastery = {}
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


def _explain_pipeline_error(exc: Exception) -> str:
    """Turn a pipeline exception into a friendlier student-facing message."""
    err_msg = str(exc).lower()
    if "429" in err_msg or "quota" in err_msg or "resource_exhausted" in err_msg:
        return (
            "_The model is rate-limited right now._\n\n"
            "Free-tier quotas reset after a short wait. Try the same question "
            "again in a minute or two — no need to rephrase."
        )
    if "no text" in err_msg or "empty" in err_msg:
        return (
            "_The model returned an empty response._\n\n"
            "This sometimes happens when a prompt confuses the model. Please "
            "ask the same concept again."
        )
    if "not_found" in err_msg or "404" in err_msg:
        return (
            "_The configured model is unavailable._\n\n"
            "Check `GEMINI_MODEL` in `.env` — the current value may not be a "
            "valid model ID on your API key."
        )
    return (
        "_Sorry, something went wrong while generating that explanation._\n\n"
        f"Error: `{type(exc).__name__}`. Please try asking again — most "
        "failures are transient (rate limits, network blips, temporary model "
        "errors)."
    )


def _generate_reply(
    user_text: str,
    profile: dict,
    on_status=None,
) -> tuple[str, bool]:
    """Run the multi-agent pipeline and return (text, ok).

    `ok` is True only when a real explanation was produced. Callers can use
    it to decide whether to offer a quiz, save `last_concept`, or treat the
    turn as an inert error.
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
        return _explain_pipeline_error(exc), False

    raw = result.get("explanation") or ""
    pre_cleaned = _sanitize_explanation(raw)

    if on_status is not None:
        try:
            on_status("polishing the answer")
        except Exception:  # noqa: BLE001
            pass

    polished = _polish_explanation(pre_cleaned or raw)

    if not polished or not polished.strip():
        return (
            "_I could not produce a clean explanation this time. Try the "
            "same concept again, or rephrase if it keeps happening._",
            False,
        )
    return polished, True


def _status_from_score(score: int) -> str:
    """Map a 0-3 score to a mastery status label."""
    if score >= 3:
        return "mastered"
    if score >= 2:
        return "partial"
    return "not_yet"


def _update_mastery(concept: str, score: int) -> None:
    """Bump attempts, take best score, refresh status for the concept."""
    if not concept:
        return
    entry = st.session_state.mastery.get(
        concept, {"attempts": 0, "best_score": 0, "status": "not_yet"},
    )
    entry["attempts"] = entry.get("attempts", 0) + 1
    entry["best_score"] = max(entry.get("best_score", 0), int(score))
    entry["status"] = _status_from_score(entry["best_score"])
    st.session_state.mastery[concept] = entry


_MASTERY_COLORS = {
    "mastered": "#2e7d32",  # green
    "partial":  "#ef6c00",  # amber
    "not_yet":  "#757575",  # grey
}


def _mastery_badge(status: str) -> str:
    """Tiny coloured pill for the sidebar mastery panel."""
    color = _MASTERY_COLORS.get(status, _MASTERY_COLORS["not_yet"])
    label = status.replace("_", " ").title()
    return (
        f'<span style="background:{color}; color:white; padding:2px 8px; '
        f'border-radius:8px; font-size:0.8em; white-space:nowrap;">'
        f"{label}</span>"
    )


def _do_pending_work(profile: dict) -> None:
    """Execute whichever long-running action `processing_action` names.

    Called from `_render_pending_actions` at the START of each render, before
    any buttons render. While this is running, the page shows ONLY a spinner
    in the assistant bubble — there are no clickable elements that a stray
    click could land on. After the work finishes, the worker clears
    `processing_action` and calls `st.rerun()`.
    """
    action = st.session_state.get("processing_action")
    if action != "generating_question":
        st.session_state.processing_action = None
        return

    concept = st.session_state.last_concept or ""
    if not concept:
        st.session_state.processing_action = None
        st.rerun()
        return

    with st.chat_message("assistant"):
        with st.spinner("EcoLearn is preparing a practice question..."):
            try:
                qdict = generate_question(
                    concept,
                    profile["interest"].lower(),
                    profile["class"],
                )
            except Exception as exc:  # noqa: BLE001 — surface any failure.
                qdict = {"error": f"{type(exc).__name__}: {exc}"}

    if qdict.get("error") or not qdict.get("question"):
        st.session_state.messages.append({
            "role": "assistant",
            "content": (
                "_I had trouble preparing a question on this concept. "
                "Try again in a moment, or ask about another topic._"
            ),
        })
        st.session_state.processing_action = None
        st.rerun()
        return

    question_text = (
        f"**Practice question — _{concept}_**\n\n"
        f"{qdict['question']}\n\n"
        "_Type your answer below._"
    )
    st.session_state.messages.append(
        {"role": "assistant", "content": question_text}
    )
    st.session_state.last_question = qdict
    st.session_state.awaiting_answer = True
    st.session_state.processing_action = None
    st.rerun()


def _format_grade(verdict: dict) -> str:
    """Render the assessor's verdict as a friendly markdown reply."""
    score = verdict.get("score", 0)
    mastery = (verdict.get("mastery_signal") or "not_yet").replace("_", " ")
    feedback = (verdict.get("feedback") or "").strip()
    missing = verdict.get("missing_concepts") or []

    lines = [f"**Score: {score} / 3 — {mastery}**", ""]
    if feedback:
        lines.append(feedback)
    if missing:
        lines.append("")
        lines.append("**Concepts to revisit:**")
        for m in missing:
            lines.append(f"- {m}")
    lines.append("")
    lines.append(
        "_Ask any concept to keep learning, or say 'test me again' for "
        "another question._"
    )
    return "\n".join(lines)


def _handle_answer(user_text: str) -> tuple[str, str, str]:
    """Grade the student's reply to the previously-asked question."""
    question_data = st.session_state.last_question or {}
    concept = st.session_state.last_concept or ""

    with st.chat_message("assistant"):
        with st.spinner("EcoLearn is grading your answer..."):
            try:
                verdict = grade_answer(
                    question_data.get("question", ""),
                    question_data.get("expected_concepts", []),
                    user_text,
                )
            except Exception as exc:  # noqa: BLE001
                verdict = {
                    "score": 0,
                    "mastery_signal": "not_yet",
                    "feedback": "",
                    "missing_concepts": [],
                    "error": f"{type(exc).__name__}: {exc}",
                }

        if verdict.get("error"):
            # Grader failed. Don't pollute mastery with a fake "not_yet". Show
            # a friendly message and return state to the post-grade buttons so
            # the student can try again.
            reply = (
                "_I could not grade that answer right now (the grader is "
                "rate-limited or returned an error)._\n\n"
                "Click **Try another question** to retry or **Move on** to "
                "continue learning."
            )
            st.markdown(reply)
            st.session_state.awaiting_answer = False
            st.session_state.last_question = None
            st.session_state.pending_action = "post_grade"
            return reply, "ANSWER", concept

        reply = _format_grade(verdict)
        st.markdown(reply)

    # Real grade: update mastery.
    _update_mastery(concept, verdict.get("score", 0))

    st.session_state.awaiting_answer = False
    st.session_state.last_question = None
    st.session_state.pending_action = "post_grade"
    return reply, "ANSWER", concept


def _handle_new_turn(user_text: str, profile: dict) -> tuple[str, str, str]:
    """Route a fresh user message through CHAT, TUTOR, or ASSESS."""
    with st.chat_message("assistant"):
        status_slot = st.empty()
        status_slot.markdown("_EcoLearn is reading your message..._")

        intent = _classify_intent(user_text, profile)
        mode = intent.get("mode", "TUTOR")
        concept_tag = (intent.get("concept") or "").strip()

        if mode == "ASSESS":
            # Use the explicit concept if the router extracted one, else fall
            # back to the most recent concept the student studied.
            target_concept = concept_tag or st.session_state.last_concept or ""
            if not target_concept:
                status_slot.empty()
                reply = (
                    "I'd love to test you. First, tell me which concept you "
                    "want to learn — for example, 'explain kinetic energy'."
                )
                st.markdown(reply)
                return reply, "CHAT", ""

            status_slot.markdown("_EcoLearn is preparing a practice question..._")
            qdict = generate_question(
                target_concept,
                profile["interest"].lower(),
                profile["class"],
            )
            status_slot.empty()

            if qdict.get("error") or not qdict.get("question"):
                reply = (
                    "I could not prepare a question right now. Could you try "
                    "again in a moment?"
                )
                st.markdown(reply)
                return reply, "CHAT", ""

            reply = (
                f"**Practice question — _{target_concept}_**\n\n"
                f"{qdict['question']}\n\n"
                "_Type your answer below and I'll grade it._"
            )
            st.markdown(reply)
            # Arm the state machine: next user message will be graded.
            st.session_state.awaiting_answer = True
            st.session_state.last_question = qdict
            return reply, "ASSESS_REQUEST", target_concept

        if mode == "CHAT":
            reply = (
                intent.get("chat_reply")
                or "Got it. What would you like to learn next?"
            )
            status_slot.empty()
            st.markdown(reply)
            return reply, "CHAT", ""

        # mode == "TUTOR"
        def _on_status(message: str) -> None:
            status_slot.markdown(f"_EcoLearn is {message}..._")

        concept = concept_tag or user_text
        reply, ok = _generate_reply(concept, profile, on_status=_on_status)
        status_slot.empty()
        st.markdown(reply)

        if not ok:
            # Pipeline error — don't pretend a concept was taught. Skip the
            # quiz offer and don't update last_concept. Logged as CHAT so the
            # sidebar's "Concepts explored" metric stays honest.
            return reply, "CHAT", ""

        # Real explanation: remember the concept and arm the quiz offer.
        st.session_state.last_concept = concept
        st.session_state.pending_action = "offer_quiz"
        return reply, "TUTOR", concept


def _render_pending_actions(profile: dict) -> None:
    """Show the transient affordance for the current pending state.

    If `processing_action` is set, ONLY a spinner renders (no buttons), so a
    stray click cannot interrupt the work.

    Otherwise — for `offer_quiz` or `post_grade` — buttons render. Their
    handlers only flip state and `st.rerun()`; they never do the long work
    inline. That keeps each button press atomic.
    """
    # In-flight work always wins. Render the spinner, do the work, rerun.
    if st.session_state.get("processing_action"):
        _do_pending_work(profile)
        return

    action = st.session_state.pending_action
    if action is None:
        return

    if action == "offer_quiz":
        with st.chat_message("assistant"):
            st.markdown("**Want to try a quick question to check?**")
            col_yes, col_no = st.columns(2)
            with col_yes:
                if st.button(
                    "Yes, quiz me",
                    key="offer_quiz_yes",
                    type="primary",
                    use_container_width=True,
                ):
                    # Two-phase: flip state, rerun. The actual question
                    # generation happens on the NEXT render with no buttons
                    # visible, so a stray click cannot cancel it.
                    st.session_state.pending_action = None
                    st.session_state.processing_action = "generating_question"
                    st.rerun()
            with col_no:
                if st.button(
                    "Not yet",
                    key="offer_quiz_no",
                    use_container_width=True,
                ):
                    st.session_state.pending_action = None
                    st.rerun()

    elif action == "post_grade":
        with st.chat_message("assistant"):
            col_again, col_done = st.columns(2)
            with col_again:
                if st.button(
                    "Try another question",
                    key="post_grade_again",
                    use_container_width=True,
                ):
                    st.session_state.pending_action = None
                    st.session_state.processing_action = "generating_question"
                    st.rerun()
            with col_done:
                if st.button(
                    "Move on",
                    key="post_grade_done",
                    type="primary",
                    use_container_width=True,
                ):
                    st.session_state.pending_action = None
                    st.rerun()


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

    # Render the current transient affordance (offer-quiz buttons OR
    # post-grade buttons). Lives between history and the input bar.
    _render_pending_actions(profile)

    # st.chat_input sticks to the bottom of the viewport and yields the user's
    # text only on submit (Enter or send button). Returns None otherwise.
    # When a long-running action is in flight we disable the input so the
    # student can't fire a new turn that races with the worker.
    user_text = st.chat_input(
        "Ask about a concept (e.g., 'projectile motion').",
        disabled=bool(st.session_state.get("processing_action")),
    )
    if not user_text:
        return

    # Typing into the chat is an implicit "skip" of any pending button
    # affordance — drop it so we don't leave stale buttons under the new turn.
    st.session_state.pending_action = None

    # 1) Render the user bubble immediately for instant visual feedback.
    with st.chat_message("user"):
        st.markdown(user_text)

    # 2) Two paths through this turn, decided by state:
    #    - If we previously asked a question, treat this message as the
    #      student's answer and grade it.
    #    - Otherwise route the message via the LLM router (CHAT / TUTOR /
    #      ASSESS) and dispatch accordingly.
    if st.session_state.awaiting_answer and st.session_state.last_question:
        reply, msg_mode, msg_concept = _handle_answer(user_text)
    else:
        reply, msg_mode, msg_concept = _handle_new_turn(user_text, profile)

    # 3) Persist both turns to history. The user message carries the routing
    #    decision so the sidebar (and any future analytics) can tell which
    #    turns were tutoring vs chat vs quiz vs answer.
    st.session_state.messages.append({
        "role": "user",
        "content": user_text,
        "mode": msg_mode,
        "concept": msg_concept,
    })
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
