"""HTTP-level auth test: sessions, cookies, status codes. No LLM calls.

Drives the real FastAPI app in-process (TestClient) against a throwaway DB and
proves the Milestone 0 acceptance criteria that live at the HTTP layer:

  1. Register → 201, sets an HttpOnly, SameSite=Lax session cookie; the body
     never contains the password hash.
  2. GET /api/auth/me → 200 with the cookie, 401 (not 500) without it.
  3. Login: right password → 200 + cookie; wrong password and unknown username
     → 401 with ONE identical message.
  4. Bad input → 400, duplicate username → 409, unknown chapter → 404.
  5. Tampered, expired, and deleted-account tokens → 401; Bearer header works.
  6. Profile PATCH and change-password need a session; logout clears it.
  7. Public curriculum endpoints: chapters carry unit/grade; interests are the
     active ones only.

Run: venv\\Scripts\\python.exe tests\\test_api_auth.py
"""

from __future__ import annotations

import os
import sys
import tempfile
import warnings
from datetime import datetime, timedelta, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

_TMP_DIR = Path(tempfile.mkdtemp(prefix="ecolearn_api_auth_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP_DIR / "api_auth.db")
warnings.simplefilter("ignore")  # the dev-secret warning and a TestClient deprecation notice

from fastapi.testclient import TestClient  # noqa: E402

from api import security  # noqa: E402
from api.main import app  # noqa: E402

_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


def new_client() -> TestClient:
    return TestClient(app)


ADA = {"name": "Ada", "username": "ada_k", "password": "hunter2hunter2",
       "interest": "football", "level": "Class 11"}


def test_register_and_me() -> str:
    print("\n[1-2] register, cookie, /me")
    c = new_client()
    r = c.post("/api/auth/register", json=ADA)
    check(r.status_code == 201, f"register → 201 (got {r.status_code})")
    body = r.json()
    check(body["username"] == "ada_k" and "password_hash" not in body, "profile returned, no hash")
    cookie = r.headers.get("set-cookie", "")
    check(security.COOKIE_NAME in cookie, "session cookie set")
    check("httponly" in cookie.lower(), "cookie is HttpOnly")
    check("samesite=lax" in cookie.lower(), "cookie is SameSite=Lax")
    check("secure" not in cookie.lower(), "cookie not Secure in development (plain http localhost)")

    me = c.get("/api/auth/me")
    check(me.status_code == 200 and me.json()["student_id"] == body["student_id"], "/me → 200 with cookie")
    anon = new_client().get("/api/auth/me")
    check(anon.status_code == 401, f"/me → 401 without cookie (got {anon.status_code})")
    check(anon.headers.get("www-authenticate") == "Bearer", "401 carries WWW-Authenticate")
    return body["student_id"]


def test_login() -> None:
    print("\n[3] login")
    c = new_client()
    ok = c.post("/api/auth/login", json={"username": "ADA_K", "password": "hunter2hunter2"})
    check(ok.status_code == 200 and security.COOKIE_NAME in ok.headers.get("set-cookie", ""),
          "right password → 200 + cookie (username case-insensitive)")
    wrong = new_client().post("/api/auth/login", json={"username": "ada_k", "password": "wrongwrongwrong"})
    unknown = new_client().post("/api/auth/login", json={"username": "nobody", "password": "hunter2hunter2"})
    check(wrong.status_code == 401 and unknown.status_code == 401, "wrong password / unknown user → 401")
    check(wrong.json()["detail"] == unknown.json()["detail"], "identical message (no username enumeration)")


def test_error_codes() -> None:
    print("\n[4] error mapping")
    c = new_client()
    dup = c.post("/api/auth/register", json={**ADA, "name": "Impostor"})
    check(dup.status_code == 409, f"duplicate username → 409 (got {dup.status_code})")
    bad = c.post("/api/auth/register", json={**ADA, "username": "a b"})
    check(bad.status_code == 400, f"invalid username → 400 (got {bad.status_code})")
    bad_interest = c.post("/api/auth/register", json={**ADA, "username": "newkid", "interest": "chess"})
    check(bad_interest.status_code == 400, "unknown interest → 400")
    missing = c.post("/api/auth/register", json={"username": "x"})
    check(missing.status_code == 422, "missing fields → 422 (FastAPI validation)")
    legacy = c.post("/api/student", json={"name": "Chapter Test", "interest": "football"}).json()
    nf = c.get("/api/roadmap", params={"student_id": legacy["student_id"], "chapter_id": "no_such_chapter"})
    check(nf.status_code == 404, f"unknown chapter → 404 (got {nf.status_code})")


def test_bad_tokens(student_id: str) -> None:
    print("\n[5] tokens")
    tampered = security.create_token(student_id)[:-2] + "xx"
    expired = security.create_token(student_id, now=datetime.now(tz=timezone.utc) - timedelta(days=8))
    ghost = security.create_token("stu_does_not_exist")
    for label, token in (("tampered", tampered), ("expired", expired), ("deleted account", ghost)):
        c = new_client()
        c.cookies.set(security.COOKIE_NAME, token)
        check(c.get("/api/auth/me").status_code == 401, f"{label} token → 401")
    good = security.create_token(student_id)
    bearer = new_client().get("/api/auth/me", headers={"Authorization": f"Bearer {good}"})
    check(bearer.status_code == 200, "Bearer header accepted")


def test_session_actions() -> None:
    print("\n[6] profile, password, logout")
    c = new_client()
    c.post("/api/auth/login", json={"username": "ada_k", "password": "hunter2hunter2"})
    patched = c.patch("/api/profile", json={"interest": "gaming"})
    check(patched.status_code == 200 and patched.json()["interest"] == "gaming", "PATCH /api/profile works")
    check(new_client().patch("/api/profile", json={"interest": "gaming"}).status_code == 401,
          "PATCH /api/profile without session → 401")
    wrong = c.post("/api/auth/change-password",
                   json={"current_password": "nope-nope-nope", "new_password": "brandnew12345"})
    check(wrong.status_code == 401, "change-password with wrong current → 401")
    changed = c.post("/api/auth/change-password",
                     json={"current_password": "hunter2hunter2", "new_password": "brandnew12345"})
    check(changed.status_code == 200, "change-password → 200")
    relog = new_client().post("/api/auth/login", json={"username": "ada_k", "password": "brandnew12345"})
    check(relog.status_code == 200, "new password logs in")

    out = c.post("/api/auth/logout")
    cookie = out.headers.get("set-cookie", "")
    check(out.status_code == 200 and security.COOKIE_NAME in cookie and "max-age=0" in cookie.lower(),
          "logout expires the cookie")
    check(c.get("/api/auth/me").status_code == 401, "after logout → 401")


def test_public_curriculum() -> None:
    print("\n[7] public curriculum endpoints")
    c = new_client()
    chapters = c.get("/api/chapters").json()
    check(len(chapters) == 29, f"29 chapters (got {len(chapters)})")
    first = chapters[0]
    check({"id", "name", "unit_id", "unit_name", "grade", "domain", "concept_count"} <= set(first),
          "chapters carry unit, grade, domain, concept_count")
    check(first["grade"] == 11 and chapters[-1]["grade"] == 12, "Class 11 first, Class 12 last")
    interests = c.get("/api/interests").json()
    check({i["id"] for i in interests} == {"football", "gaming"}, "only active interests offered")

    print("\n[8] CORS with credentials")
    pre = {"Access-Control-Request-Method": "POST", "Access-Control-Request-Headers": "content-type"}
    ok = c.options("/api/auth/login", headers={"Origin": "http://localhost:3000", **pre})
    check(ok.headers.get("access-control-allow-origin") == "http://localhost:3000"
          and ok.headers.get("access-control-allow-credentials") == "true",
          "the web app's origin may send cookies")
    evil = c.options("/api/auth/login", headers={"Origin": "https://evil.example", **pre})
    check(evil.headers.get("access-control-allow-origin") is None, "a foreign origin is refused")


def main() -> None:
    student_id = test_register_and_me()
    test_login()
    test_error_codes()
    test_bad_tokens(student_id)
    test_session_actions()
    test_public_curriculum()
    print(f"\nALL {_checks} CHECKS PASSED")


if __name__ == "__main__":
    main()
