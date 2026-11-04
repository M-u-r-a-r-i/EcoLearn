"""Login rate limiting: slows down password guessing without locking out a class.

THE CLASSROOM PROBLEM
A whole class logs in from one school network, so every student shares one IP
address. Limiting by IP alone would block thirty students typing their
passwords at once. So there are two limits:

* per ACCOUNT — 8 wrong passwords in 15 minutes locks that username for 10
  minutes. This is what stops someone guessing one student's password. A
  teacher's password reset clears it at once (api/main.py), so a student who
  got locked out isn't stuck.
* per IP — 100 wrong passwords in 15 minutes from one address blocks further
  attempts from it for 10 minutes. High enough for a class full of typos;
  low enough to stop a script trying one password across many usernames.

Unknown usernames count exactly like known ones, so the limiter never reveals
whether an account exists. A successful login clears that account's count.

LIMITS OF THIS DESIGN (written down so nobody mistakes it for more)
* In-memory and per-process: restarting the API forgets all counts, and
  running several API workers would give each its own counts. Fine for one
  local server; a shared store (e.g. Redis) is needed beyond that.
* Behind a reverse proxy, every request would come from the proxy's IP;
  read the client IP from the proxy's header then (not done: local first).
* A classmate who knows a username can lock it for 10 minutes by typing wrong
  passwords. That is the price of any per-account lock; the short lockout and
  the teacher reset keep it small.

Limits can be tuned with ECOLEARN_LOGIN_* environment variables (see below).
"""

from __future__ import annotations

import math
import os
import threading
import time
from collections import defaultdict, deque


def _env_int(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, "") or default)
    except ValueError:
        return default


class LoginLimiter:
    def __init__(
        self,
        account_failures: int | None = None,
        ip_failures: int | None = None,
        window_seconds: int | None = None,
        lockout_seconds: int | None = None,
        clock=time.monotonic,
    ):
        self.account_failures = account_failures or _env_int("ECOLEARN_LOGIN_ACCOUNT_FAILURES", 8)
        self.ip_failures = ip_failures or _env_int("ECOLEARN_LOGIN_IP_FAILURES", 100)
        self.window = window_seconds or _env_int("ECOLEARN_LOGIN_WINDOW_SECONDS", 15 * 60)
        self.lockout = lockout_seconds or _env_int("ECOLEARN_LOGIN_LOCKOUT_SECONDS", 10 * 60)
        self.clock = clock
        self._failures: dict[str, deque[float]] = defaultdict(deque)
        self._locked_until: dict[str, float] = {}
        self._lock = threading.Lock()

    @staticmethod
    def account_key(kind: str, username: str) -> str:
        return f"{kind}:{(username or '').strip().lower()}"

    @staticmethod
    def ip_key(ip: str | None) -> str:
        return f"ip:{ip or 'unknown'}"

    def retry_after(self, *keys: str) -> int | None:
        """Seconds until these keys may try again, or None if they may now."""
        now = self.clock()
        with self._lock:
            waits = [self._locked_until[k] - now for k in keys
                     if self._locked_until.get(k, 0) > now]
        return math.ceil(max(waits)) if waits else None

    def record_failure(self, account: str, ip: str) -> None:
        now = self.clock()
        with self._lock:
            for key, limit in ((account, self.account_failures), (ip, self.ip_failures)):
                q = self._failures[key]
                q.append(now)
                while q and q[0] <= now - self.window:
                    q.popleft()
                if len(q) >= limit:
                    self._locked_until[key] = now + self.lockout
                    q.clear()

    def clear(self, key: str) -> None:
        """Forget an account's failures and lock (successful login, teacher reset)."""
        with self._lock:
            self._failures.pop(key, None)
            self._locked_until.pop(key, None)


limiter = LoginLimiter()


def too_many_message(seconds: int) -> str:
    minutes = max(1, math.ceil(seconds / 60))
    return (f"Too many wrong passwords. Wait {minutes} minute{'s' if minutes != 1 else ''} "
            "and try again, or ask your teacher to reset your password.")
