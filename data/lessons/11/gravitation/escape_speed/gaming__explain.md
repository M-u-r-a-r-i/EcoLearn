---
concept_id: escape_speed
interest: gaming
format: explain
title: The launch speed the game refuses to let you cheat
check:
  question: |-
    The escape speed from the Earth's surface is about $11.2\,\text{km/s}$. A game world's planet has twice the Earth's mass and twice the Earth's radius. What is the escape speed from its surface?
  options:
    A: |-
      $22.4\,\text{km/s}$
    B: |-
      $11.2\,\text{km/s}$
    C: |-
      $15.8\,\text{km/s}$
    D: |-
      $7.9\,\text{km/s}$
  answer: B
  explanation: |-
    $v_e = \sqrt{2GM/R}$ depends on the ratio $M/R$. Doubling both leaves that ratio unchanged, so the escape speed is the same $11.2\,\text{km/s}$.
  misconceptions:
    A: |-
      Takes escape speed to be proportional to the mass, forgetting both the square root and the radius in the denominator.
    C: |-
      Accounts for the doubled mass ($\sqrt{2} \times 11.2 \approx 15.8$) but ignores the doubled radius, which pulls the answer back down by the same factor.
    D: |-
      Accounts for the doubled radius ($11.2/\sqrt{2} \approx 7.9$) but ignores the doubled mass; both changes matter, and here they cancel exactly.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor runs an orbit simulator with a planet and a ship, and a tablet shows a satellite above a planet](scenes/gaming/gravitation.svg "Every launch in the simulator comes back down — until one doesn't.")

It is the second night of a LAN party, and Imran has abandoned the tournament for a rocket-building game in the corner. His goal is simple: leave the home planet and never come back.

Attempt eleven climbs beautifully, slows, hangs there — and falls. So does twelve. So does thirteen, which he built twice as heavy with twice the boosters.

Sukanya, who has been watching the altitude readout over his shoulder, says the obvious thing. "It always comes back. Everything comes back."

"Not if it's fast enough," Imran says. "There has to be a speed where it just... keeps going. Slowing down forever but never turning around."

"And a heavy rocket needs more of it than a light one, obviously."

Imran isn't sure that's obvious at all. Is there such a speed — and does a heavier ship really need a bigger one?

## The physics

Launch a body of mass $m$ from the surface of a planet of mass $M$ and radius $R$, and ignore air. Gravity is the only force acting and it is conservative, so **mechanical energy is conserved**:

$$\tfrac{1}{2}mv^2 - \frac{GMm}{r} = \text{constant}$$

As the body climbs, $r$ grows, the potential energy $-GMm/r$ rises towards zero, and the kinetic energy falls to pay for it. There are only two outcomes.

- **Total energy negative:** the kinetic energy runs out at some finite $r$. The body stops and falls back. That was attempts eleven to thirteen.
- **Total energy zero or greater:** the body reaches "infinity" — in practice, very far away — with speed to spare, or with exactly none. It never returns.

![A graph of energy against r over R: a curve of potential energy rising towards zero, a dashed line at zero total energy that never meets it, and a lower dashed line that meets it at a finite radius](figures/escape_speed/energy-to-escape.svg "With zero total energy (the upper line) the body always has kinetic energy left over. With less, it stops where the line meets the curve and falls back.")

The **escape speed** $v_e$ is the smallest launch speed that makes the total energy exactly zero:

$$\tfrac{1}{2}mv_e^2 - \frac{GMm}{R} = 0 \quad\Rightarrow\quad v_e = \sqrt{\frac{2GM}{R}} = \sqrt{2gR}$$

using $GM = gR^2$. Three things are worth noticing.

- **The mass $m$ cancels.** Imran's heavier rocket needs exactly the same escape *speed* — though far more energy and fuel to reach it, since $\tfrac{1}{2}mv_e^2$ grows with $m$.
- **Direction does not matter**, as long as the path misses the planet, because energy is a scalar.
- It depends only on the planet: more mass, or a smaller radius, means a higher $v_e$.

## Worked example

**Given:** $g = 9.8\,\text{m/s}^2$ and $R = 6.4 \times 10^{6}\,\text{m}$ for the Earth. The game's small moon has a quarter of the Earth's surface gravity and a quarter of its radius.
**Find:** the escape speed from each.

**Earth.**

$$v_e = \sqrt{2gR} = \sqrt{2 \times 9.8 \times 6.4 \times 10^{6}} = \sqrt{1.25 \times 10^{8}} \approx 1.12 \times 10^{4}\,\text{m/s} = 11.2\,\text{km/s}$$

That is roughly the distance from Delhi to Mumbai covered in about two minutes.

**The moon.** Both $g$ and $R$ are divided by $4$, so their product is divided by $16$, and the square root divides $v_e$ by $4$:

$$v_e = \frac{11.2}{4} = 2.8\,\text{km/s}$$

**Sanity check:** a small, light world should be much easier to leave than a big one, and it is — about a quarter of the launch speed. That is also why small worlds hold on to almost no atmosphere: the fastest gas molecules escape.

## Where the picture breaks

A real rocket never needs $11.2\,\text{km/s}$ at the launch pad, and Imran's game is being generous by letting him try. Escape speed is the answer to a specific question: *what if you get one push at the surface and then coast?* A rocket instead keeps its engines burning as it climbs, so it can leave at a comfortable speed and still escape. A ship fired at $11.2\,\text{km/s}$ through thick air would be torn apart by drag, which our energy equation ignores completely.

"Escape" also means escaping **this planet**. A ship that leaves the planet at exactly $v_e$ is still bound to the game's star, and would need another push to leave the system.

## Key takeaway

Escape speed is the smallest launch speed for which total mechanical energy is zero, so the body never falls back: $v_e = \sqrt{2GM/R} = \sqrt{2gR}$, about $11.2\,\text{km/s}$ for the Earth. It does not depend on the mass of the thing being launched, or on the direction of launch — only on the planet being left behind.
