---
concept_id: position
interest: gaming
format: explain
title: The chest at 120 that was also at minus 30
check:
  question: |-
    In a side-scrolling level, the origin is at the spawn point and the positive direction points right. A portal sits $25\,\text{m}$ to the left of spawn, so $x = -25\,\text{m}$. In "mirror mode" the game redraws the same level with the origin at the finish flag, which is $200\,\text{m}$ to the right of spawn, and the positive direction now pointing left. What is the portal's position in the mirror-mode description?
  options:
    A: |-
      $x' = -25\,\text{m}$
    B: |-
      $x' = +175\,\text{m}$
    C: |-
      $x' = -225\,\text{m}$
    D: |-
      $x' = +225\,\text{m}$
  answer: D
  explanation: |-
    From the finish flag, the portal is the whole $200\,\text{m}$ to spawn plus $25\,\text{m}$ more, all in the new positive direction (left): $x' = 200 - (-25) = +225\,\text{m}$.
  misconceptions:
    A: |-
      Thinks a position belongs to the object, so it stays the same when the origin and direction change. A position is always measured from a chosen origin in a chosen direction.
    B: |-
      Subtracts $25$ from $200$, putting the portal between spawn and the flag — treating "left of spawn" as if it were towards the flag.
    C: |-
      Gets the right size but keeps a minus sign. In mirror mode the positive direction points left, and the portal lies to the left of the new origin, so its position is positive.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a monitor shows a side-scrolling game whose runner moves along a straight track marked like a number line, with a position and velocity readout; a tablet replays a velocity-time graph](scenes/gaming/motion_straight_line.svg "In a side-scroller, everything happens along one line. The HUD's x only means something once you know where its zero is.")

It is 11 p.m. and Aarav and Ishita are deep into a co-op run of a side-scrolling platformer, talking over voice chat from their own rooms.

Ishita spots a hidden treasure chest behind a waterfall. "Chest at minus thirty! Come back!"

Aarav has the game's debug overlay switched on. He checks it. "Minus? Nothing on this level is at minus thirty near you. The overlay says the waterfall is at one hundred and twenty."

"I'm literally standing next to it. Minus thirty."

"One-twenty."

Neither of them is misreading a screen. Ishita even sends a screenshot, and there is her character, beside the chest, beside the waterfall. Aarav starts to suspect a glitch in her copy of the game. Ishita starts to suspect Aarav.

How can one chest, in one place, honestly have two different numbers — and what would they need to agree on before the number means anything?

## The physics

To describe where something is along a straight line, you need three things:

1. An **origin** — a reference point you call zero.
2. A **positive direction** — which way along the line counts as "plus".
3. A **unit** — here, metres (games often use their own units, but let's say this one uses metres).

With these fixed, the **position** of an object is a single signed number $x$: its distance from the origin, with a plus sign on the positive side and a minus sign on the other side. The line, with its origin, direction and scale, is the **frame of reference** for one-dimensional motion — NCERT calls it the $x$-axis.

Aarav's debug overlay measures from the **spawn point**, with positive to the right. Ishita, playing by ear, measures from the **checkpoint flag** she just passed, which sits at $x = +150\,\text{m}$ in Aarav's frame (illustrative numbers), also with positive to the right. The chest is $30\,\text{m}$ short of the flag, so she calls it $-30\,\text{m}$; Aarav's overlay calls it $150 - 30 = +120\,\text{m}$. Both are right. A position means nothing until the origin and the positive direction have been said.

![Two number lines showing the same points P and Q: with origin O and positive to the right P is at +4 m and Q at −3 m; with origin O′ at the right end and positive to the left, P is at +2 m and Q at +9 m](figures/position/origin-and-direction.svg "Moving the origin or flipping the positive direction changes the numbers, not the places. P and Q stay 7 m apart in both frames.")

The figure shows the two changes you can make: moving the origin, and flipping which way is positive. A negative position isn't "less real" — it only means "on the other side of the origin". And the **separation** between two points never depends on the frame.

## Worked example

**Given:** Aarav's frame — origin at spawn, positive right. Checkpoint flag at $+150\,\text{m}$, chest at $+120\,\text{m}$, and a secret cave $20\,\text{m}$ left of spawn, at $-20\,\text{m}$ (illustrative).
**Find:** each position (a) in Ishita's frame, origin at the flag and positive right; (b) in "mirror mode", origin at the flag and positive left.

(a) Moving the origin $150\,\text{m}$ to the right subtracts $150$ from every position: $x' = x - 150$.

$$x'_\text{chest} = 120 - 150 = -30\,\text{m}, \qquad x'_\text{cave} = -20 - 150 = -170\,\text{m}$$

(b) Flipping the direction as well flips every sign: $x'' = 150 - x$.

$$x''_\text{chest} = 150 - 120 = +30\,\text{m}, \qquad x''_\text{cave} = 150 - (-20) = +170\,\text{m}$$

**Sanity check:** the gap from cave to chest is $120 - (-20) = 140\,\text{m}$ in Aarav's frame, $-30 - (-170) = 140\,\text{m}$ in Ishita's, and $170 - 30 = 140\,\text{m}$ in mirror mode. The places didn't move, so the gap can't change — and it doesn't.

## Where the picture breaks

A side-scroller is unusually kind: the track really is one line, so one number $x$ does the job. Even there, the character can jump, so a full position needs a height $y$ as well; we kept only the along-the-track part. Most 3D games need three coordinates, which you'll meet in *Motion in a Plane*. The overlay also tracks a single point on the character (usually its centre or its feet), not the whole sprite. And a game's "metre" is whatever the developers decided — the physics of frames and origins is the same whatever the unit.

## Key takeaway

Position is a signed number $x$ that only makes sense once you have chosen an origin and a positive direction. Move the origin or flip the direction and every number changes — but the places, and the distances between them, stay exactly the same. Say your frame before you say your numbers.
