---
concept_id: collisions
interest: smartphones
format: explain
title: The toy cars with magnetic bumpers
check:
  question: |-
    Two app-controlled toy cars, each of mass $0.50\,\text{kg}$, drive across a smooth floor at right angles to each other: one at $4.0\,\text{m/s}$ heading east, the other at $3.0\,\text{m/s}$ heading north. They meet and their magnetic bumpers lock them together. What is their speed just after the collision?
  options:
    A: |-
      $3.5\,\text{m/s}$
    B: |-
      $5.0\,\text{m/s}$
    C: |-
      $0.50\,\text{m/s}$
    D: |-
      $2.5\,\text{m/s}$
  answer: D
  explanation: |-
    Momentum is conserved as a vector. East: $0.50 \times 4.0 = 2.0\,\text{kg m/s}$; north: $0.50 \times 3.0 = 1.5\,\text{kg m/s}$. Total $p = \sqrt{2.0^2 + 1.5^2} = 2.5\,\text{kg m/s}$, shared by $1.0\,\text{kg}$, so $V = 2.5\,\text{m/s}$.
  misconceptions:
    A: |-
      Adds the momenta as plain numbers, $(2.0 + 1.5)/1.0$ — or assumes kinetic energy is conserved, which by coincidence gives about the same. Momenta at right angles add as vectors, and a stick-together collision always loses kinetic energy.
    B: |-
      Adds the two velocities as vectors, $\sqrt{4.0^2 + 3.0^2}$, forgetting that the combined mass is now twice as large. It is momentum, not velocity, that is conserved.
    C: |-
      Subtracts the momenta, $2.0 - 1.5$, as if the cars met head-on. Here they travel at right angles, so neither momentum cancels the other.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A living room in the evening: a camera drone climbs straight up, a phone falls from a shelf towards a cushion, an earbuds case is whirled on a lanyard in a vertical circle, and a robot vacuum rolls towards a sofa leg](scenes/smartphones/work_energy_power.svg "Anything moving in this room carries momentum as well as energy. When two things collide, they share both — but only one of them survives the crash intact.")

For his little cousin's birthday, Harsh has bought two toy cars that you drive with a phone app. Their bumpers have magnets in them, so when they meet nose to tail they latch together and carry on as one.

The children invent a game at once. Tara drives the heavy truck-shaped car flat out down the hallway; Omkar parks the little one in its path. *Clack* — they latch, and the pair rolls on together, noticeably slower than the truck was going.

"Where did the speed go?" Tara demands. "Nothing stopped it."

Harsh thinks it through. Momentum must be the same before and after — nothing outside pushed along the hallway. But the latched pair is clearly slower, so its energy of motion looks smaller too. If momentum is conserved, is energy lost? And how slow should the latched pair be?

## The physics

In a collision the two bodies push on each other with large internal forces for a short time. If external forces are negligible during that time, **total momentum is conserved**:

$$m_1\vec{u}_1 + m_2\vec{u}_2 = m_1\vec{v}_1 + m_2\vec{v}_2$$

Kinetic energy is a different matter:

- **Elastic collision:** total kinetic energy is also conserved. In one dimension, with body 2 at rest, $v_1 = \dfrac{m_1 - m_2}{m_1 + m_2}u_1$ and $v_2 = \dfrac{2m_1}{m_1 + m_2}u_1$. Equal masses simply swap velocities.
- **Inelastic collision:** some kinetic energy becomes heat, sound or permanent deformation.
- **Perfectly inelastic:** the bodies stick together — the largest possible loss consistent with momentum conservation. Then $V = \dfrac{m_1u_1 + m_2u_2}{m_1 + m_2}$.

In **two dimensions**, momentum is conserved as a vector, so conserve its $x$ and $y$ components separately.

![Top: an elastic head-on collision of two equal masses, where the velocities swap. Bottom: two bodies moving at right angles collide and stick, and the total momentum is the vector sum of the two momenta](figures/collisions/one-d-and-two-d.svg "In one dimension, equal masses swap velocities in an elastic collision. In two dimensions, add the momenta as vectors; a stuck-together pair moves off along the total.")

## Worked example

**Given:** truck car $m_1 = 0.40\,\text{kg}$ at $u_1 = 3.0\,\text{m/s}$; small car $m_2 = 0.20\,\text{kg}$ at rest; they latch (illustrative numbers).
**Find:** the pair's speed, and the kinetic energy lost.

1. *Momentum before:* $0.40 \times 3.0 + 0 = 1.2\,\text{kg m/s}$.
2. *Speed after:* the same momentum shared by $0.60\,\text{kg}$: $V = 1.2 / 0.60 = 2.0\,\text{m/s}$. Two-thirds of the truck's speed — the pair must now carry an extra half of the truck's mass.
3. *Energy before and after:* $K_i = \tfrac{1}{2} \times 0.40 \times 3.0^2 = 1.8\,\text{J}$; $K_f = \tfrac{1}{2} \times 0.60 \times 2.0^2 = 1.2\,\text{J}$.
4. *Lost:* $1.8 - 1.2 = 0.6\,\text{J}$ — a third of the energy, gone into the *clack*, a little heat and wobble in the bumpers. Perfectly inelastic, as the latching promised.

**Sanity check:** momentum is the same ($0.60 \times 2.0 = 1.2$), and kinetic energy went down, never up — as it must when two bodies stick.

## Where the picture breaks

Mechanics isn't smartphones' home ground; here the phone is just the remote control, and the cars are the physics. Real toy cars have motors: if the driver keeps the throttle on during the crash, the wheels push on the floor, an external force, and momentum along the hallway is no longer exactly conserved. Friction from the floor also acts, though over the few milliseconds of the collision its effect is small. And no real collision is perfectly elastic — even springy bumpers turn a little energy into sound and heat — so "elastic" is always an idealisation.

## Key takeaway

In every collision without significant external forces, total momentum is conserved — as a vector, so component by component in two dimensions. Kinetic energy is conserved only in an elastic collision; when bodies stick together, the loss is the greatest possible.
