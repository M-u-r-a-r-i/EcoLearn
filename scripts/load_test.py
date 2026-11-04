"""Load test: a whole class using EcoLearn at once.

Starts its OWN API server on a temporary database (your data/progress.db is
never touched), creates a teacher and a class of N students, then has every
student work through a lesson at the same moment — the way a real lesson
starts when a teacher says "open EcoLearn now":

    log in → who am I → chapter list → roadmap → learning plan →
    starting check (fetch + submit) → next lesson → open it → report reading
    time → answer the check → rate the lesson → roadmap again

while the teacher refreshes the class page (insights, stories, plan) the
whole time. Every request is timed. The run fails (exit code 1) if any
request errors or the slowest 5% take longer than --p95-limit seconds.

Usage (from the project root):
    venv\\Scripts\\python.exe scripts\\load_test.py                  # 30 students
    venv\\Scripts\\python.exe scripts\\load_test.py --students 45 --rounds 2

No AI is called: the AI layers are switched off for the run (LLM_MODEL is
blanked), so this measures EcoLearn itself, not a model provider.
"""

from __future__ import annotations

import argparse
import os
import random
import socket
import statistics
import subprocess
import sys
import tempfile
import threading
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import httpx

_ROOT = Path(__file__).resolve().parents[1]
CHAPTER = "laws_of_motion"


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class Recorder:
    def __init__(self):
        self.times: dict[str, list[float]] = defaultdict(list)
        self.errors: list[str] = []
        self.lock = threading.Lock()

    def call(self, client: httpx.Client, name: str, method: str, url: str, **kwargs):
        start = time.perf_counter()
        try:
            response = client.request(method, url, **kwargs)
            elapsed = time.perf_counter() - start
            with self.lock:
                self.times[name].append(elapsed)
                if response.status_code >= 400:
                    self.errors.append(f"{name}: HTTP {response.status_code} {response.text[:120]}")
            return response
        except httpx.HTTPError as exc:
            with self.lock:
                self.times[name].append(time.perf_counter() - start)
                self.errors.append(f"{name}: {type(exc).__name__}")
            return None


def student_journey(base: str, username: str, password: str, rec: Recorder, start: threading.Event) -> None:
    with httpx.Client(base_url=base, timeout=60) as c:
        start.wait()  # everyone starts at once
        rec.call(c, "login", "POST", "/api/auth/login", json={"username": username, "password": password})
        rec.call(c, "session", "GET", "/api/auth/session")
        rec.call(c, "chapters", "GET", "/api/chapters", params={"interest": "cricket"})
        rec.call(c, "roadmap", "GET", "/api/roadmap", params={"chapter_id": CHAPTER})
        rec.call(c, "learning-plan", "GET", "/api/learning-plan")
        diag = rec.call(c, "diagnostic GET", "GET", "/api/diagnostic")
        if diag is not None and diag.status_code == 200 and not diag.json().get("taken"):
            picks = {q["concept_id"]: random.choice([*q["options"], "unsure"])
                     for q in diag.json()["questions"]}
            rec.call(c, "diagnostic POST", "POST", "/api/diagnostic",
                     json={"answers": picks, "hobbies": ["badminton", "music"]})
        nxt = rec.call(c, "next-lesson", "GET", "/api/next-lesson", params={"chapter_id": CHAPTER})
        if nxt is None or nxt.status_code != 200 or not nxt.json().get("lesson"):
            return
        lesson = nxt.json()["lesson"]
        concept = lesson["concept_id"]
        view = rec.call(c, "lesson-views", "POST", "/api/lesson-views", json={"concept_id": concept})
        if view is not None and view.status_code == 201:
            rec.call(c, "lesson time", "POST", f"/api/lesson-views/{view.json()['view_id']}/time",
                     content='{"active_seconds": 20}', headers={"Content-Type": "text/plain"})
        options = list((lesson.get("check") or {}).get("options") or {"A": ""})
        rec.call(c, "assessment", "POST", "/api/assessment",
                 json={"concept_id": concept, "answer": random.choice(options)})
        rec.call(c, "rating", "POST", "/api/lesson-ratings", json={"concept_id": concept, "rating": 1})
        rec.call(c, "roadmap", "GET", "/api/roadmap", params={"chapter_id": CHAPTER})


def teacher_watch(base: str, class_id: str, rec: Recorder, start: threading.Event, stop: threading.Event) -> None:
    with httpx.Client(base_url=base, timeout=60) as c:
        start.wait()
        rec.call(c, "teacher login", "POST", "/api/teacher/login",
                 json={"username": "load.teacher", "password": "load-test-pass-1"})
        while not stop.is_set():
            rec.call(c, "class insights", "GET", f"/api/teacher/classes/{class_id}/insights")
            rec.call(c, "class stories", "GET", f"/api/teacher/classes/{class_id}/stories")
            rec.call(c, "class detail", "GET", f"/api/teacher/classes/{class_id}")
            time.sleep(0.5)
        rec.call(c, "class plan (rules)", "POST", f"/api/teacher/classes/{class_id}/plan")


def pct(values: list[float], p: float) -> float:
    ordered = sorted(values)
    return ordered[min(len(ordered) - 1, max(0, round(p / 100 * len(ordered)) - 1))]


def main() -> int:
    parser = argparse.ArgumentParser(description="EcoLearn load test (own server, temp DB).")
    parser.add_argument("--students", type=int, default=30)
    parser.add_argument("--rounds", type=int, default=1, help="how many times the class repeats the journey")
    parser.add_argument("--p95-limit", type=float, default=2.0, help="seconds; fail above this")
    args = parser.parse_args()

    tmp = Path(tempfile.mkdtemp(prefix="ecolearn_load_"))
    env = {**os.environ, "ECOLEARN_PROGRESS_DB": str(tmp / "load.db"), "LLM_MODEL": "",
           "GEMINI_API_KEY": "", "PYTHONIOENCODING": "utf-8"}
    os.environ.update({k: env[k] for k in ("ECOLEARN_PROGRESS_DB", "LLM_MODEL", "GEMINI_API_KEY")})
    sys.path.insert(0, str(_ROOT / "src"))
    sys.path.insert(0, str(_ROOT / "apps"))
    from ecolearn import platform_api as api  # noqa: E402 — after the DB is redirected

    api.create_teacher("Load Teacher", "load.teacher", "load-test-pass-1")
    teacher_id = api.authenticate_teacher("load.teacher", "load-test-pass-1")["teacher_id"]
    roster = "\n".join(f"Student {i:02d}" for i in range(args.students))
    made = api.create_class(teacher_id, "Load 11-A", "Class 11", "cricket", roster)
    class_id = made["class"]["class_id"]
    logins = [(c["username"], c["password"]) for c in made["credentials"]]

    port = free_port()
    base = f"http://127.0.0.1:{port}"
    server = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "api.main:app", "--app-dir", "apps",
         "--port", str(port), "--log-level", "warning"],
        cwd=_ROOT, env=env)
    try:
        for _ in range(60):
            try:
                if httpx.get(base + "/", timeout=1).status_code == 200:
                    break
            except httpx.HTTPError:
                time.sleep(0.5)
        else:
            print("The test server didn't start.", file=sys.stderr)
            return 1

        rec = Recorder()
        wall = time.perf_counter()
        for round_no in range(args.rounds):
            start, stop = threading.Event(), threading.Event()
            with ThreadPoolExecutor(max_workers=args.students + 1) as pool:
                watcher = pool.submit(teacher_watch, base, class_id, rec, start, stop)
                journeys = [pool.submit(student_journey, base, u, p, rec, start) for u, p in logins]
                start.set()
                for j in journeys:
                    j.result()
                stop.set()
                watcher.result()
        wall = time.perf_counter() - wall
    finally:
        server.terminate()
        server.wait(timeout=10)

    total = sum(len(v) for v in rec.times.values())
    every = [t for v in rec.times.values() for t in v]
    print(f"\nEcoLearn load test: {args.students} students × {args.rounds} round(s), "
          f"{total} requests in {wall:.1f} s, {len(rec.errors)} errors\n")
    print(f"  {'endpoint':<22}{'n':>5}{'p50 ms':>9}{'p95 ms':>9}{'max ms':>9}")
    for name, values in sorted(rec.times.items(), key=lambda kv: -pct(kv[1], 95)):
        print(f"  {name:<22}{len(values):>5}{statistics.median(values) * 1000:>9.0f}"
              f"{pct(values, 95) * 1000:>9.0f}{max(values) * 1000:>9.0f}")
    overall95 = pct(every, 95)
    print(f"\n  all requests: p50 {statistics.median(every) * 1000:.0f} ms, "
          f"p95 {overall95 * 1000:.0f} ms, max {max(every) * 1000:.0f} ms")
    for e in rec.errors[:15]:
        print(f"  ERROR {e}")
    ok = not rec.errors and overall95 <= args.p95_limit
    print("\n  RESULT:", "PASS" if ok else f"FAIL (errors or p95 above {args.p95_limit} s)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
