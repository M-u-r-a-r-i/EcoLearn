"""Randomised comparisons for the pilot (2026-10-18): who is in which arm, and what that switches off.

Why: the profile's adaptations (src/learner/profiler.py) are our own rules, and nothing yet shows they help.
The pilot is the chance to find out, and a comparison is only fair if chance, not us, decides who gets a
feature. Configured in data/experiments.yaml; pre-registered in docs/pilot-experiment.md.

How a student gets an arm (`choose_arm`):
  * once, when their account is made (or lazily the first time their profile is built, for older accounts);
  * balanced within their class: the arm with fewer students in that class so far, so a class of 30 splits
    15/15 (or 16/14), not 21/9 by bad luck;
  * a tie is broken by a hash of the experiment and the student id. That is as unpredictable as a coin to
    anyone making accounts, and anyone can re-check it later (an audit trail without storing a seed).
It never changes after that. Disabling an experiment stops the suppression (everyone gets the treatment),
and the stored arms stay for the analysis.

An arm can fix lesson preferences (`pref_overrides`: e.g. the "Before you pick" line on for treatment, off for
control) and/or switch profile insights off in control (`suppressed_insights`). Nobody is told the arm. Pure except `load_config`, which reads the YAML through the shared file cache.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
from typing import Any

import yaml

from src.file_cache import cached_parse

_PATH = Path(__file__).resolve().parents[2] / "data" / "experiments.yaml"
CONTROL, TREATMENT = "control", "treatment"
ARMS = (CONTROL, TREATMENT)


def load_config() -> list[dict[str, Any]]:
    """Every experiment in data/experiments.yaml (enabled or not)."""
    data = cached_parse(_PATH, lambda p: yaml.safe_load(p.read_text(encoding="utf-8")), "experiments")
    return list((data or {}).get("experiments") or [])


def enabled() -> list[dict[str, Any]]:
    """The enabled experiments; none at all when ECOLEARN_EXPERIMENTS=off (tests, or an operator's kill switch)."""
    if os.environ.get("ECOLEARN_EXPERIMENTS", "").strip().lower() == "off":
        return []
    return [e for e in load_config() if e.get("enabled")]


def tie_break(experiment_id: str, student_id: str) -> str:
    """The arm a tie goes to: a stable hash, re-checkable by anyone."""
    digest = hashlib.sha256(f"{experiment_id}:{student_id}".encode("utf-8")).digest()
    return ARMS[digest[0] % 2]


def choose_arm(experiment_id: str, student_id: str, class_counts: dict[str, int]) -> str:
    """The arm for a new student, given how many of their class are in each arm already."""
    control, treatment = class_counts.get(CONTROL, 0), class_counts.get(TREATMENT, 0)
    if control != treatment:
        return CONTROL if control < treatment else TREATMENT
    return tie_break(experiment_id, student_id)


def pref_overrides(arms: dict[str, str]) -> dict[str, Any]:
    """Lesson preferences fixed by a student's arms {experiment_id: arm}, e.g. {"slow_down": True}."""
    out: dict[str, Any] = {}
    for exp in enabled():
        arm = arms.get(exp["id"])
        if arm:
            out.update((exp.get("prefs") or {}).get(arm) or {})
    return out


def suppressed_insights(arms: dict[str, str]) -> set[str]:
    """The insight ids switched off for a student, from their arms {experiment_id: arm}."""
    off: set[str] = set()
    for exp in enabled():
        if arms.get(exp["id"]) == CONTROL:
            off |= set(exp.get("insights") or [])
    return off
