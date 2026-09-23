---
concept_id: magnetic_force_on_charge
interest: football
format: explain
title: The speaker that bent the video analysis
check:
  question: |-
    Inside the old tube monitor the electron beam travels horizontally towards the screen, which faces you as you look north. A stray magnetic field there points vertically upwards. Which way is the beam pushed, and what happens to the electrons' speed?
  options:
    A: |-
      Towards the east, with no change in speed
    B: |-
      Towards the west, and the electrons are slowed down
    C: |-
      Towards the west, with no change in speed
    D: |-
      Vertically upwards along the field, with no change in speed
  answer: C
  explanation: |-
    For the velocity north and $\vec{B}$ up, $\vec{v} \times \vec{B}$ points east — but the electron's charge is negative, so the force is the other way, towards the west. The force stays perpendicular to $\vec{v}$, so it does no work and the speed is unchanged.
  misconceptions:
    A: |-
      Applies the right-hand rule to $\vec{v} \times \vec{B}$ and stops there, forgetting that $q$ is negative for an electron and reverses the force.
    B: |-
      Thinks a sideways magnetic force drains the particle's energy, as friction would. A force at right angles to the motion does no work, so the speed cannot change.
    D: |-
      Thinks the force acts along $\vec{B}$, pulling the charge the way the field points. The force is perpendicular to *both* $\vec{v}$ and $\vec{B}$, and vanishes when they are parallel.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground with a coil traced around the goal frame, a pop-up sprinkler on a solenoid valve, an electric line-marking machine and a horn speaker on a pole with a compass lying on its supply cable](scenes/football/moving_charges_magnetism.svg "The speaker on the pole holds a heavy magnet — and a magnet near a moving charge is never harmless.")

The video-analysis room at Neha's academy is a store cupboard with a fan in it. On the shelf sits a monitor old enough to be deep from front to back, and on it the coach replays the same twenty seconds of her overlapping run until she can recite it.

One afternoon the kit-room speaker is parked on the shelf beside the monitor while somebody rewires the dugout. The moment it lands there, the picture goes wrong — the touchline bows outwards, the goalposts lean, and colours bleed out along one edge of the screen. Nothing has been dropped or unplugged.

Neha lifts the speaker away and the picture snaps back straight. She slides it closer; the pitch bends again, and always the same way.

The speaker is not even switched on. Whatever is doing this needs no current of its own — so what is it reaching inside a sealed glass tube to push?

## The physics

A speaker contains a heavy permanent magnet, and a tube monitor draws its picture by firing **electrons** down a vacuum tube at the screen. Electrons are charges in motion, and that is all a magnetic field needs.

> A charge $q$ moving with velocity $\vec{v}$ through a magnetic field $\vec{B}$ feels a force
> $$\vec{F} = q\,\vec{v} \times \vec{B}, \qquad F = qvB\sin\theta$$
> where $\theta$ is the angle between $\vec{v}$ and $\vec{B}$.

![A positive charge moving to the right in a field into the page, pushed upwards; a negative charge pushed downwards; and a charge moving along B feeling no force at all](figures/magnetic_force_on_charge/force-on-moving-charge.svg "The force is at right angles to both v and B — reversed for a negative charge, and zero for a charge moving along the field.")

Read four things off that one line, because every later idea in this chapter is built on them.

- **Direction.** Point the fingers of your right hand along $\vec{v}$, curl them towards $\vec{B}$, and the thumb gives $\vec{v} \times \vec{B}$. For a **negative** charge such as an electron, the force is the opposite way.
- **It needs motion.** A charge sitting still feels nothing: $v = 0$ gives $F = 0$. An electric field would push it anyway; a magnetic field will not.
- **It vanishes along the field.** If $\vec{v}$ is parallel to $\vec{B}$, $\sin\theta = 0$ and there is no force. The force is largest when the charge cuts straight across the field, at $\theta = 90°$.
- **It does no work.** $\vec{F}$ is always perpendicular to $\vec{v}$, so it changes the *direction* of the velocity and never its size. A magnetic field can steer a charge; it can never speed it up or slow it down.

That last point is the whole reason Neha's picture bends instead of dimming. The electrons still arrive with the energy they left with — they just arrive in the wrong place.

The unit of $\vec{B}$ follows from the same equation. A field of **one tesla** exerts one newton on a charge of one coulomb crossing it at one metre per second: $1\,\text{T} = 1\,\text{N}\,\text{A}^{-1}\,\text{m}^{-1}$. A tesla is a big field — the stray field beside a speaker magnet is a thousand times smaller.

## Worked example

**Given:** an electron in the tube ($q = 1.6 \times 10^{-19}\,\text{C}$ in size) travels north towards the screen at $3.0 \times 10^{7}\,\text{m/s}$, straight across a stray field of $1.0\,\text{mT} = 1.0 \times 10^{-3}\,\text{T}$ pointing vertically upwards.
**Find:** the size and direction of the magnetic force on it.

**Step 1 — the size.** The motion is perpendicular to the field, so $\sin\theta = 1$ and

$$F = qvB = (1.6 \times 10^{-19})(3.0 \times 10^{7})(1.0 \times 10^{-3}) \approx 4.8 \times 10^{-15}\,\text{N}$$

**Step 2 — the direction.** Fingers north along $\vec{v}$, curl them upwards towards $\vec{B}$: the thumb points east. The electron is negative, so the push is the other way — **west**, sideways across the beam. That sideways shift is the bowed touchline.

**Sanity check:** the electron's own weight is about $10^{-29}\,\text{N}$, so this push is more than a million billion times stronger than gravity. A force that dwarfs gravity so completely, on something as light as an electron, is exactly why a speaker left on the wrong shelf wrecks a picture.

## Where the picture breaks

A speaker magnet is not a neat uniform field. Its strength and direction change across the width of the tube, so different parts of the picture are pushed by different amounts — which is why the image *distorts* rather than sliding sideways in one piece.

The colour fringing has a second cause the equation above does not cover: the magnet also magnetises the steel mask inside the tube, and that stays magnetised after the speaker is carried away. Tube monitors have a degaussing coil to undo it.

And none of this happens to a flat screen. There is no beam of free electrons crossing empty space in one, so there is nothing for the field to bend.

## Key takeaway

A magnetic field pushes a charge only while it *moves*, only if the motion is not along the field, and always at right angles to both: $\vec{F} = q\,\vec{v} \times \vec{B}$, of size $qvB\sin\theta$. Because the force is perpendicular to the velocity it does no work — a magnetic field steers a charge but never changes its speed.
