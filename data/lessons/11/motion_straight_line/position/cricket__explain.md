---
concept_id: position
interest: cricket
format: explain
title: Six metres or fourteen, where did the ball pitch
check:
  question: |-
    On the pitch map, the origin is at the striker's stumps and the positive direction points towards the bowler. The wicketkeeper stands $15\,\text{m}$ behind the striker's stumps, so $x = -15\,\text{m}$. The analyst switches the origin to the bowler's stumps, with the positive direction now pointing towards the striker. The stumps are $20.12\,\text{m}$ apart. What is the keeper's position in the new description?
  options:
    A: |-
      $x' = -15.0\,\text{m}$
    B: |-
      $x' = +35.1\,\text{m}$
    C: |-
      $x' = +5.1\,\text{m}$
    D: |-
      $x' = -35.1\,\text{m}$
  answer: B
  explanation: |-
    From the bowler's stumps, the keeper is the whole pitch plus $15\,\text{m}$ further on, in the new positive direction: $x' = 20.12 + 15 = +35.1\,\text{m}$.
  misconceptions:
    A: |-
      Thinks a position belongs to the object itself, so it stays the same when the origin moves. A position is always measured from a chosen origin.
    C: |-
      Subtracts $15$ from the pitch length, placing the keeper between the stumps — as if "behind the striker" meant "towards the bowler".
    D: |-
      Gets the right size but keeps the minus sign from the old description. The sign depends on which way the new positive direction points, and the keeper is now on the positive side.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground in sunshine: a batter runs between the wickets on a 22-yard pitch while a fielder chases the ball towards the boundary rope](scenes/cricket/motion_straight_line.svg "Every event on this pitch happens somewhere along one line, 20.12 m long between the stumps.")

It is the inter-school final, and Kabir has talked his way into the commentary box. Beside him, Diya runs the school's tablet app that marks where each delivery pitches.

The quick bowler hits a perfect length. "That pitched six metres out!" Kabir announces.

Diya shakes her head and taps her screen. "My app says fourteen metres."

"Fourteen? That would be a bouncer," Kabir scoffs. "It was a good length."

"It *was* a good length," Diya insists. "And fourteen metres is correct."

They replay the delivery. Same ball, same bounce mark on the pitch, one small scuff on the dry surface. Neither of them misread anything, and neither of them changes their number. Kabir starts to wonder whether the app is broken; Diya wonders whether Kabir is.

How can one spot on the pitch honestly have two different numbers — and what would you need to say so that everyone agrees on it?

## The physics

To describe where something is along a straight line, you need three things:

1. An **origin** — a reference point you call zero.
2. A **positive direction** — which way along the line counts as "plus".
3. A **unit** — usually metres.

With these fixed, the **position** of an object is a single signed number $x$: its distance from the origin, with a plus sign if it lies on the positive side and a minus sign if it lies on the other side. The line with its origin, direction and scale is called a **frame of reference** for one-dimensional motion (NCERT uses the $x$-axis for this).

Kabir measured from the **striker's stumps**, with positive pointing towards the bowler: the ball pitched at $x = +6\,\text{m}$. Diya's app measures from the **bowler's stumps**, with positive pointing towards the striker. The stumps are $22$ yards $= 20.12\,\text{m}$ apart, so the same spot is at $20.12 - 6 = 14.12\,\text{m}$, which she rounded to fourteen. Both are correct. A position number means nothing until the origin and the positive direction have been said.

![Two number lines showing the same points P and Q: with origin O and positive to the right P is at +4 m and Q at −3 m; with origin O′ at the right end and positive to the left, P is at +2 m and Q at +9 m](figures/position/origin-and-direction.svg "Moving the origin or flipping the positive direction changes the numbers, not the places. The gap between P and Q is 7 m in both.")

Notice two things in the figure. A negative position is not "less real" — it just means "on the other side of the origin". And while the numbers change between frames, the **separation** between two points does not: P and Q are $7\,\text{m}$ apart in both descriptions.

## Worked example

**Given:** origin at the striker's stumps, positive towards the bowler. The ball pitches $6.00\,\text{m}$ in front of the striker's stumps; the keeper stands $15.0\,\text{m}$ behind them (illustrative). The stumps are $20.12\,\text{m}$ apart.
**Find:** each position in this frame, then in a frame with the origin at the bowler's stumps and positive towards the striker.

In the first frame: bounce $x_\text{b} = +6.00\,\text{m}$; bowler's stumps $x_\text{s} = +20.12\,\text{m}$; keeper $x_\text{k} = -15.0\,\text{m}$ (behind the origin, so negative).

In the new frame, a point at $x$ is $20.12 - x$ metres from the bowler's stumps, on the positive side. So $x' = 20.12 - x$:

$$x'_\text{b} = 20.12 - 6.00 = +14.12\,\text{m}$$
$$x'_\text{k} = 20.12 - (-15.0) = +35.1\,\text{m}$$

and the striker's stumps are at $x' = +20.12\,\text{m}$.

**Sanity check:** the gap between bounce and keeper is $6.00 - (-15.0) = 21.0\,\text{m}$ in the first frame and $35.12 - 14.12 = 21.0\,\text{m}$ in the second. The places didn't move, so the gap mustn't change — and it doesn't.

## Where the picture breaks

A real delivery is not on a single line. The ball can pitch a little outside off stump, and it travels through the air at some height, so its true position needs three numbers ($x$, $y$, $z$). Here we have kept only the component along the pitch — fine for "how far up the pitch", useless for "how wide of off stump". You will need more axes in *Motion in a Plane*. We also treated the ball as a point; really we are tracking its centre, since the ball itself is about $7\,\text{cm}$ across. And "the stumps" are three sticks, not a point — the origin is an agreed line through them.

## Key takeaway

Position is a signed number $x$ that only makes sense once you have chosen an origin and a positive direction. Change either, and every number changes — but the places, and the distances between them, stay exactly the same. Always say your frame before you say your numbers.
