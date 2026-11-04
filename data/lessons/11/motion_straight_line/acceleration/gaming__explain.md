---
concept_id: acceleration
interest: gaming
format: explain
title: Tuning a hero's run with a velocity graph
check:
  question: |-
    A kart-racing game's telemetry shows a kart's velocity falling in a straight line from $+24\,\text{m/s}$ to $0$ in $3.0\,\text{s}$ as it brakes for a hairpin. What is its acceleration during the braking?
  options:
    A: |-
      $-8.0\,\text{m/s}^2$
    B: |-
      $+8.0\,\text{m/s}^2$
    C: |-
      $-72\,\text{m/s}^2$
    D: |-
      $0\,\text{m/s}^2$
  answer: A
  explanation: |-
    Acceleration is the slope of the $v$–$t$ graph: $a = \Delta v/\Delta t = (0 - 24)/3.0 = -8.0\,\text{m/s}^2$. The minus sign shows it points opposite to the kart's motion, so the kart slows down.
  misconceptions:
    B: |-
      Treats acceleration as a size only (or subtracts final from initial), losing the sign. Slowing down while moving in the positive direction means a negative acceleration.
    C: |-
      Multiplies the change in velocity by the time ($24 \times 3.0$) instead of dividing — mixing up the slope of the graph with the area under it.
    D: |-
      Thinks that because the final velocity is zero, the acceleration is zero. Acceleration depends on how the velocity changes, not on its value at the end.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a monitor shows a side-scrolling game whose runner moves along a straight track marked like a number line, with a position and velocity readout; a tablet replays a velocity-time graph](scenes/gaming/motion_straight_line.svg "Game developers tune how a character 'feels' by shaping its velocity against time.")

Meher is making her first platformer for a school game-jam, and playtesters keep saying the hero "feels floaty". So she switches on her engine's debug graph, which plots the hero's velocity every frame, and records one run.

The hero sprints right from a standstill, holds top speed for a moment, skids to a stop at the edge of a pit, then turns and jogs back left to grab a coin.

Her friend Aditya reads the graph over her shoulder. "Accelerating the whole time, obviously. He's running."

"Look at the flat part," says Meher.

Then Aditya spots something that bothers him. On the jog back, the engine reports a **negative** acceleration — while the hero is clearly speeding up.

"Negative acceleration means slowing down," he says. "Everyone knows that. Your engine has a sign bug."

When exactly was the hero accelerating? And can a negative acceleration really make him faster?

## The physics

**Acceleration** is the rate of change of velocity. Over an interval,

$$\bar{a} = \frac{\Delta v}{\Delta t} = \frac{v_f - v_i}{t_f - t_i}$$

and at an instant, $a = dv/dt$. Its SI unit is $\text{m/s}^2$ — metres per second, per second. Acceleration is a **vector**; in one dimension its sign gives its direction.

Two consequences matter most:

- **Constant velocity means zero acceleration**, however fast you are going. Running is not the same as accelerating.
- **The sign of $a$ alone doesn't tell you whether you speed up.** If $v$ and $a$ have the *same* sign, the speed increases. If they have *opposite* signs, the speed decreases.

On a velocity–time graph, the acceleration is the **slope**: a rising line means positive $a$, a flat line means $a = 0$, a falling line means negative $a$. The steeper the line, the larger the magnitude of the acceleration.

![A velocity–time graph in five phases: up from 0 to 8 m/s, flat at 8 m/s, down to 0, down further to −3 m/s, then flat at −3 m/s](figures/acceleration/vt-slope-sign.svg "Read acceleration as slope. From 4.5 s to 5.5 s the slope is negative and so is the velocity, so the speed grows.")

Take the positive direction as right, the way the hero first sprinted. The graph above has the shape of Meher's debug trace (illustrative numbers).

## Worked example

**Given:** the hero's $v$–$t$ graph above.
**Find:** the acceleration in each phase, and whether the hero speeds up or slows down.

| Phase | $\Delta v$ (m/s) | $\Delta t$ (s) | $a$ (m/s²) | Speed |
|---|---|---|---|---|
| $0$–$2.0\,\text{s}$, sprint | $8 - 0 = +8$ | $2.0$ | $+4.0$ | rising |
| $2.0$–$3.5\,\text{s}$, top speed | $0$ | $1.5$ | $0$ | steady |
| $3.5$–$4.5\,\text{s}$, skid | $0 - 8 = -8$ | $1.0$ | $-8.0$ | falling |
| $4.5$–$5.5\,\text{s}$, turn back | $-3 - 0 = -3$ | $1.0$ | $-3.0$ | rising |
| $5.5$–$6.5\,\text{s}$, jog | $0$ | $1.0$ | $0$ | steady |

During the skid, $v > 0$ and $a < 0$: opposite signs, so the hero slows. On the way back, $v < 0$ and $a < 0$: the same sign, so he speeds up, to $3\,\text{m/s}$ leftwards. The engine is right; Aditya's "negative means slowing" rule is wrong.

**Sanity check:** units are $(\text{m/s})/\text{s} = \text{m/s}^2$ throughout. The skid is twice as sharp as the launch ($8.0$ against $4.0\,\text{m/s}^2$), which matches the graph: the skid line drops $8\,\text{m/s}$ in half the time the sprint line took to climb it.

## Where the picture breaks

A game character's velocity graph can have genuinely sharp corners, because the code can switch acceleration on and off in a single frame; a real runner's graph is always smooth, with acceleration strongest in the first strides and fading near top speed. That instant switching is part of why game movement can feel "robotic", and why developers add easing curves. Also, many games apply their own chosen accelerations rather than anything a human could produce. And we kept the hero on one straight line; a change of direction round a curve is an acceleration too, which you'll meet in *Motion in a Plane*.

## Key takeaway

Acceleration is the rate of change of velocity, $a = \Delta v/\Delta t$, read as the slope of a velocity–time graph. A flat line means zero acceleration, even at top speed. A negative acceleration slows you only if you are moving in the positive direction; when $v$ and $a$ share a sign, you speed up.
