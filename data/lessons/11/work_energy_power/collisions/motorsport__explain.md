---
concept_id: collisions
interest: motorsport
format: explain
title: Where the energy goes in a first corner tangle
check:
  question: |-
    In a slow-speed tangle, two karts of equal total mass lock together. One was moving at $10\,\text{m/s}$ and the other was stationary. Immediately afterwards, what is their common speed, and what fraction of the kinetic energy has been lost?
  options:
    A: |-
      $5\,\text{m/s}$, and half the kinetic energy is lost.
    B: |-
      $5\,\text{m/s}$, and none is lost, because momentum is conserved.
    C: |-
      $10\,\text{m/s}$, and half the kinetic energy is lost.
    D: |-
      $2.5\,\text{m/s}$, and three quarters of the kinetic energy is lost.
  answer: A
  explanation: |-
    Momentum: $mu = (2m)v$, so $v = u/2 = 5\,\text{m/s}$. Energy: $K_i = \tfrac{1}{2}mu^2$ and $K_f = \tfrac{1}{2}(2m)(u/2)^2 = \tfrac{1}{4}mu^2$, exactly half of $K_i$.
  misconceptions:
    B: |-
      Assumes that because momentum is conserved, kinetic energy must be too. Momentum is conserved in *every* collision; kinetic energy is conserved only in an elastic one, and this pair locked together.
    C: |-
      Keeps the striking kart's speed for the pair. That would double the momentum, because the moving mass has doubled — momentum must stay at $mu$, not become $2mu$.
    D: |-
      Halves the speed twice, as if each kart took half of the half. Only one sharing happens: one lot of momentum spread over twice the mass.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race track scene: a car coasts down a hill road onto the circuit, a second car speeds along the straight with a velocity arrow, a third brakes with glowing red discs, and two people push a kart in the foreground](scenes/motorsport/work_energy_power.svg "Everything in this picture is carrying energy and momentum. A collision is where two of them have to share.")

The junior race gets three corners in before it all goes wrong. Latika is settling into second place when a kart arrives from behind, still braking, and thumps square into the back of hers. The two lock bumpers, slither forward together for a couple of metres and stop.

Nobody is hurt. Both karts drive back to the pits. But the bumper bar on the back of Latika's is visibly bent, and the paint has gone.

In the awning afterwards Bilal, who was marshalling, is puzzling over something. "If they'd bounced apart, the hit would've felt harder — you'd get thrown forward more. But they stuck. So how come the damage is on the kart that *stuck*?"

Latika has a different question. Two karts go in, one joined-up pair comes out — and something about the whole thing feels like the total ought to be the same before and after. But the bent bar says something did *not* survive the crash. What quantity went in and came out unchanged, and what quantity did not?

## The physics

In any collision, the two bodies push on each other with equal and opposite forces for the same short time (Newton's third law). Those internal impulses cancel, so as long as external forces are negligible over that instant:

**Momentum is conserved in every collision.** As a vector:

$$m_1\vec{u}_1 + m_2\vec{u}_2 = m_1\vec{v}_1 + m_2\vec{v}_2$$

Kinetic energy is a different matter, and it is how collisions are classified:

- **Elastic**: kinetic energy is also conserved. Nothing is permanently deformed. Steel balls and gas molecules come close; nothing in a kart race does.
- **Inelastic**: some kinetic energy is converted into deformation, heat and sound. Most real collisions.
- **Perfectly (completely) inelastic**: the bodies move off *together* with a common velocity. This is the case that loses the **most** kinetic energy compatible with conserving momentum.

![Top: two equal balls in an elastic head-on collision swap velocities. Bottom: two bodies moving at right angles stick together, and the combined momentum is the vector sum of the two momenta](figures/collisions/one-d-and-two-d.svg "In one dimension, equal masses swap velocities in an elastic collision. In two dimensions, add the momenta as vectors to find where a stuck-together pair goes.")

**In one dimension**, choose a positive direction and keep signs. For a perfectly inelastic collision, one equation is enough:

$$m_1u_1 + m_2u_2 = (m_1 + m_2)v$$

For an **elastic** collision in one dimension, momentum *and* kinetic energy together give

$$v_1 = \frac{m_1 - m_2}{m_1 + m_2}u_1 + \frac{2m_2}{m_1 + m_2}u_2, \qquad v_2 = \frac{m_2 - m_1}{m_1 + m_2}u_2 + \frac{2m_1}{m_1 + m_2}u_1$$

Two results worth memorising fall out of these: **equal masses simply exchange velocities**, and a light body bouncing off a very heavy one comes back at almost its original speed.

**In two dimensions**, momentum is still conserved, but now as two separate equations — one for each axis. Resolve every velocity into components, conserve $x$ and $y$ separately, and recombine at the end. Momentum conservation alone does not fix a two-dimensional collision; you need one more piece of information, such as "they stuck together" or a measured angle.

Bilal's puzzle now answers itself. Sticking together is the *worst* case for energy: the maximum possible amount has to go somewhere other than motion, and bent bumper bars are where it went.

## Worked example

**Given** (illustrative): kart and driver $m_1 = 200\,\text{kg}$ travelling at $u_1 = 10\,\text{m/s}$ runs into an identical stationary kart and driver, $m_2 = 200\,\text{kg}$, $u_2 = 0$. They lock together. Take forwards as positive.
**Find:** their common speed, and the kinetic energy lost.

*Momentum before* is all in the moving kart:

$$p = 200 \times 10 = 2000\,\text{kg}\,\text{m/s}$$

*Common speed after.* The same momentum is now carried by $400\,\text{kg}$:

$$v = \frac{2000}{400} = 5\,\text{m/s}$$

*Kinetic energy before and after:*

$$K_i = \tfrac{1}{2}(200)(10)^2 = 10\,000\,\text{J}, \qquad K_f = \tfrac{1}{2}(400)(5)^2 = 5000\,\text{J}$$

Half the kinetic energy — $5000\,\text{J}$ — has gone, into bending that bumper bar, warming the metal and making the bang. That "half" is not a coincidence of these numbers: whenever equal masses stick together and one of them started at rest, exactly half is always lost.

**Sanity check:** the pair moves off slower than the kart that hit them but faster than the one that was sitting still, which is the only sensible place for it to be.

## Where the picture breaks

No collision is truly isolated. Friction, grass and the karts' own brakes act during the tangle, so momentum is only *nearly* conserved — the approximation works because the impact lasts a fraction of a second while friction needs much longer to matter. Real karts also do not stay locked: they spring apart a little, which puts them between the perfectly inelastic and elastic cases, described by a coefficient of restitution you will meet later. The energy "lost" is not destroyed either; total energy is always conserved, and the missing joules are simply no longer kinetic. And a real first-corner tangle is two-dimensional and sets both karts spinning, which stores kinetic energy in rotation that this two-line calculation never sees.

## Key takeaway

Momentum is conserved in every collision, as a vector; kinetic energy is conserved only in an **elastic** one. Bodies that move off together make the collision **perfectly inelastic**, which loses the greatest kinetic energy momentum allows — for equal masses with one at rest, exactly half. In two dimensions, conserve momentum component by component.
