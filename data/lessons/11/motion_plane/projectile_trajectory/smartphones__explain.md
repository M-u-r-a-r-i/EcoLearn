---
concept_id: projectile_trajectory
interest: smartphones
format: explain
title: Settling the launch-angle argument with a phone video
check:
  question: |-
    A lab launcher fires a ball from floor level at $14\,\text{m/s}$, and the angle can be set to anything. Ignoring air resistance and taking $g = 9.8\,\text{m/s}^2$, what is the greatest range it can reach, and at what launch angle?
  options:
    A: |-
      $40\,\text{m}$, at $45^\circ$
    B: |-
      $20\,\text{m}$, at $45^\circ$
    C: |-
      $10\,\text{m}$, at $45^\circ$
    D: |-
      $20\,\text{m}$, at $60^\circ$
  answer: B
  explanation: |-
    $R = u^2\sin 2\theta / g$ is greatest when $\sin 2\theta = 1$, at $\theta = 45^\circ$. Then $R_\text{max} = u^2/g = 196/9.8 = 20\,\text{m}$.
  misconceptions:
    A: |-
      Puts an extra factor of 2 into the range, using $2u^2/g$. The factor of 2 is already inside $\sin 2\theta = 2\sin\theta\cos\theta$.
    C: |-
      Uses $u^2/2g$, which is the greatest height for a ball fired straight up, not the greatest range.
    D: |-
      Thinks a steeper launch goes further because it stays up longer. Beyond $45^\circ$ the extra flight time is outweighed by the smaller horizontal speed; $60^\circ$ gives only about $17\,\text{m}$.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![An evening terrace: an earbud case follows a dashed curve off a table, a drone flies overhead, and a phone shows a map](scenes/smartphones/motion_plane.svg "Every object moving freely through the air in this scene follows the same kind of curve. Its shape is set by the launch speed and the launch angle.")

It's physics practical day, and Anjali's group has a spring launcher that fires a small ball at the same speed every time. The angle is adjustable. Their task: find the angle that sends the ball furthest along the lab floor.

"Sixty degrees," says Farhan. "Higher means longer in the air, and longer in the air means further."

"Thirty," says Anjali's partner Lakshmi. "Flatter means more of the speed goes forward."

Anjali sets her phone on a stool and opens a video-analysis app that tracks the ball frame by frame and draws its path on the screen. They fire at $30^\circ$, then $45^\circ$, then $60^\circ$.

Three curved paths appear, one on top of the other. Two of them land in exactly the same spot. Which angle wins, and why do two different angles tie?

## The physics

Take the launch point as the origin, $x$ horizontal and $y$ up. For launch speed $u$ at angle $\theta$, ignoring air resistance, $u_x = u\cos\theta$ and $u_y = u\sin\theta$, and

$$x = (u\cos\theta)\,t, \qquad y = (u\sin\theta)\,t - \tfrac{1}{2}gt^2$$

**Trajectory.** Eliminate $t$ using $t = x/(u\cos\theta)$:

$$y = x\tan\theta - \frac{g}{2u^2\cos^2\theta}\,x^2$$

This is of the form $y = ax - bx^2$: a **parabola**.

**Time of flight.** The ball lands when $y = 0$ again, so $t(u\sin\theta - \tfrac{1}{2}gt) = 0$, giving

$$T = \frac{2u\sin\theta}{g}$$

**Maximum height.** At the top $v_y = 0$, so $u_y^2 = 2gH$:

$$H = \frac{u^2\sin^2\theta}{2g}$$

**Horizontal range.** Distance covered in time $T$ at speed $u\cos\theta$: $R = u\cos\theta \times \dfrac{2u\sin\theta}{g}$. Using $2\sin\theta\cos\theta = \sin 2\theta$,

$$R = \frac{u^2\sin 2\theta}{g}$$

$\sin 2\theta$ can be at most 1, when $2\theta = 90^\circ$. So the **maximum range is at $\theta = 45^\circ$**, and it equals $u^2/g$. Also $\sin 2\theta$ is the same for $\theta$ and $90^\circ - \theta$, so **complementary angles** like $30^\circ$ and $60^\circ$ give the **same range**. The $60^\circ$ ball stays up longer but moves forward more slowly, and the two effects cancel exactly.

![Five parabolic trajectories at 15, 30, 45, 60 and 75 degrees for the same launch speed. 45 degrees goes furthest; 30 and 60 land at the same point, as do 15 and 75](figures/projectile_trajectory/trajectories-by-angle.svg "Same speed, five angles. This graph is drawn for a launch speed four times the lab launcher's, so divide every distance on it by 16 (range and height go as u squared). The pattern is the same: 45 degrees wins, and complementary angles tie.")

Farhan and Lakshmi were both half right, and both lost to $45^\circ$.

## Worked example

**Given (illustrative):** the launcher fires at $u = 7.0\,\text{m/s}$ from floor level; $g = 9.8\,\text{m/s}^2$; $\sin 45^\circ = \cos 45^\circ \approx 0.707$.
**Find:** time of flight, maximum height and range at $45^\circ$, and the range at $30^\circ$ and $60^\circ$.

1. **Time of flight:** $T = \dfrac{2 \times 7.0 \times 0.707}{9.8} \approx 1.0\,\text{s}$. About one second in the air.
2. **Maximum height:** $H = \dfrac{7.0^2 \times 0.707^2}{2 \times 9.8} = \dfrac{49 \times 0.50}{19.6} = 1.25\,\text{m}$, roughly chest height for a student standing beside it.
3. **Range at $45^\circ$:** $R = \dfrac{7.0^2 \times 1}{9.8} = \dfrac{49}{9.8} = 5.0\,\text{m}$, about the length of a small car.
4. **Range at $30^\circ$ and $60^\circ$:** $\sin 60^\circ = \sin 120^\circ \approx 0.866$, so both give $5.0 \times 0.866 \approx 4.3\,\text{m}$. That's the tie in Anjali's video.

**Sanity check:** the $45^\circ$ range, $5.0\,\text{m}$, is four times the greatest height, $1.25\,\text{m}$, which is exactly what the formulas give at $45^\circ$ ($R/H = 4/\tan\theta = 4$).

## Where the picture breaks

The formulas ignore air resistance, and a small light ball over $5\,\text{m}$ is slowed a little, landing slightly short. With drag, the best angle drops a little below $45^\circ$. They also assume the ball lands at the height it was launched from; a launcher on a bench firing to the floor has a different best angle, a bit below $45^\circ$. The video app's path is built from separate frames, so its landing points are only as precise as the frame rate allows.

## Key takeaway

A projectile follows a parabola, $y = x\tan\theta - \dfrac{g x^2}{2u^2\cos^2\theta}$, with time of flight $T = \dfrac{2u\sin\theta}{g}$, maximum height $H = \dfrac{u^2\sin^2\theta}{2g}$ and range $R = \dfrac{u^2\sin 2\theta}{g}$. The range is greatest, $u^2/g$, at $45^\circ$, and angles adding to $90^\circ$ give equal ranges.
