---
concept_id: dimensional_formulae
interest: football
format: misconception
title: Does a shot in kilometres per hour have different dimensions
check:
  question: |-
    A broadcast shows a shot's speed as $108\,\text{km/h}$. What is the dimensional formula of this speed?
  options:
    A: |-
      $[\text{km}\,\text{h}^{-1}]$
    B: |-
      $[3.6\,\text{L}\,\text{T}^{-1}]$
    C: |-
      $[\text{L}\,\text{T}^{-1}]$
    D: |-
      $[\text{L}\,\text{T}]$
  answer: C
  explanation: |-
    A speed is a length divided by a time, whatever units it is written in. Kilometres are a length [L] and hours are a time [T], so the dimensional formula is $[\text{L}\,\text{T}^{-1}]$ — the same as for $30\,\text{m/s}$.
  misconceptions:
    A: |-
      Writes the units instead of the dimensions. Dimensions name the kind of quantity (length, time), not the particular unit chosen to measure it.
    B: |-
      Carries a conversion factor into the dimensional formula. Numbers like $3.6$ change the size of the unit, not the kind of quantity, so they never appear in dimensions.
    D: |-
      Reads "per hour" as "times an hour". Dividing by a time gives a power of $-1$ on T, not $+1$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal 7.32 metres wide with a tape; a match clock runs above](scenes/football/units_measurement.svg "Metres on the tape, minutes on the clock. Change the units, and what stays the same?")

Samar and his cousin Nandini are watching a league match on two screens — the TV broadcast on one, an overseas stream on her laptop. A striker lets fly from twenty-five metres. The TV graphic flashes *108 km/h*; the overseas stream says *67 mph*.

Nandini has her physics homework open: *write the dimensional formula of speed.*

"Easy," Samar says. "Which speed, though? On TV it's $[\text{km}\,\text{h}^{-1}]$. On your stream it's $[\text{mi}\,\text{h}^{-1}]$. In our book it's $[\text{m}\,\text{s}^{-1}]$. Three different dimensional formulas. And to convert km/h to m/s you divide by $3.6$, so the $3.6$ must be in there somewhere too."

Nandini stares at her homework. The book gives only one answer. But the TV and the stream really do show different numbers, in different units, for the same shot. Is the book being lazy — or is Samar mixing up two different ideas?

## The common belief

"Dimensions depend on the units. A speed in km/h has different dimensions from a speed in m/s, and the conversion factor between them is part of the dimensional formula."

## Why it feels right

The words *unit* and *dimension* are both used for "what a quantity is measured in", and many people use them loosely. The numbers on the two screens really are different, so it feels as if the quantities must differ somehow. And converting between units does need numbers like $3.6$ or $1609$, which look as if they belong in the formula.

Part of Samar's instinct is right: the **numbers** and the **units** really do change from screen to screen. That's exactly what a change of units does.

## What actually happens

The shot had one speed. Check that all three screens agree (a mile is exactly $1609.344\,\text{m}$):

$$108\,\text{km/h} = \frac{108\,000\,\text{m}}{3600\,\text{s}} = 30\,\text{m/s} \qquad 30\,\text{m/s} = \frac{30 \times 3600}{1609.344}\,\text{mph} \approx 67\,\text{mph}$$

Kilometres, miles and metres are all **lengths**; hours and seconds are all **times**. The units are different-sized measuring sticks for the same two kinds of quantity. The dimensional formula records only the *kinds*:

$$[\text{speed}] = \frac{[\text{L}]}{[\text{T}]} = [\text{L}\,\text{T}^{-1}]$$

on every screen. The $3.6$ is the ratio between two unit sizes — a number, and numbers are dimensionless, so it can't appear in a dimensional formula. Samar's $[\text{km}\,\text{h}^{-1}]$ isn't a dimensional formula at all; it's a unit.

## The physics

The **dimensional formula** of a quantity gives the powers of the base quantities in it — $[\text{M}]$, $[\text{L}]$, $[\text{T}]$ in mechanics — found from its defining equation. It says what **kind** of quantity something is. A **unit** is a chosen standard of a particular size used to measure it.

![A ladder of quantities from velocity to power with their dimensional formulas](figures/dimensional_formulae/dimension-building-blocks.svg "No units appear on this ladder, only M, L and T. Velocity is [L T⁻¹] in any unit system.")

- One dimensional formula, many possible units: $[\text{L}\,\text{T}^{-1}]$ can be m/s, km/h or mph.
- Pure numbers — conversion factors, $\tfrac{1}{2}$, $\pi$ — never appear in dimensions.
- Because the dimensions don't change, they can be used to *convert* between units; that's a later concept in this chapter.

## Worked example

**Given:** a winger accelerates from rest to $18\,\text{km/h}$ in $2.0\,\text{s}$ (illustrative).
**Find:** the dimensional formula of this acceleration, and its value in $\text{m/s}^2$.

The acceleration in mixed units is $18\,\text{km/h}$ per $2.0\,\text{s}$, i.e. $9.0\,\text{km}\,\text{h}^{-1}\,\text{s}^{-1}$. It looks odd — two different time units — but hours and seconds are both $[\text{T}]$:

$$[a] = \frac{[\text{L}]}{[\text{T}][\text{T}]} = [\text{L}\,\text{T}^{-2}]$$

In SI: $18\,\text{km/h} = 5.0\,\text{m/s}$, so $a = 5.0/2.0 = 2.5\,\text{m/s}^2$.

**Sanity check:** $\text{m/s}^2$ is a length over a time squared, $[\text{L}\,\text{T}^{-2}]$ — the same dimensions as the mixed-unit version, as it must be.

## Key takeaway

Dimensions describe the *kind* of quantity; units describe the *size of the measuring stick*. A speed is $[\text{L}\,\text{T}^{-1}]$ whether it's shown in km/h, mph or m/s, and conversion factors like $3.6$ never appear in a dimensional formula.
