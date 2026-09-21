---
concept_id: dimensional_derivation
interest: cricket
format: challenge
title: How much longer does a higher catch hang in the air
check:
  question: |-
    Assume the speed $v$ of a ball dropped from rest through a height $h$ depends only on its mass $m$, on $g$ and on $h$. Dimensional analysis gives:
  options:
    A: |-
      $v = k\,mgh$
    B: |-
      $v = k\sqrt{gh}$
    C: |-
      $v = k\sqrt{h/g}$
    D: |-
      $v = k\sqrt{mgh}$
  answer: B
  explanation: |-
    Put $v = k\,m^a g^b h^c$: $[\text{L}\,\text{T}^{-1}] = [\text{M}^a\,\text{L}^{b+c}\,\text{T}^{-2b}]$. So $a = 0$, $b = \tfrac{1}{2}$, $c = \tfrac{1}{2}$, giving $v = k\sqrt{gh}$.
  misconceptions:
    A: |-
      Multiplies the quantities together without matching dimensions: $mgh$ is an energy, $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$, not a speed.
    C: |-
      Divides by $g$ instead of multiplying: $\sqrt{h/g}$ has dimensions $[\text{T}]$, a time.
    D: |-
      Keeps the mass in. No other quantity contains M, so its power must be zero; $\sqrt{mgh}$ has an unbalanced $\text{M}^{1/2}$.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch; a stopwatch reads 3.50 seconds](scenes/cricket/units_measurement.svg "A stopwatch settles arguments — or starts them.")

In the final of the inter-college tournament, a top-edge goes straight up. Keerthi, keeping wicket, calls for it, waits, waits, and finally takes the catch. The crowd roars.

Afterwards, in the dressing room, she's still buzzing. "Did you see how high that went? At least four times higher than the one I dropped last week. And I had to wait four times as long for it to come down. My legs were shaking."

Sahil, who timed both catches on the scorer's stopwatch, isn't so sure about the "four times as long". His two numbers were much closer than that.

Keerthi insists: four times higher must mean four times the wait. But how does the hang time of a ball really depend on how high it goes? And can you work it out without any equations of motion at all?

## The challenge

A ball goes straight up to a maximum height $h$ and falls back down. Suppose its total time in the air, $t$, depends only on $h$, the ball's mass $m$ and the acceleration due to gravity $g$ (ignore air resistance).

1. Use dimensional analysis to find how $t$ depends on $h$, $m$ and $g$.
2. If one catch goes four times as high as another, how many times longer is its hang time?

## Think first

Keerthi says four times as long. Maybe it's even more than four — sixteen? Or maybe height doesn't matter much at all, because a higher ball also falls faster? And does a heavier ball hang for less time? Pick an answer.

## The reveal

Assume $t = k\,h^a\,m^b\,g^c$, where $k$ is a dimensionless constant. Put in dimensions:

$$[\text{T}] = [\text{L}]^a\,[\text{M}]^b\,[\text{L}\,\text{T}^{-2}]^c = [\text{M}^b\,\text{L}^{a+c}\,\text{T}^{-2c}]$$

Match powers:

- M: $b = 0$
- T: $-2c = 1$, so $c = -\tfrac{1}{2}$
- L: $a + c = 0$, so $a = \tfrac{1}{2}$

$$t = k\sqrt{\frac{h}{g}}$$

The mass drops out: a heavier ball hangs for the same time (ignoring air). And the time grows only as the **square root** of the height. Four times as high gives

$$\frac{t_2}{t_1} = \sqrt{\frac{4h}{h}} = \sqrt{4} = 2$$

Keerthi waited **twice** as long, not four times. That matches Sahil's stopwatch.

A higher ball does go up for longer, but it also leaves the bat faster and falls back faster, so time doesn't keep pace with height. And the answer "sixteen times" squares the ratio where the dimensions demand a square root.

With the equations of motion (next chapter), you can find the constant: $t = 2\sqrt{2h/g}$, so $k = 2\sqrt{2} \approx 2.83$. For a $5\,\text{m}$ catch, $t = 2\sqrt{10/9.8} \approx 2.0\,\text{s}$; for $20\,\text{m}$, $t = 2\sqrt{40/9.8} \approx 4.0\,\text{s}$. Exactly double — the ratio came out right even without knowing $k$.

## The physics

**Deriving a relation by dimensional analysis:**

1. Decide which quantities the result depends on.
2. Write the result as $k$ times a product of their powers.
3. Equate the powers of M, L and T on both sides and solve.

![A graph of pendulum period against length: a red square-root curve for the real period, and a lower dashed curve with the same shape](figures/dimensional_derivation/period-vs-length.svg "Another square-root law found the same way: a pendulum's period. Four times the length gives twice the period, but the constant (2π) must come from experiment.")

**Limitations:** it cannot find dimensionless constants ($k$); it relies on your list of quantities being right and complete; in mechanics it can find at most three unknown powers; and it fails for relations that are sums of terms or involve trigonometric, exponential or logarithmic functions. It is most useful for **ratios**, where the unknown $k$ cancels.

## Key takeaway

Dimensional analysis gives $t = k\sqrt{h/g}$ for a ball's hang time: independent of mass, and growing as the square root of the height. So four times higher means twice as long. The constant $k$ can't be found this way — but in a ratio, you don't need it.
