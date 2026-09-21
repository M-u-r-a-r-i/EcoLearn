---
concept_id: measurement_uncertainty
interest: football
format: explain
title: Five tapes around one match ball
check:
  question: |-
    Before kick-off, an official weighs a match ball as $430\,\text{g}$ on a scale with an absolute error of $5\,\text{g}$. What is the percentage error in this measurement?
  options:
    A: |-
      $5\%$
    B: |-
      $0.012\%$
    C: |-
      $86\%$
    D: |-
      About $1.2\%$
  answer: D
  explanation: |-
    Relative error $= \Delta m/m = 5/430 \approx 0.0116$. Percentage error $= 0.0116 \times 100\% \approx 1.2\%$.
  misconceptions:
    A: |-
      Treats the absolute error ($5\,\text{g}$) as if it were already a percentage. It has a unit; to get a percentage you must divide by the measured value.
    B: |-
      Finds the relative error ($0.0116$) but forgets to multiply by $100$, then writes a percentage sign anyway.
    C: |-
      Divides the wrong way round — value over error ($430/5 = 86$) instead of error over value.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A match ball sits on a scale beside a pressure gauge while a groundsman measures a goal](scenes/football/units_measurement.svg "Every instrument at the ground gives a reading. None of them gives the true value exactly.")

It's the morning of the district under-17 tournament, and Jyoti is the referee's assistant for ball checks. The Laws say a ball's circumference must be $68$ to $70\,\text{cm}$. She has one tailor's tape, and five volunteers.

To be fair, each volunteer wraps the tape around the same ball and reads it: $68.8$, $69.2$, $69.0$, $68.9$ and $69.1\,\text{cm}$.

"Mine's right," says Harish. "I pulled the tape tight." "Mine," says Noor, "I read it at eye level." Five careful people, five different answers, and not one of them is exactly the same as another.

Jyoti has to write one number on the match sheet. Which reading is the true one? And if none of them can claim that, what *can* she honestly write down?

## The physics

No measurement is perfect. The difference between a measured value and the true value is the **error**. **Random errors** — a tape pulled a little tighter, read from a slightly different angle — scatter repeated readings on both sides of the true value, so the best estimate is their **mean**:

$$\bar{a} = \frac{a_1 + a_2 + \cdots + a_n}{n}$$

The **absolute error** of each reading is its distance from the mean, $|\Delta a_i| = |a_i - \bar{a}|$. The **mean absolute error** is their average:

$$\Delta\bar{a} = \frac{|\Delta a_1| + |\Delta a_2| + \cdots + |\Delta a_n|}{n}$$

and the result is written $a = \bar{a} \pm \Delta\bar{a}$. To compare errors in measurements of different sizes, use the **relative error** $\Delta\bar{a}/\bar{a}$, or the **percentage error** $(\Delta\bar{a}/\bar{a}) \times 100\%$.

For Jyoti's ball: the mean is $345.0/5 = 69.0\,\text{cm}$. The absolute errors are $0.2$, $0.2$, $0$, $0.1$ and $0.1\,\text{cm}$, so

$$\Delta\bar{C} = \frac{0.2 + 0.2 + 0 + 0.1 + 0.1}{5} = 0.12\,\text{cm}$$

![Five circumference readings plotted as points around a dashed mean line at 69.0 cm, with dotted lines 0.12 cm above and below](figures/measurement_uncertainty/repeated-circumference.svg "The readings scatter on both sides of the mean. The dotted band, mean plus or minus 0.12 cm, shows the typical size of the scatter.")

With the error rounded to one figure: $C = 69.0 \pm 0.1\,\text{cm}$ — comfortably legal. Percentage error: $0.12/69.0 \times 100\% \approx 0.17\%$.

**Combining errors.** When a result is calculated from several measurements, their errors combine. For the largest possible error:

![Three rules: for a sum or difference absolute errors add; for a product or quotient relative errors add; for a power the relative error is multiplied by the power](figures/measurement_uncertainty/combining-errors.svg "Sums and differences: add absolute errors. Products and quotients: add relative errors. Powers: multiply the relative error by the power.")

- $Z = A \pm B$: $\Delta Z = \Delta A + \Delta B$
- $Z = AB$ or $A/B$: $\dfrac{\Delta Z}{Z} = \dfrac{\Delta A}{A} + \dfrac{\Delta B}{B}$
- $Z = A^n$: $\dfrac{\Delta Z}{Z} = n\,\dfrac{\Delta A}{A}$

## Worked example

**Given:** a pitch measured as $L = 105.0 \pm 0.1\,\text{m}$ long and $W = 68.0 \pm 0.1\,\text{m}$ wide (illustrative).
**Find:** (a) its perimeter with error; (b) its area with error.

(a) Perimeter $P = 2(L + W) = 2 \times 173.0 = 346.0\,\text{m}$. A sum, so absolute errors add; the $2$ is exact and doubles them:

$$\Delta P = 2(0.1 + 0.1) = 0.4\,\text{m} \quad\Rightarrow\quad P = 346.0 \pm 0.4\,\text{m}$$

(b) Area $A = LW = 105.0 \times 68.0 = 7140\,\text{m}^2$. A product, so relative errors add:

$$\frac{\Delta A}{A} = \frac{0.1}{105.0} + \frac{0.1}{68.0} = 0.00095 + 0.00147 = 0.00242 \approx 0.24\%$$

$$\Delta A = 0.00242 \times 7140 \approx 17\,\text{m}^2 \quad\Rightarrow\quad A = 7140 \pm 17\,\text{m}^2$$

**Sanity check:** the worst case is a pitch $105.1 \times 68.1 = 7157.3\,\text{m}^2$, about $17\,\text{m}^2$ above $7140$. The rule agrees with direct calculation.

## Where the picture breaks

The mean absolute error only handles **random** errors, which scatter both ways. A **systematic** error pushes every reading the same way: if the tailor's tape has stretched with use, all five readings are too small, and averaging won't reveal it. The combination rules also give the *largest possible* error, as if every error worked against you at once; in practice random errors partly cancel.

## Key takeaway

Take the mean of repeated readings as the best value and the mean absolute error as its uncertainty. Relative error $= \Delta a/a$; percentage error $= (\Delta a/a) \times 100\%$. Combining: absolute errors add for sums and differences, relative errors add for products and quotients, and a power $n$ multiplies the relative error by $n$.
