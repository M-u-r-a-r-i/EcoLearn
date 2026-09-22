---
concept_id: si_units
interest: cricket
format: misconception
title: Is every cricket ball weighed against a cylinder in Paris
check:
  question: |-
    An umpire weighs a new ball on a digital scale before a match. Since 20 May 2019, what defines the kilogram that the scale's reading ultimately traces back to?
  options:
    A: |-
      A fixed, exact value of the Planck constant $h$
    B: |-
      A platinum-iridium cylinder kept in a vault near Paris
    C: |-
      The mass of one litre of water at $4\,^\circ\text{C}$
    D: |-
      The mass of the country's own national copy of the kilogram
  answer: A
  explanation: |-
    Since 2019 the kilogram is defined by fixing $h = 6.626\,070\,15 \times 10^{-34}\,\text{kg}\,\text{m}^2\,\text{s}^{-1}$ exactly. With the metre and second already defined, that pins down the kilogram.
  misconceptions:
    B: |-
      Holds the pre-2019 definition. The international prototype defined the kilogram from 1889 to 2019; it is now a historical object.
    C: |-
      Uses the 18th-century idea that a kilogram is the mass of a litre of water — a convenient approximation, but never the modern definition.
    D: |-
      Thinks each country's copy is the standard. National copies were only ever copies, calibrated against the international prototype, and today they are calibrated against the constant-based definition.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch while a ball sits on a digital scale reading 158.0 grams](scenes/cricket/units_measurement.svg "Before the toss, the new ball goes on the scale.")

Riya's uncle is umpiring a league match, and she's allowed into the umpires' room before the toss. He places the new ball on a small digital scale: $158.0\,\text{g}$. "Legal," he says. A men's ball must be between $155.9\,\text{g}$ and $163\,\text{g}$.

Her brother Siddharth, who has just started Class 11, is showing off. "You know that scale only works because of a metal cylinder in Paris. That cylinder *is* the kilogram. If somebody scratched it, every cricket ball in the world would suddenly weigh a bit more."

The umpire laughs, but he doesn't disagree. Riya isn't sure. Would one scratch in Paris really change the ball in her uncle's hand? And if not — what is a kilogram?

## The common belief

"Units are defined by master objects kept safe in a vault. The kilogram *is* a particular metal cylinder near Paris, and the metre *is* a particular metal bar. Every scale and every ruler in the world is ultimately a copy of those objects."

## Why it feels right

For most of the history of the SI, this was true. From 1889 until 2019, the kilogram was defined as the mass of the International Prototype Kilogram, a platinum-iridium cylinder kept near Paris. Countries received numbered copies. The one below, K20, is the United States' copy.

![A small metal cylinder sitting under two nested glass bell jars](famous/us-prototype-kilogram-k20.jpg "A display replica of national prototype kilogram K20, the US platinum-iridium copy of the international prototype. Such cylinders defined the kilogram until 2019; now they are history. Public domain, via Wikimedia Commons.")

The metre had a similar story: from 1889 it was the length of a metal bar, and countries held copies such as Bar No. 27.

![A platinum-iridium metre bar with an X-shaped cross-section, resting in its case](famous/us-prototype-metre-bar-27.jpg "Prototype Metre Bar No. 27 (1889). The metre was defined by a bar like this until 1960. Public domain, via Wikimedia Commons.")

Many older books still describe these objects as the definitions, so Siddharth's belief has a solid source. And his worry was real: when the prototype defined the kilogram, it was exactly $1\,\text{kg}$ by definition, whatever happened to it.

## What actually happens

Siddharth's worry is exactly why the definitions changed. Careful comparisons over the twentieth century showed that the prototype and its copies had drifted apart by tens of micrograms. Nobody could say which one had changed, because the prototype was the definition.

So the SI now defines units by constants of nature, which are the same everywhere and don't wear out:

- the **second**: the caesium-133 transition frequency is fixed at exactly $9\,192\,631\,770\,\text{Hz}$ (since 1967);
- the **metre**: the speed of light is fixed at exactly $299\,792\,458\,\text{m/s}$ (since 1983);
- the **kilogram**: the Planck constant is fixed at exactly $6.626\,070\,15 \times 10^{-34}\,\text{J}\,\text{s}$ (since 20 May 2019).

A scratch in Paris would change nothing today. The umpire's scale is calibrated against reference masses, and those are traceable to the constant-based definition. The ball weighs $158.0\,\text{g}$ whatever happens to any cylinder.

## The physics

The SI has seven **base units** — metre, kilogram, second, ampere, kelvin, mole, candela — and since 20 May 2019 every one is defined by fixing the numerical value of a constant. All other units are **derived** from these.

![A table of the seven SI base units with the constant that defines each](figures/si_units/seven-base-units.svg "Every base unit, including the kilogram, is now fixed by a constant, not an object.")

The misconception confuses a **standard object** (a good way to *realise* a unit in a lab, then and now) with the **definition** of the unit. Objects are still used to calibrate scales; they just no longer define the kilogram.

## Worked example

How can a constant define a mass? Look at the unit of $h$. The joule is $\text{kg}\,\text{m}^2\,\text{s}^{-2}$, so

$$\text{J}\,\text{s} = \text{kg}\,\text{m}^2\,\text{s}^{-2} \times \text{s} = \text{kg}\,\text{m}^2\,\text{s}^{-1}$$

Fixing $h$ fixes the number of $\text{kg}\,\text{m}^2\,\text{s}^{-1}$ it contains. Since the metre and the second are already fixed by $c$ and the caesium frequency, the only thing left free is the kilogram — so it is pinned down. That is why the unit analysis matters: the kilogram's definition only works because $h$'s unit contains $\text{kg}$ exactly once.

## Key takeaway

Since 20 May 2019, no SI unit is defined by an object. The kilogram is fixed by the Planck constant, the metre by the speed of light and the second by caesium. The famous cylinders and bars are history — excellent copies once, definitions no longer.
