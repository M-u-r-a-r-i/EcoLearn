---
concept_id: measurement_uncertainty
interest: football
format: challenge
title: Which measurement spoils the energy of a penalty
check:
  question: |-
    A ball's speed is measured with a percentage error of $3\%$, and its mass is known very precisely. Its kinetic energy is calculated from $E = \tfrac{1}{2}mv^2$. What is the percentage error in $E$?
  options:
    A: |-
      $6\%$
    B: |-
      $3\%$
    C: |-
      $9\%$
    D: |-
      $1.5\%$
  answer: A
  explanation: |-
    For a power, the relative error is multiplied by the power: $v^2$ carries $2 \times 3\% = 6\%$. The $\tfrac{1}{2}$ is exact and the mass adds almost nothing, so $\Delta E/E \approx 6\%$.
  misconceptions:
    B: |-
      Thinks an error passes through a formula unchanged. Squaring the speed doubles its relative error.
    C: |-
      Squares the percentage error ($3^2 = 9$) instead of multiplying it by the power.
    D: |-
      Divides by the power, as if taking a square root. That would be the rule for finding $v$ from $E$, not $E$ from $v$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A match ball sits on a digital scale beside a pressure gauge; a groundsman measures a goal nearby](scenes/football/units_measurement.svg "A scale for the mass, a camera for the speed. Which one needs upgrading?")

For the school science fair, Zara and Siddhant want to answer one question: how much energy does a hard penalty put into the ball?

Their kit is basic. The kitchen scale reads to the nearest $10\,\text{g}$: the ball is $430 \pm 10\,\text{g}$. For the speed, they film Siddhant's penalty in slow motion against the goal frame and count frames: about $25\,\text{m/s}$, give or take $1\,\text{m/s}$.

Siddhant has a plan. "The mass is the weak point. Ten grams! I'll borrow the chemistry lab's balance — it reads to a milligram."

Zara shakes her head. "The speed is squared in the formula. I think the camera is what's hurting us."

"One metre per second is tiny," Siddhant says. "Ten grams is a lot."

They can only fix one thing before the fair. Which measurement is really spoiling their answer?

## The challenge

Measured values (illustrative): $m = 0.43 \pm 0.01\,\text{kg}$ and $v = 25 \pm 1\,\text{m/s}$. The kinetic energy is

$$E = \tfrac{1}{2}mv^2$$

Find $E$ and its percentage error. Which measurement contributes more to the error — the mass or the speed?

## Think first

The mass error is ten whole grams; the speed error is only one metre per second. Is the mass the bigger problem? Or do you just add the two percentage errors and stop? Does the square on $v$ change anything? Decide which upgrade you'd pick.

## The reveal

Work in **relative errors**, because $E$ is built from a product and a power. Comparing $10\,\text{g}$ directly with $1\,\text{m/s}$ can't work — they have different units. Only relative errors can be compared.

**Mass:**
$$\frac{\Delta m}{m} = \frac{0.01}{0.43} = 0.023 = 2.3\%$$

**Speed:**
$$\frac{\Delta v}{v} = \frac{1}{25} = 0.04 = 4\%$$

**Speed squared.** For a power, the relative error is multiplied by the power:
$$\frac{\Delta (v^2)}{v^2} = 2 \times 4\% = 8\%$$

**Energy**, a product ($\tfrac{1}{2}$ is exact and adds nothing), so relative errors add:
$$\frac{\Delta E}{E} = 2.3\% + 8\% \approx 10\%$$

Zara is right. The speed contributes $8\%$ of the roughly $10\%$; the mass only $2.3\%$. Even a perfect balance would leave an $8\%$ error. Halving the speed error to $0.5\,\text{m/s}$ instead would bring the total down to $2.3\% + 4\% \approx 6\%$.

The numbers:

$$E = \tfrac{1}{2} \times 0.43 \times 25^2 = 0.215 \times 625 \approx 134\,\text{J}$$

$$\Delta E \approx 0.103 \times 134 \approx 14\,\text{J}$$

Rounding the error to one figure: $E = (1.3 \pm 0.1) \times 10^2\,\text{J}$.

If you guessed "add $2.3\%$ and $4\%$ to get about $6\%$", you missed the square: the speed enters the energy twice over.

## The physics

For a measured value $a$ with absolute error $\Delta a$, the relative error is $\Delta a/a$ and the percentage error is $(\Delta a/a) \times 100\%$. For the largest possible error in a calculated result:

![Three rules: for a sum or difference absolute errors add; for a product or quotient relative errors add; for a power the relative error is multiplied by the power](figures/measurement_uncertainty/combining-errors.svg "The kinetic energy used the bottom two rules: a product, and a square.")

- sum or difference, $Z = A \pm B$: $\Delta Z = \Delta A + \Delta B$;
- product or quotient, $Z = AB$ or $A/B$: $\Delta Z/Z = \Delta A/A + \Delta B/B$;
- power, $Z = A^n$: $\Delta Z/Z = n\,\Delta A/A$.

In general, for $Z = A^p B^q / C^r$: $\dfrac{\Delta Z}{Z} = p\dfrac{\Delta A}{A} + q\dfrac{\Delta B}{B} + r\dfrac{\Delta C}{C}$. Exact numbers like $\tfrac{1}{2}$ contribute no error. The quantity raised to the highest power usually deserves the most careful measurement.

## Key takeaway

A power multiplies the relative error: square a measurement and you double its percentage error. In $E = \tfrac{1}{2}mv^2$, a $4\%$ speed error becomes $8\%$, swamping a $2.3\%$ mass error. Improve the measurement that carries the biggest power.
