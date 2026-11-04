---
concept_id: torque_on_current_loop
interest: football
format: explain
title: Where the line marker gets its twist
check:
  question: |-
    A rectangular coil carrying a steady current sits in a **uniform** magnetic field, with the plane of the coil parallel to the field. Which statement is correct?
  options:
    A: |-
      The net force on the coil is zero, but the torque on it is at its maximum.
    B: |-
      Both the net force and the torque are at their maximum.
    C: |-
      The net force is at its maximum, and the torque is zero.
    D: |-
      Both the net force and the torque are zero.
  answer: A
  explanation: |-
    In a uniform field the forces on opposite sides of the loop are equal and opposite, so the net force is always zero. With the coil's plane parallel to $\vec{B}$, its normal is perpendicular to $\vec{B}$ and $\tau = NIAB\sin 90° = NIAB$ — the largest torque it can feel.
  misconceptions:
    B: |-
      Assumes a turning effect must come with a net push. A couple is two equal and opposite forces that are not in line: it turns the coil while pulling it nowhere.
    C: |-
      Swaps the conditions for force and torque. The net force in a uniform field is zero in *every* orientation, not maximum in this one.
    D: |-
      Concludes that if the forces cancel, nothing happens. Forces that cancel can still twist, provided they act along different lines.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground with a coil traced around the goal frame, a pop-up sprinkler on a solenoid valve, an electric line-marking machine and a horn speaker on a pole with a compass lying on its supply cable](scenes/football/moving_charges_magnetism.svg "The line marker, the sprinkler pump and the roller all hide the same thing: a coil that turns in a magnetic field.")

Aditi has been allowed to push the line marker, which is more of a privilege than it sounds, because the machine does the hard part itself — a small electric motor drives the wheels and she only steers.

Down the near touchline the line is beautiful. Then she reaches the corner, where the ground rises slightly and last night's rain has left the turf soft, and the motor's whine drops in pitch. The machine slows, digs in, and the line comes out fat and wavy.

The groundsman is not worried. He tells her the motor is "losing its twist" and that easing off will let it recover, which it does.

Aditi has taken the casing off one of these before. There is no gear lever inside, no clutch, nothing that grips — just a coil of wire spinning between two curved magnets. She cannot see where any twist would come from at all.

## The physics

It comes from two forces that refuse to line up.

Put a rectangular loop of wire, carrying current $I$, into a uniform field $\vec{B}$, with the loop's plane parallel to the field. The two sides that run across the field feel forces $F = BIL$ by $\vec{F} = I\vec{L} \times \vec{B}$ — one up, one down, because their currents run opposite ways.

![A current loop seen edge on in a uniform field, with one side pushed up and the other pushed down; and the magnetic moment m at an angle theta to B](figures/torque_on_current_loop/torque-on-loop.svg "Equal and opposite forces that are not in line make a couple. The net force is zero — only a twist survives.")

Equal and opposite, so the **net force is zero**: the coil is not dragged anywhere. But they act along different lines, separated by the width $b$ of the loop, so they make a **couple**, and the coil turns. For $N$ turns of area $A = L \times b$:

$$\tau = NIAB$$

Turn the coil part-way round and only the component of the field that still lies in the coil's plane does any twisting. Writing $\theta$ for the angle between $\vec{B}$ and the **normal** to the coil,

$$\tau = NIAB\sin\theta$$

This is neat enough to deserve its own quantity. Define the **magnetic dipole moment** of the loop as

$$\vec{m} = NI\vec{A} \qquad (\text{units } \text{A}\,\text{m}^{2})$$

with $\vec{A}$ along the normal, given by curling your right hand the way the current goes. Then

$$\vec{\tau} = \vec{m} \times \vec{B}, \qquad \tau = mB\sin\theta$$

which is exactly the equation for a compass needle in a field. A current loop *is* a magnetic dipole — that is the deepest idea in this chapter.

Two orientations matter. At $\theta = 90°$ (coil's plane along $\vec{B}$) the torque is largest. At $\theta = 0$ (normal along $\vec{B}$) it is zero, and the coil sits there happily: that is the position it is always trying to reach. Everything here assumes a **uniform** field, which is what makes the net force vanish.

## Worked example

**Given:** a small motor coil of $N = 50$ turns and area $A = 4.0\,\text{cm}^{2} = 4.0 \times 10^{-4}\,\text{m}^{2}$, carrying $I = 0.50\,\text{A}$ in a field $B = 0.20\,\text{T}$ (illustrative values).
**Find:** its magnetic moment and the largest torque it can produce.

**Step 1 — the magnetic moment.**

$$m = NIA = (50)(0.50)(4.0 \times 10^{-4}) = 1.0 \times 10^{-2}\,\text{A}\,\text{m}^{2}$$

**Step 2 — the maximum torque**, when the coil's plane lies along the field ($\sin\theta = 1$):

$$\tau = mB = (1.0 \times 10^{-2})(0.20) = 2.0 \times 10^{-3}\,\text{N}\,\text{m}$$

Two millinewton-metres: about what you feel pressing with the weight of a $20\,\text{g}$ object on the end of a lever a centimetre long. Small — but geared down to a wheel, and repeated fifty times a second, it is enough to roll a line marker along a pitch.

**Step 3 — half-turned.** At $\theta = 30°$ the torque is only $\tau = (2.0 \times 10^{-3})(0.5) = 1.0 \times 10^{-3}\,\text{N}\,\text{m}$. The twist depends on where the coil is pointing, not just on the current.

**Sanity check:** the torque has to fall to zero as the coil swings into line with the field, or a motor would spin for ever on one push. It does.

## Where the picture breaks

A coil in a uniform field is not yet a motor. Left alone it would swing to $\theta = 0$ and stop, or rock about that position. A real motor reverses the current every half turn with a **split-ring commutator**, so the coil is always being twisted the same way round; Aditi's machine loses its "twist" when the load slows it and the current cannot keep up.

The field between two flat magnets also is not uniform, and the $\sin\theta$ makes the torque uneven through the turn. The next lesson shows the fix used in a galvanometer: shaped pole pieces that make the field **radial**, so the coil's plane always contains $\vec{B}$ and the torque stays at $NIAB$ all the way round.

Finally, in a field that is *not* uniform, the forces on opposite sides no longer cancel, and the loop feels a net pull as well as a twist. That is how a magnet attracts a current-carrying coil at all.

## Key takeaway

A current loop in a uniform field feels no net force but a torque $\tau = NIAB\sin\theta$, because the forces on opposite sides form a couple. Writing $\vec{m} = NI\vec{A}$ for the **magnetic dipole moment** makes it $\vec{\tau} = \vec{m} \times \vec{B}$ — the same law that turns a compass needle.
