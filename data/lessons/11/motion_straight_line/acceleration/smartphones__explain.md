---
concept_id: acceleration
interest: smartphones
format: explain
title: The RC car that sped up with a negative acceleration
check:
  question: |-
    An app-controlled toy car starts from rest and reverses along a straight corridor. Its velocity–time graph is a straight line from $0$ to $-4.0\,\text{m/s}$ over $2.0\,\text{s}$ (positive is forwards). What is its acceleration, and what is happening to its speed?
  options:
    A: |-
      $+2.0\,\text{m/s}^2$, because the car speeds up
    B: |-
      $-2.0\,\text{m/s}^2$, and the car speeds up
    C: |-
      $-2.0\,\text{m/s}^2$, so the car slows down
    D: |-
      $-8.0\,\text{m/s}^2$, and the car speeds up
  answer: B
  explanation: |-
    The slope of the $v$–$t$ graph is $a = \Delta v/\Delta t = (-4.0 - 0)/2.0 = -2.0\,\text{m/s}^2$. Velocity and acceleration are both negative — the same sign — so the car's speed increases.
  misconceptions:
    A: |-
      Believes that speeding up always means a positive acceleration. The sign of $a$ comes from the slope of the graph; here $v$ goes from $0$ to $-4.0\,\text{m/s}$, so the slope is negative.
    C: |-
      Gets the right acceleration but reads "negative acceleration" as "slowing down". The speed falls only when $v$ and $a$ have opposite signs.
    D: |-
      Multiplies the change in velocity by the time ($4.0 \times 2.0$) instead of dividing — mixing up the slope of the graph with the area under it.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![An evening street: a phone shows a live-tracking map of a straight road, while a delivery scooter rides past kilometre markers](scenes/smartphones/motion_straight_line.svg "Speeding up, cruising, braking: every vehicle's motion can be logged by a phone.")

Rehan's birthday present is a fast remote-control car that you drive from a phone app. Best of all, the app logs the car's velocity and draws a graph after every run.

On Sunday morning the school basketball court is empty, so Rehan and his sister Aisha set up a straight track along one line. Rehan floors it: the car shoots forward, holds top speed for a moment, brakes hard just before the wall, then reverses and backs away steadily.

The graph appears on the phone. Aisha zooms into the reversing part.

"Look — *negative* acceleration. The car was slowing down there."

"It wasn't!" Rehan says. "It was speeding up backwards. I had my thumb on full reverse."

"Negative acceleration means slowing down," Aisha insists. "Everyone knows that. Your app's broken."

The same app correctly showed the braking as negative too. Can a car really speed up with a negative acceleration — and when, during that run, was it accelerating at all?

## The physics

**Acceleration** is the rate of change of velocity. Over an interval,

$$\bar{a} = \frac{\Delta v}{\Delta t} = \frac{v_f - v_i}{t_f - t_i}$$

and at an instant, $a = dv/dt$. Its SI unit is $\text{m/s}^2$ — metres per second, per second. Acceleration is a **vector**; in one dimension its sign gives its direction.

Two consequences matter most:

- **Constant velocity means zero acceleration**, however fast the car is going. Top speed on a straight line is not acceleration.
- **The sign of $a$ alone doesn't tell you whether the speed grows.** If $v$ and $a$ have the *same* sign, the speed increases. If they have *opposite* signs, the speed decreases.

On a velocity–time graph, the acceleration is the **slope**: a rising line means positive $a$, a flat line means $a = 0$, a falling line means negative $a$. The steeper the line, the larger the magnitude of the acceleration.

![A velocity–time graph in five phases: up from 0 to 8 m/s, flat at 8 m/s, down to 0, down further to −3 m/s, then flat at −3 m/s](figures/acceleration/vt-slope-sign.svg "Read acceleration as slope. From 4.5 s to 5.5 s the slope is negative and so is the velocity — so the speed grows.")

Take this graph as Rehan's run (illustrative numbers), with positive meaning forwards, towards the wall.

## Worked example

**Given:** the $v$–$t$ graph above.
**Find:** the car's acceleration in each phase, and whether its speed is rising or falling.

| Phase | $\Delta v$ (m/s) | $\Delta t$ (s) | $a$ (m/s²) | Speed |
|---|---|---|---|---|
| $0$–$2.0\,\text{s}$, full throttle | $8 - 0 = +8$ | $2.0$ | $+4.0$ | rising |
| $2.0$–$3.5\,\text{s}$, top speed | $0$ | $1.5$ | $0$ | steady |
| $3.5$–$4.5\,\text{s}$, braking | $0 - 8 = -8$ | $1.0$ | $-8.0$ | falling |
| $4.5$–$5.5\,\text{s}$, full reverse | $-3 - 0 = -3$ | $1.0$ | $-3.0$ | rising |
| $5.5$–$6.5\,\text{s}$, steady reverse | $0$ | $1.0$ | $0$ | steady |

While braking, $v > 0$ and $a < 0$: opposite signs, so the car slows. While reversing, $v < 0$ and $a < 0$: the same sign, so it speeds up — to $3\,\text{m/s}$ in the negative direction. Rehan is right, and the app is right. Aisha's rule "negative means slowing down" works only when the velocity is positive.

**Sanity check:** each $a$ has units $(\text{m/s})/\text{s} = \text{m/s}^2$. And $8\,\text{m/s}$ is about $29\,\text{km/h}$ — fast for a toy, but hobby RC cars do reach speeds like this.

## Where the picture breaks

A real car doesn't produce perfectly straight segments: its motor pushes hardest at low speed, and the corners of the graph are smooth bends, so each straight segment gives the *average* acceleration of that phase. The app's velocity also comes from the car's own sensors, sampled several times a second and smoothed, so short jolts don't show. There is a phone twist, too: the phone's own motion sensor (accelerometer) also feels gravity, so its raw reading is not simply the $a$ of this lesson. And if Rehan had steered in a curve, a change of direction alone would count as acceleration — that belongs to *Motion in a Plane*.

## Key takeaway

Acceleration is the rate of change of velocity, $a = \Delta v/\Delta t$, read as the slope of a velocity–time graph. Zero slope means zero acceleration, even at top speed. A negative acceleration slows you down only if you are moving in the positive direction; when $v$ and $a$ share a sign, the speed grows.
