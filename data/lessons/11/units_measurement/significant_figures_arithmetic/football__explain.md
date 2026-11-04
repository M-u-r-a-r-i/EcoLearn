---
concept_id: significant_figures_arithmetic
interest: football
format: explain
title: How many digits does a turf order deserve
check:
  question: |-
    Video analysis shows a long pass travelled $38.4\,\text{m}$, and a stopwatch gives its flight time as $1.7\,\text{s}$. The ball's average speed, reported correctly, is:
  options:
    A: |-
      $22.6\,\text{m/s}$
    B: |-
      $23\,\text{m/s}$
    C: |-
      $22\,\text{m/s}$
    D: |-
      $22.588\,235\,\text{m/s}$
  answer: B
  explanation: |-
    $38.4/1.7 = 22.588\ldots$. In a quotient, keep as many significant figures as the least precise value: $1.7\,\text{s}$ has two, so round to two. The dropped part, $0.588$, is more than half, so $22.588 \to 23\,\text{m/s}$.
  misconceptions:
    A: |-
      Applies the decimal-places rule, which is for addition and subtraction: both inputs have one decimal place, so it keeps one. Division uses significant figures.
    C: |-
      Chops off the extra digits instead of rounding. The first dropped digit is $5$ followed by more digits, which is more than half, so the $2$ must be raised to $3$.
    D: |-
      Copies the calculator display. The time was only known to two significant figures, so most of those digits mean nothing.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures the goal with a tape, beside a scale and a match clock](scenes/football/units_measurement.svg "A careful steel tape, a rough cloth tape. When you multiply their readings, which one sets the precision?")

After a wet monsoon season, the penalty area at the school ground is mostly mud. Mr. Pillai, the head groundsman, needs fresh turf before the inter-house final, and he sends Arif and Sunita to measure the patch.

Arif runs a steel tape along the goal line, reading to the centimetre: $40.32\,\text{m}$. Sunita measures the depth of the area with the old cloth tape, which is only marked every ten centimetres: $16.5\,\text{m}$.

Sunita multiplies on her phone. "$665.28$ square metres. I'll put exactly that on the order."

"Put $670$," says Arif. "Nobody sells turf by the hundredth."

Mr. Pillai wants one honest number. Sunita's calculator gave five figures, Arif's rounding gave two. How many digits does the answer actually deserve — and who decides?

## The physics

When you calculate with measured values, the result can't be more precise than the data. NCERT gives two rules.

**Multiplying or dividing:** keep as many **significant figures** as the value with the fewest significant figures.

**Adding or subtracting:** keep as many **decimal places** as the value with the fewest decimal places.

![Left: 20.12 plus 1.5 gives 21.62, rounded to 21.6 because 1.5 has one decimal place. Right: 20.12 times 3.05 gives 61.366, rounded to 61.4 because 3.05 has three significant figures](figures/significant_figures_arithmetic/add-vs-multiply-rules.svg "Adding: the unknown hundredths of 1.5 spoil the hundredths of the sum. Multiplying: the answer keeps the significant figures of the least precise factor.")

The rules differ because they protect different things. In a sum, what matters is the **position** of the last reliable digit — tenths, hundredths. In a product, what matters is the **relative** precision of each factor, and that is what significant figures measure.

**Rounding off (NCERT):** look at the first digit you are dropping.

- More than $5$: raise the preceding digit by $1$ ($22.588 \to 23$).
- Less than $5$: leave the preceding digit as it is ($665.28 \to 665$).
- Exactly $5$, with nothing after it: if the preceding digit is even, leave it; if it is odd, raise it by $1$. So $17.25 \to 17.2$, but $17.35 \to 17.4$.

**Exact numbers** — counts like "two halves", or the $2$ in $2\pi r$ — have unlimited significant figures and never limit a result. In a calculation with several steps, carry one extra digit and round only at the end.

## Worked example

**Given:** penalty-area width $40.32\,\text{m}$ (4 significant figures, 2 decimal places); depth $16.5\,\text{m}$ (3 significant figures, 1 decimal place). Mr. Pillai also wants turf to run $0.75\,\text{m}$ past the edge of the area, measured with the steel tape.
**Find:** (a) the area of turf inside the penalty area; (b) the length of each turf strip laid from the goal line, $16.5\,\text{m} + 0.75\,\text{m}$.

(a) A product, so the fewest significant figures wins — three, from the depth:

$$A = 40.32\,\text{m} \times 16.5\,\text{m} = 665.28\,\text{m}^2 \approx 665\,\text{m}^2$$

The first dropped digit is $2$, less than $5$, so the $5$ stays.

(b) A sum, so the fewest decimal places wins — one, from $16.5$:

$$L = 16.5\,\text{m} + 0.75\,\text{m} = 17.25\,\text{m} \approx 17.2\,\text{m}$$

The dropped digit is exactly $5$ and the preceding $2$ is even, so NCERT's rule leaves it: $17.2\,\text{m}$.

**Sanity check:** reverse (a): $665 / 16.5 = 40.30\,\text{m}$, within a couple of centimetres of $40.32\,\text{m}$ — the gap is just rounding. Sunita's $665.28$ claimed five figures; Arif's $670$ threw one away. The honest order is $665\,\text{m}^2$.

## Where the picture breaks

Significant-figure rules are a quick guide, not a full error calculation — you'll handle uncertainty properly with absolute and relative errors. And a real turf order adds a safety margin for cutting and waste, which is a practical choice, not a statement about precision. That's fine, as long as nobody pretends the margin was measured.

## Key takeaway

Multiplying or dividing: keep the fewest significant figures of the data. Adding or subtracting: keep the fewest decimal places. Round once, at the end, with NCERT's rule for an exact $5$, and remember that counted and defined numbers never limit the result.
