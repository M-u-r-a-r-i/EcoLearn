---
concept_id: faradays_law
interest: smartphones
format: explain
title: The shake torch that only glows while you shake it
check:
  question: |-
    A pick-up coil of $100$ turns sits around a magnet. When the magnet is pulled out, the flux through **each turn** falls steadily from $2\times10^{-4}\,\text{Wb}$ to zero in $0.01\,\text{s}$. What is the magnitude of the average emf induced in the coil?
  options:
    A: |-
      $2\,\text{V}$
    B: |-
      $0.02\,\text{V}$
    C: |-
      $0\,\text{V}$
    D: |-
      $2\times10^{-4}\,\text{V}$
  answer: A
  explanation: |-
    By Faraday's law, $|\varepsilon| = N\,\dfrac{\Delta\Phi}{\Delta t} = 100 \times \dfrac{2\times10^{-4}}{0.01} = 2\,\text{V}$. Every one of the 100 turns contributes the same emf, and they add in series.
  misconceptions:
    B: |-
      Forgets the number of turns $N$ and gives the emf of a single turn; the turns are in series, so their emfs add.
    C: |-
      Thinks that because the flux ends at zero the emf is zero; emf depends on how fast the flux changes, not on its final value.
    D: |-
      Multiplies the change in flux by the time instead of dividing by it; emf is a **rate** of change of flux, so $\Delta t$ goes underneath.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk at night with a phone on a wireless charging pad, a shake torch, a hand-crank charger, wired earbuds and a coin beside the pad](scenes/smartphones/electromagnetic_induction.svg "Every gadget on this desk works because a magnetic field is changing. This lesson is about the shake torch: a magnet that slides through a coil of wire.")

The power goes out in the middle of Kunal's revision, and his phone is already dead. His grandmother hands him her emergency torch — the kind with no batteries to buy. "Shake it," she says.

Through the clear plastic Kunal can see a heavy magnet that slides from end to end inside a coil of copper wire.

He gives it a lazy shake. A faint flicker. He shakes hard, and the torch glows properly. Curious, he stops with the magnet parked right in the middle of the coil, where the magnet's field through the copper must be strongest.

Nothing. Dark.

The magnet is closest to the wire exactly when the torch gives up. So whatever makes the electricity, it isn't simply "a strong magnet near a coil". What is it, then — and why does shaking harder give more?

## The physics

Faraday found the rule in 1831. An emf is induced in a coil whenever the magnetic flux through it **changes**, and the size of the emf is set by how fast it changes. For a coil of $N$ identical turns:

$$\varepsilon = -N\frac{d\Phi_B}{dt}$$

- $\varepsilon$ is the induced emf, in volts (V).
- $\Phi_B$ is the flux through **one** turn, in weber (Wb); $N\Phi_B$ is called the **flux linkage**.
- $\dfrac{d\Phi_B}{dt}$ is the rate of change of flux, in Wb/s. Since $1\,\text{Wb/s} = 1\,\text{V}$, the units work.
- The minus sign gives the **direction** of the emf. That is Lenz's law, the next lesson; for now we work with the size, $|\varepsilon|$.

When the flux changes steadily, the rate is simply $\Delta\Phi_B/\Delta t$, so $|\varepsilon| = N\,\Delta\Phi_B/\Delta t$. If it changes unevenly, this gives the **average** emf over that time.

![Left: a magnet moving into a coil makes a galvanometer needle kick. Right: the magnet resting inside the coil leaves the needle at zero](figures/faradays_law/magnet-into-coil.svg "A magnet at rest inside the coil gives a large flux but no emf. Only a changing flux induces anything.")

That is the parked magnet in Kunal's torch. With the magnet still, the flux through the coil is large but **constant**, so $d\Phi_B/dt = 0$ and the emf is zero. Shake harder and the same change of flux happens in less time, so the rate — and the emf — goes up.

![A graph of flux rising, staying level, then falling, with the emf below it: steady negative, then zero, then a larger positive value](figures/faradays_law/flux-and-emf-vs-time.svg "The emf follows the slope of the flux graph, not its height. Flat flux, however large, means zero emf; the steepest change gives the biggest emf.")

## Worked example

**Given:** the torch's coil has $N = 500$ turns. As the magnet slides in, the flux through each turn rises from zero to $2\times10^{-4}\,\text{Wb}$ in $\Delta t = 0.1\,\text{s}$ (illustrative values).
**Find:** the average emf, and what happens if Kunal shakes twice as fast.

**Step 1 — rate of change of flux in one turn.**

$$\frac{\Delta\Phi_B}{\Delta t} = \frac{2\times10^{-4}}{0.1} = 2\times10^{-3}\,\text{Wb/s}$$

So one turn on its own gives just $2\,\text{mV}$ — far too little to light anything.

**Step 2 — add up all the turns.** The 500 turns are in series, so their emfs add:

$$|\varepsilon| = 500 \times 2\times10^{-3} = 1\,\text{V}$$

That is a bit less than one AA cell — enough to make a small LED flicker.

**Step 3 — shake twice as fast.** The same flux change now takes $0.05\,\text{s}$, so the rate doubles and $|\varepsilon| = 2\,\text{V}$.

**Sanity check:** a handful of millivolts per turn times a few hundred turns should give about a volt, and it does — which is why these torches need so many turns of wire.

## Where the picture breaks

The magnet does not really change the flux at a steady rate. It speeds up and slows down on every shake, so the emf rises and falls; our $1\,\text{V}$ is an **average** over the stroke.

The flux also isn't the same through every turn: the turns near the ends of the coil see less of the magnet's field than those in the middle. Using one value for "the flux per turn" is an idealisation.

The emf also reverses each time the magnet changes direction. The simplest torches, like the one in the story, feed the LED almost directly, so the light dies as soon as the magnet stops. Most real ones add a small circuit that rectifies the emf and stores the energy in a capacitor or a small cell, so the light lingers for a while after you stop shaking — but the coil still only produces energy while the flux is changing.

## Key takeaway

An emf is induced whenever the magnetic flux through a coil changes, and its size depends on how **fast** the flux changes, not on how big it is: $\varepsilon = -N\,\dfrac{d\Phi_B}{dt}$. A strong but steady flux induces nothing. More turns, or a faster change, give a bigger emf.
