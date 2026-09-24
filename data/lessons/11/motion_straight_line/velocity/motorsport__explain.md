---
concept_id: velocity
interest: motorsport
format: explain
title: The logger says his average velocity was zero
check:
  question: |-
    Take the positive direction as the way the cars run down the strip. After his run, a driver returns along the return road, covering the $400\,\text{m}$ back to the start in $50\,\text{s}$. What is his average velocity on the way back?
  options:
    A: |-
      $+8\,\text{m/s}$
    B: |-
      $0\,\text{m/s}$
    C: |-
      $-8\,\text{m/s}$
    D: |-
      $-0.125\,\text{m/s}$
  answer: C
  explanation: |-
    Average velocity is displacement over time. Going back towards the start, his displacement is $-400\,\text{m}$, so $\bar{v} = -400/50 = -8\,\text{m/s}$.
  misconceptions:
    A: |-
      Gives the speed, $8\,\text{m/s}$, and forgets that velocity carries a direction. Travelling back towards the start is the negative direction here.
    B: |-
      Uses the whole out-and-back cycle, whose displacement is zero. The question asks only about the return leg, in which the position plainly changes.
    D: |-
      Divides time by displacement ($50/400$) instead of displacement by time — an inverted ratio, with units of s/m rather than m/s.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A long straight at a race circuit with a car accelerating away from the timing beam at the start line, distance boards reading 0, 100 and 200 along the verge, and an arrow marking the positive direction](scenes/motorsport/motion_straight_line.svg "A run down the strip and a long crawl back along the return road — one cycle, two very different legs.")

Sandeep has spent two years and most of his savings building the car, and today is its first proper outing: a club sprint down a $400\,\text{m}$ strip at a disused airfield. His cousin Lavanya has taped a data logger to the passenger floor.

He stages, launches, crosses the finish line, slows, turns onto the return road and crawls back to the queue.

Lavanya scrolls through the summary for the whole cycle — staging line to staging line — and reads it out flatly:

*Average speed: 8.0 m/s.*
*Average velocity: 0.0 m/s.*

Sandeep stares at the screen. "Zero? I went four hundred metres in twenty seconds. Your logger is broken."

"It also says eight metres per second," Lavanya says. "It doesn't think you were parked."

"Then speed and velocity are the same thing and it's contradicting itself."

Lavanya isn't so sure. The logger clearly treats these as two different quantities — different enough to give zero for one and not for the other.

What is velocity measuring that speed isn't?

## The physics

**Average velocity** is the displacement divided by the time taken:

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}$$

It is the **rate of change of position**. Like displacement, velocity is a **vector**: in one dimension its sign gives its direction. Its SI unit is $\text{m/s}$.

**Average speed** is the total distance divided by the time taken. It is a scalar and never negative.

The two part company whenever the path doubles back, because distance keeps adding while displacement can cancel. Put the origin at the staging line with positive pointing down the strip, and take the return road as running alongside it, so the motion stays on one line.

![A position–time graph: position falls from 0 to −18 m over 15 s, then rises back to 0 at 19 s](figures/velocity/out-slow-back-fast-xt.svg "The slope of a position–time line is the velocity. A steep line means a big speed and a falling line means a negative velocity — here, a slow outward leg and a quick return.")

The figure shows a trip taken out slowly and back quickly; Sandeep's cycle is the mirror image, fast out and slow back, but the reading rule is the same. On a position–time graph, velocity is the **slope**: rising lines mean positive velocity, falling lines negative velocity, and the steeper the line the greater the speed.

- The run: $\Delta x = +400\,\text{m}$ in $20\,\text{s}$, so $\bar{v} = +20\,\text{m/s}$, and his speed is $20\,\text{m/s}$ ($72\,\text{km/h}$ on average, having started from rest).
- The return: $\Delta x = -400\,\text{m}$ in $80\,\text{s}$, so $\bar{v} = -5\,\text{m/s}$, and his speed is $5\,\text{m/s}$.
- The whole cycle: he finishes exactly where he staged, so $\Delta x = 0$ and $\bar{v} = 0$.

The logger is right on both lines. Over the cycle the car covered $800\,\text{m}$ and got nowhere: a real speed, and zero velocity.

## Worked example

**Given:** positive down the strip. Run: $400\,\text{m}$ in $20\,\text{s}$. Return: $400\,\text{m}$ back in $80\,\text{s}$ (illustrative).
**Find:** the average speed and the average velocity for the complete cycle.

Total distance $= 400 + 400 = 800\,\text{m}$; total time $= 20 + 80 = 100\,\text{s}$:

$$\text{average speed} = \frac{800\,\text{m}}{100\,\text{s}} = 8.0\,\text{m/s}$$

Displacement $= x_f - x_i = 0 - 0 = 0$, so

$$\bar{v} = \frac{0\,\text{m}}{100\,\text{s}} = 0\,\text{m/s}$$

Those are exactly the logger's two numbers.

**Sanity check:** the average speed, $8.0\,\text{m/s}$, sits between the two leg speeds of $20$ and $5\,\text{m/s}$, and much closer to the slow one — right, because he spent four times as long crawling back as he did running. And the size of the average velocity, zero, is no larger than the average speed, as it must always be.

## Where the picture breaks

Sandeep certainly did not hold a steady $20\,\text{m/s}$ down the strip: he launched from rest and was fastest at the finish line, so $+20\,\text{m/s}$ is an average over that leg and not his velocity at any particular moment. Pinning down the latter needs **instantaneous velocity**, which is the next lesson. The straight graph segments are an idealisation for the same reason. A real return road also runs beside the strip rather than along it, and is rarely exactly the same length — we have squashed both legs onto one line to keep the motion one-dimensional.

## Key takeaway

Velocity is the rate of change of position: $\bar{v} = \Delta x / \Delta t$, a vector whose sign gives its direction in one dimension. Speed uses distance and throws the direction away. When a journey turns back on itself the two separate completely — a full run-and-return cycle has a healthy average speed and an average velocity of exactly zero.
