---
concept_id: kepler_laws
interest: gaming
format: explain
title: The space game that refused to draw a circle
check:
  question: |-
    In a space game, a moon orbits its planet at radius $r$ and takes $1$ in-game day to go round once. A second moon orbits the same planet at radius $9r$. If the game follows Kepler's third law, how long does the second moon take?
  options:
    A: |-
      $27$ in-game days
    B: |-
      $9$ in-game days
    C: |-
      $3$ in-game days
    D: |-
      $81$ in-game days
  answer: A
  explanation: |-
    $T^2 \propto a^3$, so $T \propto a^{3/2}$. Nine times the radius gives $9^{3/2} = 27$ times the period.
  misconceptions:
    B: |-
      Assumes the period is simply proportional to the radius, as if the moon travelled every orbit at the same speed; a wider orbit is both longer and slower.
    C: |-
      Uses $T \propto \sqrt{a}$, taking only the square root and losing the cube in Kepler's third law.
    D: |-
      Takes $T \propto a^2$, borrowing the inverse-square law of the force; the third law relates $T^2$ to $a^3$, giving the power $3/2$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor runs an orbit simulator showing a ship on an ellipse round a planet, marked with one dot per equal slice of time](scenes/gaming/gravitation.svg "The dots are dropped at equal time intervals. Notice where they bunch up and where they spread out.")

Aditya has spent three evenings in his hostel room trying to park a ship in a neat circular orbit around the game's home planet. Every attempt comes out as a squashed loop. He is convinced the game is broken.

His roommate Meher leans over. "Turn on the trail markers."

Aditya switches them on. The game drops a small dot along the ship's path once every sixtieth of a second, one dot per frame. The trail comes back as a closed loop with the planet sitting off to one side — and the dots are crowded together at the far end of the loop, but strung far apart as the ship swings past the planet.

"That's not a bug," Meher says. "That's the whole point. An astronomer worked that out four hundred years ago, from years of naked-eye measurements of Mars, with no telescope worth the name."

Aditya stares at the trail. Why is the planet off-centre, and what decides where the ship races and where it crawls?

## The physics

The astronomer was **Johannes Kepler**, working from observations made by Tycho Brahe. Three laws describe every orbit around a single dominant body, in a game engine or in the sky.

1. **Law of orbits:** an orbiting body moves in an **ellipse**, with the central body at one **focus** — not at the centre. That is why Aditya's planet sits off to one side.
2. **Law of areas:** the line from the central body to the orbiting body sweeps out **equal areas in equal times**. Close in, that line is short, so the ship must cover a long arc to sweep the same area: it moves fast. Far out, a short arc is enough.
3. **Law of periods:** the square of the period $T$ is proportional to the cube of the **semi-major axis** $a$, half the longest diameter of the ellipse:

$$T^2 \propto a^3$$

So if the game's inner moon takes $2$ in-game days at radius $1$ unit, a moon at $4$ units takes $4^{3/2} = 8$ times as long, or $16$ days.

![An ellipse with the central body at one focus; a short wide shaded sector near it and a long thin one far away have equal areas](figures/kepler_laws/equal-areas-ellipse.svg "The two shaded areas are equal, so the body takes the same time to sweep each. The arc near the focus is far longer, so it must be moving much faster there.")

**Why the law of areas holds.** Gravity on the ship always points straight at the planet. A force directed along the line to a point has no turning effect about that point, so the **torque** about the planet is zero and the ship's **angular momentum** $\vec{L} = \vec{r} \times \vec{p}$ stays constant. In a short time $\Delta t$ the line sweeps a thin triangle, and

$$\frac{\Delta A}{\Delta t} = \frac{L}{2m}$$

which is constant. Kepler's second law *is* conservation of angular momentum, drawn as geometry. At the nearest and farthest points the velocity is perpendicular to $\vec{r}$, so $L = mvr$ and

$$v_\text{near}\,r_\text{near} = v_\text{far}\,r_\text{far}$$

Equal-time dots spread out exactly where $v$ is large. Aditya's trail was measuring angular momentum without telling him.

## Worked example

**Given:** on the ship's orbit, the closest approach to the planet is $2$ units and the farthest point is $6$ units. At the farthest point the game's readout shows $5\,\text{km/s}$. At both points the velocity is perpendicular to the line to the planet.
**Find:** the speed at the closest point.

Gravity points at the planet, so $mvr$ is the same at both ends:

$$v_\text{near} = v_\text{far} \times \frac{r_\text{far}}{r_\text{near}} = 5 \times \frac{6}{2}\ \text{km/s}$$

The distance shrinks by a factor of $3$, so the speed must grow by a factor of $3$:

$$v_\text{near} = 15\,\text{km/s}$$

**Sanity check:** three times closer, three times faster — the ship should be at its quickest right where the trail dots are most spread out, and it is.

## Where the picture breaks

The trail only *shows* the law; it doesn't explain it. And a game engine is not the solar system. Most engines step motion forward in small slices of about $1/60\,\text{s}$ and treat gravity as constant within each slice, so a simulated orbit drifts slowly and can spiral if the time step is too coarse. Real orbits do not.

Kepler's laws are idealisations too. They assume one dominant central mass that stays put, which is why they work so well for the Sun and the planets. If a second moon in the game is massive enough, it tugs on the ship and the ellipse stops closing on itself. The constant in $T^2 \propto a^3$ is also shared only by bodies orbiting the **same** central body — you cannot compare a moon of the game's gas giant with a planet going round its star.

## Key takeaway

Orbits are ellipses with the central body at a focus; the line to it sweeps equal areas in equal times; and $T^2 \propto a^3$. The law of areas is conservation of angular momentum: gravity exerts no torque about the central body, so $vr$ is fixed between the nearest and farthest points, and anything falling closer must speed up.
