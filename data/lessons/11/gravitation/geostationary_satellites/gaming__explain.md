---
concept_id: geostationary_satellites
interest: gaming
format: explain
title: The one orbit that keeps your base online
check:
  question: |-
    A game world's planet has $8$ times the Earth's mass, but its day is the same length as an Earth day. Compared with the Earth's geostationary orbit, what is the radius of its geostationary orbit?
  options:
    A: |-
      $8$ times larger
    B: |-
      About $2.8$ times larger
    C: |-
      $2$ times larger
    D: |-
      The same
  answer: C
  explanation: |-
    From $r^3 = GMT^2/4\pi^2$ with $T$ fixed, $r \propto M^{1/3}$. Eight times the mass gives $8^{1/3} = 2$ times the radius.
  misconceptions:
    A: |-
      Takes the radius to be proportional to the mass; the relation is a cube root, because it comes from $r^3 \propto M$.
    B: |-
      Uses a square root, $\sqrt{8} \approx 2.8$, instead of the cube root that $r^3 \propto MT^2$ requires.
    D: |-
      Treats the geostationary height of about $36\,000\,\text{km}$ as a universal number; it is a result for the Earth's mass and day, and changes with both.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor runs an orbit simulator, and a tablet shows a satellite holding station above one point on a planet with a dish aimed at it](scenes/gaming/gravitation.svg "One satellite on the tablet never moves relative to the ground below it. That is not laziness in the art; it is an orbit.")

Tanvi's colony-building game has one rule she cannot get around: a base only produces while it has a live uplink to a satellite overhead. Her first satellite is cheap and low, and it screams round the planet in an hour and a half, which means her base is online for eight minutes at a time and dark for the rest.

Her co-op partner Harshil types into the chat: *put it on the ring.*

He means the thin dashed circle the game draws far above the equator, where a single satellite sits motionless above one point of the ground, forever. Tanvi tries to save money and place her satellite at the same height, but directly over her base, which sits well north of the equator.

The game lets her. And for one in-game day the satellite swings north, then south, then north again, and her uplink drops twice a day.

Why is there only one ring — and why does it have to be over the equator?

## The physics

A **geostationary** satellite stays above one fixed point on the planet's surface. Three conditions must hold together:

1. **Period** equal to the planet's rotation period relative to the stars — for the Earth, one **sidereal day**, $23\,\text{h}\,56\,\text{min} = 8.62 \times 10^{4}\,\text{s}$, slightly shorter than the 24-hour solar day.
2. **Direction** the same as the planet's spin, west to east.
3. **Plane** the equatorial plane, with the orbit circular.

**Why the equator?** Gravity always points at the planet's **centre**, so every orbit lies in a plane through the centre. A point on the ground at a latitude of, say, $28^\circ$ north is carried round a small circle whose centre is up on the axis, not at the planet's centre. No orbit can follow that circle. Tanvi's satellite was on an orbit tilted by her base's latitude: it crossed over the base twice a day and spent the rest of the time north or south of it. The only ground track whose plane contains the centre is the **equator**.

![A planet with its spin axis, equator and a circle of latitude; a geostationary orbit lies in the equatorial plane, while a tilted orbit carries the satellite north and south](figures/geostationary_satellites/equatorial-vs-inclined.svg "Every orbit's plane passes through the centre. Only an equatorial orbit can stay above one point on the ground.")

**Why only one ring?** For a circular orbit, $T = 2\pi\sqrt{r^3/GM}$. Squaring and rearranging:

$$r = \left(\frac{GMT^2}{4\pi^2}\right)^{1/3}$$

Fix the planet and fix the period, and exactly **one** radius satisfies this. Too low and the satellite laps the ground; too high and the ground overtakes it. That single radius is the ring.

A base far from the equator still gets a link, but it must aim low: the further you are from the equator, the closer the satellite appears to the horizon.

![Lines of sight to a geostationary satellite from two latitudes, and the matching dish elevations above the southern horizon](figures/geostationary_satellites/dish-elevation-latitude.svg "From near the equator the dish points steeply upward; from higher latitudes it aims much lower, closer to the southern horizon.")

## Worked example

**Given:** $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$ for the Earth; a rotation period $T = 86\,400\,\text{s}$ (one day, taken as 24 hours); $R = 6.4 \times 10^{6}\,\text{m}$.
**Find:** the radius of the geostationary orbit, and its height above the surface.

Square the period first:

$$T^2 = (8.64 \times 10^{4})^2 = 7.46 \times 10^{9}\,\text{s}^2$$

Now the cube of the radius:

$$r^3 = \frac{GMT^2}{4\pi^2} = \frac{4.0 \times 10^{14} \times 7.46 \times 10^{9}}{39.5} \approx 7.6 \times 10^{22}\,\text{m}^3$$

Take the cube root:

$$r \approx 4.2 \times 10^{7}\,\text{m} = 42\,000\,\text{km}$$

That is the distance from the centre, so the height above the ground is

$$h = r - R = 42\,000 - 6400 \approx 36\,000\,\text{km}$$

**Sanity check:** $r$ is about $6.6$ planet-radii — a satellite six and a half Earths out, roughly a tenth of the way to the Moon. A day is about $17$ times an $85$-minute low orbit, and $17^{2/3} \approx 6.6$, exactly the factor we got.

## Where the picture breaks

"Stationary" means stationary **relative to the ground**. Seen from space the satellite is racing along at about $3\,\text{km/s}$ and accelerating towards the planet the whole time. The game's dashed ring hides that.

Real geostationary satellites also drift, pulled by the Moon, the Sun and the planet's slightly non-spherical shape, so they fire small thrusters every few weeks to hold their slot — which is why the ring is a managed, crowded piece of real estate rather than a free parking space. And the signal takes about a quarter of a second to make the round trip to $36\,000\,\text{km}$ and back, which is why a satellite link feels laggy compared with a fibre connection. Tanvi's game, sensibly, does not simulate that.

## Key takeaway

A geostationary satellite orbits in the equatorial plane, west to east, with a period of one sidereal day, so it hangs above one point of the equator. Its radius follows from $r^3 = GMT^2/4\pi^2$ — about $42\,000\,\text{km}$ from the Earth's centre, some $36\,000\,\text{km}$ up. There is exactly one such orbit, and it must be over the equator because every orbit's plane passes through the planet's centre.
