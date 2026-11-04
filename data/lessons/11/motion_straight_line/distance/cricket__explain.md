---
concept_id: distance
interest: cricket
format: explain
title: How far did she really run for those three
check:
  question: |-
    A fielder in the deep sprints $25\,\text{m}$ in towards the pitch to stop a drive. The ball takes a deflection off her boot, and she runs $10\,\text{m}$ back out towards the rope to collect it. What distance has she covered?
  options:
    A: |-
      $15\,\text{m}$
    B: |-
      $25\,\text{m}$
    C: |-
      $-35\,\text{m}$
    D: |-
      $35\,\text{m}$
  answer: D
  explanation: |-
    Distance is the total length of the path, whatever the direction of each leg: $25\,\text{m} + 10\,\text{m} = 35\,\text{m}$.
  misconceptions:
    A: |-
      Subtracts the backward leg, $25 - 10 = 15\,\text{m}$ — that is how far she ended up from where she started (the size of her displacement), not the distance she ran.
    B: |-
      Takes the distance to be the farthest point she reached from her start, ignoring the extra path she ran on the way back.
    C: |-
      Gives distance a sign because her last leg was back towards the rope. Distance is a scalar and can never be negative.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground in sunshine: a batter runs between the wickets on a 22-yard pitch while a fielder chases the ball towards the boundary rope](scenes/cricket/motion_straight_line.svg "Running between the wickets means going up and down the same strip, again and again.")

Last over of a district under-17 match. Meera clips the ball into the gap at deep square leg and calls "Yes!" She and her partner run one, turn, run two, turn again as the fielder fumbles, and dive in for three. The team wins by a single run.

In the dressing room, her fitness band buzzes. Rohan, the team's twelfth man, peers at it. "It says you ran fifty-four metres. Rubbish. You started at one end and finished at the other. That's one pitch length — eighteen metres, maybe."

"Then why are my legs shaking?" Meera laughs.

Rohan isn't convinced. The band has an accelerometer and a clever algorithm; it must be measuring *something*. But he's also sure that Meera only ever finished one pitch length away from where she began.

Which number answers "how far did she run" — and why do the two disagree?

## The physics

**Distance** is the total length of the path an object actually travels. It has three defining properties:

- It adds up **every** part of the path, whichever way that part goes.
- It is a **scalar**: a size with a unit, but no direction.
- It can never be negative, and it never decreases as time goes on. The best it can do is stay the same, when the object stops.

Take the gap between the creases as about $18\,\text{m}$ (illustrative — the creases sit a little inside the $20.12\,\text{m}$ between the stumps). Meera's three runs are three legs:

$$\text{distance} = 18\,\text{m} + 18\,\text{m} + 18\,\text{m} = 54\,\text{m}$$

The second leg went back the "other way", but it still counts in full: her legs don't know which direction is positive. That is why the band says $54\,\text{m}$, and why she is tired.

Rohan's $18\,\text{m}$ is a different quantity: how far she ended up from her starting point, in a straight line. That is (the size of) her **displacement**, which you'll meet in the next lesson. For a trip that never turns around, the two are equal; as soon as the path doubles back, distance becomes larger.

![A path in three legs on a number line — 5 m forward, 5 m back, 3 m forward — with distance 13 m and displacement +3 m](figures/distance/path-legs-total.svg "Distance adds every leg as a positive length: 5 + 5 + 3 = 13 m. The start-to-end gap is only 3 m.")

In symbols, if a path is made of straight legs of lengths $d_1, d_2, d_3, \ldots$ then the distance is $d = d_1 + d_2 + d_3 + \cdots$, with every $d_i \ge 0$. Its SI unit is the metre.

## Worked example

**Given:** Meera completes three runs of about $18\,\text{m}$ each, then sets off for a fourth. After $7\,\text{m}$ her partner shouts "No!", and she turns and runs $7\,\text{m}$ back to the crease she had just reached.
**Find:** the total distance she ran, and how far she finished from where she started.

Distance adds every leg:

$$d = 18 + 18 + 18 + 7 + 7 = 68\,\text{m}$$

Where did she finish? After three runs she was at the far crease, $18\,\text{m}$ from her starting crease. The aborted fourth run took her out $7\,\text{m}$ and back $7\,\text{m}$ to that same crease. So she finished $18\,\text{m}$ from her starting point.

**Sanity check:** the distance ($68\,\text{m}$) is at least as large as the straight-line gap ($18\,\text{m}$), as it must be — and the extra $50\,\text{m}$ is exactly the two "wasted" legs of $18\,\text{m}$ plus the $14\,\text{m}$ false start: $36 + 14 = 50$.

## Where the picture breaks

Real batters don't run a perfectly straight line: they curve slightly to avoid the pitch, slow to turn, and stretch the bat across the crease, so the true path length differs from $18\,\text{m}$ per run by a metre or so. A fitness band estimates distance from arm swings and step counts — it can be off, and it has no idea about creases. Also, in this chapter every path lies along one line; in two dimensions (a fielder running a curve round the boundary) distance is the length along the curve, which a ruler laid from start to end would underestimate.

## Key takeaway

Distance is the total length of the path travelled: add every leg as a positive number, whatever its direction. It is a scalar, it is never negative, and it never goes down. Meera's three runs are $54\,\text{m}$ of distance, even though she finished only one pitch length from where she began.
