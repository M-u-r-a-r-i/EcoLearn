---
concept_id: lenzs_law
interest: gaming
format: explain
title: The rumble motor that fights back when you join its wires
check:
  question: |-
    With its two leads left apart, the shaft of the little rumble motor spins freely for a couple of seconds after a flick. With the leads twisted together, the same flick dies almost at once. Why?
  options:
    A: |-
      A current can now flow in the coil, and the magnetic force on that current opposes the rotation.
    B: |-
      The joined leads push current back into the coil, which drives the motor backwards.
    C: |-
      With the leads apart there is no induced emf at all; joining them is what creates it.
    D: |-
      The coil becomes an electromagnet that attracts the rotor's magnet and pulls it to a stop.
  answer: A
  explanation: |-
    Joining the leads completes the circuit, so the induced emf can drive a current. That current sits in the magnet's field, and by Lenz's law the force on it opposes the motion that produced it.
  misconceptions:
    B: |-
      Imagines the circuit "feeding back" and reversing the motor. The induced current opposes the *change*, so the shaft slows down; it never gets driven backwards.
    C: |-
      Confuses emf with current. A changing flux induces an emf whether or not the circuit is closed; what an open circuit prevents is the current — and with no current there is no force.
    D: |-
      Gets the direction backwards. If the coil attracted the approaching pole, the shaft would speed up on its own, induce more current still, and make energy out of nothing.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming corner at night: a pinball game on the monitor, a headset charging on a pad, a controller cut away at its rumble motor, a tablet pen hovering over a tablet, and an arcade coin chute with a magnet](scenes/gaming/electromagnetic_induction.svg "Five gaming machines. This lesson is about the rule that decides which way an induced current flows — and why it always feels like resistance.")

Meghna's controller stopped charging months ago, so she has finally opened it up on the kitchen table. Out comes the rumble motor: a cylinder the size of a thumb joint with a lopsided weight on its shaft and two thin wires hanging off it.

She flicks the shaft with a thumbnail. It spins, whirrs, and coasts for a good two seconds before it stops.

Then, for no reason except tidiness, she twists the two bare wire ends together — and flicks it again.

This time it barely completes a turn. The shaft feels stiff, as though someone has put a finger on it. She untwists the wires: free again. Twists them: stiff again.

Nothing is touching the shaft either way. The wires are not connected to anything except each other. So what is holding the motor back — and if her thumb has to push harder, where is that extra effort going?

## The physics

As the shaft turns, the rotor's magnet sweeps past the coil inside the motor, so the flux through that coil changes and Faraday's law gives an emf. Faraday's law tells you the *size* of that emf. **Lenz's law** tells you its *direction*:

> The induced current always flows in the direction that opposes the change producing it.

That is the minus sign in $\varepsilon = -N\,d\Phi_B/dt$.

![Two panels: a magnet's north pole approaching a coil is repelled, and the same magnet being pulled away is attracted](figures/lenzs_law/magnet-approaching-coil.svg "Approaching, the coil turns into a north pole and pushes back. Receding, it turns into a south pole and pulls back. Either way it resists the motion.")

To use it, ask two questions in order:

1. **Is the flux through the loop increasing or decreasing?**
2. **Which way must the current flow to fight that change?** If the flux is increasing, the induced current sets up a field *opposing* it inside the loop; if decreasing, a field *supporting* it.

**Why it has to be this way: energy conservation.** Suppose the induced current attracted the approaching pole instead. The shaft would speed up, which would induce a larger current, which would pull harder still — the motor would accelerate on its own while also heating its own wires, with energy appearing from nowhere. Lenz's law is exactly what forbids that. Because the force opposes the motion, *something* must do work to keep the flux changing, and that work is what becomes electrical energy.

Note the condition: the induced emf needs a **closed conducting path** before any current — and so any opposing force — can exist. That is the whole difference between Meghna's two flicks.

## Worked example

**Given:** as the shaft turns, the rotor's north pole sweeps towards the coil. With the leads joined, the induced current heats the motor's own winding at about $0.1\,\text{W}$ (an illustrative value), and Meghna keeps the shaft turning steadily for $5\,\text{s}$.
**Find:** which way the induced current flows in that coil, and the extra work her thumb must do.

**Direction.** The north pole is approaching, so the flux through the coil is *increasing*. To oppose that, the coil must push the pole away — the face of the coil nearest the magnet has to become a north pole too. Seen from the magnet, that means the current runs **anticlockwise** around the coil.

**Energy.** The electrical energy has to be paid for, and steady speed means none of it came from the shaft slowing down:

$$W = Pt = 0.1\,\text{W} \times 5\,\text{s} = 0.5\,\text{J}$$

Half a joule — roughly the work of lifting the controller about $20\,\text{cm}$ off the table. That is what her thumb supplies, and it all ends up as heat in the winding.

**Sanity check:** if the force helped the rotation instead, the shaft would spin faster and faster and light up a bulb for free, which no one has ever managed.

## Where the picture breaks

Even with its leads apart the motor stops eventually, because of friction in the bearings and air drag on the weight. Lenz's law explains the *extra* drag she added, not all of it.

This drag is also nothing like a brake pad: it depends on speed. Hold the shaft still with the wires joined and there is no magnetic force at all, because nothing is changing. It fades away exactly as the motion does.

And a real motor is more than one coil and one pole. It has several windings, a commutator that switches them, and an iron rotor in which currents also swirl — you will meet those as eddy currents. Treating it as a single coil gets the direction and the energy right, but it is a simplified picture.

The gaming is the setting, not an analogy: a rumble motor is simply a coil and a magnet you already own.

## Key takeaway

Lenz's law: an induced current always flows so as to oppose the change that created it — the minus sign in Faraday's law. Approach a loop and it pushes back; pull away and it holds on. It must be so, because that opposition is what forces somebody to do work, and that work is where the electrical energy comes from.
