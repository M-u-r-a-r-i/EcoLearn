---
concept_id: scalars_and_vectors
interest: motorsport
format: explain
title: Twelve kilometres that end in the same parking bay
check:
  question: |-
    All of these are measured during one lap of a track day. Which one is a vector?
  options:
    A: |-
      The car's acceleration as it pulls away from the line, $4\,\text{m/s}^2$ forwards along the track
    B: |-
      The speed-trap reading at the end of the straight, $120\,\text{km/h}$
    C: |-
      The lap length on the trip meter, $2.4\,\text{km}$
    D: |-
      The mass of the car with the driver in it, $1200\,\text{kg}$
  answer: A
  explanation: |-
    Acceleration has a size *and* a direction ("forwards along the track"), and accelerations combine by the triangle law, so it is a vector. Speed, distance and mass are each fully described by a number and a unit.
  misconceptions:
    B: |-
      Thinks speed must be a vector because it describes motion. Speed is only the size of the velocity; the trap reports no direction at all.
    C: |-
      Thinks any length measured while moving is a vector. Distance is the total path length, a scalar; only the displacement from start to finish carries a direction.
    D: |-
      Confuses mass with weight. Weight is a force and points downwards, but mass is just an amount of matter, with no direction.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race circuit seen from above: cars on the straights, one car sweeping through a curved corner, and a trackside replay screen showing a car arcing over a crest](scenes/motorsport/motion_plane.svg "A lap brings a car back to where it started. Every metre of the way counts as distance — but the journey from start to finish does not.")

Meenakshi has waited two years for her first track day. Her car is an ordinary hatchback with the boot emptied and the tyre pressures checked, and the circuit is a $2.4\,\text{km}$ club track with eight corners.

She drives five laps and comes back in, grinning. The trip meter she zeroed in the paddock now reads $12.0\,\text{km}$.

Her friend Karthik, who is halfway through Class 11 physics, is not impressed. "Twelve kilometres," he says, "and you parked in the same bay you started from. As far as physics is concerned, you went nowhere."

"Nowhere? I was out there for eight minutes."

They are both right, and both are describing the same eight minutes. How can one drive be twelve kilometres and nothing at the same time — and which number belongs on her data sheet?

## The physics

Physical quantities come in two kinds.

A **scalar** is fully described by a number with a unit: mass ($1200\,\text{kg}$), time ($480\,\text{s}$), distance ($12\,\text{km}$), speed, temperature, fuel volume. Scalars add like ordinary numbers.

A **vector** needs a size (its **magnitude**) *and* a direction: displacement, velocity, acceleration, force. To count as a vector, a quantity must also add by the triangle law, which is the next lesson. In print a vector is written with an arrow, $\vec{A}$, and its magnitude as $|\vec{A}|$ or just $A$.

The sharpest pair to compare is distance and displacement:

- **Distance** is the total length of the path actually driven. It is a scalar, it can never be negative, and it only grows while the wheels turn.
- **Displacement** is the straight-line change in position, from where you started to where you ended, *with its direction*. It is a vector, and it ignores the route entirely.

![Left: a winding dashed path from start to end with a straight arrow joining them. Right: a trip out to a point and back, with distance 2L and zero displacement](figures/scalars_and_vectors/distance-vs-displacement.svg "Distance adds up every metre of the path. Displacement compares only the start with the finish, so an out-and-back trip has zero displacement.")

That settles Meenakshi's argument. Her distance was $5 \times 2.4 = 12.0\,\text{km}$. Her displacement was $\vec{0}$, because a closed lap ends where it began.

The same split runs through the rest of motion. **Speed** (distance ÷ time) is a scalar; **velocity** (displacement ÷ time) is a vector. Over her $480\,\text{s}$ on track, her average speed was $12\,000/480 = 25\,\text{m/s}$ (about $90\,\text{km/h}$), and her average velocity was zero.

## Worked example

**Given:** an autocross course marked out with cones on an airfield, in the shape of a rectangle $400\,\text{m}$ long and $300\,\text{m}$ wide. A car starts at one corner and drives along two sides to the opposite corner, taking $50\,\text{s}$ (illustrative).
**Find:** the distance, the displacement, the average speed and the average velocity.

Distance — every stretch counts, whichever way it points:
$$d = 400 + 300 = 700\,\text{m}$$

Displacement — the straight arrow from the start corner to the finish corner, the diagonal of the rectangle:
$$|\Delta\vec{r}| = \sqrt{400^2 + 300^2} = \sqrt{250\,000} = 500\,\text{m}$$

at $\tan^{-1}(300/400) \approx 37^\circ$ away from the first side.

Average speed: $700/50 = 14\,\text{m/s}$ — a brisk $50\,\text{km/h}$.

Average velocity: $500/50 = 10\,\text{m/s}$, along that diagonal.

**Sanity check:** the displacement ($500\,\text{m}$) is smaller than the distance ($700\,\text{m}$), as it must be. The two are equal only for a straight run in one direction.

## Where the picture breaks

The trip meter is not a perfect distance meter: it counts wheel rotations, so wheelspin or a locked, sliding wheel makes it read wrong, and it measures the line Meenakshi actually drove, not the track's centre line. Her displacement is also not *exactly* zero — she parked a metre or two from where she set off — but that is tiny next to $12\,\text{km}$, so $\vec{0}$ is a fair description. And "has a direction" is not quite enough to make a quantity a vector: electric current has a direction along a wire, yet currents meeting at a junction simply add as numbers, so current is treated as a scalar. A true vector must add by the triangle law.

## Key takeaway

A scalar has only a magnitude (mass, time, distance, speed). A vector has a magnitude and a direction and adds by the triangle law (displacement, velocity, acceleration). Distance is the length of the path you drove; displacement is the straight arrow from start to finish. That is why five laps can be twelve kilometres of distance and zero displacement.
