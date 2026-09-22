---
concept_id: dimensional_formulae
interest: gaming
format: explain
title: Everything in the physics debug panel from three ingredients
check:
  question: |-
    A game engine's debug panel shows the momentum of a crate, mass times velocity. What is the dimensional formula of momentum?
  options:
    A: |-
      $[\text{M}\,\text{L}\,\text{T}^{-2}]$
    B: |-
      $[\text{M}\,\text{L}\,\text{T}]$
    C: |-
      $[\text{kg}\,\text{m}\,\text{s}^{-1}]$
    D: |-
      $[\text{M}\,\text{L}\,\text{T}^{-1}]$
  answer: D
  explanation: |-
    Velocity is displacement divided by time, $[\text{L}\,\text{T}^{-1}]$. Momentum $=$ mass $\times$ velocity $= [\text{M}] \times [\text{L}\,\text{T}^{-1}] = [\text{M}\,\text{L}\,\text{T}^{-1}]$.
  misconceptions:
    A: |-
      Multiplies mass by acceleration instead of velocity. $[\text{M}\,\text{L}\,\text{T}^{-2}]$ is force, not momentum.
    B: |-
      Multiplies by time instead of dividing: velocity is displacement *per* time, so time appears with the power $-1$.
    C: |-
      Writes the SI unit instead of the dimensions. A dimensional formula uses the base quantities M, L and T, not particular units such as kg, m and s.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk: a monitor showing a racing game with a speed readout and a frame counter, a tape measure, a controller on a scale](scenes/gaming/units_measurement.svg "A speed in km/h, a frame rate in frames per second, a mass in kilograms. How many different ingredients are really on this desk?")

Siddharth is building a demolition level for his game: a car smashes through a stack of wooden crates. To tune it, he switches on the engine's physics debug panel. Every crate sprouts a floating label: *velocity*, *acceleration*, *force*, *momentum*, *kinetic energy*. The car's label adds *engine power*.

"That's a lot of different physics," says his friend Meher, watching the numbers flicker.

Siddharth scrolls to the crate's settings. There are only three things he actually typed in: its **mass**, its **size**, and the engine's **time step**. The engine calculated everything else, every frame.

Meher isn't convinced. "Force and energy and power are totally different things. How can all of them come from mass, lengths and time?" Is there a way to write down, for any quantity on that panel, exactly what it's built from?

## The physics

Every physical quantity can be expressed in terms of base quantities. Mechanics needs three: **mass [M]**, **length [L]** and **time [T]**. (Current [A], temperature [K], amount of substance [mol] and luminous intensity [cd] join in later chapters.)

The **dimensions** of a quantity are the powers to which the base quantities must be raised to represent it. The expression showing them, in square brackets, is its **dimensional formula**. Writing $[v] = [\text{L}\,\text{T}^{-1}]$ is a **dimensional equation**.

Get a dimensional formula from the quantity's defining equation, replacing each quantity by its dimensions:

![A ladder: velocity is L T to the minus 1, acceleration L T to the minus 2, force M L T to the minus 2, work and energy M L squared T to the minus 2, power M L squared T to the minus 3](figures/dimensional_formulae/dimension-building-blocks.svg "Each rung is built from the one above. Dividing by a time lowers the power of T by one; multiplying by a length raises the power of L by one.")

- velocity $=$ displacement $\div$ time: $[\text{L}\,\text{T}^{-1}]$
- acceleration $=$ velocity $\div$ time: $[\text{L}\,\text{T}^{-2}]$
- force $=$ mass $\times$ acceleration: $[\text{M}\,\text{L}\,\text{T}^{-2}]$
- momentum $=$ mass $\times$ velocity: $[\text{M}\,\text{L}\,\text{T}^{-1}]$
- work or energy $=$ force $\times$ displacement: $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$
- power $=$ work $\div$ time: $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$

Even the frame counter fits. A frame rate or refresh rate is a number of frames per unit time; a count is a pure number, so frequency is $[\text{T}^{-1}]$. A $144\,\text{Hz}$ display and a $1/60\,\text{s}$ time step are both about time and nothing else.

**Dimensionless** quantities have no dimensions at all, $[\text{M}^0\,\text{L}^0\,\text{T}^0]$: pure numbers like $\tfrac{1}{2}$ and $2\pi$, counts like "3 crates", and ratios of like quantities, such as an angle (arc length $\div$ radius).

So Meher's "totally different things" are four recipes from the same three ingredients: force $[\text{M}\,\text{L}\,\text{T}^{-2}]$, momentum $[\text{M}\,\text{L}\,\text{T}^{-1}]$, energy $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$, power $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$.

## Worked example

**Find** the dimensional formula of (a) a crate's kinetic energy, $\tfrac{1}{2}mv^2$; (b) its density, mass $\div$ volume.

(a) The $\tfrac{1}{2}$ is a pure number and drops out:

$$\left[\tfrac{1}{2}mv^2\right] = [\text{M}] \times [\text{L}\,\text{T}^{-1}]^2 = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$$

(b) Volume is length $\times$ length $\times$ length, $[\text{L}^3]$:

$$[\rho] = \frac{[\text{M}]}{[\text{L}^3]} = [\text{M}\,\text{L}^{-3}]$$

**Sanity check:** kinetic energy should match work, force $\times$ displacement: $[\text{M}\,\text{L}\,\text{T}^{-2}] \times [\text{L}] = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$. It does, as two forms of energy must. And density's SI unit, $\text{kg/m}^3$, has exactly the shape $[\text{M}\,\text{L}^{-3}]$.

## Where the picture breaks

The debug panel prints numbers in whatever units the engine was set up with; dimensions don't care about units. $[\text{L}]$ is the same whether a length is in metres, centimetres or engine units. Dimensions also can't tell quantities apart: work and torque (which you'll meet later) share $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$. And a game engine is free to break physics — a designer can give a crate any mass and let it bounce forever — but the dimensional formula of each quantity stays the same.

## Key takeaway

A dimensional formula shows how a quantity is built from the base quantities: $[\text{L}\,\text{T}^{-1}]$ for velocity, $[\text{M}\,\text{L}\,\text{T}^{-2}]$ for force, $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$ for energy. Find it from the defining equation, one step at a time; pure numbers, counts and angles are dimensionless.
