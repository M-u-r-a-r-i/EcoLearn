---
concept_id: significant_figures_arithmetic
interest: football
format: challenge
title: How high did the goalkeeper really jump
check:
  question: |-
    A goalkeeper's standing reach is $2.315\,\text{m}$ (steel tape) and her jump height is $0.52\,\text{m}$. Her predicted jumping reach, $2.315\,\text{m} + 0.52\,\text{m}$, reported correctly, is:
  options:
    A: |-
      $2.835\,\text{m}$
    B: |-
      $2.83\,\text{m}$
    C: |-
      $2.84\,\text{m}$
    D: |-
      $2.8\,\text{m}$
  answer: C
  explanation: |-
    The sum is $2.835\,\text{m}$. In addition, keep the fewest decimal places: $0.52$ has two. The dropped digit is exactly $5$ and the preceding digit $3$ is odd, so NCERT's rule raises it: $2.84\,\text{m}$.
  misconceptions:
    A: |-
      Keeps every digit of the sum. The jump height is unknown in the thousandths place, so the thousandths digit of the total is unknown too.
    B: |-
      Chops off the $5$ (or always rounds a $5$ down). NCERT's rule raises an odd preceding digit when the dropped digit is exactly $5$.
    D: |-
      Uses the multiplication rule (fewest significant figures, two, from $0.52$) for a sum. Addition keeps decimal places, not significant figures.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal 2.44 metres high with a tape](scenes/football/units_measurement.svg "The crossbar is 2.44 m up. A goalkeeper needs to reach well above it.")

Lakshmi keeps goal for the state under-19 side, and the new goalkeeping coach measures everything. First, standing reach: Lakshmi stands flat-footed against the wall with her arm raised, and he measures to her fingertips with a steel tape, to the millimetre: $2.315\,\text{m}$.

Then she chalks her fingers and jumps as high as she can, slapping the wall. The chalk mark is smudged, so he can only read its height to the nearest centimetre: $2.84\,\text{m}$.

"Jump height, $0.525\,\text{m}$," says Neel, the reserve keeper, reading his calculator.

"Round it: $0.53$," says Asha. "Fives always go up."

"Neither," says the coach, and hands Lakshmi the tape. "You tell me what goes on your fitness card."

Lakshmi looks at the two readings, one to a millimetre and one to a centimetre. Which of them decides the answer?

## The challenge

Standing reach: $2.315\,\text{m}$. Jumping reach: $2.84\,\text{m}$.

1. What is Lakshmi's jump height, reported correctly?
2. She is $1.68\,\text{m}$ tall. What is her jump height as a fraction of her height, reported correctly?

## Think first

Neel keeps three decimal places, like the more precise reading. Asha rounds the $5$ up out of habit. Is either right? And for part 2 — does the answer keep three significant figures, like $2.84$ and $1.68$, or has something been lost along the way? Commit to answers first.

## The reveal

**Part 1: a difference.** Adding or subtracting, keep as many **decimal places** as the value with the fewest.

$$h = 2.84\,\text{m} - 2.315\,\text{m} = 0.525\,\text{m}$$

The chalk mark has two decimal places, so the thousandths digit of the answer is unknown. Round to two decimal places. The dropped digit is **exactly** $5$, so NCERT's rule looks at the preceding digit: $2$ is even, so leave it.

$$h \approx 0.52\,\text{m}$$

Neel's $0.525$ claims a millimetre nobody measured; the chalk mark wasn't that good. Asha's "fives always go up" isn't NCERT's rule: a dropped $5$ raises an **odd** preceding digit and leaves an **even** one.

![Left: adding 20.12 and 1.5 gives 21.62, rounded to 21.6. Right: 20.12 times 3.05 gives 61.366, rounded to 61.4](figures/significant_figures_arithmetic/add-vs-multiply-rules.svg "Two different rules. For the jump height, count decimal places; for the fraction of her height, count significant figures.")

**Part 2: a quotient.** Multiplying or dividing, keep as many **significant figures** as the value with the fewest. Here's the surprise: the jump height $0.52\,\text{m}$ has only **two** significant figures, even though both readings had three or four. Subtracting two close numbers kept the decimal places but lost significant figures.

Carry the unrounded $0.525$ through, and round only at the end:

$$\frac{h}{H} = \frac{0.525\,\text{m}}{1.68\,\text{m}} = 0.3125 \approx 0.31$$

Two significant figures. (Using $0.52$ instead gives $0.3095 \approx 0.31$ — the same, as it should be.) The metres cancel, so the fraction has no unit.

## The physics

NCERT's rules for arithmetic with measured values:

- **Addition and subtraction:** keep as many decimal places as the value with the fewest decimal places.
- **Multiplication and division:** keep as many significant figures as the value with the fewest significant figures.

**Rounding (NCERT):** if the first dropped digit is more than $5$, raise the preceding digit; if less than $5$, leave it; if it is exactly $5$, leave an even preceding digit and raise an odd one ($0.525 \to 0.52$, $2.835 \to 2.84$).

Carry an extra digit through multi-step work and round once, at the end. And watch subtractions of nearly equal numbers: they can leave far fewer significant figures than you started with.

## Key takeaway

Sums and differences keep the fewest **decimal places**: $2.84 - 2.315 \to 0.52\,\text{m}$. Products and quotients keep the fewest **significant figures**: $0.525/1.68 \to 0.31$. An exact $5$ is dropped by NCERT's even-odd rule, not always rounded up.
