---
concept_id: si_units
interest: cricket
format: explain
title: Who decided how long the pitch is
check:
  question: |-
    After a net session, the coach says a cricket ball ($0.16\,\text{kg}$) bowled at $30\,\text{m/s}$ has kinetic energy $\tfrac{1}{2}mv^2 = 72\,\text{J}$. Written in SI base units, one joule is:
  options:
    A: |-
      $1\,\text{kg}\,\text{m}\,\text{s}^{-2}$
    B: |-
      $1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$
    C: |-
      $1\,\text{kg}\,\text{m}\,\text{s}^{-1}$
    D: |-
      $1\,\text{g}\,\text{cm}^2\,\text{s}^{-2}$
  answer: B
  explanation: |-
    Energy is mass times speed squared: $\text{kg} \times (\text{m/s})^2 = \text{kg}\,\text{m}^2\,\text{s}^{-2}$. The same comes from work $=$ force $\times$ distance: $\text{N} \times \text{m} = (\text{kg}\,\text{m}\,\text{s}^{-2}) \times \text{m}$.
  misconceptions:
    A: |-
      Confuses the joule with the newton: $\text{kg}\,\text{m}\,\text{s}^{-2}$ is the unit of force. Energy is force times a distance, so it has one more metre.
    C: |-
      Uses mass times speed instead of mass times speed squared; $\text{kg}\,\text{m}\,\text{s}^{-1}$ is the unit of momentum, not energy.
    D: |-
      Uses CGS units (gram, centimetre) — that combination is the erg, which is $10^{-7}\,\text{J}$, not an SI base-unit expression.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch between the stumps with a tape while a ball sits on a scale and a speed display glows](scenes/cricket/units_measurement.svg "A tape, a scale, a stopwatch, a speed display: every one of them reports a number with a unit.")

The morning before the inter-school final, Tanvi helps her grandfather mark out the pitch. Venkatesh-thatha was a groundsman for thirty years, and he still carries his old steel chain. "Twenty-two yards," he says, laying it from stump to stump. "One chain. Surveyors used chains exactly this long, and so the pitch is one chain long."

Tanvi checks it with her school's metre tape: $20.12\,\text{m}$. They agree.

Then she frowns. Her chain is in yards, her tape is in metres, and last night's physics homework said the bat hits the ball with thousands of *newtons*. Somebody had to decide how long a yard is, how long a metre is, and what a newton even means. Who decided — and what did they compare it to? If a metre is just "the length of a stick somewhere", what happens when the stick changes?

## The physics

A **unit** is the agreed standard we compare a quantity against. Saying the pitch is $20.12\,\text{m}$ means it is $20.12$ times the length of one metre.

Physics does not need a separate standard for every quantity. The **SI** (Système International) chooses seven **base quantities** with seven **base units**, and builds everything else from them.

![A table of the seven SI base units: metre, kilogram, second, ampere, kelvin, mole and candela, with the constant that defines each](figures/si_units/seven-base-units.svg "Seven base units are enough for all of physics. Since 2019 each one is fixed by an exact value of a constant of nature, not by an object.")

For mechanics you mostly need three: the **metre** (m) for length, the **kilogram** (kg) for mass and the **second** (s) for time.

How are they defined? Today, by constants of nature:

- the **second** is fixed by the frequency of a particular transition in the caesium-133 atom, set at exactly $9\,192\,631\,770\,\text{Hz}$;
- the **metre** is the distance light travels in vacuum in $1/299\,792\,458$ of a second, because the speed of light is fixed at exactly $299\,792\,458\,\text{m/s}$ (since 1983);
- the **kilogram** is fixed through the Planck constant $h$ (since 20 May 2019).

It wasn't always so. From 1889 the metre was the length of a platinum-iridium bar kept near Paris, and countries kept numbered copies of it.

![A platinum-iridium metre bar with an X-shaped cross-section, resting in its case](famous/us-prototype-metre-bar-27.jpg "Prototype Metre Bar No. 27 (1889), a copy of the international metre bar; it was the US length standard until 1960. Today the metre is defined through the speed of light, not a bar. Public domain, via Wikimedia Commons.")

A bar can expand, get scratched, or be lost. The speed of light can't. That is why the SI moved from objects to constants.

Every other unit is a **derived unit**, built from base units by the equation that defines the quantity:

$$\text{force} = \text{mass} \times \text{acceleration} \;\Rightarrow\; 1\,\text{N} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$$

$$\text{work} = \text{force} \times \text{distance} \;\Rightarrow\; 1\,\text{J} = 1\,\text{N}\,\text{m} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$$

![The newton, joule and watt shown as coloured blocks of kilogram, metre and second](figures/si_units/derived-units-from-base.svg "A named unit like the newton is shorthand for a product of base units. Build it from the equation that defines the quantity.")

So Tanvi's "thousands of newtons" is really "thousands of $\text{kg}\,\text{m}\,\text{s}^{-2}$" — a name, not a new standard.

## Worked example

**Given:** a ball of mass $m = 0.16\,\text{kg}$ moving at $v = 30\,\text{m/s}$ (illustrative values).
**Find:** its kinetic energy $\tfrac{1}{2}mv^2$, and show that its unit is the joule written in base units.

$$E = \tfrac{1}{2} \times 0.16\,\text{kg} \times (30\,\text{m/s})^2 = 0.08 \times 900\,\text{kg}\,\text{m}^2\,\text{s}^{-2} = 72\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$$

The unit $\text{kg}\,\text{m}^2\,\text{s}^{-2}$ is exactly the joule we built above from $\text{N} \times \text{m}$. So $E = 72\,\text{J}$.

**Sanity check:** two different routes — mass × speed² and force × distance — give the same base-unit combination, as they must if both describe energy.

## Where the picture breaks

The chain and the tape are working tools, not definitions. Each is only as good as its calibration, which traces back — through other instruments — to the SI definitions. And cricket's Laws are written in imperial units: $22\,\text{yd}$ is exactly $20.1168\,\text{m}$ (a yard is defined as exactly $0.9144\,\text{m}$), which we round to $20.12\,\text{m}$. The yard is not an SI unit at all; it is now defined *through* the metre.

## Key takeaway

The SI has seven base units; mechanics uses the metre, kilogram and second. Since 2019 all seven are defined by fixing the values of constants of nature. Every other unit is derived from them through a defining equation, such as $1\,\text{N} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$ and $1\,\text{J} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$.
