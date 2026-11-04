---
concept_id: unit_vectors
interest: motorsport
format: explain
title: Telling the recovery truck exactly where the car is
check:
  question: |-
    On a circuit map, marshal post P is at $\vec{r}_P = (50\hat{i} + 20\hat{j})\,\text{m}$ and post Q is at $\vec{r}_Q = (20\hat{i} + 60\hat{j})\,\text{m}$. What is the displacement from P to Q?
  options:
    A: |-
      $(70\hat{i} + 80\hat{j})\,\text{m}$
    B: |-
      $(30\hat{i} - 40\hat{j})\,\text{m}$
    C: |-
      $(-0.6\hat{i} + 0.8\hat{j})\,\text{m}$
    D: |-
      $(-30\hat{i} + 40\hat{j})\,\text{m}$
  answer: D
  explanation: |-
    A displacement is final position minus initial position: $\vec{r}_Q - \vec{r}_P = (20 - 50)\hat{i} + (60 - 20)\hat{j} = (-30\hat{i} + 40\hat{j})\,\text{m}$, an arrow $50\,\text{m}$ long.
  misconceptions:
    A: |-
      Adds the two position vectors instead of subtracting them. A displacement is a *change* of position, so it is final minus initial.
    B: |-
      Subtracts the wrong way round (initial minus final). That is the displacement from Q to P: right size, opposite direction.
    C: |-
      Gives the unit vector along the displacement rather than the displacement itself. A unit vector has length 1 and carries only the direction; this displacement is $50\,\text{m}$ long.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race circuit seen from above: cars on the straights, one car sweeping through a curved corner, and a trackside replay screen showing a car arcing over a crest](scenes/motorsport/motion_plane.svg "Seen from above, every point on a circuit is just a pair of numbers — and a pair of numbers is not yet a direction.")

Ira runs race control at a small circuit outside Pune. On the wall is a survey map of the track with a grid over it, measured from a corner of the paddock: metres east, metres north.

Mid-session, a car stops at the exit of Turn 3. She calls the recovery truck.

"Car's at two hundred, two sixty," she says, reading the grid.

Sameer, who drives the truck, is parked by the paddock gate at eighty, one hundred. "Madam," he says, "that's four numbers. I can't drive to four numbers. Which way do I point the truck, how far is it, and how long will it take me?"

Ira looks at the two pairs on the screen. They contain everything he needs — but not in a form he can steer by. How do you turn two coordinates into a direction and a distance?

## The physics

Choose two perpendicular axes, and put a **unit vector** along each: $\hat{i}$ along $x$, $\hat{j}$ along $y$. A unit vector has magnitude exactly 1 and **no unit** of its own. Its only job is to point.

Any vector in the plane can then be written from its components:

$$\vec{A} = A_x\hat{i} + A_y\hat{j}$$

Here $A_x\hat{i}$ is the $x$-component vector: the number $A_x$ carries the size and the sign, and $\hat{i}$ carries the direction. On Ira's map, $\hat{i}$ points east and $\hat{j}$ points north, with the origin at the paddock corner.

The payoff is that vector algebra becomes ordinary arithmetic, one component at a time:

- **Add or subtract:** $\vec{A} \pm \vec{B} = (A_x \pm B_x)\hat{i} + (A_y \pm B_y)\hat{j}$
- **Scale by a number $\lambda$:** $\lambda\vec{A} = \lambda A_x\hat{i} + \lambda A_y\hat{j}$
- **Magnitude:** $|\vec{A}| = \sqrt{A_x^2 + A_y^2}$
- **Unit vector along $\vec{A}$:** $\hat{A} = \vec{A}/|\vec{A}|$ — a length-1 arrow pointing the same way as $\vec{A}$

![A grid showing the unit vectors i-hat and j-hat, two vectors drawn head to tail, and their sum, whose components are the sums of the separate x and y parts](figures/unit_vectors/unit-vector-addition.svg "Adding in unit-vector form is just adding the x-parts and the y-parts separately. The drawing and the arithmetic give the same arrow.")

A **position vector** $\vec{r}$ points from the origin to a spot on the map. The **displacement** from spot 1 to spot 2 is final minus initial:

$$\Delta\vec{r} = \vec{r}_2 - \vec{r}_1$$

That single subtraction is what turns Sameer's four numbers into one instruction.

## Worked example

**Given:** the stopped car is at $\vec{r}_C = (200\hat{i} + 260\hat{j})\,\text{m}$ and the truck is at $\vec{r}_T = (80\hat{i} + 100\hat{j})\,\text{m}$, with $\hat{i}$ east and $\hat{j}$ north (illustrative).
**Find:** the displacement the truck must make, its length and direction, and its velocity if it drives straight there at $10\,\text{m/s}$.

Displacement, final minus initial:
$$\vec{d} = \vec{r}_C - \vec{r}_T = (200 - 80)\hat{i} + (260 - 100)\hat{j} = (120\hat{i} + 160\hat{j})\,\text{m}$$

Its length:
$$|\vec{d}| = \sqrt{120^2 + 160^2} = \sqrt{14\,400 + 25\,600} = \sqrt{40\,000} = 200\,\text{m}$$

Its direction, as a unit vector:
$$\hat{d} = \frac{\vec{d}}{|\vec{d}|} = \frac{120\hat{i} + 160\hat{j}}{200} = 0.6\hat{i} + 0.8\hat{j}$$

So Sameer drives $200\,\text{m}$ — about two football pitches end to end — heading east and north, more north than east.

His velocity is that direction scaled up to his speed:
$$\vec{v} = 10\,\hat{d} = (6.0\hat{i} + 8.0\hat{j})\,\text{m/s}$$

and the drive takes $200/10 = 20\,\text{s}$.

**Sanity check:** $|\hat{d}| = \sqrt{0.6^2 + 0.8^2} = \sqrt{1.00} = 1$, exactly as a unit vector must be, and $|\vec{v}| = \sqrt{6.0^2 + 8.0^2} = 10\,\text{m/s}$, the speed we put in.

## Where the picture breaks

The map is flat and two-dimensional, so it ignores the circuit's gradients and any banking. More importantly, $200\,\text{m}$ is the *straight-line* displacement, and a recovery truck cannot drive through the infield fence: it has to follow service roads, so the distance it really covers is longer and the $20\,\text{s}$ is a lower limit, not a prediction. Trucks also start from rest and slow at junctions rather than moving at a steady $10\,\text{m/s}$. The straight arrow is the shortest possible route — a useful benchmark, not the actual journey.

## Key takeaway

Unit vectors $\hat{i}$ and $\hat{j}$ have length 1 and simply point along the axes, so any vector can be written $\vec{A} = A_x\hat{i} + A_y\hat{j}$. Then you add, subtract and scale component by component, get the length from $\sqrt{A_x^2 + A_y^2}$, and get the pure direction from $\hat{A} = \vec{A}/|\vec{A}|$.
