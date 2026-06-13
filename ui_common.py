"""Shared UI helpers — presentation and session state only.

This module deliberately imports NOTHING from the platform internals (engine,
store, pipeline, lesson service). Pages get all their data from
`src.platform_api`; this module only injects CSS, guards session state, and
holds UI constants. That separation is what keeps the rule true: the UI talks
to the five API functions for data, and to this module for looks.
"""

from __future__ import annotations

import streamlit as st

# The platform currently ships a single chapter. Centralised here so every
# page refers to the same id; adding a chapter picker later is a local change.
CHAPTER_ID = "motion_straight_line"
CHAPTER_NAME = "Motion in a Straight Line"

# Roadmap status → colour (mastered green / available blue / locked grey).
STATUS_COLORS = {
    "mastered": "#2e7d32",
    "available": "#1565c0",
    "locked": "#9e9e9e",
}
STATUS_LABELS = {
    "mastered": "Mastered",
    "available": "Available",
    "locked": "Locked",
}

_BASE_CSS = """
<style>
/* Tighten the default Streamlit top padding for a denser, app-like feel. */
.block-container { padding-top: 2.5rem; max-width: 820px; }

/* Concept card used on the roadmap. */
.eco-card {
    border: 1px solid #e0e0e0;
    border-left-width: 6px;
    border-radius: 10px;
    padding: 12px 16px;
    margin-bottom: 10px;
    background: #ffffff;
}
.eco-card .eco-title { font-weight: 600; font-size: 1.02rem; }
.eco-card .eco-meta  { color: #666; font-size: 0.82rem; margin-top: 2px; }

/* Status pill. */
.eco-badge {
    color: white;
    padding: 2px 10px;
    border-radius: 10px;
    font-size: 0.78rem;
    white-space: nowrap;
}
</style>
"""


def setup_page(title: str, icon: str = "📘") -> None:
    """Configure the page and inject shared CSS. Call FIRST in every page."""
    st.set_page_config(
        page_title=f"EcoLearn — {title}",
        page_icon=icon,
        layout="centered",
    )
    st.markdown(_BASE_CSS, unsafe_allow_html=True)


def require_student() -> str:
    """Return the active student_id, or halt the page and point to onboarding.

    Reads only `st.session_state` — no platform calls. Pages that need a
    student call this at the top; if none is set (e.g. the user deep-linked to
    a page first), they get a friendly nudge instead of a crash.
    """
    student_id = st.session_state.get("student_id")
    if not student_id:
        st.warning("Tell us who you are first — head to the Onboarding page.")
        st.page_link("app.py", label="Go to Onboarding", icon="🏠")
        st.stop()
    return student_id


def status_badge(status: str) -> str:
    """Return an HTML status pill for a roadmap status."""
    color = STATUS_COLORS.get(status, "#9e9e9e")
    label = STATUS_LABELS.get(status, status.title())
    return f'<span class="eco-badge" style="background:{color};">{label}</span>'


def concept_card(name: str, status: str, detail: str = "") -> str:
    """Return an HTML concept card (coloured left border by status)."""
    color = STATUS_COLORS.get(status, "#9e9e9e")
    meta = f'<div class="eco-meta">{detail}</div>' if detail else ""
    return (
        f'<div class="eco-card" style="border-left-color:{color};">'
        f'<div style="display:flex;justify-content:space-between;align-items:center;">'
        f'<span class="eco-title">{name}</span>{status_badge(status)}</div>'
        f'{meta}</div>'
    )
