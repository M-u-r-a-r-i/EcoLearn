---
concept_id: average_vs_instantaneous
interest: smartphones
format: explain
title: How a phone knows your speed right now
check:
  question: |-
    A phone's speed app logs a bus on a straight highway, with the positive direction along the bus's motion. At $t = 40.0\,\text{s}$ the bus is at $x = 520\,\text{m}$; at $t = 42.0\,\text{s}$ it is at $x = 556\,\text{m}$. What is the bus's average velocity between these two readings?
  options:
    A: |-
      $13\,\text{m/s}$
    B: |-
      $13.2\,\text{m/s}$
    C: |-
      $18\,\text{m/s}$
    D: |-
      $36\,\text{m/s}$
  answer: C
  explanation: |-
    Average velocity between two readings is the change in position over the change in time: $(556 - 520)/(42.0 - 40.0) = 36/2.0 = 18\,\text{m/s}$.
  misconceptions:
    A: |-
      Divides the earlier position by the earlier time ($520/40.0$). That is the average since $t = 0$, not between the two readings.
    B: |-
      Divides the later position by the later time ($556/42.0$) — again an average from the start of the log, over the wrong interval.
    D: |-
      Finds the change in position, $36\,\text{m}$, but doesn't divide by the $2.0\,\text{s}$ interval — as if the interval were one second.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![An evening street: a phone shows a live-tracking map of a straight road, while a delivery scooter rides past kilometre markers](scenes/smartphones/motion_straight_line.svg "The rider's app shows a speed at this moment. But what is a speed at a moment?")

Farida is on an overnight bus to her grandparents' town, and she can't sleep. She opens a GPS speedometer app on her phone. The big number in the middle says *72 km/h*. As the bus slows for a village, it drops to 40; on the open highway it climbs back up.

Below it, a smaller line: *Trip average: 45 km/h.*

Her friend Joel, on a video call, is unimpressed. "Speed is distance divided by time. Your phone can't know your speed *right now*. 'Right now' is an instant — no time passes, and the bus goes nowhere. Zero divided by zero."

Farida frowns. The big number changes every second and matches what the bus seems to be doing. The small number is clearly a different thing.

Joel's objection sounds watertight. So what exactly is the big number — and how can a speed belong to a single moment?

## The physics

**Average velocity** over an interval uses only the two endpoints:

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x(t_2) - x(t_1)}{t_2 - t_1}$$

It says nothing about what happened in between. The trip average is exactly this, over the whole journey — stops, slow villages and all.

The big number is the **instantaneous velocity** (its size is the instantaneous speed): what the average velocity becomes as the interval shrinks towards a single moment:

$$v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{dx}{dt}$$

Joel is right that you can't divide zero by zero. But you don't have to: you take shorter and shorter intervals and watch what number the averages **settle down to**. That limiting value is the velocity at the instant.

On a position–time graph, an average velocity is the slope of a **secant** — a straight line joining two points of the curve. As the second point slides towards the first, the secant turns into the **tangent**, and its slope becomes the instantaneous velocity.

![A curve x = t squared, with dotted and dashed secant lines from t = 1 s to 3 s and 1 s to 2 s, and a solid tangent line at t = 1 s](figures/average_vs_instantaneous/secants-to-tangent.svg "Shrinking the interval from 2 s to 1 s drops the average velocity from 4 to 3 m/s. In the limit it reaches the tangent's slope, 2 m/s: the velocity at the instant t = 1 s.")

A phone does a practical version of this: it takes position fixes a short time apart — say once a second (illustrative) — and works out the velocity over each short interval. That is not truly instantaneous, but it is close enough to follow the bus.

## Worked example

**Given:** as the bus pulls away from a toll plaza, its position is modelled (illustratively) by $x = 0.75t^2$, with $x$ in metres from the plaza, $t$ in seconds, positive along the road.
**Find:** average velocities over shrinking intervals starting at $t = 8.0\,\text{s}$, and the instantaneous velocity at $t = 8.0\,\text{s}$. Here $x(8.0) = 0.75 \times 64 = 48.0\,\text{m}$.

| Interval $\Delta t$ (s) | $x(8+\Delta t)$ (m) | $\bar{v} = \Delta x/\Delta t$ (m/s) |
|---|---|---|
| $2.0$ | $0.75 \times 100 = 75.0$ | $27.0/2.0 = 13.5$ |
| $1.0$ | $0.75 \times 81 = 60.75$ | $12.75/1.0 = 12.75$ |
| $0.10$ | $0.75 \times 65.61 = 49.2075$ | $1.2075/0.10 = 12.075$ |
| $0.010$ | $0.75 \times 64.1601 = 48.120075$ | $0.120075/0.010 = 12.0075$ |

The averages close in on $12\,\text{m/s}$. Algebra confirms it: for any $\Delta t$,

$$\bar{v} = \frac{0.75(8+\Delta t)^2 - 0.75(8)^2}{\Delta t} = \frac{0.75(16\,\Delta t + \Delta t^2)}{\Delta t} = 12 + 0.75\,\Delta t \;\to\; 12\,\text{m/s}$$

So at $t = 8.0\,\text{s}$ the bus is doing $12\,\text{m/s} = 12 \times 3.6 \approx 43\,\text{km/h}$.

**Sanity check:** every average is above $12\,\text{m/s}$, and longer intervals give bigger averages — right for a bus that is speeding up, since the later part of each interval is faster.

## Where the picture breaks

The formula $x = 0.75t^2$ is an illustrative model for the first few seconds after the toll plaza, not a law — the driver changes gear and eventually stops accelerating. A phone's position fixes carry errors of a few metres, so over a very short interval the error can swamp the real movement; that is why speedometer apps don't use tiny intervals, and why their reading wobbles at walking pace. Mathematically the limit is exact. Any measurement only approaches it, and a phone trades a little "instant" for a lot less noise.

## Key takeaway

Average velocity is $\Delta x/\Delta t$ between two moments — the slope of a secant on the $x$–$t$ graph. Instantaneous velocity is its limit as $\Delta t \to 0$, $v = dx/dt$ — the slope of the tangent. The app's trip average and its big live number are these two ideas, side by side.
