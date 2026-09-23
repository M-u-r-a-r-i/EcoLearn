---
concept_id: orbital_velocity
interest: gaming
format: explain
title: The tutorial level that asks you to miss the ground
check:
  question: |-
    Satellite P moves in a circular orbit of radius $r$ around a planet. Satellite Q moves in a circular orbit of radius $16r$ around the same planet. How does Q's orbital speed compare with P's?
  options:
    A: |-
      $4$ times P's speed
    B: |-
      One sixteenth of P's speed
    C: |-
      The same as P's speed
    D: |-
      One quarter of P's speed
  answer: D
  explanation: |-
    $v_o = \sqrt{GM/r}$, so $v_o \propto 1/\sqrt{r}$. Sixteen times the radius divides the speed by $\sqrt{16} = 4$.
  misconceptions:
    A: |-
      Assumes a bigger orbit needs a faster satellite; gravity is weaker out there, so *less* speed is needed to bend the path into a circle.
    B: |-
      Applies the inverse-square law to the speed; it is the force that goes as $1/r^2$, while the orbital speed goes as $1/\sqrt{r}$.
    C: |-
      Thinks every satellite travels at the same "orbital speed"; the required speed depends on the strength of gravity at that radius.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor runs an orbit simulator with a planet and a ship, and a tablet shows a satellite above a planet](scenes/gaming/gravitation.svg "The ship on the screen is falling towards the planet the whole time. It just keeps missing.")

The tutorial level of Kavya's new space game gives her one tool: a cannon on top of a very tall tower, aimed dead level at the horizon. The objective text is three words long. *Miss the ground.*

Her first shot, at low power, arcs down and lands a few kilometres away. She winds the power up. The next lands much further round the curve of the planet. Further still, and the shot crosses an entire continent before it comes down.

Her younger brother Vivaan is unimpressed. "You're just throwing it harder."

"I'm throwing it harder," Kavya agrees, "and the ground is curving away underneath it." She winds the power up again and watches the shot fall and fall and never arrive. The objective ticks green.

The shot is still falling — the planet is still pulling on it — and yet it never lands. How fast does it have to go for the ground to keep curving away exactly as fast as it drops?

## The physics

Newton described exactly this tutorial in 1687: a cannon on a mountain, firing level, faster and faster, until one shot falls all the way round. That shot is in **orbit**. An orbit is not an escape from gravity; it is a fall that keeps missing.

![On the left, shots fired level from a tower land further round the planet as the speed increases, until one circles it; on the right, a satellite in a circular orbit with gravity pointing to the centre and velocity along the path](figures/orbital_velocity/throw-to-orbit.svg "An orbit is a fall that never reaches the ground. In a circular orbit, gravity supplies exactly the centripetal force needed.")

Take a satellite of mass $m$ in a circular orbit of radius $r$ about a planet of mass $M$, with $r$ measured from the planet's **centre**. Gravity is the only force, and it points at the centre, so it must supply the whole **centripetal force**:

$$\frac{GMm}{r^2} = \frac{mv_o^2}{r} \quad\Rightarrow\quad v_o = \sqrt{\frac{GM}{r}}$$

This is the **orbital speed**. Note what is missing: the satellite's own mass, $m$, has cancelled. A cannonball and a space station in the same orbit move at the same speed. And a *larger* orbit needs a *smaller* speed, because gravity is weaker there.

The **period** is one lap's circumference divided by the speed:

$$T = \frac{2\pi r}{v_o} = 2\pi\sqrt{\frac{r^3}{GM}}$$

Square that and $T^2 \propto r^3$ — Kepler's third law, now derived rather than observed.

There is a condition worth stating: this is the speed for a *circular* orbit. Fire faster than $v_o$ and the path becomes an ellipse; faster still, above $\sqrt{2}\,v_o$, and it escapes altogether.

## Worked example

**Given:** a planet with $g = 9.8\,\text{m/s}^2$ at its surface and $R = 6.4 \times 10^{6}\,\text{m}$. Kavya's cannonball skims just above the surface, so $r \approx R$. Use $GM = gR^2$.
**Find:** the orbital speed and the time for one lap.

With $GM = gR^2$, the speed simplifies:

$$v_o = \sqrt{\frac{gR^2}{R}} = \sqrt{gR} = \sqrt{9.8 \times 6.4 \times 10^{6}} \approx 7.9 \times 10^{3}\,\text{m/s}$$

So about $7.9\,\text{km/s}$ — roughly $300$ times the speed of a car on a highway.

One lap is the circumference, $2\pi R$, at that speed:

$$T = \frac{2\pi \times 6.4 \times 10^{6}}{7.9 \times 10^{3}} \approx 5.1 \times 10^{3}\,\text{s} \approx 85\,\text{minutes}$$

**Sanity check:** an hour and a half to circle the whole planet is the right size — low satellites really do come round more than a dozen times a day. Push the orbit out to $4R$ and the speed halves, to about $4\,\text{km/s}$.

## Where the picture breaks

Kavya's tower is a thought experiment wearing a game's clothes. At ground level, air drag at $7.9\,\text{km/s}$ would stop and burn the cannonball within seconds, and mountains are in the way. Real satellites are lifted above almost all of the air first — and even then, the traces of atmosphere that remain slowly drag low orbits down.

The formula also assumes a perfect circle around a uniform sphere, with nothing else pulling. Many real orbits are ellipses, where the speed changes all the way round, as Kepler's second law requires. And $r$ is measured from the planet's *centre*, not from the launch tower: forgetting to add the planet's radius to the altitude is the most common mistake in this whole chapter.

## Key takeaway

A satellite in a circular orbit is in free fall, with gravity providing the centripetal force: $GMm/r^2 = mv_o^2/r$, so $v_o = \sqrt{GM/r}$ and $T = 2\pi\sqrt{r^3/GM}$. Higher orbits are slower and take longer, and the satellite's own mass makes no difference. Always measure $r$ from the centre of the planet.
