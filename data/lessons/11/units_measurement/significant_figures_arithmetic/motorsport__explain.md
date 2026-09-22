---
concept_id: significant_figures_arithmetic
interest: motorsport
format: explain
title: Adding up a pit stop with three different clocks
check:
  question: |-
    A car's trip through the pit lane is timed in three parts: pit entry $31.506\,\text{s}$ (timing loops), stationary $2.9\,\text{s}$ (hand stopwatch) and pit exit $27.33\,\text{s}$ (video). The total, reported correctly, is:
  options:
    A: |-
      $61.736\,\text{s}$
    B: |-
      $62\,\text{s}$
    C: |-
      $61.74\,\text{s}$
    D: |-
      $61.7\,\text{s}$
  answer: D
  explanation: |-
    $31.506 + 2.9 + 27.33 = 61.736$. In a sum, keep as many decimal places as the value with the fewest: $2.9\,\text{s}$ has one, so the total is $61.7\,\text{s}$.
  misconceptions:
    A: |-
      Copies the calculator and keeps three decimal places from the most precise timing. The hand-timed $2.9\,\text{s}$ has an unknown hundredths digit, which spoils the hundredths of the total.
    B: |-
      Uses the multiplication rule (fewest significant figures, two from $2.9$) in an addition. For sums, what matters is decimal places, not significant figures.
    C: |-
      Keeps two decimal places, from $27.33$, ignoring that the stationary time was only measured to one decimal place.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A race track with an electronic timing screen showing thousandths of a second and a marshal timing by hand with a stopwatch](scenes/motorsport/units_measurement.svg "An electronic screen and a thumb on a stopwatch. When you combine their readings, which one sets the precision?")

Neha is a data intern with a club racing team, and the team manager wants to know how long their car lost in the pit lane. There are three pieces. The timing loops give the pit-entry section: $28.412\,\text{s}$. Arjun, the mechanic, hand-timed the car standing still for its tyre change: $3.7\,\text{s}$. And a video frame count gives the pit-exit section: $30.25\,\text{s}$.

Neha adds them on her laptop: $62.362\,\text{s}$.

"Report all three decimals," says the manager. "Our timing is to the thousandth."

"No," says Arjun, "my $3.7$ has only two significant figures. So it should just be $62\,\text{s}$."

Both sound reasonable, and they can't both be right. How many digits does the total actually deserve?

## The physics

A result calculated from measurements can't be more precise than the data. NCERT gives two different rules.

**Adding or subtracting:** keep as many **decimal places** as the value with the fewest decimal places.

**Multiplying or dividing:** keep as many **significant figures** as the value with the fewest significant figures.

![Left: 20.12 plus 1.5 gives 21.62, rounded to 21.6 because 1.5 has one decimal place. Right: 20.12 times 3.05 gives 61.366, rounded to 61.4 because 3.05 has three significant figures](figures/significant_figures_arithmetic/add-vs-multiply-rules.svg "Adding: the unknown hundredths of 1.5 spoil the hundredths of the sum. Multiplying: the answer keeps the significant figures of the least precise factor.")

Why different? In a sum, the errors are absolute — Arjun's $3.7\,\text{s}$ could be off by several hundredths, so the sum's hundredths digit is unknown however precise the other parts are. What matters is the **position** of the last reliable digit. In a product or quotient, what matters is **relative** precision, which is what significant figures track.

So the manager is wrong (the hand timing spoils the hundredths and thousandths) and Arjun is wrong too (he used the product rule for a sum).

**Rounding off (NCERT):** look at the first digit you drop. More than $5$: raise the preceding digit ($62.362 \to 62.4$, because the first dropped digit is $6$). Less than $5$: leave it ($30.25 \to 30$ to two figures, because the first dropped digit is $2$). Exactly $5$ with nothing after: leave an even preceding digit, raise an odd one. **Exact numbers** (counted laps, the $2$ in $2\pi r$) never limit a result, and in multi-step work you round only at the end.

## Worked example

**Given:** the three pit-lane times above; and, separately, a kart covering a straight of $d = 45.20\,\text{m}$ (tape, 4 significant figures) in $t = 2.7\,\text{s}$ (stopwatch, 2 significant figures). Illustrative values.
**Find:** (a) the total pit-lane time; (b) the kart's average speed on the straight.

(a) Addition, so decimal places decide. The fewest is one, from $3.7\,\text{s}$:

$$28.412 + 3.7 + 30.25 = 62.362\,\text{s} \approx 62.4\,\text{s}$$

(b) Division, so significant figures decide. The fewest is two, from the time:

$$v = \frac{45.20\,\text{m}}{2.7\,\text{s}} = 16.74\ldots\,\text{m/s} \approx 17\,\text{m/s}$$

**Sanity check:** reverse (b): $17 \times 2.7 = 45.9\,\text{m}$, close to $45.20\,\text{m}$ as expected after rounding to two figures. In (a), the answer $62.4\,\text{s}$ has three significant figures, more than Arjun's two — which is fine, because in a sum the count of significant figures is not what's protected.

## Where the picture breaks

These rules are a quick guide, not a full error calculation. A hand-pressed stopwatch has a reaction-time error that may be a tenth of a second or more, so even the tenths digit of $62.4\,\text{s}$ is shaky; you'll treat that properly with errors and uncertainty. And $17\,\text{m/s}$ is the kart's **average** speed on the straight — it was still accelerating out of the previous corner.

## Key takeaway

Adding or subtracting: keep the fewest decimal places. Multiplying or dividing: keep the fewest significant figures. Round only at the end, and remember that exact, counted numbers never limit a result.
