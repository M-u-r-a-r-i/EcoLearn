---
concept_id: scalars_and_vectors
interest: gaming
format: explain
title: The patrol quest that went nowhere
check:
  question: |-
    Four numbers appear on an open-world game's screen during one quest. Which of them is a vector?
  options:
    A: |-
      The hero's health, $80$ points out of $100$
    B: |-
      A scout drone's velocity, $12\,\text{m/s}$ towards the north gate
    C: |-
      The total distance walked on the quest, $840\,\text{m}$
    D: |-
      The speed on the hero's sprint meter, $6\,\text{m/s}$
  answer: B
  explanation: |-
    Velocity needs both a size and a direction ("towards the north gate"), and velocities combine by the triangle law, so it is a vector. Health, distance and speed are each fully described by a number with a unit.
  misconceptions:
    A: |-
      Thinks anything a game tracks with a bar or a number must be a "physical vector". Health points are just a count; they have no direction at all.
    C: |-
      Thinks any distance covered while moving is a vector. Distance is the total length of the path, a scalar; only the displacement from start to finish has a direction.
    D: |-
      Thinks speed is a vector because it describes motion. Speed is only the magnitude of the velocity; the meter shows no direction.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: the monitor shows an artillery game with a shell flying along a curved arc; a tablet shows a top-down minimap of a circular kart track](scenes/gaming/motion_plane.svg "Motion in a game world happens in two dimensions, and every movement has a size and a direction.")

Tanvi has just finished the "Night Patrol" side quest in an open-world game. The quest sent her hero from the camp to three watchtowers across the valley and then, at dawn, back to the same campfire.

The end-of-quest screen pops up: **Distance travelled: 840 m.** Right beside it, the minimap's waypoint tracker reads **Distance from start: 0 m.**

Her cousin Rohan, watching from the bed, snorts. "Zero? You walked for ten minutes. That game has a bug. Report it."

Tanvi isn't so sure. The two numbers came from two different parts of the game, and both look deliberate. She walked 840 metres, and she is standing exactly where she began.

Can both numbers be right at once? And if they are, what exactly is each one measuring?

## The physics

Physical quantities come in two kinds.

A **scalar** is fully described by a number with a unit: mass, time, distance, speed, temperature, energy. Scalars add like ordinary numbers: $840\,\text{m}$ of walking plus $60\,\text{m}$ more is $900\,\text{m}$.

A **vector** needs a **magnitude** (its size) *and* a direction: displacement, velocity, acceleration, force. A vector must also add by the triangle law, which you meet in the next lesson. In print it is written $\vec{A}$, and its magnitude $|\vec{A}|$ or simply $A$.

The clearest pair to compare is distance and displacement.

- **Distance** is the total length of the path actually travelled. It is a scalar, never negative, and it only grows while you keep moving.
- **Displacement** is the straight-line change in position, from start to finish, *with its direction*. It is a vector, and it ignores the route.

![Left: a winding dashed path from start to end, with a straight arrow joining them. Right: a trip from A to B and back, with distance 2L and displacement zero](figures/scalars_and_vectors/distance-vs-displacement.svg "Distance adds up every metre of the path. Displacement only compares where you started with where you finished, so an out-and-back trip has zero displacement.")

That is exactly the split on Tanvi's screen. The quest counter adds up every step, so it is the distance, $840\,\text{m}$. The waypoint tracker compares her position now with her position at the start. Start and finish are the same campfire, so her displacement is $\vec{0}$. No bug.

The same split runs through motion. **Speed** is distance per unit time, a scalar. **Velocity** is displacement per unit time, a vector.

## Worked example

**Given:** a guard in the game (illustrative numbers) patrols $30\,\text{m}$ east, then $40\,\text{m}$ north, taking $20\,\text{s}$ in all.
**Find:** the distance, the displacement, the average speed and the size of the average velocity.

Distance counts every stretch:
$$d = 30 + 40 = 70\,\text{m}$$

Displacement is the straight arrow from start to finish. The two legs are at right angles, so its size comes from Pythagoras:
$$|\Delta\vec{r}| = \sqrt{30^2 + 40^2} = \sqrt{2500} = 50\,\text{m}$$
It points north of east, at $\tan^{-1}(40/30) \approx 53^\circ$ from the east direction.

Average speed $= 70/20 = 3.5\,\text{m/s}$. Average velocity $= 50/20 = 2.5\,\text{m/s}$, in the direction $53^\circ$ north of east.

**Sanity check:** the displacement ($50\,\text{m}$) is less than the distance ($70\,\text{m}$), as it must be. They are equal only for travel in one straight line without turning back.

## Where the picture breaks

A game's labels are not always physics labels. Some games call a speed "velocity", and many waypoint trackers show only the *size* of your displacement, "0 m" or "250 m", without its direction; the arrow on the compass supplies the direction separately. Game worlds also usually measure positions on a flat map even when the hero climbs hills, so their "distance" may leave out the up-and-down. And "has a direction" is not quite enough to make a quantity a vector: electric current has a direction along a wire, but currents meeting at a junction add as plain numbers, so current is a scalar.

## Key takeaway

A scalar has only a magnitude (mass, time, distance, speed). A vector has a magnitude and a direction and adds by the triangle law (displacement, velocity, force). Distance is the length of the path you walked; displacement is the straight arrow from start to finish. That is why a quest can be $840\,\text{m}$ long and end with zero displacement.
