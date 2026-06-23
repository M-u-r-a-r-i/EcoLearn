"""EcoLearn HTTP API — a thin FastAPI layer over src/platform_api.py.

WHAT THIS FILE IS
-----------------
This is the "web front door" to your existing Python backend. Your Next.js site
(running in the browser) cannot import Python functions directly — browsers speak
HTTP. So we put a small web server in front of `platform_api` that:

    receives an HTTP request  ->  calls your existing function  ->  returns JSON

We do NOT change any business logic here. Every real decision still lives in
`src/platform_api.py`; this file only does translation. That is what "thin" means.
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import your existing backend UNCHANGED. Because we run uvicorn from the project
# root, Python can find the `src` package, exactly like the Streamlit app does.
from src import platform_api as api

# ---------------------------------------------------------------------------
# 1. Create the FastAPI application object.
#
#    `app` is the whole web application. FastAPI is a Python library for building
#    web APIs: you write normal Python functions and "decorate" them so FastAPI
#    turns them into web endpoints. The title/version below just show up on the
#    auto-generated docs page.
# ---------------------------------------------------------------------------
app = FastAPI(title="EcoLearn API", version="0.1.0")

# ---------------------------------------------------------------------------
# 2. CORS — let your Next.js site (a different origin) call this API.
#
#    A browser blocks JavaScript on http://localhost:3000 (Next.js dev server)
#    from calling an API on http://localhost:8000 unless the API explicitly
#    allows it. This middleware grants that permission for local development.
#    (You'll tighten `allow_origins` to your real domain before deploying.)
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # the Next.js dev server
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# 3. Describe the shape of the request body.
#
#    When the browser POSTs JSON like {"name": "...", "interest": "...",
#    "level": "..."}, FastAPI validates it against this Pydantic model before
#    your code runs. If a field is missing or the wrong type, the caller gets a
#    clear 422 error automatically — you never see bad data.
# ---------------------------------------------------------------------------
class StudentRequest(BaseModel):
    name: str
    interest: str
    level: str = "Class 11"  # a sensible default if the caller omits it


# ---------------------------------------------------------------------------
# 4. A tiny health-check endpoint (handy to confirm the server is alive).
#    GET http://localhost:8000/  ->  {"status": "ok", ...}
# ---------------------------------------------------------------------------
@app.get("/")
def root() -> dict:
    return {"status": "ok", "service": "EcoLearn API"}


# ---------------------------------------------------------------------------
# 5. THE endpoint for today.
#
#    `@app.post("/api/student")` registers the function below as the handler for
#    HTTP POST requests to the path /api/student. An "endpoint" is just that
#    pairing: (HTTP method + URL path) -> a function that runs.
#
#    FastAPI gives us the parsed, validated body as `payload` (a StudentRequest).
#    We call your existing function and return its dict; FastAPI serializes it
#    to a JSON HTTP response for us.
# ---------------------------------------------------------------------------
@app.post("/api/student")
def create_student(payload: StudentRequest) -> dict:
    profile = api.create_or_load_student(
        name=payload.name,
        interest=payload.interest,
        level=payload.level,
    )
    return profile
