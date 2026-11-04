---
concept_id: si_units
interest: football
format: explain
title: Who decided how far away the penalty spot is
check:
  question: |-
    A striker's boot pushes the ball with an average force of a few hundred newtons. Written in SI base units, one newton is:
  options:
    A: |-
      $1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$
    B: |-
      $1\,\text{kg}\,\text{m}\,\text{s}^{-1}$
    C: |-
      $1\,\text{kg}\,\text{m}\,\text{s}^{-2}$
    D: |-
      $1\,\text{g}\,\text{cm}\,\text{s}^{-2}$
  answer: C
  explanation: |-
    Force is mass times acceleration, and acceleration is $(\text{m/s})/\text{s} = \text{m}\,\text{s}^{-2}$. So $1\,\text{N} = 1\,\text{kg} \times 1\,\text{m}\,\text{s}^{-2} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$.
  misconceptions:
    A: |-
      Confuses the newton with the joule. $\text{kg}\,\text{m}^2\,\text{s}^{-2}$ is force times distance, the unit of work and energy.
    B: |-
      Multiplies mass by velocity instead of acceleration; $\text{kg}\,\text{m}\,\text{s}^{-1}$ is the unit of momentum, not force.
    D: |-
      Uses CGS units (gram, centimetre). That combination is the dyne, which is $10^{-5}\,\text{N}$, not the SI newton.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures the width of a goal with a tape while a match ball sits on a scale beside a pressure gauge and a match clock](scenes/football/units_measurement.svg "A tape, a scale, a gauge, a clock: every instrument at the ground reports a number with a unit.")

The evening before the district final, Ananya helps Thomas-uncle, her school's groundsman, repaint the penalty spot. He walks out from the goal line with his old cloth tape, the kind marked in feet and yards. "Twelve yards," he says, and presses a peg into the grass.

Ananya checks with the metre tape from the physics lab: $10.97\,\text{m}$. The rulebook on her phone says the penalty mark is $11\,\text{m}$ from the goal line. Close enough — they agree.

Then she frowns. His tape is in yards, hers is in metres, and her coach keeps saying a good shot needs "hundreds of newtons" of force from the boot. Somebody must have decided how long a metre is, and what a newton even means. Who decided — and what did they compare it with? If a metre is just "the length of some stick", what happens when the stick changes?

## The physics

A **unit** is the agreed standard you compare a quantity against. "The penalty mark is $11\,\text{m}$ away" means that distance is $11$ times the length of one metre.

Physics doesn't need a separate standard for every quantity. The **SI** (Système International) picks seven **base quantities**, each with a **base unit**, and builds everything else from them.

![A table of the seven SI base units: metre, kilogram, second, ampere, kelvin, mole and candela, with the constant that defines each](figures/si_units/seven-base-units.svg "Seven base units are enough for all of physics. Since 2019, each is fixed by an exact value of a constant of nature, not by an object.")

In mechanics you need three: the **metre** (m) for length, the **kilogram** (kg) for mass and the **second** (s) for time. Today each is defined by a constant of nature:

- the **second**: the frequency of a particular transition of the caesium-133 atom is fixed at exactly $9\,192\,631\,770\,\text{Hz}$ (since 1967);
- the **metre**: the speed of light in vacuum is fixed at exactly $299\,792\,458\,\text{m/s}$, so a metre is the distance light travels in $1/299\,792\,458$ of a second (since 1983);
- the **kilogram**: the Planck constant $h$ is fixed at an exact value (since 20 May 2019).

It wasn't always like this. From 1889 the metre was the length of a platinum-iridium bar kept near Paris, and countries held numbered copies of it.

![A platinum-iridium metre bar with an X-shaped cross-section, resting in its case](famous/us-prototype-metre-bar-27.jpg "Prototype Metre Bar No. 27 (1889), a copy of the international metre bar. Bars like this defined the metre until 1960. Public domain, via Wikimedia Commons.")

A bar can expand when warm, get scratched, or be lost. The speed of light can't. That is exactly Ananya's worry, and it is why the SI moved from objects to constants.

Every other unit is a **derived unit**, built from base units through the equation that defines the quantity:

$$\text{force} = \text{mass} \times \text{acceleration} \;\Rightarrow\; 1\,\text{N} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$$

$$\text{work} = \text{force} \times \text{distance} \;\Rightarrow\; 1\,\text{J} = 1\,\text{N}\,\text{m} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$$

![The newton, joule and watt shown as coloured blocks of kilogram, metre and second](figures/si_units/derived-units-from-base.svg "A named unit like the newton is shorthand for a product of base units, read off from the quantity's defining equation.")

So the coach's "hundreds of newtons" is really "hundreds of $\text{kg}\,\text{m}\,\text{s}^{-2}$" — a name, not a new standard.

## Worked example

**Given:** a match ball of mass $m = 0.43\,\text{kg}$ leaves the boot at $v = 25\,\text{m/s}$ (illustrative values).
**Find:** its kinetic energy $\tfrac{1}{2}mv^2$, and show its unit is the joule in base units.

$$E = \tfrac{1}{2} \times 0.43\,\text{kg} \times (25\,\text{m/s})^2 = 0.215 \times 625\,\text{kg}\,\text{m}^2\,\text{s}^{-2} \approx 134\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$$

The unit $\text{kg}\,\text{m}^2\,\text{s}^{-2}$ is exactly the joule built above from $\text{N} \times \text{m}$, so $E \approx 134\,\text{J}$.

**Sanity check:** two routes, mass × speed² and force × distance, give the same base-unit combination — as they must if both describe energy.

## Where the picture breaks

Thomas-uncle's tape and Ananya's tape are tools, not definitions; each is only as good as its calibration, which traces back through other instruments to the SI definitions. Football's Laws give both metric and imperial values, rounded: $12\,\text{yd}$ is exactly $10.9728\,\text{m}$ (a yard is defined as exactly $0.9144\,\text{m}$), while the Laws say $11\,\text{m}$. The yard is not an SI unit; it is now defined *through* the metre.

## Key takeaway

The SI has seven base units; mechanics uses the metre, kilogram and second. Since 2019 all seven are defined by fixing constants of nature, not by objects. Every other unit is derived through a defining equation: $1\,\text{N} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$, $1\,\text{J} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$.
