"""The demo dataset (2026-10-03): scripts/seed_demo.py fills a separate database.

No LLM calls. Proves: it refuses to write to the pilot database; it builds the class
(25 students, a teacher who can log in, a starting check for most and an end check
for most of those); the numbers come out of the real rules (before < after, studied
ideas gain more than unstudied ones); the personal stories carry the "demo-seed"
label; no AI usage is invented; the same seed gives the same class.

Run: venv\Scripts\python.exe tests\test_seed_demo.py
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "seed_demo.py"
tmp = Path(tempfile.mkdtemp())


def seed(db: Path, *extra: str) -> subprocess.CompletedProcess:
    env = {**os.environ, "ECOLEARN_PROGRESS_DB": str(db)}
    return subprocess.run([sys.executable, str(SCRIPT), *extra], env=env, cwd=ROOT,
                          capture_output=True, text=True)


# 1. It will not touch the pilot database, and won't overwrite without --reset.
refused = seed(ROOT / "data" / "progress.db", "--reset")
assert refused.returncode != 0 and "pilot database" in (refused.stdout + refused.stderr)
print("ok: refuses data/progress.db")

db = tmp / "demo.db"
done = seed(db, "--reset")
assert done.returncode == 0, done.stderr[-2000:]
again = seed(db)
assert again.returncode != 0 and "--reset" in (again.stdout + again.stderr)
print("ok: builds the class; won't overwrite without --reset")

# 2. Read it back through the boundary.
os.environ["ECOLEARN_PROGRESS_DB"] = str(db)
sys.path.insert(0, str(ROOT))
from src import platform_api as api  # noqa: E402
from src.progress import store  # noqa: E402

teacher = api.authenticate_teacher("demo.teacher", "demo-class-2026")
klass = store.list_classes(teacher["teacher_id"])[0]
assert klass["student_count"] == 25
student = api.authenticate_student("aarav.k", "demo-class-2026")
assert student["student_id"]
summary = api.get_class_checks(teacher["teacher_id"], klass["class_id"])["summary"]
assert summary["students_started"] == 23 and summary["students_finished"] == 20, summary
assert summary["right_after"] > summary["right_before"] + 0.1, summary
assert summary["studied"]["right_after"] - summary["studied"]["right_before"] \
    > summary["not_studied"]["right_after"] - summary["not_studied"]["right_before"]
print(f"ok: before {summary['right_before']:.0%} -> after {summary['right_after']:.0%}")

# 3. Honest labels: placeholder stories say so; no invented AI usage.
students = [s["student_id"] for s in store.list_class_students(klass["class_id"])]
stories = store.list_personal_stories(students)
assert stories and all(r["model"] == "demo-seed" for r in stories)
assert all("[Demo placeholder]" in (r["story"] or "") for r in stories if r["status"] == "ready")
assert store.get_llm_calls() == []
ai = api.get_class_ai_decisions(teacher["teacher_id"], klass["class_id"])
assert ai["stories"]["attempted"] == len(stories) and ai["plans"]["rules"] == 1
print("ok: stories are labelled demo-seed; the usage log is empty")

# 4. Activity is spread over weeks, not stamped 'now'.
activity = store.get_activity(students)
times = sorted(a["answered_at"] for rows in activity.values() for a in rows
               if "answered_at" in a)
assert times and times[0] < times[-1], "timestamps were not spread out"
print("ok: timestamps spread out")

# 5. Same seed, same class.
db2 = tmp / "demo2.db"
assert seed(db2, "--reset").returncode == 0
os.environ["ECOLEARN_PROGRESS_DB"] = str(db2)
t2 = store.get_teacher_by_username("demo.teacher")
k2 = store.list_classes(t2["teacher_id"])[0]
s2 = api.get_class_checks(t2["teacher_id"], k2["class_id"])["summary"]
assert {k: s2[k] for k in ("before", "after", "fixed", "slipped")} == \
       {k: summary[k] for k in ("before", "after", "fixed", "slipped")}
print("ok: deterministic")

# 6. --south-indian: its own database, never demo.db; everyone who started was last active in the last
#    two weeks, at a daytime hour in India, and nothing they did comes after that moment.
refused = subprocess.run([sys.executable, str(SCRIPT), "--south-indian", "--reset",
                          "--db", str(ROOT / "data" / "demo.db")], cwd=ROOT, capture_output=True, text=True)
assert refused.returncode != 0 and "demo.db" in (refused.stdout + refused.stderr)
db3 = tmp / "sample.db"
made = subprocess.run([sys.executable, str(SCRIPT), "--south-indian", "--reset", "--db", str(db3)],
                      cwd=ROOT, capture_output=True, text=True)
assert made.returncode == 0, made.stderr[-2000:]
os.environ["ECOLEARN_PROGRESS_DB"] = str(db3)
from datetime import datetime, timedelta, timezone  # noqa: E402
t3 = api.authenticate_teacher("sample.teacher", "demo-class-2026")
k3 = store.list_classes(t3["teacher_id"])[0]
roster = store.list_class_students(k3["class_id"])
assert "arjun.k" in {s["username"] for s in roster} and len(roster) == 25
now = datetime.now(timezone.utc)
ist = timezone(timedelta(hours=5, minutes=30))
active = [s for s in roster if s.get("last_active")]
assert len(active) == 23, len(active)
for s in active:
    last = datetime.fromisoformat(s["last_active"])
    assert now - timedelta(days=14, hours=1) <= last <= now, s
    assert 7 <= last.astimezone(ist).hour < 22, s
later = [a for rows in store.get_activity([s["student_id"] for s in active]).values() for a in rows
         if a.get("answered_at") and a["answered_at"] > max(s["last_active"] for s in active)]
assert not later
print("ok: --south-indian sample class, last activity within two weeks")
print("test_seed_demo: all passed")
