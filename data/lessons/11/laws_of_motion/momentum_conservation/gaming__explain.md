---
concept_id: momentum_conservation
interest: gaming
format: explain
title: The toolbox trick that gets a stranded astronaut home
check:
  question: |-
    In a game with realistic physics, a $120\,\text{kg}$ robot stands at rest on frictionless ice. It fires a $2.0\,\text{kg}$ projectile forwards at $30\,\text{m/s}$. What is the robot's velocity just afterwards?
  options:
    A: |-
      zero, because the robot has nothing to push against
    B: |-
      $0.50\,\text{m/s}$ backwards
    C: |-
      $30\,\text{m/s}$ backwards
    D: |-
      $0.50\,\text{m/s}$ forwards
  answer: B
  explanation: |-
    The total momentum is zero before, so it is zero after: $120\,v + 2.0 \times 30 = 0$, giving $v = -0.50\,\text{m/s}$. The minus sign means backwards, opposite to the projectile.
  misconceptions:
    A: |-
      Thinks a body can only move by pushing on something outside it. The robot pushes the projectile, and the projectile pushes back on the robot; that internal pair is enough.
    C: |-
      Assumes both pieces move off at the same speed. It is the momenta that are equal and opposite; the heavier robot moves much more slowly.
    D: |-
      Gets the right size but loses the sign. For the total to stay zero, the robot's momentum must point opposite to the projectile's.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a racing game on the monitor and a zero-gravity game on a tablet](scenes/gaming/laws_of_motion.svg "In zero-g, every push sends two things moving. Out there, that is the only way to get anywhere.")

Kavin's space-survival game has one moment every player dreads. Your astronaut floats outside the station, the jetpack coughs and runs dry, and the airlock is thirty metres away. You are not moving. There is nothing to grab and nothing to kick against.

His friend Saanvi, watching over a video call, thinks the run is over. "Restart. You're stuck. You can't swim in space."

Kavin grins. He opens his inventory, selects the heavy toolbox, turns his astronaut to face *away* from the station, and throws it as hard as the game allows.

The toolbox tumbles off into the dark. And, slowly, very slowly, his astronaut starts drifting backwards towards the airlock.

"That's a cheat," says Saanvi. "Throwing something can't move you. You're not pushing against anything."

Is it a cheat? And if it isn't, how long will the drift home take?

## The physics

Think about the astronaut and the toolbox together as one **system**. During the throw, the astronaut pushes the toolbox and, by the third law, the toolbox pushes back on the astronaut with an equal and opposite force for exactly the same time. So their impulses are equal and opposite, and their momentum changes are equal and opposite. Added together, they give zero.

That is the **law of conservation of linear momentum**:

> If the net external force on a system is zero, its total linear momentum stays constant.

$$\vec{p}_\text{total, before} = \vec{p}_\text{total, after}$$

A system with no net external force is called **isolated**. Forces *inside* the system, like the throw, move momentum from one part to another but can never change the total.

**Recoil and explosions.** Kavin's astronaut and toolbox start at rest, so the total is zero. Afterwards the two momenta must be equal and opposite: $m_1 v_1 + m_2 v_2 = 0$. A gun recoiling, a grenade bursting into fragments, a rocket pushing out exhaust: all the same rule.

**Collisions.** When two bodies collide, huge forces act for a short time, but they are internal. So the total momentum just after equals the total just before. If the bodies stick together, they move off with one common velocity.

![Top: a large body and small ball at rest fly apart with equal and opposite momentum arrows. Bottom: a small body moving into a large body at rest; afterwards they move together with the same total momentum](figures/momentum_conservation/recoil-and-sticking-collision.svg "Top: recoil, like Kavin's toolbox throw. Bottom: a sticking collision, like a cargo pod latching onto a module. In both, the total momentum after equals the total before.")

## Worked example

**Given (illustrative values):** astronaut with suit $M = 100\,\text{kg}$ and toolbox $m = 5.0\,\text{kg}$, at rest, $30\,\text{m}$ from the airlock. The toolbox is thrown away from the station at $6.0\,\text{m/s}$.
**Find:** (a) the astronaut's recoil velocity and the time to reach the airlock; (b) later, a $400\,\text{kg}$ cargo pod moving at $2.0\,\text{m/s}$ latches onto a $1600\,\text{kg}$ module at rest. Find their common velocity.

(a) Take "away from the station" as positive. Total momentum before: $0$.

$$M V + m v = 0 \quad\Rightarrow\quad V = -\frac{m v}{M} = -\frac{5.0 \times 6.0}{100} = -0.30\,\text{m/s}$$

The minus sign means the astronaut moves *towards* the station at $0.30\,\text{m/s}$. With no force after the throw, that speed stays constant, so

$$t = \frac{30\,\text{m}}{0.30\,\text{m/s}} = 100\,\text{s}$$

A slow drift, but home in under two minutes.

(b) Before: $400 \times 2.0 + 1600 \times 0 = 800\,\text{kg m/s}$. After, together:

$$(400 + 1600)\,v = 800 \quad\Rightarrow\quad v = 0.40\,\text{m/s}$$

in the pod's original direction.

**Sanity check:** in (a), the toolbox has $5.0 \times 6.0 = 30\,\text{kg m/s}$ one way and the astronaut $100 \times 0.30 = 30\,\text{kg m/s}$ the other ✓. In (b), the pair is five times the pod's mass, so the speed should be a fifth: $2.0/5 = 0.40$ ✓.

## Where the picture breaks

Momentum is conserved only for an isolated system. Near a planet, gravity is an external force, so over long times the total changes; the law still holds very well during a quick throw or collision, when gravity's impulse is tiny compared with the internal ones. In the ice example, friction is the external force we ignored. A game may also add its own "drag" to space motion for playability, which would slowly steal the astronaut's momentum. And a real throw sets the astronaut spinning unless the push passes through the body's centre, which is rotation, coming later.

## Key takeaway

If no net external force acts on a system, its total linear momentum stays constant: $\vec{p}_\text{before} = \vec{p}_\text{after}$. Internal forces, from a throw, an explosion or a collision, can only pass momentum between the parts. From rest, the pieces fly apart with equal and opposite momenta; bodies that stick together share the total momentum they had before.
