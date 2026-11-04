"""Run the deterministic test suite in one go (no API key, no network).

    venv\\Scripts\\python.exe scripts\\check.py            # everything
    venv\\Scripts\\python.exe scripts\\check.py --fast     # skip the slow ones (~1 min seed, load test)
    venv\\Scripts\\python.exe scripts\\check.py auth mastery   # only tests whose name contains a word

Each test stays a standalone script (AGENTS.md §4: not pytest); this only runs them in order,
with the same Python, and prints a summary. Live-model tests (test_platform_api.py, the
benchmarks) are never run from here: they cost quota.
"""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (script, args) in the order AGENTS.md §6 lists them. test_persistence runs twice on purpose:
# "seed" writes a DB, "verify" reopens it in a fresh process.
SUITE: list[tuple[str, list[str]]] = [
    ("tests/test_auth.py", []),
    ("tests/test_curriculum.py", []),
    ("tests/test_path_engine.py", []),
    ("tests/test_edge_states.py", []),
    ("tests/test_scale_chapter2.py", []),
    ("tests/test_persistence.py", ["seed"]),
    ("tests/test_persistence.py", ["verify"]),
    ("tests/test_content_spine.py", []),
    ("tests/test_authored_lessons.py", []),
    ("tests/test_api_auth.py", []),
    ("tests/test_mcq_grading.py", []),
    ("tests/test_teacher.py", []),
    ("tests/test_pilot_metrics.py", []),
    ("tests/test_chapter_coverage.py", []),
    ("tests/test_teacher_agent.py", []),
    ("tests/test_learner_plan.py", []),
    ("tests/test_personal_story.py", []),
    ("tests/test_story_review.py", []),
    ("tests/test_rate_limit.py", []),
    ("tests/test_end_check.py", []),
    ("tests/test_mix_ups.py", []),
    ("tests/test_mastery.py", []),
    ("tests/test_llm_usage.py", []),
    ("tests/test_ai_decisions.py", []),
    ("tests/test_concept_locks.py", []),
    ("tests/test_survey.py", []),
    ("tests/test_pilot_survey.py", []),
    ("tests/test_coaching_agent.py", []),
    ("tests/test_help_guard.py", []),
    ("tests/test_student_data_rights.py", []),
    ("tests/test_ai_switch.py", []),
    ("tests/test_learner_profile.py", []),
    ("tests/test_pilot_experiment.py", []),
    ("tests/test_ai_practice.py", []),
    ("scripts/validate_lessons.py", []),
    ("scripts/batch_status.py", []),
    ("tests/test_seed_demo.py", []),   # slow
    ("scripts/load_test.py", []),      # slow, starts its own server
]
SLOW = {"tests/test_seed_demo.py", "scripts/load_test.py"}


def main(argv: list[str]) -> int:
    fast = "--fast" in argv
    words = [a for a in argv if not a.startswith("--")]
    suite = [(s, a) for s, a in SUITE
             if not (fast and s in SLOW) and (not words or any(w in s for w in words))]

    failed: list[str] = []
    for script, args in suite:
        label = " ".join([script, *args])
        start = time.monotonic()
        proc = subprocess.run([sys.executable, script, *args], cwd=ROOT,
                              capture_output=True, text=True, encoding="utf-8", errors="replace")
        took = time.monotonic() - start
        ok = proc.returncode == 0
        print(f"{'PASS' if ok else 'FAIL'}  {took:6.1f}s  {label}", flush=True)
        if not ok:
            failed.append(label)
            print("\n".join((proc.stdout + proc.stderr).strip().splitlines()[-25:]), "\n", flush=True)

    print(f"\n{len(suite) - len(failed)}/{len(suite)} passed")
    for f in failed:
        print(f"  failed: {f}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
