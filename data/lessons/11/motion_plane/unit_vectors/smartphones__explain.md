---
concept_id: unit_vectors
interest: smartphones
format: explain
title: How the robot vacuum finds its way home
check:
  question: |-
    On a robot vacuum's room map, $\vec{A} = 2\hat{i} + 3\hat{j}$ m and $\vec{B} = 4\hat{i} - 1\hat{j}$ m. What is $\vec{A} - \vec{B}$?
  options:
    A: |-
      $6\hat{i} + 2\hat{j}$ m
    B: |-
      $2\hat{i} - 4\hat{j}$ m
    C: |-
      $-2\hat{i} + 2\hat{j}$ m
    D: |-
      $-2\hat{i} + 4\hat{j}$ m
  answer: D
  explanation: |-
    Subtract component by component: $x$: $2 - 4 = -2$; $y$: $3 - (-1) = 4$. So $\vec{A} - \vec{B} = -2\hat{i} + 4\hat{j}$ m.
  misconceptions:
    A: |-
      Adds the vectors instead of subtracting them. $\vec{A} - \vec{B}$ means adding $-\vec{B}$, which flips the sign of each of $\vec{B}$'s components.
    B: |-
      Works out $\vec{B} - \vec{A}$, the reverse order. Vector subtraction is not commutative: swapping the order reverses the resulting arrow.
    C: |-
      Drops the minus sign on $\vec{B}$'s $y$-component, so it computes $3 - 1$ instead of $3 - (-1)$. A negative component is part of the vector and must be kept.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![An evening terrace: a phone in the foreground shows a map with a winding dashed route and a straight arrow from start to end](scenes/smartphones/motion_plane.svg "The phone's map draws the whole wandering route, but also a single straight arrow from start to end. That arrow is what you need to get back.")

Ira's family has a new robot vacuum, and she's watching it on the companion app. The app draws a map of the living room, and a dotted line appears wherever the robot goes: across under the sofa, a turn, a slant past the table leg, another turn.

Then its battery runs low, and the app shows "Returning to dock". The robot doesn't retrace its wandering path. It turns once and heads home in one straight line.

"How does it know which way?" Ira asks her brother Rohan. "It's been zig-zagging for twenty minutes."

"It keeps two numbers the whole time," says Rohan. "How far it is along the room, and how far across. That's all."

Two numbers to describe any arrow on the floor, and from them, the straight road home. How can a pair of numbers do everything a drawn arrow does?

## The physics

Pick two perpendicular axes, $x$ along one wall and $y$ along the other. A **unit vector** is a vector of size exactly 1, with no unit, that only marks a direction:

- $\hat{i}$ points along $+x$, and $\hat{j}$ points along $+y$.

Any vector in the plane can then be written in **component form**:

$$\vec{A} = A_x\hat{i} + A_y\hat{j}$$

where $A_x$ and $A_y$ are its components (carrying the units, and signs for direction). Its size is $A = \sqrt{A_x^2 + A_y^2}$.

The payoff is that all vector arithmetic reduces to arithmetic on each component separately, because $\hat{i}$ and $\hat{j}$ parts never mix:

- **Add:** $\vec{A} + \vec{B} = (A_x + B_x)\hat{i} + (A_y + B_y)\hat{j}$
- **Subtract:** $\vec{A} - \vec{B} = (A_x - B_x)\hat{i} + (A_y - B_y)\hat{j}$
- **Scale:** $k\vec{A} = kA_x\hat{i} + kA_y\hat{j}$. A negative $k$ reverses the direction.

![A grid with unit vectors i-hat and j-hat. A = 3i + 1j and B = 1i + 2j drawn head to tail, giving A + B = 4i + 3j of length 5](figures/unit_vectors/unit-vector-addition.svg "Adding in component form: add the x-parts, add the y-parts. No triangles or angles needed.")

This is exactly what the robot does. Every short straight stretch it drives is a small vector; it keeps a running total of the $\hat{i}$ parts and the $\hat{j}$ parts. That total is its displacement from the dock, however wiggly the route.

## Worked example

**Given (illustrative):** the dock is at the origin; $x$ runs along the long wall, $y$ along the short wall. The robot drives $\vec{A} = 3\hat{i} + 1\hat{j}$ m, then $\vec{B} = 1\hat{i} + 2\hat{j}$ m.
**Find:** where it is, how far from the dock, and the vector home.

1. Add the parts: $\vec{A} + \vec{B} = (3 + 1)\hat{i} + (1 + 2)\hat{j} = 4\hat{i} + 3\hat{j}$ m. The robot is 4 m along the room and 3 m across.
2. Distance from the dock: $\sqrt{4^2 + 3^2} = \sqrt{25} = 5\,\text{m}$, about the length of a small car.
3. The way home is the same arrow reversed, scaling by $-1$: $-(4\hat{i} + 3\hat{j}) = -4\hat{i} - 3\hat{j}$ m.

**Sanity check:** adding the trip and the way home, $(4 - 4)\hat{i} + (3 - 3)\hat{j} = 0$, so the robot ends back at the dock.

## Where the picture breaks

A real robot vacuum's running total drifts: wheels slip on rugs, so it corrects its position with sensors that look at the walls around it. Its routes aren't made of a few neat vectors but of thousands of tiny ones, and the "straight line home" must bend round the sofa. And the floor is only two-dimensional because the robot stays on it; a drone would need a third unit vector, $\hat{k}$, pointing up. The component rules themselves are exact.

## Key takeaway

Unit vectors $\hat{i}$ and $\hat{j}$ have size 1 and just point along the axes, so any vector can be written $\vec{A} = A_x\hat{i} + A_y\hat{j}$. Then adding, subtracting and scaling vectors is just doing the same to the $x$-parts and the $y$-parts separately, keeping their signs.
