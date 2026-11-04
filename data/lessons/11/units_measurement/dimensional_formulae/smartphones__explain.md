---
concept_id: dimensional_formulae
interest: smartphones
format: explain
title: What the sensors inside your phone are really measuring
check:
  question: |-
    A phone's gyroscope reports how fast the phone is turning, as an angular velocity in rad/s (angle turned $\div$ time). What is the dimensional formula of angular velocity?
  options:
    A: |-
      $[\text{L}\,\text{T}^{-1}]$
    B: |-
      $[\text{T}^{-1}]$
    C: |-
      $[\text{M}^0\,\text{L}^0\,\text{T}^0]$
    D: |-
      $[\text{rad}\,\text{s}^{-1}]$
  answer: B
  explanation: |-
    An angle is arc length $\div$ radius, so it is dimensionless. Angular velocity is angle $\div$ time, which leaves only $[\text{T}^{-1}]$.
  misconceptions:
    A: |-
      Treats the angle as a length, as if the phone were moving along a straight line. An angle is a ratio of two lengths, so the $\text{L}$ cancels.
    C: |-
      Reasons that because the angle is dimensionless, the whole quantity must be. Dividing by time still leaves $\text{T}^{-1}$; only the angle part drops out.
    D: |-
      Writes the unit instead of the dimensions. A dimensional formula uses the base quantities M, L and T, not particular units like the radian and second.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A study desk: a phone on a kitchen scale, a phone in a caliper, a charger and a USB meter, and a phone swinging from a shelf with a wavy graph on its screen](scenes/smartphones/units_measurement.svg "The swinging phone is recording its own motion. Every number it produces is built from mass, length and time.")

Aditi's older brother installs a sensor app on her phone and hands it back. "Your phone has more measuring instruments than our school lab," he says.

She scrolls through the list. The accelerometer shows three numbers in $\text{m/s}^2$ that jump when she shakes the phone. The barometer reads air pressure in hectopascals, and it changes, very slightly, when she climbs the stairs. The gyroscope reports "rad/s" when she spins the phone on the desk. Another screen shows the charger's power in watts.

"So there are hundreds of different kinds of quantity," Aditi says.

"Nope," says her brother. "Underneath, the sensors really only sense mass, length and time, in different mixtures."

Acceleration, pressure, spin rate, power — they look like they have nothing in common. How could all of them be recipes made from the same three ingredients? And is there a way to write down, for any quantity, exactly what the recipe is?

## The physics

Every physical quantity can be expressed through the base quantities. In mechanics you need three: **mass [M]**, **length [L]** and **time [T]**. (Current [A], temperature [K], amount of substance [mol] and luminous intensity [cd] appear in later chapters — you would need [A] for the phone's magnetometer, for example.)

The **dimensions** of a quantity are the powers to which the base quantities are raised to represent it. The expression showing them is its **dimensional formula**, written in square brackets. An equation like $[a] = [\text{L}\,\text{T}^{-2}]$ is a **dimensional equation**.

To find a dimensional formula, start from the quantity's defining equation and replace each quantity by its dimensions, one step at a time:

![A ladder: velocity is L T to the minus 1, acceleration L T to the minus 2, force M L T to the minus 2, work and energy M L squared T to the minus 2, power M L squared T to the minus 3](figures/dimensional_formulae/dimension-building-blocks.svg "Each quantity is built from the one above it. Dividing by time lowers the power of T by one; multiplying by a length raises the power of L by one.")

- velocity $=$ displacement $\div$ time: $[\text{L}\,\text{T}^{-1}]$
- acceleration $=$ velocity $\div$ time: $[\text{L}\,\text{T}^{-2}]$ — the accelerometer
- force $=$ mass $\times$ acceleration: $[\text{M}\,\text{L}\,\text{T}^{-2}]$
- work or energy $=$ force $\times$ displacement: $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$
- power $=$ work $\div$ time: $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$ — the charger's watts

Some quantities have **no** dimensions. Pure numbers like $\tfrac{1}{2}$ or $2\pi$ are dimensionless, and so are ratios of like quantities. An **angle** in radians is arc length $\div$ radius, $[\text{L}]/[\text{L}]$, so it is **dimensionless**: $[\text{M}^0\,\text{L}^0\,\text{T}^0]$. That's why the gyroscope's rad/s is, dimensionally, just $[\text{T}^{-1}]$ — the same as a frequency.

## Worked example

**Find** the dimensional formula of (a) the pressure the barometer reads (force $\div$ area); (b) the kinetic energy of a phone sliding off a table, $\tfrac{1}{2}mv^2$; (c) the gyroscope's angular velocity (angle $\div$ time).

(a) Area is length $\times$ length, $[\text{L}^2]$:

$$[\text{pressure}] = \frac{[\text{M}\,\text{L}\,\text{T}^{-2}]}{[\text{L}^2]} = [\text{M}\,\text{L}^{-1}\,\text{T}^{-2}]$$

(b) The $\tfrac{1}{2}$ is a pure number, so it has no dimensions:

$$\left[\tfrac{1}{2}mv^2\right] = [\text{M}] \times [\text{L}\,\text{T}^{-1}]^2 = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$$

(c) The angle is dimensionless:

$$[\omega] = \frac{[\text{M}^0\,\text{L}^0\,\text{T}^0]}{[\text{T}]} = [\text{T}^{-1}]$$

**Sanity check:** (b) should match work, force $\times$ displacement: $[\text{M}\,\text{L}\,\text{T}^{-2}][\text{L}] = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$. It does, as two forms of energy must. And power $\div$ energy should be $[\text{T}^{-1}]$, because power is energy per second: $[\text{M}\,\text{L}^2\,\text{T}^{-3}]/[\text{M}\,\text{L}^2\,\text{T}^{-2}] = [\text{T}^{-1}]$. It is.

## Where the picture breaks

The brother's line is a simplification: the sensors don't literally measure mass, length and time. The accelerometer senses a tiny force on a tiny mass inside a chip, and the barometer senses how a thin membrane bends. What's true is that the *quantities* they report are built from M, L and T.

Dimensions also tell you what a quantity is made of, not *which* quantity it is. Angular velocity and frequency share $[\text{T}^{-1}]$; work and torque (which you'll meet later) share $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$. And dimensions are not units: pressure is $[\text{M}\,\text{L}^{-1}\,\text{T}^{-2}]$ whether the app shows pascals or hectopascals.

## Key takeaway

A dimensional formula shows how a quantity is built from the base quantities, e.g. $[\text{M}\,\text{L}\,\text{T}^{-2}]$ for force and $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$ for power. Get it from the defining equation, one step at a time. Pure numbers and angles are dimensionless, so they drop out.
