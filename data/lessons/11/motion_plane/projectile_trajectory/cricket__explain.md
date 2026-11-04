---
concept_id: projectile_trajectory
interest: cricket
format: explain
title: The angle that clears the rope in a six-hitting contest
check:
  question: |-
    A ball leaves the bat at $20\,\text{m/s}$, at $30^\circ$ above the horizontal, from ground level. Ignoring air resistance and taking $g = 9.8\,\text{m/s}^2$, what is its horizontal range?
  options:
    A: |-
      About $20.4\,\text{m}$
    B: |-
      About $35.3\,\text{m}$
    C: |-
      About $40.8\,\text{m}$
    D: |-
      About $17.7\,\text{m}$
  answer: B
  explanation: |-
    $R = \dfrac{u^2\sin 2\theta}{g} = \dfrac{20^2 \times \sin 60^\circ}{9.8} = \dfrac{400 \times 0.866}{9.8} \approx 35.3\,\text{m}$.
  misconceptions:
    A: |-
      Uses $\sin\theta$ instead of $\sin 2\theta$. The range depends on both components of the launch velocity, which is where $2\sin\theta\cos\theta = \sin 2\theta$ comes from.
    C: |-
      Uses the maximum range $u^2/g$, which is true only at $45^\circ$. At any other angle the range is smaller.
    D: |-
      Divides by $2g$, mixing up the range formula with the one for maximum height.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A day match: a batter lofts the ball in a high arc towards the boundary as a fielder races along the rope](scenes/cricket/motion_plane.svg "Every lofted shot draws an arc. Its launch angle decides how high and how far it goes.")

Aditya has entered his town's six-hitting contest. The organisers have roped off a boundary $70\,\text{m}$ from the batting crease: clear it on the full and you score.

In practice, his cleanest hits leave the bat at about $28\,\text{m/s}$ (his friend Farhan measured it with an app; illustrative). But Aditya hits flat, at about $30^\circ$, and ball after ball lands just inside the rope.

"Hit it higher," says Farhan. "Go up at sixty degrees. Higher means further."

"Higher means it comes down sooner," Aditya argues. "Flatter is faster."

His father, a mechanical engineer, is watching. "You're both half right," he says. "There's one angle that gives the most distance for the same bat speed. And sixty degrees and thirty degrees will land in exactly the same place."

The same place? And which angle is the magic one?

## The physics

From the previous lesson, a projectile launched from ground level at speed $u$ and angle $\theta$ has, with $x$ horizontal and $y$ up:

$$x = (u\cos\theta)\,t, \qquad y = (u\sin\theta)\,t - \tfrac{1}{2}gt^2$$

Everything else follows from these two equations (air resistance ignored).

**Time of flight.** The ball lands when $y = 0$ again. So $t\left(u\sin\theta - \tfrac{1}{2}gt\right) = 0$, and the non-zero solution is

$$T = \frac{2u\sin\theta}{g}$$

**Maximum height.** At the top, the vertical velocity $v_y = u\sin\theta - gt$ is zero, at $t = u\sin\theta/g$ (half of $T$). Putting this into $y$:

$$H = \frac{u^2\sin^2\theta}{2g}$$

**Horizontal range.** The horizontal velocity stays constant for the whole time $T$:

$$R = (u\cos\theta)\,T = \frac{2u^2\sin\theta\cos\theta}{g} = \frac{u^2\sin 2\theta}{g}$$

**Maximum range.** $\sin 2\theta$ is largest (equal to 1) when $2\theta = 90^\circ$, so **$\theta = 45^\circ$ gives the maximum range, $R_\text{max} = u^2/g$**. Also $\sin 2\theta = \sin(180^\circ - 2\theta)$, so angles $\theta$ and $90^\circ - \theta$ give the **same range**. The steeper shot goes higher and stays up longer; the flatter one is quicker.

**Trajectory.** Eliminate $t$ using $t = x/(u\cos\theta)$:

$$y = x\tan\theta - \frac{g\,x^2}{2u^2\cos^2\theta}$$

This is of the form $y = ax - bx^2$: the path of a projectile is a **parabola**.

![Five parabolas for a launch speed of 28 m/s at 15, 30, 45, 60 and 75 degrees. The 45-degree path goes furthest, to 80 m; the 30 and 60 degree paths both land at 69 m](figures/projectile_trajectory/trajectories-by-angle.svg "Same speed, different angles. 45 degrees goes furthest; each pair of angles adding up to 90 degrees lands in the same place, the steeper one after a higher, longer flight.")

## Worked example

**Given:** $u = 28\,\text{m/s}$, $g = 9.8\,\text{m/s}^2$, launch from ground level, no air resistance. The boundary is $70\,\text{m}$ away.
**Find:** range at $30^\circ$ and $60^\circ$; time of flight, maximum height and range at $45^\circ$.

$u^2/g = 784/9.8 = 80\,\text{m}$, which is useful for all three.

At $30^\circ$: $R = 80 \times \sin 60^\circ = 80 \times 0.866 \approx 69.3\,\text{m}$. Just short of the rope, as Aditya kept finding.

At $60^\circ$: $R = 80 \times \sin 120^\circ \approx 69.3\,\text{m}$ too. Farhan's idea lands in the same spot.

At $45^\circ$:
$$T = \frac{2 \times 28 \times 0.707}{9.8} \approx 4.04\,\text{s}, \qquad H = \frac{784 \times 0.5}{2 \times 9.8} = 20\,\text{m}, \qquad R = 80\,\text{m}$$

So at $45^\circ$, in this ideal model, the ball clears the $70\,\text{m}$ rope by about $10\,\text{m}$.

**Sanity check:** at $45^\circ$, $R = 4H$ ($80 = 4 \times 20$), which follows from the formulas since $\tan 45^\circ = 1$. And $T$ times the horizontal speed, $4.04 \times 28\cos 45^\circ \approx 4.04 \times 19.8 \approx 80\,\text{m}$, agrees with $R$.

## Where the picture breaks

This model is a good start, but real sixes differ in important ways. Air resistance at $28\,\text{m/s}$ is large: it shortens the flight a lot and makes the best angle for a real hit **lower** than $45^\circ$. The ball also leaves the bat about a metre above the ground, not at ground level, which adds a little range and also lowers the best angle. Spin can add lift or dip. And a batter may not be able to hit as hard at $45^\circ$ as at $30^\circ$. The $45^\circ$ result is exact only for a projectile in a vacuum, launched and landing at the same height.

## Key takeaway

For a projectile launched from ground level (air ignored): $T = 2u\sin\theta/g$, $H = u^2\sin^2\theta/2g$ and $R = u^2\sin 2\theta/g$, and its path is a parabola. The range is greatest at $\theta = 45^\circ$, and angles adding up to $90^\circ$ land in the same place.
