---
concept_id: motion_graphs
interest: motorsport
format: explain
title: The distance is hiding in a graph of speed
check:
  question: |-
    A car's velocity–time graph is a straight line rising from $0$ to $24\,\text{m/s}$ over the first $6.0\,\text{s}$ of an acceleration run. What is its displacement in those $6.0\,\text{s}$?
  options:
    A: |-
      $144\,\text{m}$
    B: |-
      $4.0\,\text{m}$
    C: |-
      It cannot be found, because a velocity–time graph shows no positions.
    D: |-
      $72\,\text{m}$
  answer: D
  explanation: |-
    Displacement is the area under the $v$–$t$ graph, here a triangle: $\tfrac{1}{2} \times 6.0\,\text{s} \times 24\,\text{m/s} = 72\,\text{m}$.
  misconceptions:
    A: |-
      Multiplies the final velocity by the time, $24 \times 6.0$, as if the car had held $24\,\text{m/s}$ throughout. That is the rectangle, not the triangle under the line.
    B: |-
      Works out the slope, $24/6.0 = 4.0$, which is the acceleration in $\text{m/s}^2$, and reads it as a displacement. Slope and area of a $v$–$t$ graph give different quantities.
    C: |-
      Assumes a graph with no positions on it can say nothing about position. Its area gives the displacement, even though no position is ever plotted.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A long straight at a race circuit with a car accelerating away from the timing beam at the start line, distance boards reading 0, 100 and 200 along the verge, and an arrow marking the positive direction](scenes/motorsport/motion_straight_line.svg "One acceleration run: launch, hold, brake. The distance boards would have told them how far — if anyone had been reading them.")

Anmol's Formula-student team gets three timed acceleration runs at the university test day, and the third one is the good one — the launch is clean, the car pulls hard, and the driver brakes late and neatly.

Then they open the data. The satellite receiver lost its lock halfway through the run, so the position channel is a flat line of nonsense. Every metre of the run is gone.

What survived is the wheel-speed sensor. It gives one thing, second by second: velocity. Anmol plots it — a line climbing to a peak, a short flat top, a steep drop to zero.

"Useless," says Shreya, who has to write the report. "The judges want the distance and the braking rate. There isn't a single metre anywhere on that graph."

Anmol keeps staring at it. The plot is just a shape: a slope here, a flat bit there, a region underneath.

Can you get both the braking rate *and* the distance out of a graph that only knows about speed?

## The physics

Two graphs describe straight-line motion, and each hides information in its **slope**:

- **Position–time ($x$–$t$):** the slope at a point is the **velocity** there, $v = dx/dt$. A straight segment means constant velocity, a curve bending upwards means the velocity is growing, a flat part means the object is at rest.
- **Velocity–time ($v$–$t$):** the slope is the **acceleration**, $a = dv/dt$.

The $v$–$t$ graph carries a second piece of information in its **area**. The area between the graph and the time axis, from $t_1$ to $t_2$, is the **displacement** over that interval. The reason is worth seeing: over a short time $\Delta t$ the displacement is $v\,\Delta t$, a thin strip of height $v$ and width $\Delta t$; add every strip and you have the area. Area below the time axis counts as negative displacement.

![Two graphs of the same motion. Left: position rising along a curve, then a straight section, then levelling off. Right: velocity rising, holding flat, then falling to zero, with the three areas under it marked](figures/motion_graphs/xt-and-vt-pair.svg "Same motion, two views. The slope of the left graph is the height of the right graph; the area under the right graph is the height the left graph climbs to.")

## Worked example

**Given:** the team's $v$–$t$ trace (illustrative): from $0$ to $20\,\text{m/s}$ in the first $4.0\,\text{s}$, steady at $20\,\text{m/s}$ until $6.0\,\text{s}$, then braking to rest at $8.0\,\text{s}$.
**Find:** the acceleration in each phase, and how far the car travelled.

**Slopes give the accelerations:**

$$a_1 = \frac{20 - 0}{4.0} = +5.0\,\text{m/s}^2, \quad a_2 = \frac{20 - 20}{2.0} = 0, \quad a_3 = \frac{0 - 20}{2.0} = -10\,\text{m/s}^2$$

The car brakes twice as hard as it accelerates — which is the normal state of affairs, since tyres and brakes can shed speed far faster than an engine can add it.

**Areas give the displacement:**

$$\text{triangle} = \tfrac{1}{2}(4.0)(20) = 40\,\text{m}, \quad \text{rectangle} = (2.0)(20) = 40\,\text{m}, \quad \text{triangle} = \tfrac{1}{2}(2.0)(20) = 20\,\text{m}$$

$$\Delta x = 40 + 40 + 20 = 100\,\text{m}$$

The velocity never goes negative, so the distance covered is also $100\,\text{m}$ — one full block of distance boards down the straight.

**Sanity check:** $100\,\text{m}$ in $8.0\,\text{s}$ is an average of $12.5\,\text{m/s}$, comfortably between the $0$ the car started at and the $20\,\text{m/s}$ it peaked at — which is where an average has to sit.

## Where the picture breaks

A wheel-speed sensor samples at intervals, so the straight lines and sharp corners are a tidy stand-in for a smooth, slightly noisy curve, and any area worked out from them is an estimate. A locked or spinning wheel also reports a speed the car does not have, which is exactly when the trace is least trustworthy. The area gives *displacement*, not position: the graph cannot say where the car started, so you need one known position — here, the start line — to turn the area into a place on the track. And if the velocity had dipped below the axis, that area would have to be subtracted, and displacement and distance would part company.

## Key takeaway

On an $x$–$t$ graph, slope $=$ velocity. On a $v$–$t$ graph, slope $=$ acceleration and the area under the graph $=$ displacement. So a plot with no metres on it still tells you how far the car went: add up the areas, and Anmol's run comes to $100\,\text{m}$.
