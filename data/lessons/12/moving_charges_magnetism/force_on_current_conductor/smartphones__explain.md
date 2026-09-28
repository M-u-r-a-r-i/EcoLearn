---
concept_id: force_on_current_conductor
interest: smartphones
format: explain
title: What actually pushes your phone's speaker
check:
  question: |-
    At a phone repair bench, a straight $5.0\,\text{cm}$ length of wire carrying $2.0\,\text{A}$ lies between two magnets, in a uniform field of $0.20\,\text{T}$. The wire makes an angle of $30^\circ$ with the field. What is the size of the magnetic force on it?
  options:
    A: |-
      $0.010\,\text{N}$
    B: |-
      $0.020\,\text{N}$
    C: |-
      $0.017\,\text{N}$
    D: |-
      $1.0\,\text{N}$
  answer: A
  explanation: |-
    $F = BIL\sin\theta = (0.20)(2.0)(0.050)(\sin 30^\circ) = 0.020\times0.5 = 0.010\,\text{N}$. Only the component of the wire perpendicular to $\vec{B}$ feels a force.
  misconceptions:
    B: |-
      Ignores the angle and uses $F = BIL$, which applies only when the wire is at right angles to the field. At $30^\circ$ the force is half of that.
    C: |-
      Uses $\cos 30^\circ$ instead of $\sin 30^\circ$. The part of the wire *along* the field feels no force; what counts is the part across it, $L\sin\theta$.
    D: |-
      Forgets to convert centimetres to metres and puts $L = 5.0$ into the formula. The length must be in metres, $0.050\,\text{m}$, for the force to come out in newtons.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk with a phone lying on a charging cable showing a swung compass arrow, a wireless charging pad with its coil exposed, a flip-cover case with a small magnet in its flap, and a speaker and a small cylinder-shaped vibration motor taken apart](scenes/smartphones/moving_charges_magnetism.svg "Bottom right: a phone speaker taken apart. A ring magnet, a thin coil of wire sitting in a narrow gap, and a paper-thin membrane glued to the coil.")

Rohan's phone started buzzing whenever he played music, so he bought a tiny replacement speaker online for forty rupees and fixed it himself. The old one now sits on his desk in pieces.

His friend Sana picks through the parts. There's a small, surprisingly strong ring magnet. There's a coil of copper wire finer than a hair, wound into a little cylinder no bigger than a pencil eraser. And there's a paper-thin membrane glued onto the end of that coil. No motor, no gears, nothing that turns.

Sana drops the coil back into the narrow gap of the magnet, touches its two wires to a small cell, and the membrane gives a sharp tick and jumps. Reverse the wires: another tick, the other way.

The magnet doesn't move. The coil isn't a magnet. Yet the moment current flows, something shoves the coil. What is doing the shoving — and how hard?

## The physics

A current in a wire is a stream of moving charges, and a magnetic field pushes on every one of them ($\vec{F} = q\,\vec{v}\times\vec{B}$ for each). Those tiny pushes are passed on to the wire itself. Adding them up for a straight wire of length $L$ carrying current $I$ in a uniform field gives

$$\vec{F} = I\,\vec{L}\times\vec{B}, \qquad F = BIL\sin\theta$$

where $\vec{L}$ has the length of the wire and points along the current, and $\theta$ is the angle between the wire and the field. With $B$ in tesla, $I$ in amperes and $L$ in metres, $F$ is in newtons.

- The force is **largest**, $BIL$, when the wire is at right angles to the field.
- It is **zero** when the wire lies along the field.
- It is **perpendicular to both** the wire and the field. The right-hand rule for $\vec{L}\times\vec{B}$ (or **Fleming's left-hand rule**) gives its direction, and reversing the current reverses it.

![A straight wire of length L carrying current I in a uniform field into the page, with the force upward and equal to BIL; below, the wire tilted at an angle so only the perpendicular part counts](figures/force_on_current_conductor/force-on-current-wire.svg "Across the field, the full force BIL. Tilted, only the part of the wire perpendicular to B counts — that is where the sin θ comes from.")

In the speaker, the magnet's field in the gap points **radially** — straight outwards from the centre, all the way round. The coil's wire runs round in circles, so every bit of it is at right angles to the field. For every bit of wire, the force points along the axis of the coil. They all add up, and the whole coil is pushed along its axis, carrying the membrane with it. Music is a current that keeps changing direction and size, so the coil is pushed back and forth in step with it — and the membrane pushes the air.

## Worked example

**Given:** the speaker's coil has about $L = 1.0\,\text{m}$ of wire in the gap in total (a few dozen small turns). The field there is $B = 1.0\,\text{T}$, and the current at one instant is $I = 0.10\,\text{A}$ (illustrative values).
**Find:** the force on the coil at that instant.

**Step 1 — check the angle.** Every bit of wire runs round the coil, and the field points straight outwards across it, so $\theta = 90^\circ$ everywhere and $\sin\theta = 1$.

**Step 2 — the force.**

$$F = BIL = (1.0)(0.10)(1.0) = 0.10\,\text{N}$$

That is about the weight of a $10\,\text{g}$ object — say, a small AAA cell resting on your palm. For a membrane lighter than a feather, that is an enormous shove.

**Step 3 — what the direction does.** When the current reverses, the force reverses: $0.10\,\text{N}$ the other way. A current alternating a thousand times a second pushes the membrane back and forth a thousand times a second, and you hear a note.

**Sanity check:** doubling the current doubles the push — which is why turning up the volume, which increases the current, makes the membrane swing further and the sound louder.

## Where the picture breaks

The formula is for a **straight** wire in a **uniform** field. A speaker's coil is circular, and its field only points neatly outwards inside the narrow gap. It works because the design makes $\theta = 90^\circ$ at every bit of the wire — the lengths of all the small straight pieces just add up.

The force also doesn't settle the motion by itself. The membrane is held by a springy suspension and pushes against the air, so how far it moves depends on those too. And a moving coil in a magnet makes a voltage of its own, which pushes back on the current — you will meet that in electromagnetic induction.

## Key takeaway

A current-carrying wire in a magnetic field feels a force $\vec{F} = I\,\vec{L}\times\vec{B}$, of size $F = BIL\sin\theta$: biggest across the field, zero along it, perpendicular to both, and reversed when the current reverses. Every phone speaker is this force at work — a coil in a magnet's gap, pushed back and forth by a changing current.
