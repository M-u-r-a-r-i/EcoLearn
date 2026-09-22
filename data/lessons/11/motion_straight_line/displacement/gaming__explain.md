---
concept_id: displacement
interest: gaming
format: explain
title: Fifteen metres of fighting, three and a half metres lost
check:
  question: |-
    In a 2D fighting game, take the origin at the centre of the stage and the positive direction to the right. A fighter standing at $x = +4.0\,\text{m}$ is hit by a combo and lands at $x = -2.5\,\text{m}$. What is the fighter's displacement?
  options:
    A: |-
      $+6.5\,\text{m}$
    B: |-
      $-6.5\,\text{m}$
    C: |-
      $+1.5\,\text{m}$
    D: |-
      $-2.5\,\text{m}$
  answer: B
  explanation: |-
    Displacement is final position minus initial position: $\Delta x = (-2.5) - (+4.0) = -6.5\,\text{m}$. The fighter moved $6.5\,\text{m}$ in the negative direction, to the left.
  misconceptions:
    A: |-
      Subtracts the wrong way round (initial minus final), or drops the sign because displacement "is how far it moved". The sign carries the direction and must come from final minus initial.
    C: |-
      Adds the two positions, $4.0 + (-2.5)$, instead of subtracting the initial position from the final one.
    D: |-
      Gives the final position as the displacement. Position says where the fighter is, measured from the origin; displacement says how the position changed.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a monitor shows a side-scrolling game whose runner moves along a straight track marked like a number line, with a position and velocity readout; a tablet replays a velocity-time graph](scenes/gaming/motion_straight_line.svg "On a flat 2D stage, every move is either left or right along one line.")

It's the semi-final of the college fighting-game tournament, and Farhan's round starts brilliantly. He dashes in, about six metres of stage in a blink, and lands a jab. Then his opponent answers with a combo that bounces Farhan's fighter back across the floor, nine and a half metres, until it slumps just short of the stage edge.

He survives the round. In the break, he's buzzing. "Did you see that? I was all over the stage — fifteen metres of movement in five seconds!"

Nisha, his teammate and coach for the day, doesn't look up from her notebook. "You finished behind where you started. You gave away stage. Next round starts with your back to the wall."

"I moved fifteen metres," Farhan protests.

"And lost three and a half."

Both of them are quoting true numbers. Only one of them describes what the round actually did to Farhan's position.

Which quantity captures that — and why does it need a direction, not just a size?

## The physics

**Displacement** is the change in position. In one dimension, if an object starts at position $x_i$ and ends at $x_f$:

$$\Delta x = x_f - x_i$$

It is a **vector**: it has a size and a direction. Along a line, the direction is carried by the **sign**: $+$ means the object ended up further along the positive direction, $-$ means it ended up further along the negative direction.

Three properties follow from the definition:

- It depends only on the **start and the end**, not on the path in between.
- Its size is never larger than the distance travelled — equal if the path never turns back, smaller if it does.
- A round trip gives $\Delta x = 0$, however far you went.

![Three trips on a line: from 1 m to 5 m gives Δx = +4 m; from 5 m to 2 m gives Δx = −3 m; out 3 m and back gives Δx = 0 m although the distance is 6 m](figures/displacement/sign-in-one-dimension.svg "Displacement is final minus initial. The arrow's direction gives the sign, and a round trip gives zero however far you went.")

Farhan's $15.5\,\text{m}$ is his **distance**. Nisha's number is his displacement: the dash ($+6.0\,\text{m}$) and the knockback ($-9.5\,\text{m}$) together left him $3.5\,\text{m}$ further back than he began. In a fighting game, "stage control" is a question about position and displacement, not distance — which is why Nisha cares only about that.

## Worked example

**Given:** origin at the centre of the stage, positive to the right (towards the opponent). Farhan starts at $x = -4.0\,\text{m}$, dashes to $x = +2.0\,\text{m}$, then is knocked back to $x = -7.5\,\text{m}$ (illustrative).
**Find:** his displacement for (a) the dash, (b) the knockback, (c) the whole round.

(a) $\Delta x = (+2.0) - (-4.0) = +6.0\,\text{m}$ — to the right.

(b) $\Delta x = (-7.5) - (+2.0) = -9.5\,\text{m}$ — to the left.

(c) Only the start and the end matter:

$$\Delta x = (-7.5) - (-4.0) = -3.5\,\text{m}$$

The distance for the round is $6.0 + 9.5 = 15.5\,\text{m}$.

**Sanity check:** the displacements of the two parts add up to the whole: $+6.0 + (-9.5) = -3.5\,\text{m}$. That always works for displacements, because each one is just a difference of positions. And $|{-3.5}| = 3.5\,\text{m}$ is less than the distance of $15.5\,\text{m}$, as it must be for a path that turned back.

## Where the picture breaks

Fighting-game characters also jump and get launched into the air, so their true displacement has a vertical part too; we have kept only the left–right part along the stage floor, which is what decides how close you are to the edge. The game tracks one reference point on the character (its "position" is set by the programmers, often at the feet), while arms and legs reach further. And the sign convention is a choice: had we taken positive to the left, every sign here would flip, but Farhan's fighter would have moved in exactly the same way.

## Key takeaway

Displacement is the change in position, $\Delta x = x_f - x_i$: a vector from where you started to where you finished, with its direction shown by its sign in one dimension. It ignores the path, so $15.5\,\text{m}$ of dashing and flying across a stage can add up to a displacement of just $-3.5\,\text{m}$.
