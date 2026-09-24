---
concept_id: position
interest: motorsport
format: explain
title: Sixty metres or a hundred and forty
check:
  question: |-
    Race control measures along the straight from the start line, with the positive direction pointing towards the corner. The pit-lane exit is $40\,\text{m}$ behind the start line, so $x = -40\,\text{m}$. A marshal instead measures from the corner-entry board, $200\,\text{m}$ from the start line, with positive now pointing back towards the start line. What is the pit-lane exit's position in the marshal's description?
  options:
    A: |-
      $x' = -40\,\text{m}$
    B: |-
      $x' = +160\,\text{m}$
    C: |-
      $x' = +240\,\text{m}$
    D: |-
      $x' = -240\,\text{m}$
  answer: C
  explanation: |-
    From the corner board, the exit is the whole $200\,\text{m}$ straight plus a further $40\,\text{m}$, all in the new positive direction: $x' = 200 + 40 = +240\,\text{m}$.
  misconceptions:
    A: |-
      Treats a position as a property of the place itself, unchanged when the origin moves. A position is always measured from a chosen origin, so moving the origin changes it.
    B: |-
      Computes $200 - 40$, which puts the exit on the straight — as if "behind the start line" meant "towards the corner".
    D: |-
      Gets the right size but keeps the minus sign from race control's description. The sign depends on the new positive direction, and the exit lies on its positive side.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A long straight at a race circuit with a car accelerating away from the timing beam at the start line, distance boards reading 0, 100 and 200 along the verge, and an arrow marking the positive direction](scenes/motorsport/motion_straight_line.svg "Every event on this straight happens somewhere along one line — but only once you say where you are counting from.")

Halfway through the club karting final, a chain snaps. The kart coasts silently down the main straight and stops against the inside verge.

In race control, Devika reads the trackside camera overlay and writes it in the log: *kart stopped at 60 metres*.

Ten seconds later the marshal's radio crackles. It is Arnav, standing on the verge with a clear view. "Recovery needed. Kart is at a hundred and forty."

Devika keys the mic. "Sixty."

"A hundred and forty," says Arnav. "I'm looking at it."

They are looking at the same kart, on the same straight, and neither of them has misread anything. The recovery crew is now waiting to be told where to go.

How can one spot on one straight honestly carry two different numbers — and what would each of them have to say for the other to agree?

## The physics

To say where something is along a straight line, you must fix three things first:

1. An **origin** — the point you call zero.
2. A **positive direction** — which way along the line counts as "plus".
3. A **unit** — the metre.

Once those are fixed, the **position** of an object is a single signed number $x$: its distance from the origin, with a plus sign if it lies on the positive side and a minus sign if it lies on the other side. The line together with its origin, direction and scale is a **frame of reference** for one-dimensional motion; NCERT draws it as the $x$-axis.

Devika measures from the **start line**, positive towards the corner, so the kart is at $x = +60\,\text{m}$. Arnav counts from the **corner-entry board**, positive back towards the start line. The straight between them is $200\,\text{m}$ long (illustrative), so the same kart sits at $200 - 60 = +140\,\text{m}$ in his frame. Both numbers are right. A position means nothing until the origin and the positive direction have been stated — which is exactly what the radio call left out.

![Two number lines showing the same points P and Q: with origin O and positive to the right P is at +4 m and Q at −3 m; with origin O′ at the right end and positive to the left, P is at +2 m and Q at +9 m](figures/position/origin-and-direction.svg "Moving the origin or flipping the positive direction changes the numbers, not the places. The gap between P and Q is 7 m in both.")

Two things in the figure are worth holding on to. A negative position is not stranger or smaller than a positive one — it just means "on the other side of the origin". And although the numbers change from frame to frame, the **separation** between two points does not.

## Worked example

**Given:** the straight is $200\,\text{m}$ from the start line to the corner-entry board. Race control's frame has its origin at the start line, positive towards the corner. The stopped kart is $60\,\text{m}$ along; the marshal's post stands $25\,\text{m}$ behind the start line (illustrative).
**Find:** both positions in race control's frame, and then in the marshal's frame, whose origin is the corner board with positive back towards the start line.

In race control's frame: kart $x_\text{k} = +60\,\text{m}$; marshal's post $x_\text{m} = -25\,\text{m}$, because it lies on the negative side of the origin.

In the marshal's frame, a point at $x$ is $200 - x$ metres from the corner board, on the positive side, so $x' = 200 - x$:

$$x'_\text{k} = 200 - 60 = +140\,\text{m}$$

$$x'_\text{m} = 200 - (-25) = +225\,\text{m}$$

**Sanity check:** the gap between the kart and the marshal's post is $60 - (-25) = 85\,\text{m}$ in one frame and $225 - 140 = 85\,\text{m}$ in the other. Nothing moved, so the gap must not change — and it doesn't.

## Where the picture breaks

A straight is not really a line. The kart also has a position across the track — inside verge or racing line — and the track has a gradient, so a full description needs three numbers ($x$, $y$, $z$). We have kept only the component along the straight, which is what a recovery crew needs and useless for saying which side to approach from. We have also treated the kart as a point, when it is about two metres long, so "the kart is at $60\,\text{m}$" really means its centre, or its nose, and the log should say which. And $200\,\text{m}$ is the length of this imagined straight, not of any real one.

## Key takeaway

Position is a signed number $x$, and it only means something once you have named an origin and a positive direction. Change either and every number changes, while the places and the gaps between them stay exactly as they were. Say your frame before you say your numbers — or the recovery crew goes to the wrong end of the straight.
