---
concept_id: distance
interest: smartphones
format: explain
title: How a phone call in a corridor became a 1.2 km walk
check:
  question: |-
    A robot vacuum cleaner, steered from a phone app, moves along a straight hallway. It goes $4.0\,\text{m}$ forward, reverses $1.5\,\text{m}$ to get round a chair leg, then goes $1.0\,\text{m}$ forward again. What distance has it travelled?
  options:
    A: |-
      $6.5\,\text{m}$
    B: |-
      $3.5\,\text{m}$
    C: |-
      $5.0\,\text{m}$
    D: |-
      $4.0\,\text{m}$
  answer: A
  explanation: |-
    Distance is the total length of the path, every leg counted as positive whatever its direction: $4.0 + 1.5 + 1.0 = 6.5\,\text{m}$.
  misconceptions:
    B: |-
      Subtracts the reversing leg, $4.0 - 1.5 + 1.0 = 3.5\,\text{m}$. That is how far the vacuum ended up from its start (its displacement), not the distance it travelled.
    C: |-
      Leaves out the reversing leg, as if moving backwards "doesn't count". Every part of the path adds to the distance.
    D: |-
      Takes the distance to be the farthest point the vacuum reached from its start, ignoring the extra path it covered going back and forth.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![An evening street: a phone shows a live-tracking map of a straight road, while a delivery scooter rides past kilometre markers](scenes/smartphones/motion_straight_line.svg "Phones keep count of how far things travel — the rider, the scooter, and you.")

Mehak's best friend has moved to another city, and their Sunday phone calls last for ages. Mehak can't talk sitting down, so she paces the hostel corridor: to the window at the far end, turn, back to her door, turn, again and again.

After a forty-minute call, her phone's step-counter app buzzes with a cheerful message: *1.2 km walked today!*

Her roommate Tanya bursts out laughing. "One point two kilometres? The corridor is thirty metres long. You started at our door and you're standing at our door. You haven't gone anywhere!"

Mehak looks at the screen, then at the corridor, then at her aching feet.

The app isn't lying — it has counted every step. But Tanya is right that Mehak is exactly where she began. How can a thirty-metre corridor hold a 1.2-kilometre walk, and which of them is answering "how far did she go"?

## The physics

**Distance** is the total length of the path an object actually travels. It has three defining properties:

- It adds up **every** part of the path, whichever way that part goes.
- It is a **scalar**: a size with a unit, but no direction.
- It can never be negative, and it never decreases as time goes on. At most it stays the same, while the object is at rest.

Mehak's call is a string of straight legs along the corridor, each $30\,\text{m}$ long (illustrative). Forty lengths — twenty trips to the window and back — give

$$\text{distance} = 40 \times 30\,\text{m} = 1200\,\text{m} = 1.2\,\text{km}$$

Walking back towards her door doesn't "cancel" the walk to the window. Both legs are real metres covered by her feet, so both count in full.

Tanya is describing a different quantity: how far Mehak ended up from her starting point, in a straight line. That is (the size of) her **displacement**, the next idea in this chapter. For Mehak it is zero. For a trip that never turns around, distance and the size of the displacement are equal; the moment the path doubles back, distance becomes larger.

![A path in three legs on a number line — 5 m forward, 5 m back, 3 m forward — with distance 13 m and displacement +3 m](figures/distance/path-legs-total.svg "Distance adds every leg as a positive length: 5 + 5 + 3 = 13 m. The start-to-end gap is only 3 m.")

In symbols, if a path is made of straight legs of lengths $d_1, d_2, d_3, \ldots$ then the distance is $d = d_1 + d_2 + d_3 + \cdots$, with every $d_i \ge 0$. Its SI unit is the metre.

## Worked example

**Given:** a straight corridor $30\,\text{m}$ long. Mehak starts at her door (one end), walks $40$ full lengths during the call, then walks $15\,\text{m}$ towards the window to look outside (illustrative).
**Find:** the distance she walked, and how far she finished from her door.

Distance adds every leg:

$$d = 40 \times 30 + 15 = 1200 + 15 = 1215\,\text{m}$$

Where did she finish? Each pair of lengths (there and back) brings her to her door again. Forty lengths is twenty pairs, so after the call she is back at the door. The last $15\,\text{m}$ leaves her $15\,\text{m}$ from it.

**Sanity check:** the distance ($1215\,\text{m}$) is far bigger than the $15\,\text{m}$ gap between start and finish, as it must be for a path that turned back forty times. And it can't be less than $15\,\text{m}$ — no path between two points is shorter than the straight line joining them.

## Where the picture breaks

A step counter doesn't measure distance directly. It counts steps from the jolts its motion sensor feels, then multiplies by an estimated stride length, so its "1.2 km" could be off by a fair amount — a shuffling turn at each end may count as steps that went nowhere. We have also pretended Mehak walks along one perfect line. Real pacing wanders from side to side, which adds a little extra path. The phone's sensor is a genuine device doing a genuine job here, but the physics of distance is simply about path length: the app is only one, rather rough, way of adding it up.

## Key takeaway

Distance is the total length of the path travelled: add every leg as a positive number, whatever its direction. It is a scalar, never negative, and never goes down. Forty lengths of a $30\,\text{m}$ corridor are $1.2\,\text{km}$ of distance, even if you finish exactly where you started.
