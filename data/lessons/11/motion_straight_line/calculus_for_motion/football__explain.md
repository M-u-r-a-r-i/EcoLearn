---
concept_id: calculus_for_motion
interest: football
format: explain
title: A winger's whole sprint in one line of algebra
check:
  question: |-
    Tracking software fits the motion of a pass rolling along the grass as $x = 10t - t^2$, with $x$ in metres and $t$ in seconds, for $0 \le t \le 5\,\text{s}$. What is the ball's velocity at $t = 3\,\text{s}$?
  options:
    A: |-
      $7\,\text{m/s}$
    B: |-
      $21\,\text{m/s}$
    C: |-
      $-2\,\text{m/s}$
    D: |-
      $4\,\text{m/s}$
  answer: D
  explanation: |-
    Velocity is the derivative of position: $v = dx/dt = 10 - 2t$. At $t = 3\,\text{s}$, $v = 10 - 6 = 4\,\text{m/s}$.
  misconceptions:
    A: |-
      Divides position by time, $x/t = 21/3$. That is the average velocity since $t = 0$, not the instantaneous velocity at $t = 3\,\text{s}$.
    B: |-
      Substitutes $t = 3$ into the position formula and reports $x = 21\,\text{m}$ as the velocity — confusing position with its rate of change.
    C: |-
      Differentiates twice and reports $d^2x/dt^2 = -2\,\text{m/s}^2$, which is the ball's acceleration, not its velocity.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A winger dribbles along the touchline towards goal, chased by a defender, while the goalkeeper comes off the line; a number line with origin O and +x runs beneath](scenes/football/motion_straight_line.svg "Every run along this touchline can be written as position against time.")

Dhruv, the academy's quickest winger, keeps getting to through balls just too late. The coach thinks his first steps are fine but that he "stops accelerating too early". The analyst, Rukhsana, tracks one of his runs with the camera system, from a standing start to the moment he meets the ball five seconds later. The software sums up the whole run in one line:

$x = 1.5t^2 - 0.1t^3$ (metres, seconds), for $0 \le t \le 5\,\text{s}$.

The coach has three questions. How fast is Dhruv going when he reaches the ball? Is he still speeding up at that moment, or has he already stopped accelerating? And how long was the run — should they check it with a tape?

"It's only a formula for position," Dhruv says, peering over her shoulder. "Where's the speed?"

"It's in there," says Rukhsana. "You just have to know how to ask."

How do you get a speed — and an acceleration — out of a formula that only says where he is?

## The physics

Velocity is the rate of change of position, and acceleration is the rate of change of velocity. In calculus, those rates are **derivatives**:

$$v = \frac{dx}{dt}, \qquad a = \frac{dv}{dt} = \frac{d^2x}{dt^2}$$

For polynomials you need one rule: $\dfrac{d}{dt}(t^n) = n\,t^{n-1}$, and a constant factor just comes along. So $\dfrac{d}{dt}(1.5t^2) = 3t$ and $\dfrac{d}{dt}(0.1t^3) = 0.3t^2$.

Going the other way — from velocity back to displacement — is **integration**. The displacement between $t_1$ and $t_2$ is the area under the $v$–$t$ graph:

$$\Delta x = x(t_2) - x(t_1) = \int_{t_1}^{t_2} v\,dt$$

using $\displaystyle\int t^n\,dt = \frac{t^{n+1}}{n+1}$. Likewise, integrating acceleration gives the change in velocity. Differentiation and integration undo each other, so you can move freely between $x$, $v$ and $a$.

The figure shows the same method for a different fitted run, $x = 1.2t^2 - 0.05t^3$:

![Two graphs. Left: position curve x = 1.2t² − 0.05t³ rising to 23.75 m at 5 s, with a dashed tangent of slope 8.25 m/s. Right: velocity curve v = 2.4t − 0.15t² rising to 8.25 m/s at 5 s](figures/calculus_for_motion/x-and-v-from-formula.svg "The derivative of the left curve at any time is the height of the right curve. The area under the right curve from 0 to 5 s is the height the left curve reaches: 23.75 m.")

## Worked example

**Given:** $x = 1.5t^2 - 0.1t^3$ (m, s), valid for $0 \le t \le 5\,\text{s}$ (an illustrative fit).
**Find:** Dhruv's velocity and acceleration when he meets the ball ($t = 5\,\text{s}$), and the run length by integration.

**Differentiate:**

$$v = \frac{dx}{dt} = 3t - 0.3t^2, \qquad a = \frac{dv}{dt} = 3 - 0.6t$$

At $t = 5\,\text{s}$:

$$v = 3(5) - 0.3(25) = 15 - 7.5 = 7.5\,\text{m/s} = 27\,\text{km/h}$$
$$a = 3 - 0.6(5) = 3 - 3 = 0$$

His acceleration started at $3\,\text{m/s}^2$ and fell steadily; it reaches zero exactly as he meets the ball. He is at top speed there, no longer speeding up — so the coach's worry is about whether he stops accelerating *too early*, and this fit says "just in time", with nothing to spare.

**Integrate** the velocity to check the length:

$$\Delta x = \int_0^5 (3t - 0.3t^2)\,dt = \Big[1.5t^2 - 0.1t^3\Big]_0^5 = 37.5 - 12.5 = 25\,\text{m}$$

**Sanity check:** this matches $x(5) - x(0) = 25\,\text{m}$ directly, as it must. His average velocity is $25/5 = 5.0\,\text{m/s}$, less than his final $7.5\,\text{m/s}$ — right for someone who started from rest and sped up.

## Where the picture breaks

The formula is a curve fitted to data, not a law of nature, and it works only inside the five seconds it was fitted to. Outside, it predicts nonsense: after $t = 5\,\text{s}$ it gives a negative acceleration, and after $t = 10\,\text{s}$ a negative velocity, as if Dhruv ran backwards. Real sprints also have a small surge with every stride that a smooth polynomial irons out. And the camera tracks one point on his body, while his legs and arms move quite differently.

## Key takeaway

Differentiate position to get velocity, and velocity to get acceleration: $v = dx/dt$, $a = dv/dt$. Integrate velocity to get displacement: $\Delta x = \int v\,dt$, the area under the $v$–$t$ graph. One formula for position contains the whole motion.
