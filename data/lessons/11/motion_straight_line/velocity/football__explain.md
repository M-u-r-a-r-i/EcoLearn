---
concept_id: velocity
interest: football
format: explain
title: Why the tracker gave the centre-back a velocity of zero
check:
  question: |-
    Take the positive direction as towards the opponents' goal. A striker jogs $15\,\text{m}$ straight back towards her own goal in $10\,\text{s}$ to help defend a corner. What is her average velocity during the jog?
  options:
    A: |-
      $+1.5\,\text{m/s}$
    B: |-
      $0\,\text{m/s}$
    C: |-
      $-0.67\,\text{m/s}$
    D: |-
      $-1.5\,\text{m/s}$
  answer: D
  explanation: |-
    Average velocity is displacement over time. Jogging back towards her own goal, her displacement is $-15\,\text{m}$, so $\bar{v} = -15/10 = -1.5\,\text{m/s}$.
  misconceptions:
    A: |-
      Gives her speed, $1.5\,\text{m/s}$, and forgets that velocity carries direction. Running towards her own goal is the negative direction.
    B: |-
      Thinks that because she will run back up the pitch after the corner, her velocity cancels to zero. The question asks only about the jog back, where her position clearly changes.
    C: |-
      Divides time by displacement ($10/15$) instead of displacement by time — an inverted ratio, with units of s/m rather than m/s.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A winger dribbles along the touchline towards goal, chased by a defender, while the goalkeeper comes off the line; a number line with origin O and +x runs beneath](scenes/football/motion_straight_line.svg "Every player on this pitch moves back and forth along its length, again and again.")

Siddharth is his college team's centre-back, and his friend Meher has strapped a GPS pod between his shoulder blades for her sports-science project.

After the match she shows him one short spell. The opposition had the ball; Siddharth dropped back steadily towards his own goal, then the ball was cleared and he burst forward to push the line up again, ending exactly where he'd started. The app reports:

*Average speed: 1.9 m/s.*
*Average velocity: 0.0 m/s.*

Siddharth laughs. "Zero? I sprinted up that pitch. Your app thinks I was asleep."

"It also says one point nine for speed," Meher says. "So it knows you moved."

"Then speed and velocity are the same thing, and it's contradicting itself."

Meher isn't sure. Whoever wrote the app clearly thinks these are two different quantities — different enough to give zero for one and not the other.

What does velocity measure that speed doesn't?

## The physics

**Average velocity** is the displacement divided by the time taken:

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}$$

It is the **rate of change of position** (of displacement). Like displacement, velocity is a **vector**: in one dimension its sign gives its direction. Its SI unit is $\text{m/s}$.

**Average speed** is the total distance divided by the time taken. It is a scalar and never negative.

The two differ whenever the path doubles back, because distance keeps adding while displacement can cancel. Put the origin where Siddharth started, with positive towards the opponents' goal. Say he dropped $18\,\text{m}$ in $15\,\text{s}$, then pushed up $18\,\text{m}$ in $4.0\,\text{s}$ (illustrative).

![A position–time graph: position falls from 0 to −18 m over 15 s, then rises back to 0 at 19 s](figures/velocity/out-slow-back-fast-xt.svg "The slope of a position–time line is the velocity: gentle and negative dropping back, steep and positive pushing up.")

- Dropping back: $\Delta x = -18\,\text{m}$ in $15\,\text{s}$, so $\bar{v} = -1.2\,\text{m/s}$. His speed is $1.2\,\text{m/s}$.
- Pushing up: $\Delta x = +18\,\text{m}$ in $4.0\,\text{s}$, so $\bar{v} = +4.5\,\text{m/s}$. His speed is $4.5\,\text{m/s}$.
- Whole spell: $36\,\text{m}$ in $19\,\text{s}$ gives an average speed of $36/19 \approx 1.9\,\text{m/s}$; but he ends where he started, so $\Delta x = 0$ and $\bar{v} = 0$.

The app is right on both lines. On a position–time graph, velocity is the **slope**: a rising line means positive velocity, a falling line negative velocity, and a steeper line a faster speed.

## Worked example

**Given:** positive towards the opponents' goal. A winger sprints $40\,\text{m}$ up the touchline in $8.0\,\text{s}$, then jogs $10\,\text{m}$ back in $5.0\,\text{s}$ to receive a short pass (illustrative).
**Find:** her average speed and average velocity over the $13\,\text{s}$.

Total distance $= 40 + 10 = 50\,\text{m}$:

$$\text{average speed} = \frac{50\,\text{m}}{13\,\text{s}} \approx 3.8\,\text{m/s}$$

Displacement $= +40 + (-10) = +30\,\text{m}$:

$$\bar{v} = \frac{+30\,\text{m}}{13\,\text{s}} \approx +2.3\,\text{m/s}$$

Here the velocity is not zero, but it is still smaller in size than the speed, and it points up the pitch.

**Sanity check:** the size of an average velocity can never exceed the average speed, because $|\Delta x|$ can never exceed the distance; $2.3 < 3.8$. They would be equal only if she had never turned back.

## Where the picture breaks

Real players don't drop back at a steady $1.2\,\text{m/s}$ or push up at a steady $4.5\,\text{m/s}$: they speed up and slow down within each phase. So these are *average* velocities over each phase, not the velocity at any particular moment — that needs **instantaneous velocity**, coming next. The straight segments on the graph are an idealisation for the same reason. And Siddharth also moved sideways across the pitch; we kept only the component along its length.

## Key takeaway

Velocity is the rate of change of position: average velocity $\bar{v} = \Delta x / \Delta t$, a vector whose sign shows direction. Speed uses distance and ignores direction. When the path turns back they differ — a centre-back who drops and pushes up to the same spot has a real average speed but zero average velocity.
