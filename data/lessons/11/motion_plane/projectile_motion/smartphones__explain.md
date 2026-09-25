---
concept_id: projectile_motion
interest: smartphones
format: explain
title: The earbud case race off the desk
check:
  question: |-
    Two phones slide off the edge of the same level table at the same instant, one at $1\,\text{m/s}$ and the other at $3\,\text{m/s}$. Ignoring air resistance, which statement is correct?
  options:
    A: |-
      The faster phone reaches the floor first, because it is moving faster.
    B: |-
      The faster phone takes three times as long to land, because it travels three times as far.
    C: |-
      The slower phone lands first, because the faster phone's sideways speed helps hold it up.
    D: |-
      They land at the same time, and the faster phone lands three times as far from the table.
  answer: D
  explanation: |-
    Both leave with zero vertical velocity and fall with the same acceleration $g$, so they take the same time to fall the table's height. In that time each moves sideways at its own constant speed, so the faster one goes three times as far.
  misconceptions:
    A: |-
      Mixes up speed along the path with speed downwards. The extra speed is all horizontal, so it doesn't help the phone reach the floor sooner.
    B: |-
      Assumes a longer path must take longer. The time in the air is set by the vertical motion alone, which is the same for both.
    C: |-
      Thinks forward motion creates an upward "holding" effect. Ignoring air, the only force on either phone is gravity, straight down.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![An evening terrace: an earbud case skids off the edge of a table and follows a dashed curve to the floor, with a blue arrow for its velocity along the table and a green arrow for g](scenes/smartphones/motion_plane.svg "The earbud case leaves the table moving sideways, then curves down to the floor. The drop and the sideways drift happen at the same time.")

Tarun and his cousin Meher are arguing over two identical earbud cases on the edge of the study table.

"If I flick one off the edge," says Tarun, "and just let go of the other one at the same instant, the flicked one stays up longer. It's got to travel all that way across the room."

"No," says Meher, "it's going faster, so it gets down faster."

To settle it, Meher props her phone against a book and sets it to slow-motion video. Tarun holds one case just beyond the edge, level with the table top, ready to let go. With his other hand he gets ready to flick the second case off the edge.

Meher presses record. Tarun counts "three, two, one", lets go and flicks. Two cases, one table, one moment. Which one hits the floor first, and why?

## The physics

A **projectile** is an object moving under gravity alone once it is launched, which means we ignore air resistance. Its only force is its weight, so its acceleration is $\vec{a} = -g\hat{j}$, constant, with $g = 9.8\,\text{m/s}^2$ and $\hat{j}$ pointing up.

Because the acceleration is constant, the motion splits into two **independent** motions:

- **Horizontal ($x$):** no force, so $a_x = 0$. The horizontal velocity never changes: $v_x = u_x$ and $x = u_x t$.
- **Vertical ($y$):** $a_y = -g$. So $v_y = u_y - gt$ and $y = u_y t - \tfrac{1}{2}gt^2$, exactly as for something dropped or thrown straight up.

For a launch at speed $u$ at angle $\theta$ above the horizontal, $u_x = u\cos\theta$ and $u_y = u\sin\theta$. The flicked case leaves the table level, so $\theta = 0$: $u_x = u$ and $u_y = 0$.

That settles the argument. Both cases start with **zero vertical velocity** and have the **same vertical acceleration**. Their vertical motions are identical, so they fall the table's height in the same time and **land together**. The flicked case's horizontal speed only carries it sideways while it falls; nothing in the $y$ equations contains $u_x$.

![Strobe picture: a dropped grey ball and a red ball launched horizontally. At each flash they are at the same height; the red ball moves equal steps sideways](figures/projectile_motion/horizontal-vs-dropped.svg "At every flash both objects are at the same height. The launched one's sideways steps stay equal; only its downward speed grows, just like the dropped one's.")

A steady sideways motion combined with a speeding-up downward motion gives a curved path: a parabola, as the next lesson shows.

## Worked example

**Given (illustrative):** the flicked case leaves the table edge horizontally at $u = 2.0\,\text{m/s}$ from a height $h = 0.80\,\text{m}$. Take $g = 9.8\,\text{m/s}^2$ and ignore air resistance.
**Find:** how long it falls, how far from the table it lands, and its downward speed on landing.

1. **Time**, from the vertical motion alone (starting with $u_y = 0$):
$$h = \tfrac{1}{2}gt^2 \;\Rightarrow\; t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{2 \times 0.80}{9.8}} \approx 0.40\,\text{s}$$
   Less than half a second, the same for the case Tarun simply let go of.
2. **Distance from the table**, at steady horizontal speed: $x = u t = 2.0 \times 0.40 \approx 0.81\,\text{m}$, about one long stride.
3. **Downward speed on landing:** $v_y = g t = 9.8 \times 0.40 \approx 4.0\,\text{m/s}$, while the sideways speed is still $2.0\,\text{m/s}$.

**Sanity check:** the case hits the floor moving downward about twice as fast as sideways, which is why the curve looks steep near the floor in the slow-motion video.

## Where the picture breaks

A sliding case isn't a perfect projectile. As it leaves the edge it can catch on the table and start to tumble, and a light object with a large surface feels air resistance, which slows its sideways motion a little. At these low speeds the effect is tiny: both cases land together to within what a phone's slow-motion video can tell apart. And no hand lets go and flicks at exactly the same instant: a real test is only as fair as Tarun's timing, which is why the slow-motion video matters.

## Key takeaway

Projectile motion is two independent motions sharing one clock: steady horizontal velocity ($a_x = 0$) and uniformly accelerated vertical motion ($a_y = -g$). The time in the air depends only on the vertical motion, so something launched sideways and something dropped from the same height land together.
