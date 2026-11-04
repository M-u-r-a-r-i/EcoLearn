---
concept_id: geostationary_satellites
interest: smartphones
format: explain
title: The one satellite your dish never has to chase
check:
  question: |-
    A company wants a satellite that stays permanently above Delhi, at about $28^\circ$ north, so that phones there can point at one fixed spot in the sky. Is this possible for a satellite simply orbiting under gravity?
  options:
    A: |-
      Yes, if it is placed about $36\,000\,\text{km}$ directly above Delhi, since that height gives a $24$-hour orbit
    B: |-
      Yes, if it is placed in a lower orbit, where it moves faster and can keep up with Delhi
    C: |-
      No, because the Earth's gravity is too weak above northern latitudes to hold a satellite in orbit
    D: |-
      No, because every orbit's plane passes through the Earth's centre, so it would swing south of the equator each day
  answer: D
  explanation: |-
    Gravity points to the Earth's centre, so every orbit lies in a plane through the centre. An orbit that passes over $28^\circ$ N must also dip to $28^\circ$ S, so only a satellite over the equator can stay fixed above one spot.
  misconceptions:
    A: |-
      Thinks the right height alone makes a satellite geostationary; a $24$-hour orbit tilted to the equator still swings north and south every day.
    B: |-
      Thinks a satellite can stay over a place by going faster; a faster, lower orbit takes less than a day, so it laps the ground instead of staying above it.
    C: |-
      Thinks the Earth's pull depends on the latitude below the satellite; at a given distance from the centre the pull is the same in every direction.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A city rooftop at night: a fixed satellite dish, moving navigation satellites, a weather balloon rising with a phone, and a phone and tablet on a table showing a sky plot and a weather image](scenes/smartphones/gravitation.svg "On the right, the dish is bolted in place and aimed at a satellite that 'stays put', while the other satellites move across the sky.")

The technician tightens the last bolt on the satellite TV dish on Parth's grandparents' roof, checks the signal meter and packs up. "Don't touch it now. It's set for years."

Parth frowns. That morning, on his phone's satellite-navigation sky plot, he watched the dots drift steadily across the sky. The satellites were moving. And the weather app on his tablet shows a fresh cloud picture of the whole of India every half hour, always from the same view, as if its camera never moved.

"How can a satellite stay still?" he asks. "Everything up there is falling round the Earth. My phone's satellites never stop moving."

"This one's special," the technician says from the ladder. "It's parked."

Parth doesn't believe in parking in space. There must be a trick. Where would a satellite have to be for the Earth to seem to hold it still?

## The physics

A **geostationary satellite** stays above one point on the equator. From the ground, it seems fixed in the sky, so a dish can be bolted in place. It needs three things.

1. **Period equal to one rotation of the Earth**, about $24$ hours, so it keeps pace with the ground below.
2. **The same direction as the Earth's spin**, west to east.
3. **A circular orbit in the equatorial plane**, directly above the equator.

**Why the equator.** Gravity pulls towards the Earth's centre, so every orbit lies in a plane through the centre. A $24$-hour orbit tilted to the equator swings north and south of it each day. Only in the equatorial plane can a satellite stay above one spot.

![Earth with its axis, equator and a 28 degree north circle; a geostationary orbit lies in the equatorial plane while a tilted orbit crosses it](figures/geostationary_satellites/equatorial-vs-inclined.svg "Every orbit's plane passes through Earth's centre. Only the equatorial orbit can keep pace with a point on the ground.")

**The radius.** From the orbital speed, $T = 2\pi\sqrt{r^3/GM}$, so

$$r = \left(\frac{GM\,T^2}{4\pi^2}\right)^{1/3}$$

With $T$ fixed at one day, there is exactly **one** radius that works.

## Worked example

**Given:** $T = 24\,\text{h} = 8.64 \times 10^{4}\,\text{s}$; $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$; Earth's radius $R = 6.4 \times 10^{6}\,\text{m}$.
**Find:** the orbital radius and the height above the ground.

**Step 1 — the period squared.** $T^2 = (8.64 \times 10^{4})^2 \approx 7.46 \times 10^{9}\,\text{s}^2$.

**Step 2 — the radius cubed.** $r^3 = \dfrac{4.0 \times 10^{14} \times 7.46 \times 10^{9}}{4\pi^2} \approx 7.56 \times 10^{22}\,\text{m}^3$.

**Step 3 — the radius.** $r \approx 4.23 \times 10^{7}\,\text{m}$, about $42\,000\,\text{km}$ from the centre, or $6.6$ Earth radii.

**Step 4 — the height.** $h = r - R \approx 3.6 \times 10^{7}\,\text{m} = 36\,000\,\text{km}$. That is almost the distance once round the Earth at the equator.

**Sanity check:** navigation satellites, a few Earth radii out, take about half a day; a slower one-day orbit must lie farther out, and it does.

![Lines of sight to a geostationary satellite from two latitudes, and the matching dish elevations above the southern horizon](figures/geostationary_satellites/dish-elevation-latitude.svg "Dishes tuned to one satellite all aim at the same point above the equator. The farther north you are, the lower that point sits in the southern sky.")

That's why dishes across India tilt towards the southern sky: they all point at satellites parked above the equator.

## Where the picture breaks

Parth's phone and tablet are real windows onto this: the weather view does come from satellites above the equator, and most sky-plot dots are the moving, non-geostationary kind. (Some navigation systems do add a few satellites at this height, so a phone may show a dot or two that hardly moves at all.)

"Parked" is also the wrong word. The satellite moves at about $3\,\text{km/s}$; it only *looks* still because the ground turns with it. Strictly, the Earth turns once relative to the stars in $23$ hours $56$ minutes, which gives $r \approx 4.22 \times 10^{7}\,\text{m}$; using $24$ hours changes the answer by well under one per cent. The Moon's and Sun's pulls and the Earth's slight bulge nudge these satellites off station, so they carry small thrusters to correct their position.

## Key takeaway

A geostationary satellite orbits above the equator, west to east, once per rotation of the Earth, so it stays over one spot. From $r^3 = GMT^2/4\pi^2$ its orbital radius is about $4.2 \times 10^{7}\,\text{m}$, some $36\,000\,\text{km}$ up. It must be over the equator because every orbit's plane passes through the Earth's centre.
