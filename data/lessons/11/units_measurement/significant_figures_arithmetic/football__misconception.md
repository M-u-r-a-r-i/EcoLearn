---
concept_id: significant_figures_arithmetic
interest: football
format: misconception
title: Does one rounding rule work for every sum
check:
  question: |-
    In a fitness drill, players run the length of the pitch, $105.0\,\text{m}$, then $9.25\,\text{m}$ along the goal line (both measured with tapes). The total distance, reported correctly, is:
  options:
    A: |-
      $114.3\,\text{m}$
    B: |-
      $114.25\,\text{m}$
    C: |-
      $114.2\,\text{m}$
    D: |-
      $114\,\text{m}$
  answer: C
  explanation: |-
    The sum is $114.25\,\text{m}$. For addition, keep the fewest decimal places: $105.0$ has one. The dropped digit is exactly $5$ and the preceding $2$ is even, so NCERT's rule leaves it: $114.2\,\text{m}$.
  misconceptions:
    A: |-
      Always rounds a $5$ up. NCERT's rule leaves an even preceding digit unchanged when the dropped digit is exactly $5$.
    B: |-
      Keeps the decimal places of the more precise term. The sum is limited by the term with the fewest decimal places.
    D: |-
      Uses the significant-figure rule (fewest significant figures, three, from $9.25$) for a sum. That rule is for products and quotients; sums keep decimal places.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal with a tape while a match clock reads 45:00](scenes/football/units_measurement.svg "Two halves, two sources of data. How precise can the total be?")

After a friendly, Aakash scrolls through his numbers. In the first half he wore the club's GPS vest, which logged $5.46\,\text{km}$. At half-time the vest's battery died, so for the second half he used a running app on his phone, which showed $4.9\,\text{km}$.

He adds them up and posts on the team group: *Total distance: 10 km.*

His teammate Ruth replies at once: "Why not $10.36$?"

"Rules," Aakash types back. "My Class 11 book says the answer keeps the fewest significant figures. $4.9$ has two, so the answer has two. $10$."

Coach Rosamma reads the thread and sends one line: "You ran $360$ metres more than you're claiming, and you want the rulebook to take them away?"

Aakash scrolls back through his notes. The rule *is* in his book. Isn't it?

## The common belief

"When you calculate with measured values, the answer keeps as many significant figures as the least precise value. That's the rule for everything — adding, subtracting, multiplying and dividing."

## Why it feels right

The rule Aakash remembers is real: it is exactly the NCERT rule for **multiplying and dividing**. It's the first rounding rule most students learn, and one rule for everything feels tidier than two. Often the two rules even give the same answer, which hides the difference. And the instinct behind it is sound: the result can't be more precise than the roughest measurement.

The belief goes wrong only in *how* it measures "roughest" for a sum.

## What actually happens

In a sum, what matters is **where** each value's uncertain digit sits. The phone's $4.9\,\text{km}$ is uncertain in the tenths place, about $0.1\,\text{km}$. The vest's $5.46\,\text{km}$ is uncertain in the hundredths. Add them, and the total is uncertain in the tenths:

$$5.46\,\text{km} + 4.9\,\text{km} = 10.36\,\text{km} \approx 10.4\,\text{km}$$

That's one decimal place — and three significant figures, not two. Aakash's "$10\,\text{km}$" implies an uncertainty of about a whole kilometre, ten times worse than his data.

To see how badly the significant-figure rule fails for sums, take an extreme case. The pitch is $105.0\,\text{m}$ long; add the width of a painted line, about $0.12\,\text{m}$. The fewest significant figures is two, from $0.12$, so the "rule" would give $1.1 \times 10^2\,\text{m}$ — adding a strip of paint would move the end of the pitch by five metres! The decimal-places rule gives $105.12 \to 105.1\,\text{m}$, which makes sense.

## The physics

NCERT's rules for calculating with measured values:

- **Addition and subtraction:** keep as many **decimal places** as the value with the fewest decimal places.
- **Multiplication and division:** keep as many **significant figures** as the value with the fewest significant figures.

![Left: 20.12 plus 1.5 gives 21.62, rounded to 21.6. Right: 20.12 times 3.05 gives 61.366, rounded to 61.4](figures/significant_figures_arithmetic/add-vs-multiply-rules.svg "Two operations, two rules. Using the right-hand rule for a sum is exactly the mistake in the story.")

The reason: a sum's uncertainty depends on the absolute size of each value's last uncertain digit, so decimal places are the right measure. A product's uncertainty depends on each factor's **relative** precision, which is what significant figures track.

**Rounding (NCERT):** raise the preceding digit if the first dropped digit is more than $5$; leave it if less than $5$; if it is exactly $5$, leave an even preceding digit and raise an odd one.

## Worked example

**Given:** first half $5.46\,\text{km}$ (vest); second half $4.9\,\text{km}$ (phone).
**Find:** (a) the total distance; (b) the average speed over the $90$ minutes of play.

(a) A sum — one decimal place: $10.36 \to 10.4\,\text{km}$.

(b) A quotient. Ignore added time and treat the playing time as the Laws' $90$ minutes, an exact number: $90\,\text{min} = 1.5\,\text{h}$.

$$v = \frac{10.36\,\text{km}}{1.5\,\text{h}} = 6.906\ldots\,\text{km/h} \approx 6.91\,\text{km/h}$$

Three significant figures, from the distance $10.4\,\text{km}$ — now the significant-figure rule applies. (Carry the unrounded $10.36$ in, round at the end.)

**Sanity check:** $6.91 \times 1.5 = 10.37\,\text{km}$, back where we started, give or take rounding.

## Key takeaway

There are two rules, not one. Sums and differences keep the fewest **decimal places**; products and quotients keep the fewest **significant figures**. $5.46 + 4.9 = 10.4\,\text{km}$, not $10\,\text{km}$.
