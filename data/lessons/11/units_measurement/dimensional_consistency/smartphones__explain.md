---
concept_id: dimensional_consistency
interest: smartphones
format: explain
title: The phone-drop formula that fails before you test it
check:
  question: |-
    A phone falls from rest through a height $h$; $g$ is the acceleration due to gravity, $v$ the speed on reaching the floor and $t$ the time taken. Which of these equations is dimensionally inconsistent?
  options:
    A: |-
      $v = 2gh$
    B: |-
      $v^2 = 2gh$
    C: |-
      $t = \sqrt{2h/g}$
    D: |-
      $h = \tfrac{1}{2}gt^2$
  answer: A
  explanation: |-
    $[gh] = [\text{L}\,\text{T}^{-2}][\text{L}] = [\text{L}^2\,\text{T}^{-2}]$, but $[v] = [\text{L}\,\text{T}^{-1}]$. The two sides have different dimensions, so A must be wrong. In B, C and D both sides match.
  misconceptions:
    B: |-
      Thinks a squared speed can't equal a product like $gh$. In fact $[v^2] = [\text{L}^2\,\text{T}^{-2}]$ and $[gh] = [\text{L}^2\,\text{T}^{-2}]$: they match.
    C: |-
      Thinks a square root of a ratio can't be a time. $[h/g] = [\text{L}]/[\text{L}\,\text{T}^{-2}] = [\text{T}^2]$, and its square root is $[\text{T}]$.
    D: |-
      Thinks the $\tfrac{1}{2}$ or the $t^2$ spoils the balance. The $\tfrac{1}{2}$ is dimensionless, and $[gt^2] = [\text{L}\,\text{T}^{-2}][\text{T}^2] = [\text{L}]$, the same as $h$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A study desk: a phone on a kitchen scale, a phone in a caliper, a charger with a USB meter, and a phone swinging from a shelf](scenes/smartphones/units_measurement.svg "Lengths, times, speeds: each has its own dimensions, and they can't be mixed.")

Sameer's phone slips out of his hand at the bus stop and cracks face-down on the pavement. That evening, sulking over the spider-web screen, he and his friend Rahul argue about how fast it was going when it hit.

Rahul has watched a video on drop tests. "There's a formula for it. Impact speed is $2gh$. Your hand was about $1.2\,\text{m}$ up, $g$ is $9.8$... so about $24\,\text{m/s}$. That's over $80\,\text{km/h}$! No wonder it cracked."

Sameer's class notes say something different: a square root, $\sqrt{2gh}$, which gives under $5\,\text{m/s}$.

They can't both be right. Neither of them wants to drop another phone to find out, and the video is long gone from Rahul's history. Is there a way to throw out a wrong formula using nothing but a pencil — before doing any experiment at all?

## The physics

You can only add, subtract or equate quantities of the **same kind**. You can add a length to a length, but never a length to a time — "$3\,\text{m} + 2\,\text{s}$" means nothing. In physics this is the **principle of homogeneity of dimensions**:

> In a correct equation, every term that is added, subtracted or set equal must have the same dimensions.

An equation that obeys this is **dimensionally consistent**. One that breaks it is certainly wrong, whatever numbers you put in.

To test an equation, find the dimensions of each term separately and compare. For a falling phone:

- height $h$: $[\text{L}]$; time $t$: $[\text{T}]$;
- speed $v$: $[\text{L}\,\text{T}^{-1}]$;
- acceleration due to gravity $g$: $[\text{L}\,\text{T}^{-2}]$;
- pure numbers like $2$ or $\tfrac{1}{2}$: dimensionless.

**Rahul's formula**, $v = 2gh$: the left side is $[\text{L}\,\text{T}^{-1}]$. The right side is $[\text{L}\,\text{T}^{-2}][\text{L}] = [\text{L}^2\,\text{T}^{-2}]$. They don't match, so $v = 2gh$ is **wrong**. His "$24\,\text{m/s}$" was never a speed at all: its unit is really $\text{m}^2/\text{s}^2$.

**Sameer's formula**, $v = \sqrt{2gh}$: the right side is $\sqrt{[\text{L}^2\,\text{T}^{-2}]} = [\text{L}\,\text{T}^{-1}]$. It matches the left side, so it is **consistent**. (You'll derive it from the equations of motion in the next chapter; here we only check it.)

![Two equations checked term by term. In v squared equals u squared plus 2as, every term is L squared T to the minus 2. In s equals ut plus half at, the last term is L T to the minus 1, so the equation is inconsistent](figures/dimensional_consistency/homogeneity-check.svg "Check every term, not just the two sides. One mismatched term is enough to prove an equation wrong.")

The same principle means the argument of a function like $\sin\theta$ or an exponential must be dimensionless: you can't take the sine of a length.

## Worked example

**Check** whether each equation is dimensionally consistent: (a) $t = \sqrt{2h/g}$ for the fall time; (b) $v = \sqrt{2g/h}$.

(a) $[h/g] = \dfrac{[\text{L}]}{[\text{L}\,\text{T}^{-2}]} = [\text{T}^2]$, and the square root gives $[\text{T}]$, matching $[t]$. **Consistent.**

(b) $[g/h] = \dfrac{[\text{L}\,\text{T}^{-2}]}{[\text{L}]} = [\text{T}^{-2}]$, and the square root gives $[\text{T}^{-1}]$ — a "per second", not a speed. **Inconsistent**, so (b) must be wrong.

Now the numbers from the story, using the consistent formula with $h = 1.2\,\text{m}$ and $g = 9.8\,\text{m/s}^2$:

$$v = \sqrt{2 \times 9.8 \times 1.2}\,\text{m/s} = \sqrt{23.52}\,\text{m/s} \approx 4.9\,\text{m/s}$$

**Sanity check:** in SI units, $\sqrt{(\text{m/s}^2)(\text{m})} = \sqrt{\text{m}^2/\text{s}^2} = \text{m/s}$. And $4.9\,\text{m/s}$ (about $18\,\text{km/h}$) is a believable speed for a short fall; over $80\,\text{km/h}$ from hand height is not.

## Where the picture breaks

Passing the test doesn't prove a formula right. Dimensions ignore pure numbers, so $v = \sqrt{gh}$ and $v = 2\sqrt{gh}$ are just as consistent as $\sqrt{2gh}$ — the check can't tell Sameer whether the $2$ belongs inside the root. And the formula itself assumes free fall from rest with no air resistance; for a phone falling a metre or two that's a good approximation, but not exact. A dimensionally inconsistent equation is certainly wrong; a consistent one is only *possibly* right.

## Key takeaway

Principle of homogeneity: every term added, subtracted or equated must have the same dimensions. Check each term separately; one mismatch proves the equation wrong. Passing the check is necessary but not sufficient — it can't catch a wrong numerical factor.
