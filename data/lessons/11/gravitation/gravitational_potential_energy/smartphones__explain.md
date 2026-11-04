---
concept_id: gravitational_potential_energy
interest: smartphones
format: explain
title: When the stair-counting formula stops working
check:
  question: |-
    A small satellite of mass $m$ is lifted from the Earth's surface to a height equal to the Earth's radius $R$. In terms of $m$, $g$ and $R$, by how much does its gravitational potential energy increase?
  options:
    A: |-
      $mgR$
    B: |-
      $-\dfrac{mgR}{2}$
    C: |-
      $\dfrac{3mgR}{4}$
    D: |-
      $\dfrac{mgR}{2}$
  answer: D
  explanation: |-
    With $U = -GMm/r$ and $GM = gR^2$: $U(R) = -mgR$ and $U(2R) = -mgR/2$. The increase is $-mgR/2 - (-mgR) = mgR/2$.
  misconceptions:
    A: |-
      Uses $mgh$ far outside its range of validity; $mgh$ assumes $g$ stays constant, but $g$ weakens with height, so the true rise is only half of this.
    B: |-
      Gets the sign backwards because $U$ is negative; raising a body always increases its potential energy, so $U$ becomes less negative and the change is positive.
    C: |-
      Treats the potential energy as falling off as $1/r^2$, like the force; the potential energy varies as $1/r$.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A city rooftop at night: a fixed satellite dish, moving navigation satellites, a weather balloon rising with a phone, and a phone and tablet on a table showing a sky plot and a weather image](scenes/smartphones/gravitation.svg "The satellites overhead sit thousands of kilometres up. Lifting them there took energy, but how much?")

Diya's phone has a fitness feature that uses its pressure sensor to count how many floors she climbs. Every evening it shows her a little badge: *20 floors today*. She has worked out, from her physics lessons, that each floor is about $3\,\text{m}$, and that climbing it means doing work $mgh$ against gravity.

Her brother Om is lying on the sofa, reading about the navigation satellites that his phone's map uses. They orbit about twenty thousand kilometres up.

"Easy," he says. "Mass times $g$ times twenty thousand kilometres. That's the energy to get one up there. Your formula does satellites too."

Diya frowns. Her formula has worked perfectly for stairs, for a lift, even for a hill. But twenty thousand kilometres is three times the radius of the whole Earth. Does $mgh$ still hold that far up, and if not, what replaces it?

## The physics

$mgh$ assumes $g$ is **constant** over the height $h$. For stairs, that's excellent. But $g$ falls as $1/r^2$ with distance $r$ from the Earth's centre, so over thousands of kilometres the pull is weaker than $mg$ for most of the climb, and $mgh$ overestimates the work.

The exact result, from adding up the work against the weakening force, is the **gravitational potential energy**

$$U(r) = -\frac{GMm}{r} \qquad (r \ge R)$$

with $U = 0$ chosen at **infinity**, where the pull vanishes. So $U$ is **negative** everywhere at a finite distance, and it rises towards zero as $r$ grows. The **gravitational potential** is the potential energy per unit mass, $V = U/m = -GM/r$, measured in J/kg.

**Why $mgh$ is the near-surface version.** Lifting from $R$ to $R + h$:

$$\Delta U = GMm\left(\frac{1}{R} - \frac{1}{R+h}\right) = \frac{GMm\,h}{R(R+h)} \approx \frac{GMm}{R^2}\,h = mgh \quad (h \ll R)$$

using $g = GM/R^2$. So $mgh$ is not wrong; it is the small-$h$ limit of the true result.

![A graph of U against r over R: a red curve rising from minus one towards zero, and a grey dashed straight line leaving the surface along the curve then climbing too fast](figures/gravitational_potential_energy/u-vs-r-and-mgh.svg "Near the surface the mgh line hugs the true curve. Far out, the line climbs too fast: at h = R, mgh gives twice the true rise.")

## Worked example

**Given:** a $1\,\text{kg}$ test mass lifted from the surface to a height $h = R = 6400\,\text{km}$; $g = 9.8\,\text{m/s}^2$.
**Find:** $\Delta U$ from $mgh$, and the true value.

**Step 1 — the $mgh$ estimate.** $mgR = 1 \times 9.8 \times 6.4 \times 10^{6} \approx 6.27 \times 10^{7}\,\text{J}$.

**Step 2 — the true start and end.** With $GM = gR^2$: at the surface $U = -GMm/R = -mgR \approx -6.27 \times 10^{7}\,\text{J}$; at $r = 2R$ it is half that, $-3.14 \times 10^{7}\,\text{J}$.

**Step 3 — the true rise.** $\Delta U = -3.14 \times 10^{7} - (-6.27 \times 10^{7}) \approx 3.1 \times 10^{7}\,\text{J}$.

So $mgh$ overestimates by a factor of two. The true energy is about what a $1\,\text{kW}$ kettle uses in nine hours, for just one kilogram. Om's satellite, three Earth radii up, would be even further off.

**Sanity check:** the true answer must be smaller than $mgh$, because the pull weakens on the way up. It is.

## Where the picture breaks

The fitness app is a genuine place where $mgh$ does the job: for $3\,\text{m}$ floors, the error is less than one part in a million. The phone then turns that work into "calories" with its own rough model of your body, which is not physics we can check here.

Om's satellite is where the picture breaks, and not only because of $mgh$. Getting a satellite into orbit also needs a large **speed** along the orbit, so the potential energy is only part of the launch energy bill. Rockets also spend most of their fuel lifting fuel. And $U = -GMm/r$ holds only outside the Earth, treated as a uniform sphere.

## Key takeaway

The gravitational potential energy of a mass $m$ at distance $r$ from the Earth's centre is $U = -GMm/r$, zero at infinity and negative everywhere closer. $mgh$ is its near-surface approximation, valid only when $h \ll R$; lifting all the way to $h = R$ takes only half of what $mgh$ predicts.
