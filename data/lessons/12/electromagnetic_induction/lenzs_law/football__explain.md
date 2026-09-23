---
concept_id: lenzs_law
interest: football
format: explain
title: The magnet that crawls down a spare goalpost
check:
  question: |-
    A light aluminium ring hangs freely on a thread. You push the north pole of a strong magnet towards it, hold the magnet still for a moment, then pull it away. What does the ring do?
  options:
    A: |-
      Nothing at all, at any stage, because aluminium is not a magnetic material.
    B: |-
      Swings away from the magnet the whole time, because an induced effect always repels.
    C: |-
      Follows the magnet the whole time, because a moving magnet drags nearby metal along with it.
    D: |-
      Swings away while you approach, hangs still while you hold, then follows while you pull away.
  answer: D
  explanation: |-
    The induced current opposes the *change* in flux: rising flux is opposed by repulsion, falling flux by attraction, and while the magnet is still there is no change and so no current at all.
  misconceptions:
    A: |-
      Treats "not ferromagnetic" as "no interaction". Aluminium is not attracted by a magnet at rest, but it conducts — so a *changing* flux drives currents in it.
    B: |-
      Reads Lenz's law as "always pushes away". It opposes the change, so a falling flux is opposed by *attraction*, which pulls the ring after the magnet.
    C: |-
      Imagines the field dragging the metal along. That would accelerate the magnet and create kinetic and electrical energy out of nothing.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening football training ground with a contactless card reader at the turnstile, a magnetic-brake training bike on the touchline and a floodlight transformer cabinet](scenes/football/electromagnetic_induction.svg "Three machines around one ground. This lesson is about the rule that decides which way an induced current flows.")

The club's store room is full of spare goal parts, and Tanvi has found the best toy in it: a two-metre aluminium goalpost tube, hollow, open at both ends.

She stands it upright on the floor and drops a small strong magnet down it. Her friend counts. One, two, three, four. The magnet finally taps out of the bottom.

Then she does the same with a corner-flag pole — same length, same bore, but plastic. The magnet is through it before anyone can count at all.

The magnet does not stick to the aluminium. It does not touch the walls; you can hear that it doesn't. Aluminium is not even attracted by a magnet — Tanvi checks by holding the magnet against the tube, and it falls straight off.

So what is holding the magnet up on the way down, and where is all that lost energy going?

## The physics

As the magnet falls, the magnetic flux through each ring-shaped slice of the aluminium tube changes, so by Faraday's law a current is induced in the metal. Faraday's law gives the *size* of that emf. **Lenz's law** gives its *direction*:

> The induced current always flows in the direction that opposes the change producing it.

That is exactly what the minus sign in $\varepsilon = -N\,d\Phi_B/dt$ means.

![Two panels: a magnet's north pole approaching a coil is repelled, and the same magnet being pulled away is attracted](figures/lenzs_law/magnet-approaching-coil.svg "Approaching, the coil becomes a north pole and pushes back. Receding, it becomes a south pole and pulls back. Either way it fights the motion, never the position.")

To use it, ask two questions in order:

1. **Is the flux through the loop increasing or decreasing?**
2. **Which way must the current flow to fight that change?** If the flux is increasing, the induced current makes a field *opposing* it inside the loop; if it is decreasing, a field *supporting* it.

For Tanvi's tube: in the slices below the magnet the flux is growing, so they push it back up; in the slices above it the flux is dying away, so they pull it back up. Both act upwards, and the magnet sinks slowly.

**Why it has to be this way: energy conservation.** Suppose the induced current attracted the falling magnet instead. It would speed up, inducing a larger current, which would pull harder — faster and faster, with kinetic energy and electrical energy both appearing from nowhere. Lenz's law is precisely what forbids that. Because the force opposes the motion, gravity (or you) must do work to keep the flux changing, and that work is where the electrical energy comes from.

One condition matters: the metal must offer a **closed conducting path**. Saw the tube open along its whole length and the current can no longer loop around it, and the magnet falls almost as it would through the plastic pole.

## Worked example

**Given:** the magnet weighs $0.5\,\text{N}$ and slides down the $2.0\,\text{m}$ tube at a steady speed, taking $4.0\,\text{s}$.
**Find:** the electrical energy generated in the aluminium, and the average power.

"Steady speed" is the phrase that does the work: the magnet is going no faster at the bottom than at the top, so none of the energy released by gravity went into speeding it up.

The energy gravity releases over the drop is

$$W = (\text{weight}) \times (\text{height}) = 0.5\,\text{N} \times 2.0\,\text{m} = 1.0\,\text{J}$$

With no gain in kinetic energy, that whole joule becomes electrical energy in the metal — and since aluminium has resistance, it ends up as heat.

Spread over the four seconds of the fall, the average power is

$$P = \frac{W}{t} = \frac{1.0\,\text{J}}{4.0\,\text{s}} = 0.25\,\text{W}$$

A quarter of a watt is about a dim indicator LED — which is why nobody ever feels the tube get warm.

**Sanity check:** the magnet is small and slow, so a fraction of a joule and a fraction of a watt are the right size; anything in kilowatts would mean a free power station in a store room.

## Where the picture breaks

The tube is not really a stack of separate rings. The induced currents are continuous swirls in the metal — you meet them next as eddy currents. Thinking in rings gets the direction and the energy right, but it simplifies the pattern.

"Falling through honey" is a tempting description and a misleading one. Honey resists by contact, and nothing here touches the magnet. This drag also depends on **speed**: hold the magnet still inside the tube and it feels no magnetic force whatsoever, which no liquid does.

And the football is the setting, not an analogy. A spare goalpost is simply a long aluminium tube that happens to be lying in a football store room.

## Key takeaway

Lenz's law says an induced current always opposes the change that created it — the minus sign in Faraday's law. Approach a conducting loop and it pushes back; pull away and it holds on; stay still and it does nothing. It must be so, because that opposing force is what forces you to do work, and that work is where the electrical energy comes from.
