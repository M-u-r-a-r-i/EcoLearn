---
concept_id: unit_conversion
interest: cricket
format: explain
title: Turning a speed gun reading into physics units
check:
  question: |-
    A fast delivery leaves the hand at $40\,\text{m/s}$. What does the stadium's speed display show, in km/h?
  options:
    A: |-
      $11.1\,\text{km/h}$
    B: |-
      $144\,\text{km/h}$
    C: |-
      $0.04\,\text{km/h}$
    D: |-
      $2.4\,\text{km/h}$
  answer: B
  explanation: |-
    $40\,\text{m/s} = 40 \times \dfrac{1/1000\,\text{km}}{1/3600\,\text{h}} = 40 \times 3.6 = 144\,\text{km/h}$.
  misconceptions:
    A: |-
      Divides by $3.6$ instead of multiplying — the rule for km/h to m/s, used in the wrong direction. A kilometre per hour is a smaller unit, so the number must get bigger.
    C: |-
      Converts metres to kilometres but forgets to convert seconds to hours, changing only one of the two units in the ratio.
    D: |-
      Uses 60 seconds in an hour instead of 3600: $40 \times 60/1000 = 2.4$.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A speed display shows 142 km/h above groundstaff measuring the pitch](scenes/cricket/units_measurement.svg "The display speaks km/h. Physics equations speak m/s.")

For her physics project, Zoya is studying fast bowling. At a club match she films the stadium's speed display after every ball, and the quickest delivery reads $144\,\text{km/h}$.

Back home, she wants the ball's kinetic energy, $\tfrac{1}{2}mv^2$. She knows the answer comes out in joules only if the speed is in metres per second. So first, $144\,\text{km/h}$ has to become m/s.

Then her grandfather hands her his own college physics textbook, printed decades ago. Every energy in it is in **ergs**, every force in **dynes** — the old CGS units, built on the centimetre, gram and second. "Tell me your answer in my units too," he says, smiling.

Zoya now needs two different conversions: one for a speed, one for an energy. Is there a single method that works for any quantity?

## The physics

A physical quantity is a number times a unit: $Q = n_1 u_1 = n_2 u_2$. Changing to a bigger unit gives a smaller number, and vice versa.

Every unit can be built from base units, following the quantity's dimensional formula $[\text{M}^a\,\text{L}^b\,\text{T}^c]$. So the size of the unit is $u = M^a L^b T^c$, where $M$, $L$, $T$ are the sizes of the base units in that system. Since $n_1 u_1 = n_2 u_2$:

$$n_2 = n_1 \left[\frac{M_1}{M_2}\right]^a \left[\frac{L_1}{L_2}\right]^b \left[\frac{T_1}{T_2}\right]^c$$

Here system 1 is the one you have and system 2 the one you want. Each base-unit ratio is raised to the **same power** it has in the dimensional formula.

For a speed, $[\text{L}\,\text{T}^{-1}]$, so $a = 0$, $b = 1$, $c = -1$. Going from km/h to m/s, $L_1/L_2 = 1\,\text{km}/1\,\text{m} = 1000$ and $T_1/T_2 = 1\,\text{h}/1\,\text{s} = 3600$:

$$n_2 = 144 \times (1000)^1 \times (3600)^{-1} = \frac{144\,000}{3600} = 40$$

So $144\,\text{km/h} = 40\,\text{m/s}$.

![A chain of boxes: 144 km/h, times 1000, divided by 3600, gives 40 m/s; below it, the same step written with the dimensional formula](figures/unit_conversion/conversion-chain-kmh-ms.svg "Convert the length and the time separately; the dimensional formula tells you each factor's power. The shortcut is to divide by 3.6.")

## Worked example

**Given:** ball mass $m = 0.16\,\text{kg}$ (illustrative), speed $v = 40\,\text{m/s}$.
**Find:** the kinetic energy in joules, then in ergs (the CGS unit, $\text{g}\,\text{cm}^2\,\text{s}^{-2}$).

In SI:

$$E = \tfrac{1}{2}mv^2 = \tfrac{1}{2} \times 0.16 \times 40^2 = 0.08 \times 1600 = 128\,\text{J}$$

Energy has dimensions $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$, so $a = 1$, $b = 2$, $c = -2$. From SI to CGS: $M_1/M_2 = 1\,\text{kg}/1\,\text{g} = 10^3$; $L_1/L_2 = 1\,\text{m}/1\,\text{cm} = 10^2$; $T_1/T_2 = 1$.

$$n_2 = 128 \times (10^3)^1 \times (10^2)^2 \times (1)^{-2} = 128 \times 10^7 = 1.28 \times 10^9$$

So $E = 1.28 \times 10^9\,\text{erg}$. As a check on the method, $1\,\text{J} = 10^3 \times 10^4 = 10^7\,\text{erg}$, the standard result.

**Sanity check:** the erg is a much smaller unit than the joule, so the number should get much bigger — and it does, by $10^7$. The length ratio was squared because energy contains $\text{L}^2$.

## Where the picture breaks

A conversion changes units, not precision: $144\,\text{km/h}$ (three significant figures) becomes $40.0\,\text{m/s}$, not a more exact number. The speed display itself is an estimate from a radar or camera system, with its own uncertainty. And this method works only for units that differ by a scale factor. Temperature in $^\circ\text{C}$ and $^\circ\text{F}$ have different zero points, so they need an extra step that no power of a ratio can supply.

## Key takeaway

To convert any quantity, use its dimensional formula $[\text{M}^a\,\text{L}^b\,\text{T}^c]$: $n_2 = n_1 (M_1/M_2)^a (L_1/L_2)^b (T_1/T_2)^c$. Each base-unit ratio gets the same power as in the dimensional formula. So $144\,\text{km/h} = 40\,\text{m/s}$ and $1\,\text{J} = 10^7\,\text{erg}$.
