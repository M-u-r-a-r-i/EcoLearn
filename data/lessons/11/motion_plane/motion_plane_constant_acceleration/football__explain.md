---
concept_id: motion_plane_constant_acceleration
interest: football
format: explain
title: The free kick that bends round the wall, in one equation
check:
  question: |-
    Seen from above, a curling shot leaves the boot with $\vec{v}_0 = (20\hat{i} + 2.0\hat{j})\,\text{m/s}$ and has a constant acceleration $\vec{a} = (-5.0\hat{i} - 4.0\hat{j})\,\text{m/s}^2$. What is its velocity after $0.60\,\text{s}$?
  options:
    A: |-
      $(20\hat{i} + 2.0\hat{j})\,\text{m/s}$
    B: |-
      $(18.5\hat{i} + 0.8\hat{j})\,\text{m/s}$
    C: |-
      $(17\hat{i} - 0.4\hat{j})\,\text{m/s}$
    D: |-
      $(-3.0\hat{i} - 2.4\hat{j})\,\text{m/s}$
  answer: C
  explanation: |-
    $\vec{v} = \vec{v}_0 + \vec{a}t$: $v_x = 20 + (-5.0)(0.60) = 17\,\text{m/s}$ and $v_y = 2.0 + (-4.0)(0.60) = -0.4\,\text{m/s}$.
  misconceptions:
    A: |-
      Ignores the acceleration, as if the ball kept its starting velocity. A constant acceleration changes the velocity steadily.
    B: |-
      Uses $\tfrac{1}{2}\vec{a}t$, mixing up the velocity equation with the $\tfrac{1}{2}\vec{a}t^2$ term of the position equation.
    D: |-
      Gives only the change in velocity, $\vec{a}t$, and forgets to add the starting velocity $\vec{v}_0$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A player lofts the ball in an arc over the goalkeeper while a teammate jogs round the centre circle](scenes/football/motion_plane.svg "A struck ball rarely flies in a straight line. It can curve sideways and slow down at the same time.")

Free kick, $25$ metres out. The wall lines up $9.15$ metres away, as the Laws require, blocking the straight line to goal. Anirban places the ball, steps back, and strikes it with the inside of his right foot.

The ball sets off to the right of the wall, as if it's going wide. Then it bends. By the time it reaches the goal it has swung back in, and the goalkeeper, who had stepped towards the other post, can only watch it go past.

Afterwards, his teammate Harsh watches the drone replay, filmed from straight above. "The ball starts off one way and ends up going another. It slows down *and* it curves. You'd need a new formula for every bit of that path."

Anirban grins. "Our physics teacher says one equation does the lot. The same one as for a car on a straight road."

How can a single equation describe a ball that is slowing down and curving sideways at the same time?

## The physics

In one dimension, for constant acceleration, you know $v = u + at$ and $x = x_0 + ut + \tfrac{1}{2}at^2$. In a plane, the same equations hold with every quantity a vector. For **constant acceleration** $\vec{a}$, fixed in size *and* direction:

$$\vec{v} = \vec{v}_0 + \vec{a}\,t$$

$$\vec{r} = \vec{r}_0 + \vec{v}_0\,t + \tfrac{1}{2}\vec{a}\,t^2$$

Here $\vec{r}_0$ and $\vec{v}_0$ are the position and velocity at $t = 0$. The new position is found by adding the three vectors head to tail.

![The origin O, the position r0, then v0 t and half a t squared drawn head to tail, reaching the final position r. The actual curved path is dotted](figures/motion_plane_constant_acceleration/position-vector-sum.svg "The position at time t is r0 plus v0 t plus half a t squared, added head to tail. The path curves because the acceleration keeps bending the velocity.")

Written with unit vectors, each vector equation splits into two ordinary ones:

$$x = x_0 + v_{0x}t + \tfrac{1}{2}a_x t^2, \qquad y = y_0 + v_{0y}t + \tfrac{1}{2}a_y t^2$$

$$v_x = v_{0x} + a_x t, \qquad v_y = v_{0y} + a_y t$$

This is the big idea: **the $x$-motion and the $y$-motion are independent**. The $x$ equations contain only $x$-components, and the $y$ equations only $y$-components. Motion in a plane is two straight-line motions happening together, sharing one clock $t$.

For the drone's top view, take $\hat{i}$ from the ball towards the goal line and $\hat{j}$ sideways, the way the ball bends. Air drag gives a negative $a_x$, which slows the ball on its way to goal. The spin gives a sideways $a_y$, which first cancels the ball's outward sideways velocity and then builds up an inward one, so the path bends back. Gravity acts vertically, perpendicular to the drone's view, so it doesn't change $x$ or $y$.

## Worked example

**Given (illustrative):** $\vec{r}_0 = \vec{0}$ at the ball's spot. $\vec{v}_0 = (24\hat{i} - 3.0\hat{j})\,\text{m/s}$, aimed slightly outside the wall. $\vec{a} = (-4.0\hat{i} + 8.0\hat{j})\,\text{m/s}^2$, taken as constant.
**Find:** position and velocity at $t = 0.50\,\text{s}$ and $t = 1.0\,\text{s}$.

At $t = 0.50\,\text{s}$:
$$x = 24(0.50) + \tfrac{1}{2}(-4.0)(0.50)^2 = 12 - 0.50 = 11.5\,\text{m}$$
$$y = -3.0(0.50) + \tfrac{1}{2}(8.0)(0.50)^2 = -1.5 + 1.0 = -0.50\,\text{m}$$

The ball is past the wall and still $0.50\,\text{m}$ on the outside of the straight line. Its velocity is $\vec{v} = (24 - 2.0)\hat{i} + (-3.0 + 4.0)\hat{j} = (22\hat{i} + 1.0\hat{j})\,\text{m/s}$: already heading back in.

At $t = 1.0\,\text{s}$:
$$x = 24 - 2.0 = 22\,\text{m}, \qquad y = -3.0 + 4.0 = 1.0\,\text{m}$$
$$\vec{v} = (20\hat{i} + 5.0\hat{j})\,\text{m/s}, \quad |\vec{v}| = \sqrt{400 + 25} \approx 20.6\,\text{m/s}$$

It is $3\,\text{m}$ from the goal line and $1.0\,\text{m}$ on the inside of the line it started on.

**Sanity check:** with $\vec{a} = \vec{0}$, the ball would be at $(24\hat{i} - 3.0\hat{j})\,\text{m}$ after $1.0\,\text{s}$, $3\,\text{m}$ wide of the line. The acceleration moved it $4\,\text{m}$ sideways and $2\,\text{m}$ back, which is exactly $\tfrac{1}{2}\vec{a}t^2$.

## Where the picture breaks

A real free kick does **not** have a constant acceleration. Drag grows with speed, so it weakens as the ball slows, and the sideways push from spin also changes as the ball slows and its spin decays. Treating $\vec{a}$ as constant is a reasonable approximation only over a short time. The drone's view also hides the vertical motion: the ball has to rise over the wall and dip under the bar, which needs a third component with gravity in it.

## Key takeaway

For constant acceleration in a plane, $\vec{v} = \vec{v}_0 + \vec{a}t$ and $\vec{r} = \vec{r}_0 + \vec{v}_0 t + \tfrac{1}{2}\vec{a}t^2$. Split them into $x$ and $y$ equations and solve each as ordinary straight-line motion with the same time $t$. Perpendicular motions don't affect each other, which is how one equation draws a bending free kick.
