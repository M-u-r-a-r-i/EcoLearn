---
concept_id: distance
interest: motorsport
format: explain
title: The trip meter says 1.2 km and the car never left
check:
  question: |-
    During a brake test, a car accelerates $200\,\text{m}$ down a closed straight, then reverses $50\,\text{m}$ back to the timing beam. What distance has it covered?
  options:
    A: |-
      $250\,\text{m}$
    B: |-
      $150\,\text{m}$
    C: |-
      $200\,\text{m}$
    D: |-
      $-250\,\text{m}$
  answer: A
  explanation: |-
    Distance is the total length of the path, whichever way each leg goes: $200\,\text{m} + 50\,\text{m} = 250\,\text{m}$.
  misconceptions:
    B: |-
      Subtracts the reversing leg, $200 - 50$. That is how far the car ended up from the beam — the size of its displacement — not the path it covered.
    C: |-
      Takes the distance to be the farthest point reached from the start, ignoring the extra $50\,\text{m}$ of path travelled on the way back.
    D: |-
      Gives distance a sign because the last leg was backwards. Distance is a scalar built from lengths, so it can never be negative.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A long straight at a race circuit with a car accelerating away from the timing beam at the start line, distance boards reading 0, 100 and 200 along the verge, and an arrow marking the positive direction](scenes/motorsport/motion_straight_line.svg "Bedding in new brake pads means going up and down the same piece of tarmac, over and over.")

New brake pads have to be bedded in before they work properly, and Faizan's club has booked a closed service road for the morning — a straight $300\,\text{m}$ strip with a cone at each end. The job is simple and dull: accelerate to the far cone, brake hard, turn around, come back, repeat.

Faizan does it twice and pulls up beside his sister Meghna, who resets nothing and reads the trip meter aloud.

"One point two kilometres."

"That can't be right," she says. "You're parked exactly where you started. I watched you. You went nowhere."

Faizan points at his brake pedal, which now bites properly, and at the smell of hot pad material drifting through the window. Something definitely happened. And the trip meter is not a clever device — it just counts wheel turns.

Which number honestly answers "how far did the car go" — and why do the two of them disagree?

## The physics

**Distance** is the total length of the path an object actually travels. Three things follow from that definition:

- It adds up **every** part of the path, whichever direction that part points.
- It is a **scalar**: a size with a unit, and no direction.
- It can never be negative, and it never decreases as time goes on. The most it can do is stay the same, while the object is stopped.

Faizan's morning was four legs of $300\,\text{m}$:

$$d = 300 + 300 + 300 + 300 = 1200\,\text{m} = 1.2\,\text{km}$$

The legs that went "back the other way" still count in full. The wheels do not know which direction anyone has called positive; they simply turn, and the trip meter simply counts. That is why the meter reads $1.2\,\text{km}$, and why the pads are hot.

Meghna's answer is a different quantity: how far the car ended up from where it began, measured straight. That is (the size of) its **displacement**, which is the next lesson. When a journey never turns around, distance and displacement match. The moment the path doubles back, distance is the larger of the two.

![A path in three legs on a number line — 5 m forward, 5 m back, 3 m forward — with distance 13 m and displacement +3 m](figures/distance/path-legs-total.svg "Distance adds every leg as a positive length: 5 + 5 + 3 = 13 m. The start-to-end gap is only 3 m.")

In symbols, a path made of straight legs of lengths $d_1, d_2, d_3, \ldots$ has distance $d = d_1 + d_2 + d_3 + \cdots$, with every $d_i \ge 0$. Its SI unit is the metre.

## Worked example

**Given:** the strip is $300\,\text{m}$ between the cones. Faizan drives to the far cone, back to the start, and out to the far cone again — then a marshal waves him down, and he turns and drives $100\,\text{m}$ back before parking.
**Find:** the total distance covered, and how far he finished from where he started.

Distance adds every leg as a positive length:

$$d = 300 + 300 + 300 + 100 = 1000\,\text{m} = 1.0\,\text{km}$$

Where did he finish? After three legs he was at the far cone, $300\,\text{m}$ from the start. Driving $100\,\text{m}$ back leaves him

$$300 - 100 = 200\,\text{m}$$

from his starting point.

**Sanity check:** the distance ($1000\,\text{m}$) is far larger than the straight-line gap ($200\,\text{m}$), as it must be whenever a path doubles back — and a kilometre of gentle running up and down a strip is a very ordinary morning's bedding-in.

## Where the picture breaks

A trip meter counts wheel rotations, so it measures the path the *wheels* rolled, not the path of the car's centre: on a turn the inner and outer wheels roll different amounts, and a wheel that locks under braking slides without turning at all. Tyre wear changes the rolling radius slightly too, so the reading is a good estimate rather than an exact path length. And in this chapter every path lies along one line. Once a car turns onto a circuit, distance means the length along the curve, which a tape stretched from start to finish would badly underestimate.

## Key takeaway

Distance is the total length of the path travelled: add every leg as a positive number, whatever direction it points. It is a scalar, it is never negative, and it never goes down. Faizan really did cover $1.2\,\text{km}$ — even though the car finished in the same parking spot it started in.
