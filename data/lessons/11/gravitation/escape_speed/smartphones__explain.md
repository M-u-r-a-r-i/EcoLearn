---
concept_id: escape_speed
interest: smartphones
format: explain
title: Why the rocket home from the Moon is so small
check:
  question: |-
    On a small moon, a rover's accelerometer shows $g = 1.6\,\text{m/s}^2$ at the surface, and the moon's radius is $1.8 \times 10^{6}\,\text{m}$. What is the escape speed from its surface?
  options:
    A: |-
      $1.7\,\text{km/s}$
    B: |-
      $11.2\,\text{km/s}$
    C: |-
      $2.4\,\text{km/s}$
    D: |-
      $3.4\,\text{km/s}$
  answer: C
  explanation: |-
    $v_e = \sqrt{2gR} = \sqrt{2 \times 1.6 \times 1.8 \times 10^{6}} = \sqrt{5.76 \times 10^{6}} = 2.4 \times 10^{3}\,\text{m/s} = 2.4\,\text{km/s}$.
  misconceptions:
    A: |-
      Drops the factor of $2$ and computes $\sqrt{gR}$, the speed for skimming the surface in orbit, not the speed to escape; escaping needs $\sqrt{2}$ times more.
    B: |-
      Believes escape speed is a fixed universal number; $11.2\,\text{km/s}$ is the Earth's value, and each body's escape speed depends on its own mass and radius.
    D: |-
      Puts the $2$ outside the square root, computing $2\sqrt{gR}$; the $2$ belongs inside, so the factor is $\sqrt{2}$, not $2$.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A city rooftop at night: a fixed satellite dish, moving navigation satellites, a weather balloon rising with a phone, and a phone and tablet on a table showing a sky plot and a weather image](scenes/smartphones/gravitation.svg "The Moon hangs above the rooftop. Leaving it is far easier than leaving the Earth.")

Leela is showing her grandfather a news article on her phone about robotic missions that bring rock samples back from the Moon. There are two pictures side by side. One is the rocket that left the Earth: a tower taller than a building, wrapped in fire. The other is the little craft that will lift off from the Moon for the trip home: about the size of a cupboard.

Her grandfather zooms in on the second picture with two fingers. "That's the rocket home? It's a toy. The first one needed all that fire."

"It's the same trip, just backwards," Leela says. "Should be the same size, shouldn't it?"

"Unless the Moon holds on to things less tightly," her grandfather says.

"How much less?"

Neither of them knows. What decides how fast something must go to break free of a world, and how different is that speed for the Earth and the Moon?

## The physics

**Escape speed** $v_e$ is the smallest speed you must give a body at a planet's surface so that, with no further push and no air, it never comes back.

Use **conservation of mechanical energy**, with $U = -GMm/r$ and zero at infinity. The body "just" escapes if it arrives infinitely far away with zero speed, so its total energy there is zero. Energy is conserved, so the total at the surface is zero too:

$$\frac{1}{2}mv_e^2 - \frac{GMm}{R} = 0 \quad\Rightarrow\quad v_e = \sqrt{\frac{2GM}{R}} = \sqrt{2gR}$$

using $GM = gR^2$.

- The escaping body's mass $m$ **cancels**: a pebble and a spacecraft need the same speed (though very different energies).
- The **direction** of launch doesn't matter, because energy has no direction. That is why NCERT calls it escape *speed*.
- A body with total energy **below zero** is **bound**: it rises, stops and falls back.

![A graph of energy against distance from the centre: the potential energy curve, a zero-total-energy line that never meets it, and a lower line that meets it at twice the radius](figures/escape_speed/energy-to-escape.svg "With total energy zero, the body always has some kinetic energy left and never turns back. With less, it stops where its line meets the curve and falls.")

The formula also answers Leela's question: $v_e$ depends only on the world's $g$ and $R$. The Moon's surface gravity is about a sixth of the Earth's, and its radius a little over a quarter.

## Worked example

**Given:** for the Earth, $g = 9.8\,\text{m/s}^2$ and $R = 6.4 \times 10^{6}\,\text{m}$.
**Find:** the escape speed.

**Step 1 — the speed squared.**

$$v_e^2 = 2gR = 2 \times 9.8 \times 6.4 \times 10^{6} \approx 1.25 \times 10^{8}\,\text{m}^2/\text{s}^2$$

**Step 2 — the speed.** $v_e = \sqrt{1.25 \times 10^{8}} \approx 1.12 \times 10^{4}\,\text{m/s} = 11.2\,\text{km/s}$.

At that speed you would cover the roughly $1150\,\text{km}$ from Delhi to Mumbai in under two minutes.

The Moon, with its weaker gravity and smaller radius, has an escape speed of only a few kilometres per second; you'll work it out for a similar moon in the check question. Since the energy needed goes as $v^2$, leaving the Moon costs a small fraction of the energy per kilogram that leaving the Earth does. That is most of the answer to the "toy" rocket.

**Sanity check:** a bigger $g$ or a bigger $R$ should make escape harder, and both sit inside the square root on top. They do.

## Where the picture breaks

The phone here is just the screen the story is read on; the physics is the rockets. And the comparison is simplified. The Earth rocket is huge partly because of the **air**: a body can't simply be fired off at $11.2\,\text{km/s}$ through the atmosphere, so rockets climb gradually and fight drag and gravity the whole way. The Moon has no air at all. Real missions also don't need to fully escape: a craft heading home from the Moon only needs to reach an orbit or a transfer path, which takes less than the full escape speed. And our formula ignores the Earth's spin, which gives an eastward launch a small free head start.

## Key takeaway

Escape speed is the launch speed that makes the total mechanical energy exactly zero: $v_e = \sqrt{2GM/R} = \sqrt{2gR}$, about $11.2\,\text{km/s}$ for the Earth. It does not depend on the escaping body's mass or on the launch direction, only on the planet, which is why leaving the Moon is so much easier than leaving the Earth.
