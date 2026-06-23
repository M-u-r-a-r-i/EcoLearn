"""EcoLearn HTTP API — a thin FastAPI layer over src/platform_api.py.

WHAT THIS FILE IS
-----------------
This is the "web front door" to your existing Python backend. Your Next.js site
(running in the browser) cannot import Python functions directly — browsers speak
HTTP. So we put a small web server in front of `platform_api` that:

    receives an HTTP request  ->  calls your existing function  ->  returns JSON

We do NOT change any business logic here. Every real decision still lives in
`src/platform_api.py`; this file only does translation. That is what "thin" means.

GET vs POST (the rule of thumb used below)
------------------------------------------
* GET  = "read something." No body; inputs ride in the URL as ?query=params.
         Safe to repeat — calling it twice changes nothing.
* POST = "do/create/change something." Inputs travel in a JSON request *body*.
         Calling it twice may create/modify data, so it's not a pure read.
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import your existing backend UNCHANGED. Because we run uvicorn from the project
# root, Python can find the `src` package, exactly like the Streamlit app does.
from src import platform_api as api

# ---------------------------------------------------------------------------
# The FastAPI application object. `app` IS the web application: you attach
# endpoints to it with decorators like @app.get(...) / @app.post(...).
# ---------------------------------------------------------------------------
app = FastAPI(title="EcoLearn API", version="0.1.0")

# ---------------------------------------------------------------------------
# CORS — let your Next.js dev server (a different origin) call this API.
# A browser blocks JS on http://localhost:3000 from calling http://localhost:8000
# unless the API explicitly allows it. (Tighten this to your real domain later.)
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # the Next.js dev server
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===========================================================================
# Request body models (POST endpoints only).
#
# A Pydantic model describes the JSON shape we expect. FastAPI validates the
# incoming body against it BEFORE your handler runs: missing/wrong-typed fields
# get an automatic, descriptive 422 error, so your code only ever sees clean
# data. (GET endpoints don't use these — their inputs come from the URL.)
# ===========================================================================
class StudentRequest(BaseModel):
    """Body for POST /api/student."""

    name: str
    interest: str
    level: str = "Class 11"  # sensible default if the caller omits it


class AssessmentRequest(BaseModel):
    """Body for POST /api/assessment."""

    student_id: str
    concept_id: str
    answer: str


class HelpRequest(BaseModel):
    """Body for POST /api/help."""

    student_id: str
    concept_id: str
    question: str


# ===========================================================================
# Endpoints
# ===========================================================================
@app.get("/")
def root() -> dict:
    """Health check — confirms the server is alive."""
    return {"status": "ok", "service": "EcoLearn API"}


@app.post("/api/student")
def create_student(payload: StudentRequest) -> dict:
    """Create a student (or load an existing one) and return their profile.

    POST because it creates/updates data. Wraps `create_or_load_student`.
    """
    return api.create_or_load_student(
        name=payload.name,
        interest=payload.interest,
        level=payload.level,
    )


@app.get("/api/roadmap")
def get_roadmap(student_id: str, chapter_id: str) -> list[dict]:
    """Return every concept in a chapter tagged mastered / available / locked.

    GET because it only reads. `student_id` and `chapter_id` are query params,
    e.g. /api/roadmap?student_id=ada&chapter_id=motion_straight_line.
    Wraps `get_roadmap`.
    """
    return api.get_roadmap(student_id=student_id, chapter_id=chapter_id)


@app.get("/api/next-lesson")
def get_next_lesson(
    student_id: str,
    chapter_id: str,
    concept_id: str | None = None,
) -> dict:
    """Return the personalised lesson for the student's next concept.

    GET because it only reads. `concept_id` is optional — pass it to re-serve a
    specific concept (e.g. "practise this again") instead of the engine's pick.
    Wraps `get_next_lesson`.
    """
    return api.get_next_lesson(
        student_id=student_id,
        chapter_id=chapter_id,
        concept_id=concept_id,
    )


@app.post("/api/assessment")
def submit_assessment(payload: AssessmentRequest) -> dict:
    """Grade a student's answer to a concept's self-check and update mastery.

    POST because submitting an answer changes stored mastery. Wraps
    `submit_assessment`.
    """
    return api.submit_assessment(
        student_id=payload.student_id,
        concept_id=payload.concept_id,
        answer=payload.answer,
    )


@app.post("/api/help")
def ask_help(payload: HelpRequest) -> dict:
    """Answer a free-form question via the live (expensive) tutor pipeline.

    POST because it sends a question payload and triggers real LLM work. Wraps
    `ask_help`.
    """
    return api.ask_help(
        student_id=payload.student_id,
        concept_id=payload.concept_id,
        question=payload.question,
    )
