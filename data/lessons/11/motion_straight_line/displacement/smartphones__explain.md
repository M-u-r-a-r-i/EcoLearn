---
concept_id: displacement
interest: smartphones
format: explain
title: The phone left in the auto-rickshaw
check:
  question: |-
    Take the origin at a metro station on a straight road, with the positive direction towards the market. A tracker app shows a lost pair of earbuds at $x = +250\,\text{m}$. An hour later, after someone has carried them past the station, the app shows $x = -150\,\text{m}$. What is the displacement of the earbuds?
  options:
    A: |-
      $+400\,\text{m}$
    B: |-
      $+100\,\text{m}$
    C: |-
      $-150\,\text{m}$
    D: |-
      $-400\,\text{m}$
  answer: D
  explanation: |-
    Displacement is final position minus initial position: $\Delta x = (-150) - (+250) = -400\,\text{m}$. The earbuds moved $400\,\text{m}$ in the negative direction, away from the market.
  misconceptions:
    A: |-
      Subtracts the wrong way round (initial minus final), or drops the sign because displacement "is how far it moved". The sign carries the direction and must come from final minus initial.
    B: |-
      Adds the two positions, $250 + (-150)$, as if displacement were a total of the readings rather than the change between them.
    C: |-
      Gives the final position as the displacement. Position says where the earbuds are, measured from the origin; displacement says how their position changed.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![An evening street: a phone shows a live-tracking map of a straight road, while a delivery scooter rides past kilometre markers](scenes/smartphones/motion_straight_line.svg "On a tracking map, everything moves along the road: one way or the other.")

Kavya steps out of the auto-rickshaw at her college gate, pays, and waves goodbye. Two minutes later, in the corridor, her hand goes to her pocket. Empty. Her phone is on the auto's back seat.

Her friend Imran opens the find-my-device page on his own phone and logs her in. A little dot is moving along the main road, which runs dead straight past the college. They watch it go up the road, stop, then come back part of the way and sit still at an auto stand.

"It's travelled three point four kilometres," Imran reads from the trail. "That's miles. We'll need a bus."

"I don't care how far it went," Kavya says, grabbing her bag. "I care how far *I* have to go — and which way to turn when I walk out of the gate."

The auto's long journey and Kavya's short walk are two very different numbers. Which one is she really asking for — and why does she need a direction as well as a size?

## The physics

**Displacement** is the change in position. In one dimension, if an object starts at position $x_i$ and ends at $x_f$:

$$\Delta x = x_f - x_i$$

It is a **vector**: it has a size and a direction. Along a line, the direction is carried by the **sign** — $+$ if the object ended up further along the positive direction, $-$ if it ended up further along the negative direction.

Three properties follow from the definition:

- It depends only on the **start and the end**, not on the path in between.
- Its size is never larger than the distance travelled — equal if the path never turns back, smaller if it does.
- A round trip gives $\Delta x = 0$, however far the object went.

![Three trips on a line: from 1 m to 5 m gives Δx = +4 m; from 5 m to 2 m gives Δx = −3 m; out 3 m and back gives Δx = 0 m although the distance is 6 m](figures/displacement/sign-in-one-dimension.svg "Displacement is final minus initial. The arrow's direction gives the sign; a round trip gives zero whatever the distance.")

Put the origin at the college gate, with positive pointing up the road, the way the auto drove off (illustrative numbers). The auto went up to $x = +2.4\,\text{km}$ to drop another passenger, then came back $1.0\,\text{km}$ and parked at $x = +1.4\,\text{km}$. The phone's distance travelled is $2.4 + 1.0 = 3.4\,\text{km}$ — Imran's number. Its displacement is

$$\Delta x = x_f - x_i = (+1.4) - 0 = +1.4\,\text{km}$$

That is exactly what Kavya needs: $1.4\,\text{km}$, turning in the positive direction out of the gate. The map shows the phone as a dot — a position — and the arrow from her to that dot is a displacement.

## Worked example

**Given:** origin at the college gate, positive up the road. The phone starts at $x = 0$, is carried to $x = +2.4\,\text{km}$, then back to $x = +1.4\,\text{km}$.
**Find:** the phone's displacement for (a) the first stage, (b) the second stage, (c) the whole trip; and (d) Kavya's displacement when she walks to the auto stand and then home to the gate again.

(a) $\Delta x_1 = 2.4 - 0 = +2.4\,\text{km}$ — up the road.

(b) $\Delta x_2 = 1.4 - 2.4 = -1.0\,\text{km}$ — the minus sign says the auto came back down the road.

(c) $\Delta x = 1.4 - 0 = +1.4\,\text{km}$. Check: $\Delta x_1 + \Delta x_2 = 2.4 + (-1.0) = +1.4\,\text{km}$. Displacements in a line add with their signs.

(d) Out to the stand: $+1.4\,\text{km}$. Back: $0 - 1.4 = -1.4\,\text{km}$. Total: $0$, although she walks $2.8\,\text{km}$.

**Sanity check:** the phone's displacement ($1.4\,\text{km}$) is smaller than its distance ($3.4\,\text{km}$), as it must be for a path that turned back. And reversing a trip flips the sign of its displacement and nothing else, as in (d).

## Where the picture breaks

A real main road bends a little, and the tracking dot comes from the phone's location fix, which can be off by several metres and jumps around between updates; a stationary phone can even seem to wander. We have also squeezed everything onto one line. If the auto had turned into a side street, the displacement would need two numbers — a direction on the map, not just a sign — which you'll meet in *Motion in a Plane*. The tracker itself is real and useful, but the physics here is simpler than the app: one line, one origin, one sign.

## Key takeaway

Displacement is the change in position, $\Delta x = x_f - x_i$: a vector pointing from where something started to where it finished, with its direction shown by the sign in one dimension. It ignores the route, so an auto's $3.4\,\text{km}$ ride can leave a phone just $1.4\,\text{km}$ up the road.
