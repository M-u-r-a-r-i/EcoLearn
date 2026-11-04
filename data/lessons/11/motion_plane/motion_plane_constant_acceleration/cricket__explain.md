---
concept_id: motion_plane_constant_acceleration
interest: cricket
format: explain
title: One equation for a ball that slows down and swings
check:
  question: |-
    Seen from above, a delivery starts at $\vec{r}_0 = 0.20\hat{j}\,\text{m}$ with $\vec{v}_0 = 30\hat{i}\,\text{m/s}$ and a constant acceleration $\vec{a} = (-6.0\hat{i} - 2.0\hat{j})\,\text{m/s}^2$. Where is it after $0.40\,\text{s}$?
  options:
    A: |-
      $(11.52\hat{i} + 0.04\hat{j})\,\text{m}$
    B: |-
      $(12.00\hat{i} + 0.20\hat{j})\,\text{m}$
    C: |-
      $(11.04\hat{i} - 0.12\hat{j})\,\text{m}$
    D: |-
      $(11.52\hat{i} - 0.16\hat{j})\,\text{m}$
  answer: A
  explanation: |-
    $x = 0 + 30(0.40) + \tfrac{1}{2}(-6.0)(0.40)^2 = 12 - 0.48 = 11.52\,\text{m}$ and $y = 0.20 + 0 + \tfrac{1}{2}(-2.0)(0.40)^2 = 0.20 - 0.16 = 0.04\,\text{m}$.
  misconceptions:
    B: |-
      Ignores the acceleration and uses $\vec{r} = \vec{r}_0 + \vec{v}_0 t$, as if the velocity stayed constant.
    C: |-
      Drops the $\tfrac{1}{2}$ and uses $\vec{a}t^2$, doubling the effect of the acceleration in both directions.
    D: |-
      Forgets the starting position $\vec{r}_0$, so it gives the displacement from the start rather than the position.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A day match: a batter lofts the ball towards the boundary; a big screen shows a ball-tracking top view of a curving delivery](scenes/cricket/motion_plane.svg "Look at the big screen: from above, a swinging ball's path is a curve, not a straight line.")

Nikhil is a swing bowler in his state's under-19 squad. After a net session, the analyst plays his best ball on the big screen, in the top view the ball-tracking system draws: a red line leaving his hand and bending gently across the pitch towards the batter's stumps.

His teammate Meher points at the screen. "That line is doing two things at once. The ball is slowing down, because air drags on it. And it's curving sideways, because it's swinging. How does the computer draw that? Does it need a separate formula for every wobble?"

The analyst smiles. "For a short stretch, one equation does it. The same one you use for a car speeding up on a straight road, just written with arrows."

How can the equation for a straight road describe a ball that is slowing down and swinging sideways at the same time?

## The physics

In one dimension, for constant acceleration, you know $v = u + at$ and $x = x_0 + ut + \tfrac{1}{2}at^2$. In a plane, the same equations hold with every quantity a vector. For **constant acceleration** $\vec{a}$ (fixed in size *and* direction):

$$\vec{v} = \vec{v}_0 + \vec{a}\,t$$

$$\vec{r} = \vec{r}_0 + \vec{v}_0\,t + \tfrac{1}{2}\vec{a}\,t^2$$

Here $\vec{r}_0$ and $\vec{v}_0$ are the position and velocity at $t = 0$. Each term is a vector, and the new position is found by adding them head to tail.

![The origin O, the position r0, then v0 t and half a t squared drawn head to tail, reaching the final position r. The actual curved path is dotted](figures/motion_plane_constant_acceleration/position-vector-sum.svg "The position at time t is r0 plus v0 t plus half a t squared, added head to tail. The dotted path curves because the acceleration keeps bending the velocity.")

Written with unit vectors, each vector equation splits into two ordinary equations, one per axis:

$$x = x_0 + v_{0x}t + \tfrac{1}{2}a_x t^2, \qquad y = y_0 + v_{0y}t + \tfrac{1}{2}a_y t^2$$

$$v_x = v_{0x} + a_x t, \qquad v_y = v_{0y} + a_y t$$

This is the key idea: **the $x$-motion and the $y$-motion are independent**. The $x$ equations contain only $x$-components, and the $y$ equations only $y$-components. Motion in a plane is just two straight-line motions happening at the same time, sharing the same clock $t$.

For Nikhil's ball, seen from above, take $\hat{i}$ along the pitch towards the batter and $\hat{j}$ sideways. The drag gives a negative $a_x$, which slows the ball along the pitch. The swing gives a sideways $a_y$, which builds up a sideways velocity from zero, so the path curves. Gravity acts vertically, perpendicular to this top-view plane, so it doesn't change $x$ or $y$ at all.

## Worked example

**Given (illustrative):** origin on the line joining the middle stumps, level with the release point. $\vec{r}_0 = -0.40\hat{j}\,\text{m}$ (released $0.40\,\text{m}$ to one side of that line), $\vec{v}_0 = 36\hat{i}\,\text{m/s}$, and $\vec{a} = (-8.0\hat{i} + 4.0\hat{j})\,\text{m/s}^2$, taken as constant.
**Find:** position and velocity at $t = 0.50\,\text{s}$.

Along the pitch ($x$):
$$x = 0 + 36(0.50) + \tfrac{1}{2}(-8.0)(0.50)^2 = 18.0 - 1.0 = 17.0\,\text{m}$$
$$v_x = 36 + (-8.0)(0.50) = 32\,\text{m/s}$$

Sideways ($y$):
$$y = -0.40 + 0 + \tfrac{1}{2}(4.0)(0.50)^2 = -0.40 + 0.50 = 0.10\,\text{m}$$
$$v_y = 0 + (4.0)(0.50) = 2.0\,\text{m/s}$$

So $\vec{r} = (17.0\hat{i} + 0.10\hat{j})\,\text{m}$ and $\vec{v} = (32\hat{i} + 2.0\hat{j})\,\text{m/s}$. The ball has travelled $17\,\text{m}$ down the pitch, swung $0.50\,\text{m}$ sideways and crossed to the other side of the stumps' line by $10\,\text{cm}$. Its speed is $\sqrt{32^2 + 2.0^2} \approx 32.1\,\text{m/s}$.

**Sanity check:** if $\vec{a} = \vec{0}$, the ball would be at $18\hat{i} - 0.40\hat{j}$, still in a straight line. The sideways shift ($0.50\,\text{m}$) is tiny compared with the $17\,\text{m}$ along the pitch, which matches how subtle swing looks.

## Where the picture breaks

The acceleration of a real swinging ball is **not** constant. Air drag grows with speed, so it weakens as the ball slows, and the swing force depends on the seam, the ball's surface and the air. Taking $\vec{a}$ as constant is an approximation that is reasonable only over a short time. A ball-tracking system builds its line from camera images of the real ball, not from one constant $\vec{a}$. The top view also ignores the vertical motion and the bounce, which would need a third component.

## Key takeaway

For constant acceleration in a plane, $\vec{v} = \vec{v}_0 + \vec{a}t$ and $\vec{r} = \vec{r}_0 + \vec{v}_0 t + \tfrac{1}{2}\vec{a}t^2$. Split them into $x$ and $y$ equations and solve each as ordinary one-dimensional motion with the same time $t$: perpendicular motions don't affect each other.
