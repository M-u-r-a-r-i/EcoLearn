---
concept_id: dot_product
interest: football
format: explain
title: Was the through ball really along the striker's run
check:
  question: |-
    A tracking system gives a pass's velocity along the grass as $\vec{v} = (12\,\hat{i} + 5\,\hat{j})\,\text{m/s}$ and a striker's run as the displacement $\vec{d} = (3\,\hat{i} + 4\,\hat{j})\,\text{m}$. What is the scalar product $\vec{v} \cdot \vec{d}$?
  options:
    A: |-
      $(36\,\hat{i} + 20\,\hat{j})\,\text{m}^2/\text{s}$
    B: |-
      $65\,\text{m}^2/\text{s}$
    C: |-
      $56\,\text{m}^2/\text{s}$
    D: |-
      $33\,\text{m}^2/\text{s}$
  answer: C
  explanation: |-
    Multiply matching components and add: $\vec{v} \cdot \vec{d} = (12)(3) + (5)(4) = 36 + 20 = 56\,\text{m}^2/\text{s}$. It is less than $vd = 13 \times 5 = 65\,\text{m}^2/\text{s}$ because the two vectors are not parallel.
  misconceptions:
    A: |-
      Multiplies matching components but keeps them as a vector; the scalar product adds those products to give a single number.
    B: |-
      Multiplies the two magnitudes, which assumes the vectors are parallel; $AB$ is only the dot product when $\cos\theta = 1$.
    D: |-
      Pairs each component with the wrong partner ($12 \times 4 - 5 \times 3$), a cross-product-style mix-up; only $x$ with $x$ and $y$ with $y$ are multiplied.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A football training ground by day: a player drags a weighted sled on a strap, a striker lofts the ball in a high arc, and the goalkeeper dives to catch it](scenes/football/work_energy_power.svg "Every pass, run and dive on this ground is a vector with a direction, not just a speed.")

Meera spends her Saturdays as a volunteer analyst for her district's under-17 side, with a laptop wired to the ground's tracking cameras. Midway through the first half, the winger, Tanmay, slides a through ball behind the defence. The striker, Irfan, has already set off on a diagonal run. The ball rolls just ahead of him, over the goal line, and out of play.

At half-time, Coach Rafiq is annoyed with Irfan. "That pass was right along your run. You should have reached it."

Irfan shakes his head. "It was going somewhere else."

Meera opens the data. The tracker never records "along the run". It stores the pass's velocity and Irfan's run as components on two pitch axes. Is there a single calculation that turns those components into the angle between them, and into how much of the pass was actually heading Irfan's way?

## The physics

The **scalar product** (dot product) of two vectors $\vec{A}$ and $\vec{B}$ is

$$\vec{A} \cdot \vec{B} = AB\cos\theta$$

where $A$ and $B$ are the magnitudes and $\theta$ is the angle between the vectors drawn tail to tail. The answer is a **scalar**: a number with units, but no direction.

Geometrically, $B\cos\theta$ is the **projection** of $\vec{B}$ on $\vec{A}$. So the dot product is $A$ multiplied by the part of $\vec{B}$ that lies along $\vec{A}$. If $\hat{n}$ is a unit vector, $\vec{B} \cdot \hat{n}$ is simply the component of $\vec{B}$ along $\hat{n}$.

![Left: vectors A and B from one point, with the projection B cos theta marked along A. Right: the dot product is positive below 90 degrees, zero at 90 degrees and negative above 90 degrees](figures/dot_product/projection-and-sign.svg "The dot product measures how much of one vector lies along the other. Its sign shows whether they point roughly together, at right angles, or roughly apart.")

Because $\cos\theta$ changes sign at $90^\circ$, the dot product is positive for $\theta < 90^\circ$, zero for perpendicular vectors and negative for $\theta > 90^\circ$.

**From components.** The unit vectors satisfy $\hat{i} \cdot \hat{i} = \hat{j} \cdot \hat{j} = \hat{k} \cdot \hat{k} = 1$ and $\hat{i} \cdot \hat{j} = \hat{j} \cdot \hat{k} = \hat{k} \cdot \hat{i} = 0$. Expanding term by term, only matching pairs survive:

$$\vec{A} \cdot \vec{B} = A_x B_x + A_y B_y + A_z B_z$$

The product is commutative, $\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$, and $\vec{A} \cdot \vec{A} = A^2$. Setting the two forms equal gives the angle between any two vectors:

$$\cos\theta = \frac{\vec{A} \cdot \vec{B}}{AB}$$

In Meera's problem, $\vec{A}$ is the pass's velocity and $\vec{B}$ is Irfan's run.

## Worked example

**Given** (illustrative tracker numbers): take $x$ along the touchline towards the opponents' goal and $y$ across the pitch. The pass's velocity is $\vec{v} = (12\,\hat{i} + 9\,\hat{j})\,\text{m/s}$; Irfan's run, from where he started to where he expected to meet the ball, is $\vec{d} = (5\,\hat{i} + 12\,\hat{j})\,\text{m}$.
**Find:** the angle between pass and run, and the pass's speed along the run.

Magnitudes: $v = \sqrt{12^2 + 9^2} = \sqrt{225} = 15\,\text{m/s}$ and $d = \sqrt{5^2 + 12^2} = \sqrt{169} = 13\,\text{m}$.

Dot product from components:

$$\vec{v} \cdot \vec{d} = (12)(5) + (9)(12) = 60 + 108 = 168\,\text{m}^2/\text{s}$$

Angle:

$$\cos\theta = \frac{168}{15 \times 13} = \frac{168}{195} \approx 0.862 \quad\Rightarrow\quad \theta \approx 30.5^\circ$$

Component of the pass's velocity along the run:

$$v_\parallel = \frac{\vec{v} \cdot \vec{d}}{d} = \frac{168}{13} \approx 12.9\,\text{m/s}$$

So the pass and the run were about $30^\circ$ apart. Of the pass's $15\,\text{m/s}$, only about $12.9\,\text{m/s}$ went Irfan's way; the rest, about $15\sin 30.5^\circ \approx 7.6\,\text{m/s}$, carried the ball sideways, away from his line. Irfan had a point.

**Sanity check:** the pass points at $\tan^{-1}(9/12) \approx 36.9^\circ$ from the $x$-axis and the run at $\tan^{-1}(12/5) \approx 67.4^\circ$. The difference, $30.5^\circ$, matches.

## Where the picture breaks

A real pass slows as it rolls, and it may curl if it was struck with spin, so its velocity is not one fixed arrow. Irfan's run also bends as he adjusts. The dot product answers a clean geometric question about two arrows at one instant. Whether he could have reached the ball needs the full motion of both, including how fast each was moving and for how long.

## Key takeaway

The scalar product $\vec{A} \cdot \vec{B} = AB\cos\theta = A_xB_x + A_yB_y + A_zB_z$ is a number, not a vector. It measures how much one vector lies along another: positive when they point roughly together, zero when perpendicular, negative when roughly opposite. Comparing its two forms gives the angle between any two vectors.
