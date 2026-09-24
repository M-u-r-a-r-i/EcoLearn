---
concept_id: calculus_for_motion
interest: motorsport
format: explain
title: One line of algebra holds the whole run
check:
  question: |-
    A logger fits a car's position during a braking test as $x = 30t - 3t^2$, with $x$ in metres and $t$ in seconds. What is its acceleration at $t = 2.0\,\text{s}$?
  options:
    A: |-
      $+18\,\text{m/s}^2$
    B: |-
      $-3.0\,\text{m/s}^2$
    C: |-
      $-6.0\,\text{m/s}^2$
    D: |-
      $-12\,\text{m/s}^2$
  answer: C
  explanation: |-
    Differentiate twice: $v = dx/dt = 30 - 6t$, then $a = dv/dt = -6.0\,\text{m/s}^2$, the same at every instant including $t = 2.0\,\text{s}$.
  misconceptions:
    A: |-
      Differentiates once and stops, reporting $v = 30 - 6(2.0) = 18$ as the acceleration. That is the velocity, in m/s.
    B: |-
      Reads the coefficient of $t^2$ straight off as the acceleration, forgetting the $\tfrac{1}{2}$ in $s = ut + \tfrac{1}{2}at^2$. The acceleration is twice that coefficient.
    D: |-
      Differentiates $-3t^2$ to $-6t$ and then substitutes $t = 2.0$, instead of differentiating $-6t$ a second time. The second derivative is $-6$, with no $t$ left in it.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A long straight at a race circuit with a car accelerating away from the timing beam at the start line, distance boards reading 0, 100 and 200 along the verge, and an arrow marking the positive direction](scenes/motorsport/motion_straight_line.svg "Everything that happens on this straight can be written as position against time.")

Nithya runs the simulation side of her college racing team, which mostly means she is the one people argue with. Today the argument is about gearing.

The team has fitted a shorter final drive for the acceleration event, and the driver, Gaurav, is certain the car "runs out of pull" before the end of the $100\,\text{m}$ run. Nithya's model of the launch fits the whole run into a single line:

$x = 5t^2 - 0.2t^3$ (metres, seconds), for the five seconds from the start line.

Gaurav is unimpressed. "That tells you where the car is. I'm telling you what it *feels* like at the end — like it's given up. There isn't a speed anywhere in that."

"Isn't there?" says Nithya, and uncaps a pen.

How do you get a speed — and, more to the point, whether the car is still pulling — out of a formula that only says where it is?

## The physics

Velocity is the rate of change of position, and acceleration is the rate of change of velocity. In calculus those rates are **derivatives**:

$$v = \frac{dx}{dt}, \qquad a = \frac{dv}{dt} = \frac{d^2x}{dt^2}$$

For polynomials you need one rule, $\dfrac{d}{dt}(t^n) = n\,t^{n-1}$, with any constant factor coming along unchanged. So $\dfrac{d}{dt}(5t^2) = 10t$ and $\dfrac{d}{dt}(0.2t^3) = 0.6t^2$.

Going the other way — from velocity back to displacement — is **integration**. The displacement between two times is the area under the $v$–$t$ graph:

$$\Delta x = x(t_2) - x(t_1) = \int_{t_1}^{t_2} v\,dt$$

using $\displaystyle\int t^n\,dt = \frac{t^{n+1}}{n+1}$. Integrating acceleration in the same way gives the change in velocity. Differentiation and integration undo one another, so you can move freely between $x$, $v$ and $a$ without measuring anything new.

![Two graphs. Left: a position curve rising to a value at 5 s, with a dashed tangent line drawn at that point. Right: the corresponding velocity curve, with the area under it from 0 to 5 s marked](figures/calculus_for_motion/x-and-v-from-formula.svg "The slope of the left curve at any time is the height of the right curve; the area under the right curve is the rise of the left one. The formula plotted here is a different illustrative fit from the one in the worked example.")

## Worked example

**Given:** $x = 5t^2 - 0.2t^3$ (m, s), an illustrative fit valid for $0 \le t \le 5\,\text{s}$, with positive down the straight.
**Find:** the velocity and acceleration at the end of the run ($t = 5\,\text{s}$), and the length of the run from integration.

**Differentiate once for velocity, twice for acceleration:**

$$v = \frac{dx}{dt} = 10t - 0.6t^2, \qquad a = \frac{dv}{dt} = 10 - 1.2t$$

At $t = 5\,\text{s}$:

$$v = 10(5) - 0.6(25) = 50 - 15 = 35\,\text{m/s} = 35 \times 3.6 = 126\,\text{km/h}$$

$$a = 10 - 1.2(5) = 10 - 6 = +4\,\text{m/s}^2$$

The acceleration is still positive at the finish, so the car is still gaining speed — Gaurav's "given up" is really "no longer pulling as hard as it did at the start", where $a$ was $10\,\text{m/s}^2$.

**Integrate the velocity to get the length of the run:**

$$\Delta x = \int_0^5 (10t - 0.6t^2)\,dt = \Big[5t^2 - 0.2t^3\Big]_0^5 = 125 - 25 = 100\,\text{m}$$

**Sanity check:** that matches $x(5) - x(0) = 100\,\text{m}$ read straight off the original formula, as it must. The average velocity is $100/5 = 20\,\text{m/s}$, well under the final $35\,\text{m/s}$ — right for a car that started from rest and sped up all the way.

## Where the picture breaks

The formula is a curve fitted to data, not a law of nature, and it is honest only inside the five seconds it was fitted to. Push it further and it lies: it claims the acceleration reaches zero at about $8.3\,\text{s}$ and that the car starts going *backwards* after about $16.7\,\text{s}$, long after the run has finished. A real launch is also not smooth — there is wheelspin, a bite point, and a step at every gearshift — and the derivative of a fitted curve quietly erases all of them. And the model tracks one point on the car; a hard launch lifts the nose, so different parts of it move differently.

## Key takeaway

Differentiate position to get velocity, and velocity to get acceleration: $v = dx/dt$, $a = dv/dt$. Integrate velocity to get displacement, $\Delta x = \int v\,dt$, which is the area under the $v$–$t$ graph. One line of algebra for position contains the speed, the pull and the distance of the whole run.
