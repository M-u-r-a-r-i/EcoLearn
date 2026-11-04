r"""Measure the personal-story AI: how often it passes, where it fails, what it costs.

    venv\Scripts\python.exe scripts\eval_stories.py --cases 12

Runs the real writer and critic (the live AI configured in .env) on a spread of
student / interest / hobby / concept cases, on a TEMPORARY database (your data is
never touched), then prints a report you can quote: ready rate, first-draft pass
rate, failures by step and reason, latency, tokens and cost per story, and a few
stories to read by hand. `--out report.md` also saves it.

Cases are chosen deterministically (same command, same cases), so two runs on two
models are comparable. Needs a working AI: check with scripts\ai_check.py first.
The cost uses data/llm_prices.yaml (Google's paid-tier list prices, checked 2026-10-13):
it is what the same calls WOULD cost on a paid key, not a bill (a free tier bills nothing).
"""
from __future__ import annotations

import argparse
import os
import statistics
import sys
import tempfile
import time
import warnings
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "apps"))
_TMP = Path(tempfile.mkdtemp(prefix="ecolearn_eval_"))
os.environ["ECOLEARN_PROGRESS_DB"] = str(_TMP / "eval.db")  # before importing the app code
warnings.simplefilter("ignore")

from ecolearn import llm, platform_api as api  # noqa: E402
from ecolearn.content import lesson_service  # noqa: E402
from ecolearn.learner import diagnostic, personal_story as ps  # noqa: E402
from ecolearn.path import engine  # noqa: E402
from ecolearn.progress import metrics, store  # noqa: E402

INTERESTS = ["cricket", "football", "gaming", "smartphones", "motorsport"]


def build_cases(n: int) -> list[dict]:
    """A deterministic spread: interests in turn, concepts at a stride so domains vary,
    and for each the next listed hobby (not the student's own interest) that fits."""
    chapters = {c["id"]: c for c in engine.list_chapters()}
    by_chapter = engine.concept_ids_by_chapter()
    domain_of = {cid: chapters[ch]["domain"] for ch, ids in by_chapter.items() for cid in ids}
    hobbies = diagnostic.hobby_options()
    pools = {}
    for interest in INTERESTS:
        have = lesson_service.concepts_with_lessons(interest)
        ordered = [c for ids in by_chapter.values() for c in ids if c in have]
        pools[interest] = ordered[:: max(1, len(ordered) // 20)]
    cases, i = [], 0
    while len(cases) < n and i < 400:
        interest = INTERESTS[i % len(INTERESTS)]
        pool = pools[interest]
        concept = pool[(i // len(INTERESTS)) % len(pool)] if pool else None
        i += 1
        if concept is None:
            continue
        fits = [h for h in hobbies if h.get("interest") != interest
                and domain_of[concept] in (h.get("fits") or [])]
        if fits:
            hobby = fits[(i // len(INTERESTS)) % len(fits)]
            cases.append({"interest": interest, "concept": concept, "hobby": hobby["id"],
                          "domain": domain_of[concept]})
    return cases


def p95(values: list[float]) -> float:
    ordered = sorted(values)
    return ordered[min(len(ordered) - 1, int(0.95 * len(ordered)))]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--cases", type=int, default=12, help="how many stories to write (default 12)")
    ap.add_argument("--out", help="also save the report to this file")
    args = ap.parse_args()
    if not llm.is_configured():
        print("No AI configured (LLM_MODEL is empty): nothing to measure.")
        return 1
    cases = build_cases(args.cases)
    results = []
    for n, case in enumerate(cases, start=1):
        sid = api.register_student(f"Eval Student {n}", f"eval.s{n}", "eval-password-1",
                                   case["interest"], "Class 11")["student_id"]
        store.save_diagnostic(sid, [case["hobby"]], [])
        started = time.monotonic()
        with llm.usage_context(feature="story_writer", student_id=sid):
            row = ps.generate(sid, case["concept"])
        took = time.monotonic() - started
        status = row["status"] if row else "nothing_to_write"
        results.append({**case, "sid": sid, "status": status, "seconds": took, "row": row})
        print(f"  {n:>2}/{len(cases)} {status:<9} {took:5.1f}s  {case['interest']:<11} "
              f"{case['hobby']:<10} {case['concept']}", flush=True)

    made = [r for r in results if r["row"]]
    counts = Counter(r["status"] for r in results)
    ready = counts.get("ready", 0)
    first_try = sum(1 for r in made if r["status"] == "ready" and r["row"]["attempts"] == 1)
    steps = [t for r in made for t in r["row"].get("trail", [])]
    step_fail = Counter(t["step"] for t in steps if not t["passed"])
    reasons = Counter(p[:90] for t in steps if not t["passed"] for p in t["problems"])
    secs = [r["seconds"] for r in made]
    calls = store.get_llm_calls()
    usage = metrics.ai_usage(calls, api.llm_prices(), len(results))["total"]
    stories = max(1, len(made))

    out = [
        "# Personal-story AI evaluation",
        f"Models: {', '.join(sorted({c['model'] for c in calls})) or 'n/a'}. "
        f"{len(results)} cases on a temporary database.",
        "",
        "| Measure | Result |", "|---|---|",
        f"| Stories ready (shown to a student) | {ready} of {len(results)} ({round(100 * ready / len(results))}%) |",
        f"| Ready on the first draft | {first_try} of {len(made)} |",
        f"| Writer declined (no honest link to the hobby) | {counts.get('no_fit', 0)} |",
        f"| Failed all drafts (lesson's own story shown) | {counts.get('failed', 0)} |",
        f"| Model errors | {counts.get('error', 0)} |",
        f"| Time per story, median / p95 | {statistics.median(secs):.0f} s / {p95(secs):.0f} s |" if secs else "",
        f"| Model calls per story | {usage['calls'] / stories:.1f} (failed calls: {usage['failed']}) |",
        f"| Tokens per story (in / out) | {usage['prompt_tokens'] // stories} / {usage['completion_tokens'] // stories} |",
        f"| Cost per story at the reference price | Rs {usage['reference_inr'] / stories:.2f} |",
        "",
        "## Where drafts failed",
    ]
    out += [f"- {step}: {n}" for step, n in step_fail.most_common()] or ["- nothing failed"]
    out += ["", "## Most common reasons"]
    out += [f"- {n}x {why}" for why, n in reasons.most_common(6)] or ["- none"]
    out += ["", "## Stories to read by hand"]
    for r in [r for r in made if r["status"] == "ready"][:3]:
        row = r["row"]
        out += [f"**{r['interest']} student, hobby {r['hobby']}, concept {r['concept']}**",
                f"> {row['story']}", f"> Analogy: {row['analogy']}", f"> Limit: {row['limit_text']}", ""]
    report = "\n".join(line for line in out if line is not None)
    print("\n" + report)
    if args.out:
        Path(args.out).write_text(report + "\n", encoding="utf-8")
        print(f"\nSaved to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
