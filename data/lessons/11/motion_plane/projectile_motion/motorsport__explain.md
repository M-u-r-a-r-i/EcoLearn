---
concept_id: projectile_motion
interest: motorsport
format: explain
title: The bet about flooring it over the crest
check:
  question: |-
    Two identical karts roll off the same flat crest at the same instant, one at $6\,\text{m/s}$ and one at $18\,\text{m/s}$. The ground beyond the crest is a flat drop. Ignoring air resistance, which kart touches down first?
  options:
    A: |-
      The slower one, because it has less speed carrying it forward.
    B: |-
      The faster one, because it covers the drop more quickly.
    C: |-
      Neither — they land at the same instant, because horizontal velocity does not affect the vertical motion.
    D: |-
      The slower one, because the faster kart's path through the air is longer.
  answer: C
  explanation: |-
    Both karts leave with zero vertical velocity and both have the same vertical acceleration $g$, so they fall the same height in the same time. The extra horizontal velocity only carries the faster kart further out.
  misconceptions:
    A: |-
      Assumes forward speed somehow holds a body up. With air resistance ignored, nothing acts on a projectile except gravity, straight down.
    B: |-
      Mixes up speed *along the path* with speed *downwards*. All the extra speed is horizontal, so none of it helps the kart reach the ground.
    D: |-
      Assumes a longer path must take longer. The time in the air is set by the vertical motion alone, and that is identical for both.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race circuit seen from above, with a trackside replay screen showing a car leaving a crest and following a dashed arc down to the landing](scenes/motorsport/motion_plane.svg "Look at the replay screen: once the wheels leave the ground, the car is simply falling — forwards and downwards at the same time.")

At a club rallycross day near Nashik, the fast section ends in a crest where the gravel road goes flat for a few metres and then drops away into a dip. Cars leave the ground there every lap.

Dhruv is arguing with Kavya in the service area. "You have to be flat out over it," he says. "The faster you go, the longer you hang in the air. That's why the quick ones fly so far."

"You fly further," Kavya says. "You don't hang longer. Gravity doesn't care how fast you're going sideways."

Dhruv doesn't buy it. So they roll two identical karts off the same low ledge at the same instant — one barely moving, one given a hard shove — while Kavya's phone films it in slow motion.

Who wins the argument, and why?

## The physics

A **projectile** is a body that, once launched, moves under gravity alone — which means air resistance is ignored. The only force is its weight, straight down, so its acceleration is

$$\vec{a} = -g\,\hat{j}, \qquad g = 9.8\,\text{m/s}^2$$

constant, with $\hat{j}$ pointing up. Because $\vec{a}$ is constant, the equations from the last lesson apply, and they split into two **independent** motions:

- **Horizontal ($x$):** no force, so $a_x = 0$. The horizontal velocity never changes: $v_x = u_x$ and $x = u_x t$. Uniform velocity.
- **Vertical ($y$):** $a_y = -g$. So $v_y = u_y - gt$ and $y = u_y t - \tfrac{1}{2}gt^2$. Uniform acceleration, exactly like a dropped stone.

For a launch at speed $u$ and angle $\theta$ above the horizontal, $u_x = u\cos\theta$ and $u_y = u\sin\theta$. Off a *flat* crest, $\theta = 0$, so $u_x = u$ and $u_y = 0$.

That settles the bet. Both karts leave with **zero vertical velocity** and share the **same vertical acceleration**, so their vertical motions are identical: they fall the same height in the same time and land together. Nothing in the $y$ equations mentions $u_x$ at all. The fast kart's speed only carries it further out while it falls.

![A strobe picture: a dropped ball and a ball launched horizontally are level with each other at every flash, while the launched one moves equal steps sideways](figures/projectile_motion/horizontal-vs-dropped.svg "At every flash the two are at the same height. The horizontal velocity stays the same all the way down; only the vertical velocity grows.")

Put the two together — steady sideways motion, speeding-up downward motion — and the path is a curve. It is a parabola, as the next lesson shows.

## Worked example

**Given (illustrative):** a rally car leaves the flat crest horizontally at $u = 20\,\text{m/s}$ (about $72\,\text{km/h}$), and the landing is $h = 4.9\,\text{m}$ below the crest. Take $g = 9.8\,\text{m/s}^2$ and ignore air resistance.
**Find:** the time in the air, how far along the road it touches down, and how fast it is going when it does.

The vertical motion alone gives the time. Starting with $u_y = 0$ and falling $4.9\,\text{m}$:

$$h = \tfrac{1}{2}gt^2 \quad\Rightarrow\quad t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{9.8}{9.8}} = 1.0\,\text{s}$$

One second in the air — long enough to feel very long from inside the car.

The horizontal motion runs at a steady $20\,\text{m/s}$ for that same second:

$$x = u_x t = 20 \times 1.0 = 20\,\text{m}$$

about five car lengths out from the crest.

On landing, $v_x$ is still $20\,\text{m/s}$, while $v_y = -gt = -9.8\,\text{m/s}$, so

$$v = \sqrt{20^2 + 9.8^2} \approx 22\,\text{m/s}, \quad \text{at } \tan^{-1}\!\left(\frac{9.8}{20}\right) \approx 26^\circ \text{ below the horizontal}$$

**Sanity check:** a kart nudged gently off the same crest at $2\,\text{m/s}$ would also take $1.0\,\text{s}$ — it would simply land $2\,\text{m}$ out instead of $20\,\text{m}$. Kavya was right: further, not longer.

## Where the picture breaks

Air resistance is not really zero. At $20\,\text{m/s}$ drag trims the horizontal speed a little, so a real car lands slightly short of $20\,\text{m}$ — far too small a difference to see without slow motion. A car in the air is also not a point mass: it pitches nose-up or nose-down, which decides whether it lands on four wheels, though it does not change the path of the *centre of mass*. And the launch is only truly horizontal if the crest really is flat; a slight upward ramp gives $u_y > 0$ and a longer flight.

## Key takeaway

Projectile motion is two independent motions on one clock: steady horizontal velocity ($a_x = 0$) and uniformly accelerated vertical motion ($a_y = -g$). The time in the air depends only on the vertical motion. That is why going faster over a crest makes you land further away, not stay up longer.
