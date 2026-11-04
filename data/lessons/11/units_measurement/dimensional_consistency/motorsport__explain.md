---
concept_id: dimensional_consistency
interest: motorsport
format: explain
title: Two stopping-distance formulas and one safety briefing
check:
  question: |-
    Here $P$ is an engine's power, $F$ a force, $m$ a mass, $u$ and $v$ velocities, $t$ a time and $s$ a displacement. Which equation is dimensionally inconsistent?
  options:
    A: |-
      $P = Fvt$
    B: |-
      $P = Fv$
    C: |-
      $Ft = mv - mu$
    D: |-
      $Fs = \tfrac{1}{2}mv^2 - \tfrac{1}{2}mu^2$
  answer: A
  explanation: |-
    $[Fvt] = [\text{M}\,\text{L}\,\text{T}^{-2}][\text{L}\,\text{T}^{-1}][\text{T}] = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$, the dimensions of energy, while power is $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$. The two sides don't match, so A must be wrong.
  misconceptions:
    B: |-
      Believes power must be written as energy divided by time, so force times speed "can't" be power. In fact $[F][v] = [\text{M}\,\text{L}\,\text{T}^{-2}][\text{L}\,\text{T}^{-1}] = [\text{M}\,\text{L}^2\,\text{T}^{-3}]$, exactly power.
    C: |-
      Judges by appearance: a force times a time looks unrelated to masses and speeds. Working it out, both sides are $[\text{M}\,\text{L}\,\text{T}^{-1}]$.
    D: |-
      Thinks the $\tfrac{1}{2}$ or the squared speeds spoil the balance. The $\tfrac{1}{2}$ is dimensionless, and every term is $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A race track with a braking marker reading 100 beside the track and a race car crossing the start-finish line](scenes/motorsport/units_measurement.svg "Braking markers tell drivers how far there is to the corner. How far a car needs to stop is a formula, and formulas can be copied wrong.")

Nikhil has been asked to give the safety talk to new members of his karting club. He digs out last year's slides, and one says:

*stopping distance = (speed × reaction time) + speed ÷ (2 × deceleration)*

But the road-safety leaflet on the clubhouse noticeboard has almost the same formula, except that the last part says *speed squared* ÷ (2 × deceleration).

"The slide was made by a senior who's studying engineering," says his friend Tara. "Just trust the slide."

The talk is in twenty minutes, there's no signal in the clubhouse, and the two can't both be right. Is there a way to find out which one is wrong, using nothing but the formulas themselves?

## The physics

You can only add, subtract or equate quantities of the **same kind**: metres to metres, never metres to seconds. This is the **principle of homogeneity of dimensions**:

> In a correct equation, every term that is added, subtracted or set equal must have the same dimensions.

An equation that obeys it is **dimensionally consistent**; one that breaks it is certainly wrong. Test each term separately.

Write stopping distance $d$, speed $v$, reaction time $t_r$ and deceleration $a$:

- $[d] = [\text{L}]$
- $[v\,t_r] = [\text{L}\,\text{T}^{-1}][\text{T}] = [\text{L}]$ — the distance covered before the brakes even come on.

**The slide's last term:**
$$\left[\frac{v}{2a}\right] = \frac{[\text{L}\,\text{T}^{-1}]}{[\text{L}\,\text{T}^{-2}]} = [\text{T}]$$
That's a *time*, added to lengths. Inconsistent — the slide is wrong.

**The leaflet's last term:**
$$\left[\frac{v^2}{2a}\right] = \frac{[\text{L}^2\,\text{T}^{-2}]}{[\text{L}\,\text{T}^{-2}]} = [\text{L}]$$
A length, matching the others. Consistent. The $2$ is a pure number and doesn't affect the check.

![Two equations checked term by term. In v squared equals u squared plus 2as, every term is L squared T to the minus 2. In s equals ut plus half at, the last term is L T to the minus 1, so the equation is inconsistent](figures/dimensional_consistency/homogeneity-check.svg "Check every term, not just the two sides. One mismatched term is enough to prove an equation wrong.")

So Nikhil uses $d = v\,t_r + \dfrac{v^2}{2a}$. (You'll derive the braking part in the next chapter; here you only check it.)

The same principle means the argument of $\sin$, $\cos$ or an exponential must be dimensionless.

## Worked example

**Check** each equation: (a) $P = Fv$, the power needed to push a car at steady speed $v$ against a drag force $F$; (b) $F = \dfrac{mv}{t^2}$.

(a) $[P] = [\text{M}\,\text{L}^2\,\text{T}^{-3}]$. $[Fv] = [\text{M}\,\text{L}\,\text{T}^{-2}][\text{L}\,\text{T}^{-1}] = [\text{M}\,\text{L}^2\,\text{T}^{-3}]$. **Consistent.**

(b) $[F] = [\text{M}\,\text{L}\,\text{T}^{-2}]$, but $\left[\dfrac{mv}{t^2}\right] = \dfrac{[\text{M}][\text{L}\,\text{T}^{-1}]}{[\text{T}^2]} = [\text{M}\,\text{L}\,\text{T}^{-3}]$. **Inconsistent**, so (b) is certainly wrong. (The correct average force would be $mv/t$.)

**Sanity check:** in SI units, (a) gives $\text{N} \times \text{m/s} = \text{J/s} = \text{W}$, the unit of power, as it should.

## Where the picture breaks

Passing the test does not prove an equation right. The formula $d = v\,t_r + v^2/a$, with no $2$, is just as consistent as the leaflet's — dimensions are blind to pure numbers. Nikhil's check proved the slide wrong, but it cannot prove the leaflet right; for the $2$ he needs the derivation. And a real stopping distance also depends on things the formula idealises away: deceleration is not perfectly constant, and it changes with tyres and road surface.

## Key takeaway

Principle of homogeneity: every term added, subtracted or equated must have the same dimensions. One mismatched term proves an equation wrong. Passing the check is necessary but not sufficient, because dimensions can't catch a wrong number like a missing $2$.
