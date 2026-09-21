---
concept_id: si_units
interest: football
format: misconception
title: Is the referee's second a slice of the Earth's spin
check:
  question: |-
    The referee's watch counts the $45$ minutes of a half. Today, what defines the second that the watch is ultimately calibrated against?
  options:
    A: |-
      Exactly $1/86\,400$ of the time the Earth takes to spin once
    B: |-
      The time for one swing of a standard pendulum kept in a laboratory
    C: |-
      The time signal broadcast by the country's national laboratory
    D: |-
      A fixed, exact frequency of radiation from the caesium-133 atom
  answer: D
  explanation: |-
    Since 1967 the second has been defined by fixing the caesium-133 transition frequency at exactly $9\,192\,631\,770\,\text{Hz}$. One second is that many cycles of the radiation.
  misconceptions:
    A: |-
      Holds the old astronomical definition. The Earth's spin is not perfectly steady, which is exactly why the second was taken away from it.
    B: |-
      Thinks a pendulum defines time. Pendulum clocks were once good timekeepers, but a pendulum's period depends on its length and on $g$, so it was never the SI definition.
    C: |-
      Mistakes a way of distributing time for its definition. National laboratories broadcast time signals that are realised with caesium clocks; the signal is a copy, not the standard.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures the goal while a match clock above the stands reads 45:00](scenes/football/units_measurement.svg "The match clock shows 45:00. Forty-five minutes of what, exactly?")

Kabir's team is 1–0 down, the match clock has just hit 45:00, and the fourth official holds up the board: two minutes of added time. On the touchline, Kabir's sister Ishani is timing everything on her phone.

"Here's a fact for you," Kabir says at half-time, still breathing hard. "A second is one eighty-six-thousand-four-hundredth of a day. So a half of football is exactly a thirty-second part of one spin of the Earth. The planet is the referee's real clock."

Ishani does the division. $86\,400 \div 2700 = 32$. The arithmetic works. But something bothers her: she once read that days aren't all exactly the same length. If the Earth wobbles, does the match wobble too? What does a second really mean?

## The common belief

"Time is measured by the Earth. A day is the natural unit, and a second is simply $1/86\,400$ of it. Clocks, watches and phones are all copies of the Earth's rotation."

## Why it feels right

For most of history, it was true. Days, hours, minutes and seconds all came from the sky, and for centuries the second was defined as $1/86\,400$ of a mean solar day. Every clock was set by watching the Sun or the stars. It is still what the word "day" means in everyday life, and $24 \times 60 \times 60 = 86\,400$ really does hold for clock time. Kabir's arithmetic is correct.

## What actually happens

As clocks improved in the twentieth century, astronomers found the Earth is a slightly irregular timekeeper. Its spin speeds up and slows down by tiny amounts, and tides very slowly lengthen the day. Since 1972, occasional **leap seconds** have been added to clock time to keep it in step with the Earth — which shows the Earth, not the clocks, is the one drifting.

So the second was taken away from the Earth. In 1960 it was briefly defined through the Earth's orbit, and since 1967 by an atom: the radiation from a particular transition of **caesium-133** has a frequency fixed at exactly $9\,192\,631\,770\,\text{Hz}$. One second is that many cycles. Every caesium atom is identical, so the definition is the same in every laboratory on Earth.

The same move happened to every SI base unit: the metre is fixed through the speed of light, and since 20 May 2019 the kilogram through the Planck constant — no longer by a metal cylinder like this national copy.

![A small metal cylinder sitting under two nested glass bell jars](famous/us-prototype-kilogram-k20.jpg "National prototype kilogram K20, a copy of the international prototype that defined the kilogram until 2019. Like the Earth's spin for the second, an object was replaced by a constant. Public domain, via Wikimedia Commons.")

## The physics

The SI has seven **base units** — metre, kilogram, second, ampere, kelvin, mole, candela — and since 20 May 2019 each one is defined by fixing the exact value of a constant of nature. All other units are **derived** from them.

![A table of the seven SI base units with the constant that defines each](figures/si_units/seven-base-units.svg "The second is defined by the caesium frequency — an atomic constant, not the Earth.")

The misconception confuses the **historical origin** of a unit (the day, a metal bar, a cylinder) with its **present definition**. The second was deliberately made independent of the Earth, so that time means the same everywhere, for ever.

## Worked example

**Find** how many caesium cycles make up one $45$-minute half.

$$45\,\text{min} = 45 \times 60\,\text{s} = 2700\,\text{s}$$

$$N = 2700\,\text{s} \times 9\,192\,631\,770\,\text{s}^{-1} \approx 2.48 \times 10^{13}\ \text{cycles}$$

**Sanity check:** the unit $\text{Hz} = \text{s}^{-1}$ times seconds leaves a pure number, as a count of cycles must. For a football match, the Earth's wobbles would change a half by far less than a millisecond; the definition matters for things like satellite navigation, which depends on timing to billionths of a second.

## Key takeaway

The second is no longer a slice of the Earth's day. Since 1967 it has been defined by the caesium-133 frequency, $9\,192\,631\,770\,\text{Hz}$ exactly. All seven SI base units are now fixed by constants of nature; the day, the metre bar and the kilogram cylinder are history.
