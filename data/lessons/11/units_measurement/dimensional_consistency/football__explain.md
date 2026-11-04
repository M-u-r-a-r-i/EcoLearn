---
concept_id: dimensional_consistency
interest: football
format: explain
title: Settling a whiteboard argument about a lofted pass
check:
  question: |-
    Here $u$ and $v$ are velocities, $a$ is an acceleration, $t$ a time, $s$ a displacement, $m$ a mass, $g$ the acceleration due to gravity and $h$ a height. Which equation is dimensionally inconsistent?
  options:
    A: |-
      $v^2 = u^2 + 2as$
    B: |-
      $E = \tfrac{1}{2}mv^2 + mgh$
    C: |-
      $v = u + at^2$
    D: |-
      $s = \tfrac{1}{2}(u + v)\,t$
  answer: C
  explanation: |-
    In C, $v$ and $u$ are $[\text{L}\,\text{T}^{-1}]$ but $at^2$ is $[\text{L}\,\text{T}^{-2}][\text{T}^2] = [\text{L}]$, a length. A velocity can't be added to a length, so C must be wrong.
  misconceptions:
    A: |-
      Thinks squared terms can't balance a product like $as$. In fact $[a][s] = [\text{L}\,\text{T}^{-2}][\text{L}] = [\text{L}^2\,\text{T}^{-2}]$, the same as $v^2$.
    B: |-
      Thinks two different-looking energies can't be added. Both $\tfrac{1}{2}mv^2$ and $mgh$ work out to $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$, so the equation is consistent.
    D: |-
      Thinks the bracket or the $\tfrac{1}{2}$ spoils the balance. $u + v$ is a sum of two velocities, and velocity times time is a length, matching $s$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal with a tape, beside a scale, a gauge and a match clock](scenes/football/units_measurement.svg "Masses, lengths, times: each quantity has its own dimensions, and they don't mix.")

After training, the dressing-room whiteboard still has the coach's diagram of a long diagonal pass, the ball curving high over the midfield. Wasim, who likes to show off his physics, adds a line under it: the energy of the ball at the top of its flight.

*E = ½mv² + mg*

Irfan, the goalkeeper, takes the marker and corrects it: *E = ½mv² + mgh*.

"What's the $h$ for?" says Wasim. "The ball's energy is its moving part plus its weight. Mass times $g$ — that's the weight. Done."

"Mine has the height," Irfan says. "Higher ball, more energy."

Neither of them has done the energy chapter yet, and there's no textbook in the dressing room. Is there any way to decide, with just a marker, which line can't possibly be right?

## The physics

You can only add, subtract or equate quantities of the **same kind**. Goals can be added to goals, but never to minutes; a length can be added to a length, but never to a time. In physics this is the **principle of homogeneity of dimensions**:

> In a correct equation, every term that is added, subtracted or set equal must have the same dimensions.

An equation that obeys this is **dimensionally consistent**. One that breaks it is certainly wrong.

To test an equation, find the dimensions of **each term separately** and compare. For the whiteboard you need: mass $m$: $[\text{M}]$; speed $v$: $[\text{L}\,\text{T}^{-1}]$; $g$, an acceleration: $[\text{L}\,\text{T}^{-2}]$; height $h$: $[\text{L}]$; pure numbers like $\tfrac{1}{2}$: dimensionless.

**First term, common to both:** $\left[\tfrac{1}{2}mv^2\right] = [\text{M}][\text{L}\,\text{T}^{-1}]^2 = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$ — an energy.

**Wasim's second term:** $[mg] = [\text{M}][\text{L}\,\text{T}^{-2}] = [\text{M}\,\text{L}\,\text{T}^{-2}]$ — a force, not an energy. One L short. **Inconsistent.**

**Irfan's second term:** $[mgh] = [\text{M}][\text{L}\,\text{T}^{-2}][\text{L}] = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$ — matches. **Consistent.**

So Wasim's line is certainly wrong: you can't add a weight to an energy. Irfan's line passes. (You'll meet $mgh$, the gravitational potential energy, in the chapter on work and energy.)

![Two equations checked term by term. In v squared equals u squared plus 2as, every term is L squared T to the minus 2. In s equals ut plus half at, the last term is L T to the minus 1, so the equation is inconsistent](figures/dimensional_consistency/homogeneity-check.svg "Check every term, not just the two sides. One mismatched term is enough to prove an equation wrong.")

The same principle means the argument of a function like $\sin\theta$ or an exponential must be dimensionless — you can't take the sine of a length.

## Worked example

**Check** whether each equation is dimensionally consistent: (a) $t = \dfrac{v - u}{a}$; (b) $s = \dfrac{v^2 - u^2}{a^2}$.

(a) $[v - u] = [\text{L}\,\text{T}^{-1}]$ (a difference of two velocities). Divided by $[a] = [\text{L}\,\text{T}^{-2}]$: $[\text{L}\,\text{T}^{-1}]/[\text{L}\,\text{T}^{-2}] = [\text{T}]$, which matches $[t]$. **Consistent.**

(b) $[v^2 - u^2] = [\text{L}^2\,\text{T}^{-2}]$, and $[a^2] = [\text{L}^2\,\text{T}^{-4}]$. The ratio is $[\text{T}^2]$, but $s$ is $[\text{L}]$. **Inconsistent**, so (b) must be wrong. (The correct relation, $s = (v^2 - u^2)/2a$, is consistent: $[\text{L}^2\,\text{T}^{-2}]/[\text{L}\,\text{T}^{-2}] = [\text{L}]$.)

**Sanity check:** try (b) in SI units: $(\text{m/s})^2 \div (\text{m/s}^2)^2 = \text{s}^2$. A displacement in square seconds is nonsense, as expected.

## Where the picture breaks

Passing the test does not prove Irfan right. Dimensions ignore pure numbers, so $E = \tfrac{1}{2}mv^2 + 2mgh$ or $E = mv^2 + mgh$ would pass too. And the whiteboard's idea of "the ball's energy" leaves things out — the ball's spin, and energy lost to air resistance on the way up. A dimensionally inconsistent equation is certainly wrong; a consistent one is only *possibly* right.

## Key takeaway

Principle of homogeneity: every term added, subtracted or equated must have the same dimensions. Check each term separately; one mismatch proves the equation wrong ($mg$ is a force and can't be added to $\tfrac{1}{2}mv^2$). Passing the check is necessary but not sufficient.
