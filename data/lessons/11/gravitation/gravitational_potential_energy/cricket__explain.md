---
concept_id: gravitational_potential_energy
interest: cricket
format: explain
title: The skier with negative energy
check:
  question: |-
    Taking potential energy to be zero at infinity, what is the gravitational potential energy of a $0.16\,\text{kg}$ cricket ball resting on the Earth's surface? Use $g = 9.8\,\text{m/s}^2$ and $R = 6.4 \times 10^{6}\,\text{m}$.
  options:
    A: |-
      $0\,\text{J}$
    B: |-
      $-1.0 \times 10^{7}\,\text{J}$
    C: |-
      $+1.0 \times 10^{7}\,\text{J}$
    D: |-
      $-1.6\,\text{J}$
  answer: B
  explanation: |-
    $U = -GMm/R$, and $GM = gR^2$, so $U = -mgR = -0.16 \times 9.8 \times 6.4 \times 10^{6} \approx -1.0 \times 10^{7}\,\text{J}$. It is negative because work would have to be done on the ball to take it to infinity, where $U = 0$.
  misconceptions:
    A: |-
      Keeps the ground as the zero of potential energy, as in $mgh$; with the zero at infinity, the surface value is large and negative.
    C: |-
      Drops the minus sign, thinking potential energy must always be positive; gravity is attractive, so $U$ is below its zero at infinity.
    D: |-
      Computes $GMm/R^2$, which is the force (the ball's weight in newtons), not the energy $GMm/R$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: a ball skied above a fielder, the Moon and a satellite overhead, and a broadcast van's dish aimed at the sky](scenes/cricket/gravitation.svg "The skier climbs, stops and falls. The energy bookkeeping looks simple, until you go far enough up.")

The batter gets a top edge and the ball goes straight up, a towering skier. Farhan, keeping wicket, throws off his helmet and waits under it. It seems to hang at the top forever before dropping cleanly into his gloves.

In the dugout, Nisha has worked it out already. "About thirty metres up. So it gained $mgh$, roughly $47$ joules of potential energy, and then gave it all back as kinetic energy."

Her friend Tanmay is reading ahead in the textbook, and he frowns. "Then why does this chapter say gravitational potential energy is **negative**? And that $mgh$ is only an approximation?"

Nisha shrugs. "It works for the skier."

"Sure. But what if the ball went up six thousand kilometres? Would $mgh$ still work then?"

How can energy be negative, and when does $mgh$ stop being true?

## The physics

The formula $mgh$ assumes $g$ is constant. That's fine for a skier, but gravity weakens with distance, so far from the surface we need something better.

**Gravitational potential energy** of a mass $m$ at distance $r$ from the centre of a body of mass $M$ ($r$ at or beyond its surface) is

$$U = -\frac{GMm}{r}$$

with the **zero chosen at infinity**, where the two bodies no longer interact. It equals the work an external agent does to bring $m$ slowly from infinity to $r$. Gravity pulls $m$ inward the whole way, so the agent has to hold it back; its work is negative:

$$U(r) = \int_{\infty}^{r} \frac{GMm}{x^2}\,dx = -\frac{GMm}{r}$$

So $U$ is negative everywhere at a finite distance, and it increases (towards zero) as $r$ grows. **Negative** doesn't mean "less than nothing". It means you would have to *supply* energy to pull the ball free of the Earth.

The **gravitational potential** at a point is the potential energy per unit mass there: $V = U/m = -GM/r$, in $\text{J/kg}$.

**Where $mgh$ comes from.** Lift the ball from the surface ($r = R$) to height $h$:

$$\Delta U = GMm\left(\frac{1}{R} - \frac{1}{R + h}\right) = \frac{GMm\,h}{R(R + h)}$$

For $h \ll R$, $R + h \approx R$, and since $GM/R^2 = g$, this becomes $\Delta U \approx mgh$. So $mgh$ measures the *change* in potential energy near the surface. It is not wrong, just an approximation.

![A graph of U against r over R: a red curve rising from minus one towards zero, and a grey dashed straight line leaving the surface along the curve then climbing too fast](figures/gravitational_potential_energy/u-vs-r-and-mgh.svg "Near the surface the mgh line and the true curve agree. Far out, the line climbs too fast: at h = R, mgh gives twice the true rise.")

## Worked example

**Given:** ball $m = 0.16\,\text{kg}$; $g = 9.8\,\text{m/s}^2$; $R = 6.4 \times 10^{6}\,\text{m}$; use $GM = gR^2$.
**Find:** (a) $U$ at the surface; (b) the rise in $U$ for the $30\,\text{m}$ skier; (c) the rise in $U$ for Tanmay's height $h = R$, exactly and by $mgh$.

(a) $$U = -\frac{GMm}{R} = -mgR = -0.16 \times 9.8 \times 6.4 \times 10^{6} \approx -1.0 \times 10^{7}\,\text{J}$$

(b) Here $h/R \approx 5 \times 10^{-6}$, so $mgh$ is essentially exact: $\Delta U = 0.16 \times 9.8 \times 30 \approx 47\,\text{J}$.

(c) Exact, with $h = R$:
$$\Delta U = \frac{GMm\,R}{R \cdot 2R} = \frac{mgR}{2} \approx 5.0 \times 10^{6}\,\text{J}$$
The $mgh$ formula gives $mgR \approx 1.0 \times 10^{7}\,\text{J}$, twice the true value.

**Sanity check:** units of $mgR$ are $\text{kg} \times \text{m/s}^2 \times \text{m} = \text{J}$. For (c), the answer should be less than $mgh$, because $g$ weakens on the way up, and it is.

## Where the picture breaks

No bat can send a ball six thousand kilometres up; air drag would stop it within a hundred metres. Tanmay's thought experiment is only there to show where $mgh$ fails. The $-GMm/r$ formula also assumes the Earth is a uniform sphere and that you are at or outside its surface. And choosing the zero at infinity is a convention: only *changes* in $U$ are physically measurable. That is why both $mgh$ (zero at the ground) and $-GMm/r$ (zero at infinity) can be used, as long as you don't mix them in one calculation.

## Key takeaway

Gravitational potential energy is $U = -GMm/r$, zero at infinity and negative everywhere else, because energy must be supplied to separate the bodies. Close to the surface, the change in $U$ is approximately $mgh$; far from the surface, $mgh$ overestimates it, giving twice the true rise at $h = R$.
