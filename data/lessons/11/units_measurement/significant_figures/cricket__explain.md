---
concept_id: significant_figures
interest: cricket
format: explain
title: Three ways to write down the same pitch
check:
  question: |-
    A groundsman weighs a new ball on a precise scale and records its mass as $0.1600\,\text{kg}$. How many significant figures does this reading have?
  options:
    A: |-
      $2$ — only the $1$ and the $6$ count
    B: |-
      $5$ — every digit written down counts
    C: |-
      $4$ — the $1$, the $6$ and both final zeros
    D: |-
      It can't be decided, because final zeros are always ambiguous
  answer: C
  explanation: |-
    The leading zero only places the decimal point, so it doesn't count. The final zeros come after the decimal point, so they are measured digits and do count: $1$, $6$, $0$, $0$ gives $4$ significant figures.
  misconceptions:
    A: |-
      Thinks final zeros are never significant. After a decimal point they are: writing $0.1600$ rather than $0.16$ says the scale really read those digits.
    B: |-
      Counts the leading zero. Zeros before the first non-zero digit only locate the decimal point; $0.1600\,\text{kg} = 160.0\,\text{g}$ has the same four significant figures.
    D: |-
      Applies the whole-number rule to a decimal. Final zeros are ambiguous only in a number with no decimal point, like $1600$.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch between the stumps with a tape while a ball sits on a scale](scenes/cricket/units_measurement.svg "Same pitch, same tape. So why do people write its length differently?")

At Sneha's cricket academy, the pitch register hangs on a nail in the groundstaff shed. Its first page, in the old curator's handwriting, says: *Pitch length 20.1 m.* Below that, Aditya, the new assistant, has written *20.12 m*; he measured it with a laser distance meter. And the coach's tablet, open on the bench, shows *20.120 m*.

Sneha reads all three twice. "Did the pitch grow?"

"They're the same," Aditya says. "The zeros and the extra two are just decoration."

The coach looks up. "They're *not* the same. Each one is telling you something different."

Sneha stares at the numbers. $20.1$, $20.12$, $20.120$ — the same length, the same pitch. What could a trailing zero possibly be telling her?

## The physics

Every measurement has an uncertainty. When you write down a measured value, the digits themselves report how precise the measurement was.

The **significant figures** in a measured value are the digits that are reliably known **plus the first digit that is uncertain**. Look at a millimetre scale:

![A millimetre scale from 7 to 8 cm with an object's edge between the 7.4 and 7.5 marks; the reading 7.46 cm has 7.4 in green as certain and 6 in orange as estimated](figures/significant_figures/scale-reading-certain-estimated.svg "The marks give 7.4 cm for certain; the 6 is your best estimate between marks. All three digits are significant.")

So *20.1 m* claims precision to about $0.1\,\text{m}$; *20.12 m* to about $0.01\,\text{m}$; and *20.120 m* to about $0.001\,\text{m}$ — a millimetre. Writing the extra zero is a claim that you really measured it. The curator had a tape and eyes; Aditya had a laser; the tablet's extra zero is only honest if something really measured to the millimetre.

**The NCERT rules for counting:**

1. All non-zero digits are significant.
2. Zeros between two non-zero digits are significant ($20.12$ has four).
3. Zeros before the first non-zero digit are **not** significant; they only place the decimal point ($0.0480$ has three).
4. Final zeros after a decimal point **are** significant ($160.0$ has four).
5. Final zeros in a whole number with no decimal point are **ambiguous** ($1500$ could have two, three or four). Use scientific notation to say which: $1.5 \times 10^3$ has two; $1.500 \times 10^3$ has four.

![A table of six values with significant digits in green, leading zeros in grey and ambiguous zeros in orange, with the rule each one shows](figures/significant_figures/counting-examples.svg "Green digits count; grey leading zeros never do; orange final zeros in a whole number are ambiguous until you use powers of ten.")

Changing units never changes the number of significant figures: $20.12\,\text{m} = 2012\,\text{cm} = 0.02012\,\text{km}$ — four in each, because the precision of the measurement hasn't changed.

## Worked example

**Find** the number of significant figures in each measured value (illustrative).

| Measured value | Significant figures | Why |
|---|---|---|
| wicket width $22.86\,\text{cm}$ | $4$ | all non-zero |
| ball mass $0.1580\,\text{kg}$ | $4$ | leading zero no; final zero after point yes |
| bat–ball contact $0.0012\,\text{s}$ | $2$ | three leading zeros don't count |
| boundary $65\,000\,\text{mm}$ | ambiguous | final zeros, no decimal point |

If the boundary was measured to the nearest metre, write it as $6.5 \times 10^4\,\text{mm}$ (two significant figures, since $65\,\text{m}$ has two).

**Sanity check:** convert $0.1580\,\text{kg}$ to $158.0\,\text{g}$ — still four significant figures, as it must be.

## Where the picture breaks

Significant figures describe **precision**, not **accuracy**. A laser meter that is badly calibrated can report $20.12\,\text{m}$ with confidence and still be wrong. And some numbers are **exact**, with no uncertainty at all: six balls in an over, or the defined $22\,\text{yards}$ in the Laws. Counted and defined numbers don't limit significant figures.

## Key takeaway

The significant figures in a measurement are the certain digits plus the first uncertain one, so they report how precise it is. Leading zeros never count; final zeros after a decimal point always do; final zeros in a whole number are ambiguous, so use scientific notation.
