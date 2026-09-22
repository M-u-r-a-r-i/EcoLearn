---
concept_id: average_vs_instantaneous
interest: cricket
format: explain
title: Is the speed gun exaggerating
check:
  question: |-
    A high-speed camera tracks a delivery along the pitch, with the origin at the release point and positive towards the batter. At $t = 0.20\,\text{s}$ the ball is at $x = 7.60\,\text{m}$; at $t = 0.30\,\text{s}$ it is at $x = 11.25\,\text{m}$. What is its average velocity between these two readings?
  options:
    A: |-
      $37.5\,\text{m/s}$
    B: |-
      $38.0\,\text{m/s}$
    C: |-
      $3.65\,\text{m/s}$
    D: |-
      $36.5\,\text{m/s}$
  answer: D
  explanation: |-
    Average velocity uses the change in position over the change in time between the two readings: $(11.25 - 7.60)/(0.30 - 0.20) = 3.65/0.10 = 36.5\,\text{m/s}$.
  misconceptions:
    A: |-
      Divides the later position by the later time ($11.25/0.30$). That is the average from the moment of release, not between the two readings.
    B: |-
      Divides the earlier position by the earlier time ($7.60/0.20$) — again an average from release, and for the wrong interval.
    C: |-
      Finds the change in position, $3.65\,\text{m}$, but doesn't divide by the $0.10\,\text{s}$ interval — as if the interval were one second.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground in sunshine with a speed display reading 140 km/h above the pitch](scenes/cricket/motion_straight_line.svg "The display gives one number per ball. But the ball doesn't have one speed.")

Yash is sure the stadium speed display is showing off. The fast bowler's delivery flashes up as $140\,\text{km/h}$, and Yash has a plan to check it.

Next ball, he films from side-on in slow motion. Frame by frame, he finds the instant the ball leaves the bowler's hand and the instant it reaches the batter — about $18\,\text{m}$ (illustrative) — in $0.50\,\text{s}$.

"Eighteen divided by half a second: thirty-six metres per second," he tells his cousin Nandini. "Times three point six... a hundred and thirty km/h. Not a hundred and forty. The display is adding ten for the crowd."

Nandini, who bowls medium pace for her school, isn't so sure. "Did you measure the same thing the display measures?"

Yash's arithmetic is correct. So is the speed gun's. How can the same ball be $130\,\text{km/h}$ and $140\,\text{km/h}$ at once?

## The physics

**Average velocity** over an interval uses only the two endpoints:

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x(t_2) - x(t_1)}{t_2 - t_1}$$

It says nothing about what happened in between. Yash measured an average over half a second — including the bounce, where the ball loses speed.

The speed gun measures something else: how fast the ball is going at (almost) one instant, just after release. That is the **instantaneous velocity** — the average velocity over an interval so short that it has shrunk to a single moment:

$$v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{dx}{dt}$$

Its size is the **instantaneous speed**. Air drag slows the ball throughout its flight and the bounce slows it further, so the release speed is the highest speed of the delivery. An average over the whole journey *must* come out lower. Both instruments are honest; they answer different questions.

On a position–time graph, an average velocity is the slope of a **secant** — the straight line joining two points of the curve. As the second point slides towards the first, the secant turns into the **tangent**, and its slope becomes the instantaneous velocity.

![A curve x = t squared, with dotted and dashed secant lines from t = 1 s to 3 s and 1 s to 2 s, and a solid tangent line at t = 1 s](figures/average_vs_instantaneous/secants-to-tangent.svg "Shrinking the interval from 2 s to 1 s drops the average velocity from 4 to 3 m/s. In the limit it reaches the tangent's slope, 2 m/s: the velocity at the instant t = 1 s.")

## Worked example

**Given:** a camera model of the delivery before it pitches (illustrative): $x = 39t - 5t^2$, with $x$ in metres from the release point, $t$ in seconds, positive towards the batter.
**Find:** average velocities from $t = 0$ over shrinking intervals, and the instantaneous velocity at release.

| Interval $\Delta t$ (s) | $x(\Delta t)$ (m) | $\bar{v} = x/\Delta t$ (m/s) |
|---|---|---|
| $0.30$ | $11.7 - 0.45 = 11.25$ | $37.5$ |
| $0.10$ | $3.9 - 0.05 = 3.85$ | $38.5$ |
| $0.010$ | $0.39 - 0.0005 = 0.3895$ | $38.95$ |
| $0.001$ | $0.039 - 0.000005 = 0.038995$ | $38.995$ |

The averages close in on $39\,\text{m/s}$. Algebra confirms it: for any $\Delta t$,

$$\bar{v} = \frac{39\,\Delta t - 5\,\Delta t^2}{\Delta t} = 39 - 5\,\Delta t \;\to\; 39\,\text{m/s} \text{ as } \Delta t \to 0$$

So the release velocity is $39\,\text{m/s} = 39 \times 3.6 \approx 140\,\text{km/h}$ — the display's number.

**Sanity check:** every average is below $39\,\text{m/s}$, and longer intervals give lower averages — exactly what you expect for a ball that is slowing down.

## Where the picture breaks

The formula $x = 39t - 5t^2$ is an illustrative model that holds only until the ball pitches; the bounce changes the motion abruptly and needs a new description. We have also tracked only the motion along the pitch, ignoring the ball's fall under gravity. Real speed guns don't measure over a truly zero interval either: they use radar or cameras over a very short stretch near release, which is close enough to "instantaneous" for practical purposes. Mathematically, the limit is exact; any measurement only approaches it.

## Key takeaway

Average velocity is $\Delta x / \Delta t$ between two moments — the slope of a secant on the $x$–$t$ graph. Instantaneous velocity is its limit as $\Delta t \to 0$, $v = dx/dt$ — the slope of the tangent. A slowing ball's release speed is higher than its average, which is why the speed gun reads $140\,\text{km/h}$ while Yash's stopwatch gives $130$.
