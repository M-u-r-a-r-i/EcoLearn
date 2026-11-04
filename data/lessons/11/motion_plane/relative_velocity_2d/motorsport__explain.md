---
concept_id: relative_velocity_2d
interest: motorsport
format: explain
title: Why the crosswind hits a kart from in front
check:
  question: |-
    On two crossing service roads at a test track, car A drives north at $20\,\text{m/s}$ and car B drives east at $15\,\text{m/s}$. What is the velocity of B as seen by the driver of A?
  options:
    A: |-
      $25\,\text{m/s}$, pointing about $53^\circ$ south of east
    B: |-
      $35\,\text{m/s}$, pointing north-east
    C: |-
      $5\,\text{m/s}$, pointing east
    D: |-
      $25\,\text{m/s}$, pointing about $53^\circ$ north of east
  answer: A
  explanation: |-
    $\vec{v}_{BA} = \vec{v}_B - \vec{v}_A = 15\hat{i} - 20\hat{j}$, with $\hat{i}$ east and $\hat{j}$ north. Its size is $\sqrt{15^2 + 20^2} = 25\,\text{m/s}$, at $\tan^{-1}(20/15) \approx 53^\circ$ south of east.
  misconceptions:
    B: |-
      Adds the two speeds as plain numbers. The velocities are at right angles, so their directions have to be included; $35\,\text{m/s}$ would need both cars on the same line, moving oppositely.
    C: |-
      Subtracts the speeds as plain numbers, as though both cars moved along one line. Relative velocity subtracts vectors, not sizes.
    D: |-
      Adds A's velocity instead of subtracting it. Because A is driving north, everything else drifts *southwards* in A's view.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race circuit seen from above: cars on the straights, one car sweeping through a curved corner, and a trackside replay screen showing a car arcing over a crest](scenes/motorsport/motion_plane.svg "The same circuit, the same air — but what you feel depends on how fast you are crossing it.")

It is a breezy Sunday at the karting track, and Zoya is walking back from the grid with her helmet under her arm. The flag on the marshal's post is streaming steadily: the wind is coming straight across the main straight, from her left, and she can feel it on her cheek.

She straps in and goes out. On the straight, flat out, the wind on her face is not coming from the left at all. It is coming at her almost head-on, just tipped slightly to one side, and it is far stronger than it felt standing still.

Her brother Faiz, timing from the fence, is unconvinced. "Wind doesn't change direction because you drove into it," he says. "It's the same wind."

He is right — it is the same wind. So why does it arrive from a different direction, and faster, the moment Zoya starts moving?

## The physics

The velocity you measure depends on who is doing the measuring. The **relative velocity** of A with respect to B is the velocity that A appears to have to an observer moving along with B:

$$\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$$

Both $\vec{v}_A$ and $\vec{v}_B$ are measured relative to the ground. In one dimension this was ordinary subtraction; in a plane it is **vector** subtraction — add $-\vec{v}_B$ to $\vec{v}_A$ by the triangle rule, or subtract component by component. Note also that $\vec{v}_{BA} = -\vec{v}_{AB}$: each observer sees the other moving the opposite way.

![Two velocity arrows: one for a moving object and one for a moving observer, with minus the observer's velocity added to the object's to give the relative velocity](figures/relative_velocity_2d/subtracting-velocities.svg "To find how A looks to B, add minus v_B to v_A. The result slants backwards, towards B, and is longer than either arrow on its own.")

For Zoya, A is the air and B is the kart. Take $\hat{i}$ along the straight, in the direction she drives, and $\hat{j}$ across the track, in the direction the wind is blowing. Standing still, she feels only the wind, $\vec{v}_\text{air} = w\,\hat{j}$. Moving at speed $v$, her own velocity is $v\,\hat{i}$, so the air's velocity relative to her is

$$\vec{v}_\text{air, kart} = w\,\hat{j} - v\,\hat{i}$$

The $-v\,\hat{i}$ term is the whole story: her own forward motion adds a *backwards* component to the air, which is why the airflow arrives from in front. The faster she goes, the more the $-v\,\hat{i}$ term dominates, and the closer to head-on the wind feels.

## Worked example

**Given:** a steady crosswind of $w = 5.0\,\text{m/s}$ blowing straight across the track; Zoya's kart doing $v = 12\,\text{m/s}$ along it (illustrative).
**Find:** the velocity of the air relative to the kart — its size, and its angle from straight ahead.

Subtract, component by component:
$$\vec{v}_\text{air, kart} = (0 - 12)\hat{i} + (5.0 - 0)\hat{j} = (-12\hat{i} + 5.0\hat{j})\,\text{m/s}$$

Its size:
$$|\vec{v}_\text{air, kart}| = \sqrt{12^2 + 5.0^2} = \sqrt{144 + 25} = \sqrt{169} = 13\,\text{m/s}$$

Its direction, measured from dead ahead (the $-\hat{i}$ direction, which is where the airflow comes from):
$$\tan\theta = \frac{5.0}{12} \approx 0.42 \quad\Rightarrow\quad \theta \approx 23^\circ$$

So the air comes at her at $13\,\text{m/s}$ — a stiff breeze turned into a gale — from about $23^\circ$ off the nose, on the side the wind blows from. Not from $90^\circ$, as it felt on foot.

**Sanity check:** $13\,\text{m/s}$ is bigger than either the $5.0$ or the $12$, which is what you expect when two perpendicular motions combine. If she stopped ($v = 0$), the angle would go back to $90^\circ$ — straight across, exactly as she felt it standing on the grid.

## Where the picture breaks

Real wind is not a single steady vector: it gusts, it swirls round buildings and grandstands, and it is slower near the ground than at helmet height, so the angle Zoya feels keeps shifting. A kart is also not a point — air spills round the bodywork and the driver, so the flow actually reaching her visor is not simply $\vec{v}_\text{air} - \vec{v}_\text{kart}$. And she is not travelling in a straight line at a fixed speed; every corner changes the direction of $\vec{v}_\text{kart}$ and so changes the answer. The subtraction rule itself is exact at everyday speeds; it needs correcting only near the speed of light.

## Key takeaway

The velocity of A relative to B is $\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$ — a vector subtraction, not a subtraction of speeds. Your own motion adds a backwards component to everything you observe, which is why a pure crosswind arrives almost head-on once you are moving quickly, and why it feels stronger than it is.
