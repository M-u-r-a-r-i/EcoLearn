---
concept_id: dimensional_derivation
interest: football
format: misconception
title: Can dimensions tell a wet pitch from a dry one
check:
  question: |-
    Harsh uses dimensional analysis to find the distance a player slides in a tackle: $s = k\,v^2/g$, where $v$ is the speed at the start of the slide. What can you correctly conclude?
  options:
    A: |-
      The surface can't affect the slide, because only $v$ and $g$ appear in the formula.
    B: |-
      A dimensionless quantity, such as how grippy the surface is, can hide inside $k$, so $k$ may differ between surfaces.
    C: |-
      The player's mass must also appear, because heavier players slide further.
    D: |-
      The formula is dimensionally wrong; it should be $s = k\,v/g$.
  answer: B
  explanation: |-
    Dimensional analysis only fixes the powers of quantities that have dimensions. A pure number describing the surface (the coefficient of friction) has no dimensions, so it is invisible to the method and ends up inside $k$. For a sliding body, $s = v^2/2\mu g$.
  misconceptions:
    A: |-
      Believes dimensional analysis always finds every quantity a result depends on. It can't detect dimensionless variables, or any quantity you left off your list.
    C: |-
      Holds the everyday idea that heavier bodies slide further. Dimensionally, mass can't appear — nothing else contains M to balance it — and friction theory agrees.
    D: |-
      Makes a dimension error: $v/g$ has dimensions $[\text{T}]$, a time. Harsh's $v^2/g$ is correctly a length.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal with a tape along the goal line](scenes/football/units_measurement.svg "The groundsman measures the pitch. Does the state of the grass matter too?")

It poured all night, and the morning's practice match is on a soaking pitch. Harsh, a centre-back, goes in for a sliding tackle near the halfway line — and keeps sliding, and sliding, clean past the winger and almost to the touchline. Everyone laughs, including him.

Back on the bench, he gets out his notebook. He's just learnt dimensional analysis. "A slide should depend on how fast I'm going, $v$, my mass $m$, and $g$," he says. He matches the powers and gets $s = k\,v^2/g$. "So at the same speed, I slide the same distance on any pitch. It's physics. Today's slide must have been because I was running faster."

Coach Baruah shakes her head. "You weren't faster. On Tuesday's dry pitch you'd have stopped in half the distance."

Harsh re-checks the algebra. It's perfect. So if the maths can't be faulted, how can the wet grass matter?

## The common belief

"Dimensional analysis finds the complete formula. If a quantity mattered, it would show up when you match the dimensions. If it isn't in the answer, it doesn't affect the result."

## Why it feels right

Harsh's method was genuinely right as far as it went. He correctly found that the slide doesn't depend on mass, and that it grows as $v^2$ — both true. The algebra is rigorous, it produces a definite answer, and every step can be checked. It *feels* like the method looked at everything and found what matters.

## What actually happens

Dimensional analysis only ever looks at the quantities **you** put on the list. It can't add anything you forgot — and there's a whole class of quantities it can never see at all: **dimensionless** ones.

How grippy a surface is can be described by a pure number, the **coefficient of friction**, $\mu$ (you'll meet it in the chapter on the laws of motion). It's a ratio of two forces, so $[\mu] = [\text{M}^0\,\text{L}^0\,\text{T}^0]$. Put it on Harsh's list and try to find its power: it contributes nothing to M, L or T, so *any* power satisfies the dimensional equation. The method can't decide, and $\mu$ simply hides inside $k$.

The full theory gives, for a body sliding to rest with steady friction,

$$s = \frac{v^2}{2\mu g}$$

so $k = 1/(2\mu)$, which is different for every surface. With illustrative values $v = 6.0\,\text{m/s}$, $\mu \approx 0.50$ on dry grass and $\mu \approx 0.25$ on wet grass:

$$s_\text{dry} = \frac{36}{2 \times 0.50 \times 9.8} \approx 3.7\,\text{m} \qquad s_\text{wet} = \frac{36}{2 \times 0.25 \times 9.8} \approx 7.3\,\text{m}$$

Twice as far on the wet pitch — the coach was right, and Harsh's formula was right too. It was just incomplete in a way it could never reveal.

## The physics

**Dimensional analysis** finds the form of a relation by assuming it is a product of powers of the relevant quantities and matching M, L and T on both sides. Its limitations are exactly where the belief goes wrong:

- It gives the right answer only if **you chose the right quantities**. Leave one out, and the method won't warn you.
- **Dimensionless quantities** — a coefficient of friction, an angle, a ratio — are invisible to it and get absorbed into $k$.
- It **cannot find dimensionless constants** (the $\tfrac{1}{2}$ here, $2\pi$ for a pendulum).
- It **fails for sums of terms** and for **trigonometric, exponential and logarithmic** relations.
- In mechanics it can find **at most three** unknown powers.

![A simple pendulum: a small bob of mass m on a string of length l, swinging under gravity g](figures/dimensional_derivation/pendulum-labelled.svg "The pendulum has the same blind spot: its swing angle is dimensionless, so dimensional analysis can't say how large swings change the period.")

## Worked example

**Given:** Harsh's form $s = k\,v^2/g$ holds on any one surface (with its own $k$).
**Find:** on the wet pitch, how far he slides if he starts at $4.0\,\text{m/s}$ instead of $6.0\,\text{m/s}$.

Same surface, same $k$, so use a ratio:

$$\frac{s_2}{s_1} = \left(\frac{4.0}{6.0}\right)^2 = 0.444 \quad\Rightarrow\quad s_2 \approx 0.444 \times 7.35 \approx 3.3\,\text{m}$$

**Sanity check:** directly, $16/(2 \times 0.25 \times 9.8) = 3.3\,\text{m}$ — the same. Ratios on one surface are safe; comparisons *between* surfaces need $\mu$.

## Key takeaway

Dimensional analysis can't see what isn't on your list, or anything dimensionless. It gives $s = k\,v^2/g$ for a slide, but the surface's grippiness hides inside $k$: $s = v^2/2\mu g$. Trust its ratios on one surface; don't trust it to tell you what matters.
