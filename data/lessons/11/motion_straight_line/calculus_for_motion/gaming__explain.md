---
concept_id: calculus_for_motion
interest: gaming
format: explain
title: The boss charge written as one line of code
check:
  question: |-
    A game script moves a sliding platform along a straight rail with $x = 9t - 1.5t^2$, where $x$ is in metres and $t$ in seconds. What is the platform's velocity at $t = 2\,\text{s}$?
  options:
    A: |-
      $3\,\text{m/s}$
    B: |-
      $6\,\text{m/s}$
    C: |-
      $12\,\text{m/s}$
    D: |-
      $-3\,\text{m/s}$
  answer: A
  explanation: |-
    Velocity is the derivative of position: $v = dx/dt = 9 - 3t$. At $t = 2\,\text{s}$, $v = 9 - 6 = 3\,\text{m/s}$.
  misconceptions:
    B: |-
      Divides position by time, $x/t = 12/2$. That is the average velocity since $t = 0$, not the instantaneous velocity at $t = 2\,\text{s}$.
    C: |-
      Substitutes $t = 2$ into the position formula and reports $x = 12\,\text{m}$ as the velocity — confusing position with its rate of change.
    D: |-
      Differentiates twice and reports $d^2x/dt^2 = -3\,\text{m/s}^2$, which is the acceleration, not the velocity.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a monitor shows a side-scrolling game whose runner moves along a straight track marked like a number line, with a position and velocity readout; a tablet replays a velocity-time graph](scenes/gaming/motion_straight_line.svg "In a game, motion is often written directly as code: position as a formula in time.")

Zoya is modding a boss fight. Her favourite part is the boss's charge: it rumbles forward across the arena and, if you dodge, slams into the far wall and is stunned. In the game's script files she finds the whole charge written as one line:

`x = 1.2*t*t - 0.05*t*t*t`, in metres and seconds, running for $5$ seconds.

She wants to tune it, and she has three questions. How fast is the boss going at the end of the charge? Is it still speeding up then, or already slowing — which would make the slam feel weak? And does the charge actually reach the wall, which is $24\,\text{m}$ from the boss's starting spot, or does the boss stop short and "stun" itself on thin air?

"There's no speed anywhere in the script," she messages her friend Varun. "Just position."

Varun replies with one word: "Differentiate."

How do you get a speed — and an acceleration — out of a formula that only says where the boss is?

## The physics

Velocity is the rate of change of position, and acceleration is the rate of change of velocity. In the language of calculus, those rates are **derivatives**:

$$v = \frac{dx}{dt}, \qquad a = \frac{dv}{dt} = \frac{d^2x}{dt^2}$$

For polynomials you need one rule: $\dfrac{d}{dt}(t^n) = n\,t^{n-1}$, with a constant factor carried along. So $\dfrac{d}{dt}(1.2t^2) = 2.4t$ and $\dfrac{d}{dt}(0.05t^3) = 0.15t^2$.

Going the other way — from velocity back to displacement — is **integration**. The displacement between $t_1$ and $t_2$ is the area under the $v$–$t$ graph:

$$\Delta x = x(t_2) - x(t_1) = \int_{t_1}^{t_2} v\,dt$$

using $\displaystyle\int t^n\,dt = \frac{t^{n+1}}{n+1}$. In the same way, integrating acceleration gives the change in velocity. Differentiation and integration undo each other, so you can move freely between $x$, $v$ and $a$.

![Two graphs. Left: position curve x = 1.2t² − 0.05t³ rising to 23.75 m at 5 s, with a dashed tangent of slope 8.25 m/s. Right: velocity curve v = 2.4t − 0.15t² rising to 8.25 m/s at 5 s](figures/calculus_for_motion/x-and-v-from-formula.svg "The boss's charge, drawn from its script. The derivative of the left curve is the height of the right curve; the area under the right curve up to 5 s is where the left curve ends, 23.75 m.")

## Worked example

**Given:** $x = 1.2t^2 - 0.05t^3$ (m, s), for $0 \le t \le 5\,\text{s}$.
**Find:** the boss's velocity and acceleration at $t = 5\,\text{s}$, and the length of the charge from integration.

**Differentiate:**

$$v = \frac{dx}{dt} = 2.4t - 0.15t^2, \qquad a = \frac{dv}{dt} = 2.4 - 0.30t$$

At $t = 5\,\text{s}$:

$$v = 2.4(5) - 0.15(25) = 12 - 3.75 = 8.25\,\text{m/s} \approx 29.7\,\text{km/h}$$
$$a = 2.4 - 0.30(5) = 2.4 - 1.5 = +0.9\,\text{m/s}^2$$

The acceleration is still positive, so the boss is still speeding up at the end — the slam won't feel weak. (Its acceleration started at $2.4\,\text{m/s}^2$ and has been falling.)

**Integrate** the velocity to get the length of the charge:

$$\Delta x = \int_0^5 (2.4t - 0.15t^2)\,dt = \Big[1.2t^2 - 0.05t^3\Big]_0^5 = 30 - 6.25 = 23.75\,\text{m}$$

The charge ends $0.25\,\text{m}$ short of the $24\,\text{m}$ wall. Zoya has found a real bug.

**Sanity check:** this matches $x(5) - x(0) = 23.75\,\text{m}$ straight from the script, as it must. The average velocity is $23.75/5 = 4.75\,\text{m/s}$, below the final $8.25\,\text{m/s}$ — right for something that started from rest and kept speeding up.

## Where the picture breaks

A game doesn't evaluate the formula continuously: it evaluates it once per frame, so the boss really moves in tiny jumps — at 60 frames per second, one every $16.7\,\text{ms}$. The derivative describes the smooth curve those jumps sit on. The formula is also only meant for $0 \le t \le 5\,\text{s}$: run it longer and it predicts nonsense — the acceleration turns negative after $t = 8\,\text{s}$ and the boss would start moving backwards after $t = 16\,\text{s}$. A real charging animal or vehicle isn't described by a neat polynomial either; in real life such formulas are curves fitted to data, not laws of nature.

## Key takeaway

Differentiate position to get velocity, and velocity to get acceleration: $v = dx/dt$, $a = dv/dt$. Integrate velocity to get displacement: $\Delta x = \int v\,dt$, the area under the $v$–$t$ graph. One formula for position contains the whole motion.
