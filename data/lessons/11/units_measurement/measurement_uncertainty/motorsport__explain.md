---
concept_id: measurement_uncertainty
interest: motorsport
format: explain
title: Five phones and one kart lap
check:
  question: |-
    A kart's mass (with driver) is known to within $1\%$, and a speed gun measures its speed to within $2\%$. What is the maximum percentage error in its kinetic energy, $\tfrac{1}{2}mv^2$?
  options:
    A: |-
      $3\%$
    B: |-
      $5\%$
    C: |-
      $4\%$
    D: |-
      $2.5\%$
  answer: B
  explanation: |-
    For a product, relative errors add, and a power multiplies the relative error by the power: $1\% + 2 \times 2\% = 5\%$. The $\tfrac{1}{2}$ is an exact number and adds no error.
  misconceptions:
    A: |-
      Adds the two percentages but forgets that $v$ is squared, so its $2\%$ must be doubled.
    C: |-
      Doubles the speed's error correctly but leaves out the mass's $1\%$, as if only the squared quantity mattered.
    D: |-
      Applies the $\tfrac{1}{2}$ in the formula to the error as well. The $\tfrac{1}{2}$ is exact; it scales the energy but not its relative error.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A race track with an electronic timing screen and a marshal timing a car by hand with a stopwatch](scenes/motorsport/units_measurement.svg "The screen times electronically. The marshal times with a thumb, and thumbs are never quite the same twice.")

The karting track near Harshita's college has no electronic timing on practice days, so her club times laps the old way. For her first proper run, five friends stand at the start-finish line with phone stopwatches, all timing the same lap.

She crosses the line, and five thumbs press *stop*.

The five readings: $41.2$, $41.5$, $41.3$, $41.0$ and $41.5$ seconds.

"Take mine, it's the quickest," says Rohan, whose phone says $41.0$. "Take the two that agree," says Simran — both $41.5$s. Harshita only wants one honest number to beat next week. None of the phones knows the true lap time. So what number should she write down — and how sure can she be of it?

## The physics

No measurement is perfect. The difference between a measured value and the true value is the **error**. **Random errors**, like five slightly different reaction times, scatter readings on both sides of the true value, so the best estimate is the **mean**:

$$\bar{a} = \frac{a_1 + a_2 + \cdots + a_n}{n}$$

The **absolute error** of each reading is $|\Delta a_i| = |a_i - \bar{a}|$, and the **mean absolute error** is their average:

$$\Delta\bar{a} = \frac{|\Delta a_1| + |\Delta a_2| + \cdots + |\Delta a_n|}{n}$$

The result is written $a = \bar{a} \pm \Delta\bar{a}$. To compare errors in measurements of different sizes, use the **relative error** $\Delta\bar{a}/\bar{a}$ or the **percentage error** $(\Delta\bar{a}/\bar{a}) \times 100\%$.

For Harshita's lap: the sum is $206.5\,\text{s}$, so the mean is $206.5/5 = 41.30\,\text{s}$. The absolute errors are $0.1, 0.2, 0.0, 0.3, 0.2\,\text{s}$, so

$$\Delta\bar{t} = \frac{0.1 + 0.2 + 0.0 + 0.3 + 0.2}{5} = \frac{0.8}{5} = 0.16\,\text{s}$$

![Five lap-time readings plotted as points around a dashed mean line at 41.30 seconds, with dotted lines 0.16 seconds above and below](figures/measurement_uncertainty/repeated-lap-times.svg "The readings scatter both ways around the mean. The dotted band, 41.30 ± 0.16 s, shows how big the typical scatter is.")

Rounding the error to one figure: $t = 41.3 \pm 0.2\,\text{s}$. Percentage error: $0.16/41.30 \times 100\% \approx 0.39\%$. Neither Rohan's nor Simran's choice is justified; the mean uses all five.

**Combining errors.** When a result is calculated from measurements, the largest possible error is found like this:

![Three rules: for a sum or difference absolute errors add; for a product or quotient relative errors add; for a power the relative error is multiplied by the power](figures/measurement_uncertainty/combining-errors.svg "Sums and differences: add absolute errors. Products and quotients: add relative errors. Powers: multiply the relative error by the power.")

- $Z = A \pm B$: $\Delta Z = \Delta A + \Delta B$
- $Z = AB$ or $A/B$: $\dfrac{\Delta Z}{Z} = \dfrac{\Delta A}{A} + \dfrac{\Delta B}{B}$
- $Z = A^n$: $\dfrac{\Delta Z}{Z} = n\,\dfrac{\Delta A}{A}$

## Worked example

**Given:** kart plus driver $m = 160 \pm 2\,\text{kg}$; speed at the end of the straight $v = 20.0 \pm 0.4\,\text{m/s}$ (illustrative).
**Find:** the kinetic energy $E = \tfrac{1}{2}mv^2$ with its error.

$$E = \tfrac{1}{2} \times 160 \times (20.0)^2 = 80 \times 400 = 32\,000\,\text{J}$$

A product containing a square, so the relative errors add, with the speed's counted twice:

$$\frac{\Delta E}{E} = \frac{\Delta m}{m} + 2\,\frac{\Delta v}{v} = \frac{2}{160} + 2 \times \frac{0.4}{20.0} = 0.0125 + 0.040 = 0.0525 \approx 5\%$$

$$\Delta E = 0.0525 \times 32\,000 \approx 1700\,\text{J}$$

So $E = (3.2 \pm 0.2) \times 10^4\,\text{J}$.

**Sanity check:** the speed contributes $4\%$ of the $5.25\%$. Squaring doubles its effect, so a better speed measurement would help far more than weighing the kart more carefully.

## Where the picture breaks

The mean absolute error handles only **random** errors. A **systematic** error shifts every reading the same way: if all five friends react late at the start but anticipate the finish, every lap time comes out short, and averaging can't fix it. The combination rules also give the *largest possible* error, as if every error pushed the same way at once; in practice random errors partly cancel.

## Key takeaway

For repeated readings, report the mean with the mean absolute error: $a = \bar{a} \pm \Delta\bar{a}$. Relative error $= \Delta a/a$; percentage error $= (\Delta a/a) \times 100\%$. When combining, absolute errors add for sums and differences, relative errors add for products and quotients, and a power $n$ multiplies the relative error by $n$.
