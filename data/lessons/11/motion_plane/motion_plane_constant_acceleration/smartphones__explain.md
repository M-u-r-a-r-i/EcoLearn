---
concept_id: motion_plane_constant_acceleration
interest: smartphones
format: explain
title: Where the drone ends up when you push the stick sideways
check:
  question: |-
    A drone flying level starts at the origin with velocity $\vec{v}_0 = 3\hat{i}$ m/s and has a constant acceleration $\vec{a} = 2\hat{j}\,\text{m/s}^2$ in the same horizontal plane. Where is it after $3\,\text{s}$?
  options:
    A: |-
      $9\hat{i} + 18\hat{j}$ m
    B: |-
      $9\hat{i} + 6\hat{j}$ m
    C: |-
      $9\hat{i} + 9\hat{j}$ m
    D: |-
      $18\hat{i} + 9\hat{j}$ m
  answer: C
  explanation: |-
    Treat each direction separately. $x = v_{0x}t = 3 \times 3 = 9\,\text{m}$ (no acceleration along $x$); $y = \tfrac{1}{2}a_y t^2 = \tfrac{1}{2} \times 2 \times 9 = 9\,\text{m}$. So $\vec{r} = 9\hat{i} + 9\hat{j}$ m.
  misconceptions:
    A: |-
      Drops the $\tfrac{1}{2}$ and uses $a t^2$. The distance covered from rest under constant acceleration is $\tfrac{1}{2}at^2$.
    B: |-
      Uses $a t$, which is the velocity gained along $y$, as if it were the distance. Velocity and displacement are different quantities.
    D: |-
      Lets the $y$-acceleration change the $x$-motion too. The $x$ and $y$ motions are independent; with $a_x = 0$ the $x$-velocity stays $3\,\text{m/s}$.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![An evening terrace: a small camera drone flies at a slant above the rooftops, with a blue velocity arrow](scenes/smartphones/motion_plane.svg "A drone's velocity arrow can swing round and grow at the same time. Where it ends up depends on both.")

Aditya is flying his small camera drone over the school cricket ground, using his phone as the controller screen. It is cruising level towards the east boundary at a steady pace, filming the pitch.

His friend Zoya is watching over his shoulder. "Now push the stick left," she says. "Make it drift north as well, but don't touch the other stick."

Aditya pushes it. The drone keeps its eastward pace, and starts picking up speed towards the north, faster every second.

"Easy to predict," says Zoya. "It'll just head off in a straight slanting line, halfway between east and north."

Aditya isn't so sure. The drone keeps its eastward speed but its northward speed keeps growing. After three seconds of this, where exactly will it be, and what path does it take to get there?

## The physics

When the acceleration $\vec{a}$ is **constant** (same size and direction), the equations of motion from a straight line carry over to a plane in **vector form**:

$$\vec{v} = \vec{v}_0 + \vec{a}\,t$$
$$\vec{r} = \vec{r}_0 + \vec{v}_0\,t + \tfrac{1}{2}\vec{a}\,t^2$$

Here $\vec{r}_0$ and $\vec{v}_0$ are the position and velocity at $t = 0$.

![Position vectors r0, v0 t and half a t squared drawn head to tail to give r, with the actual curved path dotted](figures/motion_plane_constant_acceleration/position-vector-sum.svg "The three pieces of the position equation added head to tail. The actual path curves, because the half-a-t-squared piece grows faster than the others.")

The key idea is that each vector equation is really **two ordinary equations**, one per axis, that don't affect each other:

$$x = x_0 + v_{0x}t + \tfrac{1}{2}a_x t^2, \qquad y = y_0 + v_{0y}t + \tfrac{1}{2}a_y t^2$$

and likewise $v_x = v_{0x} + a_x t$, $v_y = v_{0y} + a_y t$. The $x$-motion only knows about $x$-quantities, and the $y$-motion only about $y$-quantities.

For Aditya's drone, take $x$ east and $y$ north, both horizontal. Pushing the stick tilts the drone so its rotors give it a northward acceleration; nothing changes along $x$. So the $x$-motion is steady, and the $y$-motion starts from zero and speeds up. Because $y$ grows as $t^2$ while $x$ grows as $t$, the path is not a straight line but a curve bending towards the north. Zoya's straight line is wrong.

## Worked example

**Given (illustrative):** at $t = 0$ the drone is at the origin moving east at $\vec{v}_0 = 4\hat{i}$ m/s; the push gives $\vec{a} = 2\hat{j}\,\text{m/s}^2$, held for $t = 3\,\text{s}$.
**Find:** its position and velocity at $t = 3\,\text{s}$.

1. East ($x$), no acceleration: $x = v_{0x}t = 4 \times 3 = 12\,\text{m}$.
2. North ($y$), from rest: $y = \tfrac{1}{2}a_y t^2 = \tfrac{1}{2} \times 2 \times 3^2 = 9\,\text{m}$.
   So $\vec{r} = 12\hat{i} + 9\hat{j}$ m, a straight-line distance of $\sqrt{12^2 + 9^2} = 15\,\text{m}$ from where the push began: about the length of a bus.
3. Velocity: $\vec{v} = 4\hat{i} + (2 \times 3)\hat{j} = 4\hat{i} + 6\hat{j}$ m/s. The drone now moves faster north than east.

**Sanity check:** after one second it would be at $4\hat{i} + 1\hat{j}$ m, barely north of its line; after three, $9\,\text{m}$ north. The northward drift speeds up, so the path curves, as expected.

## Where the picture breaks

A real drone doesn't switch its acceleration on and off instantly, and its flight controller constantly adjusts the thrust, so "constant acceleration" is only roughly true for a few seconds. Air drag grows with speed and would slowly eat into both components. Wind would add its own velocity to everything. The vector equations are exact whenever the acceleration really is constant; the drone only approximates that.

## Key takeaway

With constant acceleration, $\vec{v} = \vec{v}_0 + \vec{a}t$ and $\vec{r} = \vec{r}_0 + \vec{v}_0 t + \tfrac{1}{2}\vec{a}t^2$. Split them into $x$ and $y$ equations and solve each on its own: the two directions don't interfere. When the acceleration is at an angle to the starting velocity, the path curves.
