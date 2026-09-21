---
concept_id: dimensional_consistency
interest: cricket
format: misconception
title: If the dimensions match, is the formula right
check:
  question: |-
    Pranav writes $s = ut + at^2$ for the distance a ball rolls with constant acceleration, and checks that every term has dimensions $[\text{L}]$. Which statement is correct?
  options:
    A: |-
      It must be correct, because every term has dimensions $[\text{L}]$.
    B: |-
      It is dimensionally inconsistent, because $at^2$ has different dimensions from $ut$.
    C: |-
      It is dimensionally consistent but may still be wrong, since dimensions can't check numerical factors.
    D: |-
      Dimensional analysis shows the factor should be $2$, so it should read $s = ut + 2at^2$.
  answer: C
  explanation: |-
    Both $ut$ and $at^2$ are $[\text{L}]$, so the equation passes. But the correct equation is $s = ut + \tfrac{1}{2}at^2$; the missing $\tfrac{1}{2}$ is dimensionless, so no dimensional check can detect it.
  misconceptions:
    A: |-
      Thinks passing the dimensional check proves an equation correct. Consistency is necessary, not sufficient.
    B: |-
      Makes a dimension error: $[a][t^2] = [\text{L}\,\text{T}^{-2}][\text{T}^2] = [\text{L}]$, the same as $[u][t]$.
    D: |-
      Thinks dimensional analysis can find numerical factors. Pure numbers have no dimensions, so dimensions can't tell $\tfrac{1}{2}$ from $1$ or $2$.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch with a tape; a stopwatch nearby](scenes/cricket/units_measurement.svg "The tape measures what really happens. The formula only predicts it.")

It's a ground-fielding drill on the outfield. Coach Rekha rolls the ball hard along the grass, and the fielders chase it. Pranav, who has just learnt about dimensions, wants to predict where each ball will be after three seconds.

He writes his formula confidently: $s = ut + at^2$. Then he checks it the way he was taught: $ut$ is a length, $at^2$ is a length, $s$ is a length. "Dimensions match. So it's right."

His friend Sana has a tape measure. The next ball is rolled at about $10\,\text{m/s}$ and slows steadily at about $2\,\text{m/s}^2$. Pranav's formula predicts $12\,\text{m}$ after three seconds. Sana marks where the ball is when the stopwatch hits three seconds, and runs the tape out.

It's nowhere near $12$ metres. How can a formula that passed the dimension check give the wrong answer?

## The common belief

"If an equation is dimensionally consistent — every term has the same dimensions — then it is correct. The dimensional check is a proof."

## Why it feels right

The dimensional check really is powerful. It catches wrong powers, missing quantities and many copying mistakes in a few seconds, and it never gives a false alarm: if it says an equation is wrong, it *is* wrong. After seeing it catch errors again and again, it is natural to trust it the other way round too, as if passing the test meant being right.

## What actually happens

Take the direction of the roll as positive. Then $u = +10\,\text{m/s}$ and the acceleration is $a = -2.0\,\text{m/s}^2$ (the ball slows down). Pranav's formula:

$$s = ut + at^2 = 10 \times 3 + (-2.0) \times 3^2 = 30 - 18 = 12\,\text{m}$$

The correct equation of motion (you'll derive it in the next chapter) is $s = ut + \tfrac{1}{2}at^2$:

$$s = 10 \times 3 + \tfrac{1}{2} \times (-2.0) \times 3^2 = 30 - 9 = 21\,\text{m}$$

Sana's tape shows about $21\,\text{m}$. Pranav's formula was dimensionally perfect and physically wrong: it was missing a $\tfrac{1}{2}$, and a pure number has no dimensions, so the check couldn't see it.

The same blindness hides other errors. $s = ut - \tfrac{1}{2}at^2$ (a wrong sign) and $s = ut$ (a missing term) also pass.

## The physics

**Principle of homogeneity:** every term added, subtracted or equated in a correct equation has the same dimensions.

![Two equations checked term by term: one consistent, one with a term of the wrong dimensions](figures/dimensional_consistency/homogeneity-check.svg "The check can prove an equation wrong, as in the bottom box. It can never prove an equation right.")

The logic runs one way only:

- **inconsistent** ⟹ certainly wrong;
- **consistent** ⟹ *possibly* right.

The misconception reverses the second line into "consistent ⟹ right". Dimensional analysis cannot detect wrong dimensionless constants ($\tfrac{1}{2}$, $2\pi$), wrong signs, or missing terms that have the right dimensions. To confirm an equation, you need a derivation from physical laws or a measurement — like Sana's tape.

## Worked example

**Given:** $u = 10\,\text{m/s}$, $a = -2.0\,\text{m/s}^2$ (constant), and three candidate formulas.
**Find:** which pass the dimensional check, and what each predicts at $t = 3.0\,\text{s}$.

| Formula | Consistent? | Prediction |
|---|---|---|
| $s = ut + \tfrac{1}{2}at^2$ | yes | $21\,\text{m}$ |
| $s = ut + at^2$ | yes | $12\,\text{m}$ |
| $s = ut + \tfrac{1}{2}at$ | no | — |

Two formulas pass; only one matches the measurement.

**Sanity check:** at $3.0\,\text{s}$ the ball's velocity is $10 - 2.0 \times 3.0 = 4.0\,\text{m/s}$, so it is still rolling forward, and a distance well under $30\,\text{m}$ makes sense.

## Key takeaway

A dimensionally inconsistent equation is always wrong, but a consistent one is not automatically right. Dimensions can't see numerical factors, signs or missing terms — check those with a derivation or an experiment.
