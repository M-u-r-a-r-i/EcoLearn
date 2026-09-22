---
concept_id: vertical_circle_motion
interest: cricket
format: explain
title: Whirling the hanging practice ball over your head
check:
  question: |-
    A practice ball in a sock is whirled in a vertical circle on a rope, with its centre $0.40\,\text{m}$ from the hand (treat the hand as fixed). Taking $g = 9.8\,\text{m/s}^2$, what is the minimum speed at the top of the circle that keeps the rope taut?
  options:
    A: |-
      $0\,\text{m/s}$
    B: |-
      $4.4\,\text{m/s}$
    C: |-
      $3.9\,\text{m/s}$
    D: |-
      $2.0\,\text{m/s}$
  answer: D
  explanation: |-
    At the top, $T + mg = mv^2/r$. The rope stays taut as long as $T \ge 0$, so $v^2 \ge gr$ and $v_\text{min} = \sqrt{gr} = \sqrt{9.8 \times 0.40} = \sqrt{3.92} \approx 2.0\,\text{m/s}$.
  misconceptions:
    A: |-
      Thinks the ball just has to reach the top, even with zero speed; a rope can only pull, so with no speed gravity alone would pull the ball inside the circle and the rope would go slack. (Zero speed at the top is possible only for a rigid rod.)
    B: |-
      Uses the bottom-of-the-circle condition $\sqrt{5gr}$ for the top; that is the minimum speed needed at the bottom to arrive at the top with $\sqrt{gr}$.
    C: |-
      Finds $gr = 3.92$ and forgets to take the square root, so the "speed" comes out with units of $\text{m}^2/\text{s}^2$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground by day: a batter watches a ball climb high, a fielder waits under it, a player runs up the stadium steps and a groundsman pushes a roller](scenes/cricket/work_energy_power.svg "Balls on this ground fly in arcs. On a rope, a ball can be made to fly in a full circle.")

Dev practises his batting every evening in the courtyard, with an old cricket ball tied inside a sock and hung from a rope on a hook. He swings at it, it flies round, and he hits it again — a drill as old as the game.

Today his little brother Yusuf unhooks the rope and tries something else. He grips the end and whirls the ball in a big vertical circle beside him, like a windmill.

At first he goes too slowly. Each time the ball nears the top, the rope goes limp, and the ball flops inwards and drops before the rope snaps tight again. Faster, and the circle suddenly becomes smooth, with the rope taut all the way round.

"There's a magic speed," Yusuf announces. Dev thinks there might be two: one needed at the top, and a bigger one at the bottom. What are they, and why are they different?

## The physics

Motion in a vertical circle is **non-uniform** circular motion. Gravity slows the ball on the way up and speeds it up on the way down. But at every point, the net force towards the centre must supply the centripetal force $mv^2/r$.

![A mass on a string at the top, side and bottom of a vertical circle, with tension and weight drawn at each point, and the conditions for the minimum speeds at the top and bottom](figures/vertical_circle_motion/forces-top-bottom-side.svg "At the top, tension and weight both point to the centre. At the bottom they point opposite ways, so the tension there must be large.")

**At the top.** The tension $T$ and the weight $mg$ both point down, towards the centre:

$$T_\text{top} + mg = \frac{mv_\text{top}^2}{r}$$

A rope can pull but never push, so $T \ge 0$. The slowest case is $T = 0$, when gravity alone provides the centripetal force:

$$v_\text{top} \ge \sqrt{gr}$$

Any slower, and gravity pulls the ball inside the circle faster than the circle curves. The rope goes slack — exactly what Yusuf saw.

**Top to bottom.** The tension is always perpendicular to the velocity, so it does no work. Only gravity does work, and mechanical energy is conserved. The bottom is $2r$ below the top:

$$\tfrac{1}{2}mv_\text{bottom}^2 = \tfrac{1}{2}mv_\text{top}^2 + mg(2r) \quad\Rightarrow\quad v_\text{bottom}^2 = v_\text{top}^2 + 4gr$$

With the smallest allowed $v_\text{top}^2 = gr$:

$$v_\text{bottom} \ge \sqrt{5gr}$$

**At the bottom**, tension points up (towards the centre) and weight points down: $T_\text{bottom} - mg = mv_\text{bottom}^2/r$. At the minimum speeds, $T_\text{bottom} = mg + 5mg = 6mg$.

If the ball were on a rigid rod instead of a rope, the rod could push, so the ball could crawl over the top at nearly zero speed. Then $v_\text{bottom} \ge \sqrt{4gr}$.

## Worked example

**Given** (illustrative): rope length to the ball's centre $r = 0.80\,\text{m}$; ball and sock $m = 0.16\,\text{kg}$; $g = 9.8\,\text{m/s}^2$; Yusuf's hand held still.
**Find:** the minimum speeds at the top and bottom, and the tension at the bottom in that case.

$$v_\text{top} = \sqrt{gr} = \sqrt{9.8 \times 0.80} = \sqrt{7.84} = 2.8\,\text{m/s}$$

$$v_\text{bottom} = \sqrt{5gr} = \sqrt{39.2} \approx 6.3\,\text{m/s}$$

$$T_\text{bottom} = m\left(g + \frac{v_\text{bottom}^2}{r}\right) = 0.16\left(9.8 + \frac{39.2}{0.80}\right) = 0.16 \times 58.8 \approx 9.4\,\text{N}$$

**Sanity check:** $6mg = 6 \times 0.16 \times 9.8 \approx 9.4\,\text{N}$ — matches. And the energy check: $6.26^2 - 2.8^2 = 39.2 - 7.84 = 31.4 = 4gr$. Yusuf needs the ball moving at about $6.3\,\text{m/s}$ at the bottom, and his hand feels six times the ball's weight there.

## Where the picture breaks

Yusuf's hand isn't a fixed pivot. He moves it in a small circle and keeps feeding energy in, which is how he keeps the ball going at all. Air drag on the sock takes energy out every lap, so the real ball needs a little more than $\sqrt{5gr}$ at the bottom. The rope also stretches slightly and has its own mass, and the sock-wrapped ball isn't a point. The two conditions — $T \ge 0$ at the top, energy conservation from top to bottom — are the core, and they hold for anything on a string.

## Key takeaway

In a vertical circle on a string, the net force towards the centre must equal $mv^2/r$ at every point, and the string can only pull. So the speed at the top must be at least $\sqrt{gr}$. Energy conservation over the drop of $2r$ then requires at least $\sqrt{5gr}$ at the bottom, where the tension is largest.
