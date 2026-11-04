---
concept_id: eddy_currents
interest: football
format: explain
title: The training bike with no brake pads
check:
  question: |-
    On a magnetic-brake training bike, the rider turns the knob so that the magnetic field at the flywheel is **doubled**, while pedalling at exactly the same speed as before. The braking force becomes about
  options:
    A: |-
      the same, because the braking depends only on how fast the wheel turns.
    B: |-
      twice as large, because the force is proportional to the field.
    C: |-
      four times as large, because the field enters the problem twice over.
    D: |-
      half as large, because a stronger field lets the current flow more easily.
  answer: C
  explanation: |-
    A stronger field induces a bigger emf ($\varepsilon \propto Bv$), which drives a bigger eddy current ($I \propto Bv/R$), and that current then feels a force in the same field ($F = BIl$). So $F \propto B^2 v$, and doubling $B$ quadruples the force.
  misconceptions:
    A: |-
      Remembers that the brake needs motion and concludes that speed is the only thing that matters. Speed and field strength both control the braking, which is exactly what the resistance knob adjusts.
    B: |-
      Counts the field once. It acts twice: once in inducing the current, and again in exerting a force on that induced current.
    D: |-
      Confuses the magnetic field with electrical resistance. The field does not make the metal a better conductor; $R$ is fixed by the metal itself.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening football training ground with a contactless card reader at the turnstile, a magnetic-brake training bike on the touchline and a floodlight transformer cabinet](scenes/football/electromagnetic_induction.svg "Three machines around one ground. This lesson is about currents that swirl inside solid metal.")

Sana is doing her rehab session on the club's training bike, and she is arguing with the physio about it.

"There's nothing touching the wheel," she says. She has the cover off to prove it. The flywheel is a plain metal disc. Beside it, not touching, sits a curved magnet on an arm. Turn the knob and the arm swings closer; the pedals get brutally heavy. Swing it away and the wheel spins almost freely.

No pads. No belt. No rubber dust anywhere, and this bike is years old — the one in her school gym wore its brake pads out in a season.

Then she notices something else. After a hard two minutes, the rim of that disc is warm.

Nothing is rubbing on it. So what is stopping the wheel, and where is the heat coming from?

## The physics

Faraday's law does not care whether the conductor is a tidy loop of wire. A changing flux drives a current round **any** closed conducting path — and inside a solid slab of metal there are countless such paths. The currents that swirl in them are called **eddy currents**.

As Sana's flywheel spins, each patch of the disc sweeps into the magnet's field and out again, so the flux through that patch keeps changing, and eddy currents circulate. By Lenz's law they flow in whatever direction opposes the change — which means opposing the motion that caused it. The disc is dragged back. And because the metal has resistance, the energy taken from her legs is dissipated as heat at a rate $P = I^2R$. That is the warm rim.

Notice how the field enters twice. A stronger field induces a bigger emf ($\varepsilon \propto Bv$), which drives a bigger current ($I \propto Bv/R$), and that current then feels a force $F = BIl$ in the same field. So the braking force goes as $B^2 v$ — which is why a small movement of the magnet arm changes the effort so much.

![A solid metal plate swinging between magnets with large eddy-current loops, and the same plate cut into slots with only small loops](figures/eddy_currents/solid-vs-slotted-plate.svg "Big loops in the solid plate mean a big current and a hard brake. The slotted plate leaves only narrow, high-resistance paths, so it swings on almost freely.")

That gives eddy currents two faces.

**Where they are wanted**

- **Magnetic braking**, as on Sana's bike: smooth, silent, nothing in contact, nothing to wear out. Some trains stop this way too.
- **Induction heating.** Put a changing field under a steel pan and the eddy currents heat the pan itself, while the glass beneath stays cool.
- **Metal detectors**, like the one at a stadium gate: the arch senses the field produced by eddy currents induced in whatever metal walks through it.

**Where they are a nuisance**

In a transformer or a motor, the iron core sits in a changing flux, so eddy currents flow in the core and waste energy as heat. The cure is to break up their paths: build the core from thin **laminations**, each insulated from its neighbours. The current can no longer make wide loops, and the narrow paths left have a high resistance, so the losses fall sharply.

Two conditions: the material must **conduct** (copper and aluminium work perfectly well even though they are not ferromagnetic), and the flux through it must be **changing**.

## Worked example

**Given:** the flywheel is spinning with $300\,\text{J}$ of kinetic energy. Sana stops pedalling and swings the magnet fully in; the wheel comes to rest in $6\,\text{s}$, with nothing touching it.
**Find:** the average power dissipated in the metal.

Nothing is in contact, so friction is not what removed the energy. The eddy currents did, and all $300\,\text{J}$ ended up as heat in the disc:

$$P_\text{avg} = \frac{E}{t} = \frac{300\,\text{J}}{6\,\text{s}} = 50\,\text{W}$$

Fifty watts is about a bright old-style bulb — spread over a whole metal disc for six seconds, enough to leave it noticeably warm, nowhere near enough to be dangerous.

**Sanity check:** brake twice as hard and the same energy comes out in half the time, so the power doubles — which is why the fiercest setting is the one that heats the wheel most.

## Where the picture breaks

"Little whirlpools of current" is a helpful image, not a precise one. The real eddy pattern depends on the shape of the conductor, on how fast the field changes, and on how deeply the field penetrates the metal; at high frequencies the current crowds into a thin surface layer.

The brake is also not like a friction brake in one important way: the force depends on **speed**. Pedal slowly and it is weak; stop entirely and it is exactly zero. That is why an eddy-current brake alone can slow a train smoothly but cannot hold it still at a platform.

And the football here is the setting, not an analogy. A rehab bike in a club gym is just a convenient place to meet induction braking.

## Key takeaway

A changing magnetic flux induces swirling currents inside solid conductors — eddy currents — which by Lenz's law oppose the change and turn the energy into heat. They are what make magnetic brakes, induction heating and metal detectors work, and they are why transformer and motor cores are built from thin insulated laminations.
