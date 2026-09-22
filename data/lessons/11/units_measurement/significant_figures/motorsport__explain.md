---
concept_id: significant_figures
interest: motorsport
format: explain
title: One lap time written three different ways
check:
  question: |-
    At the finish line, the timing system records the gap between two cars as $0.0400\,\text{s}$. How many significant figures does this reading have?
  options:
    A: |-
      $3$ — the $4$ and both final zeros
    B: |-
      $1$ — only the $4$ counts
    C: |-
      $5$ — every digit written down counts
    D: |-
      It can't be decided, because final zeros are always ambiguous
  answer: A
  explanation: |-
    The zeros before the $4$ only place the decimal point, so they don't count. The final zeros come after the decimal point, so they are measured digits: $4$, $0$, $0$ gives $3$ significant figures.
  misconceptions:
    B: |-
      Thinks final zeros never count. After a decimal point they do: writing $0.0400$ instead of $0.04$ says the system really measured to a ten-thousandth of a second.
    C: |-
      Counts the leading zeros. Zeros before the first non-zero digit only locate the decimal point; $0.0400\,\text{s} = 40.0\,\text{ms}$ has the same three significant figures.
    D: |-
      Applies the whole-number rule to a decimal. Final zeros are ambiguous only in a number with no decimal point, like $5000$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A race track: a race car crosses the start-finish line under a timing screen reading 1:32.418, with a marshal holding a stopwatch](scenes/motorsport/units_measurement.svg "The screen shows thousandths of a second. The marshal's stopwatch doesn't. Do both numbers deserve the same trust?")

Rhea volunteers as a junior marshal at the state club championship. After qualifying, she has to copy the pole lap into the results book. Three sources give it to her.

The old marshal beside her, Mr. Pillai, timed it by hand: *92.4 s*. The timing screen says *1:32.418*, which is $92.418\,\text{s}$. And the team's printed spreadsheet, stuck to the pit wall, says *92.4180 s*.

"Same lap," says Rhea's friend Dev. "The spreadsheet has the most digits, so it's the best. Copy that."

Rhea hesitates. The timing system is the most precise instrument here. So how can a sheet of paper know a digit that the timing system never showed? Does that extra zero on the end mean anything at all?

## The physics

Every measurement has an uncertainty, and the digits you write down report how precise the measurement was.

The **significant figures** in a measured value are the digits that are reliably known **plus the first uncertain digit**. On a millimetre scale, you read the certain marks and estimate one more digit between them:

![A millimetre scale from 7 to 8 cm with an object's edge between the 7.4 and 7.5 marks; the reading 7.46 cm has 7.4 in green as certain and 6 in orange as estimated](figures/significant_figures/scale-reading-certain-estimated.svg "The marks give 7.4 cm for certain; the 6 is an estimate. All three digits are significant, and no digit beyond them is.")

So *92.4 s* claims precision to about $0.1\,\text{s}$ — honest for a thumb on a stopwatch. *92.418 s* claims about $0.001\,\text{s}$ — honest for an electronic timing loop. *92.4180 s* claims $0.0001\,\text{s}$, which **nothing measured**; the spreadsheet simply added a zero when formatting. Rhea should copy $92.418\,\text{s}$.

**The NCERT rules for counting:**

1. All non-zero digits are significant.
2. Zeros between non-zero digits are significant ($92.4\mathbf{0}8$ has five).
3. Zeros before the first non-zero digit are **not** significant ($0.050$ has two).
4. Final zeros after a decimal point **are** significant ($3.600$ has four).
5. Final zeros in a whole number with no decimal point are **ambiguous** ($5000$ could have one to four). Use scientific notation: $5.0 \times 10^3$ has two, $5.000 \times 10^3$ has four.

![A table of six values with significant digits in green, leading zeros in grey and ambiguous zeros in orange, with the rule each one shows](figures/significant_figures/counting-examples.svg "Green digits count; grey leading zeros never do; orange final zeros in a whole number stay ambiguous until you write a power of ten.")

Changing units never changes the count: $92.418\,\text{s} = 92\,418\,\text{ms}$ — five significant figures either way, because the measurement is the same.

## Worked example

**Find** the number of significant figures in each value (illustrative figures).

| Measured value | Significant figures | Why |
|---|---|---|
| lap time $92.418\,\text{s}$ | $5$ | all non-zero |
| gap to second place $0.050\,\text{s}$ | $2$ | leading zeros no; final zero after point yes |
| wheelbase $3.600\,\text{m}$ | $4$ | final zeros after the point count |
| track length $5000\,\text{m}$ | ambiguous | final zeros, no decimal point |

If the track was measured to the nearest $10\,\text{m}$, write it as $5.00 \times 10^3\,\text{m}$ — three significant figures, and no ambiguity.

**Sanity check:** convert the gap to milliseconds: $0.050\,\text{s} = 50\,\text{ms}$. Written as $50\,\text{ms}$ the zero looks ambiguous, so $5.0 \times 10^1\,\text{ms}$ is the honest form — two significant figures, the same as before.

## Where the picture breaks

Significant figures describe **precision**, not **accuracy**. A timing loop that is set up slightly wrong could print $92.418\,\text{s}$ with full confidence and still be off. And some numbers are **exact**, with no uncertainty: a race of 20 laps, or a car's grid slot number. Counted and defined numbers never limit significant figures.

## Key takeaway

Significant figures are the certain digits plus the first uncertain one, so they show how precise a measurement is. Leading zeros never count; final zeros after a decimal point always do; final zeros in a whole number are ambiguous, so use scientific notation. Never write a digit that nothing measured.
