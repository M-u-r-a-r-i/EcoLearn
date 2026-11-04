---
concept_id: significant_figures
interest: football
format: misconception
title: Are the zeros in a ball's mass just placeholders
check:
  question: |-
    A precision balance gives a match ball's mass as $0.42050\,\text{kg}$. How many significant figures does this reading have?
  options:
    A: |-
      $5$
    B: |-
      $3$
    C: |-
      $4$
    D: |-
      $6$
  answer: A
  explanation: |-
    The leading zero only places the decimal point. The zero between $2$ and $5$ is significant, and so is the final zero after the decimal point: $4$, $2$, $0$, $5$, $0$ gives five significant figures, the same as $420.50\,\text{g}$.
  misconceptions:
    B: |-
      Believes zeros are never significant and counts only $4$, $2$ and $5$. Only leading zeros are placeholders; zeros between or after measured digits are measured too.
    C: |-
      Counts the zero between $2$ and $5$ but drops the final zero. After a decimal point, a final zero is a digit the balance actually displayed.
    D: |-
      Counts the leading zero. It appears only because the mass is written in kilograms; in grams it disappears without changing the measurement.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A match ball sits on a digital scale beside a pressure gauge, while a groundsman measures a goal](scenes/football/units_measurement.svg "A ball on a scale. Which digits on the display are real measurements?")

The physics lab has a new precision balance, and Tanya has brought her football to test it — she wants to know if her ball is inside the Laws' limits of $410$ to $450\,\text{g}$. The display settles: $420.50\,\text{g}$.

She converts for her lab record and writes: *mass of ball = 0.42050 kg, 5 significant figures*.

Her lab partner Vikram shakes his head. "Three. Only the $4$, the $2$ and the $5$ are real. Zeros are just placeholders — they hold the other digits in position. My tuition sir says so."

Mr. Menon, the lab teacher, overhears and simply asks: "Vikram, which zero is doing which job?"

Vikram looks at the number again. There are three zeros in it. Are they really all the same kind of zero?

## The common belief

"Zeros in a measurement are placeholders. They show where the decimal point goes, but they're not measured. Only the non-zero digits are significant."

## Why it feels right

Part of it is true. The zero in front of $0.42050$ really *is* just a placeholder: it exists only because the mass was written in kilograms. In grams it vanishes. And in a whole number like $1500$, the final zeros may well be placeholders — you can't tell. Students meet these cases first, so "zeros are placeholders" becomes a habit.

In everyday maths, too, zeros often feel like "nothing": $0$ runs, $0$ goals. It's natural to think they carry no information.

## What actually happens

A zero is significant or not depending on **where** it sits. Look at the three zeros in $0.42050\,\text{kg}$:

- **The leading zero** (before the $4$): a placeholder. Write the mass as $420.50\,\text{g}$ and it disappears. **Not significant.**
- **The zero between $2$ and $5$**: the balance measured the tens-of-grams digit as $2$, the grams digit as $0$ and the tenths as $5$. That zero is a reading, exactly like the $2$. **Significant.**
- **The final zero** (after the $5$): the balance displays hundredths of a gram, and it showed $0$ there. It says the mass is known to about $0.01\,\text{g}$. **Significant.**

So the reading has **five** significant figures. If Vikram's "three" were right, the mass would be known only to about $1\,\text{g}$ — throwing away a balance a hundred times more precise.

![A millimetre scale reading of 7.46 cm, with 7.4 marked as certain and the 6 as estimated](figures/significant_figures/scale-reading-certain-estimated.svg "Every digit you read from an instrument, zero or not, is part of the measurement. Only the digits that locate the decimal point are not.")

## The physics

The **significant figures** of a measurement are the reliable digits plus the first uncertain digit. The NCERT rules sort zeros by position:

1. Non-zero digits are significant.
2. **Zeros between non-zero digits are significant.**
3. Leading zeros are not significant; they only place the decimal point.
4. **Final zeros after a decimal point are significant.**
5. Final zeros in a whole number without a decimal point are ambiguous; use scientific notation to show which are significant.

![A table of six values with significant digits in green, leading zeros in grey and ambiguous zeros in orange](figures/significant_figures/counting-examples.svg "Only the grey leading zeros are pure placeholders. Zeros between digits, and final zeros after a decimal point, are measured.")

The belief treats rules 2 and 4 as if they were rule 3. Only leading zeros — and possibly final zeros in a whole number — are placeholders.

## Worked example

**Find** the significant figures in each reading (illustrative).

- $0.0305\,\text{kg}$ (a shin pad): leading zeros no; zero between $3$ and $5$ yes → **three**.
- $2.440\,\text{m}$ (goal height, by laser): final zero after the point → **four**.
- $1.50 \times 10^3\,\text{g}$ (a bag of ten cones): **three**; the power of ten removes any doubt.

**Sanity check:** convert the shin pad to grams: $30.5\,\text{g}$. Still three significant figures — the leading zeros were the only placeholders.

## Key takeaway

Not every zero is a placeholder. Leading zeros only place the decimal point; zeros between non-zero digits and final zeros after a decimal point are measured and significant. $0.42050\,\text{kg}$ has five significant figures.
