---
concept_id: lenzs_law
interest: cricket
format: explain
title: The magnet that falls in slow motion down a copper post
check:
  question: |-
    A bar magnet is dropped with its north pole downwards towards a horizontal copper ring lying on the ground. While the magnet is still falling towards the ring, the ring
  options:
    A: |-
      repels the magnet, so it falls with an acceleration less than $g$.
    B: |-
      attracts the magnet, so it falls with an acceleration greater than $g$.
    C: |-
      does nothing at all, because copper is not a magnetic material.
    D: |-
      repels the magnet hard enough to hold it still, because energy must be conserved.
  answer: A
  explanation: |-
    The flux through the ring is increasing, so the induced current flows so as to make the ring's upper face a north pole, which repels the falling magnet. The magnet still falls, just with a smaller acceleration than $g$.
  misconceptions:
    B: |-
      Gets the direction backwards, assuming the ring is "pulled along" by the magnet. An induced effect always opposes the change; attraction here would speed the magnet up and create energy from nothing.
    C: |-
      Confuses "not ferromagnetic" with "no interaction". Copper is not attracted by a magnet at rest, but it conducts, so a *changing* flux drives a current in it.
    D: |-
      Reads Lenz's law as total opposition. The induced force only opposes the change; it cannot exceed what is needed, and holding the magnet up indefinitely would give free support with no energy source.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening cricket ground with a walk-through metal-detector arch at the gate, LED bails charging on a pad, and a bowling machine](scenes/cricket/electromagnetic_induction.svg "Three machines at one ground. This lesson is about the rule that decides which way an induced current goes.")

The ground staff are replacing the boundary posts, and Ananya has grabbed one of the old copper tubes to show her cousin a trick before it goes on the scrap pile.

She holds the tube upright, drops a small steel ball down it — *clack*, straight through, about half a second. Then she drops a magnet of the same size down the same tube.

It takes four seconds.

It does not stick. It does not touch the sides. It just sinks, slowly, like it is falling through honey, and drops out of the bottom with a soft tap. Her cousin checks the tube for glue.

Nothing is touching the magnet. No one is holding it back. So what, exactly, is pushing up on it — and where is the energy going while it crawls down?

## The physics

As the magnet falls, the magnetic flux through each ring-shaped slice of the copper tube changes, so Faraday's law says a current is induced in the copper. Faraday's law gives the *size* of the emf. **Lenz's law** gives its *direction*:

> The induced current always flows in the direction that opposes the change producing it.

That is the minus sign in $\varepsilon = -N\,d\Phi_B/dt$.

![Two panels: a magnet's north pole approaching a coil is repelled, and the same magnet being pulled away is attracted](figures/lenzs_law/magnet-approaching-coil.svg "Approaching, the coil turns into a north pole and pushes back. Receding, it turns into a south pole and pulls back. Either way, it resists the motion.")

To use it, ask two questions in order:

1. **Is the flux through the loop increasing or decreasing?**
2. **Which way must the induced current flow to fight that change?** If the flux is increasing, the induced current makes a field *opposing* it inside the loop; if decreasing, a field *supporting* it.

For Ananya's tube: below the falling magnet the flux is increasing, so those rings push it back up; above it the flux is decreasing, so those rings pull it back. Both act upwards, and the magnet sinks slowly.

**Why it must be so: energy conservation.** Suppose the induced current attracted the magnet instead. The magnet would accelerate, inducing a larger current, which would pull harder — faster and faster, with electrical energy and kinetic energy both appearing out of nothing. Lenz's law is exactly what forbids that. Because the force opposes the motion, *you* (or gravity) must do work to keep the flux changing, and that work is what becomes the electrical energy.

Note the condition: the loop must be a **closed conducting path**. Cut the tube lengthwise and the current can no longer circle it, and the magnet falls almost normally.

## Worked example

**Given:** the magnet weighs about $0.5\,\text{N}$ and slides down a $1.0\,\text{m}$ copper tube at a steady speed.
**Find:** how much electrical energy is generated in the copper during the fall.

"Steady speed" is the key phrase: the kinetic energy at the bottom is the same as at the top, so none of the lost gravitational potential energy went into speeding the magnet up.

The energy released by gravity over the drop is

$$W = (\text{weight}) \times (\text{height}) = 0.5\,\text{N} \times 1.0\,\text{m} = 0.5\,\text{J}$$

With no gain in kinetic energy, all of that $0.5\,\text{J}$ becomes electrical energy in the copper — and, since the copper has resistance, it ends up as heat.

**Sanity check:** half a joule is tiny — about what it takes to lift a cricket ball a third of a metre — so you would never feel the tube warm up.

## Where the picture breaks

The tube is not really a stack of separate rings; the induced currents are continuous loops swirling in the copper (you will meet them as eddy currents). Treating it as rings gets the direction and the energy right, but it is a simplification of the pattern.

"Falling through honey" is only a loose likeness too. Honey resists because of contact and viscosity, and the magnet touches nothing. The drag here also depends on *speed*: at rest, the magnet feels no magnetic force at all, which is why it is not honey but something stranger.

And the cricket is the setting, not an analogy — a copper boundary post is simply a convenient tube.

## Key takeaway

Lenz's law: an induced current always opposes the change that created it, which is the minus sign in Faraday's law. Approach a loop and it pushes back; pull away and it holds on. It has to be this way, because the opposing force is what makes you do work — and that work is where the electrical energy comes from.
