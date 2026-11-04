---
concept_id: dimensional_derivation
interest: football
format: challenge
title: Kick it twice as fast and how much higher does it go
check:
  question: |-
    Assume the maximum height $h$ of a ball kicked straight up depends only on its launch speed $v$, its mass $m$ and $g$. Dimensional analysis gives:
  options:
    A: |-
      $h = k\,v/g$
    B: |-
      $h = k\,m v^2/g$
    C: |-
      $h = k\,g/v^2$
    D: |-
      $h = k\,v^2/g$
  answer: D
  explanation: |-
    Put $h = k\,m^a v^b g^c$: $[\text{L}] = [\text{M}^a\,\text{L}^{b+c}\,\text{T}^{-b-2c}]$. So $a = 0$, $b + c = 1$ and $b + 2c = 0$, giving $c = -1$, $b = 2$: $h = k\,v^2/g$.
  misconceptions:
    A: |-
      Guesses a simple ratio without matching dimensions: $v/g$ has dimensions $[\text{T}]$, a time, not a height.
    B: |-
      Keeps the mass in. No other quantity contains M, so its power must be zero; $mv^2/g$ has an unbalanced M.
    C: |-
      Inverts the ratio: $g/v^2$ has dimensions $[\text{L}^{-1}]$, and it would wrongly predict a lower ball for a faster kick.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal 2.44 metres high; a match clock runs above the stands](scenes/football/units_measurement.svg "The crossbar is a handy ruler for a ball kicked straight up.")

The last ten minutes of practice are for fun, and today it's the "sky kick" contest: volley the ball straight up, as high as you can, standing beside the goal so the crossbar gives a scale.

Rhea's first kick is gentle, and the ball just reaches the crossbar, about $2.4\,\text{m}$. Vikas has a phone app that estimates the ball's launch speed from video: about $7\,\text{m/s}$.

"Watch this," says Rhea. "Next one I'll kick twice as fast. Twice the speed, twice the height — I'll get it to five metres."

Vikas isn't so sure. "Last week my kick was about twice as fast as my little brother's, and his hardly got over his head while mine went way up. More than twice."

A heavier, wet ball is lying by the post too. Rhea wonders if that would go higher or lower.

Who is right? And can you tell, without a single equation of motion?

## The challenge

A ball is kicked straight up at speed $v$ and rises to a maximum height $h$. Suppose $h$ depends only on $v$, the ball's mass $m$ and the acceleration due to gravity $g$ (ignore air resistance).

1. Use dimensional analysis to find how $h$ depends on $v$, $m$ and $g$.
2. If Rhea doubles her launch speed, how many times higher does the ball go?

## Think first

Rhea says twice the speed means twice the height. Vikas says more than twice — but how much more? Four times? Eight? And does the heavier wet ball rise lower, as it feels like it should? Pick your answers before reading on.

## The reveal

Assume $h = k\,m^a\,v^b\,g^c$, where $k$ is a dimensionless constant. Put in dimensions:

$$[\text{L}] = [\text{M}]^a\,[\text{L}\,\text{T}^{-1}]^b\,[\text{L}\,\text{T}^{-2}]^c = [\text{M}^a\,\text{L}^{b+c}\,\text{T}^{-b-2c}]$$

Match powers:

- M: $a = 0$
- T: $-b - 2c = 0$, so $b = -2c$
- L: $b + c = 1$, so $-2c + c = 1$, giving $c = -1$ and $b = 2$

$$h = k\,\frac{v^2}{g}$$

The mass drops out: ignoring air resistance, the wet ball kicked at the same speed rises to the same height. And the height grows as the **square** of the speed. Doubling the speed gives

$$\frac{h_2}{h_1} = \left(\frac{2v}{v}\right)^2 = 4$$

Four times as high — about $4 \times 2.4 \approx 10\,\text{m}$, far above Rhea's "five metres". Vikas's hunch was right.

Why more than double? A faster ball starts higher up the "speed ladder": gravity takes away speed at the same rate either way, so the faster kick keeps climbing for twice as long, and at a higher average speed too. Twice the time times twice the average speed gives four times the height.

With the equations of motion (next chapter) you can find the constant: $h = v^2/2g$, so $k = \tfrac{1}{2}$. For $7.0\,\text{m/s}$: $h = 49/19.6 = 2.5\,\text{m}$ — the crossbar, as seen. For $14\,\text{m/s}$: $h = 196/19.6 = 10\,\text{m}$. Exactly four times — and the ratio came out right without knowing $k$.

## The physics

**Deriving a relation by dimensional analysis:**

1. Decide which quantities the result depends on.
2. Write the result as $k$ times a product of their powers.
3. Equate the powers of M, L and T on both sides and solve.

![A graph of pendulum period against length: a red square-root curve for the real period, and a lower dashed curve with the same shape](figures/dimensional_derivation/period-vs-length.svg "Another relation found the same way: a pendulum's period grows as the square root of its length. Dimensions give the shape; only experiment gives the constant (2π).")

**Limitations:** it cannot find dimensionless constants ($k$); it relies on your list of quantities being right and complete; in mechanics it can find at most three unknown powers; and it fails for relations that are sums of terms or involve trigonometric, exponential or logarithmic functions. It is most useful for **ratios**, where the unknown $k$ cancels.

## Key takeaway

Dimensional analysis gives $h = k\,v^2/g$ for a ball kicked straight up: independent of mass, and growing as the square of the speed. So twice the speed sends the ball four times as high. The constant ($k = \tfrac{1}{2}$) can't be found this way — but in a ratio, you don't need it.
