---
concept_id: dimensional_formulae
interest: cricket
format: explain
title: Every number on the coaching screen is built from three things
check:
  question: |-
    The coaching software reports the average force of the bat on the ball. What is the dimensional formula of force?
  options:
    A: |-
      $[\text{M}\,\text{L}\,\text{T}^{-2}]$
    B: |-
      $[\text{M}\,\text{L}\,\text{T}^{-1}]$
    C: |-
      $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$
    D: |-
      $[\text{kg}\,\text{m}\,\text{s}^{-2}]$
  answer: A
  explanation: |-
    Force $=$ mass $\times$ acceleration, and acceleration $=$ velocity $\div$ time $= [\text{L}\,\text{T}^{-2}]$. So force is $[\text{M}] \times [\text{L}\,\text{T}^{-2}] = [\text{M}\,\text{L}\,\text{T}^{-2}]$.
  misconceptions:
    B: |-
      Multiplies mass by velocity instead of acceleration. $[\text{M}\,\text{L}\,\text{T}^{-1}]$ is momentum, not force.
    C: |-
      Multiplies by a length as well, giving the dimensions of work or energy (force $\times$ distance), not force itself.
    D: |-
      Writes the SI unit instead of the dimensions. A dimensional formula uses the base quantities M, L, T, not particular units like kg, m, s.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch with a tape; a ball sits on a scale, a stopwatch runs and a speed display glows](scenes/cricket/units_measurement.svg "A tape for length, a scale for mass, a stopwatch for time. Everything else is built from these.")

Aarohi's academy has new coaching software. After each net session it fills a screen with numbers: the ball's release speed, how quickly it slowed after pitching, the average force of the bat on the ball, the energy of the shot, even something called "power".

She asks the analyst, Mr. D'Souza, where it all comes from. "Only three things," he says. "The cameras measure distances. The clock measures times. And we know the ball's mass from the scale. Everything else is calculated."

Aarohi looks at the screen again. Speed, force, energy, power — they're so different from each other. How can all of them be made from just mass, length and time? And is there a way to write down, for any quantity, exactly what it's made of?

## The physics

Every physical quantity can be expressed in terms of the base quantities. In mechanics you need three: **mass [M]**, **length [L]** and **time [T]**. (The other SI base quantities — current [A], temperature [K], amount of substance [mol] and luminous intensity [cd] — appear in later chapters.)

The **dimensions** of a quantity are the powers to which the base quantities are raised to represent it. The expression that shows them is its **dimensional formula**, written in square brackets. Writing a quantity equal to its dimensional formula, like $[v] = [\text{L}\,\text{T}^{-1}]$, is called a **dimensional equation**.

To find a dimensional formula, start from the quantity's defining equation and replace each quantity by its dimensions:

![A ladder: velocity is L T to the minus 1, acceleration L T to the minus 2, force M L T to the minus 2, work and energy M L squared T to the minus 2, power M L squared T to the minus 3](figures/dimensional_formulae/dimension-building-blocks.svg "Each quantity is built from the one above it. Dividing by time lowers the power of T by one; multiplying by a length raises the power of L by one.")

- velocity $=$ displacement $\div$ time: $[\text{L}\,\text{T}^{-1}]$
- acceleration $=$ velocity $\div$ time: $[\text{L}\,\text{T}^{-2}]$
- force $=$ mass $\times$ acceleration: $[\text{M}\,\text{L}\,\text{T}^{-2}]$
- momentum $=$ mass $\times$ velocity: $[\text{M}\,\text{L}\,\text{T}^{-1}]$
- work or energy $=$ force $\times$ displacement: $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$
- power $=$ work $\div$ time: $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$

Some quantities have **no** dimensions: pure numbers like $\tfrac{1}{2}$ or $2\pi$, and ratios of like quantities, such as an angle (arc length $\div$ radius) or a relative error. They are **dimensionless**: $[\text{M}^0\,\text{L}^0\,\text{T}^0]$.

So, on Aarohi's screen, speed is $[\text{L}\,\text{T}^{-1}]$, force is $[\text{M}\,\text{L}\,\text{T}^{-2}]$, energy is $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$ and power is $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$ — four different recipes from the same three ingredients.

## Worked example

**Find** the dimensional formula of (a) kinetic energy, $\tfrac{1}{2}mv^2$; (b) the pressure of a heavy roller on the pitch, force $\div$ area.

(a) The $\tfrac{1}{2}$ is a pure number, so it has no dimensions.

$$\left[\tfrac{1}{2}mv^2\right] = [\text{M}] \times [\text{L}\,\text{T}^{-1}]^2 = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$$

(b) Area is length × length, $[\text{L}^2]$.

$$[\text{pressure}] = \frac{[\text{M}\,\text{L}\,\text{T}^{-2}]}{[\text{L}^2]} = [\text{M}\,\text{L}^{-1}\,\text{T}^{-2}]$$

**Sanity check:** kinetic energy should match work, force $\times$ displacement: $[\text{M}\,\text{L}\,\text{T}^{-2}] \times [\text{L}] = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$. It does, as two forms of energy must.

## Where the picture breaks

Dimensions tell you what a quantity is *made of*, not *which* quantity it is. Different quantities can share a dimensional formula: work and torque (which you'll meet later) are both $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$. And dimensions are not units: $[\text{L}]$ can be measured in metres, centimetres or the yards of the cricket Laws. The dimensional formula stays the same whatever units you use.

## Key takeaway

A dimensional formula shows how a quantity is built from the base quantities, e.g. $[\text{M}\,\text{L}\,\text{T}^{-2}]$ for force. Get it from the defining equation, one step at a time; pure numbers and angles are dimensionless and drop out.
