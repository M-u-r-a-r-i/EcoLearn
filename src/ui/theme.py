"""EcoLearn design system — the single source of truth for the look & feel.

Everything visual flows from the tokens in this module. Pages and components
read the palette/spacing constants here instead of hard-coding hex values, and
every page calls `inject_global_css()` once (via `ui_common.setup_page`) to
apply the global theme.

Design target: a polished, public-ready edtech product in the visual register
of Brilliant.org — clean, premium, calm, modern, with generous whitespace.

This module imports nothing from the platform internals. Presentation only.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Palette — the only place colours are defined.
# ---------------------------------------------------------------------------
PRIMARY = "#4F46E5"        # deep indigo — primary actions, brand
PRIMARY_DARK = "#3730A3"   # hover / pressed indigo
ACCENT = "#F59E0B"         # amber — highlights, callouts
SUCCESS = "#10B981"        # green — mastered / passed
WARNING = "#F59E0B"        # amber — partial / caution (same as accent by design)
BACKGROUND = "#FAFAFB"     # app background
SURFACE = "#FFFFFF"        # cards, sidebar, inputs
TEXT_DARK = "#1E293B"      # primary text
TEXT_MUTED = "#64748B"     # secondary text
BORDER = "#E2E8F0"         # hairline borders / dividers

# Status → colour, used by roadmap nodes and badges.
STATUS_COLORS = {
    "mastered": SUCCESS,
    "available": PRIMARY,
    "locked": TEXT_MUTED,
}

# ---------------------------------------------------------------------------
# Tokens — radii, shadows, spacing scale.
# ---------------------------------------------------------------------------
RADIUS_CARD = "14px"
RADIUS_BUTTON = "10px"

SHADOW_RESTING = "0 1px 3px rgba(0, 0, 0, 0.08)"
SHADOW_HOVER = "0 8px 24px rgba(79, 70, 229, 0.12)"

# 8px spacing scale — reference these so spacing stays on the grid.
SPACE = {1: "8px", 2: "16px", 3: "24px", 4: "32px", 5: "40px", 6: "48px"}

MAX_WIDTH = "960px"        # main content max-width on wide screens

FONT_STACK = (
    "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, "
    "Helvetica, Arial, sans-serif"
)


def _global_css() -> str:
    """Build the global stylesheet string from the tokens above."""
    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ---------- Typography: Inter everywhere ---------- */
html, body, [class*="css"], .stApp, .stMarkdown,
input, textarea, button, select, label, p, span, div,
h1, h2, h3, h4, h5, h6 {{
    font-family: {FONT_STACK} !important;
}}

/* Exception: never override Streamlit's Material icon font, or its icon
   ligatures (expander chevrons, sidebar arrows, page-link icons) render as
   literal text like "keyboard_double_arrow_left". */
span[data-testid="stIconMaterial"],
.material-icons, .material-symbols-outlined, .material-symbols-rounded {{
    font-family: 'Material Symbols Rounded', 'Material Symbols Outlined',
                 'Material Icons' !important;
}}

.stApp {{
    background: {BACKGROUND};
    color: {TEXT_DARK};
}}

h1, h2, h3, h4 {{
    color: {TEXT_DARK};
    font-weight: 700;
    letter-spacing: -0.015em;
}}

/* ---------- Hide Streamlit chrome ---------- */
header[data-testid="stHeader"] {{ display: none !important; }}
[data-testid="stToolbar"] {{ display: none !important; }}
[data-testid="stDecoration"] {{ display: none !important; }}
[data-testid="stStatusWidget"] {{ display: none !important; }}
#MainMenu {{ visibility: hidden !important; }}
footer {{ visibility: hidden !important; height: 0 !important; }}
/* "Made with Streamlit" / hosted badge */
[data-testid="stBottomBlockContainer"] a[href*="streamlit.io"],
a[href*="share.streamlit.io"] {{ display: none !important; }}

/* ---------- Main content: reduced top padding, centered max-width ---------- */
.block-container,
[data-testid="stMainBlockContainer"] {{
    padding-top: {SPACE[4]} !important;
    padding-bottom: {SPACE[6]} !important;
    max-width: {MAX_WIDTH} !important;
}}

/* ---------- Buttons: solid indigo, rounded, hover lift ---------- */
.stButton > button,
.stFormSubmitButton > button,
.stDownloadButton > button,
[data-testid="stBaseButton-primary"],
[data-testid="stBaseButton-secondary"],
[data-testid="stBaseButton-secondaryFormSubmit"] {{
    background: {PRIMARY} !important;
    color: #FFFFFF !important;
    border: 1px solid {PRIMARY} !important;
    border-radius: {RADIUS_BUTTON} !important;
    font-weight: 600 !important;
    padding: 0.55rem 1.2rem !important;
    box-shadow: {SHADOW_RESTING};
    transition: transform 0.12s ease, box-shadow 0.18s ease,
                background 0.18s ease !important;
}}

.stButton > button:hover,
.stFormSubmitButton > button:hover,
.stDownloadButton > button:hover,
[data-testid="stBaseButton-primary"]:hover,
[data-testid="stBaseButton-secondary"]:hover {{
    background: {PRIMARY_DARK} !important;
    border-color: {PRIMARY_DARK} !important;
    color: #FFFFFF !important;
    transform: translateY(-2px);
    box-shadow: {SHADOW_HOVER};
}}

.stButton > button:active,
.stFormSubmitButton > button:active {{
    transform: translateY(0);
    box-shadow: {SHADOW_RESTING};
}}

.stButton > button:focus,
.stFormSubmitButton > button:focus {{
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.25) !important;
}}

/* ---------- Sidebar: clean white panel ---------- */
[data-testid="stSidebar"] {{
    background: {SURFACE};
    border-right: 1px solid {BORDER};
}}
[data-testid="stSidebar"] > div:first-child {{
    padding: {SPACE[3]} {SPACE[2]};
}}
[data-testid="stSidebarNav"] a {{
    border-radius: {RADIUS_BUTTON};
}}

/* ---------- Links ---------- */
a, a:visited {{ color: {PRIMARY}; text-decoration: none; }}
a:hover {{ color: {PRIMARY_DARK}; text-decoration: underline; }}

/* ---------- Inputs ---------- */
.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] > div,
[data-baseweb="input"] {{
    border-radius: {RADIUS_BUTTON} !important;
    border: 1px solid {BORDER} !important;
    background: {SURFACE} !important;
    color: {TEXT_DARK} !important;
}}
.stTextInput input:focus,
.stTextArea textarea:focus {{
    border-color: {PRIMARY} !important;
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.12) !important;
}}
.stTextInput label, .stTextArea label, .stSelectbox label {{
    color: {TEXT_MUTED} !important;
    font-weight: 600 !important;
    font-size: 0.86rem !important;
}}

/* ---------- Progress bar ---------- */
.stProgress > div > div > div > div {{
    background: linear-gradient(90deg, {PRIMARY}, {PRIMARY_DARK}) !important;
}}

/* ---------- Captions / muted text ---------- */
[data-testid="stCaptionContainer"], .stCaption {{
    color: {TEXT_MUTED} !important;
}}
</style>
"""


def inject_global_css() -> None:
    """Inject the global EcoLearn stylesheet. Call once per page render.

    Imported lazily inside the function so this module stays import-safe even
    in non-Streamlit contexts (e.g. tooling that just reads the tokens).
    """
    import streamlit as st

    st.markdown(_global_css(), unsafe_allow_html=True)
