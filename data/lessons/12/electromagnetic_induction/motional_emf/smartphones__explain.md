---
concept_id: motional_emf
interest: smartphones
format: explain
title: How a pair of earphones can record your voice
check:
  question: |-
    In a small speaker, $4\,\text{m}$ of wire sits in a magnetic field of $0.5\,\text{T}$, with the field everywhere perpendicular to the wire. Sound pushes the wire along at $5\,\text{mm/s}$, perpendicular to both the wire and the field. What emf is induced across the wire?
  options:
    A: |-
      $10\,\text{V}$
    B: |-
      $0.01\,\text{V}$
    C: |-
      $0\,\text{V}$
    D: |-
      $400\,\text{V}$
  answer: B
  explanation: |-
    With $B$, $l$ and $v$ mutually perpendicular, $\varepsilon = Blv = 0.5 \times 4 \times 0.005 = 0.01\,\text{V}$, after converting $5\,\text{mm/s}$ to $0.005\,\text{m/s}$.
  misconceptions:
    A: |-
      Puts the speed in as $5$ instead of converting $5\,\text{mm/s}$ to $0.005\,\text{m/s}$, so the answer is a thousand times too big.
    C: |-
      Thinks an emf needs a changing magnetic field; a conductor **moving** through a steady field also has an emf, because the force $qvB$ acts on its moving charges.
    D: |-
      Divides by the speed instead of multiplying, which would mean a slower wire gives a bigger emf — the opposite of what happens.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk at night with a phone on a wireless charging pad, a shake torch, a hand-crank charger, wired earbuds and a coin beside the pad](scenes/smartphones/electromagnetic_induction.svg "Every gadget on this desk works because of induction. This lesson is about the wired earphones: a coil of wire that can move inside a magnet.")

Tara has a podcast episode due tonight and her microphone has just died. Her cousin Vihaan, who takes apart everything he owns, rummages in a drawer and pulls out a tangle of old wired earphones.

"Plug these into the mic socket and talk into one of the earpieces."

"Those are *speakers*," Tara says. "They turn electricity into sound. They can't do it backwards."

She tries anyway, holding an earpiece close to her mouth. On the laptop the recording bar jumps with every word. Played back, her voice is thin and quiet, but perfectly clear.

There is no battery in the earphones, no chip, nothing but a magnet, a tiny coil of wire and a paper-thin membrane. Where is the voltage coming from?

## The physics

Inside each earpiece, a small coil of fine wire — the voice coil — is glued to the membrane and sits in a narrow ring-shaped gap in a magnet. When Tara speaks, the sound pushes the membrane, and the wire **moves through the magnetic field**. A conductor moving through a magnetic field has an emf across it: the **motional emf**.

Picture the simplest case: a straight rod of length $l$ sliding at speed $v$ along two rails, through a uniform field $\vec{B}$, with $B$, $l$ and $v$ all at right angles.

![A metal rod sliding to the right on two rails in a field pointing into the page, with a resistor closing the circuit; positive charges are pushed along the rod, making one end positive](figures/motional_emf/rod-on-rails.svg "The rod carries its charges through the field, so each one feels a force qvB along the rod. The rod behaves like a battery — but only while it moves.")

**Why the emf appears.** Every free charge $q$ in the rod moves with the rod, so it feels the magnetic force $F = qvB$, pointing **along** the rod. Charges are pushed towards one end until the electric field this builds up balances the magnetic force. The work done per unit charge in pushing a charge along the whole rod is

$$\varepsilon = \frac{F\,l}{q} = \frac{(qvB)\,l}{q} = Blv$$

**The same answer from Faraday's law.** In one second the rod sweeps out an area $lv$ of the loop, so the flux changes at a rate $B\,lv$ — the same $Blv$. Two views, one emf.

- $B$ in tesla, $l$ in metres, $v$ in m/s gives $\varepsilon$ in volts.
- The formula holds when $B$, $l$ and $v$ are **mutually perpendicular** and $B$ is uniform along the rod. If the motion is along the rod or along the field, the force $qvB$ does not push charges along the wire and there is no emf.

In the earpiece, the magnet's gap is shaped so that the field points **radially** — straight out from the centre, like spokes. So wherever you look around the coil, the field is at right angles to the wire, and the membrane pushes the wire along the coil's axis, at right angles to both. Every short piece of the coil is a tiny rod on rails, and since the pieces are in series their emfs add. The coil acts like one long rod whose $l$ is the **total length of wire** in the gap.

## Worked example

**Given:** an earpiece whose voice coil holds $l = 2\,\text{m}$ of wire (about 60 turns, each a centimetre across) in a radial field $B = 0.5\,\text{T}$. Tara's voice moves the coil at $v = 1\,\text{cm/s} = 0.01\,\text{m/s}$ (illustrative values).
**Find:** the emf.

**Step 1 — field times length.** $Bl = 0.5 \times 2 = 1\,\text{T}\,\text{m}$. This fixed number is set by the magnet and the coil, not by Tara.

**Step 2 — multiply by the speed.**

$$\varepsilon = Blv = 1 \times 0.01 = 0.01\,\text{V}$$

Ten millivolts — about a hundredth of the voltage of a single AA cell. Tiny, but a microphone input is built to amplify exactly this size of signal.

**Sanity check:** when Tara stops talking, $v = 0$ and the emf vanishes; speak louder, the membrane moves faster, and the emf rises in proportion — which is why the recording bar jumps with each word.

## Where the picture breaks

The coil doesn't move at a steady speed: it vibrates back and forth hundreds or thousands of times a second, so the emf keeps rising, falling and reversing. $Blv$ gives the emf at each instant, using the speed at that instant. That alternating emf is the recorded sound wave.

The field in a real gap isn't perfectly uniform or perfectly radial, especially near the edges, and a real earphone coil is optimised for making sound, not catching it. That is part of why Tara's voice sounds thin: a dedicated dynamic microphone uses the same principle with a design tuned for listening.

And the rod on rails is a model, not a photograph. There are no rails in the earpiece; the coil's own turns and the cable to the laptop close the circuit.

## Key takeaway

A conductor moving through a magnetic field has an emf across it, because the magnetic force $qvB$ pushes its free charges along it. When $B$, $l$ and $v$ are mutually perpendicular, $\varepsilon = Blv$. Stop the conductor and the emf disappears — which is how the same coil can be a speaker in one direction and a microphone in the other.
