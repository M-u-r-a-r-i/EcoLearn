"""EcoLearn — multi-page learning platform (entry / onboarding page).

This is the landing page of the multi-page Streamlit app. The other pages live
in `pages/` and Streamlit auto-discovers them into the sidebar nav.

The entire UI (this file and every page) talks to the platform through exactly
one module — `src.platform_api` — and never reaches into the engine, store,
pipeline, or lesson service directly. This page uses a single API function:

    create_or_load_student(name, interest, level)

The previous single-page chatbot is preserved as `legacy_chat_app.py`
(`streamlit run legacy_chat_app.py`) and is independent of this platform.
"""

from __future__ import annotations

import streamlit as st

import ui_common
from src import platform_api as api

ui_common.setup_page("Onboarding", "🌱")

st.title("🌱 EcoLearn")
st.caption(
    "A personalised physics tutor that explains concepts through what you love."
)

# Already onboarded this session → welcome back, offer to continue or switch.
if st.session_state.get("student_id"):
    profile = st.session_state.get("profile", {})
    st.success(
        f"Welcome back, **{profile.get('name', 'there')}**! "
        f"You're learning **{ui_common.CHAPTER_NAME}** through "
        f"**{profile.get('interest', '').title()}**."
    )
    st.page_link("pages/1_Roadmap.py", label="Open my roadmap", icon="🗺️")
    st.page_link("pages/2_Lesson.py", label="Jump back into the lesson", icon="📘")

    with st.expander("Not you, or want to change interest?"):
        if st.button("Start over as a new student"):
            for key in ("student_id", "profile"):
                st.session_state.pop(key, None)
            st.rerun()

# Not onboarded → show the sign-up form.
else:
    st.write(
        "Tell us a little about yourself and we'll build your learning path."
    )
    with st.form("onboarding"):
        name = st.text_input("Your name", placeholder="e.g. Ada")
        interest = st.selectbox(
            "Learn physics through…",
            options=["Football", "Gaming"],
            help="Every lesson grounds its analogies in this interest.",
        )
        level = st.selectbox("Your class", options=["Class 11", "Class 12"])
        submitted = st.form_submit_button("Start learning", type="primary")

    if submitted:
        if not name.strip():
            st.error("Please enter your name to continue.")
        else:
            # The ONLY platform call on this page.
            profile = api.create_or_load_student(
                name=name.strip(),
                interest=interest.lower(),
                level=level,
            )
            st.session_state.student_id = profile["student_id"]
            st.session_state.profile = profile
            st.success(f"You're all set, {profile['name']}! Taking you to your roadmap…")
            st.switch_page("pages/1_Roadmap.py")
