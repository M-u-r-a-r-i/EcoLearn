---
concept_id: significant_figures
interest: cricket
format: misconception
title: Is a zero at the end of a measurement just padding
check:
  question: |-
    Four students record the length of the same bat's blade. Which record claims the most precise measurement?
  options:
    A: |-
      $56\,\text{cm}$
    B: |-
      $0.56\,\text{m}$
    C: |-
      $560\,\text{mm}$
    D: |-
      $56.0\,\text{cm}$
  answer: D
  explanation: |-
    $56.0\,\text{cm}$ has three significant figures, claiming precision to about $0.1\,\text{cm}$. $56\,\text{cm}$ and $0.56\,\text{m}$ have two; in $560\,\text{mm}$ the final zero is ambiguous, so it does not clearly claim a third figure.
  misconceptions:
    A: |-
      Treats $56$ and $56.0$ as the same measurement because they are the same number in maths — but the final zero after the decimal point is a measured digit.
    B: |-
      Thinks a decimal point or a bigger unit makes a value look more precise. $0.56\,\text{m}$ has only two significant figures; the leading zero doesn't count.
    C: |-
      Thinks more digits mean more precision. The final zero in a whole number without a decimal point is ambiguous — it may just be a placeholder.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch with a tape; a ball sits on a scale and a stopwatch reads 3.50 seconds](scenes/cricket/units_measurement.svg "Tapes, scales and stopwatches: each shows a certain number of digits, and none of them is padding.")

Mohit has brought his new bat to the physics lab. The experiment is on vernier callipers, and he has decided the blade is more interesting than the metal cylinder on his bench. The callipers close gently on the blade's width. He reads the scales carefully: $10.60\,\text{cm}$.

In his notebook, he writes *10.6 cm*.

Mrs. Kulkarni, walking past, circles it in red. "You measured a digit and then threw it away."

"Ma'am, $10.6$ and $10.60$ are the same number," Mohit says. "The zero doesn't do anything. My maths teacher would say so too."

His maths teacher probably would. So who is right — and how can a zero at the end of a number carry any information at all?

## The common belief

"Zeros at the end of a decimal don't matter. $10.6$ and $10.60$ are equal, so they're the same measurement. Writing the zero is just padding, like writing ₹10.60 instead of ₹10.6."

## Why it feels right

In mathematics, Mohit is completely right: $10.6 = 10.60$ exactly. Calculators drop trailing zeros automatically. In prices, ₹10.6 and ₹10.60 mean the same amount. Years of maths have taught students that a trailing zero after the decimal point changes nothing, and for exact numbers that's true.

The catch is that a **measurement is not an exact number**.

## What actually happens

A measured value carries its uncertainty in its digits. The significant figures are the reliable digits plus the first uncertain one.

![A millimetre scale reading of 7.46 cm, with 7.4 marked as certain and the 6 as estimated](figures/significant_figures/scale-reading-certain-estimated.svg "The last digit written is the one you estimated. Drop it, and you tell the reader you never saw it.")

Mohit's vernier callipers read to $0.01\,\text{cm}$. So $10.60\,\text{cm}$ says: the width is known to about a hundredth of a centimetre, and the final $0$ is the uncertain digit. Four significant figures.

*10.6 cm* says something weaker: known only to the nearest tenth, so anything from about $10.55$ to $10.65\,\text{cm}$ would fit. Three significant figures. That range is ten times wider. Mohit didn't just drop a zero; he threw away the extra precision the callipers gave him.

The mistake also runs the other way. With a plain ruler that reads to $0.1\,\text{cm}$, writing $10.60\,\text{cm}$ would claim a digit nobody measured.

## The physics

The NCERT rules for significant figures:

1. Non-zero digits are significant.
2. Zeros between non-zero digits are significant.
3. Leading zeros are not significant; they only place the decimal point.
4. **Final zeros after a decimal point are significant.** This is exactly where the belief goes wrong.
5. Final zeros in a whole number without a decimal point are ambiguous; write the value in scientific notation to show which are significant.

![A table of six measured values, with significant digits in green and non-significant ones in grey](figures/significant_figures/counting-examples.svg "160.0 g has four significant figures; 0.0480 kg has three. The final zeros count in both.")

The number of significant figures depends on the instrument and the reading, not on the unit: $10.60\,\text{cm} = 106.0\,\text{mm} = 0.1060\,\text{m}$, four significant figures each time.

## Worked example

**Given:** a blade width read as $10.6\,\text{cm}$ on a ruler and as $10.60\,\text{cm}$ on vernier callipers.
**Find:** the number of significant figures in each, and roughly how uncertain each is.

- Ruler: $10.6\,\text{cm}$ has three significant figures; the last digit is uncertain by about $0.1\,\text{cm}$.
- Callipers: $10.60\,\text{cm}$ has four; the last digit is uncertain by about $0.01\,\text{cm}$.

**Sanity check:** the vernier reading is about ten times more precise, and that shows up as exactly one extra significant figure — the final zero.

## Key takeaway

In a measurement, a final zero after the decimal point is a measured digit, not padding. $10.60\,\text{cm}$ and $10.6\,\text{cm}$ are equal numbers but different measurements: four significant figures versus three. Write every digit you measured, and none you didn't.
