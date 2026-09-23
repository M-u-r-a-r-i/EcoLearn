---
concept_id: eddy_currents
interest: cricket
format: explain
title: The hotplate that heats the pan but not the paper
check:
  question: |-
    The iron core of a transformer is built from many thin sheets, each coated so that it is insulated from its neighbours, instead of one solid block. Why?
  options:
    A: |-
      Thin sheets make the core lighter and cheaper to manufacture.
    B: |-
      The insulation breaks up the eddy-current paths, so far less energy is wasted as heat.
    C: |-
      Layers of iron produce a stronger magnetic field than a solid block of the same size.
    D: |-
      Without the coating the coils wound on the core would short-circuit against the iron.
  answer: B
  explanation: |-
    A changing flux induces currents in the core itself. Insulated laminations force those currents into narrow, high-resistance paths, so the power wasted heating the core drops sharply.
  misconceptions:
    A: |-
      Treats laminations as a manufacturing convenience. They are more expensive to make, not less — the reason is electrical.
    C: |-
      Assumes the layering boosts the field. The magnetic properties come from the iron itself; slicing it up does not strengthen the field, and the small air gaps slightly weaken it.
    D: |-
      Confuses core insulation with wire insulation. The coil's own wire is already insulated; the laminations are insulated from *each other*, inside the core.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening cricket ground with a walk-through metal-detector arch at the gate, LED bails charging on a pad, and a bowling machine](scenes/cricket/electromagnetic_induction.svg "Three machines at one ground. This lesson is about currents that swirl inside solid metal.")

Between sessions, Kabir goes looking for tea in the kitchen behind the pavilion. The cook has a flat glass hotplate with no flame and no coil — the sort you switch on and it just works.

Kabir watches a steel pan of milk come to the boil on it in under two minutes. Then the cook does something that looks like a trick: she lifts the pan, lays a sheet of newspaper flat on the hotplate, and puts the pan back on top of the paper.

The milk boils again. The newspaper comes out afterwards cool and unmarked. So does the glass, more or less — warm where the pan sat, cold two centimetres away.

Whatever is heating that pan is not coming up through the paper as heat. So how is the energy getting into the metal?

## The physics

Under the glass is a flat coil carrying a rapidly alternating current, which makes a rapidly changing magnetic field in the metal above it. Faraday's law does not care whether the conductor is a neat loop of wire: a changing flux drives a current in **any** closed conducting path. In a solid slab of metal, those paths are closed loops swirling inside the metal itself. They are called **eddy currents**.

Lenz's law still applies: the eddies flow so as to oppose the change in flux that made them. And because the metal has resistance, they dissipate energy as heat, at a rate $P = I^2R$.

That gives eddy currents two faces, one useful and one costly.

**Where they are wanted**

- **Induction heating.** The pan is the "resistor", so the heat appears inside the pan itself — which is why the paper below stays cool.
- **Magnetic braking.** Move a metal disc or rail through a magnetic field and the eddy currents oppose the motion, giving a smooth brake with no contact, no pads and nothing to wear out. Exercise bikes and some trains slow this way.
- **Metal detectors**, like the one at the ground's gate: the arch senses the field produced by eddy currents induced in whatever metal passes through.

**Where they are a nuisance**

In transformers and motors, the iron core sits in a changing flux, so eddy currents flow in the core and waste energy as heat. The cure is to break up their paths: build the core from thin **laminations**, each insulated from the next. The current can no longer make wide loops, and the narrow paths it is left with have high resistance, so the losses fall.

![A solid metal plate swinging between magnets with large eddy-current loops, and the same plate cut into slots with only small loops](figures/eddy_currents/solid-vs-slotted-plate.svg "The solid plate is braked hard by big eddy loops; slots leave only narrow high-resistance paths, so the slotted plate swings on.")

Note the conditions: the material must **conduct** (copper and aluminium work even though they are not ferromagnetic — a glass or plastic pan on an induction hob stays cold), and the flux through it must be **changing**.

## Worked example

**Given:** the flywheel of a bowling machine is spinning with $200\,\text{J}$ of kinetic energy. An eddy-current brake is switched on, and the wheel comes to rest in $10\,\text{s}$ with nothing touching it.
**Find:** the average power dissipated in the metal.

Nothing touches the wheel, so friction is not removing the energy. The eddy currents are, and all of the kinetic energy ends up as heat in the metal:

$$P_\text{avg} = \frac{E}{t} = \frac{200\,\text{J}}{10\,\text{s}} = 20\,\text{W}$$

That is about the power of a small LED bulb, spread over ten seconds and over the whole wheel — enough to warm it slightly, not enough to feel hot.

**Sanity check:** halve the braking time and the same energy comes out twice as fast, so the power doubles — which is why a hard, fast brake is the one that gets warm.

## Where the picture breaks

"Little whirlpools of current" is a helpful image but not a precise one: the eddy pattern depends on the shape of the conductor, the frequency and how deep the field penetrates, and at high frequencies the current crowds into a thin surface layer.

The hotplate story hides something too. Most domestic induction hobs need a pan that is ferromagnetic, because the heating there comes partly from repeated magnetisation of the iron as well as from eddy currents — an aluminium pan on such a hob may not heat at all, even though aluminium conducts well.

And the cricket here is setting, not analogy. A kitchen behind a pavilion is just a convenient place to meet induction heating.

## Key takeaway

A changing magnetic flux induces swirling currents inside solid conductors — eddy currents — which by Lenz's law oppose the change and turn energy into heat. They are the working principle of induction heating, magnetic brakes and metal detectors, and the reason transformer and motor cores are built from thin insulated laminations.
