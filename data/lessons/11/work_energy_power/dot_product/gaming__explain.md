---
concept_id: dot_product
interest: gaming
format: explain
title: The one number that tells a guard you are in front
check:
  question: |-
    In a gliding game the wind velocity is $\vec{w} = (6\,\hat{i} - 8\,\hat{j})\,\text{m/s}$ and the glider's heading is the unit vector $\hat{u} = 0.8\,\hat{i} + 0.6\,\hat{j}$. How much of the wind pushes the glider along its heading, $\vec{w} \cdot \hat{u}$?
  options:
    A: |-
      $0$ — the wind is purely sideways
    B: |-
      $9.6\,\text{m/s}$
    C: |-
      $10\,\text{m/s}$
    D: |-
      $-2.8\,\text{m/s}$
  answer: A
  explanation: |-
    Multiply matching components and add: $(6)(0.8) + (-8)(0.6) = 4.8 - 4.8 = 0$. A zero scalar product means the two vectors are perpendicular, so this wind is exactly across the glider's path and gives no push forward or back.
  misconceptions:
    B: |-
      Adds the sizes of the two products and drops the minus sign ($4.8 + 4.8$); the signs of the components are part of the arithmetic, and dropping them loses the whole point of the sign of a dot product.
    C: |-
      Uses the full wind speed $|\vec{w}| = \sqrt{6^2 + 8^2} = 10\,\text{m/s}$ as the push along the heading; that is only true when the wind blows exactly along the heading.
    D: |-
      Pairs each component with the wrong partner ($6 \times 0.6 + (-8) \times 0.8$); in a scalar product only matching components are multiplied, $x$ with $x$ and $y$ with $y$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor shows a physics sandbox with a spring launcher, a kart at the top of a loop and a crate being dragged by a rope, beside a force-feedback racing wheel and a controller](scenes/gaming/work_energy_power.svg "Every arrow drawn on this screen — a velocity, a rope's pull, a line of sight — is a vector with a direction, not just a size.")

Ishita has spent three weekends building a stealth level for her college game-dev club. The rule is simple: sneak past the guards. On test night, it falls apart. Her friend Manu crouches directly *behind* a guard, and the alarm still goes off.

"Your guards have eyes in the back of their heads," he says.

Ishita scrolls through her code and finds the bug in one line. She had written the detection test using distance alone: if the player is within $50\,\text{m}$, raise the alarm. The engine knows more than that. It stores the guard's facing as a short arrow, and the player's position relative to the guard as another arrow.

She needs a test that separates "20 metres in front" from "20 metres behind" — and she wants one number, computed every frame, that answers it. Can two arrows really be squeezed into a single number that knows the difference?

## The physics

The **scalar product** (or dot product) of two vectors $\vec{A}$ and $\vec{B}$ is

$$\vec{A} \cdot \vec{B} = AB\cos\theta$$

where $A$ and $B$ are the magnitudes and $\theta$ is the angle between the vectors drawn tail to tail. The answer is a **scalar** — a single number with units, no direction.

Geometrically, $B\cos\theta$ is the **projection** of $\vec{B}$ on $\vec{A}$: the part of $\vec{B}$ that lies along $\vec{A}$. So the dot product is $A$ multiplied by that part. If $\hat{n}$ is a unit vector (length 1), then $\vec{B} \cdot \hat{n}$ is exactly the component of $\vec{B}$ along $\hat{n}$ — which is what Ishita's guard needs.

![Left: vectors A and B drawn from one point, with the projection B cos theta marked along A. Right: the dot product is positive below 90 degrees, zero at 90 degrees and negative above 90 degrees](figures/dot_product/projection-and-sign.svg "The dot product measures how much of one vector lies along the other. Its sign says whether they point roughly together, at right angles, or roughly apart.")

Because $\cos\theta$ changes sign at $90^\circ$, the sign carries the meaning: positive for $\theta < 90^\circ$ (roughly the same way, so *in front*), zero at $90^\circ$ (exactly to the side), negative for $\theta > 90^\circ$ (*behind*).

**From components.** Since $\hat{i} \cdot \hat{i} = \hat{j} \cdot \hat{j} = \hat{k} \cdot \hat{k} = 1$ and $\hat{i} \cdot \hat{j} = \hat{j} \cdot \hat{k} = \hat{k} \cdot \hat{i} = 0$, expanding the product leaves only the matching pairs:

$$\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$$

Order does not matter ($\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$), and $\vec{A} \cdot \vec{A} = A^2$. Putting the two forms side by side gives the angle between any two vectors:

$$\cos\theta = \frac{\vec{A} \cdot \vec{B}}{AB}$$

## Worked example

**Given** (illustrative level data, in metres): the guard faces along the unit vector $\hat{n} = 0.6\,\hat{i} + 0.8\,\hat{j}$, and the player's position from the guard is $\vec{r} = (40\,\hat{i} + 30\,\hat{j})\,\text{m}$.
**Find:** how far ahead of the guard the player is, and by what angle the player is off the guard's line of sight.

**Step 1 — the dot product from components.**

$$\vec{r} \cdot \hat{n} = (40)(0.6) + (30)(0.8) = 24 + 24 = 48\,\text{m}$$

That single number is the distance *along the guard's facing direction*. It is positive, so the player is in front, about 48 metres ahead — half a football pitch.

**Step 2 — how far the player actually is.**

$$r = \sqrt{40^2 + 30^2} = \sqrt{2500} = 50\,\text{m}$$

**Step 3 — the angle off the line of sight.**

$$\cos\theta = \frac{48}{50} = 0.96 \quad\Rightarrow\quad \theta \approx 16^\circ$$

So the player sits $16^\circ$ off centre, well inside a normal view cone: spotted.

**Sanity check:** 48 out of 50 metres lies straight ahead, so the player must be nearly — but not exactly — in front, and a small angle is exactly what came out.

## Where the picture breaks

The dot product answers one clean geometric question and nothing else. It does not know about the crate the player is hiding behind, about darkness, or about the wall in between — real engines follow this test with a separate line-of-sight ray. It also treats the guard as a point looking along one line, when a head turns and eyes have a cone, not a line. And a unit vector really must have length 1: if Ishita's facing arrow drifts to length 1.2 through rounding, every distance she computes comes out 20% too large.

## Key takeaway

The scalar product $\vec{A} \cdot \vec{B} = AB\cos\theta = A_xB_x + A_yB_y + A_zB_z$ turns two vectors into one number. It measures how much of one vector lies along the other: positive when they point roughly together, zero when perpendicular, negative when roughly opposite. Comparing the two forms gives the angle between any two vectors.
