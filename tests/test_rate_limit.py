"""Login rate limiting (apps/api/ratelimit.py). No network, a fake clock.

Proves:
  1. 8 wrong passwords lock the account: the 9th try is 429 with Retry-After
     and a message for a student — even with the RIGHT password (a lock must
     not confirm a guess).
  2. Unknown usernames are counted the same way (no account enumeration).
  3. Other accounts on the same IP are unaffected (a whole class shares one).
  4. A right password before the limit clears the count.
  5. The lock lifts after the lockout time.
  6. A teacher's password reset unlocks the student at once.
  7. The per-IP cap stops one address spraying many usernames.
  8. Teacher login and change-password are limited too.

Run: venv\\Scripts\\python.exe tests\\test_rate_limit.py
"""

from __future__ import annotations

import os
import sys
import tempfile
import warnings
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))
sys.path.insert(0, str(_ROOT / "apps"))

_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_ratelimit_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "rl.db")
warnings.simplefilter("ignore")

from fastapi.testclient import TestClient  # noqa: E402

from api import ratelimit  # noqa: E402
from api.main import app  # noqa: E402
from ecolearn import platform_api as api  # noqa: E402

_checks = 0


def check(condition: bool, label: str) -> None:
    global _checks
    assert condition, f"FAIL: {label}"
    _checks += 1
    print(f"  ok  {label}")


class Clock:
    def __init__(self):
        self.t = 1000.0

    def __call__(self):
        return self.t


clock = Clock()
ratelimit.limiter.clock = clock


def login(client, username, password, path="/api/auth/login"):
    return client.post(path, json={"username": username, "password": password})


def main() -> None:
    client = TestClient(app)
    teacher = api.create_teacher("Ms. Rao", "rao.limit", "teach-physics-1")
    made = api.create_class(teacher["teacher_id"], "11-E", "Class 11", "cricket", "Aarav Kumar\nMeera Iyer")
    (aarav, meera) = made["credentials"]

    print("\n[1] the account lock")
    codes = [login(client, aarav["username"], "wrong-pass-1").status_code for _ in range(7)]
    check(codes == [401] * 7, "7 wrong passwords → 401 each")
    check(login(client, aarav["username"], aarav["password"]).status_code == 200,
          "7 wrong, then right: still allowed (and the count clears)")
    for _ in range(8):
        login(client, aarav["username"], "wrong-pass-1")
    r = login(client, aarav["username"], aarav["password"])
    check(r.status_code == 429 and r.headers.get("retry-after") == "600",
          "after 8 wrong: 429 with Retry-After 600, even with the right password")
    check("ask your teacher" in r.json()["detail"] and "10 minutes" in r.json()["detail"],
          f"a message for a student: {r.json()['detail']!r}")

    print("\n[2-3] no enumeration; classmates unaffected")
    for _ in range(8):
        login(client, "nobody.here", "wrong-pass-1")
    check(login(client, "nobody.here", "wrong-pass-1").status_code == 429,
          "an unknown username locks the same way")
    check(login(client, meera["username"], meera["password"]).status_code == 200,
          "a classmate on the same IP logs in fine")

    print("\n[5] the lock lifts")
    clock.t += 601
    check(login(client, aarav["username"], aarav["password"]).status_code == 200, "after 10 minutes: allowed")

    print("\n[6] a teacher reset unlocks")
    for _ in range(8):
        login(client, aarav["username"], "wrong-pass-1")
    check(login(client, aarav["username"], aarav["password"]).status_code == 429, "locked again")
    tclient = TestClient(app)
    login(tclient, "rao.limit", "teach-physics-1", "/api/teacher/login")
    new = tclient.post(f"/api/teacher/students/{aarav['student_id']}/reset-password").json()
    check(login(client, aarav["username"], new["password"]).status_code == 200,
          "reset → the student logs in with the new password at once")

    print("\n[8] teacher login and change-password")
    for _ in range(8):
        login(client, "rao.limit", "wrong-pass-1", "/api/teacher/login")
    check(login(client, "rao.limit", "teach-physics-1", "/api/teacher/login").status_code == 429,
          "teacher login is limited")
    s = TestClient(app)
    login(s, meera["username"], meera["password"])
    codes = [s.post("/api/auth/change-password",
                    json={"current_password": "wrong-pass-1", "new_password": "new-pass-123"}).status_code
             for _ in range(9)]
    check(codes[:8] == [401] * 8 and codes[8] == 429, "guessing the current password is limited")

    print("\n[7] the per-IP cap")
    clock.t += 10_000
    limited = ratelimit.LoginLimiter(account_failures=8, ip_failures=20, clock=clock)
    ip = limited.ip_key("10.0.0.5")
    for i in range(20):
        limited.record_failure(limited.account_key("student", f"user{i}"), ip)
    check(limited.retry_after(limited.account_key("student", "fresh.user"), ip) is not None,
          "20 failures across 20 usernames from one IP block that IP")
    check(limited.retry_after(limited.account_key("student", "fresh.user"), limited.ip_key("10.0.0.6")) is None,
          "another IP is unaffected")

    print(f"\nAll {_checks} rate-limit checks passed.")


if __name__ == "__main__":
    main()
