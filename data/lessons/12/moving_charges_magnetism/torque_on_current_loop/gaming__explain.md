---
concept_id: torque_on_current_loop
interest: gaming
format: explain
title: Four coils that never move
check:
  question: |-
    A current-carrying loop is placed in a **uniform** magnetic field with its magnetic moment $\vec{m}$ pointing in the same direction as $\vec{B}$. What are the net force and the net torque on the loop?
  options:
    A: |-
      Net force zero and net torque zero.
    B: |-
      Net force zero, and the torque at its maximum value $mB$.
    C: |-
      The force at its maximum, and zero torque.
    D: |-
      Net force zero, and a torque of $mB/2$.
  answer: A
  explanation: |-
    $\tau = mB\sin\theta$ with $\theta = 0$, so the torque vanishes — this is the loop's stable resting position. And in a *uniform* field the forces on opposite sides are equal and opposite whatever the angle, so the net force is always zero.
  misconceptions:
    B: |-
      Measures $\theta$ from the plane of the loop instead of from its normal. When $\vec{m}$ lies along $\vec{B}$ the loop's plane is *perpendicular* to the field — that is the zero-torque position, not the maximum one.
    C: |-
      Expects a magnetic field to drag a current loop bodily towards or away from something. In a uniform field the side forces cancel exactly, so a loop is twisted, never pushed.
    D: |-
      Half-remembers a factor from another formula. $\tau = mB\sin\theta$ carries no factor of a half, and at $\theta = 0$ it is exactly zero.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming workbench with a bartop arcade cabinet, a cutaway of a pinball flipper coil, a controller with its shell off, a PC case fan whose hub holds coils inside a ring magnet, and a phone on a power cable](scenes/gaming/moving_charges_magnetism.svg "Look inside the case fan on the right: four small coils sitting inside a ring of magnet. Nothing touches, and yet it turns.")

Sana's PC has developed a rattle and she has narrowed it down to one of the case fans. She takes it out, peels the sticker off the back of the hub and works off the little clip holding the shaft.

What comes away in her hand is not what she expected. The blades and the shaft lift out together, carrying a ring of grey magnet glued inside the hub. Left behind on the frame is a small star of four coils wound on iron teeth — sitting exactly where the middle of that ring used to be.

The coils are bolted to the frame. They cannot move. The magnet is the part that is free to spin. There are no brushes, no sliding contacts, nothing rubbing anywhere.

She turns the ring slowly with a finger. Nothing resists it at all. And yet this thing spins for years without wearing out.

Four little coils that never move. How do they make the ring go round?

## The physics

Put a rectangular loop of $N$ turns, area $A$, carrying current $I$, into a uniform field $\vec{B}$, with the plane of the loop containing $\vec{B}$.

Each of the two sides that run across the field feels $F = BIL$, from the force law you already have. The two forces are equal in size and **opposite** in direction, because the current runs opposite ways along opposite sides. So the net force on the loop is zero — it does not get dragged anywhere. But the two forces do not act along the same line: they form a **couple**, and a couple twists.

![On the left, a rectangular current loop seen edge on in a uniform field, with the force on one side up and the other down; on the right, the magnetic moment m at an angle to B with the torque formula](figures/torque_on_current_loop/torque-on-loop.svg "Equal and opposite forces on opposite sides: no push, but a twist. The torque dies away as m swings into line with B.")

Working out the moment of that couple gives

$$\tau = N I A B \sin\theta$$

where $\theta$ is measured from the **normal** to the loop, not from its plane. That grouping $NIA$ turns up so often that it gets its own name and symbol — the **magnetic dipole moment**:

$$\vec{m} = N I \vec{A}, \qquad \text{measured in } \text{A}\,\text{m}^{2}$$

with $\vec{A}$ along the normal, given by curling your right hand the way the current runs. Then the whole result compresses to

$$\vec{\tau} = \vec{m}\times\vec{B}$$

A current loop, seen from outside, behaves exactly like a small bar magnet with that moment. Two consequences:

- The torque is **largest** when $\vec{m}$ is perpendicular to $\vec{B}$ — that is, when the loop's plane contains the field.
- The torque is **zero** when $\vec{m}$ lines up with $\vec{B}$. That is where the loop wants to settle and stop.

Which is Sana's real problem. A loop in a fixed field swings into line and stays there; it does not keep going round. To get continuous rotation, something has to reverse the current at the moment the loop reaches the line-up point, so the twist starts again. That is the one job of the electronics under the fan's sticker. It watches where the magnet is and flips the coil currents at the right instant, forever.

All of this assumes a **uniform** field and a steady current.

## Worked example

**Given:** one of the fan's coils, treated as $N = 50$ turns of area $A = 4.0\,\text{cm}^{2} = 4.0\times10^{-4}\,\text{m}^{2}$, carrying $I = 0.50\,\text{A}$ in a field of $B = 0.20\,\text{T}$, held with its plane along the field (illustrative values).
**Find:** its magnetic moment and the torque on it.

**Step 1 — the magnetic moment.**

$$m = NIA = (50)(0.50)(4.0\times10^{-4}) = 1.0\times10^{-2}\,\text{A}\,\text{m}^{2}$$

**Step 2 — the torque.** The plane contains $\vec{B}$, so $\vec{m}$ is perpendicular to it and $\sin\theta = 1$:

$$\tau = mB = (1.0\times10^{-2})(0.20) = 2.0\times10^{-3}\,\text{N}\,\text{m}$$

**Step 3 — picture it.** Two millinewton-metres is the twist you would get by hanging a two-gram weight on the end of a ten-centimetre spanner. Small — but fan blades are light plastic on almost frictionless bearings, and there is nothing else for that twist to fight.

**Sanity check:** a fan that a breath of air can stop needs only a whisper of torque to keep going, so a couple of millinewton-metres is comfortably the right size.

## Where the picture breaks

The textbook picture has a loop turning inside a fixed field. Sana's fan has it the other way round: the coils are bolted down and the magnet spins. That is no contradiction — $\vec{m}$ and $\vec{B}$ twist *each other*, equally and oppositely, and a designer is free to choose which one to let go. Bolting down the coils is what removes the brushes, and removing the brushes is what lets the fan run for years.

"Uniform field" is also a convenient fiction here. Inside a small motor the field curves sharply between the iron teeth and the ring magnet, and the iron itself concentrates the field far beyond anything $\mu_0 n I$ would give — so the honest torque is bigger than the bare formula suggests. The formula gives the shape of the answer, not the number.

And notice what was needed to make the rotation continuous: something must know where the rotor is. In an old brushed motor a sliding **commutator** did that mechanically. In a fan it is done with a magnetic sensor and a switch — the same kind of sensor as the one in the controller thumbstick, doing the same physics.

## Key takeaway

A current loop in a uniform magnetic field feels **no net force but a torque**: $\vec{\tau} = \vec{m}\times\vec{B}$, of size $\tau = NIAB\sin\theta$, where $\vec{m} = NI\vec{A}$ is the loop's **magnetic dipole moment** and $\theta$ is the angle between $\vec{m}$ and $\vec{B}$. The twist is greatest when they are perpendicular and zero when they line up — so continuous rotation needs the current reversed every half turn.
