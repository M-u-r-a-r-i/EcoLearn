---
concept_id: acceleration_due_to_gravity
interest: football
format: explain
title: Weighing the match ball ten kilometres up
check:
  question: |-
    At what height above the Earth's surface is the acceleration due to gravity one quarter of its value at the surface? ($R$ is the Earth's radius.)
  options:
    A: |-
      $h = 3R$
    B: |-
      $h = \tfrac{3}{8}R$
    C: |-
      $h = 2R$
    D: |-
      $h = R$
  answer: D
  explanation: |-
    $g_h = g\,R^2/(R+h)^2$. For $g_h = g/4$ we need $(R+h)^2 = 4R^2$, so $R + h = 2R$ and $h = R$.
  misconceptions:
    A: |-
      Takes $g$ to fall off as $1/r$ instead of $1/r^2$, so it asks for four times the distance from the centre.
    B: |-
      Uses the small-height approximation $g(1 - 2h/R)$ far outside its range; it is valid only when $h \ll R$.
    C: |-
      Finds the distance from the centre correctly, $2R$, but gives it as the height; the height above the surface is $r - R$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: the goalkeeper's long kick at the top of its arc, the Moon and a satellite overhead, and a dish on the stand roof aimed at the satellite](scenes/football/gravitation.svg "Every long kick comes back down because of g. But is g the same everywhere?")

The under-17 team is on a flight to an away tournament, and the captain Aman is bored. The pilot has just announced that they are cruising at ten kilometres.

"Ten kilometres up," Aman says. "Gravity must be way weaker here. Ishita, the ball would weigh less."

Ishita, the goalkeeper, has a digital luggage scale in her bag. At home she had hung the match ball from it in its net: $430\,\text{g}$. She hooks it up again, holds it still, and waits for the plane to fly smoothly.

The display flickers, then settles: $430\,\text{g}$.

"Broken," says Aman.

"Or gravity hasn't changed much," says Ishita.

Who's right? By how much does $g$ change ten kilometres up, and what would the scale say at the bottom of a deep mine?

## The physics

**Where $g$ comes from.** A body of mass $m$ on the Earth's surface feels a pull $GMm/R^2$, where $M$ and $R$ are the Earth's mass and radius. That pull is its weight, $mg$:

$$mg = \frac{GMm}{R^2} \quad\Rightarrow\quad g = \frac{GM}{R^2}$$

The body's own mass cancels, so every object falls with the same $g$ (ignoring air). With $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$, $M = 6.0 \times 10^{24}\,\text{kg}$ and $R = 6.4 \times 10^{6}\,\text{m}$, $g \approx 9.8\,\text{m/s}^2$.

**Height $h$ above the surface.** The distance from the centre becomes $R + h$:

$$g_h = \frac{GM}{(R+h)^2} = g\left(\frac{R}{R+h}\right)^2 \approx g\left(1 - \frac{2h}{R}\right) \quad (h \ll R)$$

**Depth $d$ below the surface** (for an Earth of uniform density). The shell of rock above you pulls equally in all directions and gives no net force. Only the inner sphere of radius $R - d$ pulls, and its mass is smaller in proportion to its volume:

$$g_d = g\left(1 - \frac{d}{R}\right)$$

So $g$ is largest at the surface. It falls to zero at the centre, and it falls as $1/r^2$ as you go up.

![A graph of g against distance from Earth's centre: a straight line rising from zero at the centre to its maximum at the surface, then a curve falling as one over r squared](figures/acceleration_due_to_gravity/g-vs-distance.svg "Inside a uniform Earth, g grows in proportion to r; outside, it falls as 1/r². The peak is at the surface.")

A luggage scale measures the pull on the ball and converts it to grams by assuming $g = 9.8\,\text{m/s}^2$. So a smaller $g$ shows up as a smaller reading.

## Worked example

**Given:** $g = 9.8\,\text{m/s}^2$ at the surface; $R = 6.4 \times 10^{6}\,\text{m}$; ball mass $0.43\,\text{kg}$; cruising height $h = 10\,\text{km} = 1.0 \times 10^{4}\,\text{m}$.
**Find:** (a) $g$ at cruising height and what the scale should read; (b) $g$ at the bottom of a mine $2.0\,\text{km}$ deep.

(a) $h \ll R$, so the approximation works:

$$\frac{2h}{R} = \frac{2 \times 1.0 \times 10^{4}}{6.4 \times 10^{6}} = 3.1 \times 10^{-3}$$
$$g_h = 9.8 \times (1 - 0.0031) \approx 9.77\,\text{m/s}^2$$

The ball's weight drops from $0.43 \times 9.8 = 4.21\,\text{N}$ to $0.43 \times 9.77 = 4.20\,\text{N}$. The scale would read about $430 \times 0.9969 \approx 429\,\text{g}$: a change of about one gram.

(b)
$$g_d = 9.8 \times \left(1 - \frac{2.0 \times 10^{3}}{6.4 \times 10^{6}}\right) = 9.8 \times 0.99969 \approx 9.797\,\text{m/s}^2$$

**Sanity check:** the exact formula for (a) gives $9.8 \times (6400/6410)^2 = 9.77\,\text{m/s}^2$, the same. A cheap luggage scale typically shows only every $5$ or $10\,\text{g}$, so a one-gram change is invisible. Ishita was right.

## Where the picture breaks

On a plane, the scale also feels the plane's own accelerations: a bump of turbulence or a gentle turn changes the reading far more than the change in $g$. Ishita's reading only means something while the plane flies straight and level at steady speed.

The formulas are idealisations too. The depth formula assumes a uniform-density Earth, but the real Earth has a dense core, so near the surface $g$ changes differently with depth than this model predicts. The Earth is also slightly flattened and it rotates, so even at sea level $g$ varies a little between the equator and the poles.

## Key takeaway

$g = GM/R^2$, the same for every falling body. It decreases with height as $g(R/(R+h))^2 \approx g(1 - 2h/R)$ for small heights, and with depth as $g(1 - d/R)$ for a uniform Earth. Ten kilometres up, $g$ is only about $0.3\%$ smaller; you have to go up a whole Earth radius to cut it to a quarter.
