---
concept_id: vertical_circle_motion
interest: football
format: explain
title: Heading the hanging ball right over the bar
check:
  question: |-
    A heading-practice ball hangs on a cord, with its centre $0.50\,\text{m}$ below the point where the cord is tied. Taking $g = 9.8\,\text{m/s}^2$, what is the minimum speed the ball needs at the bottom to go all the way round a vertical circle with the cord taut?
  options:
    A: |-
      $2.2\,\text{m/s}$
    B: |-
      $4.4\,\text{m/s}$
    C: |-
      $4.9\,\text{m/s}$
    D: |-
      $24.5\,\text{m/s}$
  answer: C
  explanation: |-
    At the top the cord stays taut only if $v_\text{top} \ge \sqrt{gr}$. Energy conservation over the drop of $2r$ then needs $v_\text{bottom}^2 \ge gr + 4gr = 5gr$, so $v_\text{bottom} \ge \sqrt{5 \times 9.8 \times 0.50} = \sqrt{24.5} \approx 4.9\,\text{m/s}$.
  misconceptions:
    A: |-
      Uses the top-of-the-circle condition $\sqrt{gr}$ for the bottom; the ball slows as it climbs $2r$, so it needs much more speed at the bottom.
    B: |-
      Uses $\sqrt{4gr}$, which assumes the ball may crawl over the top at almost zero speed; that works for a rigid rod that can push, but a cord goes slack unless $v_\text{top} \ge \sqrt{gr}$.
    D: |-
      Finds $5gr = 24.5$ and forgets to take the square root, so the "speed" really has units of $\text{m}^2/\text{s}^2$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A football training ground by day: a player drags a weighted sled on a strap, a striker lofts the ball in a high arc, and the goalkeeper dives to catch it](scenes/football/work_energy_power.svg "Balls fly in arcs all over this ground. Tied to a cord, a ball can be made to fly in a full circle.")

After training, Sana ties the team's heading ball, a ball in a mesh bag on a strong cord, to the high steel bar of the academy's heading frame. It hangs at head height, with nothing around it but air, and she practises meeting it with her forehead, over and over.

Vikram, waiting for his turn, has a better idea. "Head it hard enough and it'll swing right up and over the bar. A full loop."

Sana tries. The ball flies up and round, higher than the bar, then the cord suddenly goes limp. The ball drops inside the circle and flops back down, and the cord snaps tight again with a jerk. She tries harder, with the same result.

"There's a speed you need," Vikram says, "and you're just short of it."

Sana thinks there are really two speeds hiding here: one the ball must still have at the very top, over the bar, and a bigger one it must start with at the bottom. What are they, and why are they different?

## The physics

Motion in a vertical circle is **non-uniform** circular motion. Gravity slows the ball as it climbs and speeds it up as it falls. But at every point, the net force towards the centre must supply the centripetal force $mv^2/r$.

![A mass on a string at the top, side and bottom of a vertical circle, with tension and weight drawn at each point, and the conditions for the minimum speeds at the top and bottom](figures/vertical_circle_motion/forces-top-bottom-side.svg "At the top, tension and weight both point to the centre. At the bottom they point opposite ways, so the tension there is large.")

**At the top.** The tension $T$ and the weight $mg$ both point down, towards the centre (the bar):

$$T_\text{top} + mg = \frac{mv_\text{top}^2}{r}$$

A cord can pull but never push, so $T \ge 0$. The slowest possible case is $T = 0$, when gravity alone provides the centripetal force:

$$v_\text{top} \ge \sqrt{gr}$$

Any slower, and gravity pulls the ball inwards faster than the circle curves. The cord goes slack, which is exactly what Sana saw.

**Bottom to top.** The tension is always perpendicular to the velocity, so it does no work. Only gravity does work, so mechanical energy is conserved. The top is $2r$ above the bottom:

$$\tfrac{1}{2}mv_\text{bottom}^2 = \tfrac{1}{2}mv_\text{top}^2 + mg(2r) \quad\Rightarrow\quad v_\text{bottom}^2 = v_\text{top}^2 + 4gr$$

With the smallest allowed $v_\text{top}^2 = gr$:

$$v_\text{bottom} \ge \sqrt{5gr}$$

**At the bottom**, the tension points up (towards the centre) and the weight down: $T_\text{bottom} - mg = mv_\text{bottom}^2/r$. At the minimum speeds, $T_\text{bottom} = mg + 5mg = 6mg$.

If the ball were on a rigid rod, the rod could push, so the ball could creep over the top at almost zero speed. Then $v_\text{bottom} \ge \sqrt{4gr}$ would be enough.

## Worked example

**Given** (illustrative): cord length to the ball's centre $r = 0.90\,\text{m}$; ball and bag $m = 0.45\,\text{kg}$; $g = 9.8\,\text{m/s}^2$; Sana's header sends the ball off horizontally from the bottom.
**Find:** the minimum speeds at the top and bottom, and the tension at the bottom in that case.

$$v_\text{top} = \sqrt{gr} = \sqrt{9.8 \times 0.90} = \sqrt{8.82} \approx 3.0\,\text{m/s}$$

$$v_\text{bottom} = \sqrt{5gr} = \sqrt{44.1} \approx 6.6\,\text{m/s}$$

$$T_\text{bottom} = m\left(g + \frac{v_\text{bottom}^2}{r}\right) = 0.45\left(9.8 + \frac{44.1}{0.90}\right) = 0.45 \times 58.8 \approx 26\,\text{N}$$

Suppose Sana's best header gives $5.0\,\text{m/s}$. That is more than the $\sqrt{2gr} \approx 4.2\,\text{m/s}$ needed to rise level with the bar, which is why the ball swung higher than the bar. But it is less than $6.6\,\text{m/s}$, so the cord goes slack somewhere in the upper half of the circle.

**Sanity check:** $6mg = 6 \times 0.45 \times 9.8 \approx 26\,\text{N}$, which matches. The energy check: $44.1 - 8.82 = 35.3 = 4gr$.

## Where the picture breaks

A header isn't an instant horizontal push; the ball is in contact with the head for a moment and may leave slightly upwards. Air drag on the ball and mesh bag takes energy every loop, so the real ball needs a little more than $\sqrt{5gr}$. The cord stretches and has its own mass. And a cord tied round a bar winds around it as the ball loops, so the radius shrinks slightly each time round. The two core conditions, $T \ge 0$ at the top and energy conservation from bottom to top, hold for anything on a cord.

## Key takeaway

In a vertical circle on a cord, the net force towards the centre must equal $mv^2/r$ at every point, and the cord can only pull. So the speed at the top must be at least $\sqrt{gr}$. Energy conservation over the rise of $2r$ then requires at least $\sqrt{5gr}$ at the bottom, where the tension is largest.
