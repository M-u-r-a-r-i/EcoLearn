"""Assessment page — answer the lesson's check question and get graded.

Two explicit modes, switched on a stored grade in session state:

  QUESTION MODE (no grade pending) — pick the concept via get_next_lesson and
      show its self-check question + answer box.
  RESULT MODE (a grade is pending)  — show score/feedback for the concept just
      graded, driven entirely by the stored grade. This is deliberately NOT
      re-derived from get_next_lesson: once you pass, the engine would advance
      to the next concept, and re-deriving here would flip the page to the next
      concept's assessment before the "next lesson" button could fire. Pinning
      the result keeps navigation correct — advancing always lands on the
      next LESSON.

Platform calls used (only the API): get_next_lesson, submit_assessment.
"""

from __future__ import annotations

import streamlit as st

import ui_common
from src import platform_api as api

ui_common.setup_page("Assessment", "✅")
student_id = ui_common.require_student()


def _go_to_next_lesson() -> None:
    """Move on: drop the pending grade + any re-practise pin, go to the lesson."""
    st.session_state.pop("active_grade", None)
    st.session_state.pop("practise_concept", None)
    st.switch_page("pages/2_Lesson.py")


def _practise_again(concept_id: str) -> None:
    """Stay on this concept: pin it and go back to its lesson."""
    st.session_state.pop("active_grade", None)
    st.session_state["practise_concept"] = concept_id
    st.switch_page("pages/2_Lesson.py")


active_grade = st.session_state.get("active_grade")

# ---------------------------------------------------------------------------
# RESULT MODE — show the grade we just stored (stable across reruns).
# ---------------------------------------------------------------------------
if active_grade is not None:
    concept_id = active_grade["concept_id"]
    concept_name = active_grade["concept_name"]
    graded = active_grade["graded"]

    st.title(f"✅ Check yourself — {concept_name}")

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
    score = graded["score"]
    st.divider()

    if new_status == "mastered":
        st.success("🌟 Mastered! Your roadmap has been updated.")
        col_a, col_b = st.columns(2)
        with col_a:
            st.page_link("pages/1_Roadmap.py", label="See updated roadmap", icon="🗺️")
        with col_b:
            if st.button("Continue to next lesson →", type="primary",
                         use_container_width=True):
                _go_to_next_lesson()

    elif score >= 2:
        st.success(
            "✅ You passed (2/3) — solid! You can move on to the next lesson, "
            "or practise this one again to fully master it."
        )
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Move on to next lesson →", type="primary",
                         use_container_width=True):
                _go_to_next_lesson()
        with col_b:
            if st.button("Practise this again", use_container_width=True):
                _practise_again(concept_id)
        st.page_link("pages/1_Roadmap.py", label="See roadmap", icon="🗺️")

    else:
        st.info("Not quite yet — let's reinforce this before moving on.")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Practise this again", type="primary",
                         use_container_width=True):
                _practise_again(concept_id)
        with col_b:
            st.page_link("pages/1_Roadmap.py", label="See roadmap", icon="🗺️")

    st.stop()

# ---------------------------------------------------------------------------
# QUESTION MODE — no grade pending: show the next concept's check question.
# ---------------------------------------------------------------------------
practise_concept = st.session_state.get("practise_concept")
result = api.get_next_lesson(
    student_id, ui_common.CHAPTER_ID, concept_id=practise_concept
)
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

# Guard: an unpolished lesson has no self-check question — don't show a blank
# question + an answer box that would grade against nothing.
check_question = (lesson.get("check_question") or "").strip()
if not check_question:
    st.warning(
        "This concept's self-check question isn't ready yet. You can still read "
        "the lesson and ask for help — check back once it's been prepared."
    )
    st.page_link("pages/2_Lesson.py", label="Back to the lesson", icon="📘")
    st.page_link("pages/1_Roadmap.py", label="Roadmap", icon="🗺️")
    st.stop()

st.markdown("#### Question")
st.markdown(check_question)

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
                # Pin the result so RESULT MODE renders it stably next run.
                st.session_state["active_grade"] = {
                    "concept_id": concept_id,
                    "concept_name": result["concept_name"],
                    "graded": graded,
                }
                st.rerun()
            except Exception as exc:  # noqa: BLE001
                st.error(
                    f"Couldn't grade that right now ({type(exc).__name__}). "
                    "Please try again in a moment."
                )
