---
concept_id: unit_vectors
interest: cricket
format: explain
title: Telling a fielder exactly where to run
check:
  question: |-
    On a ball-tracking map, fielder P stands at $\vec{r}_P = (30\hat{i} + 10\hat{j})\,\text{m}$ and fielder Q at $\vec{r}_Q = (10\hat{i} + 25\hat{j})\,\text{m}$. What is the displacement from P to Q?
  options:
    A: |-
      $(40\hat{i} + 35\hat{j})\,\text{m}$
    B: |-
      $(-20\hat{i} + 15\hat{j})\,\text{m}$
    C: |-
      $(20\hat{i} - 15\hat{j})\,\text{m}$
    D: |-
      $(-0.8\hat{i} + 0.6\hat{j})\,\text{m}$
  answer: B
  explanation: |-
    Displacement from P to Q is final minus initial: $\vec{r}_Q - \vec{r}_P = (10 - 30)\hat{i} + (25 - 10)\hat{j} = (-20\hat{i} + 15\hat{j})\,\text{m}$, which is $25\,\text{m}$ long.
  misconceptions:
    A: |-
      Adds the two position vectors instead of subtracting them. A displacement is a change in position, so it is final minus initial.
    C: |-
      Subtracts in the wrong order (initial minus final). That gives the displacement from Q to P: the right size but the opposite direction.
    D: |-
      Gives the unit vector in the right direction instead of the displacement. A unit vector has length 1 and only shows direction; the displacement is $25\,\text{m}$ long.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A day match: a batter lofts the ball towards the boundary as a fielder races along the rope](scenes/cricket/motion_plane.svg "Ball-tracking screens turn every spot on the field into a pair of numbers.")

Sneha does the analysis for her club's under-19 side. Her tablet app records, for every ball, where it was stopped, as two numbers measured from the striker's stumps: metres straight down the ground, and metres square to the leg side.

After a close loss, the captain, Arjun, points at one boundary on her screen. "Our fielder was standing *right there*. Why didn't he get to it?"

Sneha reads off the numbers. The ball crossed the rope at $(40, 30)$. The fielder had been standing at $(25, 50)$.

"Fine," says Arjun, "but that's four numbers. He can't run to four numbers. Which way should he have gone, how far, and how fast would he have needed to be?"

Sneha stares at the pairs. How do you turn coordinates like these into a direction and a distance?

## The physics

Choose two perpendicular axes, and along each put a **unit vector**: $\hat{i}$ along $x$ and $\hat{j}$ along $y$. A unit vector has magnitude exactly 1 and **no unit**. Its only job is to point in a direction.

Any vector in the plane can then be written in terms of its components:

$$\vec{A} = A_x\hat{i} + A_y\hat{j}$$

Here $A_x\hat{i}$ is the $x$-component vector: the number $A_x$ carries the size (and sign), and $\hat{i}$ carries the direction. On Sneha's map, $\hat{i}$ points straight down the ground and $\hat{j}$ points square to the leg side, with the origin at the striker's stumps.

The payoff is that vector algebra turns into ordinary arithmetic, one component at a time:

- **Add or subtract:** $\vec{A} \pm \vec{B} = (A_x \pm B_x)\hat{i} + (A_y \pm B_y)\hat{j}$
- **Scale by a number $\lambda$:** $\lambda\vec{A} = \lambda A_x\hat{i} + \lambda A_y\hat{j}$
- **Magnitude:** $|\vec{A}| = \sqrt{A_x^2 + A_y^2}$
- **Unit vector along $\vec{A}$:** $\hat{A} = \vec{A}/|\vec{A}|$, a length-1 arrow pointing the same way as $\vec{A}$.

![A grid showing unit vectors i-hat and j-hat, A = 3i + 1j, B = 1i + 2j drawn head to tail, and their sum 4i + 3j of length 5](figures/unit_vectors/unit-vector-addition.svg "Adding in unit-vector form is just adding x-parts and y-parts separately. The drawing and the arithmetic give the same arrow.")

A **position vector** $\vec{r}$ points from the origin to a spot. The **displacement** from spot 1 to spot 2 is final minus initial: $\Delta\vec{r} = \vec{r}_2 - \vec{r}_1$.

## Worked example

**Given:** ball crossed the rope at $\vec{r}_B = (40\hat{i} + 30\hat{j})\,\text{m}$; fielder started at $\vec{r}_F = (25\hat{i} + 50\hat{j})\,\text{m}$ (illustrative).
**Find:** the displacement he needed, its length and direction, and his velocity if he had run straight there at $7.0\,\text{m/s}$.

Displacement, final minus initial:
$$\vec{d} = \vec{r}_B - \vec{r}_F = (40 - 25)\hat{i} + (30 - 50)\hat{j} = (15\hat{i} - 20\hat{j})\,\text{m}$$

Length:
$$|\vec{d}| = \sqrt{15^2 + (-20)^2} = \sqrt{225 + 400} = \sqrt{625} = 25\,\text{m}$$

Direction, as a unit vector:
$$\hat{d} = \frac{\vec{d}}{|\vec{d}|} = \frac{15\hat{i} - 20\hat{j}}{25} = 0.6\hat{i} - 0.8\hat{j}$$

So he should have run $25\,\text{m}$ towards the rope and back towards the off side ($-\hat{j}$).

Velocity at $7.0\,\text{m/s}$ along $\hat{d}$, scaling the unit vector:
$$\vec{v} = 7.0\,\hat{d} = (4.2\hat{i} - 5.6\hat{j})\,\text{m/s}$$

He would have needed $25/7.0 \approx 3.6\,\text{s}$.

**Sanity check:** $|\hat{d}| = \sqrt{0.6^2 + 0.8^2} = \sqrt{0.36 + 0.64} = 1$, as a unit vector must be, and $|\vec{v}| = \sqrt{4.2^2 + 5.6^2} = \sqrt{49} = 7.0\,\text{m/s}$.

## Where the picture breaks

The map is flat and two-dimensional, so it ignores the ball's height and any slope in the outfield. Real fielders don't run in a straight line at constant speed either: they accelerate from standing and curve to meet the ball, which is itself moving. The straight-line displacement is the *shortest* possible route, which makes it a useful benchmark rather than a description of the actual run.

## Key takeaway

Unit vectors $\hat{i}$ and $\hat{j}$ have length 1 and just point along the axes, so any vector can be written $\vec{A} = A_x\hat{i} + A_y\hat{j}$. Then you add, subtract and scale vectors component by component, find the length with $\sqrt{A_x^2 + A_y^2}$, and get a direction with $\hat{A} = \vec{A}/|\vec{A}|$.
