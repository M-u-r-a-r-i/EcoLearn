---
concept_id: unit_conversion
interest: football
format: explain
title: Turning a speed-gun reading into physics units
check:
  question: |-
    A speed gun clocks a free kick at $126\,\text{km/h}$. What is this speed in m/s?
  options:
    A: |-
      $453.6\,\text{m/s}$
    B: |-
      $35\,\text{m/s}$
    C: |-
      $0.035\,\text{m/s}$
    D: |-
      $2100\,\text{m/s}$
  answer: B
  explanation: |-
    $126\,\text{km/h} = 126 \times \dfrac{1000\,\text{m}}{3600\,\text{s}} = \dfrac{126}{3.6}\,\text{m/s} = 35\,\text{m/s}$.
  misconceptions:
    A: |-
      Multiplies by $3.6$ instead of dividing — the rule for m/s to km/h, used the wrong way round. A metre per second is a bigger unit than a kilometre per hour, so the number must get smaller.
    C: |-
      Converts hours to seconds but not kilometres to metres, changing only one of the two units in the ratio; $0.035$ is the speed in km/s.
    D: |-
      Uses $60$ seconds in an hour instead of $3600$: $126 \times 1000/60 = 2100$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal with a tape, beside a scale, a gauge and a match clock](scenes/football/units_measurement.svg "Every instrument speaks its own units. Physics equations need them all in one system.")

Yamini's academy has borrowed a radar speed gun for shooting practice, and her hardest drive reads $108\,\text{km/h}$. For her physics project she wants the ball's momentum, $p = mv$, and she knows it comes out in $\text{kg}\,\text{m/s}$ only if the speed is in metres per second. So first, $108\,\text{km/h}$ has to become m/s.

Then her grandmother, a retired physics teacher, pulls an old textbook off the shelf. In it, every mass is in grams, every length in centimetres, and every force in **dynes** — the CGS system. "Give me the momentum in my units too," she says, "grams, centimetres, seconds."

Yamini now needs two conversions: a speed from km/h to m/s, and a momentum from SI to CGS. Is there one method that handles both — and any other quantity she might meet?

## The physics

A physical quantity is a number times a unit: $Q = n_1 u_1 = n_2 u_2$. Change to a bigger unit and the number gets smaller, and vice versa.

Every unit is built from base units, following the quantity's dimensional formula $[\text{M}^a\,\text{L}^b\,\text{T}^c]$. So the size of the unit is $u = M^a L^b T^c$, where $M$, $L$, $T$ are the sizes of the base units in that system. Since $n_1 u_1 = n_2 u_2$:

$$n_2 = n_1 \left[\frac{M_1}{M_2}\right]^a \left[\frac{L_1}{L_2}\right]^b \left[\frac{T_1}{T_2}\right]^c$$

System 1 is the one you have, system 2 the one you want. Each base-unit ratio is raised to the **same power** it has in the dimensional formula.

For a speed, $[\text{L}\,\text{T}^{-1}]$: $a = 0$, $b = 1$, $c = -1$. From km/h to m/s, $L_1/L_2 = 1\,\text{km}/1\,\text{m} = 1000$ and $T_1/T_2 = 1\,\text{h}/1\,\text{s} = 3600$:

$$n_2 = 108 \times (1000)^1 \times (3600)^{-1} = \frac{108\,000}{3600} = 30$$

So $108\,\text{km/h} = 30\,\text{m/s}$.

![A chain of boxes: 144 km/h, times 1000, divided by 3600, gives 40 m/s; below it, the same step written with the dimensional formula](figures/unit_conversion/conversion-chain-kmh-ms.svg "The same method for another speed: convert the length and the time separately, each with its power from the dimensional formula. The shortcut is to divide by 3.6.")

## Worked example

**Given:** ball mass $m = 0.43\,\text{kg}$, speed $v = 30\,\text{m/s}$ (illustrative).
**Find:** the momentum in SI, then in CGS units ($\text{g}\,\text{cm}\,\text{s}^{-1}$).

In SI:

$$p = mv = 0.43\,\text{kg} \times 30\,\text{m/s} = 12.9\,\text{kg}\,\text{m/s}$$

Momentum has dimensions $[\text{M}\,\text{L}\,\text{T}^{-1}]$, so $a = 1$, $b = 1$, $c = -1$. From SI to CGS: $M_1/M_2 = 1\,\text{kg}/1\,\text{g} = 10^3$; $L_1/L_2 = 1\,\text{m}/1\,\text{cm} = 10^2$; $T_1/T_2 = 1$.

$$n_2 = 12.9 \times (10^3)^1 \times (10^2)^1 \times (1)^{-1} = 12.9 \times 10^5 = 1.29 \times 10^6$$

So $p = 1.29 \times 10^6\,\text{g}\,\text{cm/s}$.

**Sanity check:** convert first, then multiply: $430\,\text{g} \times 3000\,\text{cm/s} = 1\,290\,000 = 1.29 \times 10^6\,\text{g}\,\text{cm/s}$. Both routes agree. The CGS units are smaller, so the number got bigger — by $10^5$, because momentum contains M once and L once.

## Where the picture breaks

A conversion changes units, not precision: $108\,\text{km/h}$ becomes $30.0\,\text{m/s}$, three significant figures either way. The radar gun's reading has its own uncertainty, and it measures the ball's speed along the gun's line of sight, so it reads low if the ball isn't flying straight at it. And the method works only for units that differ by a scale factor; temperatures in $^\circ\text{C}$ and $^\circ\text{F}$ have different zero points and need an extra step.

## Key takeaway

To convert any quantity, use its dimensional formula $[\text{M}^a\,\text{L}^b\,\text{T}^c]$: $n_2 = n_1 (M_1/M_2)^a (L_1/L_2)^b (T_1/T_2)^c$, each ratio carrying the same power as in the formula. So $108\,\text{km/h} = 30\,\text{m/s}$, and $12.9\,\text{kg}\,\text{m/s} = 1.29 \times 10^6\,\text{g}\,\text{cm/s}$.
