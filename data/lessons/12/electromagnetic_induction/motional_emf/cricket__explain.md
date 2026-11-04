---
concept_id: motional_emf
interest: cricket
format: explain
title: A voltmeter on the sightscreen rails
check:
  question: |-
    A straight metal rod of length $0.5\,\text{m}$ slides along horizontal rails at $4\,\text{m/s}$, in a magnetic field of $0.5\,\text{T}$ perpendicular to the plane of the rails. What emf is induced across the rod?
  options:
    A: |-
      $2.0\,\text{V}$
    B: |-
      $0.25\,\text{V}$
    C: |-
      $4.0\,\text{V}$
    D: |-
      $1.0\,\text{V}$
  answer: D
  explanation: |-
    With $B$, $l$ and $v$ mutually perpendicular, $\varepsilon = Blv = 0.5 \times 0.5 \times 4 = 1.0\,\text{V}$.
  misconceptions:
    A: |-
      Multiplies $l \times v$ and leaves out $B$ — but without a field there is no magnetic force on the charges, so no emf at all.
    B: |-
      Multiplies $B \times l$ and ignores the speed, as if a rod merely sitting in a field had an emf across it. A stationary rod gives zero.
    C: |-
      Divides by $B$ instead of multiplying. Check the units: $l v / B$ does not come out in volts.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening cricket ground with a walk-through metal-detector arch at the gate, LED bails charging on a pad, and a bowling machine](scenes/cricket/electromagnetic_induction.svg "Three machines at one ground. Here we look at the simplest generator there is: one metal bar, moving.")

Rain has stopped play, the covers are on, and Farhan is bored enough to do something odd. The sightscreen at the far end rolls on two long steel rails, and Farhan has clipped his multimeter — one lead to each rail — and set it to its most sensitive voltage range.

"Push it," he tells Meher.

Meher leans into the sightscreen and walks it along the rails. The meter, which was reading a flat zero, flickers up to a few tens of microvolts and stays there while she pushes. She stops. It drops back to zero. She pushes the other way. It flickers the other way.

There is no battery anywhere in this circuit. There are two rails, one metal frame and a bored teenager with a meter. Where is the voltage coming from?

## The physics

The sightscreen frame is a conducting bar bridging two rails, and the whole loop sits in Earth's magnetic field. Push the bar and you change the area of the loop — so the flux changes, and by Faraday's law there is an emf. This special case has its own name: **motional emf**.

![A conducting rod sliding along two rails in a field into the page, with the magnetic force pushing positive charges up the rod and a current flowing round the circuit](figures/motional_emf/rod-on-rails.svg "The rod is the battery: the magnetic force pushes positive charges to one end, and that separation of charge is the emf.")

There are two ways to see where it comes from, and they agree.

**From the charges.** Every free charge $q$ inside the rod is carried along at speed $v$, so it feels a magnetic force $F = qvB$ (for $\vec{v}$ perpendicular to $\vec{B}$), directed along the rod. Positive charge piles up at one end, negative at the other. Moving a charge the whole length $l$ takes work $W = qvB \times l$, so the work done per unit charge — which is what emf means — is

$$\varepsilon = Blv$$

**From Faraday's law.** In a time $\Delta t$ the rod sweeps out extra area $\Delta A = l\,v\,\Delta t$, so the flux changes by $\Delta\Phi_B = B l v \Delta t$ and $|\varepsilon| = \Delta\Phi_B/\Delta t = Blv$. Same answer.

The formula $\varepsilon = Blv$ holds when $\vec{B}$, the rod $l$ and the velocity $\vec{v}$ are **mutually perpendicular** and $B$ is uniform. Tilt the velocity and only the perpendicular component counts.

If the rails are joined through a resistance, a current flows — and then Lenz's law bites: the current in the rod sits in the field, so the rod feels a force opposing its motion. That is why Meher has to keep pushing.

## Worked example

**Given:** a rod $l = 0.5\,\text{m}$ long (about half a bat) slides on rails at $v = 6\,\text{m/s}$ — a brisk run — in a uniform field $B = 0.2\,\text{T}$ perpendicular to the loop.
**Find:** the emf induced across the rod.

The three quantities are mutually perpendicular, so

$$\varepsilon = Blv = 0.2 \times 0.5 \times 6$$

Take it in one step at a time. First $Bl = 0.2 \times 0.5 = 0.1\,\text{T}\,\text{m}$ — that is the emf you would get at one metre per second.

Running at six metres per second multiplies it by six:

$$\varepsilon = 0.1 \times 6 = 0.6\,\text{V}$$

About the voltage of a small cell — from nothing but a metal bar being pushed.

**Sanity check:** the units work out, since $\text{T}\times\text{m}\times\text{m/s} = \text{V}$, and a strong lab magnet with a fast-moving rod giving something under a volt is the right size.

## Where the picture breaks

The worked example uses a lab magnet. On Farhan's sightscreen the field is Earth's, which is about ten thousand times weaker — that is why the meter reads microvolts, not volts, and why you need a sensitive instrument to see anything at all. The number he saw was small enough that contact resistance at the clips and stray voltages could easily have been part of it.

The rails-and-rod picture also idealises: real rails have resistance, the frame does not make perfect contact, and only the component of Earth's field perpendicular to the loop counts, which varies with the ground's orientation.

And the cricket is the setting, not an analogy — the sightscreen track happens to be two long parallel conductors, which is exactly the geometry this physics needs.

## Key takeaway

A conductor of length $l$ moving with speed $v$ across a magnetic field $B$, all three mutually perpendicular, acts as a source of emf $\varepsilon = Blv$. The magnetic force on the moving charges is what separates them. Stop the motion and the emf disappears instantly.
