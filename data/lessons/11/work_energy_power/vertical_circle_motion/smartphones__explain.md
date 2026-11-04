---
concept_id: vertical_circle_motion
interest: smartphones
format: explain
title: When the earbuds case on the lanyard goes slack
check:
  question: |-
    A small key-finder tag is whirled on a light cord of length $0.40\,\text{m}$ in a vertical circle. Taking $g = 9.8\,\text{m/s}^2$, what is the minimum speed it must have **at the top** of the circle for the cord to stay taut?
  options:
    A: |-
      $2.0\,\text{m/s}$
    B: |-
      $0\,\text{m/s}$
    C: |-
      $4.4\,\text{m/s}$
    D: |-
      $3.9\,\text{m/s}$
  answer: A
  explanation: |-
    At the top, tension and weight both point to the centre: $T + mg = mv^2/r$. The cord is just taut when $T = 0$, so $v_\text{top} = \sqrt{gr} = \sqrt{9.8 \times 0.40} = \sqrt{3.92} \approx 2.0\,\text{m/s}$.
  misconceptions:
    B: |-
      Thinks the tag only has to reach the top, as it would on a rigid rod or over a hill. A cord can only pull, so at the top gravity alone must be no more than the centripetal force the circle needs — and that requires a speed of at least $\sqrt{gr}$.
    C: |-
      Quotes $\sqrt{5gr} = \sqrt{19.6}$, which is the minimum speed at the **bottom** of the circle, not the top. The tag slows by the time it has climbed $2r$.
    D: |-
      Finds $v^2 = gr = 3.92\,\text{m}^2/\text{s}^2$ and forgets to take the square root. The number has the wrong units for a speed.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A living room in the evening: a camera drone climbs straight up, a phone falls from a shelf towards a cushion, an earbuds case is whirled on a lanyard in a vertical circle, and a robot vacuum rolls towards a sofa leg](scenes/smartphones/work_energy_power.svg "In the middle of the picture, an earbuds case goes over the top of its circle. The lanyard can only pull; it can never push.")

Waiting for the school bus, Sneha is bored. Her earbuds case hangs from a thin lanyard, and she starts swinging it — first to and fro, then right round in a big vertical circle beside her, the lanyard held at arm's length.

It works beautifully while she swings fast. The case whooshes over the top, lanyard straight as a ruler.

Then she tries to go slower, and something odd happens. Near the top of the circle the lanyard suddenly goes floppy; the case stops following the circle, drops inwards, and the lanyard snaps taut again with a jerk.

"Don't let go of it," says her friend Aarti, stepping back.

Sneha is puzzled. She wasn't going *that* slowly. What is the slowest the case can go over the top without the lanyard going slack — and how fast must it be moving at the bottom to get there?

## The physics

For the case to move in a circle of radius $r$, the net force towards the centre must be $mv^2/r$. Two forces act on it: its weight $mg$ (always down) and the lanyard's tension $T$ (always towards the centre — a string can pull, never push).

![A mass on a string at the top, side and bottom of a vertical circle, with the tension and the weight drawn at each point, and the conditions for the minimum speeds](figures/vertical_circle_motion/forces-top-bottom-side.svg "At the top, the pull and the weight both point to the centre. At the bottom they point opposite ways, so the pull there must be large.")

**At the top**, both point down, towards the centre:

$$T + mg = \frac{mv_\text{top}^2}{r}$$

The string stays taut only while $T \ge 0$. At the limit $T = 0$, weight alone provides the centripetal force: $v_\text{top} = \sqrt{gr}$. Any slower, and gravity pulls the case inwards faster than the circle needs — the lanyard goes slack, exactly what Sneha saw.

**From bottom to top** the case rises $2r$. If only gravity does work (tension is always perpendicular to the motion, so it does none), mechanical energy is conserved:

$$\tfrac{1}{2}mv_\text{bottom}^2 = \tfrac{1}{2}mv_\text{top}^2 + mg(2r) \quad\Rightarrow\quad v_\text{bottom}^2 = v_\text{top}^2 + 4gr$$

With the minimum top speed, $v_\text{bottom} = \sqrt{5gr}$.

**At the bottom**, tension points up and weight down: $T - mg = mv_\text{bottom}^2/r$, so the pull is greatest there.

## Worked example

**Given:** radius (hand to case) $r = 0.50\,\text{m}$; case mass $m = 0.050\,\text{kg}$ (illustrative); $g = 9.8\,\text{m/s}^2$.
**Find:** the minimum speeds at the top and bottom, and the lanyard's pull at the bottom in that case.

1. *Top:* $v_\text{top} = \sqrt{gr} = \sqrt{9.8 \times 0.50} = \sqrt{4.9} \approx 2.2\,\text{m/s}$ — a brisk walking pace.
2. *Bottom:* $v_\text{bottom} = \sqrt{5gr} = \sqrt{24.5} \approx 4.9\,\text{m/s}$ — more than twice as fast, because it must still climb a whole metre.
3. *Pull at the bottom:* $T = mg + \dfrac{mv^2}{r} = m(9.8 + 49) = 0.050 \times 58.8 \approx 2.9\,\text{N}$, which is six times the case's weight.

**Sanity check:** the pull at the bottom of a fast swing is several times the case's weight — which is why the lanyard feels like it is tugging hard at the bottom and hardly at all at the top.

## Where the picture breaks

Mechanics isn't a natural home for gadgets, so here the earbuds case is just a convenient mass on a string, not an analogy. And Sneha's swing isn't a free vertical circle: her hand keeps moving and feeding in energy, so the speed doesn't follow energy conservation exactly, and the lanyard has some mass and stretch of its own. A rigid rod would behave differently — a rod can push, so it can carry a body over the top at almost zero speed. Finally, a real warning: swing a phone like this and a slack-then-jerk can snap the strap. The physics is best tested with something you don't mind dropping.

## Key takeaway

For a body on a string in a vertical circle, the string stays taut at the top only if $v_\text{top} \ge \sqrt{gr}$; energy conservation then requires $v_\text{bottom} \ge \sqrt{5gr}$. The tension is smallest at the top and largest at the bottom.
