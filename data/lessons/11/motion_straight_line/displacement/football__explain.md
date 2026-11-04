---
concept_id: displacement
interest: football
format: explain
title: Twenty-five metres of running, three metres of line
check:
  question: |-
    Take the origin on your own goal line and the positive direction up the pitch. In open play your goalkeeper stands at $x = +6.0\,\text{m}$. For an opposition corner he moves back to $x = +0.5\,\text{m}$. What is his displacement?
  options:
    A: |-
      $+5.5\,\text{m}$
    B: |-
      $+0.5\,\text{m}$
    C: |-
      $-5.5\,\text{m}$
    D: |-
      $+6.5\,\text{m}$
  answer: C
  explanation: |-
    Displacement is final position minus initial position: $\Delta x = 0.5 - 6.0 = -5.5\,\text{m}$. He moved $5.5\,\text{m}$ in the negative direction, back towards his goal line.
  misconceptions:
    A: |-
      Subtracts the wrong way round (initial minus final), or drops the sign because "displacement is how far he moved". The sign carries the direction and must come from final minus initial.
    B: |-
      Gives his final position as the displacement. Position says where he is measured from the origin; displacement says how his position changed.
    D: |-
      Adds the two positions instead of subtracting them, treating displacement like a total of the numbers on the scale.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A winger dribbles along the touchline towards goal, chased by a defender, while the goalkeeper comes off the line; a number line with origin O and +x runs beneath](scenes/football/motion_straight_line.svg "Along the length of the pitch, every movement is either towards one goal or towards the other.")

Irfan is the last defender, and he loves the offside trap. As the other team builds an attack, he pushes his back line up the pitch — fourteen metres, shouting at everyone to hold the line. Then their midfielder looks up to play the ball through, and Irfan panics and drops eleven metres back.

The pass is played. The striker, who would have been yards offside if Irfan had held his ground, is onside by a stride, runs through, and scores.

In the video session, Coach Bhatia freezes the clip at the instant of the pass. "Irfan, how far had you moved the line from where you started?"

"I ran twenty-five metres in that move, sir! Up and back!"

"That's not what I asked," says the coach.

Irfan did run twenty-five metres. But the linesman's flag didn't care about that at all. It cared about where Irfan was when the ball left the passer's foot, compared with where he had been.

Which quantity captures that — and why does it need a direction, not just a size?

## The physics

**Displacement** is the change in position. In one dimension, if an object starts at position $x_i$ and ends at $x_f$:

$$\Delta x = x_f - x_i$$

It is a **vector**: it has a size and a direction. Along a line, the direction is carried by the **sign**: $+$ means the object ended up further along the positive direction, $-$ means further along the negative direction.

Three properties follow from the definition:

- It depends only on the **start and the end**, not on the path in between.
- Its size is never larger than the distance travelled — equal if the path never turns back, smaller if it does.
- A round trip gives $\Delta x = 0$, however far you ran.

![Three trips on a line: from 1 m to 5 m gives Δx = +4 m; from 5 m to 2 m gives Δx = −3 m; out 3 m and back gives Δx = 0 m although the distance is 6 m](figures/displacement/sign-in-one-dimension.svg "Displacement is final minus initial. The arrow's direction gives the sign; a round trip gives zero whatever the distance.")

For Irfan, the coach's question is about displacement, and the linesman's flag is about position at one instant. Distance — the twenty-five metres — answers neither.

## Worked example

**Given:** origin on Irfan's own goal line, positive up the pitch. His line starts at $x = +18\,\text{m}$, pushes up to $x = +32\,\text{m}$, then drops back to $x = +21\,\text{m}$ as the pass is played (illustrative).
**Find:** his displacement for each move and for the whole thing, and the distance he ran.

Push up: $x_i = 18\,\text{m}$, $x_f = 32\,\text{m}$:

$$\Delta x_1 = 32 - 18 = +14\,\text{m}$$

Drop back: $x_i = 32\,\text{m}$, $x_f = 21\,\text{m}$:

$$\Delta x_2 = 21 - 32 = -11\,\text{m}$$

Whole move: $\Delta x = 21 - 18 = +3\,\text{m}$. The distance is $14 + 11 = 25\,\text{m}$.

So at the moment of the pass, the line was only $3\,\text{m}$ further up the pitch than where it began, not the $14\,\text{m}$ the trap needed. A striker standing at, say, $x = +22\,\text{m}$ would have been offside against a line at $+32\,\text{m}$, but was a metre onside against a line at $+21\,\text{m}$.

**Sanity check:** adding the two parts, $+14 + (-11) = +3\,\text{m}$, agrees with final minus initial for the whole move. And $3\,\text{m}$ is smaller than the $25\,\text{m}$ distance, as it must be when the path doubles back.

## Where the picture breaks

We have squashed everything onto the length of the pitch. Irfan also moved sideways, so his full displacement is a vector in two dimensions; only its component along the pitch mattered for offside. The real offside law is also more detailed than "level with the last defender" — it compares the attacker with the second-last opponent (usually the last outfield defender, because the goalkeeper is behind them), and uses the positions of body parts at the instant the ball is played. And the sign convention is a choice: take positive towards Irfan's own goal, and every sign here flips, while the movement stays the same.

## Key takeaway

Displacement is the change in position, $\Delta x = x_f - x_i$: a vector from where you started to where you finished, with its direction shown by the sign in one dimension. It ignores the path, so twenty-five metres of running can leave the defensive line just three metres from where it began.
