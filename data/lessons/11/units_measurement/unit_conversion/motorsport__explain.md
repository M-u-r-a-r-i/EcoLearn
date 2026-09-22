---
concept_id: unit_conversion
interest: motorsport
format: explain
title: From the speed trap to the physics notebook
check:
  question: |-
    A race car's brakes exert an average force of $1.5 \times 10^4\,\text{N}$ (illustrative). An older textbook works in CGS units. What is this force in dynes ($\text{g}\,\text{cm}\,\text{s}^{-2}$)?
  options:
    A: |-
      $1.5 \times 10^7\,\text{dyn}$
    B: |-
      $1.5 \times 10^{11}\,\text{dyn}$
    C: |-
      $1.5 \times 10^{-1}\,\text{dyn}$
    D: |-
      $1.5 \times 10^9\,\text{dyn}$
  answer: D
  explanation: |-
    Force is $[\text{M}\,\text{L}\,\text{T}^{-2}]$, so $n_2 = n_1 (10^3)^1 (10^2)^1 (1)^{-2} = 1.5 \times 10^4 \times 10^5 = 1.5 \times 10^9\,\text{dyn}$.
  misconceptions:
    A: |-
      Converts the kilograms to grams ($\times 10^3$) but forgets the metres-to-centimetres factor ($\times 10^2$). Every base unit in the dimensional formula must be converted.
    B: |-
      Squares the length ratio, as for energy. Force has $\text{L}^1$, so the length ratio appears only once.
    C: |-
      Inverts the ratios, dividing by $10^5$. The dyne is a much smaller unit than the newton, so the number must get bigger, not smaller.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A race track with a timing screen showing a speed-trap reading of 306 km/h](scenes/motorsport/units_measurement.svg "The speed trap speaks km/h. Physics equations want m/s.")

For her school physics project on braking, Ritika watches a club race from the grandstand with her uncle. The speed-trap screen flashes $306\,\text{km/h}$ as a car blasts past before the braking zone.

Her plan is to work out how hard the brakes must work. But every formula in her notebook expects metres and seconds; put in km/h and the answers will be nonsense.

Then her uncle, a retired mechanical engineer, lends her his old college textbook on vehicle dynamics. Every force in it is in **dynes** and every acceleration in cm/s² — the CGS system, built on the centimetre, gram and second.

"Check your numbers against my book," he says.

So now there are three systems on her desk: km and hours, SI, and CGS. Does she need a separate trick for every conversion, or is there one method that handles them all?

## The physics

A physical quantity is a number times a unit: $Q = n_1 u_1 = n_2 u_2$. A bigger unit means a smaller number.

Any unit is built from base units according to the quantity's dimensional formula $[\text{M}^a\,\text{L}^b\,\text{T}^c]$. Since $n_1 u_1 = n_2 u_2$,

$$n_2 = n_1 \left[\frac{M_1}{M_2}\right]^a \left[\frac{L_1}{L_2}\right]^b \left[\frac{T_1}{T_2}\right]^c$$

where system 1 is what you have and system 2 is what you want. Each base-unit ratio carries the **same power** as in the dimensional formula.

**The speed trap.** Speed is $[\text{L}\,\text{T}^{-1}]$: $b = 1$, $c = -1$. From km/h to m/s, $L_1/L_2 = 1\,\text{km}/1\,\text{m} = 1000$ and $T_1/T_2 = 1\,\text{h}/1\,\text{s} = 3600$:

$$n_2 = 306 \times (1000)^1 \times (3600)^{-1} = \frac{306\,000}{3600} = 85$$

So $306\,\text{km/h} = 85\,\text{m/s}$ — the familiar shortcut is to divide by $3.6$.

![A chain of boxes: 144 km/h, times 1000, divided by 3600, gives 40 m/s; below it, the same step written with the dimensional formula](figures/unit_conversion/conversion-chain-kmh-ms.svg "The same chain works for any speed: convert the length and the time separately, each with the power from the dimensional formula.")

## Worked example

**Given:** a race car braking hard at $a = 40\,\text{m/s}^2$ (illustrative, about four times $g$).
**Find:** this deceleration (a) in CGS units, cm/s²; (b) in km/h².

Acceleration is $[\text{L}\,\text{T}^{-2}]$, so the powers of M, L and T are $0$, $1$ and $-2$.

(a) SI to CGS: $L_1/L_2 = 1\,\text{m}/1\,\text{cm} = 10^2$; $T_1/T_2 = 1$.

$$n_2 = 40 \times (10^2)^1 \times (1)^{-2} = 4.0 \times 10^3\,\text{cm/s}^2$$

(b) m/s² to km/h²: $L_1/L_2 = 1\,\text{m}/1\,\text{km} = 10^{-3}$; $T_1/T_2 = 1\,\text{s}/1\,\text{h} = 1/3600$.

$$n_2 = 40 \times (10^{-3})^1 \times \left(\tfrac{1}{3600}\right)^{-2} = 40 \times 10^{-3} \times 1.296 \times 10^7 = 5.2 \times 10^5\,\text{km/h}^2$$

The time ratio is raised to the power $-2$, so it multiplies by $3600^2$, not just $3600$.

**Sanity check:** losing $40\,\text{m/s}$ each second means losing $40 \times 3.6 = 144\,\text{km/h}$ each second, which is $144 \times 3600 = 518\,400 \approx 5.2 \times 10^5\,\text{km/h}$ every hour. It matches.

## Where the picture breaks

A conversion changes units, not precision: $306\,\text{km/h}$ has three significant figures, so the honest result is $85.0\,\text{m/s}$, no more exact. The speed trap is itself a measurement with its own uncertainty. A real car's deceleration is not constant through a braking zone, so a single figure like $40\,\text{m/s}^2$ is an idealised average. And the method only works for units that differ by a scale factor: $^\circ\text{C}$ and $^\circ\text{F}$ have different zeros, which no power of a ratio can fix.

## Key takeaway

To convert any quantity, use its dimensional formula: $n_2 = n_1 (M_1/M_2)^a (L_1/L_2)^b (T_1/T_2)^c$, with each ratio raised to its power. So $306\,\text{km/h} = 85\,\text{m/s}$ and $40\,\text{m/s}^2 = 4.0 \times 10^3\,\text{cm/s}^2$; a squared time in the formula means the time ratio appears squared.
