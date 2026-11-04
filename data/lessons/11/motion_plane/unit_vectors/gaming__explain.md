---
concept_id: unit_vectors
interest: gaming
format: explain
title: Teaching a game enemy which way to walk
check:
  question: |-
    In a game's coordinate system, a vector $\vec{A} = 3\hat{i} + 4\hat{j}$ points to the player and $\vec{B} = \hat{i} - 2\hat{j}$ points to a pickup (both in metres). What is $\vec{A} - \vec{B}$?
  options:
    A: |-
      $4\hat{i} + 2\hat{j}$
    B: |-
      $2\hat{i} + 2\hat{j}$
    C: |-
      $2\hat{i} + 6\hat{j}$
    D: |-
      $-2\hat{i} - 6\hat{j}$
  answer: C
  explanation: |-
    Subtract matching parts: $x$-part $3 - 1 = 2$, $y$-part $4 - (-2) = 6$. So $\vec{A} - \vec{B} = 2\hat{i} + 6\hat{j}$.
  misconceptions:
    A: |-
      Adds the vectors instead of subtracting them. That gives $\vec{A} + \vec{B}$.
    B: |-
      Drops the minus sign on $B_y$ and works out $4 - 2$. Subtracting a negative component adds it: $4 - (-2) = 6$.
    D: |-
      Subtracts in the wrong order, finding $\vec{B} - \vec{A}$. That is the same size but points the opposite way.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: the monitor shows an artillery game with a shell flying along a curved arc; a tablet shows a top-down minimap of a circular kart track](scenes/gaming/motion_plane.svg "Every spot in a game world is a pair of coordinates, and every movement is a vector the code can add and scale.")

Nisha is coding her first enemy for a game-jam: a slime that crawls towards the player. Her idea is neat. Each frame, subtract the slime's position from the player's position, and move the slime along the result.

It works, sort of. When the player is far away, the slime charges across the room at terrifying speed. When the player is close, it barely moves, creeping the last few metres like it is out of battery. Her playtester, Kunal, keeps luring it from far away just to watch it zoom.

"It should crawl at the same speed all the time," Nisha says, staring at her code. "The direction is right. The speed is wrong."

Her vector clearly carries the right direction but the wrong size. How can she keep one and throw away the other?

## The physics

A **unit vector** has magnitude exactly $1$ and no unit. Its only job is to point. Along the $x$- and $y$-axes we use

$$\hat{i} \text{ (along } +x\text{)}, \qquad \hat{j} \text{ (along } +y\text{)}$$

Any vector in the plane can then be written from its components:

$$\vec{A} = A_x\hat{i} + A_y\hat{j}$$

This notation turns vector arithmetic into bookkeeping on matching parts:

- **Add:** $\vec{A} + \vec{B} = (A_x + B_x)\hat{i} + (A_y + B_y)\hat{j}$
- **Subtract:** $\vec{A} - \vec{B} = (A_x - B_x)\hat{i} + (A_y - B_y)\hat{j}$
- **Scale by a number $k$:** $k\vec{A} = kA_x\hat{i} + kA_y\hat{j}$

![A grid showing unit vectors i-hat and j-hat, A = 3i + 1j, B = 1i + 2j drawn head to tail, and their sum 4i + 3j of length 5](figures/unit_vectors/unit-vector-addition.svg "Adding in unit-vector form is just adding x-parts and y-parts separately. The drawing and the arithmetic give the same arrow.")

Any vector also has a unit vector in its own direction: divide it by its magnitude,

$$\hat{A} = \frac{\vec{A}}{A}, \qquad A = \sqrt{A_x^2 + A_y^2}$$

That is Nisha's fix, a step game programmers call **normalising**. Her difference vector $\vec{d}$ has the right direction but a size equal to the distance, which is why the far-away slime zoomed. Divide by that distance to get $\hat{d}$, of length $1$, then scale by the speed she wants: $\vec{v} = v\,\hat{d}$.

## Worked example

**Given (illustrative):** the slime is at $\vec{r}_s = 2\hat{i} + 1\hat{j}$ and the player at $\vec{r}_p = 8\hat{i} + 9\hat{j}$ (metres). The slime should crawl at $4.0\,\text{m/s}$.
**Find:** the slime's velocity, and its position $0.50\,\text{s}$ later (player standing still).

Subtract to get the vector from slime to player:
$$\vec{d} = \vec{r}_p - \vec{r}_s = (8 - 2)\hat{i} + (9 - 1)\hat{j} = 6\hat{i} + 8\hat{j}\ \text{m}$$

Its magnitude is $d = \sqrt{6^2 + 8^2} = 10\,\text{m}$, so the unit vector is
$$\hat{d} = \frac{6\hat{i} + 8\hat{j}}{10} = 0.6\hat{i} + 0.8\hat{j}$$

Scale by the speed:
$$\vec{v} = 4.0(0.6\hat{i} + 0.8\hat{j}) = 2.4\hat{i} + 3.2\hat{j}\ \text{m/s}$$

After $0.50\,\text{s}$ the slime has moved $0.50\,\vec{v} = 1.2\hat{i} + 1.6\hat{j}$, so it is at
$$\vec{r}_s' = (2 + 1.2)\hat{i} + (1 + 1.6)\hat{j} = 3.2\hat{i} + 2.6\hat{j}\ \text{m}$$

**Sanity check:** $|\hat{d}| = \sqrt{0.36 + 0.64} = 1$, and $|\vec{v}| = \sqrt{2.4^2 + 3.2^2} = \sqrt{16} = 4.0\,\text{m/s}$, the speed we asked for. The slime moved $2.0\,\text{m}$ in $0.50\,\text{s}$, straight towards the player.

## Where the picture breaks

Real games recompute the direction every frame (every $1/60\,\text{s}$ or so), so the slime follows a moving player along a curve; we took one frozen moment. When the slime reaches the player, $d = 0$ and dividing by zero would crash the code, which is why game code checks for that case. That is the one vector with no unit vector: the zero vector has no direction to keep. Games in 3D add $\hat{k}$ for the third axis, and the rules are the same.

## Key takeaway

$\hat{i}$ and $\hat{j}$ are unit vectors, length $1$, along $x$ and $y$, so any vector can be written $\vec{A} = A_x\hat{i} + A_y\hat{j}$. Adding, subtracting and scaling then act on the $\hat{i}$ and $\hat{j}$ parts separately. Dividing a vector by its magnitude gives a unit vector that keeps only its direction.
