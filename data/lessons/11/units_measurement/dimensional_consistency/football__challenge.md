---
concept_id: dimensional_consistency
interest: football
format: challenge
title: How much run-off space does a sprinting player need
check:
  question: |-
    A player running at speed $v$ slows down with a constant deceleration of size $a$. Which formula for the time $t$ he takes to stop could be correct?
  options:
    A: |-
      $t = a/v$
    B: |-
      $t = v^2/a$
    C: |-
      $t = va$
    D: |-
      $t = v/a$
  answer: D
  explanation: |-
    $[v/a] = [\text{L}\,\text{T}^{-1}]/[\text{L}\,\text{T}^{-2}] = [\text{T}]$, a time. Only D has the dimensions of $t$.
  misconceptions:
    A: |-
      Inverts the ratio: $[a/v] = [\text{T}^{-1}]$, an inverse time (a rate), not a time.
    B: |-
      Uses the square that appears in the stopping-distance formula: $[v^2/a] = [\text{L}]$, a length, not a time.
    C: |-
      Multiplies instead of dividing: $[va] = [\text{L}^2\,\text{T}^{-3}]$, which is not a time.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal with a tape; the grass stretches behind the goal line](scenes/football/units_measurement.svg "Behind every goal line there must be room to stop. How much?")

The town's new artificial-turf ground is being built, and Kiran's mother is on the planning committee. One question has the committee stuck: how much empty space to leave between the goal line and the fence, so a striker sprinting after a through ball can stop safely.

Kiran brings the question to his team. They agree on the numbers to use — a fast sprint of about $8.0\,\text{m/s}$, and a hard, steady braking of about $4.0\,\text{m/s}^2$ — but not on the formula.

Om is certain: "Distance equals $v^2$ over $2a$."
Leela is equally certain: "No squares. It's $v$ over $2a$."
Kiran half-remembers something else: "Wasn't it $2a$ over $v^2$?"

None of them has the kinematics chapter yet. Can they rule out the wrong formulas using nothing but the dimensions of $v$, $a$ and $s$?

## The challenge

A player runs at speed $v$ and decelerates uniformly at rate $a$ until he stops, covering a distance $s$. The three candidates are

$$\text{(1)}\; s = \frac{v^2}{2a} \qquad \text{(2)}\; s = \frac{v}{2a} \qquad \text{(3)}\; s = \frac{2a}{v^2}$$

Which are dimensionally consistent? For any that pass, what distance does it give for $v = 8.0\,\text{m/s}$ and $a = 4.0\,\text{m/s}^2$? Can dimensions alone prove the survivor is correct?

## Think first

Leela's formula is the simplest. Kiran's has the same letters as Om's, just flipped — could both pass? And if one survives, does that prove the $2$ is in the right place? Make your guesses.

## The reveal

The left side, a distance, is $[\text{L}]$, so every right side must be $[\text{L}]$ too. Use $[v] = [\text{L}\,\text{T}^{-1}]$ and $[a] = [\text{L}\,\text{T}^{-2}]$; the $2$ is dimensionless.

**(1)** $\left[\dfrac{v^2}{a}\right] = \dfrac{[\text{L}^2\,\text{T}^{-2}]}{[\text{L}\,\text{T}^{-2}]} = [\text{L}]$. **Consistent.**

**(2)** $\left[\dfrac{v}{a}\right] = \dfrac{[\text{L}\,\text{T}^{-1}]}{[\text{L}\,\text{T}^{-2}]} = [\text{T}]$. A time, not a distance. **Inconsistent.** (Interestingly, $v/a$ *is* the time the player takes to stop.)

**(3)** $\left[\dfrac{a}{v^2}\right] = \dfrac{[\text{L}\,\text{T}^{-2}]}{[\text{L}^2\,\text{T}^{-2}]} = [\text{L}^{-1}]$. An inverse length. **Inconsistent** — and it would absurdly say a *faster* player stops in a *shorter* distance.

Only Om's survives. For the agreed numbers:

$$s = \frac{(8.0\,\text{m/s})^2}{2 \times 4.0\,\text{m/s}^2} = \frac{64}{8.0}\,\text{m} = 8.0\,\text{m}$$

The units confirm it: $\text{m}^2\,\text{s}^{-2} \div \text{m}\,\text{s}^{-2} = \text{m}$.

But can dimensions *prove* the $2$? No. $s = v^2/a$ is just as consistent and would give $16\,\text{m}$. Dimensions threw out two impossible formulas; the factor of $2$ has to come from the equations of motion (next chapter) or from measurement. A committee would also add a safety margin, since real players don't brake perfectly steadily.

## The physics

**Principle of homogeneity:** in a correct physical equation, every term that is added, subtracted or equated has the same dimensions.

![Two equations checked term by term; one is consistent, one is not](figures/dimensional_consistency/homogeneity-check.svg "The same method as the run-off question: work out the dimensions of every term and compare.")

How to use it:

1. Write the dimensions of each symbol.
2. Work out the dimensions of each term separately; pure numbers are dimensionless.
3. If any term differs, the equation is wrong.
4. If all match, the equation *may* be right — the check can't detect wrong dimensionless factors like $2$, $\tfrac{1}{2}$ or $2\pi$.

## Key takeaway

A correct equation has the same dimensions in every term. That throws out impossible formulas fast: $v/2a$ is a time and $2a/v^2$ an inverse length, so only $s = v^2/2a$ can be the stopping distance. Surviving the test is necessary, not sufficient.
