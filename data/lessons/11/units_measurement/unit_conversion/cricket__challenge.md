---
concept_id: unit_conversion
interest: cricket
format: challenge
title: Measuring a delivery in gully units
check:
  question: |-
    In the gully system, the unit of length is $20\,\text{m}$, the unit of mass is $0.16\,\text{kg}$ and the unit of time is $0.5\,\text{s}$. A force of $1\,\text{N}$ is how many gully units of force?
  options:
    A: |-
      $12.8$
    B: |-
      $0.156$
    C: |-
      $0.313$
    D: |-
      $0.0781$
  answer: D
  explanation: |-
    Force is $[\text{M}\,\text{L}\,\text{T}^{-2}]$: $n_2 = 1 \times \left(\tfrac{1}{0.16}\right) \left(\tfrac{1}{20}\right) \left(\tfrac{1}{0.5}\right)^{-2} = 6.25 \times 0.05 \times 0.25 = 0.0781$. Check: one gully force unit is $0.16 \times 20/0.5^2 = 12.8\,\text{N}$, and $1/12.8 = 0.0781$.
  misconceptions:
    A: |-
      Inverts the conversion: $12.8$ is the size of one gully unit in newtons, so $1\,\text{N}$ is $1/12.8$ of a gully unit, not $12.8$ of them.
    B: |-
      Raises the time ratio to the power $-1$ instead of $-2$, as if force had dimensions $[\text{M}\,\text{L}\,\text{T}^{-1}]$ (that is momentum).
    C: |-
      Leaves out the time ratio altogether, converting only mass and length.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch as 20.12 metres; a ball sits on a scale and a stopwatch runs](scenes/cricket/units_measurement.svg "A pitch for length, a ball for mass, a delivery for time. Why not build units from them?")

Nikita and Omkar are writing questions for their school's physics quiz, and they have an idea for a fun round: **gully units**, a system built entirely from cricket.

- 1 *pitch* $= 20\,\text{m}$ (the real pitch, $20.12\,\text{m}$, rounded);
- 1 *ball* $= 0.16\,\text{kg}$ (a cricket ball's mass, rounded);
- 1 *tick* $= 0.5\,\text{s}$ (about the time a fast delivery takes to reach the batter).

Omkar writes the first question: *A fast delivery has $128\,\text{J}$ of kinetic energy. What is that in gully units?*

Nikita tries it and gets $256$. Omkar gets $10$. Neither is sure, and a quiz question with two answers is a disaster. How do you convert an energy into a system of units that nobody has ever used?

## The challenge

Using the gully units above (length $20\,\text{m}$, mass $0.16\,\text{kg}$, time $0.5\,\text{s}$):

1. How many gully units of energy is $1\,\text{J}$?
2. So what is $128\,\text{J}$ in gully units?

The dimensional formula of energy is $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$.

## Think first

Nikita's $256$ and Omkar's $10$ can't both be right; maybe neither is. Should the number get bigger or smaller when you move to gully units? Are the gully units bigger or smaller than the SI ones? And does the length ratio need squaring? Guess before you work.

## The reveal

Use $n_2 = n_1 (M_1/M_2)^a (L_1/L_2)^b (T_1/T_2)^c$ with $a = 1$, $b = 2$, $c = -2$. System 1 is SI; system 2 is gully.

$$\frac{M_1}{M_2} = \frac{1\,\text{kg}}{0.16\,\text{kg}} = 6.25 \qquad \frac{L_1}{L_2} = \frac{1\,\text{m}}{20\,\text{m}} = 0.05 \qquad \frac{T_1}{T_2} = \frac{1\,\text{s}}{0.5\,\text{s}} = 2$$

For $1\,\text{J}$:

$$n_2 = 1 \times 6.25 \times (0.05)^2 \times (2)^{-2} = 6.25 \times 0.0025 \times 0.25 = 0.00390625$$

So $1\,\text{J} \approx 3.91 \times 10^{-3}$ gully units, and

$$128\,\text{J} = 128 \times 0.00390625 = 0.5 \text{ gully units}$$

**Two independent checks.** First, the size of one gully energy unit in joules is $0.16 \times 20^2 / 0.5^2 = 0.16 \times 400/0.25 = 256\,\text{J}$. Then $128\,\text{J} = 128/256 = 0.5$ units. That's where Nikita's $256$ came from: she found the size of the new unit and stopped, instead of dividing by it.

Second, work entirely in gully units. The ball's mass is exactly 1 *ball*. Its speed, $40\,\text{m/s}$, is $40 \times 0.5/20 = 1$ *pitch per tick*. So its kinetic energy is $\tfrac{1}{2} \times 1 \times 1^2 = 0.5$ gully units. All three routes agree.

Omkar's $10$ came from using $(0.05)^1$ instead of $(0.05)^2$: $128 \times 6.25 \times 0.05 \times 0.25 = 10$. He forgot that energy contains length squared. That would be the right factor for a force, $[\text{M}\,\text{L}\,\text{T}^{-2}]$, not for an energy.

![A one-metre square divided into a ten by ten grid and a one-metre cube, showing why squared and cubed units need squared and cubed conversion factors](figures/unit_conversion/area-volume-conversion.svg "Whenever a base unit appears squared or cubed in a quantity, its conversion ratio must be squared or cubed too.")

## The physics

A quantity is $Q = n_1 u_1 = n_2 u_2$. If its dimensional formula is $[\text{M}^a\,\text{L}^b\,\text{T}^c]$, then

$$n_2 = n_1 \left[\frac{M_1}{M_2}\right]^a \left[\frac{L_1}{L_2}\right]^b \left[\frac{T_1}{T_2}\right]^c$$

This works between **any** two systems — SI, CGS, or one you invent — as long as you know the sizes of their base units. The bigger the new unit, the smaller the number. Every base-unit ratio carries exactly the power it has in the dimensional formula; forgetting a power, or using a ratio upside down, are the two classic errors.

## Key takeaway

To convert a quantity into any unit system, raise each base-unit ratio to its power in the dimensional formula: $n_2 = n_1 (M_1/M_2)^a (L_1/L_2)^b (T_1/T_2)^c$. Check by finding the size of the new unit directly: here $1$ gully energy unit $= 256\,\text{J}$, so $128\,\text{J} = 0.5$ units.
