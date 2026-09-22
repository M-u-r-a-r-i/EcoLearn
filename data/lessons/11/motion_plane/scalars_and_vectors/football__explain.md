---
concept_id: scalars_and_vectors
interest: football
format: explain
title: A 142-metre passing move that went nowhere
check:
  question: |-
    Which of these quantities, all from one match, is a scalar?
  options:
    A: |-
      The ball's velocity after a free kick, $25\,\text{m/s}$ towards the goal
    B: |-
      The ball's acceleration just after it leaves the boot, pointing towards the goal
    C: |-
      The distance a midfielder covers in the match, $10.5\,\text{km}$
    D: |-
      The push of the boot on the ball, $800\,\text{N}$ towards the goal
  answer: C
  explanation: |-
    Distance is the total length of the path, fully described by a number and a unit, so it is a scalar. Velocity, acceleration and force all need a direction as well as a size, and they combine by the triangle law.
  misconceptions:
    A: |-
      Treats velocity as if it were speed. The number $25\,\text{m/s}$ is only its size; "towards the goal" is part of the velocity too.
    B: |-
      Thinks acceleration is just a number for "how quickly it speeds up". Acceleration is the rate of change of velocity, so it has a direction.
    D: |-
      Thinks a force is only "how hard" something pushes. A push in a different direction has a different effect, so force is a vector.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A player lofts the ball in an arc over the goalkeeper while a teammate jogs round the centre circle](scenes/football/motion_plane.svg "On a football pitch everything moves in two dimensions. Some quantities care which way; some only care how much.")

Lalrinpuii, the goalkeeper of her school team, rolls the ball out to a defender to start the second half. What follows is the best move of the season: five passes, from defence out to the wing, across to midfield, back to a centre-back, and finally a firm pass back into Lalrinpuii's hands. She hasn't moved from her spot. The opponents never touch the ball.

After the match the team's analyst, Karthik, shows the move on his tablet app. "The ball travelled 142 metres in 20 seconds," he announces. Then he scrolls down and frowns. "But the app also says the ball's displacement was zero."

"Zero?" says Lalrinpuii. "It went all over the pitch. I watched it."

Both numbers come from the same 20 seconds, and the app is right about both. How can one move be 142 metres long and also zero?

## The physics

Physical quantities come in two kinds.

A **scalar** is fully described by a number with a unit: mass (the ball is about $0.43\,\text{kg}$), time ($20\,\text{s}$), distance, speed, temperature, energy. Scalars add like ordinary numbers.

A **vector** needs a size, its **magnitude**, *and* a direction: displacement, velocity, acceleration, force. A vector must also combine with others by the triangle law, which you'll meet in the next lesson. It is written $\vec{A}$, and its magnitude $|\vec{A}|$ or simply $A$.

Distance and displacement are the clearest pair to compare:

- **Distance** is the total length of the path actually travelled. It is a scalar. It is never negative, and it only grows while the ball keeps moving.
- **Displacement** is the straight arrow from the starting position to the final position. It is a vector, and it ignores the route taken in between.

![Left: a winding dashed path from start to end, with a straight arrow joining them. Right: a trip from A to B and back, with distance 2L and displacement zero](figures/scalars_and_vectors/distance-vs-displacement.svg "Distance adds up every metre of the path. Displacement only compares the start with the finish, so a round trip has zero displacement.")

In Karthik's move, the five passes were about $18$, $25$, $32$, $40$ and $27\,\text{m}$ long (illustrative). Their lengths add as plain numbers: $142\,\text{m}$ of distance. But the ball finished exactly where it started, in Lalrinpuii's hands, so its displacement was $\vec{0}$.

The same split runs through the rest of motion. **Speed** (distance ÷ time) is a scalar; **velocity** (displacement ÷ time) is a vector. The ball's average speed was $142/20 = 7.1\,\text{m/s}$, and its average velocity over the whole move was zero.

## Worked example

**Given (illustrative):** the first two passes of another move. The ball goes $24\,\text{m}$ straight up the pitch, then $10\,\text{m}$ straight across it, taking $4.0\,\text{s}$ in all.
**Find:** the distance, the displacement, the average speed and the average velocity.

Distance: add the lengths of both passes.
$$d = 24 + 10 = 34\,\text{m}$$

Displacement: the straight line from start to finish. The two passes are at right angles, so by Pythagoras
$$|\Delta\vec{r}| = \sqrt{24^2 + 10^2} = \sqrt{576 + 100} = \sqrt{676} = 26\,\text{m}$$
pointing from the starting spot to the finishing spot, mostly up the pitch and partly across.

Average speed $= 34/4.0 = 8.5\,\text{m/s}$. Average velocity $= 26/4.0 = 6.5\,\text{m/s}$, in the direction of the displacement.

**Sanity check:** the displacement ($26\,\text{m}$) is shorter than the distance ($34\,\text{m}$), as it must be. They would be equal only for a single straight pass.

## Where the picture breaks

The app treats the pitch as flat, but lofted passes also rise and fall, and the ball rarely rolls in a perfectly straight line, so the real path is a little longer than the sum of straight passes. The displacement stays exactly zero, because it depends only on the start and end points. Also, "has a direction" is not quite enough to make something a vector. Electric current has a direction along a wire, but currents meeting at a junction add as plain numbers, so current is a scalar. A true vector must add by the triangle law.

## Key takeaway

A scalar has only a magnitude (mass, time, distance, speed). A vector has a magnitude and a direction and adds by the triangle law (displacement, velocity, acceleration, force). Distance is the length of the path; displacement is the straight arrow from start to finish. That is how a 142-metre passing move can end with zero displacement.
