---
concept_id: self_inductance
interest: gaming
format: explain
title: The tiny diode that keeps the claw machine alive
check:
  question: |-
    An air-cored coil in the cabinet is rewound with twice as many turns, in the same length and with the same cross-sectional area. What happens to its self-inductance?
  options:
    A: |-
      It doubles.
    B: |-
      It goes up four times.
    C: |-
      It is unchanged, because inductance is set by the current, not the winding.
    D: |-
      It halves, because the flux is now shared between twice as many turns.
  answer: B
  explanation: |-
    For a long solenoid $L = \mu_0 N^2 A / l$. Doubling $N$ doubles the field for a given current *and* doubles the number of turns linking that field, so the flux linkage — and $L$ — goes up four times.
  misconceptions:
    A: |-
      Counts the turns only once. The extra turns make a stronger field as well as linking it, which is why $N$ appears squared.
    C: |-
      Treats $L$ as something the current decides. Self-inductance depends only on geometry and the core; a coil has the same $L$ carrying $2\,\text{A}$ or carrying nothing at all.
    D: |-
      Imagines one fixed amount of flux being split up. Every turn links the whole flux, so adding turns adds flux linkage rather than diluting it.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming corner at night: a pinball game on the monitor, a headset charging on a pad, a controller cut away at its rumble motor, a tablet pen hovering over a tablet, and an arcade coin chute with a magnet](scenes/gaming/electromagnetic_induction.svg "Five gaming machines, and every one of them holds a coil that objects to being switched.")

Karthik spends Sunday mornings at his aunt's workshop, where dead arcade machines come to be revived. Today it is a claw machine, opened up like a patient, the claw hanging by its wires.

Inside the claw is a chunky coil — energise it and the claw grips, cut the power and it lets go. What catches Karthik's eye is a small glass diode soldered straight across the coil's two terminals, and soldered *backwards*, so that in normal running it does nothing at all.

"Leave that off," his aunt says, "and the transistor that drives the claw dies inside a week. Every time."

Karthik checks the supply with a meter: twelve volts, steady. The transistor is rated far above that. And the moment it dies is not when the claw grips — it is when the claw *lets go*, when the circuit is being switched off and the supply is being disconnected.

Where does a voltage big enough to kill a transistor come from, at the exact moment you stop pushing current?

## The physics

A coil carrying a current makes its own magnetic field, so its own flux threads its own turns. Change the current and you change that flux — and by Faraday's law the coil induces an emf **in itself**. This is **self-induction**.

For a coil with no magnetic material nearby, the flux linkage is proportional to the current:

$$N\Phi_B = LI$$

The constant $L$ is the **self-inductance**, measured in **henry** (H), where $1\,\text{H} = 1\,\text{Wb/A}$. It depends only on geometry — the number of turns, the size and shape of the coil, and what it is wound on. Putting this into Faraday's law gives the equation you will use:

$$\varepsilon = -L\frac{dI}{dt}$$

The minus sign is Lenz's law again: the induced emf opposes the *change* in current, which is why it is called the **back emf**. Switch on, and it fights the current's growth, so the current climbs to its steady value instead of jumping there. Switch off, and it fights the current's collapse, trying to keep it flowing.

![A solenoid in a circuit with a battery and switch, with the back emf opposing the growing current, and a graph of current rising gradually instead of jumping](figures/self_inductance/solenoid-back-emf.svg "Closing the switch: the coil holds the current back, so it rises gradually. Opening it: the coil tries to keep the current going.")

That is the claw. A transistor can switch off in a fraction of a millisecond, so $dI/dt$ is enormous and $L\,dI/dt$ can be many times the twelve-volt supply — easily enough to destroy the transistor. The backwards diode gives that current a harmless loop to die away in, which is the whole reason it is there.

For a **long** solenoid — length much greater than its radius — of $N$ turns, length $l$ and cross-sectional area $A$, in air:

$$L = \frac{\mu_0 N^2 A}{l}$$

Notice the $N^2$: extra turns make a stronger field *and* link it, so the effect counts twice.

## Worked example

**Given:** an air-cored coil like the claw's, with $N = 400$ turns over a length $l = 0.10\,\text{m}$ and cross-sectional area $A = 5\times10^{-4}\,\text{m}^2$ (about $5\,\text{cm}^2$). The transistor cuts its $2.0\,\text{A}$ to zero in $0.1\,\text{ms}$.
**Find:** the self-inductance, and the size of the back emf.

**Step 1 — the geometry factor.** Everything but $\mu_0$ is shape:

$$\frac{N^2 A}{l} = \frac{(400)^2 \times 5\times10^{-4}}{0.10} = \frac{80}{0.10} = 800\,\text{m}$$

**Step 2 — the inductance.** Multiply by $\mu_0 = 4\pi\times10^{-7}\,\text{T}\,\text{m}/\text{A}$:

$$L = (4\pi\times10^{-7})(800) \approx 1.0\times10^{-3}\,\text{H}$$

One millihenry — a coil you could hold between two fingers.

**Step 3 — the back emf.** The current falls by $2.0\,\text{A}$ in $1\times10^{-4}\,\text{s}$, a rate of $2\times10^{4}\,\text{A/s}$:

$$|\varepsilon| = L\frac{\Delta I}{\Delta t} = (1.0\times10^{-3})(2\times10^{4}) = 20\,\text{V}$$

Twenty volts out of a twelve-volt machine, produced by switching *off*.

**Sanity check:** switch ten times faster and the emf is ten times bigger, so the danger comes from the speed of the switch, not the size of the supply.

## Where the picture breaks

The coil is not storing current, and it has no momentum, however much it behaves as though it does. What it stores is energy in its magnetic field, and the back emf follows from Faraday's law, not from inertia. The likeness to mass is a memory aid, nothing more.

The solenoid formula also assumes a long, tightly wound, air-cored coil with negligible end effects. A real claw coil has an iron plunger inside it, which makes $L$ far larger — and not even constant, since iron's response to a field is not linear. The true spike is worse than $20\,\text{V}$, which is why the diode is not optional.

A dying transistor in a real cabinet can also have other causes, from heat to a worn connector. Self-induction is the main one here, not the only possible one.

And the gaming is the setting, not an analogy: a claw machine simply happens to be a coil with a switch in front of it.

## Key takeaway

A coil opposes changes in its own current: $\varepsilon = -L\,dI/dt$, where the self-inductance $L$ (in henry) depends only on geometry — for a long solenoid, $L = \mu_0 N^2 A / l$. A steady current produces no back emf at all; a fast-changing one can produce a voltage far larger than the supply, which is why switching a coil off is the dangerous moment.
