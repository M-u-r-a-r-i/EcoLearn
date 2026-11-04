---
concept_id: torque_on_current_loop
interest: smartphones
format: explain
title: What spins the motor that makes your phone buzz
check:
  question: |-
    A rectangular coil in a tiny motor has $20$ turns, each of area $2.0\,\text{cm}^{2}$, and carries $0.50\,\text{A}$. It sits in a uniform field of $0.40\,\text{T}$, with its magnetic moment $\vec{m}$ (the normal to the coil) at $30^\circ$ to $\vec{B}$. What is the torque on the coil?
  options:
    A: |-
      $8.0\times10^{-4}\,\text{N m}$
    B: |-
      $6.9\times10^{-4}\,\text{N m}$
    C: |-
      $4.0\,\text{N m}$
    D: |-
      $4.0\times10^{-4}\,\text{N m}$
  answer: D
  explanation: |-
    $m = NIA = 20\times0.50\times(2.0\times10^{-4}) = 2.0\times10^{-3}\,\text{A m}^{2}$. Then $\tau = mB\sin\theta = (2.0\times10^{-3})(0.40)(\sin 30^\circ) = 4.0\times10^{-4}\,\text{N m}$.
  misconceptions:
    A: |-
      Ignores the angle and uses the maximum torque $mB$. That is the torque only when $\vec{m}$ is at right angles to $\vec{B}$ — when the plane of the coil lies along the field.
    B: |-
      Uses $\cos 30^\circ$, mixing up the angle of the *normal* with the angle of the coil's *plane*. In $\tau = mB\sin\theta$, $\theta$ is the angle between $\vec{m}$ and $\vec{B}$.
    C: |-
      Forgets to convert the area from $\text{cm}^{2}$ to $\text{m}^{2}$. $1\,\text{cm}^{2} = 10^{-4}\,\text{m}^{2}$, so leaving it out makes the answer $10^{4}$ times too big.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk with a phone lying on a charging cable showing a swung compass arrow, a wireless charging pad with its coil exposed, a flip-cover case with a small magnet in its flap, and a speaker and a small cylinder-shaped vibration motor taken apart](scenes/smartphones/moving_charges_magnetism.svg "Bottom right: the parts of a vibration motor. A tiny spinning part with an off-centre weight is what makes a phone buzz in your pocket.")

Tanvir's old phone buzzes so feebly now that he misses every call. At the repair stall, the technician lets him watch as she opens it and lifts out the culprit: a vibration motor no longer than your fingernail is wide — a little metal cylinder with a lopsided brass weight on its shaft.

She sets the motor on the bench and touches a cell to its two contacts. The weight whirls round into a blur and the whole bench hums. Because the weight is off-centre, each spin tugs the motor one way and then the other — that is the buzz.

Inside the cylinder, she tells him, there are just two things: a small magnet round the outside, and coils of wire on the spinning part.

Tanvir frowns. A magnetic field pushes a wire sideways, in a straight line. So how does a push in straight lines make something spin round and round?

## The physics

Take a rectangular loop carrying current $I$ in a uniform field $\vec{B}$. Each side feels a force $I\vec{L}\times\vec{B}$. For a loop whose plane lies along the field, the two sides across the field feel forces that are **equal and opposite** but **not on the same line** — one side is pushed up and the other down. There's no net force, so the loop doesn't move off; but the pair of forces forms a **couple** that twists it.

![On the left, a rectangular current loop seen edge on in a uniform field, with the force on one side up and the other down; on the right, the magnetic moment m at an angle to B with the torque formula](figures/torque_on_current_loop/torque-on-loop.svg "Equal and opposite forces on opposite sides of the loop: no net push, but a twist. The twist vanishes when m lines up with B.")

Working through the geometry, for a coil of $N$ turns, each of area $A$:

$$\tau = NIAB\sin\theta$$

where $\theta$ is the angle between $\vec{B}$ and the **normal** to the coil. This is packaged neatly by defining the coil's **magnetic dipole moment**:

$$\vec{m} = NI\vec{A}, \qquad m = NIA$$

with unit $\text{A m}^{2}$. Its direction is along the normal, given by the right-hand rule: curl your fingers along the current, and your thumb points along $\vec{m}$. Then

$$\vec{\tau} = \vec{m}\times\vec{B}, \qquad \tau = mB\sin\theta$$

The torque turns $\vec{m}$ towards $\vec{B}$. It is **largest**, $mB$, when the plane of the coil lies along the field ($\theta = 90^\circ$), and **zero** when $\vec{m}$ is lined up with $\vec{B}$ (the coil faces the field square on).

So a coil left alone would twist round, line up and stop. A motor keeps it going with a **commutator**: sliding contacts that reverse the current every half turn, just as the coil lines up, so the torque keeps pushing it round the same way.

## Worked example

**Given:** a rotor coil with $N = 50$ turns, each of area $A = 1.0\,\text{cm}^{2} = 1.0\times10^{-4}\,\text{m}^{2}$, carrying $I = 0.10\,\text{A}$, in a field of $B = 0.50\,\text{T}$ (illustrative values).
**Find:** its magnetic moment, the largest torque, and the torque when $\vec{m}$ is at $30^\circ$ to $\vec{B}$.

**Step 1 — the magnetic moment.**

$$m = NIA = 50\times0.10\times(1.0\times10^{-4}) = 5.0\times10^{-4}\,\text{A m}^{2}$$

**Step 2 — the largest torque** (plane of the coil along the field, $\theta = 90^\circ$).

$$\tau_\text{max} = mB = (5.0\times10^{-4})(0.50) = 2.5\times10^{-4}\,\text{N m}$$

That is the twist you'd get from the weight of a $2.5\,\text{g}$ object — two or three paper clips — hanging on a lever $1\,\text{cm}$ long. Tiny, but the rotor is tinier.

**Step 3 — at $30^\circ$.** $\sin 30^\circ = 0.5$, so $\tau = 1.25\times10^{-4}\,\text{N m}$, half the maximum.

**Sanity check:** as the coil turns to face the field, $\theta$ shrinks to zero and so does the torque — which is exactly when the commutator must flip the current to keep the motor spinning.

## Where the picture breaks

Real motors do not use a single flat coil in a perfectly uniform field. Several coils are spaced round the rotor, and the magnet is shaped so that the torque stays fairly steady through the whole turn, instead of rising and falling like $\sin\theta$.

Many newer phones use a flat, coin-shaped vibration motor, or a linear actuator that shakes back and forth instead of spinning. Those have different layouts; the cylinder motor here is the one closest to the textbook loop.

And the formula gives the torque at one instant. How fast the motor ends up spinning also depends on friction and on the voltage the spinning coil generates — a topic for electromagnetic induction.

## Key takeaway

A current loop in a uniform magnetic field feels no net force but a **torque**, $\vec{\tau} = \vec{m}\times\vec{B}$, of size $\tau = NIAB\sin\theta$. Its **magnetic dipole moment**, $\vec{m} = NI\vec{A}$, points along the normal to the coil by the right-hand rule. The torque turns $\vec{m}$ towards $\vec{B}$: it is largest when the coil's plane lies along the field and zero when $\vec{m}$ lines up with it.
