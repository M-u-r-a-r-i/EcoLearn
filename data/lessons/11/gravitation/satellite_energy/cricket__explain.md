---
concept_id: satellite_energy
interest: cricket
format: explain
title: The broadcast satellite that speeds up by slowing down
check:
  question: |-
    A satellite in a circular orbit has kinetic energy $5.0 \times 10^{9}\,\text{J}$. Taking potential energy as zero at infinity, what is its total mechanical energy?
  options:
    A: |-
      $+5.0 \times 10^{9}\,\text{J}$
    B: |-
      $-5.0 \times 10^{9}\,\text{J}$
    C: |-
      $-1.0 \times 10^{10}\,\text{J}$
    D: |-
      $0\,\text{J}$
  answer: B
  explanation: |-
    In a circular orbit $K = GMm/2r$ and $U = -GMm/r = -2K$, so $E = K + U = -K = -5.0 \times 10^{9}\,\text{J}$.
  misconceptions:
    A: |-
      Counts only the kinetic energy, as if a satellite in space had no potential energy; with the zero at infinity, $U$ is negative and larger in size than $K$.
    C: |-
      Gives the potential energy $U = -2K$ instead of the total $E = K + U$.
    D: |-
      Thinks an orbiting satellite is weightless and "floating", so its energies cancel; gravity is acting fully, and the total energy is negative because the satellite is bound.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: a ball skied above a fielder, the Moon and a satellite overhead, and a broadcast van's dish aimed at the sky](scenes/cricket/gravitation.svg "The satellite carrying the match is bound to the Earth. Its energy says so.")

Rain has stopped play, and Aisha and Nikhil are scrolling on their phones while the covers stay on. Aisha finds an article about the satellite carrying the live match to their TV.

"Listen to this. When a satellite like this is old, they don't let it fall. They fire its engines to push it a few hundred kilometres *higher*, into a 'graveyard orbit', out of the way of the working ones."

"Makes sense," says Nikhil. "Engines give it energy, it goes up."

"But here's the weird part. A higher orbit is a *slower* orbit. So after the engines fire, the satellite ends up moving more slowly than before."

Nikhil puts his phone down. "Firing the engine forward makes it slower? That's backwards. Where did the energy go?"

The engines definitely added energy. So how can the satellite end up with less kinetic energy?

## The physics

Take a satellite of mass $m$ in a circular orbit of radius $r$ around a planet of mass $M$, with potential energy zero at infinity.

**Kinetic energy.** Gravity supplies the centripetal force, $GMm/r^2 = mv^2/r$, so $mv^2 = GMm/r$ and

$$K = \tfrac{1}{2}mv^2 = \frac{GMm}{2r}$$

**Potential energy.** $$U = -\frac{GMm}{r}$$

**Total energy.** $$E = K + U = \frac{GMm}{2r} - \frac{GMm}{r} = -\frac{GMm}{2r}$$

So for every circular orbit, $K = -E$ and $U = 2E$.

**Why is $E$ negative?** A body with total energy below zero cannot reach infinity, where $U = 0$ and $K$ cannot be negative. It is **bound**: it stays in orbit forever unless something adds energy. The size of $E$, $GMm/2r$, is the **binding energy**: the least energy you must supply to free the satellite completely.

![A graph of energy against orbit radius: a blue kinetic energy curve above zero, a red potential energy curve below, and a green dashed total energy curve halfway between the red curve and zero](figures/satellite_energy/energy-vs-orbit-radius.svg "At every radius, K = −E and U = 2E. Going to a bigger orbit raises E and U but lowers K.")

**Now Nikhil's puzzle.** Moving to a larger $r$ makes $E = -GMm/2r$ less negative, so the total energy rises: the engines really do add energy. But $U$ rises by *twice* that amount, and $K$ falls by the same amount $E$ rises. The engines' energy, plus some of the kinetic energy, goes into potential energy. That is why the satellite ends up slower.

## Worked example

**Given:** a broadcast satellite of mass $m = 2000\,\text{kg}$ (illustrative) in geostationary orbit, $r_1 = 4.22 \times 10^{7}\,\text{m}$; it is raised to $r_2 = 4.25 \times 10^{7}\,\text{m}$ (take $300\,\text{km}$ higher as illustrative); $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$.
**Find:** $K$, $U$ and $E$ in the first orbit, and the energy the engines must supply.

$GMm = 4.0 \times 10^{14} \times 2000 = 8.0 \times 10^{17}\,\text{J m}$.

$$K_1 = \frac{8.0 \times 10^{17}}{2 \times 4.22 \times 10^{7}} \approx 9.48 \times 10^{9}\,\text{J}, \qquad U_1 = -2K_1 \approx -1.90 \times 10^{10}\,\text{J}, \qquad E_1 = -K_1 \approx -9.48 \times 10^{9}\,\text{J}$$

$$E_2 = -\frac{8.0 \times 10^{17}}{2 \times 4.25 \times 10^{7}} \approx -9.41 \times 10^{9}\,\text{J}$$

Energy supplied: $E_2 - E_1 = \dfrac{GMm}{2}\left(\dfrac{1}{r_1} - \dfrac{1}{r_2}\right) \approx 6.7 \times 10^{7}\,\text{J}$.

So $K$ falls by about $6.7 \times 10^{7}\,\text{J}$, and $U$ rises by about $1.3 \times 10^{8}\,\text{J}$, twice as much.

**Sanity check:** $\Delta K + \Delta U = -6.7 \times 10^{7} + 1.3 \times 10^{8} \approx +6.7 \times 10^{7}\,\text{J}$, equal to the energy supplied. The new speed, $\sqrt{GM/r_2} \approx 3.07\,\text{km/s}$, is slightly lower than the old $3.08\,\text{km/s}$.

## Where the picture breaks

Our "before and after" treats both orbits as circular, but a real move between them takes two engine burns. The first puts the satellite on an elliptical transfer path; the second, at the far point, makes the new orbit circular. The energy totals above are right for the start and end, but the speed rises and falls along the way. The engines also burn propellant, so the satellite's mass changes slightly, which we have ignored. And the cricket here is only the setting: the physics is the satellite itself.

## Key takeaway

For a circular orbit, $K = GMm/2r$, $U = -GMm/r$ and $E = -GMm/2r$, so $K = -E$ and $U = 2E$. The total energy is negative because the satellite is bound to the planet. Raising the orbit adds energy, but potential energy rises twice as much as the total, so kinetic energy, and the speed, go down.
