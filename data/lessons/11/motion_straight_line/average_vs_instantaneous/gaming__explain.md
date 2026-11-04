---
concept_id: average_vs_instantaneous
interest: gaming
format: explain
title: Is the racing game's speedometer lying
check:
  question: |-
    A racing game's replay tool logs a car on a straight, with positions measured from the start of the straight. At $t = 3.00\,\text{s}$ the car is at $x = 120.0\,\text{m}$; at $t = 3.50\,\text{s}$ it is at $x = 146.0\,\text{m}$. What is its average velocity between these two readings?
  options:
    A: |-
      $41.7\,\text{m/s}$
    B: |-
      $52.0\,\text{m/s}$
    C: |-
      $26.0\,\text{m/s}$
    D: |-
      $40.0\,\text{m/s}$
  answer: B
  explanation: |-
    Average velocity between two readings is the change in position over the change in time: $(146.0 - 120.0)/(3.50 - 3.00) = 26.0/0.50 = 52.0\,\text{m/s}$.
  misconceptions:
    A: |-
      Divides the later position by the later time ($146.0/3.50$). That is the average since the start of the straight, not between the two readings.
    C: |-
      Finds the change in position, $26.0\,\text{m}$, but doesn't divide by the $0.50\,\text{s}$ interval — as if the interval were one second.
    D: |-
      Divides the earlier position by the earlier time ($120.0/3.00$) — an average from the start of the straight, and over the wrong interval.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a monitor shows a side-scrolling game whose runner moves along a straight track marked like a number line, with a position and velocity readout; a tablet replays a velocity-time graph](scenes/gaming/motion_straight_line.svg "The HUD shows one number at every moment. A lap timer can only tell you what happened between two moments.")

Rohit is convinced his racing game cheats to make you feel fast. On the final straight of his favourite track, his car crosses the finish line with the speedometer reading $198\,\text{km/h}$.

He has a plan to catch it out. The game shows split times, and the final sector is the last $100\,\text{m}$ of the straight. His car covers it in exactly $2.00\,\text{s}$.

"A hundred metres in two seconds is fifty metres per second," he tells his sister Pooja. "Times three point six: one hundred and eighty km/h. Not one ninety-eight. The HUD is adding eighteen to hype you up."

Pooja, who has spent more hours in the game than he has, isn't convinced. "Is your number the same kind of number as the speedometer's?"

Rohit's arithmetic is correct. So, it turns out, is the speedometer. How can one car be doing $180\,\text{km/h}$ and $198\,\text{km/h}$ over the same stretch?

## The physics

**Average velocity** over an interval uses only the two endpoints:

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x(t_2) - x(t_1)}{t_2 - t_1}$$

It says nothing about what happened in between. Rohit measured an average over two whole seconds — and his car was still accelerating down the straight, so it was slower at the start of the sector than at the end.

The speedometer shows something else: how fast the car is going at one instant. That is the **instantaneous velocity** — the average velocity over an interval so short that it shrinks to a single moment:

$$v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{dx}{dt}$$

Its size is the **instantaneous speed**. For a car that is speeding up, the speed at the finish line *must* be higher than the average over the sector before it. Both numbers are honest; they answer different questions.

On a position–time graph, an average velocity is the slope of a **secant** — a straight line joining two points of the curve. As the two points slide together, the secant turns into the **tangent**, and its slope becomes the instantaneous velocity.

![A curve x = t squared, with dotted and dashed secant lines from t = 1 s to 3 s and 1 s to 2 s, and a solid tangent line at t = 1 s](figures/average_vs_instantaneous/secants-to-tangent.svg "Shrinking the interval from 2 s to 1 s drops the average velocity from 4 to 3 m/s. In the limit it reaches the tangent's slope, 2 m/s: the velocity at the instant t = 1 s.")

## Worked example

**Given:** a model of the car in the final sector (illustrative): $x = 45t + 2.5t^2$, with $x$ in metres from the start of the sector, $t$ in seconds, for $0 \le t \le 2.00\,\text{s}$. So $x(2.00) = 90 + 10 = 100\,\text{m}$ — the finish line.
**Find:** average velocities over shorter and shorter intervals *ending* at the finish, and the instantaneous velocity there.

| Interval | $x$ at start (m) | $\Delta x$ (m) | $\bar{v}$ (m/s) |
|---|---|---|---|
| $0$ to $2.00\,\text{s}$ | $0$ | $100$ | $50.0$ |
| $1.00$ to $2.00\,\text{s}$ | $45 + 2.5 = 47.5$ | $52.5$ | $52.5$ |
| $1.90$ to $2.00\,\text{s}$ | $85.5 + 9.025 = 94.525$ | $5.475$ | $54.75$ |
| $1.99$ to $2.00\,\text{s}$ | $89.55 + 9.90025 = 99.45025$ | $0.54975$ | $54.975$ |

The averages close in on $55\,\text{m/s}$. Algebra confirms it: over the last $\Delta t$ before the line, $\bar{v} = 55 - 2.5\,\Delta t$, which tends to $55\,\text{m/s}$ as $\Delta t \to 0$.

So the speed at the line is $55 \times 3.6 = 198\,\text{km/h}$ — the speedometer's number — while the sector average is $50 \times 3.6 = 180\,\text{km/h}$, Rohit's number.

**Sanity check:** every average is below $55\,\text{m/s}$, and shorter intervals near the line give higher averages — just what you expect for a car that is still speeding up. A game engine typically moves the car in steps of $\tfrac{1}{60}\,\text{s}$; an average over one such step, $55 - 2.5/60 \approx 54.96\,\text{m/s}$, is already within $0.1\%$ of the limit.

## Where the picture breaks

The formula is an illustrative model valid only inside the sector; a real car's speed doesn't follow a neat curve forever. A game also doesn't really have "instants": its engine updates in small, finite time steps, so what a speedometer shows is at best a value for one step. That's the everyday meaning of "instantaneous" — an interval too short to matter. Mathematically, the limit $\Delta t \to 0$ is exact; any measurement, in a game or in the real world, only approaches it. Some games also smooth or round the displayed speed.

## Key takeaway

Average velocity is $\Delta x / \Delta t$ between two moments — the slope of a secant on the $x$–$t$ graph. Instantaneous velocity is its limit as $\Delta t \to 0$, $v = dx/dt$ — the slope of the tangent. A car still accelerating crosses the line faster than its sector average, which is why the HUD says $198\,\text{km/h}$ while the split time says $180$.
