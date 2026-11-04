---
concept_id: significant_figures
interest: gaming
format: explain
title: What a ruler under the mouse can honestly say
check:
  question: |-
    Nisha weighs her new lightweight mouse on a kitchen scale and writes its mass as $0.0580\,\text{kg}$. How many significant figures does this value have?
  options:
    A: |-
      $2$ — only the $5$ and the $8$ count
    B: |-
      $5$ — every digit written down counts
    C: |-
      It can't be decided, because the final zero is ambiguous
    D: |-
      $3$ — the $5$, the $8$ and the final zero
  answer: D
  explanation: |-
    The two zeros before the $5$ only place the decimal point, so they don't count. The final zero comes after the decimal point, so it is a measured digit: $5$, $8$, $0$ gives $3$ significant figures.
  misconceptions:
    A: |-
      Thinks final zeros never count. After a decimal point they do: writing $0.0580$ rather than $0.058$ claims the scale really read that last digit.
    B: |-
      Counts the leading zeros. They only locate the decimal point; the same mass is $58.0\,\text{g}$, which plainly has three significant figures.
    C: |-
      Applies the whole-number rule to a decimal. Final zeros are ambiguous only in a number with no decimal point, like $5800$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk: a monitor with a racing game, a mouse on a mousepad with a ruler along its edge, a controller on a kitchen scale and a phone](scenes/gaming/units_measurement.svg "Look at the ruler under the mouse. How finely can it be read?")

Nisha's team is setting up for an inter-college online tournament, and the captain wants everyone's aim settings in one shared sheet. One setting matters most: how far you slide the mouse for your character to turn a full circle. Players call it "cm per 360".

Nisha lays a steel ruler along her mousepad, lines up the mouse's edge with the zero, and sweeps slowly until the view comes back to the same wall crack. The edge stops between two millimetre marks. She types *34.6 cm*.

Sameer, on voice chat, pastes his own value from an online calculator: *34.6152 cm*. "Mine's better," he says. "More digits, more accurate."

Nisha looks at the ruler, then at his six digits. Something about "more digits" bothers her. What do the digits in a measured value actually promise — and how many can a ruler honestly give?

## The physics

Every measurement has some uncertainty, and the digits you write down report how precise the measurement was.

The **significant figures** in a measured value are the digits that are reliably known **plus the first digit that is uncertain**. On a millimetre scale you read the marks for certain, then estimate one more digit between them:

![A millimetre scale from 7 to 8 cm with an object's edge between the 7.4 and 7.5 marks; the reading 7.46 cm has 7.4 in green as certain and 6 in orange as estimated](figures/significant_figures/scale-reading-certain-estimated.svg "The marks give 7.4 cm for certain; the 6 is a best estimate between marks. All three digits are significant.")

Nisha's *34.6 cm* claims precision to about a millimetre: it has **three** significant figures, and the last one (the $6$) is her estimate. Sameer's six digits came from a formula fed with his mouse's rated sensor setting, not from measuring how far the mouse really slides — and a real sensor doesn't match its rating exactly. A calculator can print as many digits as you like; the number of *significant* figures is set by how well the quantity was measured. Checked with a ruler, his value too could honestly be given to only about three figures.

**The NCERT counting rules:**

1. All non-zero digits are significant.
2. Zeros between non-zero digits are significant ($3.07$ has three).
3. Zeros before the first non-zero digit are **not** significant; they only place the decimal point ($0.0167$ has three).
4. Final zeros after a decimal point **are** significant ($3.70$ has three).
5. Final zeros in a whole number with no decimal point are **ambiguous** ($1800$ could have two, three or four). Scientific notation settles it: $1.8 \times 10^3$ has two, $1.80 \times 10^3$ has three.

![A table of six values with significant digits in green, leading zeros in grey and ambiguous zeros in orange, with the rule each one shows](figures/significant_figures/counting-examples.svg "Green digits count; grey leading zeros never do; orange final zeros in a whole number stay ambiguous until you use powers of ten.")

Changing units never changes the count: $34.6\,\text{cm} = 346\,\text{mm} = 0.346\,\text{m}$, three significant figures each time, because the measurement itself hasn't changed.

## Worked example

**Find** the number of significant figures in each measured value (illustrative).

| Measured value | Significant figures | Why |
|---|---|---|
| monitor width $59.80\,\text{cm}$ | $4$ | final zero after the point counts |
| controller cell voltage $3.70\,\text{V}$ | $3$ | final zero after the point counts |
| frame time from a slow-motion video $0.0167\,\text{s}$ | $3$ | leading zeros don't count |
| USB cable length $1800\,\text{mm}$ | ambiguous | final zeros, no decimal point |

If the cable was measured to the nearest centimetre ($10\,\text{mm}$), the digits up to the tens place are known, so write $1.80 \times 10^3\,\text{mm}$: three significant figures.

**Sanity check:** $0.0167\,\text{s} = 16.7\,\text{ms}$, still three significant figures, as it must be.

## Where the picture breaks

Significant figures describe **precision**, not **accuracy**. If Nisha's ruler slipped, *34.6 cm* could still be wrong while looking precise. Some numbers have no uncertainty at all: counted or defined ones, like "5 players in a team" or the $360^\circ$ in a full turn. They are **exact** and never limit the significant figures of anything. And a setting inside a game is exact by definition; only a *measurement* of the real world carries significant figures.

## Key takeaway

Significant figures are the certain digits plus the first uncertain one, so they report how precise a measurement is. Leading zeros never count; final zeros after a decimal point always do; final zeros in a whole number are ambiguous until you use scientific notation. More digits from a calculator are not more precision.
