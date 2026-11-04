---
concept_id: si_units
interest: football
format: challenge
title: What the pascals on a ball pump are made of
check:
  question: |-
    A coach says a hard shot gives the ball about $130\,\text{J}$ of energy. Work is defined as force times distance. Written in SI base units, one joule is:
  options:
    A: |-
      $1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$
    B: |-
      $1\,\text{kg}\,\text{m}\,\text{s}^{-2}$
    C: |-
      $1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$
    D: |-
      The joule is itself a base unit, so it cannot be written in others
  answer: A
  explanation: |-
    $1\,\text{J} = 1\,\text{N} \times 1\,\text{m} = (\text{kg}\,\text{m}\,\text{s}^{-2}) \times \text{m} = \text{kg}\,\text{m}^2\,\text{s}^{-2}$. Multiplying by a distance adds one metre to the newton.
  misconceptions:
    B: |-
      Stops at the newton and forgets that work is force times a distance, which adds a metre.
    C: |-
      Divides by a second as well; $\text{kg}\,\text{m}^2\,\text{s}^{-3}$ is the watt, the unit of power (energy per second), not of energy.
    D: |-
      Thinks any unit with its own name is a base unit. Only seven units are base units; the joule, like the newton and the watt, is derived.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures the goal while a match ball sits on a scale beside a pressure gauge reading 0.9 atm](scenes/football/units_measurement.svg "The gauge beside the ball reports a pressure. What is a unit of pressure made of?")

Saturday morning, and the academy's match balls are all soft. Fatima is on pump duty, with Rohan holding the balls steady. Her pump's gauge has two scales: one in atmospheres, and a second, smaller ring marked in kilopascals.

"Pascals are for weather reports," Rohan says. "Air pressure is its own thing. A pascal isn't made of anything — it's a pascal, the way a metre is a metre."

Fatima has just finished the units chapter. "Pressure is force spread over an area. I bet you a plate of samosas I can write a pascal using nothing but kilograms, metres and seconds."

Rohan shakes on it. He's sure a pressure unit has nothing to do with mass or time. Who is paying for the samosas?

## The challenge

Starting only from these definitions —

- acceleration $=$ change in velocity $\div$ time,
- force $=$ mass $\times$ acceleration,
- pressure $=$ force $\div$ area,

write $1\,\text{Pa}$ in SI base units. Which base units appear, and with what powers?

## Think first

Is Rohan right that the pascal is a base unit, like the metre? If not, is it $\text{kg}\,\text{m}\,\text{s}^{-2}$, the same as a newton? Or does the area add metres — $\text{kg}\,\text{m}^3\,\text{s}^{-2}$? Or take them away? Build it one step at a time before reading on.

## The reveal

**Acceleration.** Velocity is in $\text{m/s}$; dividing by a time in seconds gives $\text{m}\,\text{s}^{-2}$.

**Force.** Mass times acceleration:

$$1\,\text{N} = 1\,\text{kg} \times 1\,\text{m}\,\text{s}^{-2} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$$

**Pressure.** Force divided by an area, and area is $\text{m} \times \text{m} = \text{m}^2$:

$$1\,\text{Pa} = \frac{1\,\text{N}}{1\,\text{m}^2} = \frac{\text{kg}\,\text{m}\,\text{s}^{-2}}{\text{m}^2} = 1\,\text{kg}\,\text{m}^{-1}\,\text{s}^{-2}$$

One metre from the newton cancels one of the two metres in the area, leaving $\text{m}^{-1}$. Fatima wins: kilogram, metre and second, nothing else.

![The newton, joule and watt shown as coloured blocks of kilogram, metre and second](figures/si_units/derived-units-from-base.svg "Every named mechanical unit is built from the same three blocks. The pascal is the newton with two metres divided out.")

If you guessed $\text{kg}\,\text{m}\,\text{s}^{-2}$, you built the newton and forgot the area. If you guessed $\text{kg}\,\text{m}^3\,\text{s}^{-2}$, you multiplied by the area instead of dividing. And Rohan's idea fails because only seven units are base units; the pascal isn't one. Air pressure in the ball is a real force per square metre, pushing on the inside of the ball's skin.

## The physics

The SI has seven **base units**: metre (m), kilogram (kg), second (s), ampere (A), kelvin (K), mole (mol) and candela (cd). Since 20 May 2019, each is defined by fixing the exact value of a constant of nature — for example, the second through the caesium-133 frequency, the metre through the speed of light, the kilogram through the Planck constant.

![A table of the seven SI base units with the constant that defines each](figures/si_units/seven-base-units.svg "The seven base units. The pascal, newton, joule and watt are not on this list: they are derived.")

Every other unit is a **derived unit**. To find it, write the quantity's defining equation and replace each quantity by its unit. Some derived units get special names — newton, joule, watt, pascal — but the name is only shorthand. For mechanics, the metre, kilogram and second are always enough.

## Worked example

**Find** the joule and the watt in base units, continuing from the newton.

Work is force times distance: $1\,\text{J} = 1\,\text{N}\,\text{m} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$.

Power is work per second: $1\,\text{W} = 1\,\text{J}/\text{s} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$.

**Sanity check:** a pascal times a cubic metre is $\text{kg}\,\text{m}^{-1}\,\text{s}^{-2} \times \text{m}^3 = \text{kg}\,\text{m}^2\,\text{s}^{-2}$, a joule. Pressure times volume is an energy — a relation you'll use in the chapters on gases.

## Key takeaway

Derived units are products of base units, read off from the defining equation: $1\,\text{N} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$, $1\,\text{Pa} = 1\,\text{kg}\,\text{m}^{-1}\,\text{s}^{-2}$, $1\,\text{J} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$. A special name never makes a unit a base unit.
