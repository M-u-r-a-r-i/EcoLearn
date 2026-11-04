---
concept_id: collisions
interest: gaming
format: explain
title: What the bounciness slider is really changing
check:
  question: |-
    A $4\,\text{kg}$ crate sliding at $5\,\text{m/s}$ hits a stationary $1\,\text{kg}$ crate and the two stick together. What is their common speed just afterwards?
  options:
    A: |-
      $5\,\text{m/s}$
    B: |-
      $4\,\text{m/s}$
    C: |-
      $2.5\,\text{m/s}$
    D: |-
      $4.5\,\text{m/s}$
  answer: B
  explanation: |-
    Momentum is conserved: $(4)(5) + 0 = (4 + 1)V$, so $V = 20/5 = 4\,\text{m/s}$. Kinetic energy is not conserved — it falls from $50\,\text{J}$ to $40\,\text{J}$.
  misconceptions:
    A: |-
      Reads "momentum is conserved" as "speed is unchanged"; the momentum is shared with extra mass, so the same momentum must come with a smaller speed.
    C: |-
      Halves the speed, which would be right only if the two crates had equal masses; here the moving crate is four times heavier, so the pair barely slows.
    D: |-
      Assumes kinetic energy is conserved ($\tfrac{1}{2}(4)(5)^2 = \tfrac{1}{2}(5)v^2$ gives $4.5\,\text{m/s}$); in a collision where the bodies stick, energy is always lost, and only momentum can be used.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor shows a physics sandbox with a spring launcher, a kart at the top of a loop and a crate being dragged by a rope, beside a force-feedback racing wheel and a controller](scenes/gaming/work_energy_power.svg "Every impact in this sandbox is settled in a single frame, by two rules that the engine applies to the colliding pair.")

Zoya's physics sandbox has one slider that everybody in the playtest touches first: **bounciness**, from $0$ to $1$.

At $1$, a dropped crate comes back to the exact height it fell from, then does it again, and again, and the level never settles. Her tester Anirudh calls it "the haunted warehouse". At $0$, crates hit the floor and die where they land, as if made of wet clay.

Both extremes feel wrong. Real crates bounce a little and stop. But when Anirudh asks her what number is *correct*, Zoya realises she cannot answer, because she does not know what the slider is physically changing.

The engine itself is sure of one thing. Whatever the slider says, it always applies the same rule first, and only then uses the slider for a second rule. What is the quantity a collision never touches — and what is the one it is free to destroy?

## The physics

During a collision the two bodies push on each other with equal and opposite forces (Newton's third law) for the same short time. If no outside force matters over that instant, the **total momentum is conserved**:

$$m_1\vec{u}_1 + m_2\vec{u}_2 = m_1\vec{v}_1 + m_2\vec{v}_2$$

This holds in *every* collision — bouncy, sticky or anything between. Kinetic energy is the quantity that is free to change, and it gives the classification:

- **Elastic:** kinetic energy is also conserved. Bounciness $1$.
- **Inelastic:** some kinetic energy becomes heat, sound and deformation. Almost everything real.
- **Perfectly inelastic:** the bodies move off together, and the energy loss is the largest possible for that momentum. Bounciness $0$.

![Top: an elastic head-on collision of two equal masses, where the velocities swap. Bottom: two bodies moving at right angles collide and stick, and the total momentum is the vector sum of the two momenta](figures/collisions/one-d-and-two-d.svg "In two dimensions, add the momenta as vectors. The pair moves off along the total, tilted towards the bigger momentum.")

**One dimension.** Work with signed velocities along one axis. For a perfectly inelastic collision the two unknowns collapse into one:

$$V = \frac{m_1u_1 + m_2u_2}{m_1 + m_2}$$

For an elastic collision you solve the momentum and energy equations together; the famous special case is **equal masses**, where the velocities simply swap — which is why an elastic head-on shot in a game stops one crate dead and sends the other off at the first one's speed.

**Two dimensions.** Momentum is a vector, so conserve each component separately: $\sum p_x$ before $= \sum p_x$ after, and the same for $y$. The combined body of a sticking collision moves off along the vector sum of the two momenta.

## Worked example

**Given** (illustrative sandbox values): a $2\,\text{kg}$ crate slides at $6\,\text{m/s}$ into an identical $2\,\text{kg}$ crate at rest on a frictionless floor.
**Find:** what happens at bounciness $0$, and at bounciness $1$.

**Step 1 — momentum before.** Taking rightwards as positive:

$$p = (2)(6) + 0 = 12\,\text{kg}\,\text{m/s}$$

**Step 2 — bounciness 0: they stick.** All $4\,\text{kg}$ carries that momentum:

$$V = \frac{12}{4} = 3\,\text{m/s}$$

**Step 3 — check the energy.** Before: $\tfrac{1}{2}(2)(6)^2 = 36\,\text{J}$. After: $\tfrac{1}{2}(4)(3)^2 = 18\,\text{J}$. Exactly half has gone into heat, sound and crushed wood.

**Step 4 — bounciness 1: equal masses, elastic.** The velocities swap: the first crate stops dead, the second leaves at $6\,\text{m/s}$. Momentum is still $12\,\text{kg}\,\text{m/s}$ and the energy is still $36\,\text{J}$ — nothing is lost, which is why Anirudh's warehouse never goes quiet.

**Sanity check:** the sticky case must be slower than the bouncy one, since the same momentum is being carried by twice the mass — and $3\,\text{m/s}$ against $6\,\text{m/s}$ is just that.

## Where the picture breaks

A bounciness slider is not a physical constant: real materials are described by a coefficient of restitution that depends on *both* surfaces and even on the impact speed, so one number attached to one crate is already a simplification. Perfectly elastic collisions do not happen between everyday objects — only gas molecules and subatomic particles come close — so $1$ on the slider is a fiction, and Zoya's honest answer for wooden crates is a low value, not zero. This worked example also ignored friction and treated the impact as instantaneous; real contacts last milliseconds, during which gravity and friction do act, just not enough to matter.

## Key takeaway

Momentum is conserved in every collision; kinetic energy is not. A collision is elastic if kinetic energy is also conserved, inelastic if some is lost, and perfectly inelastic if the bodies move off together with $V = (m_1u_1 + m_2u_2)/(m_1 + m_2)$. In two dimensions, conserve each component of momentum separately.
