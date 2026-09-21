---
concept_id: measurement_uncertainty
interest: football
format: misconception
title: Can you add a metre of error to a second of error
check:
  question: |-
    A goal frame is measured as $7.32 \pm 0.01\,\text{m}$ wide and $2.44 \pm 0.01\,\text{m}$ high, so the goal mouth has an area of about $17.9\,\text{m}^2$. The absolute error in this area is closest to:
  options:
    A: |-
      $\pm 0.02\,\text{m}^2$
    B: |-
      $\pm 0.1\,\text{m}^2$
    C: |-
      $\pm 0.0001\,\text{m}^2$
    D: |-
      $\pm 0.55\,\text{m}^2$
  answer: B
  explanation: |-
    For a product, relative errors add: $0.01/7.32 + 0.01/2.44 = 0.0014 + 0.0041 = 0.0055$. So $\Delta A = 0.0055 \times 17.86\,\text{m}^2 \approx 0.1\,\text{m}^2$.
  misconceptions:
    A: |-
      Adds the absolute errors ($0.01 + 0.01$), the rule for sums. For a product, relative errors add; adding metres cannot give square metres.
    C: |-
      Multiplies the absolute errors ($0.01 \times 0.01$), as if the error of a product were the product of the errors.
    D: |-
      Finds the relative error as a percentage ($0.55\%$) and then writes the number as if it were the absolute error in square metres.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal with a tape while a match clock reads 45:00](scenes/football/units_measurement.svg "A tape for the distance, a clock for the time. How do their errors combine in a speed?")

Karan is trying to make the district team as a winger, and speed is everything. His friend Mahi times him with a stopwatch as he sprints the depth of the penalty area, from the goal line to its edge.

They measured the distance with the club's tape: $16.5\,\text{m}$, good to about $\pm 0.1\,\text{m}$. Mahi's stopwatch gives $2.2\,\text{s}$; after a few practice runs they agree her thumb is good to about $\pm 0.1\,\text{s}$.

Karan divides: $7.5\,\text{m/s}$. For the error, he adds the two: "$0.1$ plus $0.1$ is $0.2$. So $7.5 \pm 0.2\,\text{m/s}$."

Mahi squints at it. "You've just added a tenth of a metre to a tenth of a second. What does that even come out in?"

Karan opens his mouth to answer, and finds he doesn't know. Is his $\pm 0.2$ right, wrong, or meaningless?

## The common belief

"When you combine measurements, you add their absolute errors. That's the rule for errors, whatever the calculation."

## Why it feels right

Part of it is exactly right: for a **sum or a difference**, absolute errors really do add. It is usually the first error rule students meet, and it works perfectly for things like adding two lengths. It also feels like common sense — two uncertain numbers, so two uncertainties to pile up. And when both errors happen to be "$0.1$", adding them looks natural.

## What actually happens

Mahi's question is the decisive one. The distance error is $0.1\,\text{m}$ and the time error is $0.1\,\text{s}$. You can't add metres to seconds, just as you can't add goals to minutes. So Karan's "$0.2$" has no unit at all — it isn't an error in a speed.

What *can* be compared is how big each error is **relative** to its own measurement:

$$\frac{\Delta d}{d} = \frac{0.1}{16.5} = 0.006 \qquad \frac{\Delta t}{t} = \frac{0.1}{2.2} = 0.045$$

These are pure numbers, so they can be added. For a quotient, the relative errors add:

$$\frac{\Delta v}{v} = 0.006 + 0.045 = 0.051 \approx 5\%$$

$$\Delta v = 0.051 \times 7.5\,\text{m/s} \approx 0.4\,\text{m/s}$$

So $v = 7.5 \pm 0.4\,\text{m/s}$ — twice as uncertain as Karan claimed. Check it with the worst cases: the fastest possible speed is $16.6/2.1 = 7.90\,\text{m/s}$ and the slowest $16.4/2.3 = 7.13\,\text{m/s}$, about $0.4\,\text{m/s}$ either side of $7.5$.

Notice where the error comes from: the stopwatch's $4.5\%$ dwarfs the tape's $0.6\%$. A better tape would change almost nothing.

## The physics

The rules for the largest possible error in a calculated result depend on the operation:

![Three rules: for a sum or difference absolute errors add; for a product or quotient relative errors add; for a power the relative error is multiplied by the power](figures/measurement_uncertainty/combining-errors.svg "Only the top row adds absolute errors. Speed is a quotient, so it belongs in the middle row.")

- sum or difference: $\Delta Z = \Delta A + \Delta B$ (absolute errors, same units);
- product or quotient: $\dfrac{\Delta Z}{Z} = \dfrac{\Delta A}{A} + \dfrac{\Delta B}{B}$ (relative errors, dimensionless);
- power $Z = A^n$: $\dfrac{\Delta Z}{Z} = n\,\dfrac{\Delta A}{A}$.

The misconception uses the top rule everywhere. A quick test catches it: if the errors you want to add have different units, you're using the wrong rule.

## Worked example

**Given:** goal width $7.32 \pm 0.01\,\text{m}$; goal height $2.44 \pm 0.01\,\text{m}$.
**Find:** the area of the goal mouth with its error.

$$A = 7.32 \times 2.44 = 17.86\,\text{m}^2$$

$$\frac{\Delta A}{A} = \frac{0.01}{7.32} + \frac{0.01}{2.44} = 0.0014 + 0.0041 = 0.0055$$

$$\Delta A = 0.0055 \times 17.86 \approx 0.1\,\text{m}^2 \quad\Rightarrow\quad A = 17.9 \pm 0.1\,\text{m}^2$$

**Sanity check:** the largest possible area is $7.33 \times 2.45 = 17.96\,\text{m}^2$, about $0.1\,\text{m}^2$ more — matching the rule. Adding absolute errors would have given $0.02$, five times too small.

## Key takeaway

Absolute errors add only for sums and differences. For products and quotients, add **relative** errors: $v = d/t$ gives $\Delta v/v = \Delta d/d + \Delta t/t$. If the errors you're adding have different units, you've picked the wrong rule.
