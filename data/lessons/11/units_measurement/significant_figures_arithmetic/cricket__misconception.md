---
concept_id: significant_figures_arithmetic
interest: cricket
format: misconception
title: Should the answer be as precise as your best measurement
check:
  question: |-
    Two cones at the nets are $20.00\,\text{m}$ apart (steel tape), and a speed gun shows the ball at $38\,\text{m/s}$. Treating the speed as constant, the time between the cones, reported correctly, is:
  options:
    A: |-
      $0.53\,\text{s}$
    B: |-
      $0.5263\,\text{s}$
    C: |-
      $1\,\text{s}$
    D: |-
      $0.526\,315\,79\,\text{s}$
  answer: A
  explanation: |-
    $t = 20.00/38 = 0.5263\ldots\,\text{s}$. In a division, keep the fewest significant figures of the data: $38\,\text{m/s}$ has two, so $t = 0.53\,\text{s}$.
  misconceptions:
    B: |-
      Keeps the four significant figures of the most precise measurement, the tape. A result is limited by its least precise input, not its best one.
    C: |-
      Applies the decimal-places rule (for sums) to a division: $38$ has no decimal places, so the answer is wrongly rounded to a whole number.
    D: |-
      Copies the calculator display, as if every digit shown were measured.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch; a speed display shows 142 km/h and a stopwatch reads 3.50 seconds](scenes/cricket/units_measurement.svg "One number from a careful tape, one from a speed display. The answer can only be as good as the weaker one.")

Coach Rao has set the bowling machine to fire short balls, and Kavya wants to know how long she has to react. She and Nitin lay two cones on the practice strip and measure the gap with a steel tape, very carefully: $20.00\,\text{m}$. The speed gun beside the machine shows $38\,\text{m/s}$.

Kavya divides on her phone and writes $0.5263\,\text{s}$ in her notebook.

"Why four figures?" Nitin asks.

"Because we measured the distance to four figures," Kavya says. "We spent ten minutes getting that tape exactly straight. If I round the answer to two figures, all that careful work is wasted."

It sounds almost noble. But is her answer really known to a ten-thousandth of a second?

## The common belief

"A result should be as precise as the most precise measurement that went into it. Rounding to fewer figures throws away the effort you put into your best measurement."

## Why it feels right

Part of it is true: careful measurement is valuable, and it would be a waste to throw away good digits for no reason. And the calculator does show all those digits, so it feels as though they must be real. In everyday life, we tend to trust a number more when it has more decimal places.

What the belief forgets is that a calculation mixes all its inputs. Precision can be lost at any one of them.

## What actually happens

The speed gun shows $38\,\text{m/s}$: two significant figures. That means the speed could be anything from about $37.5$ to $38.5\,\text{m/s}$. Try both ends:

$$t_\text{max} = \frac{20.00}{37.5} = 0.5333\,\text{s} \qquad t_\text{min} = \frac{20.00}{38.5} = 0.5195\,\text{s}$$

The true time lies somewhere between $0.52$ and $0.53\,\text{s}$. Even the second significant figure is a little uncertain. Kavya's third and fourth digits, $6$ and $3$, are pure calculator noise.

Her careful tape wasn't wasted; it just wasn't the bottleneck. Improving the tape further would change nothing. To get a better time, she would need a more precise speed.

So the honest answer is $t = 0.53\,\text{s}$: two significant figures, the same as the least precise measurement.

## The physics

NCERT's rules for calculating with measured values:

- **Multiplication and division:** the result keeps as many significant figures as the input with the **fewest** significant figures.
- **Addition and subtraction:** the result keeps as many decimal places as the input with the **fewest** decimal places.

![Left: adding 20.12 and 1.5 gives 21.6. Right: 20.12 times 3.05 gives 61.4](figures/significant_figures_arithmetic/add-vs-multiply-rules.svg "In both rules, the weakest input decides. That is exactly what the belief gets backwards.")

The belief picks the **most** precise input; the rules pick the **least** precise. A chain is only as strong as its weakest link.

When rounding, NCERT's rule is: raise the preceding digit if the first dropped digit is more than $5$, leave it if less than $5$, and if the dropped digit is exactly $5$, leave an even preceding digit unchanged and raise an odd one. Here $0.5263$ has dropped digits $63$, which are more than half, so it rounds to $0.53$.

## Worked example

**Given:** distance $d = 20.00\,\text{m}$ (4 significant figures), speed $v = 38\,\text{m/s}$ (2 significant figures), speed assumed constant.
**Find:** the time, correctly reported.

$$t = \frac{d}{v} = \frac{20.00\,\text{m}}{38\,\text{m/s}} = 0.5263\ldots\,\text{s} \approx 0.53\,\text{s}$$

**Sanity check:** $0.53\,\text{s} \times 38\,\text{m/s} = 20.14\,\text{m}$, close to $20.00\,\text{m}$ — the small gap is just rounding. (Real balls also slow down and bounce, so the constant-speed time is only an estimate.)

## Key takeaway

A calculated result is limited by its **least** precise input, not its most precise one. For products and quotients, keep the fewest significant figures in the data; for sums and differences, the fewest decimal places.
