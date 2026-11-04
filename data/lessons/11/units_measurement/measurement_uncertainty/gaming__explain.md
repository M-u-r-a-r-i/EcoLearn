---
concept_id: measurement_uncertainty
interest: gaming
format: explain
title: Five tries at a reaction test and no single answer
check:
  question: |-
    Aryan measures the width of his monitor's screen as $60.0\,\text{cm}$, with an absolute error of $0.3\,\text{cm}$. What is the percentage error in this measurement?
  options:
    A: |-
      $0.3\%$
    B: |-
      $0.5\%$
    C: |-
      $0.005\%$
    D: |-
      $200\%$
  answer: B
  explanation: |-
    Relative error $= \Delta a/a = 0.3/60.0 = 0.005$. Percentage error $= 0.005 \times 100\% = 0.5\%$.
  misconceptions:
    A: |-
      Treats the absolute error ($0.3\,\text{cm}$) as if it were already a percentage. It has units; you must divide it by the measured value first.
    C: |-
      Finds the relative error, $0.005$, but forgets to multiply by $100$ to turn it into a percentage.
    D: |-
      Divides the wrong way round, value over error ($60.0/0.3 = 200$), instead of error over value.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk: a monitor, a mouse on a ruler, a controller on a scale, and a phone showing a reaction test reading 0.25 s](scenes/gaming/units_measurement.svg "The phone's reaction test gives a crisp number every time. But is it the same number every time?")

Farhan is sure he has the fastest reflexes in the house. His sister Ananya is sure he doesn't. They settle it the way gamers do: a reaction-time test on the phone. The screen turns green, you tap as fast as you can, and it shows your time.

Farhan's first try: $0.24\,\text{s}$. "Beat that."

Ananya makes him go again. $0.27$. Then $0.25$, $0.22$, $0.27$.

"So which one is your reaction time?" she asks. "The $0.22$ you'll brag about, or the $0.27$ I'll tell everyone?"

Farhan frowns at the list. Same thumb, same phone, same test, five different answers. If no single try is *the* answer, what number can he honestly put on the family leaderboard — and how sure can he be about it?

## The physics

No measurement is perfect. The difference between a measured value and the true value is its **error**. **Random errors** — like tiny changes in attention from one tap to the next — scatter repeated readings on both sides of the true value, so the best estimate is their **mean**:

$$\bar{a} = \frac{a_1 + a_2 + \cdots + a_n}{n}$$

The **absolute error** of each reading is $|\Delta a_i| = |a_i - \bar{a}|$, and the **mean absolute error** is their average:

$$\Delta\bar{a} = \frac{|\Delta a_1| + |\Delta a_2| + \cdots + |\Delta a_n|}{n}$$

The result is written $a = \bar{a} \pm \Delta\bar{a}$. To compare measurements of different sizes, use the **relative error** $\Delta\bar{a}/\bar{a}$ or the **percentage error** $(\Delta\bar{a}/\bar{a}) \times 100\%$.

For Farhan: the sum is $1.25\,\text{s}$, so $\bar{t} = 1.25/5 = 0.250\,\text{s}$. The absolute errors are $0.01$, $0.02$, $0$, $0.03$ and $0.02\,\text{s}$, so

$$\Delta\bar{t} = \frac{0.01 + 0.02 + 0 + 0.03 + 0.02}{5} = \frac{0.08}{5} = 0.016\,\text{s}$$

![Five reaction times plotted as points around a dashed mean line at 0.250 seconds, with dotted lines 0.016 seconds above and below](figures/measurement_uncertainty/reaction-time-readings.svg "The tries scatter on both sides of the mean. The dotted band, mean plus or minus 0.016 s, shows the typical size of the scatter.")

With the error rounded to one figure: $t = 0.25 \pm 0.02\,\text{s}$. Percentage error: $0.016/0.250 \times 100\% = 6.4\%$.

**Combining errors.** When a result is calculated from measured values, their errors combine. For the largest possible error:

![Three rules: for a sum or difference absolute errors add; for a product or quotient relative errors add; for a power the relative error is multiplied by the power](figures/measurement_uncertainty/combining-errors.svg "Sums and differences: add absolute errors. Products and quotients: add relative errors. Powers: multiply the relative error by the power.")

- $Z = A \pm B$: $\Delta Z = \Delta A + \Delta B$
- $Z = AB$ or $A/B$: $\dfrac{\Delta Z}{Z} = \dfrac{\Delta A}{A} + \dfrac{\Delta B}{B}$
- $Z = A^n$: $\dfrac{\Delta Z}{Z} = n\,\dfrac{\Delta A}{A}$

## Worked example

**Given** (illustrative): (a) the round top of a controller's thumbstick has diameter $d = 1.60 \pm 0.01\,\text{cm}$, measured with vernier calipers; (b) two charging cables are $1.80 \pm 0.02\,\text{m}$ and $1.50 \pm 0.02\,\text{m}$ long.
**Find:** (a) the area of the thumbstick top, $A = \pi d^2/4$, with its error; (b) the total length of the cables joined end to end.

(a) $\pi$ and $4$ are exact, so only $d$ carries error, raised to the power $2$:

$$\frac{\Delta A}{A} = 2 \times \frac{0.01}{1.60} = 0.0125 = 1.25\%$$

$$A = \frac{\pi \times (1.60)^2}{4} = \frac{\pi \times 2.56}{4} = 2.011\,\text{cm}^2, \qquad \Delta A = 0.0125 \times 2.011 = 0.025\,\text{cm}^2$$

So $A = 2.01 \pm 0.03\,\text{cm}^2$.

(b) A sum, so absolute errors add:

$$L = 1.80 + 1.50 = 3.30\,\text{m}, \qquad \Delta L = 0.02 + 0.02 = 0.04\,\text{m}$$

So $L = 3.30 \pm 0.04\,\text{m}$.

**Sanity check:** in (a) the diameter's error is $0.6\%$, and squaring doubles it to about $1.3\%$ — powers magnify relative errors, which is why the most-squared quantity deserves the most careful measuring.

## Where the picture breaks

The mean absolute error handles only **random** errors. A reaction test also has a **systematic** error: the phone's screen takes time to show the green, and the touchscreen takes time to register the tap. That delay adds to *every* try in the same direction, so averaging can never remove it; Farhan's true reaction time is somewhat less than $0.25\,\text{s}$, by an amount this test can't reveal. And the combination rules give the *largest possible* error, assuming every error works against you at once.

## Key takeaway

Take the mean of repeated readings as the best value and the mean absolute error as its uncertainty. Relative error $= \Delta a/a$; percentage error $= (\Delta a/a) \times 100\%$. Combining: absolute errors add for sums and differences, relative errors add for products and quotients, and a power $n$ multiplies the relative error by $n$.
