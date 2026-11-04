---
concept_id: gravitational_potential_energy
interest: gaming
format: explain
title: The energy bar that lied above the atmosphere
check:
  question: |-
    A probe of mass $2000\,\text{kg}$ is lifted from a planet's surface to a height equal to the planet's radius $R$. Taking $g = 9.8\,\text{m/s}^2$ at the surface and $R = 6.4 \times 10^{6}\,\text{m}$, by how much does its gravitational potential energy increase?
  options:
    A: |-
      $1.3 \times 10^{11}\,\text{J}$
    B: |-
      $-6.3 \times 10^{10}\,\text{J}$
    C: |-
      $0\,\text{J}$
    D: |-
      $6.3 \times 10^{10}\,\text{J}$
  answer: D
  explanation: |-
    $\Delta U = GMm\left(\dfrac{1}{R} - \dfrac{1}{2R}\right) = \dfrac{GMm}{2R} = \dfrac{mgR}{2} = \dfrac{2000 \times 9.8 \times 6.4 \times 10^{6}}{2} \approx 6.3 \times 10^{10}\,\text{J}$.
  misconceptions:
    A: |-
      Uses $mgh$ with $h = R$; that formula assumes $g$ is constant, and at this height it overestimates the gain by a factor of two.
    B: |-
      Gives the value of $U$ at the new position, $-GMm/2R$, instead of the change in $U$ between the two positions.
    C: |-
      Thinks gravity stops acting once you are above the atmosphere, so no energy is needed; gravity has no edge, and at this height it is still a quarter of its surface strength.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor runs an orbit simulator with a planet and a ship, and a tablet shows a satellite above a planet](scenes/gaming/gravitation.svg "The ship climbing away from the planet is storing energy. How much, exactly?")

Sneha tests builds for a space-flight game, and her job is to find the moment where the numbers stop making sense. Today it's the energy meter on the launch HUD, which fills as the rocket climbs.

Low flights are fine. At $6\,\text{km}$ the meter agrees with everything else in the game. So she does what testers do, and pushes the level far past what anyone intended: she flies straight up until the planet is a marble below her, a full planet-radius above the surface.

The meter reads twice what the flight computer's own fuel budget says it should.

She files the bug and pastes the offending line of code into the ticket. It says `energy = mass * 9.8 * height`.

"That's the standard formula," the programmer replies. "And why does the design doc say potential energy should be **negative** out there? Energy can't be less than nothing."

Two questions, then. Where does $mgh$ stop being true, and how can an energy be negative?

## The physics

The formula $mgh$ assumes $g$ has the same value all the way up. That is fine for a jump, and wrong for a rocket, because gravity weakens with distance.

**Gravitational potential energy** of a mass $m$ at a distance $r$ from the centre of a body of mass $M$ (with $r$ at or beyond its surface) is

$$U = -\frac{GMm}{r}$$

with the **zero chosen at infinity**, where the two bodies no longer interact. $U$ is the work an outside agent does bringing $m$ slowly in from infinity to $r$. Gravity pulls inward the whole way, so the agent must hold the mass back and its work is negative:

$$U(r) = \int_{\infty}^{r} \frac{GMm}{x^2}\,dx = -\frac{GMm}{r}$$

**Negative doesn't mean "less than nothing".** It means the mass is in a hole: you would have to *supply* energy to lift it out to infinity. The deeper in, the more negative $U$ is, and the more you owe.

The **gravitational potential** is the potential energy per unit mass at that point, $V = U/m = -GM/r$, measured in $\text{J/kg}$.

**Where $mgh$ comes from.** Lift a mass from the surface $r = R$ to a height $h$:

$$\Delta U = GMm\left(\frac{1}{R} - \frac{1}{R + h}\right) = \frac{GMm\,h}{R(R + h)}$$

If $h \ll R$, then $R + h \approx R$, and since $GM/R^2 = g$ this becomes $\Delta U \approx mgh$. So $mgh$ is not a different rule; it is this rule with the distance change ignored. Below a few kilometres the error is under a tenth of a percent. Sneha's flight was not below a few kilometres.

![A graph of U against r over R: a curve rising from minus one towards zero, with a straight dashed line that leaves the surface along the curve and then climbs too fast](figures/gravitational_potential_energy/u-vs-r-and-mgh.svg "Near the surface the mgh line and the true curve agree. Further out the straight line climbs too fast — at h = R it gives twice the true rise.")

## Worked example

**Given:** a probe of mass $m = 1000\,\text{kg}$; $g = 9.8\,\text{m/s}^2$ at the surface; $R = 6.4 \times 10^{6}\,\text{m}$. Use $GM = gR^2$.
**Find:** (a) the probe's potential energy sitting on the surface; (b) the true rise in $U$ for Sneha's flight to $h = R$, compared with what the buggy line of code reports.

(a) At $r = R$:

$$U = -\frac{GMm}{R} = -mgR = -1000 \times 9.8 \times 6.4 \times 10^{6} \approx -6.3 \times 10^{10}\,\text{J}$$

That is the energy you would have to pay to remove the probe from the planet altogether.

(b) At $h = R$ the probe is at $r = 2R$, so $U$ has risen from $-mgR$ to $-mgR/2$ — it has climbed **halfway out of the hole**:

$$\Delta U = \frac{mgR}{2} \approx 3.1 \times 10^{10}\,\text{J}$$

The code computes $mgh$ with $h = R$, which is $mgR \approx 6.3 \times 10^{10}\,\text{J}$ — exactly twice too much.

**Sanity check:** gravity gets weaker on the way up, so the real climb must cost *less* than a constant-$g$ estimate, and it does.

## Where the picture breaks

The $-GMm/r$ formula assumes a uniform spherical planet and a point outside it; inside the planet a different expression applies. The zero at infinity is a **convention**, not a discovery: only *changes* in $U$ can be measured. That is why $mgh$ (zero at the ground) and $-GMm/r$ (zero at infinity) are both usable — but never in the same calculation.

The game's bug is also a fair engineering choice for most levels. Almost every game never leaves the ground, and $mgh$ is faster to compute and accurate there. It only becomes a lie when the designer lets the player fly a planet-radius up.

## Key takeaway

Gravitational potential energy is $U = -GMm/r$, zero at infinity and negative everywhere closer, because energy must be supplied to pull the bodies apart. Near the surface the *change* in $U$ is approximately $mgh$; far from it, $mgh$ overestimates, and at a height equal to the planet's radius it gives twice the true value.
