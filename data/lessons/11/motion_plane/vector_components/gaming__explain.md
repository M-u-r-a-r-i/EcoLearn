---
concept_id: vector_components
interest: gaming
format: explain
title: Why the hero ran faster diagonally
check:
  question: |-
    A game character moves at $8.0\,\text{m/s}$ in a direction $30^\circ$ above the positive $x$-axis of the map. What is the $x$-component of its velocity?
  options:
    A: |-
      $6.9\,\text{m/s}$
    B: |-
      $4.0\,\text{m/s}$
    C: |-
      $8.0\,\text{m/s}$
    D: |-
      $5.7\,\text{m/s}$
  answer: A
  explanation: |-
    The component along the axis the angle is measured from uses the cosine: $v_x = v\cos 30^\circ = 8.0 \times 0.866 \approx 6.9\,\text{m/s}$. (The $y$-component is $v\sin 30^\circ = 4.0\,\text{m/s}$.)
  misconceptions:
    B: |-
      Swaps sine and cosine. The angle is measured from the $x$-axis, so the $x$-component is the adjacent side of the triangle, $v\cos\theta$, not $v\sin\theta$.
    C: |-
      Thinks the whole velocity lies along $x$ because the motion is "mostly sideways". A component is always smaller than the vector unless the vector lies along that axis.
    D: |-
      Splits the vector equally between the two axes, dividing by $\sqrt{2}$. That is only right for a direction at $45^\circ$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: the monitor shows an artillery game with a shell flying along a curved arc; a tablet shows a top-down minimap of a circular kart track](scenes/gaming/motion_plane.svg "A game engine stores every motion as a pair of numbers: how much along x and how much along y.")

Farhan is building a top-down dungeon game for his computer club. His code is simple: holding **right** sets the hero's sideways velocity to $5\,\text{m/s}$, and holding **up** sets the forward velocity to $5\,\text{m/s}$.

His friend Lavanya playtests it for two minutes and grins. "I've found a speed hack. Hold right and up together."

Farhan times it. Running straight across a room takes a certain time. Running diagonally, holding both keys, the hero covers noticeably more ground in the same time. Speedrunners in his club have already started zig-zagging everywhere.

"But each key only gives five," Farhan protests. "Five is five."

Is the diagonal hero really faster? And how should Farhan split one speed between two directions so that every direction is fair?

## The physics

Any vector in a plane can be replaced by two perpendicular vectors that add up to it, one along the $x$-axis and one along the $y$-axis. These are its **components**, and finding them is called **resolving** the vector.

If a vector $\vec{A}$ has magnitude $A$ and makes an angle $\theta$ with the $x$-axis, then from the right-angled triangle

$$A_x = A\cos\theta, \qquad A_y = A\sin\theta$$

Going back the other way, the components rebuild the vector:

$$A = \sqrt{A_x^2 + A_y^2}, \qquad \tan\theta = \frac{A_y}{A_x}$$

![A vector A at angle theta to the x-axis, with dashed lines dropping to each axis. The x-component A cos theta and the y-component A sin theta are drawn along the axes](figures/vector_components/resolving-a-vector.svg "Resolving: drop perpendiculars from the vector's head to each axis. The two components added head to tail rebuild the original vector exactly.")

A component can be positive or negative (for a vector pointing left, $A_x < 0$), and each component is never larger than the vector itself.

Now look at Farhan's code. It sets the **components**, not the speed. Holding one key gives $v_x = 5$, $v_y = 0$: speed $5\,\text{m/s}$. Holding both gives $v_x = 5$ and $v_y = 5$, so the actual speed is

$$v = \sqrt{5^2 + 5^2} = 5\sqrt{2} \approx 7.1\,\text{m/s}$$

at $45^\circ$. Lavanya's hack is real: diagonal running is about $41\%$ faster.

The fair fix is to choose the speed first and resolve it. For $5\,\text{m/s}$ at $45^\circ$, each component should be $5\cos 45^\circ \approx 3.5\,\text{m/s}$, not $5$.

## Worked example

**Given (illustrative):** the fixed game moves the hero at $v = 6.0\,\text{m/s}$ in a direction $30^\circ$ above the $x$-axis.
**Find:** $v_x$ and $v_y$, then rebuild the velocity from them as a check.

Resolve, measuring the angle from the $x$-axis:
$$v_x = 6.0\cos 30^\circ = 6.0 \times 0.866 \approx 5.2\,\text{m/s}$$
$$v_y = 6.0\sin 30^\circ = 6.0 \times 0.5 = 3.0\,\text{m/s}$$

Rebuild:
$$v = \sqrt{5.196^2 + 3.0^2} = \sqrt{27.0 + 9.0} = \sqrt{36.0} = 6.0\,\text{m/s}, \qquad \tan\theta = \frac{3.0}{5.196} = 0.577 \Rightarrow \theta = 30^\circ$$

**Sanity check:** the direction is closer to $x$ than to $y$, so the $x$-component should be the bigger one, and it is. Each component is smaller than $6.0\,\text{m/s}$.

## Where the picture breaks

A real person running diagonally doesn't get a bonus: legs push the body along one direction at a time, and the speed limit is the same whichever way you face. Farhan's bug existed only because his code treated $x$ and $y$ as two separate "engines". The axes themselves are also a choice. Here they follow the map's edges, but any pair of perpendicular axes works; the components change with the axes, while the vector stays the same. Many games fix this bug by scaling the input to length one, which is exactly the idea of a unit vector, the next lesson.

## Key takeaway

Any vector can be resolved into perpendicular components, $A_x = A\cos\theta$ and $A_y = A\sin\theta$, with $\theta$ measured from the $x$-axis. The components rebuild the vector through $A = \sqrt{A_x^2 + A_y^2}$ and $\tan\theta = A_y/A_x$. Setting both components to the full speed makes a diagonal speed of $\sqrt{2}$ times too much.
