---
concept_id: unit_conversion
interest: football
format: misconception
title: The winger who sprinted at walking pace
check:
  question: |-
    The centre circle has a radius of $9.15\,\text{m}$, so its area is about $263\,\text{m}^2$. What is this area in square centimetres?
  options:
    A: |-
      $2.63 \times 10^4\,\text{cm}^2$
    B: |-
      $2.63 \times 10^{-2}\,\text{cm}^2$
    C: |-
      $2.63 \times 10^6\,\text{cm}^2$
    D: |-
      $2.63 \times 10^8\,\text{cm}^2$
  answer: C
  explanation: |-
    Area is $[\text{L}^2]$, so the length ratio is squared: $1\,\text{m}^2 = (100\,\text{cm})^2 = 10^4\,\text{cm}^2$. Then $263 \times 10^4 = 2.63 \times 10^6\,\text{cm}^2$. Square centimetres are smaller units, so the number gets bigger.
  misconceptions:
    A: |-
      Multiplies by $100$ only once, converting as if area were a length. Both metres in $\text{m}^2$ must be converted.
    B: |-
      Divides instead of multiplying. A smaller unit needs a bigger number, not a smaller one.
    D: |-
      Uses the volume factor, $10^6$, for an area. An area has length squared, not cubed.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal with a tape; a match clock stands above the stands](scenes/football/units_measurement.svg "Metres and seconds on the pitch; kilometres and hours on the road. The same speed can wear either unit.")

The academy's fitness report has just come out, and Shreya is thrilled: the GPS vest clocked her top sprint speed at $9.0\,\text{m/s}$. She wants to post it for her friends, who all think in kilometres per hour, like on a scooter's speedometer.

"A kilometre is a thousand times bigger than a metre," she reasons, "so the number in km/h should be smaller. To go from m/s to km/h, you divide by $3.6$." She types it in: $9.0 \div 3.6 = 2.5\,\text{km/h}$.

Her brother Dev, reading over her shoulder, starts laughing. "Two and a half kilometres an hour? Didi, that's slower than Nani walking to the temple. You're the fastest winger in the academy and you just told the world you stroll."

Shreya checks her division. $9.0 \div 3.6$ really is $2.5$. So where did her sprint go?

## The common belief

"When you change to a bigger unit, you divide; to a smaller unit, you multiply. And you can tell which unit is bigger by looking at it: a kilometre is bigger than a metre, so km/h is the bigger unit."

## Why it feels right

The first half is exactly right. A quantity is a number times a unit, so a bigger unit needs a smaller number: $9000\,\text{m} = 9\,\text{km}$. And for a single unit, "which is bigger" really is obvious: a kilometre is bigger than a metre.

The trouble is that km/h is not a single unit. It's a kilometre **divided by** an hour, and Shreya judged its size by looking only at the top half.

## What actually happens

Size up each unit properly, by converting one into the other:

$$1\,\text{km/h} = \frac{1000\,\text{m}}{3600\,\text{s}} = 0.278\,\text{m/s}$$

The kilometre makes the unit $1000$ times bigger, but dividing by an hour instead of a second makes it $3600$ times smaller. Overall, a kilometre per hour is **smaller** than a metre per second. So converting m/s to km/h means moving to a smaller unit, and the number must get **bigger**:

$$9.0\,\text{m/s} = 9.0 \times 3.6\,\text{km/h} = 32.4\,\text{km/h}$$

That's a sprinter's speed — about as fast as a scooter in slow town traffic. Shreya's rule "bigger unit, smaller number" was correct; her judgement of which unit was bigger was not.

The dimensional formula removes the guesswork, because it treats every base unit in the quantity, top and bottom.

## The physics

A unit's conversion factor follows its **dimensional formula**. For a quantity with dimensions $[\text{M}^a\,\text{L}^b\,\text{T}^c]$:

$$n_2 = n_1 \left[\frac{M_1}{M_2}\right]^a \left[\frac{L_1}{L_2}\right]^b \left[\frac{T_1}{T_2}\right]^c$$

Speed is $[\text{L}\,\text{T}^{-1}]$. From m/s (system 1) to km/h (system 2): $L_1/L_2 = 1\,\text{m}/1\,\text{km} = 10^{-3}$ and $T_1/T_2 = 1\,\text{s}/1\,\text{h} = 1/3600$:

$$n_2 = 9.0 \times (10^{-3})^1 \times \left(\frac{1}{3600}\right)^{-1} = 9.0 \times \frac{3600}{1000} = 32.4$$

![A chain of boxes converting 144 km/h to 40 m/s by multiplying by 1000 and dividing by 3600](figures/unit_conversion/conversion-chain-kmh-ms.svg "Going from km/h to m/s divides by 3.6; Shreya's direction, m/s to km/h, is the reverse chain and multiplies by 3.6.")

Every base unit carries its own power, and the time ratio's power of $-1$ is exactly the part the misconception ignores. Powers matter for areas and volumes too: $\text{m}^2$ needs the length ratio squared.

## Worked example

**Given:** the centre circle has radius $r = 9.15\,\text{m}$.
**Find:** its area in $\text{m}^2$ and in $\text{cm}^2$.

$$A = \pi r^2 = \pi \times (9.15\,\text{m})^2 = \pi \times 83.72\,\text{m}^2 \approx 263\,\text{m}^2$$

Area is $[\text{L}^2]$, and $L_1/L_2 = 1\,\text{m}/1\,\text{cm} = 100$:

$$n_2 = 263 \times (100)^2 = 2.63 \times 10^6\,\text{cm}^2$$

![A one-metre square divided into a ten by ten grid and a one-metre cube](figures/unit_conversion/area-volume-conversion.svg "Each metre becomes 100 cm, so a square metre holds 100 × 100 = 10⁴ square centimetres.")

**Sanity check:** convert the radius first: $915\,\text{cm}$, so $A = \pi \times 915^2 \approx 2.63 \times 10^6\,\text{cm}^2$. Same answer. And the number grew, because $\text{cm}^2$ is the smaller unit.

## Key takeaway

A bigger unit means a smaller number — but judge "bigger" for the whole unit, not its top half. $1\,\text{km/h} = 0.278\,\text{m/s}$, so $9.0\,\text{m/s} = 32.4\,\text{km/h}$. Let the dimensional formula set each power, including the negative power on time and the square on area.
