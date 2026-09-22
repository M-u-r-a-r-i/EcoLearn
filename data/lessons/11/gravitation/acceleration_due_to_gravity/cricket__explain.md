---
concept_id: acceleration_due_to_gravity
interest: cricket
format: explain
title: Does the ball really fly further at a hill ground
check:
  question: |-
    A weather balloon carries a cricket ball $32\,\text{km}$ above the Earth's surface. Taking $g = 9.80\,\text{m/s}^2$ at the surface and $R = 6400\,\text{km}$, what is the acceleration due to gravity at that height?
  options:
    A: |-
      $9.80\,\text{m/s}^2$
    B: |-
      $9.75\,\text{m/s}^2$
    C: |-
      $0\,\text{m/s}^2$
    D: |-
      $9.70\,\text{m/s}^2$
  answer: D
  explanation: |-
    For $h \ll R$, $g_h \approx g(1 - 2h/R) = 9.80 \times (1 - 2 \times 32/6400) = 9.80 \times 0.990 = 9.70\,\text{m/s}^2$. The exact $g(R/(R+h))^2$ gives the same to three figures.
  misconceptions:
    A: |-
      Treats $g$ as a fixed constant everywhere; it falls off with distance from the Earth's centre.
    B: |-
      Uses the depth formula $g(1 - d/R)$ for a height; above the surface, $g$ falls twice as fast, as $g(1 - 2h/R)$.
    C: |-
      Believes gravity stops where the air thins out; gravity does not need air, and at $32\,\text{km}$ it is almost as strong as at the ground.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: a ball skied above a fielder, the Moon and a satellite overhead, and a broadcast van's dish aimed at the sky](scenes/cricket/gravitation.svg "Every skier comes down because of g. But is g the same at every ground?")

The under-19 squad has just arrived at a hill-station ground, about two kilometres above sea level. In the first practice session the ball seems to fly off the bat. Karthik skies one that clears the rope easily, and turns round with his arms up.

"It's the altitude," he announces. "We're further from the Earth up here, so gravity is weaker. The ball stays up longer."

His teammate Divya isn't convinced. "Two kilometres? The Earth is thousands of kilometres across. That's nothing."

"Nothing? You saw that shot!"

They make a bet: a round of chai for the whole squad. To settle it, they need a number. How much does gravity actually weaken two kilometres up, and what would it be if you dug down instead? And is g even the reason the ball is flying further?

## The physics

**Where $g$ comes from.** A body of mass $m$ at the Earth's surface feels the gravitational pull $GMm/R^2$, where $M$ and $R$ are the Earth's mass and radius. That is its weight, $mg$:

$$mg = \frac{GMm}{R^2} \quad\Rightarrow\quad g = \frac{GM}{R^2}$$

The ball's mass cancels, which is why every ball, heavy or light, falls with the same $g$ (ignoring air). With $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$, $M = 6.0 \times 10^{24}\,\text{kg}$ and $R = 6.4 \times 10^{6}\,\text{m}$, this gives $g \approx 9.8\,\text{m/s}^2$.

**Above the surface.** At height $h$, the distance from the centre becomes $R + h$:

$$g_h = \frac{GM}{(R + h)^2} = g\left(\frac{R}{R + h}\right)^2 \approx g\left(1 - \frac{2h}{R}\right) \quad (h \ll R)$$

**Below the surface.** Model the Earth as a sphere of uniform density. At depth $d$, the shell of rock above you pulls equally in all directions and gives no net force; only the inner sphere of radius $R - d$ pulls, and its mass is smaller in proportion to its volume. The result is

$$g_d = g\left(1 - \frac{d}{R}\right)$$

So $g$ is greatest at the surface. It falls off slowly as you go down, reaching zero at the centre, and falls off as $1/r^2$ as you go up.

![A graph of g against distance from Earth's centre: a straight line rising from zero at the centre to its maximum at the surface, then a curve falling as one over r squared](figures/acceleration_due_to_gravity/g-vs-distance.svg "Inside a uniform Earth, g grows in proportion to r; outside, it falls as 1/r². The peak is at the surface.")

## Worked example

**Given:** $g = 9.8\,\text{m/s}^2$ at sea level; $R = 6.4 \times 10^{6}\,\text{m}$; the ground is at $h = 2.0\,\text{km} = 2.0 \times 10^{3}\,\text{m}$.
**Find:** (a) $g$ at the ground; (b) $g$ at the bottom of a mine $3.2\,\text{km}$ deep.

(a) $h \ll R$, so use the approximation:

$$\frac{2h}{R} = \frac{2 \times 2.0 \times 10^{3}}{6.4 \times 10^{6}} = 6.25 \times 10^{-4}$$
$$g_h = 9.8 \times (1 - 0.000625) = 9.794\,\text{m/s}^2$$

That is a drop of $0.006\,\text{m/s}^2$, about $0.06\%$.

(b)
$$g_d = 9.8 \times \left(1 - \frac{3.2 \times 10^{3}}{6.4 \times 10^{6}}\right) = 9.8 \times (1 - 0.0005) = 9.795\,\text{m/s}^2$$

**Sanity check:** the exact formula for (a) gives $9.8 \times (6400/6402)^2 = 9.794\,\text{m/s}^2$, the same answer. For a big hit, the distance travelled in a vacuum would be proportional to $1/g$, so a $0.06\%$ smaller $g$ adds about $4\,\text{cm}$ to a $60\,\text{m}$ hit. Divya wins the chai.

## Where the picture breaks

The ball really does travel further at altitude, but not mainly because of $g$. Two kilometres up, the air is noticeably thinner, so there is less **air drag** slowing the ball. That effect is far larger than the tiny change in $g$. Our formulas ignore air completely.

The formulas are idealisations too. The depth result assumes a uniform-density Earth; the real Earth has a dense core, so near the surface $g$ actually changes differently with depth. The Earth is also not a perfect sphere and it rotates, which is why $g$ at sea level varies slightly between the poles and the equator.

## Key takeaway

$g = GM/R^2$, the same for every falling body. It decreases with height as $g(R/(R+h))^2 \approx g(1 - 2h/R)$ for small heights, and with depth as $g(1 - d/R)$ for a uniform Earth. Two kilometres up, $g$ drops by only about $0.06\%$.
