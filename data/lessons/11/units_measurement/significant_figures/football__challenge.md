---
concept_id: significant_figures
interest: football
format: challenge
title: Does the pitch get more precise in millimetres
check:
  question: |-
    A sports-science app records a goalkeeper's reaction time as $0.0280\,\text{s}$. How many significant figures does this value have?
  options:
    A: |-
      $5$
    B: |-
      $2$
    C: |-
      $4$
    D: |-
      $3$
  answer: D
  explanation: |-
    The zeros before the $2$ only place the decimal point. The significant digits are $2$, $8$ and the final $0$, which comes after the decimal point and so is a measured digit: three. It is the same value as $28.0\,\text{ms}$.
  misconceptions:
    A: |-
      Counts every digit written, including the leading zeros — but they appear only because of the unit chosen, not because anything was measured.
    B: |-
      Drops the final zero, thinking trailing zeros never count. After a decimal point, a final zero is a measured digit.
    C: |-
      Counts the zero just after the decimal point as if it sat between non-zero digits. It comes before the first non-zero digit, so it only places the decimal point.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal with a tape; a match clock stands above the stands](scenes/football/units_measurement.svg "A tape measure gives a number. How you write it down decides what it claims.")

Before the new season, Gurpreet, head groundsman at the municipal stadium, re-measures the pitch with a long surveyor's tape, reading it to the nearest ten centimetres. Touchline to touchline along its length: $105.0\,\text{m}$. He writes it on the job card.

Devika, an intern in the club office, enters it into the facilities spreadsheet as *0.1050 km*. "Kilometres look more professional," she says. "And now it has five digits instead of four — more precise."

Her colleague Ravi prefers millimetres and types *105000 mm*. "Six digits," he grins. "I win."

Gurpreet reads both over their shoulders and scratches his head. He measured the pitch once, with one tape, on one morning. Has anyone's number really become more precise than his?

## The challenge

Gurpreet's single measurement is written four ways:

- $105.0\,\text{m}$
- $0.1050\,\text{km}$
- $10\,500\,\text{cm}$
- $105\,000\,\text{mm}$

How many significant figures does each version have? Which are fair records of the measurement, and how would you fix the ones that aren't?

## Think first

Devika says the kilometre version has more digits, so it's more precise. Ravi says his has even more. Or perhaps the zeros in front of $0.1050$ make it *less* precise? Count the significant figures in each version before you read on.

## The reveal

Start with what was actually measured. The tape was read to the nearest $0.1\,\text{m}$, so in $105.0\,\text{m}$ the final $0$ is the uncertain digit. That's **four** significant figures: $1$, $0$ (between non-zero digits), $5$, and the final $0$.

A change of unit only moves the decimal point. It can't change how carefully the tape was read.

- $0.1050\,\text{km}$: the leading zero only places the decimal point, so it doesn't count; the final zero comes after the decimal point, so it does. **Four.** Devika's "five digits" includes a zero that says nothing about the measurement.
- $10\,500\,\text{cm}$: a whole number ending in zeros, with no decimal point. By the NCERT rules its final zeros are **ambiguous**. A reader can't tell whether the tens and units of centimetres were measured.
- $105\,000\,\text{mm}$: also ambiguous — and it could be misread as a measurement to the millimetre, which the tape never gave. Ravi's "six digits" claim more than Gurpreet ever measured.

Scientific notation fixes both, because every digit in front of the power of ten is significant:

$$1.050 \times 10^4\,\text{cm} \qquad 1.050 \times 10^5\,\text{mm}$$

Four significant figures each, exactly like $105.0\,\text{m}$. The pitch is no more precise in any unit.

## The physics

The **significant figures** of a measured value are its reliable digits plus the first uncertain digit. They report the precision of the measurement, so they depend on the instrument and the reading — never on the unit.

![A table of six values with significant digits in green, leading zeros in grey and ambiguous zeros in orange](figures/significant_figures/counting-examples.svg "Leading zeros (grey) never count. Final zeros count after a decimal point; in a whole number they are ambiguous until written in powers of ten.")

The NCERT rules:

1. All non-zero digits count.
2. Zeros between non-zero digits count.
3. Leading zeros never count.
4. Final zeros after a decimal point count.
5. Final zeros in a whole number without a decimal point are ambiguous; remove the doubt with scientific notation, $a \times 10^b$, where every digit of $a$ is significant.

## Worked example

**Given:** the goal's height, measured with a steel tape to the nearest centimetre, is $2.44\,\text{m}$.
**Find:** a fair way to write it in centimetres, millimetres and kilometres.

The measurement has three significant figures. In centimetres, $244\,\text{cm}$ (three, with no trailing zeros to worry about). In millimetres, $2440\,\text{mm}$ would be ambiguous, so write $2.44 \times 10^3\,\text{mm}$. In kilometres, $0.00244\,\text{km}$ — three, since leading zeros don't count.

**Sanity check:** each version has the same three significant digits, $2$, $4$, $4$, as it must.

## Key takeaway

Changing the unit never changes the number of significant figures, because it doesn't change how precisely you measured. $105.0\,\text{m}$, $0.1050\,\text{km}$ and $1.050 \times 10^5\,\text{mm}$ all have four. Where final zeros in a whole number would be ambiguous, use scientific notation.
