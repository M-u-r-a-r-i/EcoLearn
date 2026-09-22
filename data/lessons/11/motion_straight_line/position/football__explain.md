---
concept_id: position
interest: football
format: explain
title: Twelve metres or forty, where was the striker
check:
  question: |-
    On a $105\,\text{m}$ pitch, an analyst puts the origin at the halfway line, with the positive direction towards the opponents' goal. Your own goalkeeper stands at $x = -47.0\,\text{m}$. The analyst then switches the origin to the opponents' goal line, with the positive direction now pointing back towards the halfway line. The halfway line is $52.5\,\text{m}$ from each goal line. What is your goalkeeper's position in the new description?
  options:
    A: |-
      $x' = -47.0\,\text{m}$
    B: |-
      $x' = +5.5\,\text{m}$
    C: |-
      $x' = -99.5\,\text{m}$
    D: |-
      $x' = +99.5\,\text{m}$
  answer: D
  explanation: |-
    From the opponents' goal line, your keeper is the $52.5\,\text{m}$ to halfway plus another $47.0\,\text{m}$ beyond it, all in the new positive direction: $x' = 52.5 + 47.0 = +99.5\,\text{m}$.
  misconceptions:
    A: |-
      Thinks a position belongs to the player, so it stays the same when the origin moves. A position is always measured from a chosen origin.
    B: |-
      Subtracts $47.0$ from $52.5$, placing the keeper between the halfway line and the opponents' goal — as if being in your own half were on the same side as the opponents' goal.
    C: |-
      Gets the right size but keeps the minus sign from the old description. The sign depends on which way the new positive direction points, and the keeper is now on the positive side.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A winger dribbles along the touchline towards goal, chased by a defender, while the goalkeeper comes off the line; a number line with origin O and +x runs beneath](scenes/football/motion_straight_line.svg "Every run along this touchline can be written as one number on the line below — once you have said where zero is and which way is plus.")

It is the district under-17 final, and Anika has the job of live-texting the match for the school group. Beside her in the stand, Rehan runs a free analysis app that logs where each shot is struck from.

The keeper is caught off his line, and the striker tries an audacious lob. "Shot from twelve metres!" Anika types.

Rehan glances at his screen. "My app says forty and a half."

"Forty? Forty is miles," Anika says. "I watched him. Twelve metres, I'm sure of it."

"Twelve metres from *what*?" Rehan asks. He isn't sure of his own number either; the app just prints it.

They replay the clip on his phone. Same striker, same spot, same patch of scuffed grass. Neither of them has misread anything, and each is certain of their own number.

How can one spot on the pitch honestly be both twelve and forty and a half — and what would you have to say so that everyone agrees?

## The physics

To describe where something is along a straight line, you need three things:

1. An **origin** — a reference point you call zero.
2. A **positive direction** — which way along the line counts as "plus".
3. A **unit** — usually metres.

With these fixed, the **position** of an object is a single signed number $x$: its distance from the origin, with a plus sign on the positive side and a minus sign on the other side. The line with its origin, direction and scale is a **frame of reference** for one-dimensional motion (NCERT uses the $x$-axis for this).

Take this pitch as $105\,\text{m}$ long (illustrative, and inside the Laws of the Game range of $90$–$120\,\text{m}$), so the halfway line is $52.5\,\text{m}$ from each goal line. Anika measured from the **halfway line**, with positive towards the opponents' goal: the shot came from $x = +12\,\text{m}$. Rehan's app measures from the **opponents' goal line**, with positive pointing back up the pitch. The same spot is $52.5 - 12 = 40.5\,\text{m}$ from that line. Both are correct. A position means nothing until the origin and the positive direction have been said.

![Two number lines showing the same points P and Q: with origin O and positive to the right P is at +4 m and Q at −3 m; with origin O′ at the right end and positive to the left, P is at +2 m and Q at +9 m](figures/position/origin-and-direction.svg "Moving the origin or flipping the positive direction changes the numbers, not the places. The gap between P and Q is 7 m in both.")

Two things to notice. A negative position is not "less real" — it just means "on the other side of the origin". And while the numbers change between frames, the **separation** between two points does not.

## Worked example

**Given:** origin at the halfway line, positive towards the opponents' goal, halfway $52.5\,\text{m}$ from each goal line. The striker is $12.0\,\text{m}$ into the opponents' half; your own keeper is $47.0\,\text{m}$ back in your half (illustrative). The opponents' penalty mark is $11\,\text{m}$ from their goal line.
**Find:** each position in this frame, then in a frame with the origin on the opponents' goal line and positive back towards halfway.

First frame: striker $x_\text{s} = +12.0\,\text{m}$; keeper $x_\text{k} = -47.0\,\text{m}$ (behind the origin); penalty mark $x_\text{p} = 52.5 - 11 = +41.5\,\text{m}$.

In the new frame, a point at $x$ is $52.5 - x$ metres from the opponents' goal line, on the positive side. So $x' = 52.5 - x$:

$$x'_\text{s} = 52.5 - 12.0 = +40.5\,\text{m}, \qquad x'_\text{p} = 52.5 - 41.5 = +11.0\,\text{m}$$
$$x'_\text{k} = 52.5 - (-47.0) = +99.5\,\text{m}$$

The penalty mark comes out at $11.0\,\text{m}$ from the goal line, exactly as the Laws say — a good sign the conversion is right.

**Sanity check:** the gap between striker and keeper is $12.0 - (-47.0) = 59.0\,\text{m}$ in the first frame and $99.5 - 40.5 = 59.0\,\text{m}$ in the second. The places didn't move, so the gap mustn't change.

## Where the picture breaks

A real pitch is two-dimensional: a shot can come from near the touchline or dead centre, so its full position needs two numbers (three, if you count height). Here we kept only the component along the length of the pitch — fine for "how far out", useless for "how wide". You'll add axes in *Motion in a Plane*. We also treated the striker as a point, though a player's body is half a metre across; really we are tracking one agreed point, such as where the ball was struck.

## Key takeaway

Position is a signed number $x$ that only makes sense once you have chosen an origin and a positive direction. Change either and every number changes — but the places, and the distances between them, stay exactly the same. Say your frame before you say your numbers.
