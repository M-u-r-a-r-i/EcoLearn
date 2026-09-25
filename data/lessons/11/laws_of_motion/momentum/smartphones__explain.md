---
concept_id: momentum
interest: smartphones
format: explain
title: Same speed, but the robot vacuum still changed something
check:
  question: |-
    A $0.20\,\text{kg}$ phone falls onto a hard floor, hitting it at $5.0\,\text{m/s}$ downwards, and bounces up at $2.0\,\text{m/s}$. What is the change in the phone's momentum?
  options:
    A: |-
      $0.60\,\text{kg m/s}$, upwards
    B: |-
      $1.4\,\text{kg m/s}$, downwards
    C: |-
      $1.0\,\text{kg m/s}$, upwards
    D: |-
      $1.4\,\text{kg m/s}$, upwards
  answer: D
  explanation: |-
    Take up as positive. Before: $p = 0.20 \times (-5.0) = -1.0\,\text{kg m/s}$. After: $p = 0.20 \times (+2.0) = +0.40\,\text{kg m/s}$. Change $= 0.40 - (-1.0) = +1.4\,\text{kg m/s}$, upwards.
  misconceptions:
    A: |-
      Subtracts the speeds, $5.0 - 2.0 = 3.0\,\text{m/s}$, as if momentum had no direction. The downward and upward velocities have opposite signs, so the change is their *sum* in size.
    B: |-
      Gets the size right but points the change along the original motion. The floor reversed the phone, so the change in momentum points the way the floor pushed: up.
    C: |-
      Counts only the stopping part, $0.20 \times 5.0$. Stopping the phone is not the end; sending it back up at $2.0\,\text{m/s}$ needs another $0.40\,\text{kg m/s}$ of change.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A study room at night: a camera drone hovers pushing air down, a phone tumbles off a shelf towards the tiles, and a power bank dangles off a desk by its cable](scenes/smartphones/laws_of_motion.svg "Moving things in this room carry momentum — the falling phone, the air in the drone's downwash, even the sliding phone on the desk.")

Kiran's family bought a robot vacuum cleaner, and he has decided to study it properly. He props his phone against a chair leg, sets the camera to slow motion, and films the robot trundling across the hall.

It rolls straight at the wall, taps its bumper against the skirting board, and reverses away along the same line. Frame by frame, Kiran marks its position against the floor tiles. The result is neat: it approaches at about the same speed it leaves with.

"So the wall didn't change anything," he tells his sister Divya. "Same speed in, same speed out."

"Then why did the bumper click?" she says. "Something happened at that wall. You heard it."

Kiran replays the clip. The speed really is unchanged. So what did change when the robot hit the wall — and how would you put a number on it?

## The physics

The **linear momentum** of a body is its mass times its velocity:

$$\vec{p} = m\vec{v}$$

Its SI unit is $\text{kg m/s}$ (equivalently $\text{N s}$).

Because velocity is a vector and mass is a positive scalar, **momentum is a vector** that points the same way as the velocity. Two facts follow.

- Momentum depends on *both* mass and velocity. A light, fast body can carry as much momentum as a heavy, slow one.
- A change of **direction** is a change of momentum, even at unchanged speed. Choose a positive direction and give each momentum a sign.

That answers Kiran. Take "away from the wall" as positive. Before the tap the robot's momentum is $-mv$; after it is $+mv$. The speeds match, but the change is

$$\Delta p = (+mv) - (-mv) = 2mv$$

— twice the size of either momentum, and pointing away from the wall. That is the click Divya heard: the wall had to push on the bumper to produce it.

![A body arriving leftwards with negative momentum, driven back at the same speed with positive momentum, and the change twice the size of either](figures/momentum/momentum-is-a-vector.svg "Drawn for a small ball, but it is the robot at the skirting board exactly: same speed, opposite arrows, so the change in momentum is double, not zero.")

## Worked example

**Given:** the robot vacuum has mass $3.0\,\text{kg}$ and moves at $0.50\,\text{m/s}$; a $0.20\,\text{kg}$ phone falls onto the tiles at $5.0\,\text{m/s}$ (illustrative values).
**Find:** each momentum, and the robot's change in momentum when it reverses at the wall.

1. *The robot.*
$$p = mv = 3.0 \times 0.50 = 1.5\,\text{kg m/s}$$
A heavy gadget moving at a slow walking pace.

2. *The phone.*
$$p = 0.20 \times 5.0 = 1.0\,\text{kg m/s}$$
Fifteen times lighter, but ten times faster — so two-thirds of the robot's momentum.

3. *The robot reversing.* Taking "away from the wall" as positive, it goes from $-1.5$ to $+1.5\,\text{kg m/s}$:
$$\Delta p = 1.5 - (-1.5) = 3.0\,\text{kg m/s}, \text{ away from the wall}$$

**Sanity check:** a reversal must need more change than a plain stop, and $3.0$ is exactly twice the $1.5$ it would take just to bring the robot to rest.

## Where the picture breaks

A real robot vacuum doesn't bounce off the wall like a ball: it senses the bump and drives its own wheels in reverse, so the floor's friction on the wheels does much of the pushing, not only the wall. The calculation still holds for the total change in momentum; it just doesn't tell you which force supplied it. Its speed in and out also only roughly match. And note that a *bigger* momentum doesn't mean a bigger energy in the same way — the lighter, faster phone carries far more kinetic energy than the robot, which you'll meet in Work, Energy and Power.

## Key takeaway

Momentum is mass times velocity, $\vec{p} = m\vec{v}$, and it is a vector pointing along the velocity. Reversing direction at the same speed changes the momentum by $2mv$, not zero — so always choose a positive direction and keep the signs.
