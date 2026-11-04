---
concept_id: orbital_velocity
interest: smartphones
format: explain
title: The satellites creeping across your phone's sky plot
check:
  question: |-
    Two satellites orbit the Earth in circles. Satellite Q's orbit radius (measured from the Earth's centre) is **four times** satellite P's. How does Q's orbital speed compare with P's?
  options:
    A: |-
      Half as fast
    B: |-
      A quarter as fast
    C: |-
      The same speed
    D: |-
      Twice as fast
  answer: A
  explanation: |-
    $v = \sqrt{GM/r}$, so $v \propto 1/\sqrt{r}$. Four times the radius gives $1/\sqrt{4} = 1/2$ of the speed.
  misconceptions:
    B: |-
      Carries over the inverse-square law of the force to the speed; it is $v^2$, not $v$, that goes as $1/r$, so the speed falls as $1/\sqrt{r}$.
    C: |-
      Thinks every satellite moves at one standard orbital speed; the speed depends on the radius, because the pull needed and the pull available both change with it.
    D: |-
      Thinks a bigger orbit, like the outside lane of a track, must be run faster to keep up; the pull is weaker farther out, so a slower speed is enough to stay on the circle.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A city rooftop at night: a fixed satellite dish, moving navigation satellites, a weather balloon rising with a phone, and a phone and tablet on a table showing a sky plot and a weather image](scenes/smartphones/gravitation.svg "The navigation satellites move along their paths across the sky. The phone on the table plots where each one is.")

It's a long overnight train journey, and Rhea can't sleep. She opens a free app that shows her phone's satellite-navigation receiver at work: a round **sky plot**, with a dot for every satellite the phone can hear, placed where it sits in the sky.

She watches for a minute. Nothing moves. She checks again an hour later, near a station. Every dot has shifted. Some have slid towards the edge and vanished; new ones have appeared.

Tenzin, in the berth below, is awake too. "They're satellites, they have to move a bit. Little engines, pushing all the time, or they'd fall."

"Engines running for years?"

"Or they're just hovering up there."

Rhea looks at the slowly creeping dots. They seem almost still. But they're thousands of kilometres up. So what really holds them up, and how fast are they actually going?

## The physics

A satellite doesn't hover, and it doesn't need engines to stay up. It is **falling** all the time, but it moves sideways so fast that the ground curves away beneath it as quickly as it falls. It keeps missing the Earth.

![Left: shots fired level from a tower land farther round the Earth as speed increases, and the fastest circles it. Right: a satellite in a circular orbit with gravity pointing to the centre and velocity along the orbit](figures/orbital_velocity/throw-to-orbit.svg "An orbit is a fall that never reaches the ground. In a circular orbit, gravity alone supplies the centripetal force.")

For a **circular orbit** of radius $r$ (measured from the Earth's centre) around a planet of mass $M$, gravity supplies exactly the centripetal force:

$$\frac{GMm}{r^2} = \frac{mv^2}{r} \quad\Rightarrow\quad v = \sqrt{\frac{GM}{r}}$$

The **orbital period** is one circumference divided by the speed:

$$T = \frac{2\pi r}{v} = 2\pi\sqrt{\frac{r^3}{GM}}$$

- The satellite's mass $m$ cancels: a tiny satellite and a huge space station at the same radius move at the same speed.
- Farther out, $v$ is **smaller** and $T$ is **longer**. Squaring the period formula gives $T^2 \propto r^3$: Kepler's third law.
- Just above the surface, $r \approx R$ and $v = \sqrt{gR} \approx 7.9\,\text{km/s}$.

So Tenzin's engines aren't needed. Once a satellite has the right sideways speed, gravity does the rest, with no work done on it in a circular orbit, because the force is always at right angles to the motion.

## Worked example

**Given:** a navigation satellite in a circular orbit of radius $r = 2.5 \times 10^{7}\,\text{m}$ (illustrative; about four Earth radii); $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$ for the Earth.
**Find:** its orbital speed and period.

**Step 1 — speed squared.** $v^2 = GM/r = 4.0 \times 10^{14} / 2.5 \times 10^{7} = 1.6 \times 10^{7}\,\text{m}^2/\text{s}^2$.

**Step 2 — speed.** $v = 4.0 \times 10^{3}\,\text{m/s} = 4\,\text{km/s}$. That's about $1200\,\text{km}$, the length of a long train journey, every five minutes.

**Step 3 — one lap.** The circumference is $2\pi r \approx 1.57 \times 10^{8}\,\text{m}$.

**Step 4 — period.** $T = 1.57 \times 10^{8} / 4.0 \times 10^{3} \approx 3.9 \times 10^{4}\,\text{s}$, about $11$ hours.

So the satellite is racing along at $4\,\text{km/s}$, yet crosses the sky slowly because it is so far away and a lap takes most of half a day. That's why Rhea's dots crept.

**Sanity check:** the speed is below the $7.9\,\text{km/s}$ of a low orbit, as it should be for a satellite farther out.

## Where the picture breaks

This is not an analogy: the sky plot really shows real satellites. But how the dots move on it is not the same as the satellite's speed. The plot shows only **direction** in the sky, not distance, and the Earth is turning under the satellites while Rhea watches, so each dot's drift mixes the satellite's motion with her own. Our $11$-hour period also comes from round numbers; real navigation orbits are chosen to take roughly half a day.

The formula assumes a perfectly circular orbit around a spherical Earth, with no air drag. At navigation-satellite heights there is essentially no air, which is why they can coast for years; in low orbits a trace of air slowly drags satellites down. Small thrusters are used, but only for occasional corrections, not to hold the satellite up.

## Key takeaway

A satellite in a circular orbit is in continuous free fall, with gravity providing the centripetal force. Its speed is $v = \sqrt{GM/r}$ and its period $T = 2\pi r / v$, independent of its own mass. Higher orbits are slower and take longer.
