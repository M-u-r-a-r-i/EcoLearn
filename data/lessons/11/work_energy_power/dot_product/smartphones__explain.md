---
concept_id: dot_product
interest: smartphones
format: explain
title: How your phone knows which way is up
check:
  question: |-
    While testing a tilt game, two vectors are logged: $\vec{P} = 3\hat{i} + 4\hat{j}$ and $\vec{Q} = 4\hat{i} + 3\hat{j}$ (same units). What is the scalar product $\vec{P} \cdot \vec{Q}$?
  options:
    A: |-
      $0$
    B: |-
      $24$
    C: |-
      $25$
    D: |-
      $12\hat{i} + 12\hat{j}$
  answer: B
  explanation: |-
    Multiply matching components and add: $\vec{P} \cdot \vec{Q} = (3)(4) + (4)(3) = 12 + 12 = 24$. It is a plain number (a scalar), slightly less than $PQ = 5 \times 5 = 25$ because the two vectors are about $16^\circ$ apart.
  misconceptions:
    A: |-
      Cross-multiplies and subtracts, $3 \times 4 - 4 \times 3 = 0$, as if it were a determinant, and concludes the vectors are perpendicular. The dot product pairs $x$ with $x$ and $y$ with $y$, then adds.
    C: |-
      Multiplies the two magnitudes, $5 \times 5 = 25$, which is only the dot product when the vectors point the same way. Here they are at an angle, so $\cos\theta < 1$ and the product is smaller.
    D: |-
      Multiplies the components but keeps them as a vector. The scalar product is a single number, with no direction: add the component products together.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A living room in the evening: a camera drone climbs straight up, a phone falls from a shelf towards a cushion, an earbuds case is whirled on a lanyard in a vertical circle, and a robot vacuum rolls towards a sofa leg](scenes/smartphones/work_energy_power.svg "Every arrow in this room is a vector. This lesson is about one way of multiplying two of them.")

Nandini is lying on her back on the sofa, reading on her phone held above her face. Every time she tilts it slightly, the screen flips from portrait to landscape and back, and she loses her place.

"It's broken," she tells her cousin Yash, who is studying engineering.

"It's not broken, it's measuring," says Yash. He opens a sensor app. Held upright, the phone shows about $9.8\,\text{m/s}^2$ along its long edge. Laid flat on the table, the same number moves entirely to the axis coming out of the screen, and the long-edge reading drops to zero.

"The chip doesn't know which way is up," Yash says. "It only knows one arrow, and it asks how much of that arrow lies along each edge of the phone."

Nandini frowns. How do you ask "how much of one arrow lies along another" — and why does lying flat confuse the phone completely?

## The physics

The **scalar product** (dot product) of two vectors $\vec{A}$ and $\vec{B}$ at an angle $\theta$ is

$$\vec{A} \cdot \vec{B} = AB\cos\theta$$

The answer is a **scalar** — a single number, with no direction. Read it as "$A$ times the part of $\vec{B}$ that lies along $\vec{A}$". Its sign carries meaning:

- $\theta < 90^\circ$: positive (the vectors point roughly together);
- $\theta = 90^\circ$: zero (perpendicular);
- $\theta > 90^\circ$: negative (roughly opposite).

![Left: vectors A and B drawn from one point, with the projection B cos theta marked along A. Right: the dot product is positive below 90 degrees, zero at 90 degrees and negative above](figures/dot_product/projection-and-sign.svg "The dot product is A times the projection of B on A. Its sign says whether the arrows point roughly together, at right angles, or roughly apart.")

**From components.** Since $\hat{i} \cdot \hat{i} = \hat{j} \cdot \hat{j} = \hat{k} \cdot \hat{k} = 1$ and the cross terms like $\hat{i} \cdot \hat{j}$ are zero,

$$\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$$

The dot product is commutative ($\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$), and $\vec{A} \cdot \vec{A} = A^2$.

**Back to the phone.** The accelerometer reports one arrow, $\vec{a}$, pointing straight up, of size about $g$. Auto-rotate works out $\vec{a} \cdot \hat{y}$, where $\hat{y}$ is a unit arrow along the phone's long edge. Upright, the angle is $0^\circ$ and the product is large, so: portrait. Lying flat — or held flat above your face — every edge is at $90^\circ$ to "up", so every edge's dot product is close to zero, and tiny wobbles decide the answer.

## Worked example

**Given:** Yash tilts the phone. The app shows the "up" arrow in the phone's own axes as $\vec{a} = 0\,\hat{i} + 6.0\,\hat{j} + 8.0\,\hat{k}$ in $\text{m/s}^2$ (illustrative, rounded so the size comes out as $10$ rather than $9.8$).
**Find:** the angle between the phone's long edge, $\hat{y} = \hat{j}$, and straight up.

1. *The size of the arrow:* $a = \sqrt{0^2 + 6.0^2 + 8.0^2} = \sqrt{100} = 10\,\text{m/s}^2$.
2. *The dot product from components:* $\vec{a} \cdot \hat{j} = (0)(0) + (6.0)(1) + (8.0)(0) = 6.0\,\text{m/s}^2$. So $6$ of the $10$ units lie along the long edge.
3. *The angle from $AB\cos\theta$:* $\cos\theta = \dfrac{6.0}{10 \times 1} = 0.60$, so $\theta \approx 53^\circ$.

The long edge leans about $53^\circ$ away from vertical — more than halfway to flat — but still has more "up" in it than the short edge (which has none), so the phone stays in portrait.

**Sanity check:** $6.0$ lies between $0$ (flat) and $10$ (upright), so the tilt must lie between $0^\circ$ and $90^\circ$ — and it does.

## Where the picture breaks

The phone is the setting here, not an analogy: the chip genuinely computes projections of one vector on its axes. But the real reading isn't just gravity's arrow. When you move the phone, its own acceleration mixes in, which is why auto-rotate waits a moment before flipping. Real software also compares all three axes and adds a margin, so it won't flip at exactly $45^\circ$. And the reading is the push supporting the phone per kilogram, which points *up*; we have taken that for granted from the laws of motion rather than proved it here.

## Key takeaway

The scalar product $\vec{A} \cdot \vec{B} = AB\cos\theta = A_xB_x + A_yB_y + A_zB_z$ is a single number: how much of one vector lies along the other, times the other's size. It is positive, zero or negative as the angle is below, at or above $90^\circ$.
