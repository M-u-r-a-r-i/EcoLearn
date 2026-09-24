---
concept_id: geostationary_satellites
interest: motorsport
format: explain
title: Why the uplink dish points lower up north
check:
  question: |-
    A satellite is put into a circular orbit of radius $4.2 \times 10^{7}\,\text{m}$, travelling west to east with a period of exactly one sidereal day — but the orbit is **inclined at $19^\circ$** to the equator, so that it passes over a city at latitude $19^\circ\,\text{N}$. What does an observer in that city see?
  options:
    A: |-
      The satellite fixed in the sky above the city, exactly as intended.
    B: |-
      The satellite drifting steadily westwards right around the sky, once a day.
    C: |-
      The satellite fixed in the sky, but at the wrong elevation, so the dish needs re-aiming once.
    D: |-
      The satellite back in the same place each day, but swinging north and south of it in between.
  answer: D
  explanation: |-
    The period is right, so the satellite returns to the same longitude daily — it is geo*synchronous*. But a tilted orbit spends half of each day north of the equator and half south, so it traces a slow loop in the sky instead of standing still.
  misconceptions:
    A: |-
      Assumes the right height and the right period are enough. The orbit's **plane** matters too: every orbital plane contains the Earth's centre, and no such plane follows a point at $19^\circ\,\text{N}$.
    B: |-
      Confuses a wrong period with a wrong plane. A steady drift around the sky is what a period *different* from a sidereal day produces; here the period is exactly right.
    C: |-
      Pictures the tilt as simply shifting where the satellite sits. A tilted orbit is not stationary at all — the satellite's latitude changes continuously through the day.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A pit lane at a hill-climb event: a car on a weighbridge, a team truck with a satellite dish on its roof, a GPS aerial on the car's engine cover and a drop-test rig beside the scrutineering bay](scenes/motorsport/gravitation.svg "The dish on the truck roof is aimed once at the start of the weekend and never touched again.")

Trisha's job on race weekends is the truck: park it, level it, raise the dish, get the team's data link up before the cars run.

At the southern event last month the dish sat steep, pointing almost overhead. This weekend the circuit is a thousand kilometres north, and she has left the rookie, Hemant, to set it up while she deals with the timing loop.

She comes back to find him furious with the equipment. He has matched last month's angles exactly — same elevation, same heading, marked on the mount with tape — and the link is dead.

"The satellite must have moved," he says.

"That satellite," says Trisha, "has not moved in eleven years. That's the entire point of it."

The dish never moves during a weekend, so the satellite really does hang still. Yet the angle it hangs at changed when the truck drove north. Why should both be true at once?

## The physics

A **geostationary** satellite stays above one fixed point on the Earth's surface. Three conditions must all hold:

1. **Period** equal to one **sidereal day** — one turn of the Earth relative to the stars, $T \approx 23\,\text{h}\,56\,\text{min} = 8.62 \times 10^{4}\,\text{s}$, slightly shorter than the 24-hour solar day.
2. **Direction** the same as the Earth's spin: west to east.
3. **Plane** the equatorial plane, and the orbit circular.

Get the first two right and the third wrong and you have a **geosynchronous** satellite: it comes back to the same longitude each day, but wanders north and south in between. Only an equatorial orbit stands still.

**Why the equator?** Gravity always points at the Earth's **centre**, so every orbit lies in a plane through the centre. A point at latitude $19^\circ\,\text{N}$ is carried round a small circle whose centre sits on the Earth's axis, well above the Earth's centre — no orbital plane can follow it. The equator is the only ground track whose plane passes through the centre.

![Earth with its axis, equator and a circle of latitude; a geostationary orbit lying in the equatorial plane beside a tilted orbit crossing it](figures/geostationary_satellites/equatorial-vs-inclined.svg "Every orbital plane cuts through the Earth's centre. Only the equatorial one can keep pace with a point on the ground.")

**The radius.** From the circular-orbit result $T = 2\pi\sqrt{r^3/GM}$, squaring and rearranging gives

$$r = \left(\frac{GMT^2}{4\pi^2}\right)^{1/3}$$

For a given planet and a given period there is exactly **one** possible radius — which is why every geostationary satellite shares a single crowded ring above the equator.

**And Hemant's angles.** The satellite sits above the equator, so from anywhere in India you look south to see it. The further north you stand, the lower it sits above the southern horizon.

![Left: the Earth and a geostationary satellite drawn to scale with lines of sight from two different latitudes. Right: the resulting dish elevations, steep at the lower latitude and shallow at the higher one](figures/geostationary_satellites/dish-elevation-latitude.svg "Both dishes point at the same satellite. Standing further north drops its elevation above the southern horizon.")

## Worked example

**Given:** $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$, $T = 8.62 \times 10^{4}\,\text{s}$, Earth's radius $R = 6.4 \times 10^{6}\,\text{m}$.
**Find:** the geostationary orbit radius and height.

**Step 1 — square the period.** $T^2 = (8.62 \times 10^{4})^2 = 7.43 \times 10^{9}\,\text{s}^2$.

**Step 2 — the cube of the radius.**

$$r^3 = \frac{4.0 \times 10^{14} \times 7.43 \times 10^{9}}{4\pi^2} = \frac{2.97 \times 10^{24}}{39.5} = 7.52 \times 10^{22}\,\text{m}^3$$

**Step 3 — the cube root.** $r = 4.22 \times 10^{7}\,\text{m}$, about $42\,000\,\text{km}$ — so the height above the ground is $r - R \approx 3.6 \times 10^{7}\,\text{m}$, about $36\,000\,\text{km}$.

**Sanity check:** $r$ is about $6.6$ Earth radii, far further out than a 90-minute low orbit — which is what $T^2 \propto r^3$ demands when the period goes from an hour and a half to a day.

## Where the picture breaks

Motorsport is the setting, not the analogy. A truck with a dish on its roof is a genuine reason to care where a satellite sits, but nothing about racing explains an orbit.

"Stationary" also means stationary *relative to the ground*. Seen from space the satellite is travelling at about $3\,\text{km/s}$ and accelerating towards the Earth's centre the whole time. Real geostationary satellites drift, too — tugged by the Moon, the Sun and the Earth's slightly out-of-round shape — so they fire small thrusters every few weeks to hold their slot, and when the fuel runs out they are retired. Finally, the low elevation angle at high latitudes is a practical problem: a hill, a grandstand or a tall tree in the southern view is enough to kill the link, which is a real part of Trisha's job.

## Key takeaway

A geostationary satellite orbits in the equatorial plane, west to east, with a period of one sidereal day, so it hangs over one point on the equator. Its radius follows from $r^3 = GMT^2/4\pi^2$: about $42\,000\,\text{km}$ from the centre, some $36\,000\,\text{km}$ up. It must be over the equator because every orbital plane passes through the Earth's centre.
