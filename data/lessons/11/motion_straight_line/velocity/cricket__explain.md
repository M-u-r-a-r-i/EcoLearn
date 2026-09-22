---
concept_id: velocity
interest: cricket
format: explain
title: Why the app says a fast bowler's velocity was zero
check:
  question: |-
    Take the positive direction as towards the batter. Between deliveries, a fast bowler walks $18\,\text{m}$ straight back to his mark in $12\,\text{s}$. What is his average velocity during the walk back?
  options:
    A: |-
      $+1.5\,\text{m/s}$
    B: |-
      $-1.5\,\text{m/s}$
    C: |-
      $-0.67\,\text{m/s}$
    D: |-
      $0\,\text{m/s}$
  answer: B
  explanation: |-
    Average velocity is displacement over time. Walking away from the batter, his displacement is $-18\,\text{m}$, so $v = -18/12 = -1.5\,\text{m/s}$.
  misconceptions:
    A: |-
      Gives his speed, $1.5\,\text{m/s}$, and forgets that velocity carries direction. Walking away from the batter is the negative direction.
    C: |-
      Divides time by displacement ($12/18$) instead of displacement by time — an inverted ratio, with units of s/m rather than m/s.
    D: |-
      Uses the whole walk-back-and-run-in cycle, whose displacement is zero. The question asks only about the walk back, where his position clearly changes.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground in sunshine: a batter runs between the wickets on a 22-yard pitch while a fielder chases the ball towards the boundary rope](scenes/cricket/motion_straight_line.svg "Every run-up is a round trip: back to the mark, then in to the crease.")

Pranav is the fastest bowler in his college team, and his friend Zara has clipped a tracking pod to his back for her sports-science project.

After the over, she shows him the app. For one delivery cycle — walking back to his mark, turning, and charging in to bowl — it reports two numbers:

*Average speed: 1.9 m/s.*
*Average velocity: 0.0 m/s.*

Pranav stares at the second line. "Zero? I was flying in that run-up. Your app is broken."

"It also says your speed was one point nine," Zara points out. "It can't think you were standing still."

"Then speed and velocity are the same thing, and it's contradicting itself."

Zara isn't sure. The app was made by people who know physics, and it clearly thinks these are two different quantities — different enough to give zero for one and not the other.

What does velocity measure that speed doesn't?

## The physics

**Average velocity** is the displacement divided by the time taken:

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}$$

It is the **rate of change of position**. Like displacement, velocity is a **vector**: in one dimension its sign gives its direction. Its SI unit is $\text{m/s}$.

**Average speed** is the total distance divided by the time taken. It is a scalar and never negative.

The two differ whenever the path doubles back, because distance keeps adding while displacement can cancel. Put the origin at the point where Pranav delivers the ball, with positive towards the batter. Take his mark to be $18\,\text{m}$ back (illustrative).

![A position–time graph: position falls from 0 to −18 m over 15 s, then rises back to 0 at 19 s](figures/velocity/out-slow-back-fast-xt.svg "The slope of a position–time line is the velocity: gentle and negative walking away, steep and positive running in.")

- Walking back: $\Delta x = -18\,\text{m}$ in $15\,\text{s}$, so $\bar{v} = -1.2\,\text{m/s}$. His speed is $1.2\,\text{m/s}$.
- Running in: $\Delta x = +18\,\text{m}$ in $4.0\,\text{s}$, so $\bar{v} = +4.5\,\text{m/s}$. His speed is $4.5\,\text{m/s}$.
- Whole cycle: he ends exactly where he started, so $\Delta x = 0$ and $\bar{v} = 0$.

The app is right on both lines. Over the whole cycle, he went $36\,\text{m}$ but got nowhere: a real speed, zero velocity.

On a position–time graph, velocity is the **slope** — rising lines mean positive velocity, falling lines mean negative velocity, and a steeper line means a faster speed.

## Worked example

**Given:** positive towards the batter. Walk back: $18\,\text{m}$ in $15\,\text{s}$. Run in: $18\,\text{m}$ in $4.0\,\text{s}$.
**Find:** average speed and average velocity for the whole cycle.

Total distance $= 18 + 18 = 36\,\text{m}$; total time $= 15 + 4.0 = 19\,\text{s}$.

$$\text{average speed} = \frac{36\,\text{m}}{19\,\text{s}} \approx 1.9\,\text{m/s}$$

Displacement $= x_f - x_i = 0 - 0 = 0$:

$$\bar{v} = \frac{0\,\text{m}}{19\,\text{s}} = 0\,\text{m/s}$$

Those are exactly the app's two numbers.

**Sanity check:** the average speed ($1.9\,\text{m/s}$) lies between the two leg speeds ($1.2$ and $4.5\,\text{m/s}$), closer to the slower one because he spent much longer walking. And the size of the average velocity ($0$) is no larger than the average speed, as it must always be.

## Where the picture breaks

Pranav doesn't really walk back at a steady $1.2\,\text{m/s}$ or run in at a steady $4.5\,\text{m/s}$: he starts his run-up slowly and is fastest at the crease. So these are average velocities over each leg, not his velocity at any particular moment — that needs **instantaneous velocity**, coming next. The straight-line graph segments are an idealisation for the same reason. And a real bowler follows through past the crease after releasing the ball, then walks back along a slightly different line; we've kept everything on one straight track.

## Key takeaway

Velocity is the rate of change of position: average velocity $\bar{v} = \Delta x / \Delta t$, a vector whose sign shows direction. Speed uses distance and ignores direction. When the path turns back, they differ — a complete run-up cycle has a real average speed but zero average velocity.
