---
concept_id: projectile_motion
interest: football
format: explain
title: Two balls off the terrace wall, and which lands first
check:
  question: |-
    A ball rolls off the edge of a high terrace at $6.0\,\text{m/s}$, moving horizontally. Ignoring air resistance, what is its horizontal velocity halfway through its fall?
  options:
    A: |-
      Still $6.0\,\text{m/s}$, because nothing acts on it horizontally
    B: |-
      Less than $6.0\,\text{m/s}$, because gravity is slowing it down
    C: |-
      More than $6.0\,\text{m/s}$, because it is speeding up as it falls
    D: |-
      Zero, because once it starts to fall it stops moving forwards
  answer: A
  explanation: |-
    With air resistance ignored, the only force is gravity, which acts straight down. So $a_x = 0$ and the horizontal velocity stays $6.0\,\text{m/s}$; only the vertical velocity grows.
  misconceptions:
    B: |-
      Thinks gravity acts against the whole motion. Gravity pulls vertically, so it cannot change the horizontal part of the velocity.
    C: |-
      Mixes up the speed along the path, which does increase, with its horizontal part. All the extra speed is vertical.
    D: |-
      Believes a moving object runs out of forward motion and then drops straight down, like a cartoon character off a cliff. The horizontal motion carries on unchanged.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A player lofts the ball in an arc over the goalkeeper while a teammate jogs round the centre circle](scenes/football/motion_plane.svg "Every ball in the air, from a lofted pass to a lob over the keeper, follows the same kind of curved path.")

Joel's school is in a hill town, and its practice pitch sits on a terrace, with a stone wall dropping to the main ground below. Balls go over that wall all the time.

At the end of training, Joel and Tsering are sent to fetch two strays, and they decide to send the balls down the quick way. Joel whacks his along the flat top of the terrace so it shoots off the edge. Tsering just nudges hers, so it trickles off. By luck, both leave the edge at exactly the same moment.

"Mine will hit the ground first," says Joel. "It's going much faster."

"No way," says Tsering. "Yours has to travel much further out. Mine drops almost straight down. Mine wins."

Their coach, Ms Bora, is watching from the ground below. "Neither of you," she calls up.

What does she mean, and how can a fast ball and a slow ball take the same time to fall?

## The physics

A **projectile** is an object that, once launched, moves under gravity alone, so we ignore air resistance. The only force is its weight, straight down. Its acceleration is $\vec{a} = -g\hat{j}$, constant, with $g = 9.8\,\text{m/s}^2$ and $\hat{j}$ pointing up.

Because the acceleration is constant, the equations for motion in a plane apply, and they split into two **independent** motions:

- **Horizontal ($x$):** no force, so $a_x = 0$. The horizontal velocity never changes: $v_x = u_x$ and $x = u_x t$. Uniform velocity.
- **Vertical ($y$):** $a_y = -g$. So $v_y = u_y - gt$ and $y = u_y t - \tfrac{1}{2}gt^2$. Uniform acceleration, exactly as for a dropped ball.

For a launch at speed $u$ and angle $\theta$ above the horizontal, $u_x = u\cos\theta$ and $u_y = u\sin\theta$. A ball rolling off a flat edge leaves horizontally, $\theta = 0$, so $u_x = u$ and $u_y = 0$.

That answers Ms Bora's riddle. Both balls leave with **zero vertical velocity** and have the **same vertical acceleration**, and nothing in the $y$ equations depends on $u_x$. Their vertical motions are identical, so they fall the same height in the same time and **land together**. Joel's bigger horizontal velocity only carries his ball further out while it falls.

![Strobe picture: a dropped grey ball and a red ball launched horizontally. At each flash they are at the same height; the red ball moves equal steps sideways while its downward velocity grows](figures/projectile_motion/horizontal-vs-dropped.svg "At every flash both balls are at the same height. The launched ball moves equal steps sideways, while its vertical velocity grows exactly like the dropped ball's.")

Steady horizontal motion plus speeding-up vertical motion makes a curved path, which you'll show is a parabola in the next lesson.

## Worked example

**Given (illustrative):** the wall is $h = 4.9\,\text{m}$ high. Joel's ball leaves the edge horizontally at $8.0\,\text{m/s}$; Tsering's at $1.0\,\text{m/s}$. Take $g = 9.8\,\text{m/s}^2$ and ignore air resistance.
**Find:** the time each takes to land, how far from the wall each lands, and Joel's ball's velocity as it lands.

Vertical motion alone gives the time. With $u_y = 0$:
$$h = \tfrac{1}{2}gt^2 \;\Rightarrow\; t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{2 \times 4.9}{9.8}} = \sqrt{1.0} = 1.0\,\text{s}$$

The same $1.0\,\text{s}$ for both balls. Horizontal motion at constant velocity for that time:
$$x_\text{Joel} = 8.0 \times 1.0 = 8.0\,\text{m}, \qquad x_\text{Tsering} = 1.0 \times 1.0 = 1.0\,\text{m}$$

Joel's ball on landing: $v_x = 8.0\,\text{m/s}$ (unchanged) and $v_y = -gt = -9.8\,\text{m/s}$. So
$$v = \sqrt{8.0^2 + 9.8^2} = \sqrt{64 + 96.04} \approx 12.7\,\text{m/s}, \quad \text{at } \tan^{-1}\!\left(\frac{9.8}{8.0}\right) \approx 51^\circ \text{ below the horizontal}$$

**Sanity check:** reverse it: in $1.0\,\text{s}$ from rest, a falling ball covers $\tfrac{1}{2}(9.8)(1.0)^2 = 4.9\,\text{m}$, the height of the wall. The landing speed is more than $8.0\,\text{m/s}$, as it must be, because gravity has added a vertical part.

## Where the picture breaks

Air resistance isn't zero. It slows Joel's faster ball more, so it lands a little short of $8.0\,\text{m}$, and it also lands a tiny fraction of a second later, because once its path tilts downwards, part of the drag pushes slightly up. The difference is far too small to notice by eye. A spinning ball can also feel a sideways or upward push. And a ball bouncing along the terrace may leave the edge slightly upwards or downwards rather than perfectly level, which changes $u_y$.

## Key takeaway

Projectile motion is two independent motions sharing one clock: steady horizontal velocity ($a_x = 0$) and uniformly accelerated vertical motion ($a_y = -g$). The time in the air is set by the vertical motion alone. That is why a fast ball and a slow ball leaving a ledge horizontally land at the same moment, just at different distances.
