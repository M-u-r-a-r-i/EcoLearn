---
concept_id: dimensional_formulae
interest: cricket
format: misconception
title: Does the half in kinetic energy change its dimensions
check:
  question: |-
    A ball of mass $m$ moves at speed $v$. What is the dimensional formula of its kinetic energy, $\tfrac{1}{2}mv^2$?
  options:
    A: |-
      $[\tfrac{1}{2}\,\text{M}\,\text{L}^2\,\text{T}^{-2}]$
    B: |-
      $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$
    C: |-
      $[\text{M}\,\text{L}\,\text{T}^{-2}]$
    D: |-
      $[\text{M}\,\text{L}^2\,\text{T}^{-1}]$
  answer: B
  explanation: |-
    The $\tfrac{1}{2}$ is a pure number with no dimensions. $[m] = [\text{M}]$ and $[v^2] = [\text{L}\,\text{T}^{-1}]^2 = [\text{L}^2\,\text{T}^{-2}]$, so $[\tfrac{1}{2}mv^2] = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$.
  misconceptions:
    A: |-
      Carries the numerical factor into the dimensional formula. Numbers change the size of a quantity, not its kind, so they never appear in dimensions.
    C: |-
      Squares the $\text{T}^{-1}$ but not the L, writing $v^2$ as $[\text{L}\,\text{T}^{-2}]$ like an acceleration — which gives the dimensions of force, not energy.
    D: |-
      Squares the L in the velocity but not the $\text{T}^{-1}$. Squaring $[\text{L}\,\text{T}^{-1}]$ squares every factor: $[\text{L}^2\,\text{T}^{-2}]$.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch; a ball sits on a scale and a speed display glows](scenes/cricket/units_measurement.svg "The same ball, the same speed. Two formulas that differ by a half.")

The match is on TV, but Lavanya and her cousin Farhan are supposed to be doing their dimensions homework. Question 4: *find the dimensional formula of kinetic energy.*

Farhan writes: $[\tfrac{1}{2}\,\text{M}\,\text{L}^2\,\text{T}^{-2}]$.

Lavanya frowns. "Why is there a half inside the brackets?"

"Because kinetic energy is *half* of $mv^2$," Farhan says. "So it must have half the dimensions of $mv^2$. They're different kinds of quantity. It's obvious — $\tfrac{1}{2}x$ isn't the same as $x$."

On the TV, a spinner's ball grips and turns sharply. "And while we're at it," Farhan adds, "the angle that ball turned through is in radians. Radians are a unit. So angles have dimensions too."

Lavanya isn't sure how to argue with him. Does a half belong inside a dimensional formula? And what are the dimensions of an angle?

## The common belief

"Every part of a formula, including numbers like $\tfrac{1}{2}$ and $2\pi$, belongs in its dimensional formula. So $\tfrac{1}{2}mv^2$ and $mv^2$ have different dimensions. And an angle, which has a unit (the radian), must have dimensions."

## Why it feels right

In algebra, $\tfrac{1}{2}x$ really is different from $x$, and it's natural to expect every symbol in a formula to show up in its "fingerprint". The radian also looks like a unit — it has a name and a symbol, just like the metre. And students are told that dimensional formulas must be exact, so leaving something out feels careless.

Part of Farhan's instinct is right: $\tfrac{1}{2}mv^2$ and $mv^2$ are different **amounts**. The ball's kinetic energy really is half of $mv^2$.

## What actually happens

Dimensions describe the **kind** of quantity, not the **amount**. Multiplying a quantity by a number changes how much of it there is, not what it is. Half a pitch length is still a length; half an over's worth of time is still a time. So $\tfrac{1}{2}mv^2$ and $mv^2$ are both energies, and both are measured in joules.

Take a ball of $0.16\,\text{kg}$ at $30\,\text{m/s}$ (illustrative):

$$\tfrac{1}{2}mv^2 = 72\,\text{J} \qquad mv^2 = 144\,\text{J}$$

Different sizes, same unit, same dimensions $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$. You could never put "$\tfrac{1}{2}$" into a unit anyway — there is no such thing as a "half-joule unit".

Angles work the same way. An angle in radians is defined as arc length divided by radius, $\theta = s/r$:

$$[\theta] = \frac{[\text{L}]}{[\text{L}]} = [\text{M}^0\,\text{L}^0\,\text{T}^0]$$

So an angle is **dimensionless**. The radian is a name for this ratio, not a new base quantity.

## The physics

A **dimensional formula** gives the powers of the base quantities — [M], [L], [T] in mechanics — in a physical quantity. Build it from the defining equation, replacing each quantity by its dimensions.

![A ladder of quantities from velocity to power with their dimensional formulas](figures/dimensional_formulae/dimension-building-blocks.svg "Work and energy: [M L² T⁻²]. As the footnote says, pure numbers such as ½ carry no dimensions.")

Pure numbers ($\tfrac{1}{2}$, $2$, $\pi$), angles and ratios of like quantities are **dimensionless**: they are left out of the dimensional formula. This is exactly where the misconception goes wrong. It is also why dimensional analysis can never find numerical factors like $\tfrac{1}{2}$ — a limitation you'll meet later in this chapter.

When a quantity is squared, every factor inside is squared: $[v^2] = [\text{L}\,\text{T}^{-1}]^2 = [\text{L}^2\,\text{T}^{-2}]$.

## Key takeaway

Dimensional formulas describe what kind of quantity something is, not how much of it there is. Numbers like $\tfrac{1}{2}$ and angles are dimensionless and never appear: $[\tfrac{1}{2}mv^2] = [mv^2] = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$.
