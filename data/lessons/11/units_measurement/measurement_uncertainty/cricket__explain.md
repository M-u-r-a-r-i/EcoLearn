---
concept_id: measurement_uncertainty
interest: cricket
format: explain
title: Five stopwatches and one quick single
check:
  question: |-
    Before a match, an umpire measures a ball's circumference as $22.8\,\text{cm}$, with an absolute error of $0.2\,\text{cm}$. What is the percentage error in this measurement?
  options:
    A: |-
      $0.2\%$
    B: |-
      $0.009\%$
    C: |-
      $114\%$
    D: |-
      About $0.9\%$
  answer: D
  explanation: |-
    Relative error $= \Delta a/a = 0.2/22.8 \approx 0.0088$. Percentage error $= 0.0088 \times 100\% \approx 0.9\%$.
  misconceptions:
    A: |-
      Treats the absolute error ($0.2\,\text{cm}$) as if it were already a percentage. It has units; a percentage error needs dividing by the measured value.
    B: |-
      Finds the relative error ($0.0088$) but forgets to multiply by $100$ to make it a percentage.
    C: |-
      Divides the wrong way round, value over error, instead of error over value.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch; a stopwatch nearby reads 3.50 seconds](scenes/cricket/units_measurement.svg "The tape is careful. The stopwatch depends on a thumb.")

It's selection day for the under-17 team, and Coach Meenakshi wants to know who runs quickest between the wickets. She doesn't trust one stopwatch, so she gives phones to five players standing in a line at square leg, and asks all five to time the same single by Tushar.

He sprints, dives, grounds his bat. Five thumbs press *stop*.

Five different answers come back: $3.4$, $3.6$, $3.5$, $3.3$ and $3.7$ seconds.

"Mine's right," says Chirag. "I'm the fastest clicker." "No, mine," says Esha. Tushar just wants one number for his record. But which reading is the true one? And if none of them can claim that, what *can* you honestly write down?

## The physics

No measurement is perfect. The difference between a measured value and the true value is the **error**. Random errors — like five slightly different thumb reactions — scatter repeated readings on both sides of the true value, so the best estimate is the **mean**.

For readings $a_1, a_2, \ldots, a_n$:

$$\bar{a} = \frac{a_1 + a_2 + \cdots + a_n}{n}$$

The **absolute error** of each reading is its distance from the mean, $|\Delta a_i| = |a_i - \bar{a}|$. The **mean absolute error** is their average:

$$\Delta \bar{a} = \frac{|\Delta a_1| + |\Delta a_2| + \cdots + |\Delta a_n|}{n}$$

and the result is written $a = \bar{a} \pm \Delta\bar{a}$.

To compare errors in measurements of different sizes, use the **relative error** $\Delta\bar{a}/\bar{a}$, or the **percentage error** $(\Delta\bar{a}/\bar{a}) \times 100\%$.

For the five stopwatches: the mean is $17.5/5 = 3.50\,\text{s}$; the absolute errors are $0.1, 0.1, 0, 0.2, 0.2\,\text{s}$; so

$$\Delta\bar{t} = \frac{0.1 + 0.1 + 0 + 0.2 + 0.2}{5} = 0.12\,\text{s}$$

![Five readings plotted as points around a dashed mean line at 3.50 seconds, with dotted lines 0.12 seconds above and below](figures/measurement_uncertainty/repeated-readings.svg "The readings scatter on both sides of the mean. The dotted band, mean plus or minus 0.12 s, shows the typical size of the scatter.")

Written with the error rounded to one figure: $t = 3.5 \pm 0.1\,\text{s}$. Percentage error: $0.12/3.50 \times 100\% \approx 3.4\%$.

**Combining errors.** When a result is calculated from several measurements, their errors combine. For the largest possible error:

![Three rules: for a sum or difference absolute errors add; for a product or quotient relative errors add; for a power the relative error is multiplied by the power](figures/measurement_uncertainty/combining-errors.svg "Sums and differences: add absolute errors. Products and quotients: add relative errors. Powers: multiply the relative error by the power.")

- $Z = A \pm B$: $\Delta Z = \Delta A + \Delta B$
- $Z = AB$ or $A/B$: $\dfrac{\Delta Z}{Z} = \dfrac{\Delta A}{A} + \dfrac{\Delta B}{B}$
- $Z = A^n$: $\dfrac{\Delta Z}{Z} = n\,\dfrac{\Delta A}{A}$

## Worked example

**Given:** distance between popping creases $d = 17.68 \pm 0.01\,\text{m}$; time $t = 3.50 \pm 0.12\,\text{s}$ (from above).
**Find:** Tushar's average speed with its error.

$$v = \frac{d}{t} = \frac{17.68}{3.50} = 5.05\,\text{m/s}$$

A quotient, so relative errors add:

$$\frac{\Delta v}{v} = \frac{0.01}{17.68} + \frac{0.12}{3.50} = 0.0006 + 0.0343 = 0.0349 \approx 3.5\%$$

$$\Delta v = 0.0349 \times 5.05 \approx 0.18\,\text{m/s}$$

So $v = 5.1 \pm 0.2\,\text{m/s}$.

**Sanity check:** the time's error ($3.4\%$) is almost all of the total. The tape hardly matters; better timing would improve the result, and a better tape would not.

## Where the picture breaks

The mean absolute error only deals with **random** errors, which scatter both ways. A **systematic** error pushes every reading the same way — for example, if everyone reacts late to the start but not to the finish, all five times are too long, and averaging won't fix it. The combination rules also give the *largest possible* error, assuming every error works against you at once; in practice random errors partly cancel.

## Key takeaway

Take the mean of repeated readings as the best value and the mean absolute error as its uncertainty; relative error $= \Delta a/a$, percentage error $= (\Delta a/a) \times 100\%$. When combining, absolute errors add for sums and differences, relative errors add for products and quotients, and a power $n$ multiplies the relative error by $n$.
