---
concept_id: momentum_conservation
interest: motorsport
format: explain
title: The push that sent both of them rolling
check:
  question: |-
    A $1500\,\text{kg}$ recovery truck rolls at $2.0\,\text{m/s}$ into a stalled $500\,\text{kg}$ race car standing at rest, and the two move off locked together. Ignoring friction, their common speed is:
  options:
    A: |-
      $1.5\,\text{m/s}$
    B: |-
      $1.0\,\text{m/s}$
    C: |-
      $2.0\,\text{m/s}$
    D: |-
      $6.0\,\text{m/s}$
  answer: A
  explanation: |-
    Total momentum before is $1500 \times 2.0 = 3000\,\text{kg m/s}$, and afterwards the moving mass is $2000\,\text{kg}$, so $V = 3000/2000 = 1.5\,\text{m/s}$.
  misconceptions:
    B: |-
      Averages the two speeds, $2.0$ and $0$. Averaging is only correct when the two masses are equal; here the heavier body dominates the result.
    C: |-
      Thinks conservation of momentum means the speed cannot change. Momentum is conserved, but it is now shared by a larger mass, so the speed must drop.
    D: |-
      Divides the total momentum by the stalled car's mass alone. Once they lock together, the moving body is truck plus car, so use the combined mass.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race car in a braking zone with glowing brake discs, a skid mark and tyre smoke, a tyre barrier along the wall and a marshal with a yellow flag](scenes/motorsport/laws_of_motion.svg "Every shunt, every recovery, every push-start is momentum changing hands between two bodies.")

The garage floor at the karting club is smooth painted concrete, and the mechanics' creeper boards — the low trolleys you lie on to get under a car — roll on it beautifully. Aisha and Karthik were sent to fetch a gearbox, and are, inevitably, sitting on the creepers instead.

Karthik, the heavier of the two, plants his feet on Aisha's board and shoves. She shoots away down the garage, which is what he intended. What he did not intend is that he slides the other way, slowly but unmistakably, and fetches up against the tyre rack.

"You pushed me," Aisha calls back. "So who pushed you?"

An hour later they see it again in the pit lane: a stalled car standing still, and the recovery buggy rolling gently into the back of it. The two move off together, far slower than the buggy was going.

Nobody pushed Karthik. Nothing from outside sped the stalled car up. Could either result have been predicted beforehand?

## The physics

Treat a group of bodies as one **system** and add up all their momenta to get the total. Inside the system the bodies push on one another, but by Newton's third law every internal force comes with an equal and opposite partner, so the internal impulses cancel exactly in the total. Only **external** forces can change it.

**Law of conservation of linear momentum:** if the net external force on a system is zero — an **isolated system** — its total momentum stays constant:

$$m_1\vec{u}_1 + m_2\vec{u}_2 = m_1\vec{v}_1 + m_2\vec{v}_2$$

where the $u$ are velocities before the interaction and the $v$ after. It holds whatever goes on in between, however messy the forces.

- **Recoil and explosions.** The system starts at rest, so the total momentum is zero before *and after*. The two parts must fly apart with equal and opposite momenta. Karthik pushed Aisha one way; his own momentum had to be equal and opposite, and because he is heavier, his speed is smaller.
- **Collisions.** When the buggy runs into the stalled car and they stay together, the momentum the buggy brought is now shared by a much larger mass, so the pair crawls away.

![Top: two bodies at rest flying apart with equal and opposite momentum arrows. Bottom: a body moving into a stationary one; afterwards they travel together with the same total momentum](figures/momentum_conservation/recoil-and-sticking-collision.svg "Recoil above, a sticking collision below. In both, the total momentum arrow after is the same as before.")

Notice carefully what is conserved: **momentum, not velocity**. Equal momenta shared between unequal masses always give unequal speeds.

## Worked example

Take the direction of the push, and of the buggy's travel, as positive throughout.

**Part 1 — recoil.** Karthik, $M = 60\,\text{kg}$, and Aisha, $m = 40\,\text{kg}$, both start at rest on creepers. After the push Aisha moves at $1.5\,\text{m/s}$. Friction on the creepers is ignored.

Before: total $p = 0$. After it must still be zero:

$$40 \times 1.5 + 60\,V = 0 \quad\Rightarrow\quad V = -\frac{60}{60} = -1.0\,\text{m/s}$$

Karthik slides backwards at $1.0\,\text{m/s}$ — a slow walk, and two-thirds of Aisha's speed, because he has one and a half times her mass.

**Part 2 — sticking collision.** The recovery buggy, $600\,\text{kg}$ with its driver, rolls at $2.0\,\text{m/s}$ into a stalled car of $1400\,\text{kg}$ at rest, and the two move off together.

$$600 \times 2.0 + 1400 \times 0 = (600 + 1400)\,V$$

$$V = \frac{1200}{2000} = 0.60\,\text{m/s}$$

Less than a third of the buggy's speed, because the momentum now has to move more than three times the mass.

**Sanity check:** in Part 1 the two momenta are $+60$ and $-60\,\text{kg m/s}$, adding to zero; in Part 2, $2000 \times 0.60 = 1200\,\text{kg m/s}$, the same total as before the bump.

## Where the picture breaks

Conservation needs zero **net external** force, and a garage floor is not frictionless: both creepers do slow down and stop, because the floor has joined the system. A pit lane is rarely perfectly level either, and gravity along a slope is another external force. Note also what is *not* conserved: when the buggy and the car stay locked together, kinetic energy is lost to crumpled panels and heat, even though momentum is untouched — you will meet that distinction with collisions and energy. And the interaction is never instantaneous; it just does not matter, because the totals come out the same however long the push lasts.

## Key takeaway

If no net external force acts on a system, its total momentum is unchanged: $m_1\vec{u}_1 + m_2\vec{u}_2 = m_1\vec{v}_1 + m_2\vec{v}_2$. In recoil the total starts at zero, so the two bodies get equal and opposite momenta and the heavier one moves more slowly. In a sticking collision the momentum is shared out over a bigger mass, so the pair moves off slowly.
