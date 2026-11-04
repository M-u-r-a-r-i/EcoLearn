---
concept_id: motion_graphs
interest: gaming
format: explain
title: Half a metre short of the switch
check:
  question: |-
    In a racing game, a car's velocity–time graph is a straight line rising from $0$ to $30\,\text{m/s}$ over the first $4.0\,\text{s}$ after the start. What is the car's displacement in those $4.0\,\text{s}$?
  options:
    A: |-
      $120\,\text{m}$
    B: |-
      $7.5\,\text{m}$
    C: |-
      $60\,\text{m}$
    D: |-
      It cannot be found, because a velocity–time graph shows no positions.
  answer: C
  explanation: |-
    Displacement is the area under the $v$–$t$ graph. Here the area is a triangle: $\tfrac{1}{2} \times 4.0\,\text{s} \times 30\,\text{m/s} = 60\,\text{m}$.
  misconceptions:
    A: |-
      Multiplies the final velocity by the time, $30 \times 4.0$, as if the car had done $30\,\text{m/s}$ from the start. That is the area of the rectangle, not of the triangle under the line.
    B: |-
      Works out the slope, $30/4.0 = 7.5$ — which is the acceleration in $\text{m/s}^2$ — and reads it as a displacement. The slope and the area of a $v$–$t$ graph give different quantities.
    D: |-
      Thinks a $v$–$t$ graph says nothing about position. The area under it gives the displacement, even though no position is plotted.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a monitor shows a side-scrolling game whose runner moves along a straight track marked like a number line, with a position and velocity readout; a tablet replays a velocity-time graph](scenes/gaming/motion_straight_line.svg "The tablet on the right shows a velocity replay: a climb, a flat top and a drop. There's more in that shape than it looks.")

Tanish is stuck on a puzzle room. His character has to dash from a doorway to a pressure switch on the floor before a gate slams shut, and every time, the dash ends and the switch doesn't click. The switch, the level editor says, is $18\,\text{m}$ from the doorway.

He wrote a little logging mod last month to study movement, but it has a bug: the position column is blank. Only the velocity column works. He plots it anyway: a line climbing to $7\,\text{m/s}$, a short flat top, then a steep drop to zero as the dash ends.

His friend Priyanka, on a video call, isn't hopeful. "You want to know how far the dash goes. There's not a single distance on that graph."

Tanish keeps staring at it. The graph is a shape — a slope here, a flat bit there, a region underneath it. It feels as if the answer should be hiding in the shape somewhere.

Can you get the acceleration *and* the distance out of a graph that shows only velocity?

## The physics

Two graphs describe straight-line motion, and each carries information in its **slope**:

- **Position–time ($x$–$t$) graph:** the slope at any point is the **velocity** there, $v = dx/dt$. A straight segment means constant velocity; a curve bending upwards means the velocity is increasing; a flat part means the object is at rest.
- **Velocity–time ($v$–$t$) graph:** the slope is the **acceleration**, $a = dv/dt$.

The $v$–$t$ graph also carries information in its **area**. The area between the graph and the time axis, from $t_1$ to $t_2$, equals the **displacement** in that interval. Why? Over a short time $\Delta t$, the displacement is $v\,\Delta t$ — a thin strip of height $v$ and width $\Delta t$. Adding all the strips gives the area. (A game engine does exactly this every frame: it moves each object by $v\,\Delta t$, with $\Delta t$ commonly $\tfrac{1}{60}\,\text{s}$.) Area below the time axis counts as negative displacement.

![Two graphs of the same run. Left: position rising along a curve, then a straight section, then levelling off at 17.5 m. Right: velocity rising to 7 m/s over 2 s, flat for 1 s, then falling to zero at 4 s, with areas 7 m, 7 m and 3.5 m marked](figures/motion_graphs/xt-and-vt-pair.svg "Same dash, two views. The slope of the left graph is the height of the right graph; the area under the right graph is the height the left graph reaches.")

## Worked example

**Given:** Tanish's $v$–$t$ graph (illustrative): from $0$ to $7\,\text{m/s}$ in the first $2.0\,\text{s}$, steady at $7\,\text{m/s}$ until $3.0\,\text{s}$, then down to $0$ at $4.0\,\text{s}$.
**Find:** the acceleration in each phase and how far the dash goes.

**Slopes (acceleration):**

$$a_1 = \frac{7 - 0}{2.0} = +3.5\,\text{m/s}^2, \quad a_2 = \frac{7 - 7}{1.0} = 0, \quad a_3 = \frac{0 - 7}{1.0} = -7.0\,\text{m/s}^2$$

The dash stops twice as sharply as it starts.

**Areas (displacement):**

$$\text{triangle} = \tfrac{1}{2}(2.0)(7) = 7.0\,\text{m}, \quad \text{rectangle} = (1.0)(7) = 7.0\,\text{m}, \quad \text{triangle} = \tfrac{1}{2}(1.0)(7) = 3.5\,\text{m}$$

$$\Delta x = 7.0 + 7.0 + 3.5 = 17.5\,\text{m}$$

The velocity never goes negative, so the distance is also $17.5\,\text{m}$ — half a metre short of the switch at $18\,\text{m}$. Tanish needs to start the dash from a little further in, or find a move that keeps the top speed longer.

**Sanity check:** on the $x$–$t$ graph, the straight middle section climbs from $7\,\text{m}$ to $14\,\text{m}$ in $1\,\text{s}$ — a slope of $7\,\text{m/s}$, matching the flat top of the $v$–$t$ graph. And it levels off at $17.5\,\text{m}$, matching the total area.

## Where the picture breaks

A logger records velocity once per frame, not continuously, so the smooth lines are an idealisation of a staircase of samples; the area from samples is a very good estimate, not an exact value. The area gives displacement measured from wherever the dash began — the graph alone can't say *where* that was, so you need one known position (the doorway) to turn it into a position. And if the velocity had dipped below zero (the character turned back), that area would subtract: then displacement and distance would differ.

## Key takeaway

On an $x$–$t$ graph, slope $=$ velocity. On a $v$–$t$ graph, slope $=$ acceleration and area under the graph $=$ displacement. So a graph with no distance on it still tells you how far the dash went: add up the areas.
