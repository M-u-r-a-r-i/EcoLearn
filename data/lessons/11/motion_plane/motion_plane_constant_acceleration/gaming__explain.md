---
concept_id: motion_plane_constant_acceleration
interest: gaming
format: explain
title: Why the spaceship curved instead of climbing
check:
  question: |-
    A spaceship in a space game drifts with velocity $\vec{v}_0 = 3.0\hat{i}\ \text{m/s}$. Its thruster then gives it a constant acceleration $\vec{a} = 2.0\hat{j}\ \text{m/s}^2$. What is its velocity $2.0\,\text{s}$ later?
  options:
    A: |-
      $7.0\,\text{m/s}$ along $\hat{i}$
    B: |-
      $3.0\hat{i}\ \text{m/s}$
    C: |-
      $4.0\hat{j}\ \text{m/s}$
    D: |-
      $3.0\hat{i} + 4.0\hat{j}\ \text{m/s}$
  answer: D
  explanation: |-
    $\vec{v} = \vec{v}_0 + \vec{a}t = 3.0\hat{i} + (2.0)(2.0)\hat{j} = 3.0\hat{i} + 4.0\hat{j}\ \text{m/s}$, a speed of $5.0\,\text{m/s}$. The $x$-part is unchanged because there is no acceleration along $x$.
  misconceptions:
    A: |-
      Adds the change in speed to the starting speed as plain numbers ($3 + 4$), ignoring that the new velocity is added at right angles.
    B: |-
      Thinks a sideways acceleration can't change the velocity because it doesn't act along the motion. It adds a new $y$-part to the velocity.
    C: |-
      Thinks the thruster replaces the old motion, so the ship now moves only along $\hat{j}$. With no force along $x$, the $x$-velocity carries on unchanged.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: the monitor shows an artillery game with a shell flying along a curved arc; a tablet shows a top-down minimap of a circular kart track](scenes/gaming/motion_plane.svg "Curved paths in games, from shells to spaceships, come from a steady acceleration acting on a moving object.")

Rehaan is playing a retro-style space game where the ship drifts forever unless you fire a thruster. There's no air, no friction, nothing to slow it down.

His ship is drifting steadily to the right across the screen. A gap in an asteroid belt is directly above him, so he spins the ship to point its engine downwards and holds the thrust button, expecting to rise straight up into the gap.

Instead the ship swoops upwards in a long curve, still sliding right the whole time, and clips the edge of an asteroid. Game over.

"The controls are broken," he tells his sister Bhavya. "I pushed it up. It should go up."

Bhavya, who has been reading about how game physics engines work, shakes her head. "It *is* going up. It's also still going right."

Why does a steady push straight up give a curved path, and where exactly will the ship be after a few seconds?

## The physics

When the acceleration $\vec{a}$ is **constant** in size and direction, the equations of motion you know from a straight line carry over to a plane, written as vectors:

$$\vec{v} = \vec{v}_0 + \vec{a}t$$
$$\vec{r} = \vec{r}_0 + \vec{v}_0 t + \tfrac{1}{2}\vec{a}t^2$$

Here $\vec{r}_0$ and $\vec{v}_0$ are the position and velocity at $t = 0$.

The key idea is that each vector equation is really **two independent equations**, one for each axis:

$$v_x = v_{0x} + a_x t, \qquad x = x_0 + v_{0x}t + \tfrac{1}{2}a_x t^2$$
$$v_y = v_{0y} + a_y t, \qquad y = y_0 + v_{0y}t + \tfrac{1}{2}a_y t^2$$

The $x$-motion knows nothing about $a_y$, and the $y$-motion knows nothing about $a_x$. Each is just a straight-line motion, sharing the same clock $t$.

![The origin O, the position r0, then v0 t and half a t squared drawn head to tail, reaching the final position r. The actual curved path is dotted](figures/motion_plane_constant_acceleration/position-vector-sum.svg "The position at time t is r0 plus v0 t plus half a t squared, added head to tail. The dotted path curves because the acceleration keeps bending the velocity.")

That is Rehaan's ship. Along $x$: no thrust, so $a_x = 0$ and the rightward drift carries on unchanged. Along $y$: constant thrust, so the ship speeds up upwards from zero. Steady sideways motion plus growing upward motion gives a curved path, not a vertical one.

## Worked example

**Given (illustrative):** the ship starts at the origin, $\vec{r}_0 = \vec{0}$, drifting at $\vec{v}_0 = 4.0\hat{i}\ \text{m/s}$. The thruster gives $\vec{a} = 2.0\hat{j}\ \text{m/s}^2$ ($\hat{j}$ up the screen).
**Find:** the velocity and position after $t = 3.0\,\text{s}$.

Velocity, one component at a time:
$$v_x = 4.0 + 0 = 4.0\,\text{m/s}, \qquad v_y = 0 + (2.0)(3.0) = 6.0\,\text{m/s}$$
$$\vec{v} = 4.0\hat{i} + 6.0\hat{j}\ \text{m/s}, \qquad v = \sqrt{16 + 36} \approx 7.2\,\text{m/s}$$

Position:
$$x = (4.0)(3.0) = 12\,\text{m}, \qquad y = \tfrac{1}{2}(2.0)(3.0)^2 = 9.0\,\text{m}$$
$$\vec{r} = 12\hat{i} + 9.0\hat{j}\ \text{m}, \qquad r = \sqrt{144 + 81} = 15\,\text{m}$$

So after $3\,\text{s}$ Rehaan is $9\,\text{m}$ higher, but also $12\,\text{m}$ further right: that is why he missed a gap directly above him.

**Sanity check:** if the thruster were off ($a = 0$), the ship would be at $12\hat{i}$, drifting straight; if the ship had started at rest, it would be at $9.0\hat{j}$, straight above. The real answer is simply both added together.

## Where the picture breaks

A game engine doesn't use these formulas directly. It updates velocity and position in small steps, commonly every $1/60\,\text{s}$, adding $\vec{a}\,\Delta t$ to the velocity and $\vec{v}\,\Delta t$ to the position each frame. With small steps the result is very close to the exact equations, but not identical. Real spacecraft are also not in a truly force-free region: gravity from nearby bodies curves their paths too. And a real rocket loses mass as it burns fuel, so constant thrust does not quite give constant acceleration.

## Key takeaway

For constant acceleration in a plane, $\vec{v} = \vec{v}_0 + \vec{a}t$ and $\vec{r} = \vec{r}_0 + \vec{v}_0 t + \tfrac{1}{2}\vec{a}t^2$. Split them into $x$ and $y$ and solve each as an independent straight-line motion on a shared clock. An acceleration at an angle to the velocity bends the path into a curve.
