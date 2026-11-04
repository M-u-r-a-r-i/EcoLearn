---
concept_id: significant_figures_arithmetic
interest: gaming
format: explain
title: How many digits a screen measurement deserves
check:
  question: |-
    A slow-motion video shows a player's mouse sliding $34.5\,\text{cm}$ in a full flick lasting $0.42\,\text{s}$. The mouse's average speed, reported to the correct number of significant figures, is:
  options:
    A: |-
      $82.1\,\text{cm/s}$
    B: |-
      $82.142\,857\,\text{cm/s}$
    C: |-
      $82\,\text{cm/s}$
    D: |-
      $82.14\,\text{cm/s}$
  answer: C
  explanation: |-
    $34.5/0.42 = 82.14\ldots$. In a quotient, keep as many significant figures as the least precise value: $0.42\,\text{s}$ has two, so the answer is $82\,\text{cm/s}$.
  misconceptions:
    A: |-
      Keeps the three significant figures of the more precise value, $34.5\,\text{cm}$. A result can't be more precise than its roughest measurement, the time.
    B: |-
      Copies the calculator display. Most of those digits are meaningless, because the time was measured to only two significant figures.
    D: |-
      Uses a decimal-places idea meant for addition and copies the two decimal places of $0.42$. Division is governed by significant figures, not decimal places.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk with a monitor, and a yellow tape measure stretched along the top edge of the screen](scenes/gaming/units_measurement.svg "The tape reads to a millimetre at best. How many digits can a calculation from it keep?")

Tara is writing a desk-setup review for her school's tech blog. She stretches a tape across her monitor's screen: $59.8\,\text{cm}$ wide and $33.6\,\text{cm}$ tall. She also measures the gap she'll leave between this screen and a second, identical one: $1.27\,\text{cm}$, with her father's vernier calipers.

Then she opens the calculator. Screen area: *2009.28*. Width of both screens plus the gap: *120.87*. Width divided by height: *1.779761905*.

Her brother Kabir reads over her shoulder. "Put all of that in the review. Nine decimal places looks serious. People will think you used lab equipment."

Tara hesitates. Her tape can't see a tenth of a millimetre, let alone a billionth of anything. So which of these digits has she actually earned — and is the rule the same for adding as for multiplying?

## The physics

A result calculated from measured values can't be more precise than the data. NCERT gives two rules.

**Multiplying or dividing:** keep as many **significant figures** as the value with the fewest significant figures.

**Adding or subtracting:** keep as many **decimal places** as the value with the fewest decimal places.

![Left: 20.12 plus 1.5 gives 21.62, rounded to 21.6 because 1.5 has one decimal place. Right: 20.12 times 3.05 gives 61.366, rounded to 61.4 because 3.05 has three significant figures](figures/significant_figures_arithmetic/add-vs-multiply-rules.svg "Adding: an unknown hundredths digit in one value spoils the hundredths of the sum. Multiplying: the answer keeps the significant figures of the least precise factor.")

Why two rules? In a sum, the **position** of the last reliable digit matters: if one width is known only to the tenth of a centimetre, the hundredths of the total can't be known. In a product, the **relative** precision matters, and that is what significant figures measure.

**Rounding off (NCERT):** look at the first digit you drop.

- More than $5$: raise the preceding digit by $1$.
- Less than $5$: leave the preceding digit unchanged.
- Exactly $5$ with nothing after it: leave an even preceding digit, raise an odd one. So $6.965 \to 6.96$ but $6.975 \to 6.98$.

**Exact numbers** — counted or defined, like "two screens" or the $16$ and $9$ of a 16:9 format — have unlimited significant figures and never limit a result. In multi-step work, keep one extra digit in intermediate results and round only at the end.

## Worked example

**Given:** screen width $w = 59.8\,\text{cm}$ and height $h = 33.6\,\text{cm}$ (three significant figures each, one decimal place); gap $g = 1.27\,\text{cm}$ (two decimal places). Illustrative values.
**Find:** (a) the screen area; (b) the total width of two screens plus the gap; (c) the width-to-height ratio.

(a) A product, so three significant figures:

$$A = 59.8 \times 33.6 = 2009.28\,\text{cm}^2 \approx 2.01 \times 10^3\,\text{cm}^2$$

Writing $2010$ would leave the final zero ambiguous; scientific notation shows exactly three figures.

(b) A sum. The "two" screens is an exact count:

$$2 \times 59.8 + 1.27 = 119.6 + 1.27 = 120.87\,\text{cm} \approx 120.9\,\text{cm}$$

One decimal place, because $59.8$ has only one. The dropped $7$ is more than $5$, so the $8$ becomes $9$.

(c) A quotient, three significant figures:

$$\frac{w}{h} = \frac{59.8}{33.6} = 1.7797\ldots \approx 1.78$$

**Sanity check:** a 16:9 screen has an exact ratio $16/9 = 1.7778$, which also rounds to $1.78$. Tara's measurement agrees with the format to three figures, and that is all it can claim.

## Where the picture breaks

These rules are a quick estimate of precision, not a full error calculation — the next lesson on errors does that properly. They also ignore how well the tape was *used*: a tape held at a slight angle adds an error the digits can't show. And the area in (a) is the area of the visible screen as Tara measured it, not a manufacturer's specification.

## Key takeaway

Multiplying or dividing: keep the fewest significant figures of the data. Adding or subtracting: keep the fewest decimal places. Round only at the end, using the NCERT rounding rules, and never let an exact count limit the answer.
