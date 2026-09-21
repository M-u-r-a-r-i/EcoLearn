---
concept_id: unit_conversion
interest: cricket
format: misconception
title: The cricket ball that would float away like a balloon
check:
  question: |-
    A practice strip at the nets has an area of $24.0\,\text{m}^2$. What is this area in square centimetres?
  options:
    A: |-
      $2.40 \times 10^5\,\text{cm}^2$
    B: |-
      $2.40 \times 10^3\,\text{cm}^2$
    C: |-
      $2.40 \times 10^{-3}\,\text{cm}^2$
    D: |-
      $2.40 \times 10^7\,\text{cm}^2$
  answer: A
  explanation: |-
    Area has dimensions $[\text{L}^2]$, so the length ratio is squared: $1\,\text{m}^2 = (100\,\text{cm})^2 = 10^4\,\text{cm}^2$. Then $24.0 \times 10^4 = 2.40 \times 10^5\,\text{cm}^2$.
  misconceptions:
    B: |-
      Multiplies by $100$ only once, converting as if area were a length. Both factors of metre must be converted.
    C: |-
      Divides instead of multiplying. Square centimetres are smaller units than square metres, so the number must get bigger.
    D: |-
      Cubes the factor ($10^6$), using the volume conversion for an area.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A cricket ball sits on a digital scale next to groundstaff measuring the pitch](scenes/cricket/units_measurement.svg "A ball on a scale, a pitch under a tape. Mass and length are easy. Density needs both, and a conversion.")

The science fair is tomorrow, and Ritika's poster is nearly done: *How dense is a cricket ball?* She measured the mass and the circumference of a ball, worked out its volume, and found a density of about $0.80\,\text{g/cm}^3$.

The judges prefer SI units, so she converts. "Grams to kilograms: divide by $1000$. Centimetres to metres: divide by $100$. So cm$^3$ becomes m$^3$ by dividing by $100$ as well." Her final line in big letters: **Density = 0.08 kg/m³**.

Her friend Yusuf reads it and bursts out laughing. "Ritika, air is about $1.2\,\text{kg/m}^3$. If your ball were $0.08$, it would be lighter than air. It would float off your hand like a helium balloon."

Ritika checks her multiplication twice. It's fine. So where did a solid leather ball turn into a balloon?

## The common belief

"To convert a unit, convert each base unit once. A centimetre is $10^{-2}\,\text{m}$, so anything in centimetres — cm, cm², cm³ — is converted by the same factor of $100$."

## Why it feels right

For a plain length, it's exactly right: $1\,\text{cm} = 10^{-2}\,\text{m}$, always. Most conversions students do early on are single units — cm to m, g to kg, minutes to seconds — where one factor is enough. So "cm to m means divide by 100" becomes a habit that feels like a rule. The symbol cm³ even *looks* like centimetres with a small label attached, not like three centimetres multiplied together.

## What actually happens

A cubic centimetre is a centimetre **times** a centimetre **times** a centimetre:

$$1\,\text{cm}^3 = (10^{-2}\,\text{m})^3 = 10^{-6}\,\text{m}^3$$

So Ritika's density conversion should be

$$0.80\,\frac{\text{g}}{\text{cm}^3} = 0.80 \times \frac{10^{-3}\,\text{kg}}{10^{-6}\,\text{m}^3} = 0.80 \times 10^{3}\,\frac{\text{kg}}{\text{m}^3} = 800\,\text{kg/m}^3$$

That is ten thousand times her poster's value. Now it makes sense: a little less dense than water ($1000\,\text{kg/m}^3$), and far denser than air.

![A one-metre square divided into a 10 by 10 grid, and a one-metre cube, showing that one square metre is ten thousand square centimetres and one cubic metre is a million cubic centimetres](figures/unit_conversion/area-volume-conversion.svg "Each metre in the unit becomes 100 cm, so m² needs 100 × 100 and m³ needs 100 × 100 × 100.")

## The physics

A unit's conversion factor follows its **dimensional formula**. For a quantity with dimensions $[\text{M}^a\,\text{L}^b\,\text{T}^c]$:

$$n_2 = n_1 \left[\frac{M_1}{M_2}\right]^a \left[\frac{L_1}{L_2}\right]^b \left[\frac{T_1}{T_2}\right]^c$$

Density is $[\text{M}\,\text{L}^{-3}]$, so $a = 1$ and $b = -3$. From CGS to SI: $M_1/M_2 = 1\,\text{g}/1\,\text{kg} = 10^{-3}$ and $L_1/L_2 = 1\,\text{cm}/1\,\text{m} = 10^{-2}$:

$$n_2 = 0.80 \times (10^{-3})^{1} \times (10^{-2})^{-3} = 0.80 \times 10^{-3} \times 10^{6} = 800$$

The misconception uses $(10^{-2})^{1}$ where the dimensional formula demands $(10^{-2})^{-3}$. Every base-unit factor must carry its full power: squared for areas, cubed for volumes, and inverted when the unit is in the denominator.

## Worked example

**Given:** the pitch area $61.4\,\text{m}^2$ (from $20.12\,\text{m} \times 3.05\,\text{m}$).
**Find:** the area in $\text{cm}^2$.

Area is $[\text{L}^2]$, and $L_1/L_2 = 1\,\text{m}/1\,\text{cm} = 100$:

$$n_2 = 61.4 \times (100)^2 = 61.4 \times 10^4 = 6.14 \times 10^5\,\text{cm}^2$$

**Sanity check:** $20.12\,\text{m} = 2012\,\text{cm}$ and $3.05\,\text{m} = 305\,\text{cm}$; $2012 \times 305 = 613\,660 \approx 6.14 \times 10^5\,\text{cm}^2$. Converting the lengths first gives the same answer.

## Key takeaway

Squared and cubed units need squared and cubed conversion factors: $1\,\text{m}^2 = 10^4\,\text{cm}^2$ and $1\,\text{m}^3 = 10^6\,\text{cm}^3$. Let the dimensional formula set each power — then $0.80\,\text{g/cm}^3 = 800\,\text{kg/m}^3$, not $0.08$. When an answer looks absurd, like a ball lighter than air, check the powers.
