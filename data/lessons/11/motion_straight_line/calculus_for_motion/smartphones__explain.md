---
concept_id: calculus_for_motion
interest: smartphones
format: explain
title: One line of tracking data and a speed limit
check:
  question: |-
    A delivery app fits a scooter's position as the rider brakes towards a stop: $x = 10t - t^2$, with $x$ in metres and $t$ in seconds. What is the scooter's velocity at $t = 3\,\text{s}$?
  options:
    A: |-
      $4\,\text{m/s}$
    B: |-
      $7\,\text{m/s}$
    C: |-
      $21\,\text{m/s}$
    D: |-
      $-2\,\text{m/s}$
  answer: A
  explanation: |-
    Velocity is the derivative of position: $v = dx/dt = 10 - 2t$. At $t = 3\,\text{s}$, $v = 10 - 6 = 4\,\text{m/s}$.
  misconceptions:
    B: |-
      Divides position by time, $x/t = 21/3$. That is the average velocity since $t = 0$, not the instantaneous velocity at $t = 3\,\text{s}$.
    C: |-
      Substitutes $t = 3$ into the position formula and reports $x = 21\,\text{m}$ as the velocity — confusing position with its rate of change.
    D: |-
      Differentiates twice and reports $d^2x/dt^2 = -2\,\text{m/s}^2$, which is the scooter's acceleration, not its velocity.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![An evening street: a phone shows a live-tracking map of a straight road, while a delivery scooter rides past kilometre markers](scenes/smartphones/motion_straight_line.svg "The rider's phone reports position again and again. Everything else is hidden inside those positions.")

Varun's aunt runs a small cloud kitchen, and her riders carry the kitchen's tracking app on their phones. Varun is helping her make sense of the data.

One stretch worries her. Outside a school, there's a straight road with a $25\,\text{km/h}$ limit (illustrative), and a parent has complained that a rider "shot off" from the traffic signal there. The app's analytics turned the rider's position logs from that moment into one tidy line:

$x = 1.2t^2 - 0.05t^3$ (metres, seconds), for the $5$ seconds after the light turned green.

"So how fast was he going at the end of those five seconds?" his aunt asks. "Was he still speeding up? And did he really go twenty-odd metres?"

"The app only gives position," Varun says. "There's no speed in that formula anywhere."

His aunt raises an eyebrow. "Didn't you just learn derivatives in maths?"

How do you get a speed and an acceleration out of a formula that only says where the scooter is?

## The physics

Velocity is the rate of change of position, and acceleration is the rate of change of velocity. In the language of calculus, those rates are **derivatives**:

$$v = \frac{dx}{dt}, \qquad a = \frac{dv}{dt} = \frac{d^2x}{dt^2}$$

For polynomials you need one rule: $\dfrac{d}{dt}(t^n) = n\,t^{n-1}$, and a constant factor just comes along. So $\dfrac{d}{dt}(1.2t^2) = 2.4t$ and $\dfrac{d}{dt}(0.05t^3) = 0.15t^2$.

Going the other way — from velocity back to displacement — is **integration**. The displacement between $t_1$ and $t_2$ is the area under the $v$–$t$ graph:

$$\Delta x = x(t_2) - x(t_1) = \int_{t_1}^{t_2} v\,dt$$

using $\displaystyle\int t^n\,dt = \frac{t^{n+1}}{n+1}$. In the same way, integrating acceleration gives the change in velocity. Differentiation and integration undo each other, so you can move freely between $x$, $v$ and $a$.

![Two graphs. Left: position curve x = 1.2t² − 0.05t³ rising to 23.75 m at 5 s, with a dashed tangent of slope 8.25 m/s. Right: velocity curve v = 2.4t − 0.15t² rising to 8.25 m/s at 5 s](figures/calculus_for_motion/x-and-v-from-formula.svg "The derivative of the left curve at any time is the height of the right curve. The area under the right curve from 0 to 5 s is the height the left curve reaches: 23.75 m.")

## Worked example

**Given:** $x = 1.2t^2 - 0.05t^3$ (m, s), positive along the road, valid for $0 \le t \le 5\,\text{s}$ (an illustrative fit).
**Find:** the scooter's velocity and acceleration at $t = 5\,\text{s}$, and the distance covered, by integration.

**Differentiate:**

$$v = \frac{dx}{dt} = 2.4t - 0.15t^2, \qquad a = \frac{dv}{dt} = 2.4 - 0.30t$$

At $t = 5\,\text{s}$:

$$v = 2.4(5) - 0.15(25) = 12 - 3.75 = 8.25\,\text{m/s} = 8.25 \times 3.6 \approx 29.7\,\text{km/h}$$
$$a = 2.4 - 0.30(5) = 2.4 - 1.5 = +0.9\,\text{m/s}^2$$

So after five seconds the rider was doing almost $30\,\text{km/h}$ in a $25\,\text{km/h}$ zone, and his acceleration was still positive — still speeding up. The parent had a point.

**Integrate** the velocity to check the distance:

$$\Delta x = \int_0^5 (2.4t - 0.15t^2)\,dt = \Big[1.2t^2 - 0.05t^3\Big]_0^5 = 30 - 6.25 = 23.75\,\text{m}$$

**Sanity check:** this matches $x(5) - x(0) = 23.75\,\text{m}$ directly, as it must. The average velocity is $23.75/5 = 4.75\,\text{m/s}$, less than the final $8.25\,\text{m/s}$ — right for a scooter that started from rest and sped up. And when did he pass $25\,\text{km/h} \approx 6.9\,\text{m/s}$? Solving $2.4t - 0.15t^2 = 6.9$ gives $t \approx 3.8\,\text{s}$ (the smaller root; the other lies outside the fit).

## Where the picture breaks

The formula is a curve fitted to a phone's position fixes, not a law of nature, and those fixes carry errors of a few metres — so a real analysis would treat the $29.7\,\text{km/h}$ as an estimate, not proof for a fine. The fit also works only inside the $5\,\text{s}$ it was made for: outside, it predicts nonsense — a negative acceleration after $t = 8\,\text{s}$ and a negative velocity after $t = 16\,\text{s}$, though the rider simply kept going. Differentiating a fitted curve also smooths over the real jerks of gear changes and bumps.

## Key takeaway

Differentiate position to get velocity, and velocity to get acceleration: $v = dx/dt$, $a = dv/dt$. Integrate velocity to get displacement: $\Delta x = \int v\,dt$, the area under the $v$–$t$ graph. A single line of position data contains the whole motion.
