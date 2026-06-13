"""Roadmap page — the visual chapter map.

Shows every concept in the chapter coloured by status (mastered green /
available blue / locked grey) and a "Continue Learning" button that jumps to
the next lesson.

Platform calls used (only the API): get_roadmap.
"""

from __future__ import annotations

import streamlit as st

import ui_common
from src import platform_api as api

ui_common.setup_page("Roadmap", "🗺️")
student_id = ui_common.require_student()
profile = st.session_state.get("profile", {})

st.title("🗺️ Your roadmap")
st.caption(
    f"{ui_common.CHAPTER_NAME} · learning through "
    f"{profile.get('interest', '').title()}"
)

roadmap = api.get_roadmap(student_id, ui_common.CHAPTER_ID)

# Progress summary.
total = len(roadmap)
mastered = sum(1 for r in roadmap if r["status"] == "mastered")
st.progress(
    mastered / total if total else 0.0,
    text=f"{mastered} of {total} concepts mastered",
)

# Edge states: a friendly nudge when brand-new, a celebration when finished.
all_done = total > 0 and mastered == total
if mastered == 0:
    first_available = next(
        (r["name"] for r in roadmap if r["status"] == "available"), None
    )
    starter = f" — start with **{first_available}**" if first_available else ""
    st.info(f"You're just getting started{starter}. Hit *Continue learning* below.")
elif all_done:
    st.success(
        "🎉 You've mastered every concept in this chapter! "
        "Revisit any concept for review, or take a well-earned break."
    )

st.write("")

# Concept cards in teaching order.
for row in roadmap:
    if row["status"] == "locked":
        missing = ", ".join(row["missing_prerequisites"])
        detail = f"Locked until you master: {missing}"
    elif row["status"] == "mastered":
        detail = f"Best score {row['best_score']}/3 · {row['attempts']} attempt(s)"
    else:  # available
        detail = "Ready to learn" + (
            f" · best so far {row['best_score']}/3" if row["attempts"] else ""
        )
    st.markdown(
        ui_common.concept_card(row["name"], row["status"], detail),
        unsafe_allow_html=True,
    )

st.divider()
button_label = "🔁 Review the chapter" if all_done else "▶ Continue learning"
if st.button(button_label, type="primary", use_container_width=True):
    st.switch_page("pages/2_Lesson.py")
