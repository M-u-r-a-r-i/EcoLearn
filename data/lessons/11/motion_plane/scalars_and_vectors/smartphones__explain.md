---
concept_id: scalars_and_vectors
interest: smartphones
format: explain
title: The walk that was 1.2 km and also 500 m
check:
  question: |-
    Riya's smartwatch logs one full lap of a circular jogging path $400\,\text{m}$ long. She finishes exactly where she started. What are the distance she covered and her displacement for the lap?
  options:
    A: |-
      Distance $400\,\text{m}$; displacement zero
    B: |-
      Distance $400\,\text{m}$; displacement $400\,\text{m}$
    C: |-
      Distance zero; displacement $400\,\text{m}$
    D: |-
      Distance $400\,\text{m}$; displacement about $127\,\text{m}$, the width of the circle
  answer: A
  explanation: |-
    Distance is a scalar that adds up every metre of path, so it is $400\,\text{m}$. Displacement is a vector from the start point to the end point; she ends where she began, so it is zero.
  misconceptions:
    B: |-
      Treats displacement as just another name for distance. Displacement only compares where you started with where you ended, not how far you went.
    C: |-
      Swaps the two ideas: a finished lap does not cancel the ground covered. It is the displacement, not the distance, that comes back to zero.
    D: |-
      Takes displacement as the farthest you ever got from the start. Displacement is measured from start to the final position, and here those coincide.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![An evening terrace: a phone shows a map with a winding orange walking route and a straight black arrow from the start to the end, while a drone flies overhead and an earbud case skids off a table](scenes/smartphones/motion_plane.svg "On the phone's map, the dashed orange route and the straight black arrow describe the same walk in two different ways.")

Diya walks to her friend Sneha's house through the old lanes of her neighbourhood, left, right, round the temple, past the tea stall. Her smartwatch buzzes when she arrives: "Walk complete: 1.2 km."

Sneha laughs. "One point two? My phone's location-sharing app said you were only 500 metres away when you left."

"Your app is wrong," says Diya. "My watch counted every step."

Sneha turns her phone round. The map shows Diya's dashed orange route snaking through the lanes, and one straight arrow from Diya's front door to Sneha's gate. The arrow has a length and it points north-east.

Two gadgets, one walk, two very different numbers. Is one of them lying, or are they measuring two different things?

## The physics

Neither gadget is wrong. They report two different kinds of quantity.

A **scalar** is a quantity described completely by a size (a number with a unit). Mass, time, temperature, energy, and the battery charge on your phone are scalars. So is **distance**: the total length of the path actually travelled. The watch adds up every metre Diya walked, including every turn, so it reports $1.2\,\text{km}$.

A **vector** needs a size **and** a direction, and vectors combine by the rules of vector addition (next lesson), not by plain arithmetic. **Displacement** is the vector from the starting point to the final point. It ignores the route completely. Sneha's map arrow is Diya's displacement: $500\,\text{m}$, towards the north-east.

![Left: a winding path with a dashed line for the path length and a straight arrow from start to end. Right: a trip from A to B and back, with distance 2L and displacement zero](figures/scalars_and_vectors/distance-vs-displacement.svg "Distance counts every metre along the path. Displacement joins only the start and the end, so a round trip has zero displacement.")

Other pairs follow the same pattern. **Speed** is a scalar (how fast), while **velocity** is a vector (how fast *and* which way). A phone's GPS speed reading is a speed; pair it with the compass heading and you have a velocity. Acceleration and force are vectors too.

In print a vector is written in bold or with an arrow, $\vec{A}$, and its size (magnitude) as $|\vec{A}|$ or just $A$. Two facts always hold:

- $|\text{displacement}| \le \text{distance}$, with equality only for straight-line motion in one direction.
- Displacement can be zero when distance is not: walk out and come back, and you have gone somewhere but ended up nowhere.

## Worked example

**Given (illustrative):** a simpler route. Diya walks $300\,\text{m}$ east along one lane, then $400\,\text{m}$ north along another.
**Find:** the distance travelled and her displacement.

1. **Distance** just adds the lengths: $300 + 400 = 700\,\text{m}$. That is the number a step counter would show.
2. **Displacement size.** The two legs are at right angles, so the start-to-end arrow is the hypotenuse of a right-angled triangle:
$$|\vec{d}| = \sqrt{300^2 + 400^2} = \sqrt{90\,000 + 160\,000} = \sqrt{250\,000} = 500\,\text{m}$$
3. **Displacement direction.** $\tan\theta = \dfrac{400}{300} \approx 1.33$, so $\theta \approx 53^\circ$ north of east.

So she walked $700\,\text{m}$, but ended up $500\,\text{m}$ from home, at about $53^\circ$ north of east: roughly the length of five football pitches in a straight line.

**Sanity check:** the straight arrow is shorter than the route with a corner in it, as it must be.

## Where the picture breaks

A step counter doesn't measure distance directly: it counts steps and multiplies by an assumed stride length, so its distance is an estimate. Location apps plot GPS fixes that can wander by several metres, so the map arrow is only as good as the two positions it joins. And a map is flat: a walk up a hill also has an upward part of displacement that a flat map leaves out. None of this changes the idea: path length is a scalar, start-to-end change of position is a vector.

## Key takeaway

A **scalar** has only a size (distance, speed, mass, time); a **vector** has a size and a direction (displacement, velocity, acceleration, force). Distance adds up the whole path; displacement is the single arrow from start to end, so it can be much smaller than the distance, or even zero.
