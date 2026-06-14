"""Lesson page — the personalised lesson for the student's next concept.

Shows the scenario/explanation and the formal restatement (worked example),
plus a persistent "I'm stuck — ask for help" box that answers inline via the
live tutor without leaving the page.

Platform calls used (only the API): get_next_lesson, ask_help.
"""

from __future__ import annotations

import streamlit as st

import ui_common
from src import platform_api as api

ui_common.setup_page("Lesson", "📘")
student_id = ui_common.require_student()
chapter = ui_common.chapter_selector(api.list_chapters())

# If the student chose "practise this again" after a partial pass, the engine
# would otherwise advance past it — so honour the explicit concept override.
practise_concept = st.session_state.get("practise_concept")
result = api.get_next_lesson(
    student_id, chapter["id"], concept_id=practise_concept
)
status = result["status"]

# Terminal / non-teaching states.
if status == "done":
    st.title("🎉 Chapter complete")
    st.success(result["reason"])
    st.page_link("pages/1_Roadmap.py", label="Back to roadmap", icon="🗺️")
    st.stop()

if status in ("blocked", "lesson_missing"):
    st.title("Nothing to learn just yet")
    st.warning(result["reason"])
    st.page_link("pages/1_Roadmap.py", label="Back to roadmap", icon="🗺️")
    st.stop()

# Teaching states: "new" or "review".
concept_id = result["concept_id"]
lesson = result["lesson"]

st.title(result["concept_name"])
if status == "review":
    st.info(f"🔁 **Quick review before we move on.** {result['reason']}")
else:
    st.caption(result["reason"])

# Scenario (the analogy + mapping + where-it-breaks-down) lives in `body`;
# the formal restatement lives in `worked_example`. The section headers were
# stripped during parsing, so we re-add them here for a clean reading layout.
st.markdown("### Scenario")
st.markdown(lesson["body"])

if lesson["worked_example"].strip():
    st.markdown("### Formal restatement")
    st.markdown(lesson["worked_example"])

# ---------------------------------------------------------------------------
# Persistent "ask for help" box — answers inline, never leaves the lesson.
# ---------------------------------------------------------------------------
st.divider()
st.subheader("🙋 I'm stuck — ask for help")

help_key = f"help_reply::{concept_id}"

with st.form(f"help_form::{concept_id}", clear_on_submit=False):
    question = st.text_area(
        "Ask anything about this concept",
        placeholder="e.g. Why is displacement a vector but distance is not?",
        height=90,
    )
    asked = st.form_submit_button("Ask for help")

if asked and question.strip():
    with st.spinner("Thinking through your question…"):
        try:
            resp = api.ask_help(student_id, concept_id, question.strip())
            answer = resp["answer"]
        except Exception as exc:  # noqa: BLE001 — keep the lesson usable on failure.
            answer = (
                f"_Sorry, live help is unavailable right now "
                f"({type(exc).__name__}). Please try again in a moment._"
            )
    # Stash so the reply survives reruns and the student stays on the lesson.
    st.session_state[help_key] = {"question": question.strip(), "answer": answer}

if help_key in st.session_state:
    record = st.session_state[help_key]
    with st.chat_message("user"):
        st.markdown(record["question"])
    with st.chat_message("assistant"):
        st.markdown(record["answer"])

st.divider()
col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/1_Roadmap.py", label="Roadmap", icon="🗺️")
with col2:
    if st.button("Take the assessment →", type="primary", use_container_width=True):
        st.switch_page("pages/3_Assessment.py")
