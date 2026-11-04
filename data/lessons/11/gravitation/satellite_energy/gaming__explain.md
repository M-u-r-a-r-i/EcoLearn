---
concept_id: satellite_energy
interest: gaming
format: explain
title: Burn the engine forward and watch the speed drop
check:
  question: |-
    A satellite is moved from a circular orbit of radius $r$ to a circular orbit of radius $2r$ around the same planet. What happens to its kinetic energy?
  options:
    A: |-
      It halves.
    B: |-
      It doubles.
    C: |-
      It is unchanged.
    D: |-
      It falls to a quarter.
  answer: A
  explanation: |-
    For a circular orbit $K = GMm/2r$, so $K \propto 1/r$. Doubling the radius halves the kinetic energy, even though the engines added energy to the satellite.
  misconceptions:
    B: |-
      Assumes that because the engines added energy, the kinetic energy must have gone up; the total energy does rise, but the potential energy rises by twice as much, so $K$ falls.
    C: |-
      Thinks orbital speed is the same at every radius; the circular-orbit speed is $\sqrt{GM/r}$, which is smaller further out.
    D: |-
      Applies the inverse-square law of the force to the energy; $K = GMm/2r$ depends on $1/r$, not $1/r^2$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor runs an orbit simulator with a ship circling a planet, and a tablet shows a satellite holding station above a planet](scenes/gaming/gravitation.svg "The ship's engine is about to fire forwards. Watch what the speed readout does.")

Rehan is streaming an orbit simulator to about forty viewers, and he has promised a simple manoeuvre: raise his ship from a low circular orbit to a higher one. He points the nose along the direction of travel, fires the engine, coasts to the top of the new path, fires again to round it off, and settles into the higher orbit.

Then he reads the speed off the HUD and stops talking.

It is **lower** than before. Noticeably lower.

The chat does not hold back. *engine was pointed backwards.* *bug.* *he burned retrograde lol.*

"I burned forwards," Rehan says. "Twice. Both burns added energy — I watched the fuel go down."

He is right about the fuel and right about the direction, and his ship is still slower than it was. The engines put energy in. So where did it go, and why did the speed come out lower?

## The physics

Take a satellite of mass $m$ in a circular orbit of radius $r$ around a planet of mass $M$, with potential energy measured as zero at infinity.

**Kinetic energy.** Gravity supplies the centripetal force, $GMm/r^2 = mv^2/r$, so $mv^2 = GMm/r$ and

$$K = \tfrac{1}{2}mv^2 = \frac{GMm}{2r}$$

**Potential energy.**

$$U = -\frac{GMm}{r}$$

**Total energy.**

$$E = K + U = \frac{GMm}{2r} - \frac{GMm}{r} = -\frac{GMm}{2r}$$

So in any circular orbit, $K = -E$ and $U = 2E$. The potential energy is always twice the total, and the kinetic energy is always exactly its opposite.

**Why is $E$ negative?** A body whose total energy is below zero can never reach infinity, where $U = 0$ and $K$ cannot be negative. It is **bound**. The size of $E$, namely $GMm/2r$, is the **binding energy**: the least energy you would have to supply to set the satellite free.

![A graph of energy against orbit radius: a kinetic energy curve above zero, a potential energy curve below, and a total energy curve halfway between the potential curve and zero](figures/satellite_energy/energy-vs-orbit-radius.svg "At every radius, K = −E and U = 2E. Moving out raises both E and U, but lowers K.")

**Now Rehan's problem.** Going to a larger $r$ makes $E = -GMm/2r$ **less negative**, so the total energy really did rise — the engines did their job. But $U$ rises by *twice* that amount, and the difference has to come from somewhere. It comes from $K$, which falls by exactly the amount $E$ rose. The engines' energy, plus a slice of the ship's kinetic energy, is all deposited as potential energy. Higher orbit, slower ship.

## Worked example

**Given:** a ship of mass $m = 1000\,\text{kg}$ moves from a circular orbit of radius $r_1 = 1.0 \times 10^{7}\,\text{m}$ to one of radius $r_2 = 2.0 \times 10^{7}\,\text{m}$; $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$, so $GMm = 4.0 \times 10^{17}\,\text{J m}$.
**Find:** the kinetic energy in each orbit and the energy the engines had to supply.

**In the first orbit:**

$$K_1 = \frac{GMm}{2r_1} = \frac{4.0 \times 10^{17}}{2.0 \times 10^{7}} = 2.0 \times 10^{10}\,\text{J}$$

and since $E = -K$ for a circular orbit, $E_1 = -2.0 \times 10^{10}\,\text{J}$.

**In the second orbit,** the radius has doubled, so both halve:

$$K_2 = 1.0 \times 10^{10}\,\text{J}, \qquad E_2 = -1.0 \times 10^{10}\,\text{J}$$

**The engines' bill** is the rise in total energy:

$$E_2 - E_1 = -1.0 \times 10^{10} - (-2.0 \times 10^{10}) = +1.0 \times 10^{10}\,\text{J}$$

So the ship gained $1.0 \times 10^{10}\,\text{J}$ overall and *lost* the same amount of kinetic energy, while its potential energy rose by twice that, $2.0 \times 10^{10}\,\text{J}$.

**Sanity check:** the orbital speed drops from $\sqrt{GM/r_1} \approx 6.3\,\text{km/s}$ to $\sqrt{GM/r_2} \approx 4.5\,\text{km/s}$ — a factor of $\sqrt{2}$, which halves the kinetic energy, exactly as the energies say. Chat was wrong; Rehan was right.

## Where the picture breaks

The two-line story treats the move as "circle, then circle", but the journey between them is an ellipse, and along it the speed rises right after the first burn and falls again before the second. The totals above are correct for the start and the end, not for every moment in between.

The engine also burns propellant, so the ship's mass drops during the manoeuvre — we held $m$ fixed. And the formulas $K = GMm/2r$, $U = -GMm/r$, $E = -GMm/2r$ hold only for **circular** orbits: on an ellipse, $K$ and $U$ change all the way round, and only their sum stays constant. If Rehan's engine had fired *backwards*, his total energy would have dropped, his orbit would have sunk, and his speed would have gone **up** — the same strange arithmetic in reverse.

## Key takeaway

For a circular orbit, $K = GMm/2r$, $U = -GMm/r$ and $E = -GMm/2r$, so $K = -E$ and $U = 2E$. The total is negative because the satellite is bound to the planet. Raising an orbit adds energy, but potential energy climbs by twice as much as the total, so kinetic energy — and speed — go down.
