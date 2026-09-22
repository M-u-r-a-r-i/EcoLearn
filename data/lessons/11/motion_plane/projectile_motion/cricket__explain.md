---
concept_id: projectile_motion
interest: cricket
format: explain
title: The bowling machine bet in the nets
check:
  question: |-
    From the same height, one ball is dropped and another is fired horizontally at $20\,\text{m/s}$, at the same instant. Ignoring air resistance, which statement is correct?
  options:
    A: |-
      The fired ball lands later, because it travels along a longer path.
    B: |-
      The fired ball lands first, because it is moving much faster.
    C: |-
      The dropped ball lands first, because the fired ball's forward speed helps hold it up.
    D: |-
      Both land together, because the horizontal velocity does not change the vertical motion.
  answer: D
  explanation: |-
    Both balls start with zero vertical velocity and have the same vertical acceleration $g$, so they fall the same height in the same time. The fired ball's horizontal velocity only carries it sideways.
  misconceptions:
    A: |-
      Assumes a longer path must take longer. The time to land is set by the vertical motion alone, which is identical for both.
    B: |-
      Mixes up speed along the path with speed downwards. The extra speed is all horizontal, so it doesn't help the ball reach the ground.
    C: |-
      Thinks forward motion creates an upward "holding" effect. With air resistance ignored, nothing acts on a projectile except gravity, straight down.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A day match: a batter lofts the ball in a high arc towards the boundary as a fielder races along the rope](scenes/cricket/motion_plane.svg "Every ball in the air, from a lofted drive to a throw, follows the same kind of curved path.")

It's the last session of the under-16 camp, and Coach Rehana has a bet for the squad.

She has set the bowling machine to fire a ball perfectly level, from the height of its mouth. On top of the machine sits a second ball. She has rigged a small lever so that the button also knocks that ball off. "When I press this," she says, "one ball flies straight out down the net and the other just drops, at the same moment. Which hits the ground first?"

Kabir answers at once. "The dropped one. The fired one has to go all the way down the pitch." Half the squad agrees. A few say the fired ball, since it's so fast. Nobody picks a tie.

Rehana props up a phone to film in slow motion and presses the button.

Who wins the bet, and why?

## The physics

A **projectile** is an object that, once launched, moves under gravity alone. That means we ignore air resistance. The only force is its weight, straight down, so its acceleration is $\vec{a} = -g\hat{j}$, constant, with $g = 9.8\,\text{m/s}^2$ and $\hat{j}$ pointing up.

Because the acceleration is constant, the equations from the previous lesson apply, and they split into two **independent** motions:

- **Horizontal ($x$):** no force, so $a_x = 0$. The horizontal velocity never changes: $v_x = u_x$ and $x = u_x t$. Uniform velocity.
- **Vertical ($y$):** $a_y = -g$. So $v_y = u_y - gt$ and $y = u_y t - \tfrac{1}{2}gt^2$. Uniform acceleration, exactly as for a dropped ball.

For a ball launched at speed $u$ at angle $\theta$ above the horizontal, $u_x = u\cos\theta$ and $u_y = u\sin\theta$. For the bowling machine, fired level, $\theta = 0$: so $u_x = u$ and $u_y = 0$.

That settles the bet. Both balls start with **zero vertical velocity** and have the **same vertical acceleration**. Their vertical motions are identical, so they fall the same height in the same time and **land together**. The fired ball's horizontal velocity only carries it sideways while it falls. Nothing in the $y$ equations depends on $u_x$.

![Strobe picture: a dropped grey ball and a red ball launched horizontally. At each flash they are at the same height; the red ball moves equal steps sideways while its downward velocity grows](figures/projectile_motion/horizontal-vs-dropped.svg "At every flash both balls are at the same height. The red ball's horizontal velocity stays the same; only its vertical velocity grows.")

Put together, the horizontal motion stays steady while the vertical motion speeds up, and the path is a curve. It is in fact a parabola, as you'll see in the next lesson.

## Worked example

**Given (illustrative):** the machine fires the ball horizontally at $u = 30\,\text{m/s}$ from a height $h = 2.0\,\text{m}$. Take $g = 9.8\,\text{m/s}^2$ and ignore air resistance.
**Find:** the time to reach the ground, how far along the pitch it lands, and its velocity on landing.

Vertical motion alone gives the time. With $u_y = 0$, falling $2.0\,\text{m}$:
$$h = \tfrac{1}{2}gt^2 \;\Rightarrow\; t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{2 \times 2.0}{9.8}} = \sqrt{0.408} \approx 0.64\,\text{s}$$

Horizontal motion, at constant velocity for that time:
$$x = u_x t = 30 \times 0.639 \approx 19\,\text{m}$$

Velocity on landing: $v_x = 30\,\text{m/s}$ (unchanged) and $v_y = -gt = -9.8 \times 0.639 \approx -6.3\,\text{m/s}$. So
$$v = \sqrt{30^2 + 6.3^2} \approx 30.7\,\text{m/s}, \quad \text{at } \tan^{-1}\!\left(\frac{6.3}{30}\right) \approx 12^\circ \text{ below the horizontal}$$

The dropped ball also lands after $0.64\,\text{s}$, right below the machine.

**Sanity check:** $19\,\text{m}$ is just short of the $20.12\,\text{m}$ pitch, so a level ball would bounce near the far end. In practice the machine's angle is adjusted to choose where the ball pitches. The landing speed is only slightly more than $30\,\text{m/s}$, because a $0.64\,\text{s}$ fall adds only a small vertical part.

## Where the picture breaks

Air resistance isn't zero. At $30\,\text{m/s}$ drag noticeably slows a cricket ball's horizontal motion, and the ball lands a little short of the ideal $19\,\text{m}$. Drag points backwards along the path, and once the fast ball's path tilts downwards, part of that drag pushes slightly upwards. So in a real net the fired ball lands a tiny fraction later, perhaps a hundredth of a second or two, far too little to see without slow motion. The slow dropped ball is barely affected by drag. Spin and swing can add sideways or vertical forces that the model leaves out.

## Key takeaway

Projectile motion is two independent motions sharing one clock: steady horizontal velocity ($a_x = 0$) and uniformly accelerated vertical motion ($a_y = -g$). The time in the air is set by the vertical motion alone. That's why a ball fired sideways and a ball dropped from the same height land together.
