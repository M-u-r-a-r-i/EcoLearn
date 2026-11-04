---
concept_id: significant_figures
interest: football
format: explain
title: Three ways to write down the same match ball
check:
  question: |-
    A kit manager measures the length of a boot stud with vernier callipers and records it as $0.01050\,\text{m}$. How many significant figures does this reading have?
  options:
    A: |-
      $6$ — every digit written down counts
    B: |-
      $4$ — the $1$, the $0$ after it, the $5$ and the final $0$
    C: |-
      $3$ — the $1$, the $0$ after it and the $5$
    D: |-
      $2$ — only the $1$ and the $5$ count
  answer: B
  explanation: |-
    The two leading zeros only place the decimal point, so they don't count. The zero between $1$ and $5$ counts, and the final zero after the decimal point is a measured digit, so it counts too: $4$ significant figures.
  misconceptions:
    A: |-
      Counts the leading zeros. They appear only because the stud was written in metres; in millimetres the same reading is $10.50\,\text{mm}$, with four significant figures.
    C: |-
      Thinks final zeros are never significant. After a decimal point, a final zero says the callipers really read that digit.
    D: |-
      Thinks zeros never count. A zero between two non-zero digits, or at the end after a decimal point, is a measured digit like any other.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal with a tape while a match ball sits on a scale](scenes/football/units_measurement.svg "The same ball can be measured with different tools. Do the numbers say the same thing?")

Meera is the kit manager for her college team, and before the league starts she checks every match ball against the rules: circumference between $68$ and $70\,\text{cm}$.

For ball number 7, she finds three records. The coach's notebook says *69 cm*. Meera's own tailor's-tape reading from last month says *68.6 cm*. And the new equipment app, where somebody typed a measurement made with a flexible steel tape, says *68.60 cm*.

"They're all the same ball," says Sahil, the captain, bored. "The app just adds a zero to look fancy. $68.6$ and $68.60$ are equal numbers."

Meera isn't so sure. The coach said $69$, not $68.6$, and nobody thinks he measured a different ball. If the numbers are "the same", why does each person write them differently — and could a zero at the end really be telling her something?

## The physics

Every measurement has some uncertainty, and the digits you write down report how precise the measurement was.

The **significant figures** in a measured value are the digits that are reliably known **plus the first digit that is uncertain**. Look at a millimetre scale:

![A millimetre scale from 7 to 8 cm with an object's edge between the 7.4 and 7.5 marks; the reading 7.46 cm has 7.4 in green as certain and 6 in orange as estimated](figures/significant_figures/scale-reading-certain-estimated.svg "The marks give 7.4 cm for certain; the 6 is your best estimate between marks. All three digits are significant.")

So *69 cm* claims precision to about $1\,\text{cm}$; *68.6 cm* to about $0.1\,\text{cm}$; *68.60 cm* to about $0.01\,\text{cm}$. They are the same ball measured with different care. The final zero in $68.60$ is a claim that somebody really read the hundredths — honest only if the steel tape could.

**The NCERT rules for counting:**

1. All non-zero digits are significant.
2. Zeros between two non-zero digits are significant ($7.032$ has four).
3. Zeros before the first non-zero digit are **not** significant; they only place the decimal point ($0.0480$ has three).
4. Final zeros after a decimal point **are** significant ($68.60$ has four).
5. Final zeros in a whole number with no decimal point are **ambiguous** ($1500$ could have two, three or four). Scientific notation settles it: $1.5 \times 10^3$ has two, $1.500 \times 10^3$ has four.

![A table of six values with significant digits in green, leading zeros in grey and ambiguous zeros in orange, with the rule each one shows](figures/significant_figures/counting-examples.svg "Green digits count; grey leading zeros never do; orange final zeros in a whole number stay ambiguous until you use powers of ten.")

Changing units never changes the count: $68.60\,\text{cm} = 686.0\,\text{mm} = 0.6860\,\text{m}$ — four each time, because the measurement hasn't changed.

## Worked example

**Find** the number of significant figures in each measured value (illustrative).

| Measured value | Significant figures | Why |
|---|---|---|
| goal width $7.32\,\text{m}$ | $3$ | all non-zero |
| ball mass $0.430\,\text{kg}$ | $3$ | leading zero no; final zero after point yes |
| stud length $0.012\,\text{m}$ | $2$ | leading zeros don't count |
| pitch length $105\,000\,\text{mm}$ | ambiguous | final zeros, no decimal point |

If the pitch was measured to the nearest $0.1\,\text{m}$, as $105.0\,\text{m}$, write it as $1.050 \times 10^5\,\text{mm}$: four significant figures, now visible.

**Sanity check:** in grams, $0.430\,\text{kg} = 4.30 \times 10^2\,\text{g}$ — still three significant figures. Written plainly as $430\,\text{g}$, the final zero would look ambiguous, which is why the power of ten is the safer way to write it.

## Where the picture breaks

Significant figures describe **precision**, not **accuracy**. A stretched tailor's tape can give a very precise-looking $68.60\,\text{cm}$ and still be wrong. And some numbers are **exact**, with no uncertainty: eleven players a side, two halves. Counted numbers, and values fixed by definition, never limit significant figures. (The Laws' $68$–$70\,\text{cm}$ is a permitted range, not a measurement.)

## Key takeaway

Significant figures are the certain digits plus the first uncertain one, so they report how precisely something was measured. Leading zeros never count; zeros between non-zero digits always count; final zeros after a decimal point count; final zeros in a whole number are ambiguous — use scientific notation.
