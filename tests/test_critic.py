"""Smoke test for the Pedagogical Critic.

Feeds two hand-crafted explanations through critique():
  1. A clean, structurally honest explanation (expected PASS).
  2. An explanation with a real physics error (expected FAIL on scientific
     correctness, with actionable feedback).

Runs only critic calls (no generator), so it is cheap on quota.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PROJECT_ROOT))

from src.agents.critic import critique


GOOD_EXPLANATION = """\
1. SCENARIO
You are a defender sprinting at 7 m/s along the touchline, chasing an attacker running 10 m/s in the same direction. To the spectators in the stands, the attacker moves at 10 m/s. To you, the gap opens at only 3 m/s — the attacker drifts away slowly, not at full pace. That 3 m/s is the attacker's velocity relative to you.

    attacker's ground speed  →  v_A = 10 m/s
    your ground speed        →  v_B = 7 m/s
    perceived closing speed  →  v_AB = v_A − v_B = 3 m/s
    spectators in the stands →  ground frame of reference

The analogy breaks if the attacker cuts laterally — then v_AB becomes a vector, and the 1D subtraction no longer captures the chase.

2. FORMAL RESTATEMENT
The **relative velocity** of A with respect to B along a straight line is v_AB = v_A − v_B, where velocities are signed in a chosen positive direction. The result describes A's motion as observed from B's frame.

3. SELF-CHECK QUESTION
If you accelerate to match the attacker at 10 m/s exactly, what does v_AB become, and what would the chase look like from your point of view at that instant?

[ANALOGY_QUALITY: 5]
"""

# Deliberately broken: claims KE is proportional to v (it is proportional to
# v^2). Also misstates the work-energy theorem as W = m·v.
BAD_EXPLANATION = """\
1. SCENARIO
In a racing game, your car's kinetic energy is just its mass times its speed. So if you double your speed, you double your kinetic energy. A boost pad that doubles your speed therefore doubles the work done on the car.

    car's speed         →  v
    kinetic energy bar  →  KE = m · v
    work by boost pad   →  W = m · v

The analogy breaks because in some games speed has a soft cap.

2. FORMAL RESTATEMENT
The **work-energy theorem** says the net work on an object equals the change in its **kinetic energy**: W_net = m · v_f − m · v_i, where m is mass and v is speed.

3. SELF-CHECK QUESTION
If a boost pad doubles your car's speed from 20 m/s to 40 m/s, how much does the kinetic energy change in terms of mass?

[ANALOGY_QUALITY: 5]
"""


def _pretty(verdict: dict) -> str:
    return json.dumps(verdict, indent=2, ensure_ascii=False)


def main() -> None:
    print("=" * 78)
    print("CASE 1 — GOOD explanation (relative velocity, football)")
    print("=" * 78)
    verdict_good = critique(GOOD_EXPLANATION, concept="relative velocity")
    print(_pretty(verdict_good))

    print()
    print("=" * 78)
    print("CASE 2 — BROKEN explanation (KE wrongly stated as linear in v)")
    print("=" * 78)
    verdict_bad = critique(BAD_EXPLANATION, concept="work-energy theorem")
    print(_pretty(verdict_bad))


if __name__ == "__main__":
    main()
