---
concept_id: orbital_velocity
interest: motorsport
format: explain
title: The transmitters that never stop falling
check:
  question: |-
    A satellite is in a circular orbit of radius $r = 1.6 \times 10^{7}\,\text{m}$ about the Earth, for which $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$. What is its orbital speed?
  options:
    A: |-
      $5.0\,\text{km/s}$
    B: |-
      $7.1\,\text{km/s}$
    C: |-
      $25\,000\,\text{km/s}$
    D: |-
      $3.5\,\text{km/s}$
  answer: A
  explanation: |-
    $v = \sqrt{GM/r} = \sqrt{4.0 \times 10^{14} / 1.6 \times 10^{7}} = \sqrt{2.5 \times 10^{7}} = 5.0 \times 10^{3}\,\text{m/s}$.
  misconceptions:
    B: |-
      Uses $\sqrt{2GM/r}$, the escape speed from that distance. That is $\sqrt{2}$ times too big — escaping needs twice the kinetic energy of orbiting.
    C: |-
      Stops at $v^2 = 2.5 \times 10^{7}$ and reads it as the answer. Check the units: that number is in $\text{m}^2/\text{s}^2$ and still needs its square root.
    D: |-
      Takes $v = \sqrt{GM/2r}$, borrowing the $2r$ from the kinetic-energy formula $K = GMm/2r$. The $2$ there comes from the $\tfrac{1}{2}m$ in $\tfrac{1}{2}mv^2$, not from the orbit.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A pit lane at a hill-climb event: a car on a weighbridge, a team truck with a satellite dish on its roof, a GPS aerial on the car's engine cover and a drop-test rig beside the scrutineering bay](scenes/motorsport/gravitation.svg "The little aerial on the car's engine cover is listening to transmitters thousands of kilometres away, all of them moving.")

Nivedita runs the data on a club endurance car, and her job after every session is to lay one lap's satellite trace over another's. Today they will not line up. The line through the fast left-hander wanders by a couple of metres from lap to lap.

The logger's status page explains itself: **four** satellites in view at the start of the session, **seven** by the end.

Joel, who drove the session, reads it over her shoulder. "Four to seven. They moved?"

"Of course they moved," says Nivedita. "They're doing kilometres a second up there."

Joel thinks about this for a while. "Then why hasn't a single one of them fallen down?"

Nivedita opens her mouth and finds she has no good answer. They are certainly falling — everything does. So what speed keeps a falling thing missing the ground, lap after lap?

## The physics

Newton's own picture: fire something horizontally from a very tall tower. Slow, and it lands nearby. Faster, and it lands further round the curve of the Earth. Fast enough, and the ground curves away exactly as quickly as the body falls, so it never lands at all. That is an **orbit** — permanent free fall.

![Left: faster and faster horizontal launches from a tall tower land further round the Earth until one never lands. Right: a circular orbit with gravity pointing to the centre and the velocity along the orbit](figures/orbital_velocity/throw-to-orbit.svg "An orbit is not an escape from gravity. It is a fall that keeps missing, because gravity's pull is exactly the centripetal force the circle needs.")

For a **circular** orbit of radius $r$ (measured from the Earth's **centre**), gravity is the only force, and it points at the centre — so it is the centripetal force:

$$\frac{GMm}{r^2} = \frac{mv^2}{r}$$

The satellite's mass $m$ cancels from both sides, and one power of $r$ goes with it:

$$v = \sqrt{\frac{GM}{r}}$$

A heavy satellite and a loose bolt in the same orbit travel at the same speed, side by side. And the **higher the orbit, the slower the satellite** — the opposite of the intuition that being further out means going faster to keep up.

The **period** is one circumference at that speed:

$$T = \frac{2\pi r}{v} = 2\pi\sqrt{\frac{r^3}{GM}}$$

Square it and you have $T^2 = (4\pi^2/GM)\,r^3$ — Kepler's third law, now derived rather than observed.

Two limits worth remembering. Skimming the surface ($r = R$) would need $v = \sqrt{gR} \approx 7.9\,\text{km/s}$. And the escape speed is exactly $\sqrt{2}$ times the circular speed at the same distance.

## Worked example

**Given:** a navigation-type satellite in a circular orbit of radius $r = 1.0 \times 10^{7}\,\text{m}$ (about $3600\,\text{km}$ above the surface); $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$.
**Find:** its orbital speed and its period.

**Step 1 — the speed squared.**

$$v^2 = \frac{GM}{r} = \frac{4.0 \times 10^{14}}{1.0 \times 10^{7}} = 4.0 \times 10^{7}\,\text{m}^2/\text{s}^2$$

**Step 2 — the speed.** $v = \sqrt{4.0 \times 10^{7}} \approx 6.3 \times 10^{3}\,\text{m/s} = 6.3\,\text{km/s}$ — about seventy-five times the speed of a car on a fast straight.

**Step 3 — the period.**

$$T = \frac{2\pi r}{v} = \frac{6.28 \times 10^{7}}{6.3 \times 10^{3}} \approx 1.0 \times 10^{4}\,\text{s} \approx 2.8\,\text{hours}$$

**Sanity check:** eight or nine laps of the Earth a day means a satellite crosses the sky in minutes, not hours — exactly why Nivedita's count went from four to seven during one session.

## Where the picture breaks

Motorsport is the setting, not the analogy. A car on a banked corner and a satellite in orbit do share one equation, $F = mv^2/r$ — but on the corner the centripetal force comes from tyre friction and the road's normal force, which is nothing like gravity. What the pit lane genuinely contributes here is the receiver on the car's engine cover: those transmitters really are in the orbits this formula describes, and their motion is why the satellites in view keep changing.

The idealisations: a perfectly **circular** orbit and a perfectly spherical Earth. Real orbits are ellipses, so $v$ varies round them; the Earth's equatorial bulge slowly twists orbital planes; and below about $500\,\text{km}$ the remaining air drags satellites down. The cancelling of $m$ also assumes the satellite is far lighter than the Earth, which every satellite comfortably is.

## Key takeaway

In a circular orbit, gravity *is* the centripetal force: $GMm/r^2 = mv^2/r$, giving $v = \sqrt{GM/r}$ and $T = 2\pi\sqrt{r^3/GM}$. The satellite's own mass cancels, and a higher orbit is a slower one. An orbit is not the absence of gravity — it is free fall that keeps missing the ground.
