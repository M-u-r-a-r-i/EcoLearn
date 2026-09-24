---
concept_id: magnetic_force_on_charge
interest: gaming
format: explain
title: The thumbstick that never touches anything
check:
  question: |-
    In a stick sensor the charge carriers move east across the chip while the magnet's field points straight up, and each carrier feels a sideways magnetic force. The magnet is now turned so that its field at the chip points **east as well**, along the carriers' motion. What happens to the magnetic force on each carrier?
  options:
    A: |-
      It doubles, because $\vec{v}$ and $\vec{B}$ now line up.
    B: |-
      It stays the same, because the field is just as strong as before.
    C: |-
      It falls to zero, because only a part of $\vec{B}$ across the motion can push a moving charge.
    D: |-
      It keeps the same size but reverses direction.
  answer: C
  explanation: |-
    $F = qvB\sin\theta$, and $\theta$ is now $0°$. A charge moving straight along the field lines feels no magnetic force at all — the force needs $\vec{B}$ to have a component perpendicular to $\vec{v}$.
  misconceptions:
    A: |-
      Thinks the force is biggest when $\vec{v}$ and $\vec{B}$ are parallel. That is how a dot product behaves; the cross product $\vec{v}\times\vec{B}$ is *zero* for parallel vectors and largest when they are perpendicular.
    B: |-
      Treats the magnetic force like the electric one, $F = qE$, where only the size of the field matters. The magnetic force also depends on how fast the charge moves and on the angle between $\vec{v}$ and $\vec{B}$.
    D: |-
      Remembers correctly that reversing $\vec{v}$, or the sign of $q$, flips the force — and then applies that to swinging $\vec{B}$ into line with $\vec{v}$, which switches the force off rather than flipping it.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming workbench with a bartop arcade cabinet, a cutaway of a pinball flipper coil, a controller with its shell off showing a magnet and a sensor chip under the thumbstick, a PC case fan, and a phone on a power cable](scenes/gaming/moving_charges_magnetism.svg "Look at the opened controller: a magnet sitting above a chip, with nothing touching in between.")

Meher's controller has the fault every player dreads. She lets go of the stick and her character keeps drifting left, slowly and stubbornly, into a wall.

At a repair stall in the market the man offers her two replacement sticks. The cheap one is the usual kind: two little variable resistors with metal wipers scraping along a carbon track, which is exactly the thing that had worn out. The other costs more and has, he says, no contact at all.

She opens that one on the counter. Under the stick there is a magnet smaller than a grain of rice. Below it, not touching, sits a chip. Nothing rubs on anything.

Meher is pleased about the drift. She is annoyed about not understanding. She has held magnets flat against her phone screen plenty of times and nothing ever happened. So how does a chip *feel* which way a magnet is leaning?

## The physics

Because the chip is not sitting still on the inside. A current is flowing through it, and a magnetic field pushes on **moving** charge:

$$\vec{F} = q\,\vec{v}\times\vec{B}$$

Here $q$ is the charge in coulombs, $\vec{v}$ its velocity in $\text{m/s}$, and $\vec{B}$ the magnetic field in **tesla** (T). The size of the force is

$$F = qvB\sin\theta$$

where $\theta$ is the angle between $\vec{v}$ and $\vec{B}$. Four consequences carry most of the physics:

- **No motion, no force.** Put $v = 0$ and $F = 0$. A magnet held against a phone does nothing to the charges sitting in the glass — which is exactly why Meher's experiment kept coming out boring.
- **Moving along the field is the same as not moving.** If $\vec{v}$ is parallel to $\vec{B}$, $\sin\theta = 0$ and the force vanishes. The force is greatest when they are at right angles.
- **The force is sideways.** $\vec{F}$ is perpendicular to $\vec{v}$ *and* to $\vec{B}$ — never along either of them.
- **Sign matters.** For a positive charge, point the fingers of the right hand along $\vec{v}$, curl them towards $\vec{B}$, and the thumb gives $\vec{F}$. For a negative charge the force is the other way.

![A uniform magnetic field into the page, with a positive charge moving right feeling an upward force, a negative charge moving right feeling a downward force, and a charge moving along the field feeling nothing](figures/magnetic_force_on_charge/force-on-moving-charge.svg "Same field, same velocity, opposite charge: opposite force. Move along the field and there is no force at all.")

So inside the stick sensor, the carriers drifting through the chip are shoved gently to one side. They crowd along one edge and leave the other edge short, and that lopsidedness is a tiny voltage the chip can read. Tilt the stick, the magnet turns, the angle changes, the voltage changes — and the console knows where your thumb is, with nothing ever touching.

## Worked example

**Given:** the stick's magnet produces a field of about $0.10\,\text{T}$ at the chip (an illustrative value), and a charge carrier drifts across the chip at about $1.0\times10^{-3}\,\text{m/s}$, at right angles to the field. Take the carrier's charge as $1.6\times10^{-19}\,\text{C}$.
**Find:** the magnetic force on one carrier, and which way it acts.

**Step 1 — the size.** With $\theta = 90°$, $\sin\theta = 1$:

$$F = qvB = (1.6\times10^{-19})(1.0\times10^{-3})(0.10) = 1.6\times10^{-23}\,\text{N}$$

**Step 2 — the direction.** Say the carriers drift to the right across the chip and the field points straight up out of it. Fingers along $\vec{v}$ (right), curl up towards $\vec{B}$: the thumb points towards you. Positive carriers pile up on the near edge, leaving the far edge short.

**Step 3 — is that force big?** An electron weighs about $9\times10^{-30}\,\text{N}$. The magnetic push is roughly two million times its own weight.

**Sanity check:** the number looks impossibly small, but the thing it is pushing is smaller still — gravity is simply irrelevant down here, and the sideways shove wins easily.

## Where the picture breaks

The sensor's full story goes past this chapter. The moment carriers crowd onto one edge, the separated charge sets up an *electric* field that pushes back, and within an instant the two balance; the steady voltage that is left is what the chip actually measures. You will meet that balance later — here the point is only the first shove.

The numbers above are illustrative, and the drift speed genuinely is that slow. It works only because a chip holds a colossal number of carriers and needs no more than a few microvolts to make a reading.

And "no contact" describes the *sensing*, not the whole stick. The pivot still has bearings, and they still wear; what has gone is the scraping wiper that caused the drift.

One last warning about the magnet-on-the-phone experiment: nothing happens to charges at rest, but a strong magnet can still disturb parts that are magnetised already, or coils with current running in them. That is a different mechanism, later in this chapter.

## Key takeaway

A magnetic field only pushes charge that is **moving**, and only the part of the motion across the field counts: $\vec{F} = q\,\vec{v}\times\vec{B}$, with size $F = qvB\sin\theta$. The force is perpendicular to both $\vec{v}$ and $\vec{B}$, it is zero when they are parallel, and it reverses if the charge is negative.
