---
concept_id: si_units
interest: motorsport
format: explain
title: The spec sheet that speaks in kilowatts
check:
  question: |-
    A car's spec sheet gives its engine's peak power in kilowatts. Power is energy delivered per second. Written in SI base units, one watt is:
  options:
    A: |-
      $1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$
    B: |-
      $1\,\text{kg}\,\text{m}\,\text{s}^{-2}$
    C: |-
      $1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$
    D: |-
      $1\,\text{kg}\,\text{m}\,\text{s}^{-1}$
  answer: C
  explanation: |-
    $1\,\text{W} = 1\,\text{J/s}$, and $1\,\text{J} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$. Dividing by one more second gives $1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$.
  misconceptions:
    A: |-
      Stops at the joule. $\text{kg}\,\text{m}^2\,\text{s}^{-2}$ is energy; power is energy per second, so it needs one more $\text{s}^{-1}$.
    B: |-
      Confuses power with force. $\text{kg}\,\text{m}\,\text{s}^{-2}$ is the newton, which is a push, not a rate of delivering energy.
    D: |-
      Thinks power is mass times speed ("how hard the car is going"). $\text{kg}\,\text{m}\,\text{s}^{-1}$ is the unit of momentum.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A race track: a red race car crosses the start-finish line under a timing screen showing a lap time and a speed-trap reading, beside a braking marker and a marshal with a stopwatch](scenes/motorsport/units_measurement.svg "Lap time in seconds, speed in km/h, distances in metres: every reading at the track is a number with a unit.")

Kabir's aunt Farhana is a data engineer for a club racing team, and on track day she lets him sit on the pit wall. Between sessions she hands him the car's spec sheet. It is a jumble: engine power in *kilowatts*, torque in *newton metres*, top speed in *km/h*, mass in *kilograms*, fuel in *litres*.

"Why so many units?" Kabir asks. "Does each one have its own official standard somewhere?"

"Not really," Farhana says. "Nearly all of them are built from just three."

Kabir looks at the timing screen: $1{:}32.418$, a lap measured to a thousandth of a second. A thousandth of *what*, exactly? Somebody must have decided how long a second is, and how heavy a kilogram is. What did they compare them to — and how can a kilowatt be "built" out of anything?

## The physics

A **unit** is the agreed standard a quantity is compared against. A mass of $800\,\text{kg}$ means $800$ times one kilogram.

The **SI** (Système International) picks seven **base quantities**, each with a **base unit**, and builds every other unit from them.

![A table of the seven SI base units: metre, kilogram, second, ampere, kelvin, mole and candela, with the constant that defines each](figures/si_units/seven-base-units.svg "Seven base units cover all of physics. Since 2019 each is fixed by an exact value of a constant of nature.")

Mechanics needs three: the **metre** (m), the **kilogram** (kg) and the **second** (s). Today they are defined by constants of nature:

- the **second**: the caesium-133 atom's transition frequency is fixed at exactly $9\,192\,631\,770\,\text{Hz}$ — this is what the timing screen's thousandths ultimately trace back to;
- the **metre**: the distance light travels in vacuum in $1/299\,792\,458$ of a second;
- the **kilogram**: fixed through the Planck constant $h$, since 20 May 2019.

Before 2019 the kilogram *was* an object: a platinum-iridium cylinder kept near Paris, with numbered copies held by different countries.

![A metal cylinder under two nested glass bell jars on a stand](famous/us-prototype-kilogram-k20.jpg "A display replica of K20, the US copy of the kilogram prototype. An object can gain grime or lose atoms; a constant of nature cannot, so since 2019 the kilogram is defined through the Planck constant. Public domain, via Wikimedia Commons.")

Everything else on Farhana's sheet is a **derived unit**, built from base units through the equation that defines the quantity:

$$\text{force} = \text{mass} \times \text{acceleration} \;\Rightarrow\; 1\,\text{N} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$$

$$\text{work} = \text{force} \times \text{distance} \;\Rightarrow\; 1\,\text{J} = 1\,\text{N}\,\text{m} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$$

$$\text{power} = \frac{\text{work}}{\text{time}} \;\Rightarrow\; 1\,\text{W} = 1\,\text{J/s} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$$

![The newton, joule and watt shown as coloured blocks of kilogram, metre and second](figures/si_units/derived-units-from-base.svg "A named unit is shorthand for a product of base units. The watt is a joule divided by one more second.")

So the engine's "kilowatts" are thousands of $\text{kg}\,\text{m}^2\,\text{s}^{-3}$. The km/h and litres on the sheet are not SI units at all; they are accepted everyday units defined through the metre and second.

## Worked example

**Given:** a car of mass $m = 800\,\text{kg}$ reaches $v = 50\,\text{m/s}$ from rest in $t = 10\,\text{s}$ (illustrative values).
**Find:** its kinetic energy $\tfrac{1}{2}mv^2$, and the average power needed to give it that energy, in base units.

$$E = \tfrac{1}{2} \times 800\,\text{kg} \times (50\,\text{m/s})^2 = 400 \times 2500\,\text{kg}\,\text{m}^2\,\text{s}^{-2} = 1.0 \times 10^6\,\text{J}$$

$$P = \frac{E}{t} = \frac{1.0 \times 10^6\,\text{kg}\,\text{m}^2\,\text{s}^{-2}}{10\,\text{s}} = 1.0 \times 10^5\,\text{kg}\,\text{m}^2\,\text{s}^{-3} = 100\,\text{kW}$$

**Sanity check:** dividing a joule by a second adds one $\text{s}^{-1}$, giving exactly the watt built above. And $100\,\text{kW}$ is a believable figure for a quick road car.

## Where the picture breaks

The worked example ignores air drag and friction, so the real engine must deliver more than $100\,\text{kW}$ on average; the calculation gives only the energy that ends up as motion. The spec sheet also mixes in non-SI units: km/h (divide by $3.6$ for m/s), litres ($10^{-3}\,\text{m}^3$), and sometimes horsepower, which isn't SI at all. And the timing screen's thousandths are only as good as its clock's calibration — the caesium definition is the reference, not something inside the timing box.

## Key takeaway

The SI has seven base units; mechanics uses the metre, kilogram and second, all now defined by fixed constants of nature. Every other unit is derived through a defining equation: $1\,\text{N} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$, $1\,\text{J} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$ and $1\,\text{W} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$.
