---
concept_id: eddy_currents
interest: smartphones
format: explain
title: The coin that got hot on the wireless charger
check:
  question: |-
    Under the transmitting coil of a wireless charging pad there is a thin sheet of **ferrite** — a ceramic magnetic material that guides magnetic flux well but conducts electricity very poorly. Why is ferrite used there instead of a solid plate of iron?
  options:
    A: |-
      Ferrite is a permanent magnet stronger than iron, so it adds its own steady field to the coil's field.
    B: |-
      Iron conducts, so current from the coil would leak into the plate through the wire's insulation and short the coil out.
    C: |-
      Ferrite is lighter than iron, and saving weight is the only reason for the choice.
    D: |-
      The coil's changing flux would drive large eddy currents in solid iron, wasting energy as heat; ferrite barely conducts, so they stay small.
  answer: D
  explanation: |-
    Any conductor in a changing flux carries induced eddy currents that turn energy into heat. Ferrite still guides the flux, but its very high resistivity keeps those currents, and the heat they make, small.
  misconceptions:
    A: |-
      Confuses a material that guides flux with a permanent magnet; a steady field from a magnet would induce nothing, since only a changing flux induces an emf.
    B: |-
      Thinks eddy currents are current leaking out of the circuit by contact; they are induced inside the metal by the changing flux, with no connection needed.
    C: |-
      Picks a practical side reason; weight is not the point — a solid iron plate would waste energy as heat through eddy currents.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk at night with a phone on a wireless charging pad, a shake torch, a hand-crank charger, wired earbuds and a coin beside the pad](scenes/smartphones/electromagnetic_induction.svg "Every gadget on this desk works because a magnetic field is changing. This lesson is about the coin next to the charging pad: a piece of metal nobody connected to anything.")

Farhan empties his pockets onto the desk every evening: keys, earbuds, a couple of coins. Tonight he drops his phone onto the wireless charging pad without looking — right on top of a coin that had slid onto it.

Ten minutes later the pad's light is blinking an unhappy orange and the phone has barely charged. He lifts the phone and picks up the coin.

It is hot. Not burning, but hot enough that he drops it and shakes his fingers.

Farhan stares at it. The coin isn't plugged into anything. It has no wires, no battery, no circuit — it's a disc of metal. The pad was supposed to be sending energy to the phone. Somehow a fair part of it went into a coin that was never part of any circuit at all.

How can current flow in a lump of metal with nowhere to go?

## The physics

The pad's coil makes a magnetic field that reverses direction many thousands of times a second, so the flux through anything lying on the pad is constantly **changing**. Faraday's law doesn't care whether there is a coil of wire there. Any closed path inside a solid conductor — a circle drawn anywhere in the coin — has a changing flux through it, so an emf acts around it and a current flows around it.

These swirling currents inside a solid piece of metal are called **eddy currents**. By Lenz's law, they circulate so as to **oppose the change** that produced them. And because the metal has resistance, they turn energy into heat at the rate $I^2R$. That energy comes from the pad — which is why the phone charged so slowly, and why the coin got hot.

Eddy currents are useful when you want exactly that:

- **Induction heating.** An induction hob drives a changing field through the base of a pan, and eddy currents heat the pan directly.
- **Magnetic braking.** A metal disc or plate moving through a magnetic field carries eddy currents that oppose its motion, slowing it with nothing touching it. Some trains and exercise bikes use this.
- **Damping.** Meter needles and balances settle quickly when a metal vane swings through a magnet's field.

![Two metal plates swinging through a magnetic field: a solid plate with large eddy-current loops that stops quickly, and a slotted plate with only small loops that keeps swinging](figures/eddy_currents/solid-vs-slotted-plate.svg "Cutting slots forces eddy currents into narrow, high-resistance paths, so much less energy is lost as heat — the same idea as a laminated core.")

They are a nuisance wherever you *don't* want heat. Transformer cores, like the one inside a wall charger, are built from thin, insulated sheets — **laminations** — instead of one solid block, because the insulation breaks the big current loops into small ones and the loss falls sharply. For the same reason, wireless chargers put their coils on **ferrite**, a ceramic magnetic material that guides the flux but hardly conducts at all.

## Worked example

**Given:** a steel coin of mass $m = 0.004\,\text{kg}$ absorbs $1\,\text{W}$ of eddy-current heating for $t = 40\,\text{s}$. Steel's specific heat capacity is about $500\,\text{J/(kg K)}$ (illustrative values, ignoring heat lost to the air).
**Find:** how much the coin warms up.

**Step 1 — the energy delivered.** $E = Pt = 1 \times 40 = 40\,\text{J}$.

**Step 2 — the energy needed per degree.** $mc = 0.004 \times 500 = 2\,\text{J/K}$. It takes just two joules to warm this coin by one degree.

**Step 3 — the temperature rise.**

$$\Delta T = \frac{E}{mc} = \frac{40}{2} = 20\,\text{K}$$

A coin at a room temperature of $30\,^\circ\text{C}$ reaches about $50\,^\circ\text{C}$ in under a minute — hot enough to sting your fingers, just as Farhan found.

**Sanity check:** a single watt sounds small, but a coin weighs so little that it needs only a couple of joules per degree, so a rise of tens of degrees in a minute is the right size.

## Where the picture breaks

"Little whirlpools of current" is a useful image, not a precise one. The real pattern depends on the shape of the metal, on the frequency and on how deep the changing field gets into it; at high frequencies the currents crowd into a thin layer near the surface.

The coin's heating is not purely eddy currents either. A steel coin is magnetic, and repeatedly magnetising it one way and then the other also wastes some energy as heat. An aluminium or copper object would heat by eddy currents alone.

And real pads are designed for this problem. Many watch for signs that power is going somewhere it shouldn't — the orange light in the story — and cut back. Don't test it on purpose: a hot coin or key can burn you.

## Key takeaway

A changing magnetic flux through a solid conductor drives swirling **eddy currents** inside it. By Lenz's law they oppose the change, and they turn energy into heat. That heating is useful in induction hobs and magnetic brakes, and wasteful in transformers and chargers — which is why cores are laminated and charging coils sit on ferrite, to break up the current paths.
