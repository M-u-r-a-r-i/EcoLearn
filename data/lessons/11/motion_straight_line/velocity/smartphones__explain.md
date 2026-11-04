---
concept_id: velocity
interest: smartphones
format: explain
title: The cab was doing 36 km/h, so why was it getting further away
check:
  question: |-
    A delivery app tracks a rider on a straight road, with the positive direction pointing east. In $3.0\,\text{min}$ the rider goes from $x = +1.2\,\text{km}$ to $x = +0.3\,\text{km}$. What is the rider's average velocity?
  options:
    A: |-
      $-5.0\,\text{m/s}$
    B: |-
      $+5.0\,\text{m/s}$
    C: |-
      $+1.7\,\text{m/s}$
    D: |-
      $-0.20\,\text{m/s}$
  answer: A
  explanation: |-
    Average velocity is displacement over time. $\Delta x = 0.3 - 1.2 = -0.9\,\text{km} = -900\,\text{m}$ and $\Delta t = 180\,\text{s}$, so $\bar{v} = -900/180 = -5.0\,\text{m/s}$: $5.0\,\text{m/s}$ towards the west.
  misconceptions:
    B: |-
      Gives the rider's speed and forgets that velocity carries a direction. Moving from larger $x$ to smaller $x$ means moving in the negative direction.
    C: |-
      Divides the final position by the time ($300/180$). Velocity uses the change in position, not the position itself.
    D: |-
      Divides time by displacement ($180/900$) — an inverted ratio, with units of s/m rather than m/s.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![An evening street: a phone shows a live-tracking map of a straight road, while a delivery scooter rides past kilometre markers](scenes/smartphones/motion_straight_line.svg "The map shows where the vehicle is. Whether it's coming towards you is another matter.")

It's raining, and Tara is waiting under the awning of her building for a cab to the railway station. The app shows her driver on the long, straight road outside: *500 m away.*

Her brother Aarush leans over her shoulder. "Relax. He's moving at about thirty-six kilometres an hour — ten metres every second. Fifty seconds and he's here."

Thirty seconds later the screen says *800 m away.*

"That's impossible," Aarush says. "He's still doing the same speed. How can he be further away?"

Tara watches the little car icon keep sliding smoothly along the road — away from her. The road is one-way here. The driver has to go up to the next U-turn before he can come back.

Aarush's number was perfectly true. So what did he leave out — and what is the quantity that would have warned them the cab was heading the wrong way?

## The physics

**Average velocity** is the displacement divided by the time taken:

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}$$

It is the **rate of change of position**. Like displacement, velocity is a **vector**; in one dimension its sign gives its direction. Its SI unit is $\text{m/s}$.

**Average speed** is total distance divided by the time taken. It is a scalar and never negative. Speed tells you *how fast*; velocity tells you *how fast and which way*.

Aarush quoted a speed. Tara needed a velocity. Put the origin at Tara's building, with positive pointing up the road, the way the cab was actually driving (illustrative numbers). The cab went from $x = +500\,\text{m}$ to $x = +800\,\text{m}$ in $30\,\text{s}$:

$$\bar{v} = \frac{800 - 500}{30} = +10\,\text{m/s}$$

A speed of $10\,\text{m/s}$ ($36\,\text{km/h}$), just as Aarush said — but the $+$ sign means *away from Tara*. To reach her, the cab needs a negative velocity, so that its $x$ shrinks towards zero.

![A position–time graph: position falls from 0 to −18 m over 15 s, then rises back to 0 at 19 s](figures/velocity/out-slow-back-fast-xt.svg "Velocity is the slope of the position–time line. A falling line has negative velocity, a rising line positive; steeper means faster.")

On a position–time graph, velocity is the **slope**. In the graph above, the object first moves slowly in the negative direction (a gentle downward slope) and then quickly back in the positive direction (a steep upward slope). The cab's graph would do the reverse: rise while it drives away, then fall steeply as it returns.

## Worked example

**Given:** positive up the road from Tara's building. The cab starts at $x = +500\,\text{m}$, drives to a U-turn at $x = +800\,\text{m}$ in $30\,\text{s}$, turns (take the turn as instant), and drives back to $x = 0$ at $10\,\text{m/s}$.
**Find:** the average velocity of each leg, then the average speed and average velocity for the whole trip.

Leg 1: $\bar{v}_1 = (800 - 500)/30 = +10\,\text{m/s}$.

Leg 2 takes $800/10 = 80\,\text{s}$: $\bar{v}_2 = (0 - 800)/80 = -10\,\text{m/s}$.

Same speed on both legs, opposite velocities.

Whole trip: distance $= 300 + 800 = 1100\,\text{m}$; time $= 30 + 80 = 110\,\text{s}$; displacement $= 0 - 500 = -500\,\text{m}$.

$$\text{average speed} = \frac{1100\,\text{m}}{110\,\text{s}} = 10\,\text{m/s}, \qquad \bar{v} = \frac{-500\,\text{m}}{110\,\text{s}} \approx -4.5\,\text{m/s}$$

**Sanity check:** the size of the average velocity ($4.5\,\text{m/s}$) is smaller than the average speed ($10\,\text{m/s}$), as it must be whenever the path turns back. Had the road been two-way, the cab would have come straight in: $500\,\text{m}$ at $-10\,\text{m/s}$ in $50\,\text{s}$ — Aarush's estimate, which silently assumed the direction.

## Where the picture breaks

Real cabs don't hold a steady $10\,\text{m/s}$; they slow at the U-turn and for traffic, so these are average velocities over each leg, not the velocity at any single moment — that is **instantaneous velocity**, coming next. The app's "500 m away" is usually a distance *along the route* it plans, not a straight-line gap, and its dot comes from location fixes a few metres off. Here the road is straight, so we could treat it as a number line. On a curving road, velocity's direction changes even when its size doesn't — a two-dimensional idea for later.

## Key takeaway

Velocity is the rate of change of position: $\bar{v} = \Delta x / \Delta t$, a vector whose sign shows direction. Speed uses distance and ignores direction. A cab at a steady $36\,\text{km/h}$ can have a positive or a negative velocity, and only the sign tells you whether it's coming to you.
