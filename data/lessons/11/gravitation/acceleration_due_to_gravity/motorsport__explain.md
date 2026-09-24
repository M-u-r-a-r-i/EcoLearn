---
concept_id: acceleration_due_to_gravity
interest: motorsport
format: explain
title: The car is lighter at the top of the hill
check:
  question: |-
    Take the Earth's radius as $6400\,\text{km}$. At what height above the surface does $g$ fall to one quarter of its surface value?
  options:
    A: |-
      $6400\,\text{km}$
    B: |-
      $12\,800\,\text{km}$
    C: |-
      $3200\,\text{km}$
    D: |-
      $2400\,\text{km}$
  answer: A
  explanation: |-
    $g = GM/r^2$ measured from the *centre*, so a quarter of $g$ needs $r = 2R$. That is a height of $h = r - R = R = 6400\,\text{km}$.
  misconceptions:
    B: |-
      Gets $r = 2R$ right but then reads it as a *height* of $2R$. The doubling is in the distance from the centre, and the surface is already one radius out.
    C: |-
      Borrows the depth rule, where $g$ falls in proportion to the distance from the centre. Below the surface $g$ is linear in $r$; above it, it is an inverse square, and the two cannot be swapped.
    D: |-
      Solves $1 - 2h/R = 1/4$ using the near-surface approximation. That approximation only holds for $h \ll R$; it cannot describe a fall as large as a factor of four.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A pit lane at a hill-climb event: a car on a weighbridge, a team truck with a satellite dish on its roof, a GPS aerial on the car's engine cover and a drop-test rig beside the scrutineering bay](scenes/motorsport/gravitation.svg "The car on the weighbridge is being checked against a minimum weight. What the scale reads depends on where the scale is standing.")

Rukmini's hill-climb car has to meet a minimum weight, and it clears it by barely two kilograms. She has been trimming the car for weeks and has run out of ideas.

The event is unusual: scrutineers weigh the cars at the **finish**, on a platform beside the last hairpin, about two kilometres higher than the paddock where the team's own scales live.

Varun, who fits the tyres, thinks this is wonderful news. "Two kilometres further from the centre of the Earth. Gravity's weaker up there. The car will weigh less on their scale than on ours — free margin."

Rukmini isn't sure whether to laugh or start recalculating. He isn't wrong about the physics. But is it two kilograms of margin, or two grams?

## The physics

Drop something near the ground and it accelerates downwards at $g$. Where does that number come from? Put a body of mass $m$ on the surface of a spherical Earth of mass $M$ and radius $R$. Newton's law of gravitation gives the pull, and Newton's second law turns it into an acceleration:

$$\frac{GMm}{R^2} = mg \quad\Rightarrow\quad g = \frac{GM}{R^2}$$

The body's own mass **cancels**. That is why a race car and a wheel nut fall side by side — the reason Galileo's result and this formula are the same statement.

**Going up.** At a height $h$ the distance from the centre is $R + h$:

$$g_h = \frac{GM}{(R+h)^2} = g\left(1 + \frac{h}{R}\right)^{-2} \approx g\left(1 - \frac{2h}{R}\right) \quad \text{for } h \ll R$$

The approximation is a binomial expansion, keeping only the first correction; it is useless once $h$ is comparable with $R$.

**Going down.** Treat the Earth as a sphere of uniform density. A shell of matter *above* you pulls you in all directions at once and its effects cancel, so only the ball of radius $R - d$ below you counts. Its mass goes as the cube of its radius while the inverse square divides by the square, leaving

$$g_d = g\left(1 - \frac{d}{R}\right)$$

Straight down at the centre, $g$ is zero. Above the surface the fall-off is an inverse square; below it, a straight line.

![A graph of g against distance from the Earth's centre: rising in a straight line from zero at the centre to a maximum at the surface, then falling as an inverse square outside](figures/acceleration_due_to_gravity/g-vs-distance.svg "g is largest at the surface. Inside it falls linearly to zero at the centre; outside it falls as 1/r², reaching a quarter of its surface value one Earth radius up.")

Two more reasons $g$ is not a single number: the Earth is slightly flattened, so $R$ is a little larger at the equator, and the Earth's rotation reduces the *effective* $g$ you measure there.

## Worked example

**Given:** a car of mass $m = 800\,\text{kg}$ (illustrative), carried to $h = 2000\,\text{m}$; $R = 6.4 \times 10^{6}\,\text{m}$, $g = 9.8\,\text{m/s}^2$ at the paddock.
**Find:** how much less the car weighs at the top.

**Step 1 — the fractional change.** Since $h \ll R$, use $2h/R$:

$$\frac{2h}{R} = \frac{2 \times 2000}{6.4 \times 10^{6}} = \frac{1}{1600}$$

So $g$ drops by one sixteen-hundredth, about $0.06\%$.

**Step 2 — in $\text{m/s}^2$.** $\Delta g = 9.8/1600 \approx 0.006\,\text{m/s}^2$, leaving $g_h \approx 9.794\,\text{m/s}^2$.

**Step 3 — what the scale reads.** A scale calibrated for the paddock would show the car's $800\,\text{kg}$ reduced by $800/1600 = 0.5\,\text{kg}$.

**Sanity check:** half a kilogram, not two — less than the fuel burned on one run up the hill. Varun's free margin is real, but it is a quarter of the two kilograms he was picturing.

## Where the picture breaks

The motorsport here is the setting, not the analogy: hill-climb cars are a way to get two kilometres of height into the story, and nothing about racing explains gravity. The scrutineer's rule is about **mass**, and the car's mass has not changed at all — the same number of atoms went up the hill. Only its *weight*, the force $mg$, has changed, and only because $g$ did.

Real scales complicate things further. Most are calibrated at the factory for a standard $g$ and read out in kilograms, so a careful scrutineer recalibrates on site. And the uniform-density Earth behind $g_d = g(1 - d/R)$ is a teaching model: the real Earth has a dense iron core, so $g$ actually rises slightly for the first few hundred kilometres down before falling.

## Key takeaway

$g = GM/R^2$ — set by the planet, not by the falling body, which is why everything falls together. Above the surface $g_h = GM/(R+h)^2 \approx g(1 - 2h/R)$ for small heights; below it, with a uniform Earth, $g_d = g(1 - d/R)$. Both mean that mass stays put while weight quietly changes.
