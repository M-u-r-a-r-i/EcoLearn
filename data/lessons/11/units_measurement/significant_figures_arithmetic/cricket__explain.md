---
concept_id: significant_figures_arithmetic
interest: cricket
format: explain
title: How many digits does a quick single deserve
check:
  question: |-
    A batter runs a single between the popping creases, $17.68\,\text{m}$ apart, and a stopwatch gives $3.3\,\text{s}$. The average speed, reported to the correct number of significant figures, is:
  options:
    A: |-
      $5.358\,\text{m/s}$
    B: |-
      $5.4\,\text{m/s}$
    C: |-
      $5.36\,\text{m/s}$
    D: |-
      $5.357\,575\,\text{m/s}$
  answer: B
  explanation: |-
    $17.68/3.3 = 5.3576\ldots$. In a quotient, keep as many significant figures as the least precise value: $3.3\,\text{s}$ has two, so the answer is $5.4\,\text{m/s}$.
  misconceptions:
    A: |-
      Keeps the significant figures of the most precise value ($17.68$, four). The answer can't be more precise than the rougher measurement, the time.
    C: |-
      Applies the decimal-places rule, which is for addition and subtraction, and copies the two decimal places of $17.68$. Division uses significant figures.
    D: |-
      Copies the calculator display. Most of those digits are meaningless — the time was only measured to two significant figures.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch with a tape; a stopwatch nearby reads 3.50 seconds](scenes/cricket/units_measurement.svg "A tape measured to the centimetre, a stopwatch pressed by a thumb. Which one limits the answer?")

After fielding practice, Yash wants proof that he's the quickest runner between the wickets. His friend Harsh times him with a phone stopwatch as he sprints a single from one popping crease to the other: $3.3\,\text{s}$.

The popping creases are $17.68\,\text{m}$ apart; Harsh checked it with the ground's tape. He divides on his phone and reads out the answer: "Five point three five seven five seven five seven… metres per second!"

Yash is delighted. "Post exactly that on the team group. All the digits. Nobody else will have a number that precise."

Harsh hesitates. The tape was good to a centimetre. But his thumb on the stopwatch? Surely the answer can't be more precise than that. Then how many of those digits actually mean something?

## The physics

When you calculate with measured values, the result can't be more precise than the data. NCERT gives two rules.

**Multiplying or dividing:** the result keeps as many **significant figures** as the value with the fewest significant figures.

**Adding or subtracting:** the result keeps as many **decimal places** as the value with the fewest decimal places.

![Left: 20.12 plus 1.5 gives 21.62, rounded to 21.6 because 1.5 has one decimal place. Right: 20.12 times 3.05 gives 61.366, rounded to 61.4 because 3.05 has three significant figures](figures/significant_figures_arithmetic/add-vs-multiply-rules.svg "Adding: the unknown hundredths digit of 1.5 spoils the hundredths of the sum. Multiplying: the answer keeps the significant figures of the least precise factor.")

The two rules are different because they protect different things. In a sum, what matters is the **position** of the last reliable digit (tenths, hundredths). In a product, what matters is the **relative** precision, which is what significant figures measure.

**Rounding off (NCERT):** look at the first digit you are dropping.

- More than $5$: raise the preceding digit by $1$ ($61.366 \to 61.4$).
- Less than $5$: leave the preceding digit unchanged ($21.62 \to 21.6$).
- Exactly $5$, with nothing after it: if the preceding digit is even, leave it; if it is odd, raise it by $1$. So $2.745 \to 2.74$ but $2.735 \to 2.74$.
- A $5$ followed by other non-zero digits is more than half, so raise ($5.3576 \to 5.4$).

Two more points. **Exact numbers** — counted or defined, like "3 runs" or the $2$ in $2\pi r$ — have unlimited significant figures and never limit a result. And in a calculation with several steps, keep one extra digit in the intermediate results, and round only at the end.

## Worked example

**Given:** distance between popping creases $d = 17.68\,\text{m}$ (4 significant figures); time for a single $t = 3.3\,\text{s}$ (2 significant figures).
**Find:** (a) the average speed; (b) the total distance run in completing three runs.

(a) Division, so the fewest significant figures wins — two, from the time:

$$v = \frac{d}{t} = \frac{17.68\,\text{m}}{3.3\,\text{s}} = 5.3576\ldots\,\text{m/s} \approx 5.4\,\text{m/s}$$

The dropped part, $0.0576$, is more than half of $0.1$, so the $3$ rounds up to $4$.

(b) The $3$ in "three runs" is a count, so it is exact:

$$3 \times 17.68\,\text{m} = 53.04\,\text{m}$$

This keeps four significant figures, from the measured distance.

**Sanity check:** reverse (a): $5.4 \times 3.3 = 17.82\,\text{m}$, close to $17.68\,\text{m}$, as expected after rounding.

## Where the picture breaks

The significant-figure rules are a quick guide, not a full error calculation. A hand-pressed stopwatch has a reaction-time error that can easily be a tenth of a second or more, which you'll learn to handle properly with errors and uncertainty. And $5.4\,\text{m/s}$ is Yash's **average** speed; he starts from rest, accelerates, and slows to turn.

## Key takeaway

Multiplying or dividing: keep the fewest significant figures of the data. Adding or subtracting: keep the fewest decimal places. Round only at the end, and remember that exact numbers never limit the result.
