---
concept_id: motion_graphs
interest: cricket
format: explain
title: How far did he run, from a graph with no distance on it
check:
  question: |-
    A batter's velocity–time graph is a straight line rising from $0$ to $6\,\text{m/s}$ over the first $3\,\text{s}$ of a run. What is his displacement in those $3\,\text{s}$?
  options:
    A: |-
      $18\,\text{m}$
    B: |-
      $2\,\text{m}$
    C: |-
      $9\,\text{m}$
    D: |-
      It cannot be found, because a velocity–time graph shows no positions.
  answer: C
  explanation: |-
    Displacement is the area under the $v$–$t$ graph. Here that is a triangle: $\tfrac{1}{2} \times 3\,\text{s} \times 6\,\text{m/s} = 9\,\text{m}$.
  misconceptions:
    A: |-
      Multiplies the final velocity by the time, $6 \times 3$, as if he had run at $6\,\text{m/s}$ the whole time. That is the area of the rectangle, not of the triangle under the line.
    B: |-
      Works out the slope, $6/3 = 2$ — which is the acceleration in $\text{m/s}^2$ — and reads it as a displacement. Slope and area of a $v$–$t$ graph give different quantities.
    D: |-
      Thinks a $v$–$t$ graph cannot tell you about position. The area under it gives the displacement, even though no position is plotted.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground in sunshine: a batter runs between the wickets on a 22-yard pitch while a fielder chases the ball towards the boundary rope](scenes/cricket/motion_straight_line.svg "One quick single — sprint, cruise, brake and ground the bat.")

Nikhil is helping the academy's video analyst for the summer. In the match footage, the non-striker takes off for a sharp single — and at the crucial moment the umpire steps right in front of the tracking camera. The position data for the whole run is lost.

All that survives is the batter's speed sensor. It gives one thing: his velocity, second by second. Nikhil plots it: a line climbing to $7\,\text{m/s}$, a short flat top, a steep drop to zero as he grounds his bat.

"Useless," says the analyst's assistant, Priyanka. "The coach wants to know how far he ran and how hard he braked. There isn't a single distance on that graph."

Nikhil keeps looking at it. The graph is just a shape — a slope here, a flat bit there, a region underneath. It feels as if the answers ought to be hiding in the shape.

Can you get acceleration *and* distance out of a graph of velocity alone?

## The physics

Two graphs describe straight-line motion, and each carries information in its **slope**:

- **Position–time ($x$–$t$) graph:** the slope at any point is the **velocity** there, $v = dx/dt$. A straight segment means constant velocity; a curve bending upwards means the velocity is increasing; a flat part means the object is at rest.
- **Velocity–time ($v$–$t$) graph:** the slope is the **acceleration**, $a = dv/dt$.

The $v$–$t$ graph also carries information in its **area**. The area between the graph and the time axis, from $t_1$ to $t_2$, equals the **displacement** in that interval. Why? For a short time $\Delta t$, the displacement is $v\,\Delta t$ — a thin strip of height $v$ and width $\Delta t$. Adding all the strips gives the area. Area below the time axis counts as negative displacement.

![Two graphs of the same run. Left: position rising along a curve, then a straight section, then levelling off at 17.5 m. Right: velocity rising to 7 m/s over 2 s, flat for 1 s, then falling to zero at 4 s, with areas 7 m, 7 m and 3.5 m marked](figures/motion_graphs/xt-and-vt-pair.svg "Same run, two views. The slope of the left graph is the height of the right graph; the area under the right graph is the height the left graph reaches.")

## Worked example

**Given:** the batter's $v$–$t$ graph (illustrative): from $0$ to $7\,\text{m/s}$ in the first $2.0\,\text{s}$, steady at $7\,\text{m/s}$ until $3.0\,\text{s}$, then down to $0$ at $4.0\,\text{s}$.
**Find:** his acceleration in each phase and the distance he ran.

**Slopes (acceleration):**

$$a_1 = \frac{7 - 0}{2.0} = +3.5\,\text{m/s}^2, \quad a_2 = \frac{7 - 7}{1.0} = 0, \quad a_3 = \frac{0 - 7}{1.0} = -7.0\,\text{m/s}^2$$

He braked twice as hard as he accelerated.

**Areas (displacement):**

$$\text{triangle} = \tfrac{1}{2}(2.0)(7) = 7.0\,\text{m}, \quad \text{rectangle} = (1.0)(7) = 7.0\,\text{m}, \quad \text{triangle} = \tfrac{1}{2}(1.0)(7) = 3.5\,\text{m}$$

$$\Delta x = 7.0 + 7.0 + 3.5 = 17.5\,\text{m}$$

Since his velocity never went negative, the distance run is also $17.5\,\text{m}$ — about the gap between the creases.

**Sanity check:** read the $x$–$t$ graph. Its straight middle section climbs from $7\,\text{m}$ to $14\,\text{m}$ in $1\,\text{s}$ — a slope of $7\,\text{m/s}$, matching the flat top of the $v$–$t$ graph. It levels off at $17.5\,\text{m}$, matching the total area.

## Where the picture breaks

The sensor gives velocity at intervals, not continuously, so the straight lines and sharp corners are an idealisation of a smooth, wobbly real curve; areas computed from them are estimates. The area gives displacement only from the moment you start adding — the graph alone can't tell you *where* the batter started, so you need one known position (here, his crease) to turn displacement into position. And if the velocity had dipped below zero (he turned back), that area would subtract: then displacement and distance would differ.

## Key takeaway

On an $x$–$t$ graph, slope $=$ velocity. On a $v$–$t$ graph, slope $=$ acceleration and area under the graph $=$ displacement. So a graph with no distance on it still tells you how far the batter ran: add up the areas.
