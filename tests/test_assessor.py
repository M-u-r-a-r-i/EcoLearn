"""Smoke test for the Assessor agent.

Generates one question about the work-energy theorem themed in football,
then grades three hand-written answers spanning the quality spectrum:
GREAT (correct, complete, applied), PARTIAL (formula right but shallow),
and WRONG (uses the wrong formula entirely).

Prints the question and three verdicts for visual inspection.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_PROJECT_ROOT))

from src.agents.assessor import generate_question, grade_answer


CONCEPT = "work-energy theorem"
INTEREST = "football"
LEVEL = "Class 11"


# Three answers spanning the quality spectrum. Written in a Class 11 student
# voice — slightly informal, ASCII-only math, no LaTeX.

GREAT_ANSWER = """
The work-energy theorem says the net work done on an object equals the
change in its kinetic energy: W_net = (1/2) m v_f^2 - (1/2) m v_i^2.

Suppose a striker of mass 80 kg accelerates from rest (v_i = 0) to a sprint
speed of 8 m/s. The change in KE is (1/2)(80)(8^2 - 0) = 2560 J. So the
net work on the player must be 2560 J. That net work is the work done by
the legs minus the work done against grass friction.

If the same striker doubles their final speed to 16 m/s, the new KE is
(1/2)(80)(16^2) = 10240 J — four times the original. This is the v^2
dependence: doubling speed quadruples the energy needed, which is why
sprinting at the top of your speed is exhausting compared with jogging.
""".strip()


PARTIAL_ANSWER = """
The work-energy theorem says that the work done on the player equals the
change in kinetic energy. So W = (1/2) m v^2 - (1/2) m v_0^2. You can plug
in the player's mass and their starting and ending speeds to find how much
energy the player put in.
""".strip()


WRONG_ANSWER = """
The work-energy theorem just says that work equals mass times velocity:
W = m * v. So if a player runs faster, the work done by their legs is
bigger because v is bigger. A heavier player also does more work for the
same speed.
""".strip()


def _pretty(d: dict) -> str:
    return json.dumps(d, indent=2, ensure_ascii=False)


def main() -> None:
    bar = "=" * 78

    print(bar)
    print(
        f"GENERATING QUESTION  concept={CONCEPT!r}  "
        f"interest={INTEREST!r}  level={LEVEL!r}"
    )
    print(bar)
    question_dict = generate_question(CONCEPT, INTEREST, LEVEL)
    print(_pretty(question_dict))
    print()

    question = question_dict.get("question", "")
    expected_concepts = question_dict.get("expected_concepts", [])

    if not question or "error" in question_dict:
        print("Question generation failed; cannot grade answers.")
        return

    for label, answer in [
        ("GREAT", GREAT_ANSWER),
        ("PARTIAL", PARTIAL_ANSWER),
        ("WRONG", WRONG_ANSWER),
    ]:
        print(bar)
        print(f"GRADING — '{label}' answer")
        print(bar)
        print("Student answer:")
        print(answer)
        print()
        print("Verdict:")
        verdict = grade_answer(question, expected_concepts, answer)
        print(_pretty(verdict))
        print()


if __name__ == "__main__":
    main()
