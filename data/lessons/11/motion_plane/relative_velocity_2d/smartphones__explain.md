---
concept_id: relative_velocity_2d
interest: smartphones
format: explain
title: Why the rain slants in your auto-rickshaw video
check:
  question: |-
    On a delivery app's map, rider P heads north at $6\,\text{m/s}$ and rider Q heads east at $8\,\text{m/s}$. What is the velocity of P relative to Q?
  options:
    A: |-
      $10\,\text{m/s}$, at about $37^\circ$ north of west
    B: |-
      $10\,\text{m/s}$, at about $37^\circ$ north of east
    C: |-
      $2\,\text{m/s}$, towards the north
    D: |-
      $14\,\text{m/s}$, at about $37^\circ$ north of west
  answer: A
  explanation: |-
    $\vec{v}_{PQ} = \vec{v}_P - \vec{v}_Q = 6\,\text{m/s north} + 8\,\text{m/s west}$. Its size is $\sqrt{6^2 + 8^2} = 10\,\text{m/s}$, at $\tan^{-1}(6/8) \approx 37^\circ$ north of west.
  misconceptions:
    B: |-
      Adds Q's velocity instead of subtracting it. Relative to Q, P picks up Q's velocity reversed, so the east-west part points west, not east.
    C: |-
      Subtracts the speeds as plain numbers, as in one dimension. Perpendicular velocities must be subtracted as vectors.
    D: |-
      Adds the two speeds as numbers. Perpendicular vectors combine by Pythagoras, so the size can't be $6 + 8$.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![An evening terrace: a phone, a drone flying at a slant and an earbud case skidding off a table](scenes/smartphones/motion_plane.svg "A phone camera records motion as seen from wherever the phone is, and if the phone is moving, that changes what it sees.")

The monsoon has arrived, and Pooja is filming it. At the bus stop, with no wind at all, her phone video shows the raindrops falling in perfectly straight, vertical streaks.

Then her auto-rickshaw arrives. She climbs in, the driver pulls away, and she keeps filming out of the side. On her screen, the streaks now slant steeply, as if the rain were being blown at them from the front.

"Wind's picked up," says the driver.

Pooja leans out. The trees are perfectly still. There is no wind. The rain outside is falling just as straight as it was a minute ago.

So why does her phone, and her face, say the rain is coming at them from ahead? And at what angle should she tilt her umbrella?

## The physics

Every velocity is measured **relative to** something. The **velocity of A relative to B** is how A's motion looks to an observer riding along with B:

$$\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$$

where both $\vec{v}_A$ and $\vec{v}_B$ are measured relative to the ground. In one dimension that was plain subtraction of numbers; in a plane it is **vector** subtraction. Subtracting $\vec{v}_B$ is the same as adding $-\vec{v}_B$, the same arrow reversed:

$$\vec{v}_{AB} = \vec{v}_A + (-\vec{v}_B)$$

For Pooja, A is the rain (falling vertically) and B is the auto (moving horizontally forward). To the auto, the rain has its own downward velocity **plus** the auto's velocity reversed, pointing backwards. The sum of those two is a slanting arrow, and that is what the phone films.

![Left: A moves down and observer B moves right, as seen from the ground. Right: v_A plus minus v_B gives v_AB slanting down and backwards](figures/relative_velocity_2d/subtracting-velocities.svg "To add minus v_B, reverse B's arrow and put it head to tail with v_A. The resultant slants towards B from ahead, and is longer than either.")

When the two velocities are at right angles, as here, the size is

$$|\vec{v}_{AB}| = \sqrt{v_A^2 + v_B^2}$$

and the angle from the vertical satisfies $\tan\theta = v_B / v_A$. The faster the auto goes, the more the rain appears to slant.

## Worked example

**Given (illustrative):** rain falling vertically at $v_R = 6\,\text{m/s}$; the auto moving forward at $v_A = 8\,\text{m/s}$ (about $29\,\text{km/h}$).
**Find:** the velocity of the rain relative to the auto.

1. Relative to the auto, the rain has $6\,\text{m/s}$ downwards and $8\,\text{m/s}$ **backwards** (the auto's velocity reversed).
2. Size: $\sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\,\text{m/s}$.
3. Direction: $\tan\theta = \dfrac{8}{6} \approx 1.33$, so $\theta \approx 53^\circ$ from the vertical, coming down from the front.

So in Pooja's video the drops fly past at $10\,\text{m/s}$, tilted more than halfway towards the horizontal. She should tilt her umbrella forward, about $53^\circ$ from upright.

**Sanity check:** if the auto stopped ($v_A = 0$), the angle would be zero and the rain would look vertical again, just as at the bus stop.

## Where the picture breaks

Raindrops don't all fall at the same speed: big drops fall faster than small ones, so real streaks have a spread of angles. A phone video also shows each drop as a smear across one frame's exposure, which makes streaks look longer than the eye sees them. And close to a moving vehicle the air itself is dragged along and swirls, bending the drops' paths near the window. The subtraction $\vec{v}_R - \vec{v}_A$ is exact; still air and one drop speed are the idealisations.

## Key takeaway

The velocity of A relative to B is $\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$: take A's velocity and add B's velocity reversed, head to tail. For perpendicular velocities the size is $\sqrt{v_A^2 + v_B^2}$. That's why vertical rain looks slanted, and faster, from a moving vehicle.
