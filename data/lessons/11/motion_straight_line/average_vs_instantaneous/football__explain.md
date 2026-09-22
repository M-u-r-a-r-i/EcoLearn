---
concept_id: average_vs_instantaneous
interest: football
format: explain
title: Did the shot-speed radar add ten km/h
check:
  question: |-
    A camera tracks a penalty, with the origin at the penalty mark and positive towards the goal. At $t = 0.10\,\text{s}$ the ball is at $x = 2.44\,\text{m}$; at $t = 0.30\,\text{s}$ it is at $x = 6.96\,\text{m}$. What is its average velocity between these two readings?
  options:
    A: |-
      $23.2\,\text{m/s}$
    B: |-
      $22.6\,\text{m/s}$
    C: |-
      $4.52\,\text{m/s}$
    D: |-
      $24.4\,\text{m/s}$
  answer: B
  explanation: |-
    Average velocity uses the change in position over the change in time between the two readings: $(6.96 - 2.44)/(0.30 - 0.10) = 4.52/0.20 = 22.6\,\text{m/s}$.
  misconceptions:
    A: |-
      Divides the later position by the later time ($6.96/0.30$). That is the average since the kick, not between the two readings.
    C: |-
      Finds the change in position, $4.52\,\text{m}$, but doesn't divide by the $0.20\,\text{s}$ interval — as if the interval were one second.
    D: |-
      Divides the earlier position by the earlier time ($2.44/0.10$) — again an average from the kick, and for the wrong interval.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A winger dribbles along the touchline towards goal, chased by a defender, while the goalkeeper comes off the line; a number line with origin O and +x runs beneath](scenes/football/motion_straight_line.svg "A tracking board shows one number. A moving ball doesn't keep one speed for long.")

At the city football fan fest, there's a "shot speed" booth: take a penalty at an empty goal, and a radar flashes your speed on a screen. Zoya, her school team's striker, drills one low into the corner. The screen reads $90\,\text{km/h}$.

Her cousin Ritwik is suspicious. "They pump the numbers so people pay for another go." He filmed the kick in slow motion, and frame by frame he finds that the ball took $0.50\,\text{s}$ to travel the $11\,\text{m}$ from the penalty mark to the goal line.

"Eleven metres in half a second is twenty-two metres per second," he says. "Times three point six — seventy-nine km/h. Not ninety. Told you."

Zoya shrugs. "Your phone and their radar can't both be right."

Ritwik's arithmetic is correct. The radar's physics is sound. How can the same shot honestly be $79\,\text{km/h}$ and $90\,\text{km/h}$ at once?

## The physics

**Average velocity** over an interval uses only the two endpoints:

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x(t_2) - x(t_1)}{t_2 - t_1}$$

It says nothing about what happened in between. Ritwik measured an average over half a second, during which air drag was steadily slowing the ball.

The radar measures something else: how fast the ball is going at (almost) one instant, just after the kick. That is the **instantaneous velocity** — the average velocity over an interval so short that it shrinks to a single moment:

$$v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{dx}{dt}$$

Its size is the **instantaneous speed**. The ball is fastest the moment it leaves the boot and slows all the way to the goal, so an average over the whole journey *must* come out lower. Both measurements are honest; they answer different questions.

On a position–time graph, an average velocity is the slope of a **secant** — the straight line joining two points on the curve. As the second point slides towards the first, the secant turns into the **tangent**, and its slope becomes the instantaneous velocity.

![A curve x = t squared, with dotted and dashed secant lines from t = 1 s to 3 s and 1 s to 2 s, and a solid tangent line at t = 1 s](figures/average_vs_instantaneous/secants-to-tangent.svg "Shrinking the interval from 2 s to 1 s drops the average velocity from 4 to 3 m/s. In the limit it reaches the tangent's slope, 2 m/s: the velocity at the instant t = 1 s.")

## Worked example

**Given:** a camera model of Zoya's shot (illustrative): $x = 25t - 6t^2$, with $x$ in metres from the penalty mark, $t$ in seconds after the kick, positive towards the goal. Check: $x(0.50) = 12.5 - 1.5 = 11.0\,\text{m}$, the goal line.
**Find:** average velocities from $t = 0$ over shrinking intervals, and the instantaneous velocity at the kick.

| Interval $\Delta t$ (s) | $x(\Delta t)$ (m) | $\bar{v} = x/\Delta t$ (m/s) |
|---|---|---|
| $0.50$ | $12.5 - 1.5 = 11.0$ | $22.0$ |
| $0.10$ | $2.5 - 0.06 = 2.44$ | $24.4$ |
| $0.010$ | $0.25 - 0.0006 = 0.2494$ | $24.94$ |
| $0.001$ | $0.025 - 0.000006 = 0.024994$ | $24.994$ |

The averages close in on $25\,\text{m/s}$. Algebra confirms it: for any $\Delta t$,

$$\bar{v} = \frac{25\,\Delta t - 6\,\Delta t^2}{\Delta t} = 25 - 6\,\Delta t \;\to\; 25\,\text{m/s} \text{ as } \Delta t \to 0$$

So the velocity at the kick is $25\,\text{m/s} = 25 \times 3.6 = 90\,\text{km/h}$ — the radar's number. Ritwik's $22.0\,\text{m/s}$ is the first row of the table.

**Sanity check:** every average is below $25\,\text{m/s}$, and longer intervals give lower averages — exactly what you expect for a ball that is slowing down.

## Where the picture breaks

The formula $x = 25t - 6t^2$ is an illustrative fit that holds only from the kick until the ball reaches the goal; it assumes a constant slowing, while real drag weakens as the ball slows. We have also kept only the motion along the line from spot to goal, ignoring any rise or sideways travel. And a real radar doesn't measure over a truly zero interval: it samples over a very short stretch near the kick, close enough to "instantaneous" for practical purposes. The limit is exact; any measurement only approaches it.

## Key takeaway

Average velocity is $\Delta x / \Delta t$ between two moments — the slope of a secant on the $x$–$t$ graph. Instantaneous velocity is its limit as $\Delta t \to 0$, $v = dx/dt$ — the slope of the tangent. A slowing ball's speed off the boot is higher than its average, which is why the radar says $90\,\text{km/h}$ while Ritwik's video gives $79$.
