---
concept_id: distance
interest: gaming
format: explain
title: The stats screen that says you walked 280 metres
check:
  question: |-
    In a side-scroller, your character runs $40\,\text{m}$ to the right to pull a lever, then turns and runs $15\,\text{m}$ back to the left to a door that has just opened. What distance has the character covered?
  options:
    A: |-
      $55\,\text{m}$
    B: |-
      $25\,\text{m}$
    C: |-
      $-55\,\text{m}$
    D: |-
      $40\,\text{m}$
  answer: A
  explanation: |-
    Distance is the total length of the path, whatever the direction of each leg: $40\,\text{m} + 15\,\text{m} = 55\,\text{m}$.
  misconceptions:
    B: |-
      Subtracts the backward leg, $40 - 15 = 25\,\text{m}$. That is how far the character ended up from the start (the size of the displacement), not the distance run.
    C: |-
      Gives distance a sign because the last leg went left. Distance is a scalar and can never be negative.
    D: |-
      Takes the distance to be the farthest point reached from the start, ignoring the extra path run on the way back.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a monitor shows a side-scrolling game whose runner moves along a straight track marked like a number line, with a position and velocity readout; a tablet replays a velocity-time graph](scenes/gaming/motion_straight_line.svg "Side-scroller quests send you left and right along the same strip of ground, again and again.")

Rehan has been stuck on the same side-scrolling quest for an hour. The village elder wants water from the well, so Rehan runs his character right to the well, fills the bucket, and runs back left to the village. Then the elder says the blacksmith needs it more — and the forge is past the well, further to the right. Off he goes again.

When the quest finally completes, a stats screen pops up: *Distance travelled: 280 m.*

His younger brother Kabir, watching from the bed, laughs. "Bugged. Look at the map. The forge is a hundred and twenty metres from the village. You started at the village, you ended at the forge. That's a hundred and twenty."

"Then why did it take me so long?" Rehan says.

Kabir is sure the map is right. Rehan is sure the game counts properly — its step counter unlocks an achievement.

Which number answers "how far did the character go" — and why do the two disagree?

## The physics

**Distance** is the total length of the path an object actually travels. It has three defining properties:

- It adds up **every** part of the path, whichever way that part goes.
- It is a **scalar**: a size with a unit, but no direction.
- It can never be negative, and it never decreases as time goes on. The most it can do is stay the same, while the object stands still.

Put the village at $0$ and take the well to be $80\,\text{m}$ away and the forge $120\,\text{m}$ away, on the same side (illustrative numbers). Rehan's quest had three legs:

$$\text{distance} = 80\,\text{m} + 80\,\text{m} + 120\,\text{m} = 280\,\text{m}$$

The middle leg went back towards the village, but it still counts in full — the character's legs ran every one of those metres. That is the game's $280\,\text{m}$.

Kabir's $120\,\text{m}$ is a different quantity: how far the character ended up from where it started, in a straight line. That is (the size of) the **displacement**, which you'll meet in the next lesson. For a trip that never turns back, the two are equal; as soon as the path doubles back, distance becomes larger.

![A path in three legs on a number line — 5 m forward, 5 m back, 3 m forward — with distance 13 m and displacement +3 m](figures/distance/path-legs-total.svg "Distance adds every leg as a positive length: 5 + 5 + 3 = 13 m, even though the trip ends only 3 m from the start.")

In symbols, if a path is made of straight legs of lengths $d_1, d_2, d_3, \ldots$ then the distance is $d = d_1 + d_2 + d_3 + \cdots$, with every $d_i \ge 0$. Its SI unit is the metre.

## Worked example

**Given:** a speedrunner, Divya, starts a level at $x = 0$. She runs $60\,\text{m}$ right to grab a key, $35\,\text{m}$ back left to a locked door, then $90\,\text{m}$ right to the exit (illustrative).
**Find:** the distance she ran, and how far from the start she finished.

Distance adds every leg:

$$d = 60 + 35 + 90 = 185\,\text{m}$$

Where did she finish? Track the position leg by leg: $0 \to 60\,\text{m} \to 60 - 35 = 25\,\text{m} \to 25 + 90 = 115\,\text{m}$. She finished $115\,\text{m}$ from the start.

**Sanity check:** the distance ($185\,\text{m}$) is more than the start-to-finish gap ($115\,\text{m}$), as it must be once the path turns back. The extra $70\,\text{m}$ is exactly the $35\,\text{m}$ backtrack plus the $35\,\text{m}$ she then had to run again to get back past the key: $2 \times 35 = 70$. That is why speedrunners hunt for routes with no backtracking.

## Where the picture breaks

A game can count distance exactly, because it knows the character's position every frame and adds up the small steps; a fitness band on your wrist has to estimate it and can be off. Still, the game counts what its programmers chose — some count every tiny wobble, some only horizontal movement, and jumping adds path length up and down that a side-scroller's stats may ignore. Here we have kept everything on one line. On a curved route (a racing track, say) distance is the length measured along the curve, which is always at least the straight-line gap between start and finish.

## Key takeaway

Distance is the total length of the path travelled: add every leg as a positive number, whatever its direction. It is a scalar, never negative, and it never goes down. Rehan's character really did run $280\,\text{m}$, even though it finished only $120\,\text{m}$ from where it started.
