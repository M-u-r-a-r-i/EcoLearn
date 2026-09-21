---
concept_id: dimensional_derivation
interest: cricket
format: misconception
title: Can dimensions alone predict how fast the dropped ball lands
check:
  question: |-
    Sameer uses dimensional analysis to get $v = \sqrt{gh}$ for the speed of a ball dropped from rest through a height $h$, and says the formula is exact. What is wrong with his claim?
  options:
    A: |-
      Nothing — dimensional analysis always gives the exact formula.
    B: |-
      The ball's mass should appear, because heavier balls fall faster.
    C: |-
      The formula should be $v = \sqrt{g/h}$ for the dimensions to match.
    D: |-
      Dimensions can't fix the dimensionless constant; the correct result (ignoring air) is $v = \sqrt{2gh}$.
  answer: D
  explanation: |-
    Dimensional analysis gives only $v = k\sqrt{gh}$ with $k$ unknown. The equations of motion (or an experiment) give $k = \sqrt{2}$, so $v = \sqrt{2gh}$, about $41\%$ larger than Sameer's value.
  misconceptions:
    A: |-
      Believes dimensional analysis gives complete formulas. It can never find a pure-number factor, because numbers have no dimensions.
    B: |-
      Holds the everyday idea that heavier objects fall faster. Without air resistance they don't — and dimensionally, mass can't appear, since nothing else contains M to balance it.
    C: |-
      Makes a dimension error: $\sqrt{g/h}$ has dimensions $[\text{T}^{-1}]$, not a speed. Sameer's form $\sqrt{gh}$ was dimensionally right.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch with a tape; a ball rests on a scale nearby](scenes/cricket/units_measurement.svg "Before a big match, groundstaff check everything about the pitch — including how the ball bounces.")

Sameer's aunt is the curator at a district ground. One way groundstaff get a feel for a pitch's bounce is simple: drop a ball from a fixed height and watch how high it comes back up. This morning she's dropping one from a stand $5.0\,\text{m}$ above the pitch.

Sameer has just learnt dimensional analysis, and he's proud of it. "I can tell you how fast the ball hits the pitch without any experiment," he says. He writes: $v = k\,m^a\,g^b\,h^c$, matches the powers, and gets $v = \sqrt{gh}$. "So $v = \sqrt{9.8 \times 5.0} = 7.0$ metres per second. Exactly."

His aunt films the next drop in slow motion, with a marked pole behind the ball. Frame by frame, Sameer measures the speed just before impact: close to $10\,\text{m/s}$.

His algebra was careful. His dimensions matched. So why is his "exact" answer so far off?

## The common belief

"Dimensional analysis gives you the complete formula for a physical quantity. If the dimensions balance, the formula is exact — you don't need the equations of motion or an experiment."

## Why it feels right

The method really is powerful. Sameer correctly found that the speed doesn't depend on the mass, and that it grows as $\sqrt{h}$ — both true. The algebra is rigorous and the answer *looks* complete, with no gaps or blanks. And sometimes the unknown constant happens to be close to $1$, so a dimensional estimate lands near the right value, which reinforces the habit.

## What actually happens

Every step Sameer did was right except the last one, where he quietly set $k = 1$. Dimensional analysis only ever gives

$$v = k\sqrt{gh}$$

because a pure number like $k$ has no dimensions, and so no dimensional equation can pin it down. For a ball dropped from rest (ignoring air resistance), the equation of motion $v^2 = u^2 + 2gh$ — which you'll meet in the next chapter — with $u = 0$ gives

$$v = \sqrt{2gh} = \sqrt{2 \times 9.8 \times 5.0} = \sqrt{98} \approx 9.9\,\text{m/s}$$

So $k = \sqrt{2} \approx 1.41$, and the slow-motion video agrees. Sameer's value was about $30\%$ too low.

## The physics

**Dimensional analysis** finds the form of a relation by assuming it is a product of powers of the relevant quantities and matching the dimensions M, L, T on both sides. Its limitations are exactly where the belief goes wrong:

- It **cannot determine dimensionless constants** ($\sqrt{2}$ here, $2\pi$ for a pendulum, $\tfrac{1}{2}$ in kinetic energy).
- It **fails for sums of terms**: $s = ut + \tfrac{1}{2}at^2$ can't be derived, only checked.
- It **fails for trigonometric, exponential and logarithmic** relations.
- In mechanics it can find **at most three** unknown powers (one per base quantity).
- It gives the right answer only if **you chose the right quantities**. Leave one out, or include a wrong one, and the method won't warn you.

![A graph of pendulum period against length: the true red curve and a much lower dashed curve with the same shape](figures/dimensional_derivation/period-vs-length.svg "The same trap in another relation: setting k = 1 gives the dashed curve, far below the real pendulum's 2π times larger values.")

To find $k$, you need physical laws (like the equations of motion) or an experiment.

## Worked example

**Given:** drop height $h = 5.0\,\text{m}$; $g = 9.8\,\text{m/s}^2$; measured impact speed about $9.9\,\text{m/s}$.
**Find:** Sameer's prediction, and the value of $k$ implied by the measurement.

$$v_\text{Sameer} = \sqrt{gh} = \sqrt{49} = 7.0\,\text{m/s}$$

$$k = \frac{v_\text{measured}}{\sqrt{gh}} = \frac{9.9}{7.0} \approx 1.41 \approx \sqrt{2}$$

**Sanity check:** what dimensional analysis *did* get right can be tested with a ratio, where $k$ cancels. Dropping from $4 \times 5.0 = 20\,\text{m}$ should double the speed: $\sqrt{2 \times 9.8 \times 20} = \sqrt{392} \approx 19.8\,\text{m/s}$, exactly twice $9.9$.

## Key takeaway

Dimensional analysis gives the form of a relation, not the whole formula: here $v = k\sqrt{gh}$, with $k = \sqrt{2}$ coming from the equations of motion or experiment. It can't find numerical constants and fails for sums of terms and for sine, exponential or log relations. Trust its ratios; don't trust its $k = 1$.
