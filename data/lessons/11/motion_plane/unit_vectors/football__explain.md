---
concept_id: unit_vectors
interest: football
format: explain
title: Turning a coach's tablet into passes you can play
check:
  question: |-
    On a tactics board, a midfielder stands at $\vec{r}_P = (40\hat{i} + 30\hat{j})\,\text{m}$ and a striker at $\vec{r}_Q = (52\hat{i} + 21\hat{j})\,\text{m}$. What is the displacement of a pass from the midfielder to the striker?
  options:
    A: |-
      $(92\hat{i} + 51\hat{j})\,\text{m}$
    B: |-
      $(-12\hat{i} + 9\hat{j})\,\text{m}$
    C: |-
      $(0.8\hat{i} - 0.6\hat{j})\,\text{m}$
    D: |-
      $(12\hat{i} - 9\hat{j})\,\text{m}$
  answer: D
  explanation: |-
    Displacement is final minus initial: $\vec{r}_Q - \vec{r}_P = (52 - 40)\hat{i} + (21 - 30)\hat{j} = (12\hat{i} - 9\hat{j})\,\text{m}$, a pass $15\,\text{m}$ long.
  misconceptions:
    A: |-
      Adds the two position vectors instead of subtracting them. A displacement is a change in position, final minus initial.
    B: |-
      Subtracts in the wrong order (initial minus final). That gives the pass from the striker back to the midfielder: the right length but the opposite direction.
    C: |-
      Gives the unit vector along the pass instead of the pass itself. A unit vector has length 1 and only shows direction; this pass is $15\,\text{m}$ long.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A player lofts the ball in an arc over the goalkeeper while a teammate jogs round the centre circle](scenes/football/motion_plane.svg "Every spot on the pitch can be named by two numbers, and every pass by a change in those numbers.")

The night before a cup semi-final, Coach Ayesha sends the squad a counter-attack on the team app. On her tactics board, every player is a dot, and every dot has two numbers: metres up the pitch from the corner flag by their own goal, and metres across from the left touchline.

Nandini, on the left wing, starts at $(60, 8)$. The ball goes from her to Karthik at $(72, 13)$, and from Karthik to the striker, Dev, at $(88, 25)$ (illustrative).

Dev messages the group: "Great, a list of numbers. But when I get the ball, how far has it come from Nandini, and in which direction? And how hard does Karthik have to hit his pass?"

Nandini stares at the dots. How do you turn pairs of numbers like these into lengths, directions and speeds?

## The physics

Choose two perpendicular axes and put a **unit vector** along each: $\hat{i}$ along $x$ and $\hat{j}$ along $y$. A unit vector has magnitude exactly 1 and **no unit**. Its only job is to point in a direction. On Ayesha's board, $\hat{i}$ points up the pitch and $\hat{j}$ points across it, from the left touchline, with the origin at the corner flag.

Any vector in the plane can then be written in terms of its components:

$$\vec{A} = A_x\hat{i} + A_y\hat{j}$$

The number $A_x$ carries the size and sign of the $x$-part, and $\hat{i}$ carries its direction. Nandini's dot, for example, is the **position vector** $\vec{r}_1 = (60\hat{i} + 8\hat{j})\,\text{m}$: the arrow from the corner flag to her.

Vector algebra now becomes ordinary arithmetic, one component at a time:

- **Add or subtract:** $\vec{A} \pm \vec{B} = (A_x \pm B_x)\hat{i} + (A_y \pm B_y)\hat{j}$
- **Scale by a number $\lambda$:** $\lambda\vec{A} = \lambda A_x\hat{i} + \lambda A_y\hat{j}$
- **Magnitude:** $|\vec{A}| = \sqrt{A_x^2 + A_y^2}$
- **Unit vector along $\vec{A}$:** $\hat{A} = \vec{A}/|\vec{A}|$, a length-1 arrow pointing the same way as $\vec{A}$.

![A grid showing unit vectors i-hat and j-hat, A = 3i + 1j, B = 1i + 2j drawn head to tail, and their sum 4i + 3j of length 5](figures/unit_vectors/unit-vector-addition.svg "Adding in unit-vector form means adding the x-parts and the y-parts separately. The drawing and the arithmetic give the same arrow.")

The **displacement** from one spot to another is final minus initial: $\Delta\vec{r} = \vec{r}_2 - \vec{r}_1$. That is a pass, written as a vector.

## Worked example

**Given:** $\vec{r}_1 = (60\hat{i} + 8\hat{j})\,\text{m}$ (Nandini), $\vec{r}_2 = (72\hat{i} + 13\hat{j})\,\text{m}$ (Karthik), $\vec{r}_3 = (88\hat{i} + 25\hat{j})\,\text{m}$ (Dev).
**Find:** each pass as a vector, the ball's total displacement, and Karthik's pass velocity if he plays it along the ground at $15\,\text{m/s}$.

Subtract to get each pass:
$$\vec{d}_1 = \vec{r}_2 - \vec{r}_1 = (12\hat{i} + 5\hat{j})\,\text{m}, \qquad |\vec{d}_1| = \sqrt{144 + 25} = 13\,\text{m}$$
$$\vec{d}_2 = \vec{r}_3 - \vec{r}_2 = (16\hat{i} + 12\hat{j})\,\text{m}, \qquad |\vec{d}_2| = \sqrt{256 + 144} = 20\,\text{m}$$

Add them for the whole move:
$$\vec{d} = \vec{d}_1 + \vec{d}_2 = (28\hat{i} + 17\hat{j})\,\text{m}, \qquad |\vec{d}| = \sqrt{784 + 289} = \sqrt{1073} \approx 32.8\,\text{m}$$

Direction of Karthik's pass, as a unit vector, then scaled by the speed:
$$\hat{d}_2 = \frac{16\hat{i} + 12\hat{j}}{20} = 0.8\hat{i} + 0.6\hat{j}, \qquad \vec{v} = 15\,\hat{d}_2 = (12\hat{i} + 9\hat{j})\,\text{m/s}$$

The ball takes about $20/15 \approx 1.3\,\text{s}$ to reach Dev.

**Sanity check:** $\vec{d}$ equals $\vec{r}_3 - \vec{r}_1 = (28\hat{i} + 17\hat{j})\,\text{m}$ directly, as it must. And $|\hat{d}_2| = \sqrt{0.64 + 0.36} = 1$, and $|\vec{v}| = \sqrt{144 + 81} = 15\,\text{m/s}$.

## Where the picture breaks

The tactics board is flat, so it ignores a lofted pass's height. Players are dots, but real players are moving while the ball travels, so a pass aimed at where Dev *is* would miss where he *will be*; you'll handle that with relative velocity. Real passes also slow down on the grass, so $15\,\text{m/s}$ can only be an average.

## Key takeaway

Unit vectors $\hat{i}$ and $\hat{j}$ have length 1 and simply point along the axes, so any vector can be written $\vec{A} = A_x\hat{i} + A_y\hat{j}$. Add, subtract and scale vectors component by component, find a length with $\sqrt{A_x^2 + A_y^2}$, and find a direction with $\hat{A} = \vec{A}/|\vec{A}|$.
