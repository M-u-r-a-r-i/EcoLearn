---
concept_id: si_units
interest: gaming
format: explain
title: Why the hero floated down like a feather
check:
  question: |-
    A gaming PC's graphics card draws about $200\,\text{W}$ while a game runs. One watt is one joule per second. Written in SI base units, one watt is:
  options:
    A: |-
      $1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$
    B: |-
      $1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$
    C: |-
      $1\,\text{kg}\,\text{m}\,\text{s}^{-3}$
    D: |-
      $1\,\text{kg}\,\text{m}^2\,\text{s}^{-1}$
  answer: A
  explanation: |-
    $1\,\text{J} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$, and a watt is a joule divided by a second: $\text{kg}\,\text{m}^2\,\text{s}^{-2} \div \text{s} = \text{kg}\,\text{m}^2\,\text{s}^{-3}$.
  misconceptions:
    B: |-
      Confuses power with energy: $\text{kg}\,\text{m}^2\,\text{s}^{-2}$ is the joule. Power is energy per second, so it needs one more factor of $\text{s}^{-1}$.
    C: |-
      Builds the joule from the newton but forgets that work is force times a distance, so one metre is missing before dividing by the second.
    D: |-
      Multiplies the joule by a second instead of dividing by it, so the power of $\text{s}$ goes up instead of down.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk: a monitor showing a racing game, a tape measure across the screen, a controller on a kitchen scale and a phone running a reaction test](scenes/gaming/units_measurement.svg "Every readout on this desk is a number with a unit: km/h, frames per second, kilograms, seconds, centimetres.")

Kavya has spent three weekends building her first platform game for the school coding club. The hero runs, the hero jumps — and then the hero drifts back down like a feather in slow motion.

She checks her code. `gravity = 9.8`. "That's the real value," she tells Dev, who is playtesting on the club laptop. "Textbook number."

Dev scrolls through the engine's settings. "Your engine measures lengths in *pixels*," he says. "So you've told it gravity is $9.8$ pixels per second per second. Your hero is about $64$ pixels tall. You've built a world with almost no gravity."

Kavya stares at the line of code. The number was right. The game is wrong. So what does "$9.8$" actually mean on its own — and who decided what a metre, a kilogram or a second is in the first place?

## The physics

A number on its own says nothing about a quantity. A **unit** is the agreed standard you compare the quantity against: $g = 9.8\,\text{m/s}^2$ means "$9.8$ metres per second, gained every second". Change the unit and the same number describes a completely different world, which is exactly Kavya's bug.

The **SI** (Système International) picks seven **base quantities**, each with a **base unit**, and builds every other unit from them.

![A table of the seven SI base units: metre, kilogram, second, ampere, kelvin, mole and candela, with the constant that defines each](figures/si_units/seven-base-units.svg "Seven base units cover all of physics. Since 2019 each is fixed by an exact value of a constant of nature.")

Mechanics needs three: the **metre** (m), the **kilogram** (kg) and the **second** (s). Today they are defined by constants of nature:

- the **second**, by the frequency of a particular transition of the caesium-133 atom, fixed at exactly $9\,192\,631\,770\,\text{Hz}$;
- the **metre**, as the distance light travels in vacuum in $1/299\,792\,458$ of a second;
- the **kilogram**, through an exact value of the Planck constant $h$ (since 20 May 2019).

Before 2019, the kilogram *was* an object: a platinum-iridium cylinder kept near Paris, with numbered national copies around the world.

![A small metal cylinder under two glass bell jars on a stand](famous/us-prototype-kilogram-k20.jpg "Kilogram K20, the US national copy of the old prototype kilogram. An object can gain grime or lose atoms; a constant of nature can't, which is why the definition changed. Public domain, via Wikimedia Commons.")

All other units are **derived units**, built from the base units through the equation that defines the quantity:

$$\text{force} = \text{mass} \times \text{acceleration} \;\Rightarrow\; 1\,\text{N} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$$

$$\text{work} = \text{force} \times \text{distance} \;\Rightarrow\; 1\,\text{J} = 1\,\text{N}\,\text{m} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$$

$$\text{power} = \frac{\text{work}}{\text{time}} \;\Rightarrow\; 1\,\text{W} = 1\,\text{J}\,\text{s}^{-1} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$$

![The newton, joule and watt shown as coloured blocks of kilogram, metre and second](figures/si_units/derived-units-from-base.svg "A named unit is shorthand for a product of base units. Read the recipe off the defining equation.")

## Worked example

**Given:** Kavya decides one engine unit is one metre, gives her hero a mass of $m = 60\,\text{kg}$ and sets $g = 9.8\,\text{m/s}^2$ (illustrative values).
**Find:** (a) the hero's weight in newtons and in base units; (b) the work needed to lift the hero through a $2.0\,\text{m}$ jump.

(a) Weight is mass times the acceleration due to gravity:

$$W = mg = 60\,\text{kg} \times 9.8\,\text{m}\,\text{s}^{-2} = 588\,\text{kg}\,\text{m}\,\text{s}^{-2} = 588\,\text{N}$$

(b) Work is force times distance:

$$W_\text{lift} = 588\,\text{N} \times 2.0\,\text{m} = 1176\,\text{N}\,\text{m} \approx 1.2 \times 10^3\,\text{J}$$

and $\text{N}\,\text{m} = (\text{kg}\,\text{m}\,\text{s}^{-2})(\text{m}) = \text{kg}\,\text{m}^2\,\text{s}^{-2}$, the joule.

**Sanity check:** $588\,\text{N}$ is about $600\,\text{N}$, the familiar weight of an adult; and $600 \times 2 = 1200$, matching (b).

## Where the picture breaks

A game engine is not a measuring instrument. Its "units" are whatever the programmer declares, and the engine never checks them — it just multiplies numbers. That is why Kavya's bug happened silently: the code has no idea whether $9.8$ means metres, pixels or nothing at all. Real SI units are different: they are fixed by constants of nature and every calibrated instrument traces back to them. The game only *borrows* the metre by agreement.

## Key takeaway

The SI has seven base units; mechanics uses the metre, kilogram and second, all defined today by constants of nature. Every other unit is derived from them: $1\,\text{N} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$, $1\,\text{J} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$, $1\,\text{W} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$. A number without its unit means nothing.
