---
concept_id: significant_figures
interest: smartphones
format: explain
title: Does a phone get thinner in metres
check:
  question: |-
    A digital caliper reads a phone's thickness as $7.90\,\text{mm}$. Written in metres, that is $0.00790\,\text{m}$. How many significant figures does $0.00790\,\text{m}$ have?
  options:
    A: |-
      $3$ — the $7$, the $9$ and the final zero
    B: |-
      $6$ — every digit written down counts
    C: |-
      $2$ — only the $7$ and the $9$ count
    D: |-
      $5$ — every digit after the decimal point counts
  answer: A
  explanation: |-
    The zeros before the $7$ only place the decimal point, so they don't count. The final zero comes after the decimal point, so it is a measured digit and does count: $7$, $9$, $0$ gives $3$ — the same as $7.90\,\text{mm}$, because changing units can't change precision.
  misconceptions:
    B: |-
      Counts the leading zeros as if they were measured. They only appear because a metre is a big unit; in millimetres the same reading is $7.90$, with no leading zeros at all.
    C: |-
      Thinks a final zero is never significant. After a decimal point it is: the caliper really read that $0$, which is why it's written $7.90$ and not $7.9$.
    D: |-
      Counts decimal places instead of significant figures. The number of digits after the point depends on the unit chosen; significant figures don't.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A study desk: a phone in the jaws of a digital caliper that reads 7.92 mm, a phone on a scale, a charger and USB meter](scenes/smartphones/units_measurement.svg "The caliper shows three digits. How many of them does it really know?")

Meera's school science club is 3D-printing a phone stand, and the slot has to fit her phone snugly. So she measures its thickness three ways.

Her geometry-box ruler: about $8\,\text{mm}$. The lab's vernier callipers: $7.9\,\text{mm}$. The club's new digital caliper, beeping as it closes: $7.92\,\text{mm}$.

Her friend Farah types the last one into the printer software, which wants metres: $0.00792\,\text{m}$. She grins. "Look — six digits now! Converting to metres made your measurement *way* more precise. Let's always use metres."

Meera frowns. The phone hasn't changed. The caliper hasn't changed. Only the unit has. Can writing a number in a different unit really make a measurement more precise? And if not, which of those digits is actually telling her something?

## The physics

Every measurement has some uncertainty, and the digits you write down report how precise the measurement was.

The **significant figures** in a measured value are the digits that are reliably known **plus the first digit that is uncertain**. On a scale, you read the marks for certain and estimate the last digit between them:

![A millimetre scale from 7 to 8 cm with an object's edge between the 7.4 and 7.5 marks; the reading 7.46 cm has 7.4 in green as certain and 6 in orange as estimated](figures/significant_figures/scale-reading-certain-estimated.svg "The marks give 7.4 cm for certain; the 6 is your best estimate between marks. All three digits are significant.")

So Meera's three readings make three different claims: *8 mm* is good to about a millimetre (one significant figure); *7.9 mm* to about a tenth of a millimetre (two); *7.92 mm* to about a hundredth of a millimetre (three).

**The NCERT rules for counting:**

1. All non-zero digits are significant.
2. Zeros between two non-zero digits are significant ($1.05$ has three).
3. Zeros before the first non-zero digit are **not** significant; they only place the decimal point ($0.00792$ has three).
4. Final zeros after a decimal point **are** significant ($7.90$ has three).
5. Final zeros in a whole number with no decimal point are **ambiguous** ($5000$ could have one, two, three or four). Scientific notation settles it: $5.0 \times 10^3$ has two; $5.000 \times 10^3$ has four.

![A table of six values with significant digits in green, leading zeros in grey and ambiguous zeros in orange, with the rule each one shows](figures/significant_figures/counting-examples.svg "Green digits count; grey leading zeros never do; orange final zeros in a whole number are ambiguous until you use powers of ten.")

Now Farah's claim falls apart. The zeros in $0.00792\,\text{m}$ are grey zeros: they appear only because a metre is enormous compared with a phone's thickness. **Changing units never changes the number of significant figures**: $7.92\,\text{mm} = 0.792\,\text{cm} = 0.00792\,\text{m} = 7.92 \times 10^{-3}\,\text{m}$ — three significant figures every time. Scientific notation makes this obvious, because only the significant digits stay in front of the power of ten.

## Worked example

**Find** the number of significant figures in each measured value (illustrative gadget measurements).

| Measured value | Significant figures | Why |
|---|---|---|
| screen diagonal $16.51\,\text{cm}$ | $4$ | all non-zero |
| charging cable $1.00\,\text{m}$ | $3$ | final zeros after the point count |
| one earbud $0.0045\,\text{kg}$ | $2$ | three leading zeros don't count |
| a stand's slot $10.05\,\text{mm}$ | $4$ | the zero between $1$ and $5$ counts |
| battery "$5000\,\text{mAh}$" | ambiguous | final zeros, no decimal point |

If the battery figure is only known to the nearest hundred, write it as $5.0 \times 10^3\,\text{mAh}$ (two significant figures).

**Sanity check:** convert the earbud to grams: $0.0045\,\text{kg} = 4.5\,\text{g}$ — still two significant figures, as it must be.

## Where the picture breaks

Significant figures describe **precision**, not **accuracy**. A digital caliper with dirt on its jaws, or one not zeroed before use, will happily show $7.92\,\text{mm}$ and still be wrong. A digital display can also show more digits than the instrument can honestly resolve, so the last digit on a screen isn't automatically trustworthy. And counted or defined numbers are **exact** — two earbuds in a case, $1000\,\text{mm}$ in a metre — so they have no uncertainty to report.

## Key takeaway

Significant figures are the certain digits plus the first uncertain one, so they tell you how precise a measurement is. Leading zeros never count, final zeros after a decimal point always do, and final zeros in a whole number are ambiguous until you use scientific notation. Changing units never changes the count.
