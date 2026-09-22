---
concept_id: projectile_motion
interest: gaming
format: explain
title: The speedrunner who thought sprinting meant hang time
check:
  question: |-
    In a game that uses realistic gravity and no air resistance, two heroes run off the same flat ledge at the same instant: one at $4\,\text{m/s}$, the other at $8\,\text{m/s}$, both moving horizontally. Which statement is correct?
  options:
    A: |-
      Both land at the same time; the faster one lands twice as far out.
    B: |-
      The faster one lands later, because it has further to travel.
    C: |-
      The faster one lands first, because it is moving faster.
    D: |-
      The faster one lands twice as far out and takes twice as long.
  answer: A
  explanation: |-
    Both start with zero vertical velocity and fall with the same acceleration $g$, so the time to fall is the same. Horizontal distance is $x = u_x t$, so doubling $u_x$ doubles the distance for the same $t$.
  misconceptions:
    B: |-
      Assumes a longer path must take longer. The time in the air is set by the vertical motion alone, which is identical for both.
    C: |-
      Mixes up speed along the path with speed downwards. The extra speed is all horizontal, so it doesn't help the hero reach the ground sooner.
    D: |-
      Links time to horizontal speed. Horizontal speed only changes how far the hero goes; the fall time depends on the height and $g$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: the monitor shows an artillery game with a shell flying along a curved arc; a tablet shows a top-down minimap of a circular kart track](scenes/gaming/motion_plane.svg "A shell, a jumping hero, a thrown grenade: anything flying through a game world under gravity follows the same kind of path.")

Manav practises speedruns of an indie platformer that uses realistic gravity. There's a gap near the end of one level with a narrow platform below and to the right of a ledge, and he swears by his technique: sprint off the ledge at full speed.

"If you're fast, you hang in the air longer," he tells his friend Ritika. "That's how you reach the far platform. Walk off slowly and you just drop."

Ritika is a level designer on a school project and has the engine's debug tools open. She sets up a test: two copies of the hero on the same ledge, one sprinting, one walking, both stepping off on the same frame. She switches on frame counting, so every frame the characters spend in the air is logged.

Manav is certain the sprinter will hang in the air for more frames. Ritika presses play.

Does speed really buy you hang time?

## The physics

A **projectile** is an object moving under gravity alone once it is launched, which means we ignore air resistance. The only force is its weight, straight down, so its acceleration is constant: $\vec{a} = -g\hat{j}$, with $g = 9.8\,\text{m/s}^2$ and $\hat{j}$ pointing up.

Constant acceleration means the motion splits into two **independent** parts:

- **Horizontal ($x$):** no force, so $a_x = 0$. The horizontal velocity never changes: $v_x = u_x$ and $x = u_x t$.
- **Vertical ($y$):** $a_y = -g$. So $v_y = u_y - gt$ and $y = u_y t - \tfrac{1}{2}gt^2$, exactly as for a dropped object.

For a launch at speed $u$ and angle $\theta$ above the horizontal, $u_x = u\cos\theta$ and $u_y = u\sin\theta$. Running off a flat ledge is a horizontal launch, $\theta = 0$: so $u_x = u$ and $u_y = 0$.

Now look at Ritika's test. Both heroes start with **zero vertical velocity** and have the **same vertical acceleration**. Their vertical motions are identical, so they spend exactly the same time falling, and land on the same frame. The sprinter's extra speed is all horizontal: it carries him further sideways during the same fall.

![Strobe picture: a dropped grey ball and a red ball launched horizontally. At each flash they are at the same height; the red ball moves equal steps sideways while its downward velocity grows](figures/projectile_motion/horizontal-vs-dropped.svg "At every flash both balls are at the same height. The red ball's horizontal velocity stays the same; only its vertical velocity grows.")

So Manav's technique works, but not for his reason. Sprinting doesn't buy hang time; it buys horizontal distance.

## Worked example

**Given (illustrative):** the hero runs off a ledge $h = 5.0\,\text{m}$ above the lower platform, at $u = 8.0\,\text{m/s}$ horizontally. $g = 9.8\,\text{m/s}^2$, no air resistance.
**Find:** the time in the air, how far out the hero lands, and the velocity on landing.

Time from the vertical motion alone, with $u_y = 0$:
$$h = \tfrac{1}{2}gt^2 \;\Rightarrow\; t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{2 \times 5.0}{9.8}} = \sqrt{1.02} \approx 1.01\,\text{s}$$

At $60$ frames per second, that is about $61$ frames, for the walker and the sprinter alike.

Horizontal distance, at constant velocity:
$$x = u_x t = 8.0 \times 1.01 \approx 8.1\,\text{m}$$

Landing velocity: $v_x = 8.0\,\text{m/s}$ (unchanged) and $v_y = -gt = -9.8 \times 1.01 \approx -9.9\,\text{m/s}$, so
$$v = \sqrt{8.0^2 + 9.9^2} \approx 12.7\,\text{m/s}, \quad \text{at } \tan^{-1}\!\left(\frac{9.9}{8.0}\right) \approx 51^\circ \text{ below the horizontal}$$

**Sanity check:** a walker at $4.0\,\text{m/s}$ also falls for $1.01\,\text{s}$ but lands only $4.0\,\text{m}$ out, half as far. Doubling the horizontal speed doubled the distance and changed the time not at all.

## Where the picture breaks

Many platformers deliberately break real physics. Designers often use a gravity far stronger than $9.8\,\text{m/s}^2$ so jumps feel snappy, give extra "air control" so you can steer mid-fall, or let a hero jump for a few frames after leaving a ledge. Any of those would change Ritika's result. In the real world, air resistance also matters a little: it slows the horizontal motion and, for fast objects, slightly lengthens the fall. The model here is the ideal one: gravity only, over a flat, non-rotating Earth.

## Key takeaway

Projectile motion is two independent motions sharing one clock: steady horizontal velocity ($a_x = 0$) and uniformly accelerated vertical motion ($a_y = -g$). The time in the air is set by the vertical motion alone. Running off a ledge faster makes you land further away, never later.
