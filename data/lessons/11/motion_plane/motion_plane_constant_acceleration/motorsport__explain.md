---
concept_id: motion_plane_constant_acceleration
interest: motorsport
format: explain
title: One equation for a car that brakes and drifts sideways
check:
  question: |-
    Seen from above, a car starts at the origin with $\vec{v}_0 = 30\hat{i}\,\text{m/s}$ and has a constant acceleration $\vec{a} = (-5.0\hat{i} + 2.0\hat{j})\,\text{m/s}^2$. Where is it after $2.0\,\text{s}$?
  options:
    A: |-
      $(60\hat{i} + 0\hat{j})\,\text{m}$
    B: |-
      $(50\hat{i} + 4.0\hat{j})\,\text{m}$
    C: |-
      $(40\hat{i} + 8.0\hat{j})\,\text{m}$
    D: |-
      $(70\hat{i} + 4.0\hat{j})\,\text{m}$
  answer: B
  explanation: |-
    $x = 30(2.0) + \tfrac{1}{2}(-5.0)(2.0)^2 = 60 - 10 = 50\,\text{m}$ and $y = 0 + \tfrac{1}{2}(2.0)(2.0)^2 = 4.0\,\text{m}$.
  misconceptions:
    A: |-
      Ignores the acceleration and uses $\vec{r} = \vec{r}_0 + \vec{v}_0 t$, as if the velocity stayed constant for the whole $2.0\,\text{s}$.
    C: |-
      Drops the factor $\tfrac{1}{2}$ and uses $\vec{a}t^2$, which doubles the effect of the acceleration in both directions.
    D: |-
      Loses the minus sign on $a_x$ and speeds the car up instead of slowing it. The sign of a component is its direction.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race circuit seen from above: cars on the straights, one car sweeping through a curved corner, and a trackside replay screen showing a car arcing over a crest](scenes/motorsport/motion_plane.svg "Seen from above, a car that is slowing down and sliding sideways at the same time traces out a curve, not a line.")

Harsh and his co-driver Tanvi are running a new car up and down an old test road for a club endurance event. The last two kilometres cross a long, exposed bridge, and today the wind is coming hard off the river, side-on.

Tanvi is watching the data logger. On the bridge, Harsh brakes for the far end — and on the screen the car's path, drawn from above, is not the straight line it feels like from inside. It bends steadily towards the downwind kerb, even though Harsh insists he never turned the wheel.

"So the computer is drawing two things at once," Tanvi says. "You're slowing down, hard. And the wind is pushing you sideways the whole time. Does it need a different formula for each?"

Harsh shrugs. "It's one car. It should be one equation."

Can a single equation handle a car that is braking in one direction and drifting in another at the same time?

## The physics

In one dimension, for constant acceleration, you already know $v = u + at$ and $x = x_0 + ut + \tfrac{1}{2}at^2$. In a plane the same two equations hold, with every quantity a vector. For a **constant acceleration** $\vec{a}$ — constant in size *and* direction:

$$\vec{v} = \vec{v}_0 + \vec{a}\,t$$

$$\vec{r} = \vec{r}_0 + \vec{v}_0\,t + \tfrac{1}{2}\vec{a}\,t^2$$

Here $\vec{r}_0$ and $\vec{v}_0$ are the position and velocity at $t = 0$. Each term on the right is a vector, and the final position is found by laying them head to tail.

![The origin, then the starting position, then v0 t and half a t squared drawn head to tail, reaching the final position, with the actual curved path shown dotted](figures/motion_plane_constant_acceleration/position-vector-sum.svg "The position at time t is r0 plus v0 t plus half a t squared, added head to tail. The dotted path curves because the acceleration keeps bending the velocity away from its starting direction.")

Written with unit vectors, each vector equation splits into two ordinary equations, one per axis:

$$x = x_0 + v_{0x}t + \tfrac{1}{2}a_x t^2, \qquad y = y_0 + v_{0y}t + \tfrac{1}{2}a_y t^2$$

$$v_x = v_{0x} + a_x t, \qquad v_y = v_{0y} + a_y t$$

This is the key idea: **the $x$-motion and the $y$-motion are independent**. The $x$ equations contain only $x$-components and the $y$ equations only $y$-components. Motion in a plane is two straight-line motions happening at once, sharing one clock $t$.

For Harsh's car, seen from above, take $\hat{i}$ along the bridge and $\hat{j}$ across it, downwind. Braking gives a negative $a_x$, which eats away the forward speed. The crosswind gives a steady sideways force and so a small positive $a_y$, which builds a sideways velocity up from zero — and that is what bends the path. Gravity acts perpendicular to this top view, so it changes neither $x$ nor $y$.

## Worked example

**Given (illustrative):** at $t = 0$ the car is at the origin with $\vec{v}_0 = 24\hat{i}\,\text{m/s}$ (about $86\,\text{km/h}$ along the bridge). Braking and a steady crosswind together give a constant $\vec{a} = (-6.0\hat{i} + 1.0\hat{j})\,\text{m/s}^2$.
**Find:** the position and velocity $2.0\,\text{s}$ later.

Along the bridge ($x$):
$$x = 24(2.0) + \tfrac{1}{2}(-6.0)(2.0)^2 = 48 - 12 = 36\,\text{m}$$

So braking has cost $12\,\text{m}$ compared with carrying straight on at $24\,\text{m/s}$.

Across the bridge ($y$), starting with no sideways velocity at all:
$$y = 0 + \tfrac{1}{2}(1.0)(2.0)^2 = 2.0\,\text{m}$$

About half a lane's width — exactly the drift Tanvi saw on the screen.

The velocity after $2.0\,\text{s}$:
$$\vec{v} = \left[24 + (-6.0)(2.0)\right]\hat{i} + \left[0 + (1.0)(2.0)\right]\hat{j} = (12\hat{i} + 2.0\hat{j})\,\text{m/s}$$

**Sanity check:** the forward speed has halved, from $24$ to $12\,\text{m/s}$, which is what $6.0\,\text{m/s}^2$ of braking does in $2.0\,\text{s}$. The sideways drift of $2.0\,\text{m}$ is small beside the $36\,\text{m}$ travelled forward, which is why the path looks *nearly* straight — a gentle bend, not a swerve.

## Where the picture breaks

The acceleration of a real car on a windy bridge is **not** constant. Braking force varies as weight shifts onto the front tyres, and wind gusts rather than pushing steadily, so $\vec{a}$ is an average over the two seconds rather than a fixed arrow. A real driver also feels the drift and steers against it, adding a sideways acceleration of the opposite sign that straightens the path again. And the top view leaves out the vertical direction: the road's camber and bumps would need a third component.

## Key takeaway

For constant acceleration in a plane, $\vec{v} = \vec{v}_0 + \vec{a}t$ and $\vec{r} = \vec{r}_0 + \vec{v}_0 t + \tfrac{1}{2}\vec{a}t^2$. Split them into $x$ and $y$ equations and solve each as ordinary one-dimensional motion on the same clock: perpendicular motions never interfere with each other.
