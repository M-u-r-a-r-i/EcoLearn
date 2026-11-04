---
concept_id: dimensional_consistency
interest: cricket
format: explain
title: Rescuing a smudged formula on the team bus
check:
  question: |-
    Here $u$ and $v$ are velocities, $a$ is an acceleration, $t$ is a time and $s$ is a displacement. Which equation is dimensionally inconsistent?
  options:
    A: |-
      $v = u + at$
    B: |-
      $s = ut + \tfrac{1}{2}at^2$
    C: |-
      $v^2 = u^2 + 2as$
    D: |-
      $s = ut + \tfrac{1}{2}at$
  answer: D
  explanation: |-
    In D, $s$ and $ut$ are $[\text{L}]$ but $\tfrac{1}{2}at$ is $[\text{L}\,\text{T}^{-2}][\text{T}] = [\text{L}\,\text{T}^{-1}]$, a velocity. Terms of different dimensions can't be added, so D must be wrong.
  misconceptions:
    A: |-
      Judges by the look of the symbols ("an acceleration can't be added to a velocity") instead of working out dimensions: $at$ is $[\text{L}\,\text{T}^{-2}][\text{T}] = [\text{L}\,\text{T}^{-1}]$, a velocity.
    B: |-
      Thinks the $t^2$ or the $\tfrac{1}{2}$ spoils the balance. $\tfrac{1}{2}at^2$ is $[\text{L}\,\text{T}^{-2}][\text{T}^2] = [\text{L}]$, the same as $s$.
    C: |-
      Thinks squared quantities can't match a product like $as$. In fact $[a][s] = [\text{L}\,\text{T}^{-2}][\text{L}] = [\text{L}^2\,\text{T}^{-2}]$, the same as $v^2$.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch with a tape; a stopwatch and a speed display nearby](scenes/cricket/units_measurement.svg "Lengths, times, speeds: each has its own dimensions, and they don't mix.")

The team bus to the away match is three hours long, and Vihaan has a physics test on Monday. He opens his formula notebook — and finds that his water bottle has leaked all over it.

One line has survived, mostly. It's the equation for the distance covered by a body with constant acceleration: $s = ut + \tfrac{1}{2}a\,t$... and then a wet blot where there might, or might not, have been a small "2" above the last $t$.

"Just check the book on Monday," says Rishi, the wicketkeeper, from the next seat.

But Vihaan wants to revise now, and there's no book and no signal. Is there any way to decide, sitting on a bus with only a pencil, whether that last $t$ should be squared?

## The physics

You can only add, subtract or equate quantities of the **same kind**. Runs can be added to runs, but runs can't be added to overs; a length can be added to a length, but never to a time. In physics this is the **principle of homogeneity of dimensions**:

> In a correct equation, every term that is added, subtracted or set equal must have the same dimensions.

An equation that obeys this is **dimensionally consistent**. One that breaks it is certainly wrong.

To test an equation, find the dimensions of each term separately and compare them. The quantities you'll need:

- displacement $s$: $[\text{L}]$; time $t$: $[\text{T}]$;
- velocity $u$ or $v$: $[\text{L}\,\text{T}^{-1}]$;
- acceleration $a$: $[\text{L}\,\text{T}^{-2}]$;
- pure numbers like $\tfrac{1}{2}$ or $2$: dimensionless.

Now Vihaan's two candidates (you'll study these equations of motion properly in the next chapter; here we only check them):

**With $t$:** $\left[\tfrac{1}{2}at\right] = [\text{L}\,\text{T}^{-2}][\text{T}] = [\text{L}\,\text{T}^{-1}]$ — a velocity, while $s$ and $ut$ are lengths. Inconsistent.

**With $t^2$:** $\left[\tfrac{1}{2}at^2\right] = [\text{L}\,\text{T}^{-2}][\text{T}^2] = [\text{L}]$ — matches $s$ and $ut$, both $[\text{L}]$. Consistent.

![Two equations checked term by term. In v squared equals u squared plus 2as, every term is L squared T to the minus 2. In s equals ut plus half at, the last term is L T to the minus 1, so the equation is inconsistent](figures/dimensional_consistency/homogeneity-check.svg "Check every term, not just the two sides. One mismatched term is enough to prove an equation wrong.")

So the blot hid a "2". The correct equation is $s = ut + \tfrac{1}{2}at^2$.

The same principle also means that the argument of a function like $\sin\theta$ or an exponential must be dimensionless — you can't take the sine of a length.

## Worked example

**Check** whether each equation is dimensionally consistent: (a) $v^2 = u^2 + 2as$; (b) $v = u + as$.

(a) $[v^2] = [u^2] = [\text{L}\,\text{T}^{-1}]^2 = [\text{L}^2\,\text{T}^{-2}]$. And $[2as] = [\text{L}\,\text{T}^{-2}][\text{L}] = [\text{L}^2\,\text{T}^{-2}]$. All three terms match: **consistent**.

(b) $[v] = [u] = [\text{L}\,\text{T}^{-1}]$, but $[as] = [\text{L}\,\text{T}^{-2}][\text{L}] = [\text{L}^2\,\text{T}^{-2}]$. The last term doesn't match: **inconsistent**, so (b) must be wrong.

**Sanity check:** in (b), try it in SI units: $\text{m/s} + (\text{m/s}^2)(\text{m}) = \text{m/s} + \text{m}^2/\text{s}^2$. You can't add those, just as you can't add runs to overs.

## Where the picture breaks

Passing the test does not prove an equation right. Dimensions ignore pure numbers, so $s = ut + at^2$ (no $\tfrac{1}{2}$) is also consistent, and so is $s = ut + 3at^2$. The dimensional check told Vihaan the power of $t$, but it can't tell him whether the $\tfrac{1}{2}$ is right; for that he needs the derivation or the book. A dimensionally inconsistent equation is certainly wrong; a consistent one is only *possibly* right.

## Key takeaway

Principle of homogeneity: every term added, subtracted or equated must have the same dimensions. Check each term separately; one mismatch proves the equation wrong. Passing the check is necessary but not sufficient — it can't catch a wrong numerical factor.
