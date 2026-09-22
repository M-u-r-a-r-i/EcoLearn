---
concept_id: unit_conversion
interest: smartphones
format: explain
title: A fast charger in old-fashioned units
check:
  question: |-
    A phone charger delivers $20\,\text{W}$. In CGS units, where power is measured in erg per second ($\text{g}\,\text{cm}^2\,\text{s}^{-3}$), this is:
  options:
    A: |-
      $2.0 \times 10^{6}\,\text{erg/s}$
    B: |-
      $2.0 \times 10^{-6}\,\text{erg/s}$
    C: |-
      $2.0 \times 10^{4}\,\text{erg/s}$
    D: |-
      $2.0 \times 10^{8}\,\text{erg/s}$
  answer: D
  explanation: |-
    Power is $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$, so $n_2 = 20 \times (10^3)^1 \times (10^2)^2 \times (1)^{-3} = 20 \times 10^7 = 2.0 \times 10^8\,\text{erg/s}$.
  misconceptions:
    A: |-
      Converts the length but forgets to square the length ratio: power contains $\text{L}^2$, so the factor is $(10^2)^2 = 10^4$, not $10^2$.
    B: |-
      Inverts the base-unit ratios (small unit over big unit). The erg per second is a much smaller unit than the watt, so the number must get bigger, not smaller.
    C: |-
      Converts only the mass (kilogram to gram) and leaves out the length conversion entirely.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A study desk: a charger labelled 5 V and 2 A plugged into a USB meter reading 5.01 V and 1.80 A, beside a phone on a scale and a phone in a caliper](scenes/smartphones/units_measurement.svg "The charger's label speaks SI. Older physics books speak centimetres, grams and seconds.")

Rhea's olympiad coaching class has handed out a stack of old practice papers, and every one of them is in **CGS** units — centimetre, gram, second. Force in dynes, energy in ergs, power in erg per second.

Question 4 on tonight's sheet: *A phone's fast charger works at $9\,\text{V}$ and $2\,\text{A}$, delivering $18\,\text{W}$. Express this power in erg/s.* Question 5: *Express $g = 9.8\,\text{m/s}^2$ in $\text{cm/s}^2$.*

Her study partner Aman finishes both in ten seconds. "One metre is a hundred centimetres. So multiply everything by a hundred: $980\,\text{cm/s}^2$ and $1800\,\text{erg/s}$. Done."

Rhea checks the answer key at the back. Question 5: $980$. Correct. Question 4: not $1800$ — something enormously bigger.

The same trick worked once and failed once. Why? Is there a single method that tells you, for *any* quantity, exactly what to multiply by?

## The physics

A physical quantity is a number times a unit: $Q = n_1 u_1 = n_2 u_2$. Change to a smaller unit and the number gets bigger, and vice versa.

Every unit is built from base units according to the quantity's dimensional formula $[\text{M}^a\,\text{L}^b\,\text{T}^c]$. So the size of the unit is $u = M^a L^b T^c$, where $M$, $L$ and $T$ are the sizes of the base units in that system. Since $n_1 u_1 = n_2 u_2$:

$$n_2 = n_1 \left[\frac{M_1}{M_2}\right]^a \left[\frac{L_1}{L_2}\right]^b \left[\frac{T_1}{T_2}\right]^c$$

System 1 is the one you have; system 2 is the one you want. Each base-unit ratio is raised to the **same power** it has in the dimensional formula.

From SI to CGS: $M_1/M_2 = 1\,\text{kg}/1\,\text{g} = 10^3$; $L_1/L_2 = 1\,\text{m}/1\,\text{cm} = 10^2$; $T_1/T_2 = 1\,\text{s}/1\,\text{s} = 1$.

**Question 5.** Acceleration is $[\text{L}\,\text{T}^{-2}]$: $a = 0$, $b = 1$, $c = -2$.

$$n_2 = 9.8 \times (10^2)^1 \times (1)^{-2} = 980, \quad\text{so } g = 980\,\text{cm/s}^2$$

Aman's "times a hundred" worked only because length appears to the first power and there's no mass.

**Question 4.** Power is $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$: $a = 1$, $b = 2$, $c = -3$.

$$n_2 = 18 \times (10^3)^1 \times (10^2)^2 \times (1)^{-3} = 18 \times 10^3 \times 10^4 = 1.8 \times 10^8$$

So $18\,\text{W} = 1.8 \times 10^8\,\text{erg/s}$. Aman missed two things: the mass also changes units, and length appears **squared**.

![A one-metre square divided into a ten-by-ten grid of 10 cm squares, and a one-metre cube, showing that one square metre is ten thousand square centimetres and one cubic metre is a million cubic centimetres](figures/unit_conversion/area-volume-conversion.svg "When a length appears squared, its conversion factor is squared too: 1 m² is 10⁴ cm², not 100 cm². That's why power picks up 10⁴ from its L².")

## Worked example

**Given:** a power bank's label gives its stored energy as $37\,\text{Wh}$ (illustrative), meaning a power of one watt for $37$ hours.
**Find:** this energy in joules, then in ergs.

A watt-hour is a watt times an hour, and $1\,\text{h} = 3600\,\text{s}$, so $1\,\text{Wh} = 3600\,\text{J}$:

$$E = 37 \times 3600\,\text{J} = 133\,200\,\text{J} \approx 1.33 \times 10^5\,\text{J}$$

Energy is $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$, so $a = 1$, $b = 2$, $c = -2$:

$$n_2 = 1.33 \times 10^5 \times (10^3)^1 \times (10^2)^2 \times (1)^{-2} = 1.33 \times 10^5 \times 10^7 = 1.33 \times 10^{12}$$

So $E \approx 1.33 \times 10^{12}\,\text{erg}$. This also confirms the standard result $1\,\text{J} = 10^7\,\text{erg}$.

**Sanity check:** the erg is a far smaller unit than the joule, so the number should grow — it grows by $10^7$. And the watt converts by the same $10^7$ as the joule, because the second is the same in both systems, so the extra $\text{T}^{-1}$ contributes a factor of $1$.

## Where the picture breaks

A conversion changes the unit, not the precision: $18\,\text{W}$ (two significant figures) becomes $1.8 \times 10^8\,\text{erg/s}$, not a more exact number. The watt-hour is a practical unit, not part of a coherent system, so it needed an ordinary time conversion first. And the method works only for units that differ by a scale factor. Temperatures in $^\circ\text{C}$ and $^\circ\text{F}$ have different zeros, so no product of ratios can convert them.

## Key takeaway

To convert any quantity, use its dimensional formula $[\text{M}^a\,\text{L}^b\,\text{T}^c]$: $n_2 = n_1 (M_1/M_2)^a (L_1/L_2)^b (T_1/T_2)^c$. Each base-unit ratio gets the same power as in the dimensional formula, so $9.8\,\text{m/s}^2 = 980\,\text{cm/s}^2$ but $1\,\text{W} = 10^7\,\text{erg/s}$.
