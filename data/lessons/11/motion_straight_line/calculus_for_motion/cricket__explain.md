---
concept_id: calculus_for_motion
interest: cricket
format: explain
title: Getting a bowler's speed out of one formula
check:
  question: |-
    Tracking software fits a fielder's position as she runs in and slows down: $x = 4t - 0.5t^2$, with $x$ in metres and $t$ in seconds. What is her velocity at $t = 2\,\text{s}$?
  options:
    A: |-
      $3\,\text{m/s}$
    B: |-
      $2\,\text{m/s}$
    C: |-
      $6\,\text{m/s}$
    D: |-
      $-1\,\text{m/s}$
  answer: B
  explanation: |-
    Velocity is the derivative of position: $v = dx/dt = 4 - t$. At $t = 2\,\text{s}$, $v = 4 - 2 = 2\,\text{m/s}$.
  misconceptions:
    A: |-
      Divides position by time, $x/t = 6/2$. That is the average velocity since $t = 0$, not the instantaneous velocity at $t = 2\,\text{s}$.
    C: |-
      Substitutes $t = 2$ into the position formula and reports $x = 6\,\text{m}$ as the velocity — confusing position with its rate of change.
    D: |-
      Differentiates twice and reports $d^2x/dt^2 = -1\,\text{m/s}^2$, which is her acceleration, not her velocity.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground in sunshine: a batter runs between the wickets on a 22-yard pitch while a fielder chases the ball towards the boundary rope](scenes/cricket/motion_straight_line.svg "Every movement on this ground can be written as position against time.")

Aditi spends Saturdays at the academy's bowling lab. Today's subject is Harsh, a young fast bowler whose run-up the coach wants to fix. A camera tracks him from his mark to the crease, and the software sums up the whole run-up in a single line:

$x = 1.2t^2 - 0.05t^3$ (metres, seconds), for the $5$ seconds from his first step to the crease.

Coach Menon has three questions. How fast is Harsh going when he reaches the crease? Is he still speeding up there, or has he already started to slow down — a common fault? And did the software get the run-up length right, or should they measure it with a tape?

"The software only gave us position," Aditi says. "There's no speed in that formula."

"Isn't there?" says the coach, and hands her a pen.

How do you get a speed — and an acceleration — out of a formula that only tells you where he is?

## The physics

Velocity is the rate of change of position, and acceleration is the rate of change of velocity. In the language of calculus, those rates are **derivatives**:

$$v = \frac{dx}{dt}, \qquad a = \frac{dv}{dt} = \frac{d^2x}{dt^2}$$

For polynomials you need one rule: $\dfrac{d}{dt}(t^n) = n\,t^{n-1}$, and a constant factor just comes along. So $\dfrac{d}{dt}(1.2t^2) = 2.4t$ and $\dfrac{d}{dt}(0.05t^3) = 0.15t^2$.

Going the other way — from velocity back to displacement — is **integration**. The displacement between $t_1$ and $t_2$ is the area under the $v$–$t$ graph:

$$\Delta x = x(t_2) - x(t_1) = \int_{t_1}^{t_2} v\,dt$$

using $\displaystyle\int t^n\,dt = \frac{t^{n+1}}{n+1}$. Likewise, integrating acceleration gives the change in velocity. Differentiation and integration undo each other, so you can move freely between $x$, $v$ and $a$.

![Two graphs. Left: position curve x = 1.2t² − 0.05t³ rising to 23.75 m at 5 s, with a dashed tangent of slope 8.25 m/s. Right: velocity curve v = 2.4t − 0.15t² rising to 8.25 m/s at 5 s](figures/calculus_for_motion/x-and-v-from-formula.svg "The derivative of the left curve at any time is the height of the right curve. The area under the right curve from 0 to 5 s is the height the left curve reaches: 23.75 m.")

## Worked example

**Given:** $x = 1.2t^2 - 0.05t^3$ (m, s), valid for $0 \le t \le 5\,\text{s}$ (an illustrative model).
**Find:** Harsh's velocity and acceleration at the crease ($t = 5\,\text{s}$), and the run-up length from integration.

**Differentiate:**

$$v = \frac{dx}{dt} = 2.4t - 0.15t^2, \qquad a = \frac{dv}{dt} = 2.4 - 0.30t$$

At $t = 5\,\text{s}$:

$$v = 2.4(5) - 0.15(25) = 12 - 3.75 = 8.25\,\text{m/s} \approx 29.7\,\text{km/h}$$
$$a = 2.4 - 0.30(5) = 2.4 - 1.5 = +0.9\,\text{m/s}^2$$

The acceleration is still positive at the crease, so he is still speeding up — the coach's fear is unfounded. (It started at $2.4\,\text{m/s}^2$ at $t = 0$ and has been decreasing.)

**Integrate** the velocity to check the length:

$$\Delta x = \int_0^5 (2.4t - 0.15t^2)\,dt = \Big[1.2t^2 - 0.05t^3\Big]_0^5 = 30 - 6.25 = 23.75\,\text{m}$$

**Sanity check:** this matches $x(5) - x(0) = 23.75\,\text{m}$ directly, as it must. The average velocity is $23.75/5 = 4.75\,\text{m/s}$, less than the final $8.25\,\text{m/s}$ — right for someone who started from rest and sped up.

## Where the picture breaks

The formula is a curve fitted to data, not a law of nature. It works only inside the $5\,\text{s}$ it was fitted to: outside that, it predicts nonsense — after $t = 8\,\text{s}$ it gives a negative acceleration, and after $t = 16\,\text{s}$ a negative velocity, though Harsh has long since bowled the ball. Real run-ups also have small wobbles from each stride that a smooth polynomial ignores; the derivative of a fitted curve smooths over them. And the tracking follows one point on his body, while his arms and legs move quite differently.

## Key takeaway

Differentiate position to get velocity, and velocity to get acceleration: $v = dx/dt$, $a = dv/dt$. Integrate velocity to get displacement: $\Delta x = \int v\,dt$, the area under the $v$–$t$ graph. One formula for position contains the whole motion.
