---
concept_id: acceleration_due_to_gravity
interest: smartphones
format: explain
title: The phone that rode a weather balloon
check:
  question: |-
    A phone's sensor app on a hill $1.6\,\text{km}$ high would show $g$ smaller than at sea level by some small amount. At roughly what depth down a mine would $g$ be smaller by the **same** amount? Take the Earth as a uniform sphere of radius $6400\,\text{km}$, and both distances small compared with it.
  options:
    A: |-
      $3.2\,\text{km}$
    B: |-
      $1.6\,\text{km}$
    C: |-
      $0.8\,\text{km}$
    D: |-
      $6.4\,\text{km}$
  answer: A
  explanation: |-
    For small heights $g_h \approx g(1 - 2h/R)$; below the surface $g_d = g(1 - d/R)$. Equal drops need $d/R = 2h/R$, so $d = 2h = 3.2\,\text{km}$.
  misconceptions:
    B: |-
      Assumes going up and going down change $g$ by the same formula; above the surface $g$ falls twice as fast with distance as it does below.
    C: |-
      Has the factor of two the wrong way round, as if depth reduced $g$ faster than height; going down, less of the Earth's mass pulls you, which is the slower effect.
    D: |-
      Uses a factor of four from the inverse-square law, but for small heights $(1 + h/R)^{-2} \approx 1 - 2h/R$, which gives a factor of two.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A city rooftop at night: a fixed satellite dish, moving navigation satellites, a weather balloon rising with a phone, and a phone and tablet on a table showing a sky plot and a weather image](scenes/smartphones/gravitation.svg "On the left, a weather balloon lifts a phone into the sky. Its sensors keep logging the whole way up.")

The school science club has a weather balloon, a foam box and an old phone. Riya has set the phone to log everything its sensors can: pressure, position and the accelerometer. The plan is to let the balloon climb to about $32\,\text{km}$, far above any aeroplane, until it bursts and the box parachutes down.

On the ground, the phone lies in the box and the accelerometer app reads close to $9.8\,\text{m/s}^2$.

"At the top it'll be half that," says Manav confidently. "Thirty-two kilometres up is basically space, and in space things are weightless."

"Half?" says Riya. "I'd guess it barely changes."

Manav holds out his hand. "Fifty rupees says it drops a lot."

Riya shakes on it. How much weaker is the Earth's pull, $32\,\text{km}$ up, and who will win the bet?

## The physics

**Deriving $g$.** A phone of mass $m$ at the Earth's surface feels the pull $F = GMm/R^2$, where $M$ and $R$ are the Earth's mass and radius. Its free-fall acceleration is $F/m$, so

$$g = \frac{GM}{R^2}$$

The phone's own mass cancels: every object near the surface falls with the same $g$, about $9.8\,\text{m/s}^2$.

**Above the surface.** At height $h$, the distance from the centre is $R + h$:

$$g_h = \frac{GM}{(R+h)^2} = g\left(1 + \frac{h}{R}\right)^{-2} \approx g\left(1 - \frac{2h}{R}\right) \quad (h \ll R)$$

**Below the surface.** Down a mine at depth $d$, only the Earth's mass inside radius $R - d$ pulls you on balance (the shell above you pulls equally in all directions). For a uniform Earth this gives

$$g_d = g\left(1 - \frac{d}{R}\right)$$

and at the centre, $d = R$, so $g = 0$.

![A graph of g against distance from Earth's centre: a straight line rising from zero at the centre to its maximum at the surface, then a curve falling as one over r squared](figures/acceleration_due_to_gravity/g-vs-distance.svg "Inside a uniform Earth, g grows in proportion to r; outside, it falls as 1/r². Either way, g is largest at the surface.")

The balloon only climbs a tiny way along this curve, because $32\,\text{km}$ is small next to the Earth's radius of about $6400\,\text{km}$.

## Worked example

**Given:** $g = 9.8\,\text{m/s}^2$ at the surface, $R = 6400\,\text{km}$, balloon height $h = 32\,\text{km}$.
**Find:** $g$ at the top of the flight.

**Step 1 — how far up, compared with the Earth.** $h/R = 32/6400 = 0.005$: half of one per cent of the way out from the centre.

**Step 2 — the fractional drop.** $2h/R = 0.01$, so $g$ is about one per cent smaller.

**Step 3 — the new value.** $g_h \approx 9.8 \times (1 - 0.01) = 9.70\,\text{m/s}^2$.

Riya wins the fifty rupees. At more than three times the height of the highest mountains, the Earth still pulls about $99\%$ as hard.

**Sanity check:** the exact formula gives $9.8 \times (6400/6432)^2 \approx 9.70\,\text{m/s}^2$ too, as it should when $h$ is this small compared with $R$.

## Where the picture breaks

The phone is a real instrument here, but an imperfect one. An accelerometer does not measure gravity directly: it measures the push from whatever supports it. Lying still in the box, that push balances gravity, so it reads about $g$. But a balloon payload sways and jolts, and after the burst the box is nearly in free fall, when the accelerometer reads close to **zero** even though gravity is still $99\%$ as strong. That zero is what Manav's "weightless in space" really is: falling, not an absence of gravity. A one per cent change is also hard to pick out from a phone sensor's noise and calibration errors, so the neat $9.70$ is the physics, not a promised reading.

The formulas also assume a uniform, non-rotating, spherical Earth. The real Earth spins, bulges at the equator and is denser near its core, so $g$ varies slightly with latitude and place.

## Key takeaway

From the law of gravitation, $g = GM/R^2$, independent of the falling object's mass. Going up by $h$ reduces it to about $g(1 - 2h/R)$; going down by $d$ reduces it to $g(1 - d/R)$. Even $32\,\text{km}$ up, gravity is still about $99\%$ as strong as at the ground.
