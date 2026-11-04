---
concept_id: force_on_current_conductor
interest: gaming
format: explain
title: The rumble pack with nothing spinning in it
check:
  question: |-
    A straight piece of wire $5.0\,\text{cm}$ long lies across a uniform field of $0.40\,\text{T}$ and carries $0.50\,\text{A}$, so it feels a force of $0.010\,\text{N}$. The wire is now turned so that it lies **along** the field lines instead of across them, with the same current and the same field. What force does it feel?
  options:
    A: |-
      $0.010\,\text{N}$ — the same as before, since $B$, $I$ and $L$ are all unchanged.
    B: |-
      Zero — the wire feels no force at all.
    C: |-
      $0.020\,\text{N}$ — twice as much, since the wire now runs the whole length of the field.
    D: |-
      $0.005\,\text{N}$ — half as much, since only half the wire is across the field.
  answer: B
  explanation: |-
    The force is $F = BIL\sin\theta$, and $\theta$, the angle between the wire and the field, is now $0°$. A current flowing straight along the field lines feels nothing.
  misconceptions:
    A: |-
      Remembers $F = BIL$ and forgets that it is really $BIL\sin\theta$. The angle between the wire and the field is part of the physics, not a detail.
    C: |-
      Thinks lining the wire up with the field gives the strongest effect. The cross product works the other way round: biggest at right angles, zero when parallel.
    D: |-
      Pictures the wire as "partly in" the field. The whole wire is in the field the whole time; what changed is the angle, and at $0°$ none of its length counts.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming workbench with a bartop arcade cabinet, a cutaway of a pinball flipper coil, a controller with its shell off showing a flat haptic coil beside its magnet, a PC case fan, and a phone on a power cable](scenes/gaming/moving_charges_magnetism.svg "In the opened controller, look at the flat coil lying face to face with a block magnet. That pair is this whole lesson.")

Sahil's controller has stopped rumbling on one side, and he is not paying a repair bill for something that only shakes. He opens both grips on the kitchen table.

The left grip holds exactly what he expected: a small motor with a lump of metal bolted off-centre to its shaft. Spin that and the whole controller wobbles.

The right grip holds something else — a flat sealed module with two wires going in. He prises it open and finds no motor at all. A block magnet. A flat coil of fine wire lying face to face with it. A small mass on springs. Nothing in there rotates; nothing in there *can* rotate.

He touches the coil's two wires to a cell for half a second. The mass jumps sideways, hard enough to feel through the plastic.

A coil, a magnet, one moment of current — and something kicks. Where is the push coming from?

## The physics

From the last lesson, with one extra step. A current is just charge on the move, so a wire carrying current in a magnetic field is a whole crowd of charges each being pushed sideways — and the wire has to go where the crowd goes.

Count it up. If the wire has $n$ free charges per unit volume, cross-section $A$ and length $L$, it holds $nAL$ carriers, each of charge $q$ drifting at $v_d$ and each feeling $qv_dB$. Multiply:

$$F = (nAL)(qv_dB) = (nAqv_d)LB = BIL$$

because $I = nAqv_d$ is exactly the current. The drift speed and the carrier count vanish, and what is left is something you can measure with an ammeter and a ruler. In vector form, for a straight wire,

$$\vec{F} = I\,(\vec{L}\times\vec{B}) \qquad\text{so}\qquad F = BIL\sin\theta$$

where $\vec{L}$ points along the conventional current and $\theta$ is the angle between the wire and the field.

![A straight wire of length L carrying current I in a uniform field into the page, with the force upward and equal to BIL; below, the wire tilted at an angle so only the perpendicular part counts](figures/force_on_current_conductor/force-on-current-wire.svg "Only the part of the wire across the field counts. Turn the wire to lie along B and the force disappears.")

Three things to hold on to. The force is **perpendicular to both** the wire and the field. It is largest when the wire is at right angles to $\vec{B}$ and zero when it lies along it. And **reverse the current and the force reverses** — which is the whole secret of Sahil's module. Send current one way and the mass is thrown one way; flip it and the mass is thrown back. Do that a few hundred times a second and you have a sharp tap you can feel.

The formula as written assumes a **straight** wire in a **uniform** field carrying a **steady** current.

## Worked example

**Given:** inside the module, about $2.0\,\text{m}$ of fine wire lies across the magnet's field; the field there is about $0.50\,\text{T}$ and at right angles to the wire (illustrative values). A pulse of $0.20\,\text{A}$ goes through.
**Find:** the force on the coil.

**Step 1 — the force.** With $\theta = 90°$, $\sin\theta = 1$:

$$F = BIL = (0.50)(0.20)(2.0) = 0.20\,\text{N}$$

**Step 2 — picture it.** That is about the weight of a $20\,\text{g}$ object — two or three coins resting in your palm.

**Step 3 — why you feel it as a *tap*.** The moving mass inside is only a couple of grams, so a fifth of a newton throws it at roughly ten times the acceleration of gravity. It reaches the end of its travel almost instantly, and the whole controller feels the jolt.

**Sanity check:** you can push a controller around with a couple of coins' worth of force, but you certainly notice it arriving all at once — which is exactly what a haptic module is for.

## Where the picture breaks

$F = BIL$ is written for one straight wire in a uniform field, and the module has neither. Its coil is many short turns and the magnet's field bulges and weakens near the edges. Treating it as "$2.0\,\text{m}$ of wire at $0.50\,\text{T}$" works only because a flat coil facing a flat magnet has most of its wire running the same way through much the same field; the honest calculation adds up the pieces separately.

Newton's third law is also hiding in the story. The magnet pushes the coil, so the coil pushes the magnet just as hard. In the real module one of the two is fixed to the case and the other rides on springs, and what you feel is them shoving against each other.

And a steady current would be useless here. Hold the current on and the mass simply sits held against its springs. The tap comes from the current being switched and reversed — which is why the left grip's spinning weight gives a dull rumble, while this one can deliver a single crisp click.

## Key takeaway

A current-carrying wire in a magnetic field feels a force, because every drifting charge in it feels one: $\vec{F} = I\,(\vec{L}\times\vec{B})$, of size $F = BIL\sin\theta$. It is perpendicular to both the wire and the field, largest when they are at right angles, zero when the wire lies along the field — and it reverses when the current does.
