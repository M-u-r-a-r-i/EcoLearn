---
concept_id: motional_emf
interest: football
format: explain
title: The camera trolley that makes its own voltage
check:
  question: |-
    A straight metal rod of length $0.5\,\text{m}$ slides along horizontal rails at $3\,\text{m/s}$, in a uniform field of $0.4\,\text{T}$ perpendicular to the plane of the rails. What emf is induced across the rod?
  options:
    A: |-
      $0.06\,\text{V}$
    B: |-
      $0.6\,\text{V}$
    C: |-
      $0.2\,\text{V}$
    D: |-
      $1.5\,\text{V}$
  answer: B
  explanation: |-
    With $B$, $l$ and $v$ mutually perpendicular, $\varepsilon = Blv = 0.4 \times 0.5 \times 3 = 0.6\,\text{V}$.
  misconceptions:
    A: |-
      The right method with a decimal slip of a factor of ten — worth redoing as $(0.4 \times 0.5) \times 3$ and checking the size before answering.
    C: |-
      Works out $Bl$ and stops, as though a rod merely lying in a field had an emf across it. A stationary rod gives exactly zero.
    D: |-
      Multiplies $l \times v$ and leaves out $B$. With no field there is no magnetic force on the moving charges, so nothing separates them and there is no emf at all.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening football training ground with a contactless card reader at the turnstile, a magnetic-brake training bike on the touchline and a floodlight transformer cabinet](scenes/football/electromagnetic_induction.svg "Three machines around one ground. This lesson is about the simplest generator there is: one metal bar, moving.")

The club films training from a camera trolley that runs on two long metal rails laid along the touchline. Imran is the one who pushes it, and today he is bored, because the session is all stretching.

He has a multimeter in his bag for a school project. He clips one lead to each rail, sets it to its most sensitive voltage range, and watches it read a flat zero.

Then he walks the trolley towards the goal. The reading lifts to about a tenth of a millivolt and holds there while he walks. He stops: back to zero. He parks the trolley at the halfway line and waits: zero. He parks it by the corner flag: zero. He walks it back the other way — and the reading appears again, with a **minus sign** in front of it.

There is no battery anywhere in this circuit. There are two rails, one metal trolley frame and a bored teenager. Where is the voltage coming from, and why does the direction he walks decide its sign?

## The physics

The trolley frame is a conducting bar bridging two rails, and the whole loop sits in the Earth's magnetic field. Push the bar along and the *area* of the loop changes, so the flux changes, so Faraday's law gives an emf. This particular case has its own name: **motional emf**.

![A conducting rod sliding along two rails in a field into the page, with the magnetic force pushing positive charges up the rod and a current flowing round the circuit](figures/motional_emf/rod-on-rails.svg "The rod is the battery: the magnetic force on the charges inside it pushes them to one end, and that separation of charge is the emf.")

There are two ways to see where it comes from, and they agree.

**From the charges.** Every free charge $q$ in the rod is carried along at speed $v$, so it feels a magnetic force $F = qvB$ (for $\vec{v}$ perpendicular to $\vec{B}$), directed along the rod. Positive charge collects at one end and negative at the other. Pushing a charge the full length $l$ takes work $W = qvB \times l$, and emf means work per unit charge:

$$\varepsilon = Blv$$

**From Faraday's law.** In a time $\Delta t$ the rod sweeps out an extra area $\Delta A = l\,v\,\Delta t$, so $\Delta\Phi_B = Blv\,\Delta t$ and $|\varepsilon| = \Delta\Phi_B/\Delta t = Blv$. Same answer, different route.

The formula holds when $\vec{B}$, the rod $l$ and the velocity $\vec{v}$ are **mutually perpendicular** and $B$ is uniform. Tilt the velocity and only the component perpendicular to $\vec{B}$ counts.

Imran's minus sign is now easy. Reverse $\vec{v}$ and the force $q\vec{v}\times\vec{B}$ on every charge reverses, so the charge piles up at the other end and the emf changes sign. Position never mattered — only motion does, and its direction sets the sign.

One more thing. Join the rails through a resistance and a current flows; that current sits in the field, so the rod feels a force opposing its motion. That is Lenz's law again, and it is why a generator gets harder to turn the moment you switch on the load.

## Worked example

**Given:** the rails are $l = 1.0\,\text{m}$ apart, Imran walks the trolley at $v = 2.0\,\text{m/s}$, and the part of the Earth's field perpendicular to the loop is about $B = 5\times10^{-5}\,\text{T}$.
**Find:** the emf across the trolley frame.

First combine the two quantities that never change while he walks:

$$Bl = 5\times10^{-5} \times 1.0 = 5\times10^{-5}\,\text{T}\,\text{m}$$

That is the emf he would get at one metre per second — fifty microvolts, which is already close to nothing.

Walking at two metres per second doubles it:

$$\varepsilon = Blv = 5\times10^{-5} \times 2.0 = 1\times10^{-4}\,\text{V}$$

A tenth of a millivolt — ten thousand times smaller than a torch cell, and exactly the sort of reading that needs a sensitive meter to see at all.

**Sanity check:** the units multiply out as $\text{T} \times \text{m} \times \text{m/s} = \text{V}$, and the Earth's field is feeble, so microvolts rather than volts is the size to expect.

## Where the picture breaks

The rails-and-rod diagram is an idealisation. Real rails have resistance, the trolley wheels make patchy contact, and at a reading this small the contact voltages at Imran's crocodile clips could easily be as large as the effect he is measuring — a careful experimenter would not trust the number without swapping the leads over.

Only the component of the Earth's field **perpendicular to the plane of the loop** counts, and that depends on where on the planet the ground is and which way the rails run. Lay the same rails on a vertical wall and the reading would change.

And the football here is the setting, not an analogy. A camera track is simply two long parallel conductors, which is exactly the geometry this physics needs.

## Key takeaway

A conductor of length $l$ moving at speed $v$ across a magnetic field $B$, all three mutually perpendicular, is a source of emf $\varepsilon = Blv$. The magnetic force on the moving charges is what separates them, the direction of motion sets the sign, and the moment the motion stops the emf vanishes.
