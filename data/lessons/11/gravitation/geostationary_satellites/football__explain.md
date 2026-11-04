---
concept_id: geostationary_satellites
interest: football
format: explain
title: Two dishes, one match and a satellite that never moves
check:
  question: |-
    Suppose the Earth kept its mass but turned on its axis twice as slowly, so one rotation took twice as long. By what factor would the radius of a geostationary orbit change?
  options:
    A: |-
      It would become about $1.6$ times larger.
    B: |-
      It would become $2$ times larger.
    C: |-
      It would become about $2.8$ times larger.
    D: |-
      It would become about $0.63$ times as large.
  answer: A
  explanation: |-
    From $r^3 = GMT^2/4\pi^2$, $r \propto T^{2/3}$. Doubling $T$ multiplies $r$ by $2^{2/3} \approx 1.59$.
  misconceptions:
    B: |-
      Assumes the orbital radius is simply proportional to the period; Kepler's third law gives $r^3 \propto T^2$, not $r \propto T$.
    C: |-
      Swaps the powers in Kepler's third law, using $r \propto T^{3/2}$ instead of $r \propto T^{2/3}$.
    D: |-
      Thinks a slower-turning Earth would need a satellite closer in; a longer period needs a larger orbit, where gravity is weaker and the satellite moves more slowly.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: the goalkeeper's long kick at the top of its arc, the Moon and a satellite overhead, and a dish on the stand roof aimed at the satellite](scenes/football/gravitation.svg "The dish on the stand roof is bolted in place. The satellite it talks to must stay in one spot in the sky.")

The cup final is on, and cousins Anjana and Gurpreet are watching it together on a video call: Anjana at home in Kochi, Gurpreet more than two thousand kilometres north in Srinagar. At half-time they both go up to their roofs to show off their dishes.

"Mine points almost straight up," Anjana says, tilting her phone at the sky.

Gurpreet turns his camera. "Mine points much lower. Towards the south, over the mountains."

"Same channel, same satellite?"

"Same satellite. And the man who fitted mine said it never has to move. Not once, in years."

"But satellites fly round the Earth," says Anjana. "How can one stay in the same spot? And why does it look so different from our two roofs?"

## The physics

A **geostationary** satellite stays above one fixed point on the Earth's surface. The Earth turns once relative to the stars in one **sidereal day**, $T \approx 23\,\text{h}\,56\,\text{min} = 8.62 \times 10^{4}\,\text{s}$. A satellite that goes round in exactly that time, in step with the turning Earth, never appears to move.

**Three conditions** must all hold:

1. The **period** is one sidereal day.
2. The satellite moves in the **same direction** as the Earth turns, west to east.
3. The orbit is **circular** and lies in the **equatorial plane**.

**Why above the equator?** Gravity always points to the Earth's centre, so every orbit lies in a plane through the centre. A point on the ground at latitude $34^\circ\,\text{N}$ is carried round a small circle whose centre is on the Earth's axis, *above* the Earth's centre. No orbit can follow that circle. A tilted orbit could pass over Srinagar once a lap, but it would swing north and south of it every day. The only ground circle whose plane contains the Earth's centre is the **equator**.

![Earth with its axis, equator and a 28 degree north circle; a geostationary orbit lies in the equatorial plane while a tilted orbit crosses it](figures/geostationary_satellites/equatorial-vs-inclined.svg "Every orbit's plane passes through Earth's centre. Only the equatorial orbit can keep pace with a point on the ground.")

**The radius.** For a circular orbit, $T = 2\pi\sqrt{r^3/GM}$, so

$$r = \left(\frac{GMT^2}{4\pi^2}\right)^{1/3}$$

For a given planet and period there is exactly **one** radius, so all geostationary satellites share one ring above the equator.

That answers the cousins' puzzle. Both dishes point at the same spot above the equator. Kochi is only about $10^\circ$ north of the equator, so from there the satellite is high in the sky. Srinagar is about $34^\circ$ north, so the same satellite appears much lower, towards the south.

![Left: Earth and a geostationary satellite drawn to scale with lines of sight from 10 and 34 degrees north. Right: a dish at 10 degrees north tilted 78 degrees up and a dish at 34 degrees north tilted 50 degrees up](figures/geostationary_satellites/dish-elevation-latitude.svg "Both dishes aim at one point above the equator. The farther north you are, the lower that point sits in your southern sky (shown for a satellite due south).")

## Worked example

**Given:** $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$; $M = 5.97 \times 10^{24}\,\text{kg}$, so $GM = 3.98 \times 10^{14}\,\text{m}^3/\text{s}^2$; $T = 8.616 \times 10^{4}\,\text{s}$; $R = 6.37 \times 10^{6}\,\text{m}$.
**Find:** (a) the orbital radius and height; (b) the orbital speed; (c) the shortest time for the TV signal to go up to the satellite and back down.

(a)
$$T^2 = (8.616 \times 10^{4})^2 = 7.42 \times 10^{9}\,\text{s}^2$$
$$r^3 = \frac{3.98 \times 10^{14} \times 7.42 \times 10^{9}}{4\pi^2} = \frac{2.95 \times 10^{24}}{39.5} = 7.48 \times 10^{22}\,\text{m}^3$$
$$r = (7.48 \times 10^{22})^{1/3} \approx 4.21 \times 10^{7}\,\text{m} \approx 42\,100\,\text{km}$$

Height: $h = r - R \approx 42\,140 - 6370 \approx 35\,800\,\text{km}$.

(b)
$$v = \frac{2\pi r}{T} = \frac{2\pi \times 4.21 \times 10^{7}}{8.616 \times 10^{4}} \approx 3.07 \times 10^{3}\,\text{m/s}$$

(c) Radio waves travel at $3.0 \times 10^{8}\,\text{m/s}$. The path is at least $2h$:
$$t = \frac{2 \times 3.58 \times 10^{7}}{3.0 \times 10^{8}} \approx 0.24\,\text{s}$$

So the picture reaches both cousins at least a quarter of a second after the stadium camera sent it.

**Sanity check:** $\sqrt{GM/r} = \sqrt{3.98 \times 10^{14}/4.21 \times 10^{7}} \approx 3.07 \times 10^{3}\,\text{m/s}$, which matches (b). And $r \approx 6.6R$, much farther out than a 90-minute orbit, as $T^2 \propto r^3$ requires.

## Where the picture breaks

"Stationary" means stationary *relative to the ground*. Seen from space, the satellite moves at about $3\,\text{km/s}$ and is accelerating towards the Earth's centre all the time. Real geostationary satellites also drift slowly under the pulls of the Moon and the Sun and the Earth's slightly flattened shape, so they fire small thrusters now and then to hold position. The dish angles in the figure assume the satellite is due south; for a satellite east or west of that, the dish also turns sideways. The football is only the setting here: the physics is the orbit.

## Key takeaway

A geostationary satellite orbits in the equatorial plane, west to east, with a period of one sidereal day, so it stays above one point on the equator. From $r^3 = GMT^2/4\pi^2$, its orbit radius is about $42\,100\,\text{km}$, some $36\,000\,\text{km}$ up, at about $3.1\,\text{km/s}$. It must be above the equator because every orbit's plane passes through the Earth's centre.
