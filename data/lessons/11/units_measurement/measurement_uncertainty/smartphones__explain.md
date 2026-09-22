---
concept_id: measurement_uncertainty
interest: smartphones
format: explain
title: Five caliper readings for one phone case
check:
  question: |-
    The round window over a phone's camera has a radius measured as $4.0\,\text{mm}$, with a percentage error of $3\%$. What is the percentage error in its area, $A = \pi r^2$?
  options:
    A: |-
      $3\%$
    B: |-
      $6\%$
    C: |-
      $9\%$
    D: |-
      $1.5\%$
  answer: B
  explanation: |-
    For a power, $\dfrac{\Delta A}{A} = n\,\dfrac{\Delta r}{r}$. Here $n = 2$, so the percentage error in the area is $2 \times 3\% = 6\%$. The $\pi$ is an exact number and adds no error.
  misconceptions:
    A: |-
      Thinks the area inherits the radius's error unchanged. Squaring the radius uses its error twice, so the relative error doubles.
    C: |-
      Squares the percentage error ($3^2 = 9$) instead of multiplying it by the power. The rule is $n$ times the relative error, not the relative error to the power $n$.
    D: |-
      Divides by the power instead of multiplying, as if the area were the square root of the radius. That rule would apply to $\sqrt{r}$, not $r^2$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A study desk: a phone held in a digital caliper reading 7.92 mm, a phone on a scale, a charger with a USB meter](scenes/smartphones/units_measurement.svg "The caliper shows a crisp 7.92 mm. Close it again and it may not.")

Ritika is designing her own phone case, and the print shop near her college needs one number from her by evening: the phone's thickness. Too tight and the phone won't go in; too loose and it rattles.

She borrows a digital caliper from the physics lab and measures. $7.92\,\text{mm}$. To be safe she opens the jaws, closes them again, and measures once more: $7.88$. Then $7.96$, $7.90$ and $7.94$.

"Just send the first one," says her roommate Swati. "The caliper shows two decimal places. It's obviously accurate."

But the caliper showed two decimal places *every* time, and gave five different answers. Ritika stares at the list. Which of the five is the phone's true thickness? And if she can't say, what number can she honestly send — and how sure should the shop be about it?

## The physics

No measurement is perfect. The difference between a measured value and the true value is the **error**. **Random errors** — a slightly different squeeze of the jaws, a slightly different spot on the phone's edge — scatter repeated readings on both sides of the true value. So the best estimate is the **mean**:

$$\bar{a} = \frac{a_1 + a_2 + \cdots + a_n}{n}$$

The **absolute error** of each reading is its distance from the mean, $|\Delta a_i| = |a_i - \bar{a}|$. The **mean absolute error** is their average:

$$\Delta\bar{a} = \frac{|\Delta a_1| + |\Delta a_2| + \cdots + |\Delta a_n|}{n}$$

and the result is written $a = \bar{a} \pm \Delta\bar{a}$. To compare errors in quantities of different sizes, use the **relative error** $\Delta\bar{a}/\bar{a}$, or the **percentage error** $(\Delta\bar{a}/\bar{a}) \times 100\%$.

For Ritika: the five readings add to $39.60\,\text{mm}$, so $\bar{d} = 39.60/5 = 7.920\,\text{mm}$. The absolute errors are $0.00$, $0.04$, $0.04$, $0.02$ and $0.02\,\text{mm}$, so

$$\Delta\bar{d} = \frac{0.00 + 0.04 + 0.04 + 0.02 + 0.02}{5} = \frac{0.12}{5} = 0.024\,\text{mm}$$

![Five caliper readings plotted as points around a dashed mean line at 7.920 millimetres, with dotted lines 0.024 millimetres above and below](figures/measurement_uncertainty/repeated-thickness.svg "The readings scatter on both sides of the mean. The dotted band, mean plus or minus 0.024 mm, shows the typical size of the scatter.")

She sends $d = 7.92 \pm 0.02\,\text{mm}$, a percentage error of $0.024/7.920 \times 100\% \approx 0.3\%$.

**Combining errors.** When a result is calculated from measured quantities, their errors combine. For the largest possible error:

![Three rules: for a sum or difference absolute errors add; for a product or quotient relative errors add; for a power the relative error is multiplied by the power](figures/measurement_uncertainty/combining-errors.svg "Sums and differences: add absolute errors. Products and quotients: add relative errors. Powers: multiply the relative error by the power.")

- $Z = A \pm B$: $\Delta Z = \Delta A + \Delta B$
- $Z = AB$ or $A/B$: $\dfrac{\Delta Z}{Z} = \dfrac{\Delta A}{A} + \dfrac{\Delta B}{B}$
- $Z = A^n$: $\dfrac{\Delta Z}{Z} = n\,\dfrac{\Delta A}{A}$

So if the case's back wall is $1.50 \pm 0.05\,\text{mm}$, the phone-plus-case thickness is $9.42 \pm 0.07\,\text{mm}$: in a sum, absolute errors add.

## Worked example

**Given:** a USB power meter between a charger and a phone reads $V = 5.00 \pm 0.05\,\text{V}$ and $I = 1.80 \pm 0.05\,\text{A}$ (illustrative).
**Find:** the power delivered, $P = VI$, with its error.

$$P = VI = 5.00\,\text{V} \times 1.80\,\text{A} = 9.00\,\text{W}$$

A product, so relative errors add:

$$\frac{\Delta P}{P} = \frac{0.05}{5.00} + \frac{0.05}{1.80} = 0.0100 + 0.0278 = 0.0378 \approx 3.8\%$$

$$\Delta P = 0.0378 \times 9.00\,\text{W} \approx 0.34\,\text{W}$$

So $P = 9.0 \pm 0.3\,\text{W}$.

**Sanity check:** the current's relative error ($2.8\%$) is almost three times the voltage's ($1.0\%$), so a better ammeter would improve the result far more than a better voltmeter. Worst case: $5.05 \times 1.85 = 9.34\,\text{W}$, about $0.34\,\text{W}$ above $9.00$ — matching $\Delta P$.

## Where the picture breaks

The mean absolute error handles only **random** errors. A **systematic** error shifts every reading the same way: if the caliper wasn't zeroed and reads $0.03\,\text{mm}$ high even when closed, all five readings are too big, and averaging won't reveal it. The combination rules give the *largest possible* error, assuming every error works against you at once; in practice random errors partly cancel. And the phone itself isn't perfectly uniform — its edges are curved — so part of the scatter is the object, not the instrument.

## Key takeaway

Take the mean of repeated readings as the best value and the mean absolute error as its uncertainty; relative error $= \Delta a/a$ and percentage error $= (\Delta a/a) \times 100\%$. When combining, absolute errors add for sums and differences, relative errors add for products and quotients, and a power $n$ multiplies the relative error by $n$.
