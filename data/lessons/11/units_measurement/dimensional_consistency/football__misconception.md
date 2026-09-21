---
concept_id: dimensional_consistency
interest: football
format: misconception
title: If the dimensions match, is the hang time right
check:
  question: |-
    Priyanka writes $t = v/g$ for the total time a ball kicked straight up at speed $v$ spends in the air, and checks that both sides have dimensions $[\text{T}]$. Which statement is correct?
  options:
    A: |-
      It is dimensionally consistent but may still be wrong, since dimensions can't check numerical factors.
    B: |-
      It must be correct, because both sides have dimensions $[\text{T}]$.
    C: |-
      It is dimensionally inconsistent, because $v/g$ has the dimensions of a length.
    D: |-
      Dimensional analysis shows the factor should be $\tfrac{1}{2}$, so it should read $t = v/2g$.
  answer: A
  explanation: |-
    $[v/g] = [\text{L}\,\text{T}^{-1}]/[\text{L}\,\text{T}^{-2}] = [\text{T}]$, so the equation passes. But $v/g$ is only the time to reach the top; the total time up and down is $2v/g$. The missing $2$ is dimensionless, so no dimensional check can see it.
  misconceptions:
    B: |-
      Thinks passing the dimensional check proves an equation correct. Consistency is necessary, not sufficient.
    C: |-
      Makes a dimension error: dividing $[\text{L}\,\text{T}^{-1}]$ by $[\text{L}\,\text{T}^{-2}]$ cancels the L and leaves $[\text{T}]$, a time.
    D: |-
      Thinks dimensional analysis can find numerical factors. Pure numbers have no dimensions, so dimensions can't tell $\tfrac{1}{2}$ from $1$ or $2$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal with a tape while a match clock runs above the stands](scenes/football/units_measurement.svg "A clock measures what really happens. A formula only predicts it.")

It's the end of training, and the goalkeepers are messing about. Priyanka plays a game with Jatin: she volleys the ball straight up, as high as she can, and he has to guess how long it will be before it lands back at her feet.

Priyanka has just learnt about dimensions, and she wants to beat him with physics. She reckons her best kick leaves her boot at about $9.8\,\text{m/s}$, straight up. She writes a formula for the time in the air: $t = v/g$. Then she checks it: "$v$ over $g$ is metres per second divided by metres per second squared. That's seconds. Dimensions match — so it's right."

Her prediction: $9.8/9.8 = 1.0$ second.

Jatin starts his stopwatch as the ball leaves her boot and stops it as it lands back at her feet. He holds up the screen: $2.0$ seconds.

Twice as long. How can a formula that passed the dimension check be so wrong?

## The common belief

"If an equation is dimensionally consistent — every term has the same dimensions — then it is correct. The dimensional check is a proof."

## Why it feels right

The dimensional check really is powerful. It catches wrong powers, missing quantities and many copying errors in seconds, and it never gives a false alarm: if it says an equation is wrong, it *is* wrong. After watching it catch mistake after mistake, it's natural to trust it the other way round too — as if passing the test meant being right. And Priyanka's formula even has real physics in it: $v/g$ is a genuine time in this problem.

## What actually happens

Take upwards as positive. The ball leaves at $u = +9.8\,\text{m/s}$ and gravity slows it by $9.8\,\text{m/s}$ every second, so it stops rising after

$$t_\text{up} = \frac{u}{g} = \frac{9.8}{9.8} = 1.0\,\text{s}$$

That is exactly Priyanka's formula — but it's only the trip **up**. Ignoring air resistance, the fall back down takes just as long, so the total time in the air is

$$t = \frac{2u}{g} = \frac{2 \times 9.8}{9.8} = 2.0\,\text{s}$$

which matches Jatin's stopwatch. (You'll derive this properly with the equations of motion in the next chapter.)

Priyanka's formula was dimensionally perfect and physically wrong by a factor of $2$. A pure number has no dimensions, so the check was blind to it. It would be equally blind to $t = 3v/g$, or $t = \pi v/g$.

## The physics

**Principle of homogeneity:** every term added, subtracted or equated in a correct equation has the same dimensions.

![Two equations checked term by term: one consistent, one with a term of the wrong dimensions](figures/dimensional_consistency/homogeneity-check.svg "The check can prove an equation wrong, as in the bottom box. It can never prove an equation right.")

The logic runs one way only:

- **inconsistent** ⟹ certainly wrong;
- **consistent** ⟹ *possibly* right.

The misconception turns the second line into "consistent ⟹ right". Dimensional analysis cannot detect wrong dimensionless factors ($2$, $\tfrac{1}{2}$, $2\pi$), wrong signs, or a missing term that happens to have the right dimensions. To confirm an equation you need a derivation from physical laws, or a measurement — like Jatin's stopwatch.

## Worked example

**Given:** launch speed $u = 9.8\,\text{m/s}$ straight up; $g = 9.8\,\text{m/s}^2$; no air resistance.
**Find:** which candidate formulas pass the dimensional check, and what each predicts.

| Formula | Consistent? | Prediction |
|---|---|---|
| $t = 2u/g$ | yes | $2.0\,\text{s}$ |
| $t = u/g$ | yes | $1.0\,\text{s}$ |
| $t = 2u^2/g$ | no — gives $[\text{L}]$ | — |

Two formulas pass; only one matches the stopwatch.

**Sanity check:** the maximum height is $u^2/2g = 96.04/19.6 = 4.9\,\text{m}$, about twice the crossbar's $2.44\,\text{m}$ — a believable kick, and a ball falling $4.9\,\text{m}$ from rest does take $1.0\,\text{s}$, as the up-and-down symmetry says.

## Key takeaway

A dimensionally inconsistent equation is always wrong, but a consistent one is not automatically right. Dimensions can't see numerical factors, signs or missing terms: $t = v/g$ passes the check and is still half the true hang time, $2v/g$.
