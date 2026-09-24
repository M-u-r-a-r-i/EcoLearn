---
concept_id: average_vs_instantaneous
interest: motorsport
format: explain
title: Is the speed trap flattering the car
check:
  question: |-
    A data logger records a car's position along the straight, measured from the corner exit with positive down the straight. At $t = 2.0\,\text{s}$ it is at $x = 50.0\,\text{m}$; at $t = 2.5\,\text{s}$ it is at $x = 66.0\,\text{m}$. What is its average velocity between these two readings?
  options:
    A: |-
      $32.0\,\text{m/s}$
    B: |-
      $26.4\,\text{m/s}$
    C: |-
      $25.0\,\text{m/s}$
    D: |-
      $16.0\,\text{m/s}$
  answer: A
  explanation: |-
    Average velocity uses the change in position over the change in time between the two readings: $(66.0 - 50.0)/(2.5 - 2.0) = 16.0/0.50 = 32.0\,\text{m/s}$.
  misconceptions:
    B: |-
      Divides the later position by the later time ($66.0/2.5$). That is the average velocity since the corner exit, not between the two readings.
    C: |-
      Divides the earlier position by the earlier time ($50.0/2.0$) — again an average from the corner exit, and for the wrong interval.
    D: |-
      Finds the change in position, $16.0\,\text{m}$, but never divides by the $0.50\,\text{s}$ interval, as though the readings were a second apart.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A long straight at a race circuit with a car accelerating away from the timing beam at the start line, distance boards reading 0, 100 and 200 along the verge, and an arrow marking the positive direction](scenes/motorsport/motion_straight_line.svg "One straight, one car — and two instruments that will not agree about how fast it went.")

Bhavna is convinced the speed-trap board at her local circuit is showing off for the spectators. A car sweeps out of the last corner, howls down the main straight, and the board flashes $144\,\text{km/h}$.

She has a plan to catch it out. The straight is $300\,\text{m}$ from the corner-exit board to the trap, and she has a stopwatch.

Next car through, she clicks at the corner board and clicks again at the trap: $10$ seconds, near enough.

"Three hundred metres in ten seconds," she tells her friend Imran. "Thirty metres per second. Times three point six — a hundred and eight kilometres per hour. The board says a hundred and forty-four. It's inflating them by nearly forty."

Imran bowls at the nets for his college side and has been on the wrong end of a speed gun. "Did you measure the same thing the board measures?"

Bhavna's arithmetic is perfect. So, almost certainly, is the trap's. How can one car down one straight be $108\,\text{km/h}$ and $144\,\text{km/h}$ at once?

## The physics

**Average velocity** over an interval uses nothing but the two endpoints:

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x(t_2) - x(t_1)}{t_2 - t_1}$$

It says nothing whatever about what happened in between. Bhavna averaged over ten seconds that began at the corner exit, where the car was slow, and ended at the trap, where it was fast.

The trap measures something else: how fast the car is going at (almost) a single instant, as it passes the beam. That is the **instantaneous velocity** — the average velocity over an interval so short that it has shrunk to one moment:

$$v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{dx}{dt}$$

Its size is the **instantaneous speed**. A car accelerating all the way down a straight is slowest at the start of it, so an average over the whole straight *must* come out below the speed at the far end. Both instruments are honest; they answer different questions.

On a position–time graph, an average velocity is the slope of a **secant** — the straight line joining two points of the curve. Slide the second point towards the first and the secant becomes the **tangent**, whose slope is the instantaneous velocity.

![A curve x = t squared, with dotted and dashed secant lines from t = 1 s to 3 s and 1 s to 2 s, and a solid tangent line at t = 1 s](figures/average_vs_instantaneous/secants-to-tangent.svg "Shrinking the interval drags the secant's slope towards the tangent's. The tangent slope is the velocity at that one instant.")

## Worked example

**Given:** an illustrative fit to the logger's data for this straight, with $x$ in metres from the corner-exit board and $t$ in seconds:

$$x = 20t + t^2, \qquad 0 \le t \le 10\,\text{s}$$

**Find:** the average velocities over intervals ending at the trap ($t = 10\,\text{s}$), and the instantaneous velocity there.

At the trap, $x = 20(10) + 10^2 = 300\,\text{m}$ — the length of the straight, as it should be. Now step backwards from $t = 10\,\text{s}$ by smaller and smaller amounts:

| Interval $\Delta t$ (s) | $x$ at the start of it (m) | $\bar{v} = \Delta x/\Delta t$ (m/s) |
|---|---|---|
| $1$ | $261$ | $39$ |
| $0.5$ | $280.25$ | $39.5$ |
| $0.1$ | $296.01$ | $39.9$ |
| $0.01$ | $299.6001$ | $39.99$ |

The averages are closing in on $40\,\text{m/s}$. Algebra confirms it: for any $\Delta t$,

$$\bar{v} = \frac{40\,\Delta t - \Delta t^2}{\Delta t} = 40 - \Delta t \;\to\; 40\,\text{m/s} \text{ as } \Delta t \to 0$$

So the car crosses the trap at $40\,\text{m/s} = 40 \times 3.6 = 144\,\text{km/h}$ — the board's number — while Bhavna's ten-second average is $300/10 = 30\,\text{m/s}$, or $108\,\text{km/h}$. Hers is the average, the board's is the instant.

**Sanity check:** every average in the table is below $40\,\text{m/s}$, and the longer the interval the lower it goes — exactly what you expect for a car that has been speeding up the whole way.

## Where the picture breaks

$x = 20t + t^2$ is a curve fitted to one straight, not a law: it holds from the corner exit to the trap and nowhere else, since the driver brakes hard a moment later. It also assumes a steady gain in speed, while a real car pulls hardest in the lower gears and tails off as drag builds. Speed traps do not measure over a truly zero interval either — radar and light gates work over a very short stretch, which is close enough to an instant for a results sheet. Mathematically the limit is exact; any measurement only approaches it.

## Key takeaway

Average velocity is $\Delta x/\Delta t$ between two moments — the slope of a secant on the position–time graph. Instantaneous velocity is what that becomes as $\Delta t \to 0$, $v = dx/dt$ — the slope of the tangent. A car that accelerates down the whole straight is quicker at the trap than its average over the straight, which is why the board reads $144\,\text{km/h}$ and Bhavna's stopwatch gives $108$.
