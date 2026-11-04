---
concept_id: magnetic_force_on_charge
interest: cricket
format: explain
title: The fridge magnet that bent the picture
check:
  question: |-
    An electron and a proton are fired into the same uniform magnetic field with the same speed, both moving at right angles to the field. How do the magnetic forces on them compare in size?
  options:
    A: |-
      The force on the proton is larger, because the proton has far more mass.
    B: |-
      The forces are equal in size and opposite in direction.
    C: |-
      The force on the electron is larger, because a negative charge is repelled by a magnetic field.
    D: |-
      The force on the proton is larger, because the field pushes positive charges harder than negative ones.
  answer: B
  explanation: |-
    The magnitude is $F = |q|vB\sin\theta$. The two particles have the same speed, the same angle and the same size of charge, so the forces are equal in size; the opposite signs of $q$ flip the direction.
  misconceptions:
    A: |-
      Thinks mass belongs in the force. It doesn't — there is no $m$ in $F = qvB\sin\theta$. Mass decides the *acceleration* that follows, not the force.
    C: |-
      Treats a magnetic field like a charged object that attracts or repels by sign. A magnetic field does not repel charges at all; it pushes them sideways, along $\vec{v} \times \vec{B}$.
    D: |-
      Thinks the sign of the charge changes the size of the force. Only the magnitude $|q|$ enters, and that is the same for an electron and a proton.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground with an electric roller, a compass lying on a thick power cable, a bowling machine and a loudspeaker on a pole](scenes/cricket/moving_charges_magnetism.svg "Every machine on this ground works because a current makes a magnetic field — and because a magnetic field pushes moving charges.")

Rain has stopped play, so the whole club is crowded into the pavilion watching the coverage on the old tube television that has been bolted to the corner shelf for twenty years.

Zoya's younger brother, bored, peels a fridge magnet off the canteen noticeboard and presses it against the glass. The bottom corner of the picture bulges. The fielders stretch sideways and turn a sickly green. He slides the magnet across and the smear follows it like a shadow.

The groundsman snatches it away before anyone can blame him for the television as well. But Zoya has stopped watching the cricket.

Nothing touched the picture. The magnet was on the outside of thick glass, and it is not even switched on to anything. So how did it reach inside and shove the image around?

## The physics

The picture in that television is painted by a beam of **electrons** fired from the back of the tube at the screen. They are charges, and they are moving — and that is all a magnetic field needs.

> A charge $q$ moving with velocity $\vec{v}$ through a magnetic field $\vec{B}$ feels a force

$$\vec{F} = q\,\vec{v} \times \vec{B}$$

Its magnitude is

$$F = |q|\,v\,B\sin\theta$$

where $\theta$ is the angle between $\vec{v}$ and $\vec{B}$. The unit of $B$ is the **tesla**, and $1\,\text{T} = 1\,\text{N}/(\text{A}\,\text{m})$.

![A positive charge moving to the right in a field into the page, pushed upwards; a negative charge pushed downwards; and a charge moving along B feeling no force at all](figures/magnetic_force_on_charge/force-on-moving-charge.svg "The force is at right angles to both v and B — and vanishes when the charge moves along the field.")

Three features of this force are worth more than the formula itself:

- **It is sideways.** $\vec{F}$ is perpendicular to $\vec{v}$ *and* to $\vec{B}$. Use the right hand for $\vec{v} \times \vec{B}$: fingers along $\vec{v}$, curl them towards $\vec{B}$, thumb gives the direction — then **reverse it** for a negative charge such as an electron.
- **A charge at rest feels nothing**, and neither does one moving straight along the field ($\sin 0° = 0$). Only the part of the velocity across the field counts.
- **It can never change the speed.** Because $\vec{F}$ is always perpendicular to $\vec{v}$, it does no work. It steers; it does not accelerate the particle along its path.

That last point is the answer to Zoya's question. The magnet does not slow the electrons or add energy to them. It simply steers them, so each electron lands on a slightly wrong part of the screen.

## Worked example

**Given:** an electron crosses the tube to the right at $2.0 \times 10^{7}\,\text{m/s}$, through a stray field of $5.0 \times 10^{-4}\,\text{T}$ pointing into the page (at right angles to its motion).
**Find:** the size and direction of the magnetic force on it.

**Step 1 — the size.** With $\theta = 90°$, $\sin\theta = 1$, so $F = |q|vB$:

$$F = (1.6 \times 10^{-19}) \times (2.0 \times 10^{7}) \times (5.0 \times 10^{-4}) = 1.6 \times 10^{-15}\,\text{N}$$

That is the whole push the electron gets, sideways, for as long as it is in the field.

**Step 2 — the direction.** Point your right fingers to the right along $\vec{v}$ and curl them into the page along $\vec{B}$: the thumb points **up**. That is for a positive charge. The electron is negative, so its force is **downwards** — and the spot it was heading for lands lower than it should.

**Sanity check:** a force of $10^{-15}\,\text{N}$ would not stir a grain of dust, but an electron is lighter still by a huge margin, so a nudge like this easily bends its path over the last few centimetres of the tube.

## Where the picture breaks

The television is not a victim of magnetism — it *runs* on it. The picture is scanned across the screen by deflection coils that do this deliberately, thousands of times a second. The fridge magnet only adds an unwanted extra field on top.

The colour smear is one step beyond this lesson: a colour tube has three beams that must hit three different coloured dots, and pushing them sideways makes each land on the wrong dot. Some of that damage lingers, because the steel mask inside the tube becomes slightly magnetised and has to be demagnetised.

And the trick fails completely on the flat screen in the new clubhouse. An LCD panel has no beam of moving charge crossing it — no moving charge, no magnetic force, no smear.

## Key takeaway

A magnetic field pushes a charge only while the charge is moving, and pushes it *sideways*: $\vec{F} = q\vec{v} \times \vec{B}$, with magnitude $F = |q|vB\sin\theta$. The force is zero when $\vec{v}$ is along $\vec{B}$, and because it is always perpendicular to the velocity it changes the direction of motion but never the speed.
