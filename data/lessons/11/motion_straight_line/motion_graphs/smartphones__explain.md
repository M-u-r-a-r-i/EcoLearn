---
concept_id: motion_graphs
interest: smartphones
format: explain
title: How high did the drone go, from a graph with no height on it
check:
  question: |-
    A camera drone climbing straight up slows to a hover. Its velocity–time graph (upwards positive) is a straight line falling from $6\,\text{m/s}$ to $0$ over $3\,\text{s}$. How much height does it gain in those $3\,\text{s}$?
  options:
    A: |-
      $18\,\text{m}$
    B: |-
      $2\,\text{m}$
    C: |-
      $-9\,\text{m}$
    D: |-
      $9\,\text{m}$
  answer: D
  explanation: |-
    Displacement is the area under the $v$–$t$ graph. Here the area is a triangle above the time axis: $\tfrac{1}{2} \times 3\,\text{s} \times 6\,\text{m/s} = 9\,\text{m}$, upwards.
  misconceptions:
    A: |-
      Multiplies the starting velocity by the time, $6 \times 3$, as if the drone had climbed at $6\,\text{m/s}$ the whole time. That is the area of the rectangle, not of the triangle under the line.
    B: |-
      Works out the slope, $6/3 = 2$ — the size of the acceleration in $\text{m/s}^2$ — and reads it as a height. Slope and area of a $v$–$t$ graph give different quantities.
    C: |-
      Thinks a falling line means the drone is moving down. The line slopes down because the drone is slowing, but $v$ stays positive, so the area — and the displacement — is positive.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![An evening street: a phone shows a live-tracking map of a straight road, while a delivery scooter rides past kilometre markers](scenes/smartphones/motion_straight_line.svg "Phones log motion as data — positions, speeds, times. Sometimes only part of the log survives.")

Sanya is in charge of the school's camera drone for Annual Day, flying it from a phone app. The principal has one rule: the drone must stay below $20\,\text{m}$ above the ground (illustrative). She sends it straight up for an overhead shot of the whole assembly.

That evening, the video teacher Mr. Bose wants to check the flight. But the height log is corrupted. The only data that survives is the drone's vertical velocity, sampled through the climb. Sanya plots it: a line climbing to $7\,\text{m/s}$, a short flat top, then a steep drop to zero as the drone stopped to hover.

"No heights anywhere," Mr. Bose sighs. "So we can't know whether you broke the rule."

Sanya stares at the shape on her screen: a slope, a flat bit, a slope the other way, and a region underneath. It feels as if the answer ought to be hiding in the shape.

Can you get the drone's acceleration *and* its height out of a graph of velocity alone?

## The physics

Two graphs describe straight-line motion, and each carries information in its **slope**:

- **Position–time ($x$–$t$) graph:** the slope at any point is the **velocity** there, $v = dx/dt$. A straight segment means constant velocity; a curve bending upwards means the velocity is increasing; a flat part means the object is at rest.
- **Velocity–time ($v$–$t$) graph:** the slope is the **acceleration**, $a = dv/dt$.

The $v$–$t$ graph also carries information in its **area**. The area between the graph and the time axis, from $t_1$ to $t_2$, equals the **displacement** in that interval. Why? Over a very short time $\Delta t$, the displacement is $v\,\Delta t$ — a thin strip of height $v$ and width $\Delta t$. Adding all the strips gives the area. Area below the time axis counts as negative displacement.

For the drone the line is vertical, so take $x$ as its height above the launch pad, with upwards positive.

![Two graphs of the same motion. Left: position rising along a curve, then a straight section, then levelling off at 17.5 m. Right: velocity rising to 7 m/s over 2 s, flat for 1 s, then falling to zero at 4 s, with areas 7 m, 7 m and 3.5 m marked](figures/motion_graphs/xt-and-vt-pair.svg "Same climb, two views. The slope of the left graph is the height of the right graph; the area under the right graph is the height the left graph reaches.")

## Worked example

**Given:** the drone's $v$–$t$ graph (illustrative): from $0$ to $7\,\text{m/s}$ in the first $2.0\,\text{s}$, steady at $7\,\text{m/s}$ until $3.0\,\text{s}$, then down to $0$ at $4.0\,\text{s}$. It started on the ground.
**Find:** its acceleration in each phase and the height it reached.

**Slopes (acceleration):**

$$a_1 = \frac{7 - 0}{2.0} = +3.5\,\text{m/s}^2, \quad a_2 = \frac{7 - 7}{1.0} = 0, \quad a_3 = \frac{0 - 7}{1.0} = -7.0\,\text{m/s}^2$$

It braked twice as hard as it sped up.

**Areas (displacement):**

$$\text{triangle} = \tfrac{1}{2}(2.0)(7) = 7.0\,\text{m}, \quad \text{rectangle} = (1.0)(7) = 7.0\,\text{m}, \quad \text{triangle} = \tfrac{1}{2}(1.0)(7) = 3.5\,\text{m}$$

$$\Delta x = 7.0 + 7.0 + 3.5 = 17.5\,\text{m}$$

It started at ground level, so it hovered at $17.5\,\text{m}$ — under the $20\,\text{m}$ limit. Sanya kept the rule.

**Sanity check:** read the $x$–$t$ graph. Its straight middle section climbs from $7\,\text{m}$ to $14\,\text{m}$ in $1\,\text{s}$ — a slope of $7\,\text{m/s}$, matching the flat top of the $v$–$t$ graph. It levels off at $17.5\,\text{m}$, matching the total area.

## Where the picture breaks

The log gives velocity at intervals, not continuously, so straight lines and sharp corners are an idealisation of a smoother real curve; areas worked out from them are estimates. The area gives the *change* in height only — the graph can't tell you where the drone started, so you need one known position (here, the ground). A real drone also drifts sideways in wind, which a single vertical axis ignores. And if the drone had descended, its velocity would go negative and that area would subtract: then displacement and distance would differ.

## Key takeaway

On an $x$–$t$ graph, slope $=$ velocity. On a $v$–$t$ graph, slope $=$ acceleration and area under the graph $=$ displacement. So a velocity log with no heights on it still tells you how high the drone went: add up the areas.
