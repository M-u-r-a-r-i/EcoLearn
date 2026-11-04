---
concept_id: dot_product
interest: motorsport
format: explain
title: The crosswind that does nothing at all
check:
  question: |-
    On a club circuit the wind velocity is $\vec{w} = (6\,\hat{i} + 8\,\hat{j})\,\text{m/s}$, and one straight runs along the unit vector $\hat{n} = 0.8\,\hat{i} - 0.6\,\hat{j}$. What is the component of the wind along that straight, $\vec{w} \cdot \hat{n}$?
  options:
    A: |-
      $10\,\text{m/s}$
    B: |-
      $9.6\,\text{m/s}$
    C: |-
      $0$
    D: |-
      $(4.8\,\hat{i} - 4.8\,\hat{j})\,\text{m/s}$
  answer: C
  explanation: |-
    Multiply matching components and add: $(6)(0.8) + (8)(-0.6) = 4.8 - 4.8 = 0$. The dot product is zero, so the wind blows exactly across this straight — no headwind, no tailwind.
  misconceptions:
    A: |-
      Uses the whole wind speed $|\vec{w}| = 10\,\text{m/s}$ as the component along the straight. A vector only delivers its full magnitude along a line when it points exactly along that line.
    B: |-
      Drops the minus sign on the $\hat{j}$ component and adds $4.8 + 4.8$. Signs carry the directions; throwing them away turns a crosswind into a gale up the road.
    D: |-
      Multiplies matching components but leaves the answer as a vector. The scalar product *adds* those products into a single number — that is what makes it scalar.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race track scene: a car coasts down a hill road onto the circuit, a second car speeds along the straight with a velocity arrow, a third brakes with glowing red discs, and two people push a kart in the foreground](scenes/motorsport/work_energy_power.svg "Four ways energy moves at a circuit: down a hill, into speed, into brake heat, and out of somebody's arms.")

The club sprint runs on a disused airfield outside Nashik, and the wind sock at the end of the runway has been standing straight out all morning. In the paddock everyone has an opinion about it.

"It's a headwind on the main straight," says Hemant, who is driving. "That's half a second gone, every lap."

Chaitali has the weather station logging to her laptop, and it does not speak in words like *headwind*. It stores the wind as two numbers: so many metres per second east, so many metres per second north. The course map stores the straights the same way. Two lists of numbers, and a driver who wants a yes or a no.

She could sketch the arrows on graph paper and measure the angle with a protractor. But there must be an arithmetic that answers it directly — one operation that takes two arrows given as components and tells you how much of one lies along the other.

## The physics

The **scalar product** (or dot product) of two vectors $\vec{A}$ and $\vec{B}$ is

$$\vec{A} \cdot \vec{B} = AB\cos\theta$$

where $A$ and $B$ are the magnitudes and $\theta$ is the angle between the vectors drawn tail to tail. The answer is a **scalar** — one number with units, and no direction at all.

Its meaning is geometric. $B\cos\theta$ is the **projection** of $\vec{B}$ onto the line of $\vec{A}$, so $\vec{A} \cdot \vec{B}$ is $A$ multiplied by the part of $\vec{B}$ that lies along $\vec{A}$. If $\hat{n}$ is a **unit vector** (magnitude $1$), then $\vec{B} \cdot \hat{n}$ is simply the component of $\vec{B}$ along $\hat{n}$ — exactly what Chaitali wants.

![Left: vectors A and B from one point, with the projection B cos theta marked along A. Right: three cases showing the dot product positive for angles below 90 degrees, zero at 90 degrees and negative above 90 degrees](figures/dot_product/projection-and-sign.svg "The dot product is A times the projection of B on A. Its sign tells you whether the two arrows point roughly together, at right angles, or roughly apart.")

Because $\cos\theta$ changes sign at $90^\circ$, the sign of the dot product is a verdict: **positive** for $\theta < 90^\circ$ (roughly together — a tailwind), **zero** at exactly $90^\circ$ (a pure crosswind), **negative** for $\theta > 90^\circ$ (roughly opposed — a headwind).

**From components.** Since $\hat{i} \cdot \hat{i} = \hat{j} \cdot \hat{j} = \hat{k} \cdot \hat{k} = 1$ and $\hat{i} \cdot \hat{j} = \hat{j} \cdot \hat{k} = \hat{k} \cdot \hat{i} = 0$, expanding the product leaves only the matching pairs:

$$\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$$

Order does not matter ($\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$), and $\vec{A} \cdot \vec{A} = A^2$. Setting the two forms equal gives the angle between any two vectors:

$$\cos\theta = \frac{\vec{A} \cdot \vec{B}}{AB}$$

## Worked example

**Given** (illustrative logger values): take $x$ east and $y$ north. The wind velocity is $\vec{w} = (8\,\hat{i} - 6\,\hat{j})\,\text{m/s}$. The main straight runs along $\hat{n}_1 = 0.6\,\hat{i} + 0.8\,\hat{j}$ and the back straight along $\hat{n}_2 = 0.8\,\hat{i} + 0.6\,\hat{j}$; both are unit vectors.
**Find:** the wind's component along each straight, and the angle it makes with the back straight.

*Wind speed first.* $w = \sqrt{8^2 + 6^2} = \sqrt{100} = 10\,\text{m/s}$ — a brisk breeze, about $36\,\text{km/h}$.

*Main straight.*

$$\vec{w} \cdot \hat{n}_1 = (8)(0.6) + (-6)(0.8) = 4.8 - 4.8 = 0$$

Zero. The wind is exactly square across the main straight, so it is neither helping nor holding the car back along that line. Hemant's headwind does not exist.

*Back straight.*

$$\vec{w} \cdot \hat{n}_2 = (8)(0.8) + (-6)(0.6) = 6.4 - 3.6 = 2.8\,\text{m/s}$$

Positive, so it is a tailwind — but only $2.8\,\text{m/s}$ of the $10\,\text{m/s}$ blowing.

*Angle with the back straight,* using $\cos\theta = (\vec{w} \cdot \hat{n}_2)/(w \times 1)$:

$$\cos\theta = \frac{2.8}{10} = 0.28 \quad\Rightarrow\quad \theta \approx 74^\circ$$

**Sanity check:** $74^\circ$ is not far off a right angle, and a wind almost across a road should push you along it only feebly — a jogging pace of help out of a brisk breeze. That fits.

## Where the picture breaks

Treating the wind as one steady arrow is the idealisation here. Real wind gusts, swirls behind buildings and trees, and changes with height, so the logger's number is an average over a few seconds at one mast. A moving car also meets the *relative* wind — the vector difference between the true wind and the car's own velocity — so even a pure crosswind arrives partly from the front once you are travelling at $50\,\text{m/s}$. And a tailwind component of $2.8\,\text{m/s}$ does not translate into a simple time saving: drag depends on the square of the relative speed, which is a later story. The dot product answers one clean geometric question, and only that one.

## Key takeaway

The scalar product $\vec{A} \cdot \vec{B} = AB\cos\theta = A_xB_x + A_yB_y + A_zB_z$ turns two vectors into a single number. It measures how much of one vector lies along the other: positive when they point roughly the same way, zero when they are perpendicular, negative when they oppose. Dotting with a unit vector picks out a component directly.
