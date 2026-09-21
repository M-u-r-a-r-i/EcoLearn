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

from pathlib import Path

from fastapi import Depends, FastAPI, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Import your existing backend UNCHANGED. Because we run uvicorn from the project
# root, Python can find the `src` package, exactly like the Streamlit app does.
from src import platform_api as api
from src.errors import AuthError, ConflictError, EcoLearnError, NotFoundError

from api.security import clear_session_cookie, get_current_student_id, set_session_cookie

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
    # Credentials = cookies. Needed so the browser sends the session cookie to
    # this API. Browsers refuse credentials with allow_origins=["*"], so the
    # allowed origins must always be listed explicitly.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Errors → HTTP status codes. The boundary raises typed errors; this is the one
# place that decides what each means over HTTP, so every endpoint answers
# consistently with {"detail": "..."} instead of a bare 500.
# Starlette picks the most specific registered class, so NotFoundError (a
# subclass of EcoLearnError, itself a ValueError) gets 404, not 400.
# ---------------------------------------------------------------------------
def _error(code: int):
    async def handler(_: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(status_code=code, content={"detail": str(exc)})
    return handler


app.add_exception_handler(NotFoundError, _error(status.HTTP_404_NOT_FOUND))
app.add_exception_handler(ConflictError, _error(status.HTTP_409_CONFLICT))
app.add_exception_handler(AuthError, _error(status.HTTP_401_UNAUTHORIZED))
app.add_exception_handler(EcoLearnError, _error(status.HTTP_400_BAD_REQUEST))
app.add_exception_handler(ValueError, _error(status.HTTP_400_BAD_REQUEST))
# A live-LLM failure (e.g. the grader is out of quota) raises RuntimeError with a
# student-ready message; that is "try again later", not "your request was wrong".
app.add_exception_handler(RuntimeError, _error(status.HTTP_503_SERVICE_UNAVAILABLE))

# ---------------------------------------------------------------------------
# Lesson images — graphs, diagrams, scene illustrations and famous images —
# served as static files from data/media/. Lessons reference them by relative
# path (e.g. "figures/ohms_law/vi-ohmic-vs-lamp.svg"); the web app prefixes
# this route. Every file is checked by scripts/validate_lessons.py first
# (SVGs are rejected if they contain scripts, handlers or external links).
# ---------------------------------------------------------------------------
_MEDIA_DIR = Path(__file__).resolve().parents[1] / "data" / "media"
app.mount("/media", StaticFiles(directory=_MEDIA_DIR), name="media")


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


class RegisterRequest(BaseModel):
    """Body for POST /api/auth/register."""

    name: str
    username: str
    password: str
    interest: str
    level: str = "Class 11"


class LoginRequest(BaseModel):
    """Body for POST /api/auth/login."""

    username: str
    password: str


class ChangePasswordRequest(BaseModel):
    """Body for POST /api/auth/change-password."""

    current_password: str
    new_password: str


class ProfilePatch(BaseModel):
    """Body for PATCH /api/profile — send only the fields to change."""

    name: str | None = None
    interest: str | None = None
    level: str | None = None


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


# ---------------------------------------------------------------------------
# Accounts. Register and login set the session cookie (see api/security.py);
# everything the student does afterwards is identified by that cookie.
# ---------------------------------------------------------------------------
@app.post("/api/auth/register", status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, response: Response) -> dict:
    """Create an account, log it in, and return its profile (201).

    400 for invalid input (username rules, unknown interest, short password),
    409 if the username is taken.
    """
    profile = api.register_student(
        name=payload.name,
        username=payload.username,
        password=payload.password,
        interest=payload.interest,
        level=payload.level,
    )
    set_session_cookie(response, profile["student_id"])
    return profile


@app.post("/api/auth/login")
def login(payload: LoginRequest, response: Response) -> dict:
    """Check credentials, set the session cookie, return the profile.

    401 with one generic message for any failure, so the response never reveals
    whether a username exists.
    """
    profile = api.authenticate_student(payload.username, payload.password)
    set_session_cookie(response, profile["student_id"])
    return profile


@app.post("/api/auth/logout")
def logout(response: Response) -> dict:
    """Clear the session cookie. Safe to call when already logged out."""
    clear_session_cookie(response)
    return {"logged_out": True}


@app.get("/api/auth/me")
def me(student_id: str = Depends(get_current_student_id)) -> dict:
    """Who am I? The browser can't read its httpOnly cookie, so the web app asks
    this on load: 200 with the profile, or 401 → show the login page."""
    return api.get_student_profile(student_id)


@app.post("/api/auth/change-password")
def change_password(
    payload: ChangePasswordRequest,
    student_id: str = Depends(get_current_student_id),
) -> dict:
    """Change the password; requires the current one (401 if it's wrong)."""
    return api.change_password(student_id, payload.current_password, payload.new_password)


@app.patch("/api/profile")
def update_profile(
    payload: ProfilePatch,
    student_id: str = Depends(get_current_student_id),
) -> dict:
    """Change name / interest / level. Only the fields sent are changed."""
    return api.update_student_profile(
        student_id, name=payload.name, interest=payload.interest, level=payload.level
    )


# ---------------------------------------------------------------------------
# Curriculum. Public on purpose: the syllabus and the interest list aren't
# secrets, and the signup page needs the interests before anyone has logged in.
# ---------------------------------------------------------------------------
@app.get("/api/chapters")
def chapters() -> list[dict]:
    """Every chapter in teaching order, with unit and class for grouping."""
    return api.list_chapters()


@app.get("/api/interests")
def interests() -> list[dict]:
    """The interests a student can pick right now (active ones only)."""
    return api.list_interests(active_only=True)


# ---------------------------------------------------------------------------
# Learning. These still take student_id explicitly so the current web app and
# its tests keep working. The planned "breaking flip" (ROADMAP §5) will switch
# them to Depends(get_current_student_id) in one commit, together with the web
# client — until then they are unauthenticated, as before.
# ---------------------------------------------------------------------------
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
    """Return every concept in a chapter tagged mastered / available (nothing is locked).

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
