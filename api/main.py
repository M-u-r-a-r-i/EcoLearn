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

import json
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Import your existing backend UNCHANGED. Because we run uvicorn from the project
# root, Python can find the `src` package, exactly like the Streamlit app does.
from src import platform_api as api
from src.errors import AuthError, ConflictError, EcoLearnError, NotFoundError

from api.ratelimit import limiter, too_many_message
from api.security import (
    clear_session_cookie,
    get_current_account,
    get_current_student_id,
    get_current_teacher_id,
    set_session_cookie,
)

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
    # The Next.js dev server, by either loopback name: localhost and 127.0.0.1
    # are different origins to a browser, and people open both.
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
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
    """Body for POST /api/assessment. The student comes from the session cookie.
    `confidence`: sure | think | guess ("how sure are you?"), optional."""

    concept_id: str
    answer: str
    confidence: str | None = None


class HelpRequest(BaseModel):
    """Body for POST /api/help. The student comes from the session cookie."""

    concept_id: str
    question: str


class LessonViewRequest(BaseModel):
    """Body for POST /api/lesson-views."""

    concept_id: str


class RatingRequest(BaseModel):
    """Body for POST /api/lesson-ratings: 1 = 👍, -1 = 👎, 0 = clear."""

    concept_id: str
    rating: int


class DiagnosticRequest(BaseModel):
    """Body for POST /api/diagnostic: {concept_id: "A".."D" or "unsure"} + hobbies."""

    answers: dict[str, str]
    hobbies: list[str] = []
    confidence: dict[str, str] = {}  # concept_id -> sure | think | guess


class EndCheckRequest(BaseModel):
    """Body for POST /api/end-check: {concept_id: "A".."D" or "unsure"}."""

    answers: dict[str, str]
    confidence: dict[str, str] = {}  # concept_id -> sure | think | guess


class RevisionRequest(BaseModel):
    """Body for POST /api/revision: a revision question's pick (+ how sure)."""

    concept_id: str
    answer: str
    confidence: str | None = None


class EndCheckOpenRequest(BaseModel):
    """Body for POST /api/teacher/classes/{id}/end-check: open or close it."""

    open: bool


class StoryReportRequest(BaseModel):
    """Body for POST /api/personal-story/report. `reason` is one of
    wrong_physics | confusing | not_appropriate | other (no free text)."""

    concept_id: str
    reason: str


class StoryVisibilityRequest(BaseModel):
    """Body for POST /api/teacher/stories/{student_id}/{concept_id}/visibility."""

    hidden: bool


class CreateClassRequest(BaseModel):
    """Body for POST /api/teacher/classes. `roster`: one student name per line,
    optionally "Name, interest"."""

    name: str
    level: str = "Class 11"
    interest: str
    roster: str


class AddStudentsRequest(BaseModel):
    """Body for POST /api/teacher/classes/{class_id}/students."""

    interest: str
    roster: str


# ===========================================================================
# Password guessing protection (see api/ratelimit.py for the design)
# ===========================================================================
def _client_ip(request: Request) -> str | None:
    return request.client.host if request.client else None


def _check_password_attempt(account_key: str, request: Request, attempt):
    """Run a password check under the rate limiter.

    Locked → 429 with Retry-After, without even checking the password (so a
    lock can't be used to confirm a guess). A wrong password counts against
    the account and the IP; a right one clears the account's count.
    """
    ip_key = limiter.ip_key(_client_ip(request))
    wait = limiter.retry_after(account_key, ip_key)
    if wait:
        raise HTTPException(status.HTTP_429_TOO_MANY_REQUESTS, too_many_message(wait),
                            headers={"Retry-After": str(wait)})
    try:
        result = attempt()
    except AuthError:
        limiter.record_failure(account_key, ip_key)
        raise
    limiter.clear(account_key)
    return result


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
def login(payload: LoginRequest, request: Request, response: Response) -> dict:
    """Check credentials, set the session cookie, return the profile.

    401 with one generic message for any failure, so the response never reveals
    whether a username exists. 429 after too many wrong passwords.
    """
    profile = _check_password_attempt(
        limiter.account_key("student", payload.username), request,
        lambda: api.authenticate_student(payload.username, payload.password))
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


@app.get("/api/auth/session")
def session(account: tuple[str, dict] = Depends(get_current_account)) -> dict:
    """Who is logged in, and as what: {"role": "student"|"teacher", "profile": {...}}.

    The web app calls this once on load to decide which home to show. 401 when
    nobody is logged in. (/api/auth/me stays as it was, for students only.)
    """
    role, profile = account
    return {"role": role, "profile": profile}


@app.post("/api/auth/change-password")
def change_password(
    payload: ChangePasswordRequest,
    request: Request,
    student_id: str = Depends(get_current_student_id),
) -> dict:
    """Change the password; requires the current one (401 if it's wrong, 429
    after too many wrong tries — someone at an unlocked screen could guess)."""
    return _check_password_attempt(
        f"change:{student_id}", request,
        lambda: api.change_password(student_id, payload.current_password, payload.new_password))


@app.patch("/api/profile")
def update_profile(
    payload: ProfilePatch,
    student_id: str = Depends(get_current_student_id),
) -> dict:
    """Change name / interest. Only the fields sent are changed.

    The class level is NOT the student's to change (2026-10-03): a teacher sets
    it (POST /api/teacher/students/{id}/level). Re-sending the current level is
    harmless, so older clients that send the whole form still work.
    """
    if payload.level is not None:
        current = (api.get_student_profile(student_id) or {}).get("level")
        if payload.level.strip() != current:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only your teacher can change your class.",
            )
    return api.update_student_profile(
        student_id, name=payload.name, interest=payload.interest, level=None
    )


# ---------------------------------------------------------------------------
# Teachers. Teacher accounts are made on the server (scripts/create_teacher.py),
# never over HTTP. Every endpoint below needs a teacher's session; a student's
# session gets 401. Responses that carry freshly generated passwords are marked
# no-store, so no browser or proxy cache keeps a copy.
# ---------------------------------------------------------------------------
def _no_store(response: Response) -> None:
    response.headers["Cache-Control"] = "no-store"


@app.post("/api/teacher/login")
def teacher_login(payload: LoginRequest, request: Request, response: Response) -> dict:
    """Teacher login. Same generic 401 and the same rate limit as students."""
    profile = _check_password_attempt(
        limiter.account_key("teacher", payload.username), request,
        lambda: api.authenticate_teacher(payload.username, payload.password))
    set_session_cookie(response, profile["teacher_id"])
    return profile


@app.get("/api/teacher/me")
def teacher_me(teacher_id: str = Depends(get_current_teacher_id)) -> dict:
    return api.get_teacher_profile(teacher_id)


@app.post("/api/teacher/change-password")
def teacher_change_password(
    payload: ChangePasswordRequest,
    request: Request,
    teacher_id: str = Depends(get_current_teacher_id),
) -> dict:
    return _check_password_attempt(
        f"change:{teacher_id}", request,
        lambda: api.change_teacher_password(teacher_id, payload.current_password,
                                            payload.new_password))


@app.get("/api/teacher/classes")
def teacher_classes(teacher_id: str = Depends(get_current_teacher_id)) -> list[dict]:
    return api.list_teacher_classes(teacher_id)


@app.post("/api/teacher/classes", status_code=status.HTTP_201_CREATED)
def teacher_create_class(
    payload: CreateClassRequest,
    response: Response,
    teacher_id: str = Depends(get_current_teacher_id),
) -> dict:
    """Create a class from a roster. The response holds every new student's
    password — the only time they exist in plaintext."""
    _no_store(response)
    return api.create_class(
        teacher_id, payload.name, payload.level, payload.interest, payload.roster
    )


@app.get("/api/teacher/classes/{class_id}")
def teacher_class_detail(
    class_id: str, teacher_id: str = Depends(get_current_teacher_id)
) -> dict:
    return api.get_class_detail(teacher_id, class_id)


@app.post("/api/teacher/classes/{class_id}/students", status_code=status.HTTP_201_CREATED)
def teacher_add_students(
    class_id: str,
    payload: AddStudentsRequest,
    response: Response,
    teacher_id: str = Depends(get_current_teacher_id),
) -> dict:
    """Add latecomers to an existing class; same response shape as creating one."""
    _no_store(response)
    return api.add_students_to_class(teacher_id, class_id, payload.roster, payload.interest)


@app.get("/api/teacher/classes/{class_id}/insights")
def teacher_class_insights(
    class_id: str, teacher_id: str = Depends(get_current_teacher_id)
) -> dict:
    """Pilot metrics and the misconception view for one of this teacher's classes."""
    return api.get_class_insights(teacher_id, class_id)


@app.get("/api/teacher/classes/{class_id}/checks")
def teacher_class_checks(
    class_id: str, teacher_id: str = Depends(get_current_teacher_id)
) -> dict:
    """The class's starting check -> end check: before and after, per student and concept."""
    return api.get_class_checks(teacher_id, class_id)


@app.post("/api/teacher/classes/{class_id}/end-check")
def teacher_set_end_check(
    class_id: str,
    payload: EndCheckOpenRequest,
    teacher_id: str = Depends(get_current_teacher_id),
) -> dict:
    """Open the end check for the class (or close it again)."""
    return api.set_class_end_check(teacher_id, class_id, payload.open)


@app.get("/api/teacher/classes/{class_id}/plan")
def teacher_class_plan(
    class_id: str, teacher_id: str = Depends(get_current_teacher_id)
) -> dict | None:
    """The teacher assistant's latest plan for this class, or null if none yet."""
    return api.get_class_plan(teacher_id, class_id)


@app.post("/api/teacher/classes/{class_id}/plan")
def teacher_generate_plan(
    class_id: str, teacher_id: str = Depends(get_current_teacher_id)
) -> dict:
    """Ask the teacher assistant for a new plan (takes seconds: a live model call,
    or the rules-based fallback when no model is available)."""
    return api.generate_class_plan(teacher_id, class_id)


@app.get("/api/teacher/classes/{class_id}/stories")
def teacher_class_stories(
    class_id: str, teacher_id: str = Depends(get_current_teacher_id)
) -> dict:
    """Every AI-written personal story in this class, reported ones first."""
    return api.list_class_stories(teacher_id, class_id)


@app.get("/api/teacher/classes/{class_id}/ai-decisions")
def teacher_ai_decisions(
    class_id: str, teacher_id: str = Depends(get_current_teacher_id)
) -> dict:
    """How the AI decided: guardrail counts and each personal story's step-by-step record."""
    return api.get_class_ai_decisions(teacher_id, class_id)


@app.post("/api/teacher/stories/{student_id}/{concept_id}/visibility")
def teacher_story_visibility(
    student_id: str,
    concept_id: str,
    payload: StoryVisibilityRequest,
    teacher_id: str = Depends(get_current_teacher_id),
) -> dict:
    """Hide a story from the student (they see the reviewed one), or show it again."""
    return api.set_class_story_hidden(teacher_id, student_id, concept_id, payload.hidden)


@app.post("/api/teacher/students/{student_id}/reset-password")
def teacher_reset_password(
    student_id: str,
    response: Response,
    teacher_id: str = Depends(get_current_teacher_id),
) -> dict:
    """Give a student in one of this teacher's classes a new password."""
    _no_store(response)
    result = api.reset_student_password(teacher_id, student_id)
    # A student locked out by wrong passwords can log in with the new one now.
    limiter.clear(limiter.account_key("student", result["username"] or ""))
    return result


class LevelPatch(BaseModel):
    level: str


@app.post("/api/teacher/students/{student_id}/level")
def teacher_set_level(
    student_id: str,
    payload: LevelPatch,
    teacher_id: str = Depends(get_current_teacher_id),
) -> dict:
    """Move a student in one of this teacher's classes to Class 11 or Class 12."""
    return api.set_student_level(teacher_id, student_id, payload.level)


# ---------------------------------------------------------------------------
# Curriculum. Public on purpose: the syllabus and the interest list aren't
# secrets, and the signup page needs the interests before anyone has logged in.
# ---------------------------------------------------------------------------
@app.get("/api/chapters")
def chapters(interest: str | None = None) -> list[dict]:
    """Every chapter in teaching order, with unit and class for grouping.

    ?interest=cricket adds `lessons_ready` per chapter (400 for an unknown interest).
    """
    return api.list_chapters(interest)


@app.get("/api/interests")
def interests() -> list[dict]:
    """The interests a student can pick right now (active ones only)."""
    return api.list_interests(active_only=True)


# ---------------------------------------------------------------------------
# Learning. Every endpoint below needs a logged-in student: `Depends` reads the
# session cookie and answers 401 before the handler runs if it is missing or
# invalid. The student id is never taken from the request itself, so nobody can
# read or change another student's progress by sending a different id.
# (Streamlit is unaffected: it calls src/platform_api.py directly, not HTTP.)
# ---------------------------------------------------------------------------
@app.get("/api/roadmap")
def get_roadmap(
    chapter_id: str,
    student_id: str = Depends(get_current_student_id),
) -> list[dict]:
    """Return every concept in a chapter tagged mastered / available (nothing is locked).

    GET because it only reads, e.g. /api/roadmap?chapter_id=motion_straight_line.
    Wraps `get_roadmap`.
    """
    return api.get_roadmap(student_id=student_id, chapter_id=chapter_id)


@app.get("/api/next-lesson")
def get_next_lesson(
    chapter_id: str,
    concept_id: str | None = None,
    student_id: str = Depends(get_current_student_id),
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
def submit_assessment(
    payload: AssessmentRequest,
    student_id: str = Depends(get_current_student_id),
) -> dict:
    """Grade a student's answer to a concept's self-check and update mastery.

    POST because submitting an answer changes stored mastery. Wraps
    `submit_assessment`.
    """
    return api.submit_assessment(
        student_id=student_id,
        concept_id=payload.concept_id,
        answer=payload.answer,
        confidence=payload.confidence,
    )


# ---------------------------------------------------------------------------
# The starting check and the learning plan (personalisation, layers 1 and 2).
# ---------------------------------------------------------------------------
@app.get("/api/diagnostic")
def get_diagnostic(student_id: str = Depends(get_current_student_id)) -> dict:
    """The starting check: its questions (no answers), or the result once taken."""
    return api.get_diagnostic(student_id)


@app.post("/api/diagnostic")
def submit_diagnostic(
    payload: DiagnosticRequest,
    student_id: str = Depends(get_current_student_id),
) -> dict:
    """Grade the starting check (once; 409 if already taken) and return the plan."""
    return api.submit_diagnostic(student_id, payload.answers, payload.hobbies, payload.confidence)


@app.get("/api/revision")
def revision(student_id: str = Depends(get_current_student_id)) -> dict:
    """Concepts answered right once: a fresh question on each, due or later."""
    return api.get_revision(student_id)


@app.get("/api/revision/question")
def revision_question(concept_id: str, student_id: str = Depends(get_current_student_id)) -> dict:
    """The fresh question for one concept in the revision list (no answer key)."""
    return api.get_revision_question(student_id, concept_id)


@app.post("/api/revision")
def submit_revision(
    payload: RevisionRequest, student_id: str = Depends(get_current_student_id)
) -> dict:
    """Grade a revision answer; two different questions right = mastered."""
    return api.submit_revision(student_id, payload.concept_id, payload.answer, payload.confidence)


@app.get("/api/mix-ups")
def mix_ups(student_id: str = Depends(get_current_student_id)) -> dict:
    """Every misconception you've shown, and whether it's fixed."""
    return api.get_mix_ups(student_id)


@app.get("/api/end-check")
def get_end_check(student_id: str = Depends(get_current_student_id)) -> dict:
    """The end check: not open yet, its questions (no answers), or before -> after."""
    return api.get_end_check(student_id)


@app.post("/api/end-check")
def submit_end_check(
    payload: EndCheckRequest,
    student_id: str = Depends(get_current_student_id),
) -> dict:
    """Grade the end check (once; 409 if already taken, 400 if not open)."""
    return api.submit_end_check(student_id, payload.answers, payload.confidence)


@app.get("/api/personal-story")
def personal_story(
    concept_id: str, student_id: str = Depends(get_current_student_id)
) -> dict:
    """The story written for this student's hobby: ready, pending (poll), or none."""
    return api.get_personal_story(student_id, concept_id)


@app.post("/api/personal-story/report")
def report_personal_story(
    payload: StoryReportRequest, student_id: str = Depends(get_current_student_id)
) -> dict:
    """Report the story written for you: it's hidden at once and your teacher sees it."""
    return api.report_personal_story(student_id, payload.concept_id, payload.reason)


@app.get("/api/learning-plan")
def learning_plan(student_id: str = Depends(get_current_student_id)) -> dict:
    """What to focus on and where to start, from the starting check and lessons."""
    return api.get_learning_plan(student_id)


# ---------------------------------------------------------------------------
# Pilot metrics: lesson opens, reading time, 👍/👎. (Answers are logged by
# /api/assessment.) All tied to the session's student, like everything above.
# ---------------------------------------------------------------------------
@app.post("/api/lesson-views", status_code=status.HTTP_201_CREATED)
def start_lesson_view(
    payload: LessonViewRequest,
    student_id: str = Depends(get_current_student_id),
) -> dict:
    """The student opened a lesson. Returns a view id to report reading time against."""
    return api.start_lesson_view(student_id, payload.concept_id)


@app.post("/api/lesson-views/{view_id}/time")
async def record_lesson_time(
    view_id: str,
    request: Request,
    student_id: str = Depends(get_current_student_id),
) -> dict:
    """Report the running total of active seconds on a lesson view.

    The body is JSON, {"active_seconds": 42}, but deliberately accepted with any
    content type: the browser sends it with `fetch(..., {keepalive: true})` as
    text/plain while the page is closing, and text/plain is the only way to do a
    cross-origin request without a CORS preflight, which a closing page has no
    time for.
    """
    try:
        body = json.loads(await request.body() or b"{}")
        seconds = body["active_seconds"]
    except (ValueError, KeyError, TypeError):
        raise EcoLearnError('Send {"active_seconds": <number>}.') from None
    return api.record_lesson_time(student_id, view_id, seconds)


@app.post("/api/lesson-ratings")
def rate_lesson(
    payload: RatingRequest,
    student_id: str = Depends(get_current_student_id),
) -> dict:
    """👍 (1) / 👎 (-1) for the lesson in the student's interest; 0 clears it."""
    return api.rate_lesson(student_id, payload.concept_id, payload.rating)


@app.post("/api/help")
def ask_help(
    payload: HelpRequest,
    student_id: str = Depends(get_current_student_id),
) -> dict:
    """Answer a free-form question via the live (expensive) tutor pipeline.

    POST because it sends a question payload and triggers real LLM work. Wraps
    `ask_help`.
    """
    return api.ask_help(
        student_id=student_id,
        concept_id=payload.concept_id,
        question=payload.question,
    )
