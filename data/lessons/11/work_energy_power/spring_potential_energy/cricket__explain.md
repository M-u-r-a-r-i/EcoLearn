---
concept_id: spring_potential_energy
interest: cricket
format: explain
title: How much a hard ball squashes against a wall
check:
  question: |-
    Model a cricket ball hitting a solid wall as an ideal spring: all its kinetic energy is stored as $\tfrac{1}{2}kx^2$ at the moment of maximum squash. If the ball hits the wall at twice the speed, how does its maximum squash $x$ change?
  options:
    A: |-
      It doubles.
    B: |-
      It becomes four times as large.
    C: |-
      It becomes about $1.4$ times as large.
    D: |-
      It stays the same, because the ball's stiffness $k$ has not changed.
  answer: A
  explanation: |-
    From $\tfrac{1}{2}mv^2 = \tfrac{1}{2}kx^2$, $x = v\sqrt{m/k}$, so $x$ is proportional to $v$. Twice the speed means four times the energy, and since the energy goes as $x^2$, the squash doubles.
  misconceptions:
    B: |-
      Correctly sees that the energy becomes four times as large, but assumes the squash is proportional to the energy; the stored energy grows as $x^2$, so four times the energy needs only twice the squash.
    C: |-
      Thinks doubling the speed doubles the energy and then takes a square root ($\sqrt{2} \approx 1.4$); kinetic energy depends on $v^2$, so it quadruples.
    D: |-
      Thinks the stiffness alone fixes how far a spring compresses; $k$ fixes the force for a given squash, but a body arriving with more energy compresses the spring further.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground by day: a batter watches a ball climb high, a fielder waits under it, a player runs up the stadium steps and a groundsman pushes a roller](scenes/cricket/work_energy_power.svg "Every impact on this ground — bat on ball, ball on glove — briefly squashes something.")

Kabir does the same fielding drill every evening: throw the ball hard at the concrete wall behind his building, then catch the rebound. This week he filmed it on his phone in slow motion, and he can't stop replaying one frame. For an instant, the ball touching the wall isn't round. It's flattened on one side, like a squashed orange.

His sister Riya doesn't believe it. "A cricket ball is as hard as a stone. You can't squash it with a throw."

But the video doesn't lie, and the ball does bounce back. For that instant it has stopped moving, so its kinetic energy has gone somewhere — and then come back out again. Where is the energy while the ball is flattened? And how far does a "rock-hard" ball actually squash?

## The physics

Many things behave like a **spring** when squashed or stretched a little. For an ideal spring, the restoring force obeys **Hooke's law**:

$$F = -kx$$

Here $x$ is the extension (positive) or compression (negative) from the natural length. $k$ is the **spring constant**, in N/m, which measures stiffness. The minus sign means the force always points back towards the natural length.

**Stored energy from the graph.** To compress the spring slowly by $x$, you must push with a force that grows from $0$ to $kx$. The work you do is the area under the force-displacement graph — a triangle:

$$W = \tfrac{1}{2} \times x \times kx = \tfrac{1}{2}kx^2$$

The spring force is conservative, so this work is stored as **elastic potential energy**:

$$U = \tfrac{1}{2}kx^2$$

This takes $U = 0$ at the natural length. Because of the $x^2$, the energy is the same for a compression or an extension of the same size. Doubling $x$ stores four times the energy.

![Left: spring force rising in a straight line with compression, with the triangle under it equal to one half k x squared. Right: stored energy rising as a parabola, four times larger when the compression doubles](figures/spring_potential_energy/spring-force-and-energy.svg "The force grows in step with x, so the stored energy — the area under the force line — grows with x squared.")

**Using it in energy problems.** When a moving body compresses a spring and no other force does work, its kinetic energy turns into spring energy. At maximum compression the body is momentarily at rest, so

$$\tfrac{1}{2}mv^2 = \tfrac{1}{2}kx_\text{max}^2$$

The ball against Kabir's wall is exactly this: the ball itself is the spring.

## Worked example

**Given** (illustrative): ball mass $m = 0.16\,\text{kg}$; it hits the wall head-on at $v = 20\,\text{m/s}$; treat the ball as an ideal spring with $k = 2.0 \times 10^{6}\,\text{N/m}$ and the wall as perfectly rigid.
**Find:** the maximum squash and the largest force between ball and wall.

Kinetic energy on arrival:

$$K = \tfrac{1}{2} \times 0.16 \times 20^2 = 32\,\text{J}$$

At maximum squash, all of it is stored:

$$x_\text{max} = \sqrt{\frac{2K}{k}} = \sqrt{\frac{2 \times 32}{2.0 \times 10^{6}}} = \sqrt{3.2 \times 10^{-5}} \approx 5.7 \times 10^{-3}\,\text{m}$$

That is about $5.7\,\text{mm}$ — small, but clearly visible in slow motion. The peak force is

$$F_\text{max} = kx_\text{max} = 2.0 \times 10^{6} \times 5.66 \times 10^{-3} \approx 1.1 \times 10^{4}\,\text{N}$$

**Sanity check:** $\tfrac{1}{2} \times 2.0 \times 10^{6} \times (5.66 \times 10^{-3})^2 = 10^{6} \times 3.2 \times 10^{-5} = 32\,\text{J}$, as it should be. So Riya is half right: the ball is so stiff that even $32\,\text{J}$ squashes it by only a few millimetres.

## Where the picture breaks

A cricket ball is not an ideal spring. Its force grows faster than in proportion to the squash, because the contact patch widens as it flattens, so a single $k$ is only an average. More importantly, a real ball does not give all its energy back. Some becomes heat and sound, which is why the rebound is always slower than the throw. The ideal spring gives the size of the squash, not the full story. The same model works much better for a real steel spring, which returns almost all its energy.

## Key takeaway

A spring (or anything springy) stretched or compressed by $x$ stores elastic potential energy $U = \tfrac{1}{2}kx^2$, the area under its $F = kx$ line. In energy problems, set the kinetic energy lost equal to the spring energy gained: $\tfrac{1}{2}mv^2 = \tfrac{1}{2}kx^2$.
