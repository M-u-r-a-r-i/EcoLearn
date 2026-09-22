---
concept_id: scalars_and_vectors
interest: cricket
format: explain
title: Two runs, forty metres and a displacement of zero
check:
  question: |-
    Which of these quantities, all from one delivery in a match, is a vector?
  options:
    A: |-
      The mass of the ball, $0.16\,\text{kg}$
    B: |-
      The speed on the speed gun display, $130\,\text{km/h}$
    C: |-
      The ball's velocity, $36\,\text{m/s}$ from the bowler towards the batter
    D: |-
      The distance the batter ran for two runs, $36\,\text{m}$
  answer: C
  explanation: |-
    Velocity has a size and a direction ("towards the batter"), and velocities combine by the triangle law, so it is a vector. Mass, speed and distance are fully described by a number and a unit.
  misconceptions:
    A: |-
      Confuses mass with weight: weight is a force that points downwards, but mass is just an amount of matter with no direction.
    B: |-
      Thinks speed is a vector because it describes motion. Speed is only the size of the velocity; the display gives no direction.
    D: |-
      Thinks any distance covered while moving is a vector. Distance is the total path length, a scalar; only the displacement from start to finish has a direction.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A day match: a batter lofts the ball towards the boundary as a fielder races along the rope](scenes/cricket/motion_plane.svg "Every movement on a cricket field has a size and a direction. Some quantities care about the direction; some don't.")

It's the last ball of an inter-school final and Devika's team needs two to win. She pushes the ball into the gap at cover and sets off. She sprints to the far crease, turns, and dives back into her own crease as the throw comes in. Two runs. The team wins.

In the pavilion her physics teacher, Mr Kulkarni, who was also the scorer, grins at her. "Brilliant running," he says. "You covered about 36 metres in eight seconds. And your displacement was zero."

Devika laughs. "Zero? My legs don't think it was zero."

He isn't joking, though. Both numbers are correct, and both describe the same eight seconds. How can one run be 36 metres and nothing at the same time? And which one tells you how far she really went?

## The physics

Physical quantities come in two kinds.

A **scalar** is fully described by a number with a unit: mass ($0.16\,\text{kg}$), time ($8\,\text{s}$), distance ($36\,\text{m}$), speed, temperature, energy. Scalars add like ordinary numbers.

A **vector** needs a size (its **magnitude**) *and* a direction: displacement, velocity, acceleration, force. To be a vector, a quantity must also add by the triangle law, which you will meet in the next lesson. In print a vector is written in bold or with an arrow, $\vec{A}$, and its magnitude as $|\vec{A}|$ or just $A$.

The clearest pair to compare is distance and displacement:

- **Distance** is the total length of the path actually travelled. It is a scalar, it can never be negative, and it only grows as you keep moving.
- **Displacement** is the straight-line change in position, from where you started to where you ended, *with its direction*. It is a vector, and it ignores the route taken.

![Left: a winding dashed path from start to end, with a straight arrow joining them. Right: a trip from A to B and back, with distance 2L and displacement zero](figures/scalars_and_vectors/distance-vs-displacement.svg "Distance adds up every metre of the path. Displacement only compares where you started with where you finished, so an out-and-back trip has zero displacement.")

In Devika's two runs, she ran a little under the $20.12\,\text{m}$ between the stumps each way, since she only had to ground her bat over the crease. Call it $18\,\text{m}$ each way (illustrative). Her distance was $18 + 18 = 36\,\text{m}$. But she finished exactly where she began, so her displacement was $\vec{0}$.

The same split runs through the rest of motion. **Speed** (distance ÷ time) is a scalar; **velocity** (displacement ÷ time) is a vector. So her average speed was $36/8 = 4.5\,\text{m/s}$, and her average velocity was zero.

## Worked example

**Given:** a batter completes **three** runs, about $18\,\text{m}$ each way (illustrative), in $12\,\text{s}$. Take the direction towards the bowler's end as positive.
**Find:** the distance, the displacement, the average speed and the average velocity.

Distance: every stretch counts, whatever its direction.
$$d = 18 + 18 + 18 = 54\,\text{m}$$

Displacement: out, back and out again leaves the batter one pitch-length from the start, at the bowler's end.
$$\Delta \vec{x} = +18\,\text{m} \;\;(\text{towards the bowler's end})$$

Average speed $= 54/12 = 4.5\,\text{m/s}$. Average velocity $= 18/12 = 1.5\,\text{m/s}$ towards the bowler's end.

**Sanity check:** the size of the displacement ($18\,\text{m}$) is less than the distance ($54\,\text{m}$), as it must be. The two are equal only for a straight run in one direction.

## Where the picture breaks

Devika didn't run in a perfect straight line; batters curve slightly and slow down to turn. Her distance would be a little more than $36\,\text{m}$, but her displacement would still be exactly zero, because it depends only on the start and end points. "Has a direction" is not quite enough to make something a vector, either. Electric current has a direction along a wire, but currents meeting at a junction simply add as numbers, so current is treated as a scalar. A true vector must add by the triangle law.

## Key takeaway

A scalar has only a magnitude (mass, time, distance, speed). A vector has a magnitude and a direction and adds by the triangle law (displacement, velocity, force). Distance is the length of the path you took; displacement is the straight arrow from start to finish. That is why two runs can be $36\,\text{m}$ of distance and zero displacement.
