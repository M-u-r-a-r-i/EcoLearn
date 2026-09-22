---
concept_id: motion_graphs
interest: football
format: explain
title: Was the keeper outside his box, from a graph with no positions
check:
  question: |-
    A striker's velocity–time graph is a straight line rising from $0$ to $8\,\text{m/s}$ over the first $2.5\,\text{s}$ of a run onto a through ball. What is her displacement in those $2.5\,\text{s}$?
  options:
    A: |-
      $10\,\text{m}$
    B: |-
      $20\,\text{m}$
    C: |-
      $3.2\,\text{m}$
    D: |-
      It cannot be found, because a velocity–time graph shows no positions.
  answer: A
  explanation: |-
    Displacement is the area under the $v$–$t$ graph. Here that is a triangle: $\tfrac{1}{2} \times 2.5\,\text{s} \times 8\,\text{m/s} = 10\,\text{m}$.
  misconceptions:
    B: |-
      Multiplies the final velocity by the time, $8 \times 2.5$, as if she ran at $8\,\text{m/s}$ the whole time. That is the rectangle's area, not the triangle's under the line.
    C: |-
      Works out the slope, $8/2.5 = 3.2$ — which is the acceleration in $\text{m/s}^2$ — and reads it as a displacement. Slope and area of a $v$–$t$ graph give different quantities.
    D: |-
      Thinks a $v$–$t$ graph cannot tell you about position. The area under it gives the displacement, even though no position is plotted.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A winger dribbles along the touchline towards goal, chased by a defender, while the goalkeeper comes off the line; a number line with origin O and +x runs beneath](scenes/football/motion_straight_line.svg "A keeper rushing off his line moves along one straight line: out from the goal.")

The ball is played in behind the defence, and Aman, the goalkeeper, charges straight off his goal line to meet it. He sprints, reaches full speed, brakes, and smothers the ball with both hands at the feet of the striker.

The other team's bench erupts. "He's out of the box! Handball!" A goalkeeper may handle the ball only inside his own penalty area, which reaches $16.5\,\text{m}$ out from the goal line. The referee waves play on.

After the match, Nandini, who helps the team's analyst, pulls up the footage — and a steward's back blocks the camera at exactly the wrong moment. All that survives is Aman's vest sensor, which records only one thing: his velocity, moment by moment.

"No positions at all," the analyst sighs. "So we'll never know."

Nandini looks at the plot: a line rising to $7\,\text{m/s}$, a short flat top, a steep drop to zero. Surely the shape is hiding something.

Can a graph of velocity alone tell you how far Aman ran — and so where he stopped?

## The physics

Two graphs describe straight-line motion, and each carries information in its **slope**:

- **Position–time ($x$–$t$) graph:** the slope at any point is the **velocity** there, $v = dx/dt$. A straight segment means constant velocity; a curve bending upwards means increasing velocity; a flat part means the object is at rest.
- **Velocity–time ($v$–$t$) graph:** the slope is the **acceleration**, $a = dv/dt$.

The $v$–$t$ graph also carries information in its **area**. The area between the graph and the time axis, from $t_1$ to $t_2$, equals the **displacement** in that interval. Why? In a short time $\Delta t$ the displacement is $v\,\Delta t$ — a thin strip of height $v$ and width $\Delta t$. Adding all the strips gives the area. Area below the time axis counts as negative displacement.

![Two graphs of the same run. Left: position rising along a curve, then a straight section, then levelling off at 17.5 m. Right: velocity rising to 7 m/s over 2 s, flat for 1 s, then falling to zero at 4 s, with areas 7 m, 7 m and 3.5 m marked](figures/motion_graphs/xt-and-vt-pair.svg "Same run, two views. The slope of the left graph is the height of the right graph; the area under the right graph is the height the left graph reaches.")

## Worked example

**Given:** Aman's $v$–$t$ graph (illustrative): from $0$ to $7\,\text{m/s}$ in the first $2.0\,\text{s}$, steady at $7\,\text{m/s}$ until $3.0\,\text{s}$, then down to $0$ at $4.0\,\text{s}$. He started on his goal line; positive is straight out from the goal.
**Find:** his acceleration in each phase, and where he stopped.

**Slopes (acceleration):**

$$a_1 = \frac{7 - 0}{2.0} = +3.5\,\text{m/s}^2, \quad a_2 = \frac{7 - 7}{1.0} = 0, \quad a_3 = \frac{0 - 7}{1.0} = -7.0\,\text{m/s}^2$$

He braked twice as hard as he accelerated.

**Areas (displacement):**

$$\text{triangle} = \tfrac{1}{2}(2.0)(7) = 7.0\,\text{m}, \quad \text{rectangle} = (1.0)(7) = 7.0\,\text{m}, \quad \text{triangle} = \tfrac{1}{2}(1.0)(7) = 3.5\,\text{m}$$

$$\Delta x = 7.0 + 7.0 + 3.5 = 17.5\,\text{m}$$

Starting from the goal line, he stopped $17.5\,\text{m}$ out — about a metre beyond the $16.5\,\text{m}$ line. The bench had a case.

**Sanity check:** on the $x$–$t$ graph, the straight middle section climbs from $7\,\text{m}$ to $14\,\text{m}$ in $1\,\text{s}$ — a slope of $7\,\text{m/s}$, matching the flat top of the $v$–$t$ graph. It levels off at $17.5\,\text{m}$, matching the total area.

## Where the picture breaks

The sensor samples velocity at intervals, so straight lines and sharp corners idealise a smooth, wobbly real curve; areas from them are estimates, and an error of a metre is easily possible — too much to settle a one-metre decision on its own. The vest tracks one point on Aman's back, while the law asks where the ball was when he handled it; his arms reach well in front of his body. And the area gives displacement only: you need one known position (here, his goal line) to turn it into where he ended up.

## Key takeaway

On an $x$–$t$ graph, slope $=$ velocity. On a $v$–$t$ graph, slope $=$ acceleration and area under the graph $=$ displacement. So a graph with no positions on it can still tell you how far the keeper came: add up the areas.
