---
concept_id: dimensional_formulae
interest: motorsport
format: explain
title: What the telemetry screen is really made of
check:
  question: |-
    The telemetry screen shows the engine's power output. Power is work done per unit time. What is the dimensional formula of power?
  options:
    A: |-
      $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$
    B: |-
      $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$
    C: |-
      $[\text{M}\,\text{L}\,\text{T}^{-3}]$
    D: |-
      $[\text{kg}\,\text{m}^2\,\text{s}^{-3}]$
  answer: B
  explanation: |-
    Work is force $\times$ displacement $= [\text{M}\,\text{L}\,\text{T}^{-2}][\text{L}] = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$. Dividing by time lowers the power of T by one: $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$.
  misconceptions:
    A: |-
      Gives the dimensions of work or energy and forgets that power is work *per unit time*, which needs one more $\text{T}^{-1}$.
    C: |-
      Treats power as force divided by time, leaving out the displacement. Power is the rate of doing work, and work includes a length.
    D: |-
      Writes the SI unit, not the dimensions. A dimensional formula uses the base quantities M, L, T, not particular units like kg, m, s.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A race track with a timing screen showing a lap time and a speed-trap reading, a car crossing the line, and a braking marker by the track](scenes/motorsport/units_measurement.svg "Times from the timing loops, distances from the track, and the car's known mass. Every other number is calculated from these.")

Ishita has joined her college's student racing team, and on test day she sits beside the lead engineer, Mr. Bhattacharya, watching the telemetry screen fill with numbers: speed, braking deceleration in "g", downforce in newtons, the kinetic energy the brakes must soak up at each corner, and the engine's power.

"Where do all these come from?" she asks.

"Sensors measure positions and times," he says. "We know the car's mass. The software calculates everything else."

Ishita stares at the screen. Speed, force, energy, power — they seem like completely different kinds of thing. Can they all really be made from mass, length and time? And if so, is there a way to write down exactly what each one is made of?

## The physics

Every physical quantity can be expressed in terms of base quantities. Mechanics needs three: **mass [M]**, **length [L]** and **time [T]**. (Current, temperature, amount of substance and luminous intensity join in later chapters.)

The **dimensions** of a quantity are the powers to which the base quantities are raised to represent it. The expression showing them, in square brackets, is its **dimensional formula**; writing $[v] = [\text{L}\,\text{T}^{-1}]$ is a **dimensional equation**.

To find a dimensional formula, start from the defining equation and replace each quantity by its dimensions:

![A ladder: velocity is L T to the minus 1, acceleration L T to the minus 2, force M L T to the minus 2, work and energy M L squared T to the minus 2, power M L squared T to the minus 3](figures/dimensional_formulae/dimension-building-blocks.svg "Each rung is built from the one above. Dividing by time lowers the power of T by one; multiplying by a length raises the power of L by one.")

- velocity $=$ displacement $\div$ time: $[\text{L}\,\text{T}^{-1}]$
- acceleration $=$ velocity $\div$ time: $[\text{L}\,\text{T}^{-2}]$
- force $=$ mass $\times$ acceleration: $[\text{M}\,\text{L}\,\text{T}^{-2}]$
- momentum $=$ mass $\times$ velocity: $[\text{M}\,\text{L}\,\text{T}^{-1}]$
- work or energy $=$ force $\times$ displacement: $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$
- power $=$ work $\div$ time: $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$

Pure numbers and ratios of like quantities are **dimensionless**, $[\text{M}^0\,\text{L}^0\,\text{T}^0]$.

So on Ishita's screen: speed $[\text{L}\,\text{T}^{-1}]$, downforce $[\text{M}\,\text{L}\,\text{T}^{-2}]$ (a force, like any other), brake energy $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$, engine power $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$. Four different recipes, three ingredients.

## Worked example

**Find** the dimensional formula of (a) the car's momentum, $mv$, and of force $\times$ time, $Ft$; (b) a braking deceleration shown as "$2.5\,g$", i.e. the ratio $a/g$.

(a) $$[mv] = [\text{M}][\text{L}\,\text{T}^{-1}] = [\text{M}\,\text{L}\,\text{T}^{-1}]$$
$$[Ft] = [\text{M}\,\text{L}\,\text{T}^{-2}][\text{T}] = [\text{M}\,\text{L}\,\text{T}^{-1}]$$

They match. That is no accident: you'll learn in Laws of Motion that a force acting for a time changes momentum (impulse).

(b) Both $a$ and $g$ are accelerations, $[\text{L}\,\text{T}^{-2}]$:

$$\left[\frac{a}{g}\right] = \frac{[\text{L}\,\text{T}^{-2}]}{[\text{L}\,\text{T}^{-2}]} = [\text{M}^0\,\text{L}^0\,\text{T}^0]$$

So "$2.5\,g$" is a pure number: the deceleration is $2.5$ times $g$. With $g = 9.8\,\text{m/s}^2$, that is $2.5 \times 9.8 \approx 25\,\text{m/s}^2$ (illustrative).

**Sanity check:** in (b), the units cancel as well — $(\text{m/s}^2)/(\text{m/s}^2)$ leaves nothing — which is exactly what "dimensionless" means.

## Where the picture breaks

A dimensional formula tells you what a quantity is made of, not which quantity it is. Work and torque (which you'll meet later) share $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$; momentum and impulse share $[\text{M}\,\text{L}\,\text{T}^{-1}]$. And "g-force" is a misleading name: it is a ratio of accelerations, not a force, and its dimensions show that plainly. Dimensions are also not units — power is $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$ whether the spec sheet uses watts, kilowatts or horsepower.

## Key takeaway

A dimensional formula shows how a quantity is built from M, L and T — force $[\text{M}\,\text{L}\,\text{T}^{-2}]$, energy $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$, power $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$. Build it step by step from the defining equation; pure numbers and ratios like $a/g$ are dimensionless.
