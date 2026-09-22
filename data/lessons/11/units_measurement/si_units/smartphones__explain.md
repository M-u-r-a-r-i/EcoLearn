---
concept_id: si_units
interest: smartphones
format: explain
title: The alphabet soup on a charger label
check:
  question: |-
    Kavya's charger label says it can deliver $10\,\text{W}$. Written in SI base units, one watt is:
  options:
    A: |-
      $1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$
    B: |-
      $1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}\,\text{A}^{-1}$
    C: |-
      $1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$
    D: |-
      $1\,\text{kg}\,\text{m}\,\text{s}^{-2}$
  answer: C
  explanation: |-
    Power is energy per unit time: $1\,\text{W} = 1\,\text{J/s}$. Since $1\,\text{J} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$, dividing by a second gives $1\,\text{W} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$.
  misconceptions:
    A: |-
      Confuses power with energy: $\text{kg}\,\text{m}^2\,\text{s}^{-2}$ is the joule. A watt is a joule *per second*, so it has one more $\text{s}^{-1}$.
    B: |-
      Confuses the watt with the volt, which also appears on the label. The volt is a watt per ampere, $\text{kg}\,\text{m}^2\,\text{s}^{-3}\,\text{A}^{-1}$.
    D: |-
      Confuses power with force, as if "powerful" meant "pushes hard". $\text{kg}\,\text{m}\,\text{s}^{-2}$ is the newton, the unit of force.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A study desk: a phone on a kitchen scale, a phone in a caliper, a charger labelled 5 V and 2 A plugged into a USB meter, and a phone swinging on a string](scenes/smartphones/units_measurement.svg "Grams, millimetres, volts, amps: every gadget on this desk reports a number with a unit.")

Kavya's new phone has finally arrived, and she and her cousin Dev unbox it on the dining table. Dev reads out the small print like a quiz master.

The charger: "Output $5\,\text{V}$, $2\,\text{A}$, $10\,\text{W}$. Fast charging at $9\,\text{V}$." The box: battery in "mAh", screen in inches, weight in grams, Wi-Fi at "$5\,\text{GHz}$".

"Volts, amps, watts, milliamp-hours, gigahertz, inches," Dev counts on his fingers. "Every gadget company just invents its own units. There must be fifty of them."

Kavya isn't so sure. Her physics teacher said last week that the whole of physics runs on a handful of units. But the label is right there, full of letters. Are volts and watts and hertz each a separate standard that someone had to define? Or are some of these secretly made out of the others?

## The physics

A **unit** is the agreed standard we compare a quantity against. "The phone weighs $185\,\text{g}$" means $185$ times one gram.

The **SI** (Système International) doesn't need a separate standard for every quantity. It picks seven **base quantities**, each with a **base unit**, and builds every other unit from them.

![A table of the seven SI base units: metre, kilogram, second, ampere, kelvin, mole and candela, with the constant that defines each](figures/si_units/seven-base-units.svg "Seven base units are enough for all of physics. Since 2019 each one is fixed by an exact value of a constant of nature, not by an object.")

Mechanics needs the **metre** (m), **kilogram** (kg) and **second** (s). A charger adds a fourth, the **ampere** (A), the unit of electric current; that's the "$2\,\text{A}$" on Kavya's label. The other three — kelvin, mole and candela — belong to heat, chemistry and light.

Since 20 May 2019, all seven are defined by fixing exact values of constants of nature: the second by a caesium-133 atom's frequency, the metre through the speed of light, the kilogram through the Planck constant, and the ampere through the charge of an electron. Before that, the kilogram was a *thing* — a platinum-iridium cylinder kept near Paris, with numbered copies in other countries.

![A small metal cylinder under two nested glass bell jars on a stand](famous/us-prototype-kilogram-k20.jpg "A NIST display replica of the US national prototype kilogram K20, itself a platinum-iridium copy of the international kilogram. Until 2019 the kilogram was defined by an object like this; now it is fixed through the Planck constant. Public domain, via Wikimedia Commons.")

An object can gain dust or lose atoms when it's cleaned. A constant of nature can't. That's why the SI moved away from objects.

Every other unit is a **derived unit**, built from base units by the equation that defines the quantity:

- force $=$ mass $\times$ acceleration: $1\,\text{N} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$
- energy (work) $=$ force $\times$ distance: $1\,\text{J} = 1\,\text{N}\,\text{m} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$
- power $=$ energy $\div$ time: $1\,\text{W} = 1\,\text{J/s} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$
- frequency $=$ cycles per second: $1\,\text{Hz} = 1\,\text{s}^{-1}$, so "$5\,\text{GHz}$" is $5 \times 10^9\,\text{s}^{-1}$
- charge $=$ current $\times$ time: $1\,\text{C} = 1\,\text{A}\,\text{s}$

![The newton, joule and watt shown as coloured blocks of kilogram, metre and second](figures/si_units/derived-units-from-base.svg "A named unit like the watt is shorthand for a product of base units. Build it from the equation that defines the quantity.")

So Dev's "fifty units" collapse. A milliamp-hour is a current times a time, which is a charge: $1\,\text{mAh} = 10^{-3}\,\text{A} \times 3600\,\text{s} = 3.6\,\text{C}$. The inch isn't an SI unit at all; it is defined through the metre as exactly $2.54\,\text{cm}$.

## Worked example

**Given:** the charger supplies $V = 5.0\,\text{V}$ at $I = 2.0\,\text{A}$ (the label's values).
**Find:** (a) its power, using $P = VI$ from Class 10; (b) the energy it delivers in $30$ minutes, in base units; (c) the volt in base units.

(a) $P = VI = 5.0\,\text{V} \times 2.0\,\text{A} = 10\,\text{W}$ — matching the label.

(b) Energy $=$ power $\times$ time, with $t = 30 \times 60 = 1800\,\text{s}$:

$$E = 10\,\text{W} \times 1800\,\text{s} = 18\,000\,\text{J} = 1.8 \times 10^4\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$$

(c) From $P = VI$, a volt is a watt per ampere:

$$1\,\text{V} = \frac{1\,\text{W}}{1\,\text{A}} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}\,\text{A}^{-1}$$

**Sanity check:** in (b), $\text{W} \times \text{s} = (\text{kg}\,\text{m}^2\,\text{s}^{-3}) \times \text{s} = \text{kg}\,\text{m}^2\,\text{s}^{-2}$, the joule, as energy must be.

## Where the picture breaks

A charger label is a rating, not a measurement: the phone decides how much current it actually draws, and that changes as the battery fills. Some units on the box are also conveniences outside the SI. The milliamp-hour is a legitimate charge unit but not a coherent SI one, and the inch belongs to an older system. Neither is a new standard; each is defined through SI units.

## Key takeaway

The SI has seven base units; mechanics uses the metre, kilogram and second, and electricity adds the ampere. Since 2019 all seven are fixed by constants of nature. Every other unit is derived through a defining equation: $1\,\text{N} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$, $1\,\text{J} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$, $1\,\text{W} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$.
