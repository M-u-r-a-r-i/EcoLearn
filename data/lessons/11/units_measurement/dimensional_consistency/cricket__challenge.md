---
concept_id: dimensional_consistency
interest: cricket
format: challenge
title: Three remembered formulas for a high catch
check:
  question: |-
    A ball is dropped from a height $h$ during catching practice, where $g$ is the acceleration due to gravity. Which formula for its speed $v$ on reaching the ground could be correct?
  options:
    A: |-
      $v = \sqrt{2gh}$
    B: |-
      $v = 2gh$
    C: |-
      $v = \sqrt{2g/h}$
    D: |-
      $v = \sqrt{2h/g}$
  answer: A
  explanation: |-
    $[gh] = [\text{L}\,\text{T}^{-2}][\text{L}] = [\text{L}^2\,\text{T}^{-2}]$, and its square root is $[\text{L}\,\text{T}^{-1}]$ — a speed. Only A is dimensionally consistent.
  misconceptions:
    B: |-
      Forgets the square root: $2gh$ has dimensions $[\text{L}^2\,\text{T}^{-2}]$, a speed squared, not a speed.
    C: |-
      Divides by $h$ instead of multiplying: $\sqrt{g/h}$ has dimensions $[\text{T}^{-1}]$, a frequency, not a speed.
    D: |-
      Picks a formula for a time: $\sqrt{h/g}$ has dimensions $[\text{T}]$. It looks familiar because a fall time does have this form.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch; a stopwatch and a speed display stand nearby](scenes/cricket/units_measurement.svg "Heights, speeds and times: each has its own dimensions.")

It's high-catch practice. Coach Anand has a machine that fires balls almost straight up, and the fielders take turns under them. Between catches, Bhavna wonders how high the ball actually goes. The machine's display says it launches at $20\,\text{m/s}$.

"There's a formula," she says. "Height from launch speed. We did it last year." But nobody remembers it the same way.

Aman is certain: "Height equals $v^2$ over $2g$."
Chetan is equally certain: "No, $v$ over $2g$. There's no square."
Bhavna herself half-remembers: "Wasn't it $2g$ over $v^2$?"

The next ball is already in the air. No book, no phone. Can they rule out the wrong ones with nothing but the dimensions of $v$, $g$ and $h$?

## The challenge

A ball is launched straight up at speed $v$; $g$ is the acceleration due to gravity and $h$ is the maximum height reached (ignore air resistance). The three candidates are

$$\text{(1)}\; h = \frac{v^2}{2g} \qquad \text{(2)}\; h = \frac{v}{2g} \qquad \text{(3)}\; h = \frac{2g}{v^2}$$

Which of them are dimensionally consistent? For any that pass, what height does it predict for $v = 20\,\text{m/s}$ and $g = 9.8\,\text{m/s}^2$? Can dimensions alone prove the surviving formula is correct?

## Think first

Chetan's version looks simplest. Bhavna's has the same letters as Aman's, just rearranged — could both pass? And if one survives, does that mean it's definitely right, with the $2$ in the correct place? Commit to a guess.

## The reveal

The left side, a height, is $[\text{L}]$. Every candidate's right side must also be $[\text{L}]$. Use $[v] = [\text{L}\,\text{T}^{-1}]$ and $[g] = [\text{L}\,\text{T}^{-2}]$; the $2$ is dimensionless.

**(1)** $\left[\dfrac{v^2}{g}\right] = \dfrac{[\text{L}^2\,\text{T}^{-2}]}{[\text{L}\,\text{T}^{-2}]} = [\text{L}]$. **Consistent.**

**(2)** $\left[\dfrac{v}{g}\right] = \dfrac{[\text{L}\,\text{T}^{-1}]}{[\text{L}\,\text{T}^{-2}]} = [\text{T}]$. That's a time, not a height. **Inconsistent** — Chetan's formula is wrong. (Interestingly, $v/g$ *is* the time the ball takes to reach the top.)

**(3)** $\left[\dfrac{g}{v^2}\right] = \dfrac{[\text{L}\,\text{T}^{-2}]}{[\text{L}^2\,\text{T}^{-2}]} = [\text{L}^{-1}]$. An inverse length. **Inconsistent** — and it would absurdly predict a *lower* catch for a faster launch.

Only Aman's survives. For $v = 20\,\text{m/s}$:

$$h = \frac{(20\,\text{m/s})^2}{2 \times 9.8\,\text{m/s}^2} = \frac{400}{19.6}\,\text{m} \approx 20\,\text{m}$$

The units confirm it: $\text{m}^2\,\text{s}^{-2} \div \text{m}\,\text{s}^{-2} = \text{m}$.

But can dimensions *prove* the $2$? No. $h = v^2/g$ is equally consistent and would predict about $41\,\text{m}$. Dimensions eliminated two wrong formulas; the factor of $2$ has to come from the equations of motion (next chapter) or from measurement. Real balls also go a little lower than this, because of air resistance.

## The physics

**Principle of homogeneity:** in a correct physical equation, every term that is added, subtracted or equated has the same dimensions.

![Two equations checked term by term; one is consistent, one is not](figures/dimensional_consistency/homogeneity-check.svg "The same method as the catch: work out the dimensions of every term and compare.")

How to use it:

1. Write the dimensions of each symbol.
2. Work out the dimensions of each term separately; pure numbers are dimensionless.
3. If any term differs, the equation is wrong.
4. If all match, the equation *may* be right — a dimensional check can't detect wrong dimensionless factors like $2$, $\tfrac{1}{2}$ or $2\pi$.

## Key takeaway

A correct equation must have the same dimensions in every term. Use this to throw out impossible formulas quickly: $h = v/2g$ gives a time and $h = 2g/v^2$ an inverse length, so only $h = v^2/2g$ can be right. Surviving the test is necessary, not sufficient.
