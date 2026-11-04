---
concept_id: relative_velocity_2d
interest: football
format: explain
title: Why a square pass to your feet ends up behind you
check:
  question: |-
    Seen from above, a striker runs east at $3.0\,\text{m/s}$ while the ball rolls south across his path at $4.0\,\text{m/s}$. What is the velocity of the ball relative to the striker?
  options:
    A: |-
      $7.0\,\text{m/s}$
    B: |-
      $5.0\,\text{m/s}$, pointing $37^\circ$ west of south
    C: |-
      $1.0\,\text{m/s}$
    D: |-
      $5.0\,\text{m/s}$, pointing $37^\circ$ east of south
  answer: B
  explanation: |-
    With $\hat{i}$ east and $\hat{j}$ north, $\vec{v}_{\text{ball, striker}} = -4.0\hat{j} - 3.0\hat{i}$. Its size is $\sqrt{3.0^2 + 4.0^2} = 5.0\,\text{m/s}$, at $\tan^{-1}(3.0/4.0) \approx 37^\circ$ west of south.
  misconceptions:
    A: |-
      Adds the two speeds as plain numbers, as if the velocities were along the same line. They are at right angles, so the directions must be included.
    C: |-
      Subtracts the speeds as plain numbers. Relative velocity subtracts vectors, not their sizes.
    D: |-
      Adds the striker's velocity instead of subtracting it. The striker moves east, so to him the ball drifts west.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A player lofts the ball in an arc over the goalkeeper while a teammate jogs round the centre circle](scenes/football/motion_plane.svg "Players and ball are all moving at once, so how a pass looks depends on who is watching it.")

Zoya is the quickest player in her college team, and she is fed up. Three times in the first half she has burst up the right wing, and three times Rizwan, the centre midfielder, has rolled a pass straight across the pitch to her. Every time, the ball has arrived behind her, and she has had to stop and turn back for it.

"I passed it right to your feet!" Rizwan protests at half-time. "Straight across. Where you were standing."

"I wasn't standing," says Zoya. "And from where I was running, your pass didn't look straight at all. It came at me on a slant, drifting backwards the whole way, and went past behind me."

Their coach, Mr D'Souza, just nods. Rizwan saw the ball roll straight across the grass. Zoya saw it come in on a slant. Which of them is right, and how do you work out the path the ball seems to take for a player who is moving?

## The physics

The velocity you measure depends on who is measuring. The **relative velocity** of A with respect to B is the velocity A seems to have to an observer moving along with B:

$$\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$$

Both $\vec{v}_A$ and $\vec{v}_B$ are measured relative to the ground. In one dimension this was ordinary subtraction. In a plane it is **vector** subtraction: add $-\vec{v}_B$ to $\vec{v}_A$ by the triangle rule, or subtract component by component. Also, $\vec{v}_{BA} = -\vec{v}_{AB}$: each sees the other moving the opposite way.

![Left: A moves straight down and observer B moves right. Right: v_A drawn down, then minus v_B drawn to the left, giving v_AB slanting down and backwards](figures/relative_velocity_2d/subtracting-velocities.svg "To find how A looks to B, add minus v_B to v_A. The result slants back against B's motion and is faster than either motion alone.")

In the story, A is the ball and B is Zoya. Seen from above, take $\hat{i}$ up the pitch, the way Zoya runs, and $\hat{j}$ across the pitch, the way the pass rolls. The ball's velocity is $v_b\,\hat{j}$ and Zoya's is $v_Z\,\hat{i}$, so

$$\vec{v}_{bZ} = v_b\,\hat{j} - v_Z\,\hat{i}$$

The $-v_Z\,\hat{i}$ part is the key. To Zoya, the ball also moves *backwards*, towards her own goal, as fast as she runs forwards. That is why, although the pass starts level with her, it seems to slant backwards and slide past behind her. Both players are right: they are describing the same ball from two different frames.

## Worked example

**Given (illustrative):** Rizwan's pass rolls straight across the pitch at $12\,\text{m/s}$; Zoya runs straight up the pitch at $5.0\,\text{m/s}$. When he plays it, she is $18\,\text{m}$ across from him. Take the ball's speed as constant.
**Find:** the ball's velocity relative to Zoya, and where it arrives compared with her.

$$\vec{v}_{bZ} = (0 - 5.0)\hat{i} + (12 - 0)\hat{j} = (-5.0\hat{i} + 12\hat{j})\,\text{m/s}$$

$$|\vec{v}_{bZ}| = \sqrt{5.0^2 + 12^2} = \sqrt{169} = 13\,\text{m/s}$$

$$\tan\phi = \frac{5.0}{12} \approx 0.42 \quad\Rightarrow\quad \phi \approx 23^\circ$$

So to Zoya the ball comes at $13\,\text{m/s}$, tilted $23^\circ$ back from the straight-across line.

The ball crosses the $18\,\text{m}$ in $18/12 = 1.5\,\text{s}$. In her frame it drifts back by $5.0 \times 1.5 = 7.5\,\text{m}$, so it arrives $7.5\,\text{m}$ behind her. To reach her feet, Rizwan must aim $7.5\,\text{m}$ ahead of where she is.

**Sanity check:** from the ground, Zoya runs $5.0 \times 1.5 = 7.5\,\text{m}$ up the pitch while the ball crosses, which gives the same gap. If she stood still ($v_Z = 0$), $\phi = 0$ and the pass would reach her feet.

## Where the picture breaks

We took the ball's speed and Zoya's speed as constant. A real pass slows on the grass, and a sprinting player speeds up, so the tilt Zoya sees changes during the pass, and the "aim $7.5\,\text{m}$ ahead" figure is only a first estimate. Players learn to judge this by feel, not by calculation. The subtraction rule itself is exact at everyday speeds.

## Key takeaway

The velocity of A relative to B is $\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$, a vector subtraction. Your own motion adds a backwards part to everything you watch. So a pass rolled straight across to a running player comes at them on a slant and passes behind them, unless it is aimed ahead.
