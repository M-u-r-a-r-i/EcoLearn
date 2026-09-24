---
concept_id: projectile_trajectory
interest: motorsport
format: explain
title: The ramp angle that wins the long-jump trophy
check:
  question: |-
    A car leaves a ramp at $14\,\text{m/s}$, at $30^\circ$ above the horizontal, from ground level. Ignoring air resistance and taking $g = 9.8\,\text{m/s}^2$, what is the greatest height it reaches?
  options:
    A: |-
      $5.0\,\text{m}$
    B: |-
      $10.0\,\text{m}$
    C: |-
      $17.3\,\text{m}$
    D: |-
      $2.5\,\text{m}$
  answer: D
  explanation: |-
    $H = \dfrac{u^2\sin^2\theta}{2g} = \dfrac{14^2 \times (0.50)^2}{2 \times 9.8} = \dfrac{196 \times 0.25}{19.6} = 2.5\,\text{m}$.
  misconceptions:
    A: |-
      Uses $\sin\theta$ instead of $\sin^2\theta$. Only the *vertical* component $u\sin\theta$ climbs, and the height formula comes from squaring it.
    B: |-
      Uses $u^2/2g$, the height for a body fired straight up. At $30^\circ$ most of the launch speed is horizontal and never contributes to height.
    C: |-
      Gives the horizontal range, $u^2\sin 2\theta/g \approx 17.3\,\text{m}$, instead of the height. Range and height are different formulas.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race circuit seen from above, with a trackside replay screen showing a car leaving a crest and following a dashed arc down to its landing](scenes/motorsport/motion_plane.svg "Every jump traces an arc. Its launch angle decides how high it goes and how far along it comes down.")

Over the monsoon break, when the circuit is shut, Sanjana's motorsport club runs a long-jump contest for radio-controlled off-road cars: a wooden ramp, a taped landing zone, and a trophy for the longest jump.

Her car leaves the ramp at about $14\,\text{m/s}$ — she measured it with a timing gate over a marked metre (illustrative). The ramp is bolted at $30^\circ$, and her jumps keep landing just short of the tape.

"Steepen it," says her clubmate Imtiaz. "Put it at sixty. Higher means further."

"Higher means it comes down sooner," Sanjana argues. "Thirty is flatter, so it's quicker to the tape."

Her coach, watching from the pit table, shakes her head at both of them. "Sixty degrees and thirty degrees will land in exactly the same place. And neither of them is the best angle you could bolt that ramp at."

The same place? Then which angle wins the trophy?

## The physics

From the last lesson, a projectile launched from ground level at speed $u$ and angle $\theta$, with $x$ horizontal and $y$ up, obeys

$$x = (u\cos\theta)\,t, \qquad y = (u\sin\theta)\,t - \tfrac{1}{2}gt^2$$

Everything else follows from those two, with air resistance ignored throughout.

**Time of flight.** The car lands when $y = 0$ again, so $t\left(u\sin\theta - \tfrac{1}{2}gt\right) = 0$, and the non-zero root is

$$T = \frac{2u\sin\theta}{g}$$

**Maximum height.** At the top the vertical velocity $v_y = u\sin\theta - gt$ is zero, at $t = u\sin\theta/g$ — exactly half of $T$. Substituting into $y$:

$$H = \frac{u^2\sin^2\theta}{2g}$$

**Horizontal range.** The horizontal velocity is unchanged for the whole flight:

$$R = (u\cos\theta)\,T = \frac{2u^2\sin\theta\cos\theta}{g} = \frac{u^2\sin 2\theta}{g}$$

**Maximum range.** $\sin 2\theta$ is largest, equal to 1, when $2\theta = 90^\circ$. So **$\theta = 45^\circ$ gives the longest jump**, $R_\text{max} = u^2/g$. And because $\sin 2\theta = \sin(180^\circ - 2\theta)$, angles $\theta$ and $90^\circ - \theta$ give the **same range** — the steep one after a higher, slower flight, the flat one after a low, quick one. That is the coach's point about $30^\circ$ and $60^\circ$.

**Trajectory.** Eliminate $t$ using $t = x/(u\cos\theta)$:

$$y = x\tan\theta - \frac{g\,x^2}{2u^2\cos^2\theta}$$

which has the form $y = ax - bx^2$: a projectile's path is a **parabola**.

![Several parabolic paths for one launch speed at different angles; the 45-degree path reaches the furthest, and pairs of angles adding to 90 degrees land together](figures/projectile_trajectory/trajectories-by-angle.svg "Same launch speed, different angles (this figure is drawn for one particular speed). The 45-degree path goes furthest, and each pair of angles adding to 90 degrees lands in the same place.")

## Worked example

**Given:** $u = 14\,\text{m/s}$, $g = 9.8\,\text{m/s}^2$, launch and landing at the same level, air resistance ignored.
**Find:** the range at $30^\circ$ and at $60^\circ$, and the range, height and flight time at $45^\circ$.

One number does most of the work: $u^2/g = 196/9.8 = 20\,\text{m}$.

At $30^\circ$: $R = 20\sin 60^\circ = 20 \times 0.866 \approx 17.3\,\text{m}$ — a little short of the tape, just as Sanjana kept finding.

At $60^\circ$: $R = 20\sin 120^\circ \approx 17.3\,\text{m}$ as well. Imtiaz's steeper ramp lands in the very same spot.

At $45^\circ$, where $\sin 2\theta = 1$:

$$R = 20\,\text{m}, \qquad H = \frac{196 \times 0.50}{19.6} = 5.0\,\text{m}, \qquad T = \frac{2 \times 14 \times 0.707}{9.8} \approx 2.0\,\text{s}$$

So $45^\circ$ adds nearly three metres over either of their guesses — and sends the car about as high as a first-floor balcony on the way.

**Sanity check:** at $45^\circ$ the formulas force $R = 4H$, and $20 = 4 \times 5.0$. Checking the range a second way, $T$ times the horizontal speed gives $2.0 \times 14\cos 45^\circ \approx 2.0 \times 9.9 \approx 20\,\text{m}$. They agree.

## Where the picture breaks

This model is a clean starting point, not the whole story. Air resistance shortens every real jump and, because it eats the flight time, pushes the *best* angle below $45^\circ$. A car also leaves the ramp a few centimetres above the ground rather than exactly at ground level, which adds a little range. Most importantly, a car is not a point: it rotates in the air, and a very steep launch lands it nose-first or on its roof, so no club would actually bolt a ramp at $45^\circ$. The $45^\circ$ result is exact only for a point projectile in a vacuum, launched and landing at the same height.

## Key takeaway

For a projectile launched from ground level, with air ignored: $T = 2u\sin\theta/g$, $H = u^2\sin^2\theta/2g$ and $R = u^2\sin 2\theta/g$, and the path is a parabola. The range is greatest at $\theta = 45^\circ$, and any two angles adding up to $90^\circ$ land in the same place.
