"""Assessment page — answer the lesson's check question and get graded.

Shows the current concept's self-check question, takes the student's answer,
grades it via the API, and shows score + feedback. Because the grade is
persisted, the roadmap reflects the new mastery the next time it's viewed.

Platform calls used (only the API): get_next_lesson, submit_assessment.
"""

from __future__ import annotations

import streamlit as st

import ui_common
from src import platform_api as api

ui_common.setup_page("Assessment", "✅")
student_id = ui_common.require_student()

result = api.get_next_lesson(student_id, ui_common.CHAPTER_ID)
status = result["status"]

if status == "done":
    st.title("🎉 Chapter complete")
    st.success(result["reason"])
    st.page_link("pages/1_Roadmap.py", label="Back to roadmap", icon="🗺️")
    st.stop()

if status in ("blocked", "lesson_missing"):
    st.title("Nothing to assess yet")
    st.warning(result["reason"])
    st.page_link("pages/2_Lesson.py", label="Back to the lesson", icon="📘")
    st.stop()

concept_id = result["concept_id"]
lesson = result["lesson"]

st.title(f"✅ Check yourself — {result['concept_name']}")
st.markdown("#### Question")
st.markdown(lesson["check_question"])

result_key = f"assess_result::{concept_id}"

with st.form(f"assess_form::{concept_id}", clear_on_submit=False):
    answer = st.text_area("Your answer", height=160, placeholder="Explain your reasoning…")
    submitted = st.form_submit_button("Submit answer", type="primary")

if submitted:
    if not answer.strip():
        st.error("Write an answer before submitting.")
    else:
        with st.spinner("Grading your answer…"):
            try:
                graded = api.submit_assessment(student_id, concept_id, answer.strip())
                st.session_state[result_key] = graded
            except Exception as exc:  # noqa: BLE001
                st.error(
                    f"Couldn't grade that right now ({type(exc).__name__}). "
                    "Please try again in a moment."
                )

# Show the most recent grade for this concept (persists across reruns).
if result_key in st.session_state:
    graded = st.session_state[result_key]
    st.divider()
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Score", f"{graded['score']} / 3")
        st.caption(f"Signal: {graded['mastery_signal'].replace('_', ' ').title()}")
    with col2:
        st.markdown("**Feedback**")
        st.markdown(graded["feedback"] or "_(no feedback returned)_")
        if graded.get("missing_concepts"):
            st.caption("Worth revisiting: " + ", ".join(graded["missing_concepts"]))

    new_status = graded["mastery"]["status"]
    if new_status == "mastered":
        st.success("Mastered! Your roadmap has been updated.")
    else:
        st.info("Keep at it — try the lesson again or ask for help, then re-test.")

    st.divider()
    col_a, col_b = st.columns(2)
    with col_a:
        st.page_link("pages/1_Roadmap.py", label="See updated roadmap", icon="🗺️")
    with col_b:
        if st.button("Next concept →", type="primary", use_container_width=True):
            # Clear this concept's stale result before advancing.
            st.session_state.pop(result_key, None)
            st.switch_page("pages/2_Lesson.py")
