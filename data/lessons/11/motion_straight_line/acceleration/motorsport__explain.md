---
concept_id: acceleration
interest: motorsport
format: explain
title: Can a negative acceleration make you faster
check:
  question: |-
    A data logger shows a car's velocity falling in a straight line from $+30\,\text{m/s}$ to $+10\,\text{m/s}$ in $4.0\,\text{s}$ as it brakes for a corner, with positive taken as its direction of travel. What is its acceleration?
  options:
    A: |-
      $+5.0\,\text{m/s}^2$
    B: |-
      $-5.0\,\text{m/s}^2$
    C: |-
      $-80\,\text{m/s}^2$
    D: |-
      $-2.5\,\text{m/s}^2$
  answer: B
  explanation: |-
    Acceleration is the slope of the velocity–time graph: $a = \Delta v/\Delta t = (10 - 30)/4.0 = -5.0\,\text{m/s}^2$. The minus sign says it points against the motion, so the car slows.
  misconceptions:
    A: |-
      Subtracts initial from final the wrong way round, or reports the size only. Slowing down while moving in the positive direction needs a negative acceleration.
    C: |-
      Multiplies the change in velocity by the time ($20 \times 4.0$) instead of dividing — confusing the slope of the graph with the area under it.
    D: |-
      Divides the final velocity by the time ($10/4.0$). Acceleration uses the *change* in velocity, not the velocity left at the end.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A long straight at a race circuit with a car accelerating away from the timing beam at the start line, distance boards reading 0, 100 and 200 along the verge, and an arrow marking the positive direction](scenes/motorsport/motion_straight_line.svg "Pull away, hold a steady speed, brake, reverse — four different things the same logger has to describe.")

The logger on Tejas's college team car runs whenever the ignition is on, which is how a two-minute crawl through the paddock ended up on the big screen at the debrief.

It is nothing dramatic. Tejas pulled away from the garage, ran down the paddock lane at a steady speed, braked at the end of it, and then reversed neatly into the scrutineering bay.

Ruchi, the team's data engineer, puts the velocity–time trace up anyway. "Tell me where you were accelerating."

"All of it," says Tejas. "The car was moving the whole time."

"Look at the flat bit," says Ruchi.

Then Tejas notices something worse. While he was reversing into the bay — picking up pace, not losing it — the trace shows a **negative** acceleration.

"Negative acceleration means slowing down," he says. "Everyone knows that. Your logger is broken."

So when exactly was he accelerating? And can a negative acceleration really make a car faster?

## The physics

**Acceleration** is the rate of change of velocity. Over an interval,

$$\bar{a} = \frac{\Delta v}{\Delta t} = \frac{v_f - v_i}{t_f - t_i}$$

and at an instant, $a = dv/dt$. Its SI unit is $\text{m/s}^2$ — metres per second, per second. Acceleration is a **vector**, and in one dimension its sign carries its direction.

Two consequences do most of the work:

- **Constant velocity means zero acceleration**, however fast you are going. Moving is not accelerating.
- **The sign of $a$ by itself does not tell you whether you speed up.** If $v$ and $a$ have the *same* sign, the speed grows. If they have *opposite* signs, the speed falls.

On a velocity–time graph, acceleration is the **slope**: a rising line means positive $a$, a flat line means $a = 0$, a falling line means negative $a$, and the steeper the line the bigger the magnitude.

![A velocity–time graph in five phases: up from 0 to 8 m/s, flat at 8 m/s, down to 0, down further to −3 m/s, then flat at −3 m/s](figures/acceleration/vt-slope-sign.svg "Read acceleration as slope. In the fourth phase the slope is negative and so is the velocity — same sign, so the speed is growing.")

Take positive as the direction Tejas first drove, down the paddock lane. The trace in the figure has exactly his five phases in it.

## Worked example

**Given:** the five phases of the trace above (illustrative numbers).
**Find:** the acceleration in each, and whether the car is speeding up or slowing down.

| Phase | $\Delta v$ (m/s) | $\Delta t$ (s) | $a$ (m/s²) | Speed |
|---|---|---|---|---|
| $0$–$2.0\,\text{s}$, pulling away | $8 - 0 = +8$ | $2.0$ | $+4.0$ | rising |
| $2.0$–$3.5\,\text{s}$, steady | $0$ | $1.5$ | $0$ | steady |
| $3.5$–$4.5\,\text{s}$, braking | $0 - 8 = -8$ | $1.0$ | $-8.0$ | falling |
| $4.5$–$5.5\,\text{s}$, reversing | $-3 - 0 = -3$ | $1.0$ | $-3.0$ | rising |
| $5.5$–$6.5\,\text{s}$, steady reverse | $0$ | $1.0$ | $0$ | steady |

While braking, $v > 0$ and $a < 0$: opposite signs, so the car slows. While reversing, $v < 0$ and $a < 0$: the same sign, so the car speeds up — to $3\,\text{m/s}$ backwards. The logger was right, and the rule "negative means slowing" is wrong.

**Sanity check:** $8\,\text{m/s}$ is about $29\,\text{km/h}$, a sensible paddock speed, and each acceleration has units of $(\text{m/s})/\text{s} = \text{m/s}^2$. The hardest number here is the $-8\,\text{m/s}^2$ of braking, which is under $1g$ — easy for a car with racing brakes, and roughly what you feel when a bus stops sharply.

## Where the picture breaks

A real trace has no perfectly straight segments and no sharp corners: a car pulls hardest in first gear and tails off, brakes bite over a few tenths of a second, and every line on the graph is really a smooth bend. The straight segments give the *average* acceleration of each phase. The graph also stops making sense the moment the car turns: a change of direction alone is an acceleration too, even at constant speed, which is why cornering forces exist at all — you will meet that in *Motion in a Plane*. Here everything has been kept on one straight paddock lane.

## Key takeaway

Acceleration is the rate of change of velocity, $a = \Delta v/\Delta t$, read off a velocity–time graph as its slope. Zero slope means zero acceleration, even flat out. And a negative acceleration slows you only when you are moving in the positive direction: when $v$ and $a$ share a sign, you speed up — backwards, if that is the way you are pointing.
