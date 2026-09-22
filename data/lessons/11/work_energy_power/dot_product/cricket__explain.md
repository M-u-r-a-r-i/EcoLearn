---
concept_id: dot_product
interest: cricket
format: explain
title: Was that shot really straight at the fielder
check:
  question: |-
    A ball-tracking system gives a shot's horizontal velocity as $\vec{v} = (20\,\hat{i} + 15\,\hat{j})\,\text{m/s}$. The line from the batter to a boundary fielder has unit vector $\hat{n} = 0.6\,\hat{i} + 0.8\,\hat{j}$. What is the component of the ball's velocity along the fielder's line, $\vec{v} \cdot \hat{n}$?
  options:
    A: |-
      $(12\,\hat{i} + 12\,\hat{j})\,\text{m/s}$
    B: |-
      $24\,\text{m/s}$
    C: |-
      $25\,\text{m/s}$
    D: |-
      $7\,\text{m/s}$
  answer: B
  explanation: |-
    Multiply matching components and add: $\vec{v} \cdot \hat{n} = (20)(0.6) + (15)(0.8) = 12 + 12 = 24\,\text{m/s}$. The result is a scalar, a little less than the full speed of $25\,\text{m/s}$ because the shot is not exactly along the fielder's line.
  misconceptions:
    A: |-
      Multiplies matching components but keeps them as a vector; the scalar product adds those products to give a single number, not a vector.
    C: |-
      Takes the full speed $|\vec{v}| = 25\,\text{m/s}$ as the component along any direction; a component along a line is only the full speed when the vector points exactly along that line.
    D: |-
      Pairs each component with the wrong partner ($20 \times 0.8 - 15 \times 0.6$), mixing up the scalar product with a cross-product-style formula; only matching components ($x$ with $x$, $y$ with $y$) are multiplied.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground by day: a batter watches a ball climb high, a fielder waits under it, a player runs up the stadium steps and a groundsman pushes a roller](scenes/cricket/work_energy_power.svg "Every moment on this ground involves forces, motion and energy — this chapter's subject.")

Nisha is spending her summer as an intern with her city's club team, sitting behind a laptop connected to the ball-tracking cameras. In the fourth over, the batter lofts a drive and the long-on fielder dives — and misses it by a whisker. The ball runs away for four.

At the drinks break, the captain, Rohan, storms over. "That was straight at him! He should have caught it."

Nisha checks the numbers. The tracker never says "straight at him". It stores everything as components: the ball's velocity along two ground axes, and the fielder's position on the same axes. The shot's speed was $30\,\text{m/s}$; the fielder stood $65\,\text{m}$ away.

Rohan wants a yes or no. Nisha needs two things from two arrows given only as components: the angle between them, and how much of the ball's speed was actually heading towards the fielder. Is there one calculation that gives both?

## The physics

The **scalar product** (or dot product) of two vectors $\vec{A}$ and $\vec{B}$ is defined as

$$\vec{A} \cdot \vec{B} = AB\cos\theta$$

where $A$ and $B$ are the magnitudes and $\theta$ is the angle between the vectors when they are drawn tail to tail. The result is a **scalar** — just a number (with units), no direction.

It has a clean geometric meaning: $B\cos\theta$ is the **projection** of $\vec{B}$ on $\vec{A}$, so $\vec{A} \cdot \vec{B}$ is $A$ times the part of $\vec{B}$ that lies along $\vec{A}$. If $\hat{n}$ is a unit vector, $\vec{B} \cdot \hat{n}$ is simply the component of $\vec{B}$ along $\hat{n}$.

![Left: vectors A and B from one point, with the projection B cos theta marked along A. Right: three cases showing the dot product positive for angles below 90 degrees, zero at 90 degrees and negative above 90 degrees](figures/dot_product/projection-and-sign.svg "The dot product is A times the projection of B on A. Its sign tells you whether the vectors point roughly together, at right angles, or roughly apart.")

Because $\cos\theta$ changes sign at $90^\circ$, the dot product is positive for $\theta < 90^\circ$, zero for perpendicular vectors, and negative for $\theta > 90^\circ$.

**From components.** Since $\hat{i} \cdot \hat{i} = \hat{j} \cdot \hat{j} = \hat{k} \cdot \hat{k} = 1$ (angle $0^\circ$) and $\hat{i} \cdot \hat{j} = \hat{j} \cdot \hat{k} = \hat{k} \cdot \hat{i} = 0$ (angle $90^\circ$), expanding the product term by term leaves only matching pairs:

$$\vec{A} \cdot \vec{B} = A_x B_x + A_y B_y + A_z B_z$$

Two more useful facts: $\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$ (order doesn't matter), and $\vec{A} \cdot \vec{A} = A^2$. Putting the two forms together gives the angle between any two vectors:

$$\cos\theta = \frac{\vec{A} \cdot \vec{B}}{AB}$$

In Nisha's problem, $\vec{A}$ is the ball's velocity and $\vec{B}$ is the fielder's position.

## Worked example

**Given** (illustrative tracker numbers): take $x$ straight down the ground and $y$ towards the leg side, both along the grass. The shot's horizontal velocity is $\vec{v} = (24\,\hat{i} + 18\,\hat{j})\,\text{m/s}$; the fielder's position from the batter is $\vec{r} = (60\,\hat{i} + 25\,\hat{j})\,\text{m}$.
**Find:** the angle between the shot and the fielder's line, and the ball's speed along that line.

Magnitudes: $v = \sqrt{24^2 + 18^2} = \sqrt{900} = 30\,\text{m/s}$ and $r = \sqrt{60^2 + 25^2} = \sqrt{4225} = 65\,\text{m}$.

Dot product from components:

$$\vec{v} \cdot \vec{r} = (24)(60) + (18)(25) = 1440 + 450 = 1890\,\text{m}^2/\text{s}$$

Angle:

$$\cos\theta = \frac{1890}{30 \times 65} = \frac{1890}{1950} = 0.969 \quad\Rightarrow\quad \theta \approx 14^\circ$$

Component of the velocity along the fielder's line:

$$v_\parallel = \frac{\vec{v} \cdot \vec{r}}{r} = \frac{1890}{65} \approx 29.1\,\text{m/s}$$

So the shot missed the fielder's line by about $14^\circ$ — at $65\,\text{m}$, roughly $65 \times \sin 14^\circ \approx 16\,\text{m}$ to one side. Rohan's "straight at him" was wrong.

**Sanity check:** the shot points at $\tan^{-1}(18/24) \approx 36.9^\circ$ from the $x$-axis and the fielder at $\tan^{-1}(25/60) \approx 22.6^\circ$. The difference, $14.3^\circ$, matches.

## Where the picture breaks

The ball's real velocity also has an upward component, and it changes during flight: gravity bends the path and air drag slows it. Using only the horizontal velocity at the moment it left the bat treats the flight as a straight line along the ground. The fielder also moves the instant the ball is hit. The dot product answers a clean geometric question — the angle between two arrows — but whether the catch was possible needs the full motion.

## Key takeaway

The scalar product $\vec{A} \cdot \vec{B} = AB\cos\theta = A_xB_x + A_yB_y + A_zB_z$ is a number, not a vector. It measures how much one vector lies along another: positive when they point roughly together, zero when perpendicular, negative when roughly opposite. Comparing the two forms gives the angle between any two vectors.
