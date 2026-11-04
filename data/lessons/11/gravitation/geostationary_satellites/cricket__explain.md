---
concept_id: geostationary_satellites
interest: cricket
format: explain
title: Why the dish on the roof never has to move
check:
  question: |-
    Why can't a geostationary satellite be placed so that it stays directly above a city at latitude $28^\circ\,\text{N}$?
  options:
    A: |-
      It can, provided it is launched to the geostationary height of about $36\,000\,\text{km}$ straight above the city.
    B: |-
      The Earth turns more slowly at $28^\circ\,\text{N}$ than at the equator, so no orbit there can have a one-day period.
    C: |-
      The orbital radius needed for a one-day period is different at each latitude, and at $28^\circ\,\text{N}$ it lies inside the Earth.
    D: |-
      Gravity points to the Earth's centre, so every orbit lies in a plane through the centre; the circle traced by a point at $28^\circ\,\text{N}$ does not.
  answer: D
  explanation: |-
    An orbit's plane must contain the Earth's centre, because that is where gravity points. To stay over one spot, the satellite would have to circle in the same plane as that spot's daily path, and the only such path through the centre is the equator.
  misconceptions:
    A: |-
      Thinks the right height is the only requirement; a satellite at that height over $28^\circ\,\text{N}$ would be on a tilted orbit and drift north and south each day.
    B: |-
      Confuses speed with angular speed; every point on the Earth turns through $360^\circ$ in the same time, whatever its latitude.
    C: |-
      Thinks the orbit radius depends on latitude; it is fixed by the period and the Earth's mass alone, $r^3 = GMT^2/4\pi^2$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: a ball skied above a fielder, the Moon and a satellite overhead, and a broadcast van's dish aimed at the sky](scenes/cricket/gravitation.svg "The broadcast dish is aimed at one spot in the sky, and it never has to follow anything.")

The final is about to start, and Siddharth's grandmother has claimed the best seat in front of the TV. Last week the installer came to fit their new dish. He spent twenty minutes tilting it, aimed it at a spot in the southern sky, tightened the bolts, and left. It hasn't moved since, and the picture has never dropped.

"So the satellite is just standing still up there?" she asks during the toss.

"It's moving, Paati. Very fast," Siddharth says. "Kilometres every second."

"Then how does the dish keep pointing at it without moving?"

Siddharth opens his mouth and closes it again. If the satellite is racing along, why does it stay over the same spot? And why is the dish aimed south rather than straight up?

## The physics

The satellite is **geostationary**: it stays above one fixed point on the Earth's surface. The Earth turns once relative to the stars in one **sidereal day**, $T \approx 23\,\text{h}\,56\,\text{min} = 8.62 \times 10^{4}\,\text{s}$ (a little shorter than 24 hours, because the Sun appears to drift against the stars). A satellite whose orbit keeps pace with that turning never seems to move.

**Three conditions** must all hold:

1. **Period** equal to one sidereal day.
2. **Direction** the same as the Earth's spin, west to east.
3. **Plane** of the orbit is the equatorial plane, and the orbit is circular.

**Why the equator?** Gravity always points to the Earth's centre, so a satellite can only orbit in a plane passing through the centre. A point at latitude $28^\circ\,\text{N}$ is carried round a small circle whose centre lies on the Earth's axis, *above* the Earth's centre. No orbit can follow that circle. An orbit tilted at $28^\circ$ would pass over the city once each lap, but it would swing north and south of it every day. The only circle a ground point traces whose plane contains the Earth's centre is the **equator**.

![Earth with its axis, equator and a 28 degree north circle; a geostationary orbit lies in the equatorial plane while a tilted orbit crosses it](figures/geostationary_satellites/equatorial-vs-inclined.svg "Every orbit's plane passes through Earth's centre. Only the equatorial orbit can keep pace with a point on the ground.")

**The orbital radius.** For a circular orbit, $T = 2\pi\sqrt{r^3/GM}$. Square it and rearrange:

$$r = \left(\frac{GMT^2}{4\pi^2}\right)^{1/3}$$

For a given planet and period, there is exactly **one** possible radius. That is why all geostationary satellites share a single ring above the equator. And it answers the second half of Siddharth's puzzle: India lies north of the equator, so the dish looks towards the southern sky to see a satellite above the equator.

## Worked example

**Given:** $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$; $T = 8.62 \times 10^{4}\,\text{s}$; $R = 6.4 \times 10^{6}\,\text{m}$.
**Find:** the orbital radius, the height above the surface and the orbital speed.

$$T^2 = (8.62 \times 10^{4})^2 = 7.43 \times 10^{9}\,\text{s}^2$$
$$r^3 = \frac{4.0 \times 10^{14} \times 7.43 \times 10^{9}}{4\pi^2} = \frac{2.97 \times 10^{24}}{39.5} = 7.52 \times 10^{22}\,\text{m}^3$$
$$r = (7.52 \times 10^{22})^{1/3} \approx 4.22 \times 10^{7}\,\text{m} \approx 42\,200\,\text{km}$$

Height: $h = r - R = 42\,200 - 6400 \approx 35\,800\,\text{km}$, about $36\,000\,\text{km}$.

Speed: $$v = \frac{2\pi r}{T} = \frac{2\pi \times 4.22 \times 10^{7}}{8.62 \times 10^{4}} \approx 3.1 \times 10^{3}\,\text{m/s} = 3.1\,\text{km/s}$$

**Sanity check:** $\sqrt{GM/r} = \sqrt{4.0 \times 10^{14}/4.22 \times 10^{7}} = \sqrt{9.48 \times 10^{6}} \approx 3.08 \times 10^{3}\,\text{m/s}$, which matches. And $r \approx 6.6R$, much farther out than a 90-minute orbit, as $T^2 \propto r^3$ requires.

## Where the picture breaks

"Stationary" means stationary *relative to the ground*. Seen from space, the satellite is moving at about $3\,\text{km/s}$ and accelerating towards the Earth's centre all the time. Real geostationary satellites also drift slowly, pulled by the Moon and the Sun and by the Earth's slightly non-spherical shape, so they fire small thrusters now and then to hold their slot. And the dish needs a clear line of sight to the southern sky, which is why a tall building in the way can block the signal. The cricket here is only the setting: the physics is the satellite's orbit itself.

## Key takeaway

A geostationary satellite orbits in the equatorial plane, west to east, with a period of one sidereal day, so it stays above one point on the equator. From $r^3 = GMT^2/4\pi^2$, its radius is about $42\,200\,\text{km}$ (about $36\,000\,\text{km}$ up), moving at about $3.1\,\text{km/s}$. It must be over the equator because every orbit's plane passes through the Earth's centre.
