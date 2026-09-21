---
concept_id: significant_figures
interest: cricket
format: challenge
title: Does a run-up get more precise in kilometres
check:
  question: |-
    A bowler's run-up is recorded in a spreadsheet as $0.02250\,\text{km}$. How many significant figures does this value have?
  options:
    A: |-
      $4$
    B: |-
      $6$
    C: |-
      $3$
    D: |-
      $5$
  answer: A
  explanation: |-
    The zeros before the $2$ only place the decimal point. The significant digits are $2$, $2$, $5$ and the final $0$, which comes after the decimal point and so counts: four. It is the same measurement as $22.50\,\text{m}$.
  misconceptions:
    B: |-
      Counts every digit written, including the leading zeros — but those appear only because of the unit chosen, not because anything was measured.
    C: |-
      Drops the final zero, thinking trailing zeros never count. After a decimal point a final zero is a measured digit.
    D: |-
      Counts the zero just after the decimal point as if it sat between non-zero digits. It comes before the first non-zero digit, so it only places the decimal point.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch with a tape while a speed display glows](scenes/cricket/units_measurement.svg "A tape measure gives a number. How you write it down decides what it claims.")

Harpreet is the fastest bowler in her college team, and her run-up is sacred. Before every season, she measures it from the bowling crease with a steel tape and marks it with a white disc: $22.50\,\text{m}$.

Pooja, the team's scorer, keeps a spreadsheet of everything. She types the run-up as *0.02250 km*. "Kilometres is more scientific," she explains. "And look — six digits now. It's more precise than your $22.50$."

Harpreet's brother Manav, reading over her shoulder, disagrees for a completely different reason: "Wrong way round. Those zeros in front are nothing. It's *less* precise now."

Harpreet just wants to know whether her run-up has changed. Has it? Is one of them right?

## The challenge

Harpreet's run-up, measured once with a steel tape, is written four ways:

- $22.50\,\text{m}$
- $2250\,\text{cm}$
- $0.02250\,\text{km}$
- $22\,500\,\text{mm}$

How many significant figures does each version have? Which ones are fair records of the measurement, and how would you fix any that aren't?

## Think first

Pooja says the kilometre version has more digits, so it must be more precise. Manav says leading zeros make it less precise. Maybe the centimetre and millimetre versions, with zeros at the end, are the most precise of all? Count the significant figures in each before reading on.

## The reveal

Start from what was actually measured: $22.50\,\text{m}$. The tape reads to the nearest centimetre, so the $5$ is certain and the final $0$ is the estimated digit. That's **four** significant figures.

Now convert. A change of unit moves the decimal point; it cannot change how carefully the tape was read.

- $0.02250\,\text{km}$: the zeros in front only place the decimal point, so they don't count. The final zero comes after the decimal point, so it does. **Four.** Pooja's "six digits" includes two zeros that say nothing about the measurement; Manav's "less precise" is wrong for the same reason — those zeros don't *remove* precision either.
- $2250\,\text{cm}$: a whole number ending in zero, with no decimal point. By the NCERT rules its final zero is **ambiguous**: a reader can't tell whether it was measured.
- $22\,500\,\text{mm}$: also ambiguous, and worse: it could be read as claiming a millimetre, which the tape never gave.

The fix is scientific notation, which shows the significant figures directly:

$$2.250 \times 10^3\,\text{cm} \qquad 2.250 \times 10^4\,\text{mm}$$

Both clearly have four significant figures, like $22.50\,\text{m}$ and $0.02250\,\text{km}$. Harpreet's run-up hasn't changed at all.

## The physics

The **significant figures** of a measured value are its reliable digits plus the first uncertain digit. They report precision, so they depend on the measurement, not on the unit.

![A table of six values with significant digits in green, leading zeros in grey and ambiguous zeros in orange](figures/significant_figures/counting-examples.svg "Leading zeros (grey) never count. Final zeros count after a decimal point; in a whole number they are ambiguous until written in powers of ten.")

The NCERT rules:

1. All non-zero digits count.
2. Zeros between non-zero digits count.
3. Leading zeros (before the first non-zero digit) never count.
4. Final zeros after a decimal point count.
5. Final zeros in a whole number without a decimal point are ambiguous; remove the doubt with scientific notation, $a \times 10^b$, where every digit of $a$ is significant.

## Key takeaway

Changing the unit never changes the number of significant figures, because it doesn't change how precisely you measured. $22.50\,\text{m}$, $0.02250\,\text{km}$ and $2.250 \times 10^3\,\text{cm}$ all have four. When zeros at the end of a whole number would be ambiguous, write it in scientific notation.
