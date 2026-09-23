---
concept_id: force_on_current_conductor
interest: cricket
format: explain
title: The loudspeaker on the pole has no motor
check:
  question: |-
    A straight horizontal wire carries a current from south to north. It sits in a uniform magnetic field that points vertically **downwards**. In which direction is the force on the wire?
  options:
    A: |-
      Towards the west
    B: |-
      Towards the east
    C: |-
      Vertically upwards, opposite to the field
    D: |-
      Towards the north, along the current
  answer: A
  explanation: |-
    Use $\vec{F} = I\vec{L} \times \vec{B}$: point the right fingers north along the current, curl them downwards into the field, and the thumb points west.
  misconceptions:
    B: |-
      Gets the right-hand rule backwards — usually by using the left hand, or by curling from $\vec{B}$ to $\vec{L}$ instead of $\vec{L}$ to $\vec{B}$. Either mistake reverses every answer.
    C: |-
      Thinks the force lies along the field line (pushing the wire "up the field"). The force is perpendicular to *both* the current and the field, never along either.
    D: |-
      Treats the magnetic force like an electric one, which does push a charge along the field. A magnetic force on a current is always sideways to the current.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground with an electric roller, a compass lying on a thick power cable, a bowling machine and a loudspeaker on a pole](scenes/cricket/moving_charges_magnetism.svg "The horn speaker on the pole turns a current into a push, thousands of times a second.")

The loudspeaker on the corner pole has been crackling all season, and on finals day it dies completely in the middle of the toss. Nandini, who scores for the club and reads out the batting order, is furious.

The electrician brings the old one down and opens it on the boundary rope. Nandini expects machinery. Instead there is a stiff paper cone, a heavy ring of black magnet, and a small cylinder of wire wound tight — the coil, its two thin ends soldered to the speaker wire. That is all. Nothing turns. Nothing pumps. There is no motor of any kind.

Yet this thing has been shouting across a field for years, pushing air hard enough to be heard at the far sightscreen. A current goes in; a cone moves out and back. Where does the *push* come from?

## The physics

You already know that a magnetic field pushes a single moving charge sideways. A current is simply an enormous number of charges moving together, held inside a wire — so the sideways pushes on all of them add up and act on the wire itself.

For a straight conductor of length $L$ carrying a current $I$ in a uniform field $\vec{B}$:

$$\vec{F} = I\,\vec{L} \times \vec{B} \qquad\text{so}\qquad F = BIL\sin\theta$$

where $\vec{L}$ points along the conventional current and $\theta$ is the angle between the wire and the field.

![A straight wire carrying current across a field into the page, with the force upwards; and the same wire tilted at an angle theta to the field, giving F = BIL sin θ](figures/force_on_current_conductor/force-on-current-wire.svg "Only the part of the wire across the field counts: the force is greatest at 90° and vanishes when the wire lies along B.")

Where does that come from? If each charge carrier has charge $q$ and drifts at speed $v_d$, the force on one is $qv_dB$. A length $L$ of wire of cross-section $A$ holds $nAL$ carriers, so the total is $nALqv_dB$ — and since the current is $I = nAqv_d$, that whole clump collapses to $F = BIL$.

Three things to hold on to:

- **Direction:** right fingers along the current, curl into $\vec{B}$, thumb gives $\vec{F}$. The force is perpendicular to both.
- **A wire lying along the field feels no force at all** ($\sin 0° = 0$), and the force is largest when the wire is at right angles to the field.
- The formula as written assumes a **straight** wire in a **uniform** field over its whole length.

In the speaker, the magnet's field points radially outwards through the coil, and the coil's turns run around the cylinder — so the current is everywhere at right angles to the field, and every part of the coil is pushed the *same* way: along the axis. Send the current one way and the cone goes out; reverse it and the cone comes back. An audio signal reverses it thousands of times a second, and the cone shoves the air into Nandini's announcement.

## Worked example

**Given:** a speaker coil sits in a radial field of $0.50\,\text{T}$, carries a current of $2.0\,\text{A}$, and has a total of $4.0\,\text{m}$ of wire inside the field.
**Find:** the force driving the cone.

The field is radial, so the current is at right angles to it everywhere: $\sin\theta = 1$ and $F = BIL$.

$$F = (0.50)(2.0)(4.0) = 4.0\,\text{N}$$

That is the weight of about $0.4\,\text{kg}$ — roughly two and a half cricket balls resting in your hand, delivered to a cone that weighs a few grams.

**Sanity check:** a light cone driven by the weight of a couple of cricket balls should move sharply, which is exactly what a loudspeaker has to do.

## Where the picture breaks

The diagram shows a straight wire in a uniform field, and a loudspeaker coil is neither: it is a coil, in a field that points outwards in every direction. The reason the simple formula still works is the special design — the field is radial *so that* every turn is at right angles to it. Put the same coil in an ordinary left-to-right field and the two sides would be pushed opposite ways, and it would twist instead of moving (which is the next lesson but one).

Two idealisations are also hiding in $F = BIL$. The field is taken as the same all along the wire, and the wire as perfectly straight. Near the edges of a real magnet both fail, and you would have to add up the force piece by piece.

And the loudspeaker is only the setting here, not an analogy: there is no likeness between sound and magnetism to lean on. The physics is happening in the device itself.

## Key takeaway

A magnetic field pushes a current-carrying wire sideways, because it pushes each moving charge inside it: $\vec{F} = I\vec{L} \times \vec{B}$, with magnitude $F = BIL\sin\theta$. The push is perpendicular to both the wire and the field, largest at $90°$, and zero when the wire lies along the field.
