---
concept_id: measurement_uncertainty
interest: cricket
format: challenge
title: Which measurement spoils the density of a cricket ball
check:
  question: |-
    The radius of a ball is measured with a percentage error of $2\%$. Its volume is calculated from $V = \tfrac{4}{3}\pi r^3$. What is the percentage error in the volume?
  options:
    A: |-
      $2\%$
    B: |-
      $6\%$
    C: |-
      $8\%$
    D: |-
      $0.67\%$
  answer: B
  explanation: |-
    For a power, the relative error is multiplied by the power: $\Delta V/V = 3 \times \Delta r/r = 3 \times 2\% = 6\%$. The $\tfrac{4}{3}$ and $\pi$ are exact, so they add no error.
  misconceptions:
    A: |-
      Thinks the error passes through a formula unchanged. Cubing the radius triples its relative error.
    C: |-
      Cubes the percentage error ($2^3 = 8$) instead of multiplying it by the power.
    D: |-
      Divides by the power, as if taking a cube root. That would be the rule for finding $r$ from $V$, not $V$ from $r$.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A ball sits on a digital scale beside groundstaff measuring the pitch](scenes/cricket/units_measurement.svg "A scale for the mass, a tape for the size. Which one deserves the upgrade?")

For the school science exhibition, Ishita and Varun are finding the density of a cricket ball. Their kit is basic: a kitchen scale that reads to the nearest gram, and a tailor's tape wrapped around the ball's seam.

Mass: $160\,\text{g}$, give or take $1\,\text{g}$. Circumference: $22.8\,\text{cm}$, give or take $0.2\,\text{cm}$.

Varun has a plan. "Density is mass divided by volume, so the mass matters most. I'll borrow the chemistry lab's balance — it reads to a milligram."

Ishita isn't convinced. "The volume comes from the circumference, and it's *cubed*. I think it's the tape we need to improve." Varun laughs: "A tape is a tape."

They can only get one upgrade before the exhibition. Which measurement is really spoiling their answer?

## The challenge

Measured values: $m = 160 \pm 1\,\text{g}$ and circumference $C = 22.8 \pm 0.2\,\text{cm}$. The ball is treated as a sphere, so its volume is

$$V = \frac{4}{3}\pi r^3 \quad \text{with} \quad r = \frac{C}{2\pi}, \quad \text{which gives} \quad V = \frac{C^3}{6\pi^2}$$

and its density is $\rho = m/V$. Find the percentage error in $\rho$. Which measurement contributes more to it — the mass or the circumference?

## Think first

The mass error is $1\,\text{g}$ and the circumference error is only $0.2\,\text{cm}$ — so is the mass the bigger problem? Or do you add the two percentage errors and stop there? Does the cube in the volume formula change anything? Make a guess, and note which of the two you'd upgrade.

## The reveal

Work in **relative errors**, because $\rho$ is built from products, quotients and a power.

**Mass:**
$$\frac{\Delta m}{m} = \frac{1}{160} = 0.0063 = 0.63\%$$

**Circumference:**
$$\frac{\Delta C}{C} = \frac{0.2}{22.8} = 0.0088 = 0.88\%$$

**Volume**, which depends on $C^3$. For a power, the relative error is multiplied by the power ($6\pi^2$ is exact and adds no error):
$$\frac{\Delta V}{V} = 3 \times 0.88\% = 2.6\%$$

**Density**, a quotient, so relative errors add:
$$\frac{\Delta\rho}{\rho} = \frac{\Delta m}{m} + \frac{\Delta V}{V} = 0.63\% + 2.6\% \approx 3.3\%$$

Ishita is right. The circumference contributes $2.6\%$ of the $3.3\%$; the mass only $0.63\%$. Even a perfect balance would leave a $2.6\%$ error. Halving the tape's error to $0.1\,\text{cm}$ would bring the total down to about $0.63\% + 1.3\% \approx 1.9\%$.

For the numbers: $V = 22.8^3/(6\pi^2) \approx 200\,\text{cm}^3$, so $\rho = 160/200 \approx 0.80\,\text{g/cm}^3$, and $\Delta\rho \approx 0.033 \times 0.80 \approx 0.03\,\text{g/cm}^3$. Result: $\rho = 0.80 \pm 0.03\,\text{g/cm}^3$.

If you guessed "add $0.63\%$ and $0.88\%$ to get $1.5\%$", you missed the cube: the circumference enters the volume three times over. And comparing $1\,\text{g}$ with $0.2\,\text{cm}$ directly can't work — they have different units. Only relative errors can be compared.

## The physics

For a quantity with measured value $a$ and absolute error $\Delta a$, the relative error is $\Delta a/a$ and the percentage error is $(\Delta a/a) \times 100\%$. For the largest possible error in a calculated result:

![Three rules: for a sum or difference absolute errors add; for a product or quotient relative errors add; for a power the relative error is multiplied by the power](figures/measurement_uncertainty/combining-errors.svg "The density used the bottom two rules: a quotient, and a cube.")

- sum or difference, $Z = A \pm B$: $\Delta Z = \Delta A + \Delta B$;
- product or quotient, $Z = AB$ or $A/B$: $\Delta Z/Z = \Delta A/A + \Delta B/B$;
- power, $Z = A^n$: $\Delta Z/Z = n\,\Delta A/A$.

In general, for $Z = A^p B^q / C^r$: $\dfrac{\Delta Z}{Z} = p\dfrac{\Delta A}{A} + q\dfrac{\Delta B}{B} + r\dfrac{\Delta C}{C}$. The quantity with the highest power deserves the most careful measurement.

## Key takeaway

A power multiplies the relative error: cube a measurement and you triple its percentage error. So in $\rho = m/V$ with $V \propto C^3$, the circumference, not the mass, dominates the error. Improve the measurement that carries the biggest power.
