---
concept_id: projectile_trajectory
interest: football
format: explain
title: The goal-kick angle that reaches the halfway line
check:
  question: |-
    A ball is kicked from the ground at $15\,\text{m/s}$, at $60^\circ$ above the horizontal. Ignoring air resistance and taking $g = 9.8\,\text{m/s}^2$, how high does it rise? ($\sin 60^\circ \approx 0.866$)
  options:
    A: |-
      About $11.5\,\text{m}$
    B: |-
      About $9.9\,\text{m}$
    C: |-
      About $2.9\,\text{m}$
    D: |-
      About $8.6\,\text{m}$
  answer: D
  explanation: |-
    $H = \dfrac{u^2\sin^2\theta}{2g} = \dfrac{15^2 \times 0.75}{2 \times 9.8} = \dfrac{168.75}{19.6} \approx 8.6\,\text{m}$, since $\sin^2 60^\circ = 0.75$.
  misconceptions:
    A: |-
      Uses $u^2/2g$, the height for a ball kicked straight up. Only the vertical component of the launch velocity, $u\sin\theta$, lifts the ball.
    B: |-
      Uses $\sin\theta$ instead of $\sin^2\theta$. The height depends on the square of the vertical component, $(u\sin\theta)^2$.
    C: |-
      Uses the horizontal component, $u\cos\theta$, to find the height. The horizontal motion has no effect on how high the ball goes.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A player lofts the ball in an arc over the goalkeeper while a teammate jogs round the centre circle](scenes/football/motion_plane.svg "Every lofted ball draws an arc. The launch angle decides how high it climbs and how far it goes.")

Sanjana keeps goal for her state's under-17 team, and her new coach, Ms Thomas, wants every goal kick to reach the halfway line. On their $100\,\text{m}$ training pitch, from where Sanjana places the ball, that's about $45$ metres.

Sanjana's best kicks leave her boot at about $21\,\text{m/s}$ (Ms Thomas measured it with a radar app; illustrative). But she kicks flat, at about $30^\circ$, and ball after ball lands a few metres short.

"Get under it more," says Rahul, the centre-back. "Kick it up at sixty. Higher goes further."

"Higher just comes down sooner," Sanjana argues. "Flat is faster."

Ms Thomas smiles. "You don't need to kick any harder. There's one angle that sends the same kick furthest. And your thirty and Rahul's sixty will land in exactly the same spot."

The same spot? And which angle is the one that reaches halfway?

## The physics

From the previous lesson, a projectile launched from ground level at speed $u$ and angle $\theta$ has, with $x$ horizontal and $y$ up:

$$x = (u\cos\theta)\,t, \qquad y = (u\sin\theta)\,t - \tfrac{1}{2}gt^2$$

Everything follows from these two equations, with air resistance ignored.

**Time of flight.** The ball lands when $y = 0$ again: $t\left(u\sin\theta - \tfrac{1}{2}gt\right) = 0$. The non-zero solution is

$$T = \frac{2u\sin\theta}{g}$$

**Maximum height.** At the top, $v_y = u\sin\theta - gt = 0$, at $t = u\sin\theta/g$, half of $T$. Putting this into $y$:

$$H = \frac{u^2\sin^2\theta}{2g}$$

**Horizontal range.** The horizontal velocity stays constant for the whole flight time $T$:

$$R = (u\cos\theta)\,T = \frac{2u^2\sin\theta\cos\theta}{g} = \frac{u^2\sin 2\theta}{g}$$

**Maximum range.** $\sin 2\theta$ is largest, equal to 1, when $2\theta = 90^\circ$. So **$\theta = 45^\circ$ gives the maximum range, $R_\text{max} = u^2/g$**. And because $\sin 2\theta = \sin(180^\circ - 2\theta)$, the angles $\theta$ and $90^\circ - \theta$ give the **same range**: the steeper kick climbs higher and hangs longer, the flatter one arrives sooner.

**Trajectory.** Eliminate $t$ using $t = x/(u\cos\theta)$:

$$y = x\tan\theta - \frac{g\,x^2}{2u^2\cos^2\theta}$$

This has the form $y = ax - bx^2$, so the path of a projectile is a **parabola**.

![Five parabolas for a launch speed of 28 m/s at 15, 30, 45, 60 and 75 degrees. The 45-degree path goes furthest, to 80 m; the 30 and 60 degree paths both land at 69 m](figures/projectile_trajectory/trajectories-by-angle.svg "Drawn for a faster launch than Sanjana's, but the pattern holds at any speed: 45 degrees goes furthest, and angles adding up to 90 degrees land together.")

## Worked example

**Given:** $u = 21\,\text{m/s}$, $g = 9.8\,\text{m/s}^2$, launched from the ground, no air resistance. The halfway line is $45\,\text{m}$ away.
**Find:** the range at $30^\circ$ and $60^\circ$, then the time of flight, maximum height and range at $45^\circ$.

A useful number first: $u^2/g = 441/9.8 = 45\,\text{m}$.

At $30^\circ$: $R = 45 \times \sin 60^\circ = 45 \times 0.866 \approx 39\,\text{m}$. Six metres short, as Sanjana kept finding. It flies for $T = 2(21)(0.5)/9.8 \approx 2.1\,\text{s}$ and rises only $H = 441 \times 0.25/19.6 \approx 5.6\,\text{m}$.

At $60^\circ$: $R = 45 \times \sin 120^\circ \approx 39\,\text{m}$ too, but after a flight of $3.7\,\text{s}$ and a climb of $16.9\,\text{m}$.

At $45^\circ$:
$$T = \frac{2 \times 21 \times 0.707}{9.8} \approx 3.0\,\text{s}, \qquad H = \frac{441 \times 0.5}{2 \times 9.8} \approx 11.3\,\text{m}, \qquad R = 45\,\text{m}$$

So in this ideal model, a $45^\circ$ kick at the same speed just reaches halfway.

**Sanity check:** at $45^\circ$, $R = 4H$ ($45 = 4 \times 11.25$). And horizontal speed times flight time, $21\cos 45^\circ \times 3.03 \approx 14.85 \times 3.03 \approx 45\,\text{m}$, agrees with $R$.

## Where the picture breaks

A football is light for its size, so air resistance matters a lot at $21\,\text{m/s}$. A real kick falls well short of the vacuum range, and the best angle is **lower** than $45^\circ$, because a high ball spends longer fighting the air. Backspin can add lift and stretch the flight; a knuckling ball with little spin can dip or wobble. Players also can't always strike as hard at a steep angle. The $45^\circ$ result is exact only for a projectile in a vacuum, launched and landing at the same height.

## Key takeaway

For a projectile launched from the ground (air ignored): $T = 2u\sin\theta/g$, $H = u^2\sin^2\theta/2g$ and $R = u^2\sin 2\theta/g$, and the path is a parabola. The range is greatest at $\theta = 45^\circ$, and angles that add up to $90^\circ$ land in the same place.
