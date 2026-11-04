---
concept_id: acceleration
interest: football
format: explain
title: A negative acceleration that made her faster
check:
  question: |-
    Take the positive direction as towards the opponents' goal. A defender tracking back speeds up in a straight line: her velocity changes from $-2.0\,\text{m/s}$ to $-6.0\,\text{m/s}$ in $0.80\,\text{s}$. What is her average acceleration?
  options:
    A: |-
      $+5.0\,\text{m/s}^2$
    B: |-
      $-3.2\,\text{m/s}^2$
    C: |-
      $-5.0\,\text{m/s}^2$
    D: |-
      $-10\,\text{m/s}^2$
  answer: C
  explanation: |-
    Acceleration is the change in velocity over time: $a = (v_f - v_i)/\Delta t = (-6.0 - (-2.0))/0.80 = -4.0/0.80 = -5.0\,\text{m/s}^2$. It has the same sign as her velocity, so she speeds up.
  misconceptions:
    A: |-
      Thinks "speeding up" must mean a positive acceleration. The sign of $a$ shows its direction; she speeds up because $a$ and $v$ are both negative.
    B: |-
      Multiplies the change in velocity by the time ($-4.0 \times 0.80$) instead of dividing — mixing up the slope of the $v$–$t$ graph with the area under it.
    D: |-
      Adds the two velocities instead of subtracting, $(-6.0 + (-2.0))/0.80$. Acceleration depends on the change in velocity, final minus initial.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A winger dribbles along the touchline towards goal, chased by a defender, while the goalkeeper comes off the line; a number line with origin O and +x runs beneath](scenes/football/motion_straight_line.svg "Sprint down the line, hold top speed, brake, turn and come back: a winger's day in one picture.")

At the state trials, every player wears a GPS vest. Lalremruati — Mami to her team — is on the right wing when a long ball is played over the top. She sprints down the touchline, holds top speed for a moment, brakes hard as the ball runs out near the corner flag, then turns and jogs back into position.

In the analysis room, the coach puts her velocity–time graph on the screen. Ishita, her teammate, shrugs. "Easy. She was accelerating the whole time. She was running!"

"Look at the flat part," says the coach.

Then Ishita spots something odd. On the way back, the graph shows a **negative** acceleration — yet Mami was speeding up, not slowing down.

"Negative acceleration means slowing down. Everyone knows that," Ishita says. "The vest has a bug."

When exactly was Mami accelerating? And can a negative acceleration really make you faster?

## The physics

**Acceleration** is the rate of change of velocity. Over an interval,

$$\bar{a} = \frac{\Delta v}{\Delta t} = \frac{v_f - v_i}{t_f - t_i}$$

and at an instant, $a = dv/dt$. Its SI unit is $\text{m/s}^2$ — metres per second, per second. Acceleration is a **vector**; in one dimension its sign gives its direction.

Two consequences matter most:

- **Constant velocity means zero acceleration**, however fast you're going. Running is not the same as accelerating.
- **The sign of $a$ alone doesn't tell you whether you speed up.** If $v$ and $a$ have the *same* sign, speed increases. If they have *opposite* signs, speed decreases.

On a velocity–time graph, the acceleration is the **slope**: a rising line means positive $a$, a flat line $a = 0$, a falling line negative $a$. The steeper the line, the larger the magnitude.

![A velocity–time graph in five phases: up from 0 to 8 m/s, flat at 8 m/s, down to 0, down further to −3 m/s, then flat at −3 m/s](figures/acceleration/vt-slope-sign.svg "Read acceleration as slope. From 4.5 s to 5.5 s the slope is negative and so is the velocity — so the speed grows.")

Take the positive direction as down the touchline towards the opponents' goal line, the way Mami first sprinted.

## Worked example

**Given:** Mami's $v$–$t$ graph above (illustrative numbers).
**Find:** her acceleration in each phase, and whether she is speeding up or slowing down.

| Phase | $\Delta v$ (m/s) | $\Delta t$ (s) | $a$ (m/s²) | Speed |
|---|---|---|---|---|
| $0$–$2.0\,\text{s}$, sprint | $8 - 0 = +8$ | $2.0$ | $+4.0$ | rising |
| $2.0$–$3.5\,\text{s}$, top speed | $0$ | $1.5$ | $0$ | steady |
| $3.5$–$4.5\,\text{s}$, braking | $0 - 8 = -8$ | $1.0$ | $-8.0$ | falling |
| $4.5$–$5.5\,\text{s}$, turning back | $-3 - 0 = -3$ | $1.0$ | $-3.0$ | rising |
| $5.5$–$6.5\,\text{s}$, jogging | $0$ | $1.0$ | $0$ | steady |

During braking, $v > 0$ and $a < 0$: opposite signs, so she slows. On the way back, $v < 0$ and $a < 0$: the same sign, so she speeds up — to $3\,\text{m/s}$ back up the pitch. The vest was right; "negative means slowing" is the bug.

**Sanity check:** $8\,\text{m/s}$ ($28.8\,\text{km/h}$) is a quick sprint for a winger, and braking at $8\,\text{m/s}^2$ is hard but possible over a few strides. Every $a$ has units of $(\text{m/s})/\text{s} = \text{m/s}^2$.

## Where the picture breaks

Real sprints don't give straight-line segments on a $v$–$t$ graph: acceleration is largest in the first strides and fades as a player nears top speed, and the corners are really smooth bends. The straight segments give the *average* acceleration of each phase. Also, a winger who curves infield is changing direction, and a change of direction alone is also an acceleration — you'll meet that in *Motion in a Plane*. Here Mami stays on one straight line.

## Key takeaway

Acceleration is the rate of change of velocity, $a = \Delta v/\Delta t$, read as the slope of a velocity–time graph. Zero slope means zero acceleration, even at top speed. A negative acceleration slows you only if you are moving in the positive direction; if $v$ and $a$ share a sign, you speed up.
