---
concept_id: vector_components
interest: motorsport
format: explain
title: Half a kilometre of road, eighty-seven metres of climb
check:
  question: |-
    A car is driven up a transporter's loading ramp, inclined at $30^\circ$ to the horizontal, at a steady $2.0\,\text{m/s}$ along the ramp. How fast is it rising, and how fast is it moving horizontally? ($\sin 30^\circ = 0.50$, $\cos 30^\circ \approx 0.866$)
  options:
    A: |-
      $1.7\,\text{m/s}$ upwards and $1.0\,\text{m/s}$ horizontally
    B: |-
      $1.0\,\text{m/s}$ upwards and $1.0\,\text{m/s}$ horizontally
    C: |-
      $1.0\,\text{m/s}$ upwards and $1.7\,\text{m/s}$ horizontally
    D: |-
      $1.0\,\text{m/s}$ upwards and $2.0\,\text{m/s}$ horizontally
  answer: C
  explanation: |-
    The vertical component is $v\sin\theta = 2.0 \times 0.50 = 1.0\,\text{m/s}$ and the horizontal component is $v\cos\theta = 2.0 \times 0.866 \approx 1.7\,\text{m/s}$. Check: $\sqrt{1.0^2 + 1.7^2} \approx 2.0\,\text{m/s}$.
  misconceptions:
    A: |-
      Swaps sine and cosine. The component alongside the angle — here the horizontal one — takes $\cos\theta$.
    B: |-
      Shares the velocity out equally between the two directions, as if each component were simply half of it. They are equal only at $45^\circ$.
    D: |-
      Keeps the full $2.0\,\text{m/s}$ as the horizontal part, as if the components had to add up as ordinary numbers. Perpendicular components combine by Pythagoras, not by addition.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race circuit seen from above: cars on the straights, one car sweeping through a curved corner, and a trackside replay screen showing a car arcing over a crest](scenes/motorsport/motion_plane.svg "One motion, two questions: how far along, and how far up? A single arrow answers both once you split it.")

Nandini's club runs a hill-climb sprint on a closed ghat road: one car at a time, flat out from the bottom gate to the finish board near the top. She has entered for the first time, and she is logging everything on a phone app clamped to the windscreen.

At the finish she reads out two numbers to her navigator, Tejas. The app says she covered $500\,\text{m}$ of road on the last section. It also says she climbed $87\,\text{m}$.

"Both can't be right," says Tejas. "You drove five hundred metres, so you went five hundred metres. Where did the other four hundred and thirteen go?"

Nandini looks back down at the road behind them, a pale ribbon climbing steadily at the same angle all the way. Nothing was lost. One straight stretch of driving somehow counts as $500\,\text{m}$ *and* $87\,\text{m}$ at the same time. How?

## The physics

Any vector in a plane can be replaced by two perpendicular vectors that add up to it. These are its **components**. Choose axes first: here $x$ horizontal (measured on a flat map) and $y$ vertically up.

If a vector $\vec{A}$ has magnitude $A$ and makes an angle $\theta$ with the $x$-axis, its **rectangular components** are

$$A_x = A\cos\theta, \qquad A_y = A\sin\theta$$

This is nothing more than right-angled-triangle trigonometry: $\vec{A}$ is the hypotenuse and the components are the two sides. The side *next to* $\theta$ takes $\cos\theta$; the side *opposite* $\theta$ takes $\sin\theta$.

![A vector A at an angle theta to the x-axis, with dashed lines dropped to each axis, showing the x-component A cos theta and the y-component A sin theta](figures/vector_components/resolving-a-vector.svg "Resolving a vector: drop perpendiculars from its head onto each axis. The two components, added head to tail, rebuild the original arrow exactly.")

Going the other way, you can **reconstruct** the vector from its components:

$$A = \sqrt{A_x^2 + A_y^2}, \qquad \tan\theta = \frac{A_y}{A_x}$$

Components carry signs. A car coming back *down* the hill has a negative $A_y$; one heading west when $x$ points east has a negative $A_x$. The sign is the direction.

Why do it at all? Because perpendicular directions can be handled separately. Once a displacement, velocity or force is split into an $x$-part and a $y$-part, each part behaves like one-dimensional motion, which you already know how to handle. On Nandini's hill, the $x$-component is how far she moved across the map and the $y$-component is how much height she gained — and it is the height that decides how much work the engine had to do against gravity.

## Worked example

**Given:** a straight section of hill-climb road $500\,\text{m}$ long, rising at a steady $\theta = 10^\circ$ to the horizontal ($\cos 10^\circ \approx 0.985$, $\sin 10^\circ \approx 0.174$) — illustrative, but a realistically steep ghat section.
**Find:** the horizontal and vertical components of the car's displacement, then rebuild the displacement from them.

Horizontal component, along the map:
$$A_x = 500 \times 0.985 \approx 493\,\text{m}$$

Vertical component, the height gained:
$$A_y = 500 \times 0.174 \approx 87\,\text{m}$$

So in driving half a kilometre of road, Nandini moved about $493\,\text{m}$ across the map and rose about $87\,\text{m}$ — roughly the height of a twenty-five-storey building.

Rebuild it, as a check:
$$A = \sqrt{493^2 + 87^2} = \sqrt{243\,049 + 7569} = \sqrt{250\,618} \approx 500\,\text{m}$$
$$\tan\theta = \frac{87}{493} \approx 0.176 \quad\Rightarrow\quad \theta \approx 10^\circ$$

**Sanity check:** each component is smaller than $500\,\text{m}$, as it must be, and the horizontal part is much the bigger one because $10^\circ$ is a shallow angle. Nothing was lost — $493$ and $87$ simply do not add up as ordinary numbers.

## Where the picture breaks

A real ghat road is not one straight ramp at one angle: it bends, the gradient changes, and hairpins turn the car right round, so the app is really adding up many short sections, each with its own $\theta$. Splitting a vector into components is exact; the idealisation here is pretending the road has a single constant slope and lies in one vertical plane. A road that also curves sideways needs a third axis. And the app's height figure comes from a satellite fix or a pressure sensor, each with its own uncertainty of a few metres.

## Key takeaway

A vector at angle $\theta$ to the $x$-axis splits into perpendicular components $A_x = A\cos\theta$ and $A_y = A\sin\theta$, and you rebuild it with $A = \sqrt{A_x^2 + A_y^2}$ and $\tan\theta = A_y/A_x$. Components let you treat each direction on its own — which is how one $500\,\text{m}$ drive becomes $493\,\text{m}$ across and $87\,\text{m}$ up.
