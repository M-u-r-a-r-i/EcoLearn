---
concept_id: significant_figures_arithmetic
interest: cricket
format: challenge
title: Sizing the rain cover for the pitch
check:
  question: |-
    A groundsman adds three lengths: $20.12\,\text{m}$ (measured with a tape), $1.5\,\text{m}$ (paced out) and $0.365\,\text{m}$ (measured with a steel rule). Reported correctly, the total is:
  options:
    A: |-
      $21.985\,\text{m}$
    B: |-
      $22\,\text{m}$
    C: |-
      $22.0\,\text{m}$
    D: |-
      $21.99\,\text{m}$
  answer: C
  explanation: |-
    The sum is $21.985\,\text{m}$. In addition, keep the fewest decimal places: $1.5\,\text{m}$ has one, so round to one decimal place. The dropped digits $85$ are more than half of $0.1$, so $21.985 \to 22.0\,\text{m}$.
  misconceptions:
    A: |-
      Keeps every digit of the sum. The paced $1.5\,\text{m}$ is unknown in the hundredths and thousandths places, so those digits of the total are unknown too.
    B: |-
      Uses the multiplication rule (fewest significant figures, two, from $1.5$) for a sum. Addition keeps decimal places, so the answer is $22.0$, not $22$.
    D: |-
      Keeps two decimal places, as in the tape reading $20.12$ — but a sum is limited by its least precise term, not its most precise one.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch between the stumps with a tape](scenes/cricket/units_measurement.svg "Before you can cover a pitch, you have to measure it — and then decide how many digits to trust.")

The forecast says heavy rain tomorrow, and the old pitch cover has finally torn. Mr. Bhattacharya, the head groundsman, sends his two helpers to measure the pitch so he can order a new cover sheet.

Salim runs the steel tape: $20.12\,\text{m}$ long and $3.05\,\text{m}$ wide. Deepa multiplies on her phone. "Area is $61.366$ square metres," she announces.

"Write $61$," Salim says. "Nobody measures grass to three decimal places."

"But the calculator says $61.366$," Deepa replies. "Why would I throw away digits?"

Mr. Bhattacharya adds one more instruction: the cover must overhang by about $1.5$ metres at each end, which he paces out by eye. Neither helper is sure how to write the total length either. Whose number goes on the order form?

## The challenge

The pitch is measured as $20.12\,\text{m}$ long and $3.05\,\text{m}$ wide (the Laws give $10\,\text{ft}$, about $3.05\,\text{m}$). The overhang is paced as $1.5\,\text{m}$ at each end.

1. What is the area of the pitch, reported to the correct number of significant figures?
2. What is the total length of cover needed, reported correctly?

## Think first

Is Deepa right to keep all the calculator digits, or Salim right to round to a whole number? Or neither? For the length, does $20.12 + 1.5 + 1.5$ keep two decimal places, one, or none? Are the rules for multiplying and adding even the same? Decide before reading on.

## The reveal

**Part 1: a product.** Multiplying or dividing, the result keeps as many **significant figures** as the least precise factor.

- $20.12\,\text{m}$ has four significant figures.
- $3.05\,\text{m}$ has three.

$$A = 20.12\,\text{m} \times 3.05\,\text{m} = 61.366\,\text{m}^2 \approx 61.4\,\text{m}^2$$

Three significant figures. The first dropped digit is $6$, more than $5$, so the $3$ rounds up to $4$.

![Left: adding 20.12 and 1.5 gives 21.62, rounded to 21.6. Right: 20.12 times 3.05 gives 61.366, rounded to 61.4](figures/significant_figures_arithmetic/add-vs-multiply-rules.svg "Two different rules. For the area, count significant figures; for the cover length, count decimal places.")

Deepa's $61.366$ claims five significant figures, more than either measurement had. Salim's $61$ throws away a figure the tape really gave. Neither is right.

**Part 2: a sum.** Adding or subtracting, the result keeps as many **decimal places** as the term with the fewest.

$$L = 20.12\,\text{m} + 1.5\,\text{m} + 1.5\,\text{m} = 23.12\,\text{m} \approx 23.1\,\text{m}$$

The paced $1.5\,\text{m}$ is known only to the tenths place, so the hundredths digit of the sum is unknown: one decimal place. (Here that is also three significant figures — but that's a coincidence. The rule for sums is about decimal places.)

So the order form says: pitch area $61.4\,\text{m}^2$, cover length $23.1\,\text{m}$.

## The physics

NCERT's rules for arithmetic with measured values:

- **Multiplication and division:** keep as many significant figures as the value with the fewest significant figures.
- **Addition and subtraction:** keep as many decimal places as the value with the fewest decimal places.

**Rounding (NCERT):** if the first dropped digit is more than $5$, raise the preceding digit; if less than $5$, leave it. If the dropped digit is exactly $5$, leave an even preceding digit unchanged and raise an odd one ($2.745 \to 2.74$, $2.735 \to 2.74$).

Round only once, at the end. In multi-step work, carry one extra digit through the intermediate steps so that rounding errors don't pile up. Exact numbers, such as "two ends" or "six balls", never limit the result.

## Key takeaway

A product is only as precise, in significant figures, as its least precise factor: $20.12 \times 3.05 \to 61.4\,\text{m}^2$. A sum is only as precise, in decimal places, as its least precise term: $20.12 + 1.5 + 1.5 \to 23.1\,\text{m}$.
