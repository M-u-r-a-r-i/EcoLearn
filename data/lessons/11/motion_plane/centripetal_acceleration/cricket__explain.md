---
concept_id: centripetal_acceleration
interest: cricket
format: explain
title: The hidden acceleration on a spinner's seam
check:
  question: |-
    A fielder runs round a curved stretch of boundary, a circular arc of radius $40\,\text{m}$, at a steady $8.0\,\text{m/s}$. What is the fielder's acceleration?
  options:
    A: |-
      $0.20\,\text{m/s}^2$, towards the centre of the arc
    B: |-
      $1.6\,\text{m/s}^2$, outwards, away from the centre
    C: |-
      Zero, because the speed is not changing
    D: |-
      $1.6\,\text{m/s}^2$, towards the centre of the arc
  answer: D
  explanation: |-
    $a_c = v^2/r = 8.0^2/40 = 64/40 = 1.6\,\text{m/s}^2$, directed towards the centre of the circle, because the velocity keeps turning inwards.
  misconceptions:
    A: |-
      Uses $v/r$ instead of $v^2/r$. That gives the angular speed in rad/s, not an acceleration.
    B: |-
      Believes the acceleration points outwards, following the "pushed outwards" feeling on a turn. The acceleration of a body moving in a circle points inwards.
    C: |-
      Thinks acceleration means only a change of speed. A change in the direction of the velocity is also an acceleration.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A day match: a batter lofts the ball towards the boundary as a fielder races along the rope](scenes/cricket/motion_plane.svg "Circles are everywhere in cricket, even on the surface of the ball itself.")

At a spin-bowling clinic, Harpreet bowls her off-break into a net while a high-speed camera records it. Played back slowly, the seam turns over and over as the ball flies. The coach reads out the spin rate from the software: about 30 revolutions every second (illustrative).

Her friend Tanmay works it out on his phone. "A point on the seam is only moving at about 24 kilometres per hour around the ball. I cycle faster than that."

"And it's spinning at a steady rate," Harpreet adds, "so the seam isn't accelerating at all."

The coach shakes his head. "That point on the seam is accelerating more than a hundred times harder than a falling ball."

A slow-moving point with a huge acceleration? How big is it really, and which way does it point?

## The physics

In the last lesson you saw that a body in uniform circular motion is accelerating, because its velocity keeps changing direction. This acceleration is called **centripetal acceleration** ("centre-seeking").

**Direction.** Look at the velocity at two nearby moments. Both have the same length $v$, but the later one has turned a little. The change $\Delta\vec{v}$ joins their heads, and it points **towards the centre** of the circle. Since $\vec{a} = \Delta\vec{v}/\Delta t$, the acceleration points towards the centre too, at every instant, at right angles to the velocity.

![Left: a circle with three points, each showing a tangent velocity arrow and an acceleration arrow pointing to the centre. Right: velocity vectors at two nearby moments drawn tail to tail, with the change in velocity pointing inwards](figures/centripetal_acceleration/acceleration-towards-centre.svg "The velocity turns, so the change in velocity, and so the acceleration, points to the centre. The speed never changes, only the direction.")

**Size.** The triangle formed by the two velocities has the same shape as the triangle formed by the two position vectors (both have an angle $\Delta\theta$ between two equal sides). So $|\Delta\vec{v}|/v = |\Delta\vec{r}|/r$. For a short interval, $|\Delta\vec{r}| \approx v\,\Delta t$, which gives $|\Delta\vec{v}|/\Delta t = v^2/r$:

$$a_c = \frac{v^2}{r} = \omega^2 r$$

using $v = \omega r$. Here $v$ is the speed, $r$ the radius and $\omega$ the angular speed. The SI unit is $\text{m/s}^2$. This holds for **uniform** circular motion (constant speed). Both $v$ and $r$ matter: doubling the speed on the same circle gives **four times** the acceleration, and a tighter circle at the same speed gives more.

In Harpreet's delivery, the circle is the path of a point on the seam around the ball's spin axis. That circle is tiny, which is why a modest speed gives a huge $v^2/r$.

## Worked example

**Given:** a ball of circumference about $22.6\,\text{cm}$ (a men's ball is $22.4$–$22.9\,\text{cm}$), so $r = C/2\pi \approx 3.6\,\text{cm} = 0.036\,\text{m}$. Spin rate $30$ revolutions per second (illustrative). Consider a point on the circle farthest from the spin axis.
**Find:** its speed around the ball and its centripetal acceleration, relative to the ball's centre.

In one revolution the point travels one circumference, so

$$v = C \times 30 = 0.226 \times 30 \approx 6.8\,\text{m/s} \quad (\approx 24\,\text{km/h})$$

$$a_c = \frac{v^2}{r} = \frac{6.78^2}{0.036} = \frac{46.0}{0.036} \approx 1.3 \times 10^{3}\,\text{m/s}^2$$

pointing from the seam towards the centre of the ball.

Compared with gravity: $1.3 \times 10^3 / 9.8 \approx 130$. That is about $130$ times the acceleration of a freely falling ball, just as the coach said.

**Sanity check (a second way):** $\omega = 2\pi \times 30 \approx 188\,\text{rad/s}$, so $\omega^2 r = 188^2 \times 0.036 \approx 35\,400 \times 0.036 \approx 1.3 \times 10^3\,\text{m/s}^2$. Same answer.

## Where the picture breaks

We measured the seam's motion **relative to the ball's centre**. The whole ball is also flying down the pitch, slowing under drag and falling under gravity, so relative to the ground the seam's path is a looping curve, not a circle. Our $a_c$ is the part of its acceleration due to the spin alone. The spin rate also slowly drops during flight, so the motion isn't perfectly uniform. And not every point on the seam is at the full radius: points closer to the spin axis move in smaller circles and have smaller accelerations.

## Key takeaway

A body moving in a circle at constant speed has a **centripetal acceleration** of size $a_c = v^2/r = \omega^2 r$, always pointing towards the centre, at right angles to the velocity. Constant speed does not mean zero acceleration. A small, fast circle, like a spinning ball's seam, can mean an enormous one.
