---
concept_id: measurement_uncertainty
interest: cricket
format: misconception
title: Do errors cancel when you subtract two weighings
check:
  question: |-
    A ball weighs $161.0 \pm 0.5\,\text{g}$ after a night in the rain and $158.0 \pm 0.5\,\text{g}$ when dry. How much water did it absorb, with its error?
  options:
    A: |-
      $3.0 \pm 0\,\text{g}$
    B: |-
      $3.0 \pm 0.5\,\text{g}$
    C: |-
      $3.0 \pm 1.0\,\text{g}$
    D: |-
      $3.0\,\text{g} \pm 0.6\%$
  answer: C
  explanation: |-
    For a difference, the absolute errors add: $\Delta = 0.5 + 0.5 = 1.0\,\text{g}$. So the water absorbed is $3.0 \pm 1.0\,\text{g}$ — an error of about $33\%$.
  misconceptions:
    A: |-
      Believes the errors subtract and cancel because the same scale was used. Random errors can push the two readings in opposite directions, so for a difference they add.
    B: |-
      Thinks the result simply inherits the error of one reading. Both readings are uncertain, so both errors count.
    D: |-
      Adds the relative errors ($0.3\% + 0.3\%$), which is the rule for products and quotients. A difference needs absolute errors added.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A cricket ball sits on a digital scale while groundstaff measure the pitch](scenes/cricket/units_measurement.svg "The same scale, used twice. Does that make the difference exact?")

Somebody left the practice balls out by the sightscreen all night, and it rained. Gaurav, the club's equipment in-charge, is annoyed — wet balls get heavy and lose their shape. He wants to know how much water one has soaked up.

The club log says this ball weighed $158.0\,\text{g}$ when new. Gaurav puts it on the same digital scale, whose manual says it is accurate to $\pm 0.5\,\text{g}$. It now reads $161.0\,\text{g}$.

"Three grams of water," he writes, "plus or minus zero. Same scale both times, so its errors cancel out when I subtract."

His younger sister Pallavi, who has a physics test on errors next week, reads it over his shoulder. Something about "plus or minus zero" bothers her. Can subtracting two uncertain numbers really give a certain one?

## The common belief

"When you subtract two measurements made with the same instrument, the errors subtract too. They cancel, so the difference is more reliable than either reading."

## Why it feels right

Part of it is genuinely true. If the scale has a **systematic** error — say it always reads $0.3\,\text{g}$ too high — that offset is in both readings, and it does cancel in the difference. Physicists use this trick on purpose: measure twice with the same instrument and subtract.

It also feels natural that "minus" should apply to everything, errors included.

## What actually happens

The scale's $\pm 0.5\,\text{g}$ is not a fixed offset. It says each reading could be anywhere within $0.5\,\text{g}$ of the true value, and the two readings are independent. Look at the worst cases:

- wet ball really $161.5\,\text{g}$, dry ball really $157.5\,\text{g}$: difference $4.0\,\text{g}$;
- wet ball really $160.5\,\text{g}$, dry ball really $158.5\,\text{g}$: difference $2.0\,\text{g}$.

The true water content could be anywhere from $2.0$ to $4.0\,\text{g}$. So

$$\text{water} = 3.0 \pm 1.0\,\text{g}$$

The errors **added**. Each weighing was good to about $0.3\%$; the difference is uncertain by about $33\%$. Subtracting two nearly equal numbers keeps the absolute errors but shrinks the answer, so the relative error balloons.

## The physics

For a sum or a difference, the largest possible absolute error is the **sum** of the absolute errors:

$$Z = A \pm B \quad \Rightarrow \quad \Delta Z = \Delta A + \Delta B$$

The sign in front of $B$ doesn't matter, because $\Delta B$ describes a range on both sides of $B$, and the worst case always stretches the result. This is the rule the belief gets wrong.

![Three rules: for a sum or difference absolute errors add; for a product or quotient relative errors add; for a power the relative error is multiplied by the power](figures/measurement_uncertainty/combining-errors.svg "Top row: for A minus B, the absolute errors still add.")

For products and quotients, relative errors add; for a power $n$, the relative error is multiplied by $n$. Systematic errors are a separate story: they can cancel in a difference, but only if you know they are the same in both readings.

## Worked example

**Given:** wet mass $161.0 \pm 0.5\,\text{g}$; dry mass $158.0 \pm 0.5\,\text{g}$.
**Find:** the water absorbed, with its absolute and percentage error.

$$m_\text{water} = 161.0 - 158.0 = 3.0\,\text{g}$$

$$\Delta m_\text{water} = 0.5 + 0.5 = 1.0\,\text{g}$$

$$\text{percentage error} = \frac{1.0}{3.0} \times 100\% \approx 33\%$$

Compare: each single weighing had a percentage error of $0.5/160 \times 100\% \approx 0.3\%$.

**Sanity check:** the worst cases above gave $2.0$ and $4.0\,\text{g}$, exactly $3.0 \pm 1.0\,\text{g}$. To measure small changes well, you need a more precise scale, not the same scale twice.

## Key takeaway

For a difference, as for a sum, absolute errors **add**: $\Delta Z = \Delta A + \Delta B$. Subtracting two close measurements gives a small result with a large relative error. Only a known systematic offset cancels in a difference; random errors never do.
