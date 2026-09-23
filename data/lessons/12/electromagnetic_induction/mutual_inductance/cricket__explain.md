---
concept_id: mutual_inductance
interest: cricket
format: explain
title: The charging pad on the scorer's table
check:
  question: |-
    Two coaxial solenoids have a mutual inductance $M$. The inner coil is rewound with twice as many turns; the outer solenoid, the area and the length are all unchanged. What happens to $M$?
  options:
    A: |-
      It quadruples, because inductance always goes as the square of the number of turns.
    B: |-
      It stays the same, because $M$ belongs to the coil that carries the current.
    C: |-
      It halves, because the same flux is now shared between twice as many turns.
    D: |-
      It doubles, because $M$ is proportional to the turns on each coil.
  answer: D
  explanation: |-
    $M = \mu_0 N_1 N_2 A / l$ is proportional to $N_2$ to the first power, so doubling the inner coil's turns doubles $M$: each extra turn links the same flux, so the flux linkage doubles.
  misconceptions:
    A: |-
      Carries the $N^2$ of *self*-inductance across to mutual inductance. There $N$ appears twice because the same coil both makes the flux and links it; here each coil contributes its own turns once.
    B: |-
      Treats $M$ as a property of the driving coil alone. $M$ belongs to the *pair*, and it is the same number whichever coil you drive.
    C: |-
      Thinks the flux is divided up among the turns. Each turn links the whole flux, so more turns mean more flux linkage, not less per turn.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening cricket ground with a walk-through metal-detector arch at the gate, LED bails charging on a pad, and a bowling machine](scenes/cricket/electromagnetic_induction.svg "Three machines at one ground. This lesson is about two coils that pass energy across a gap without touching.")

Sneha is scoring the night match from the pavilion table, and her phone is down to four per cent with eleven overs still to go. The scorer from the visiting side slides a flat white pad across to her. A cable runs into the pad. Nothing runs into the phone.

She drops the phone on it, thick plastic case and all. The charging symbol appears.

Then she nudges the phone sideways to make room for the scorebook — three centimetres, no more. The symbol vanishes. She slides it back to the middle and it comes straight back.

Nothing is touching anything. There is no socket, no contact, no exposed metal. Energy is crossing a gap of solid plastic — and somehow it cares, to the centimetre, exactly where the phone is sitting.

## The physics

Inside the pad is a coil. Inside the back of the phone is a second coil. That is the whole trick.

Send a current $I_1$ through coil 1 and it makes a magnetic field, so some of its flux passes through coil 2. Double the current and you double the field everywhere, so you double that flux. The flux linkage of coil 2 is therefore proportional to the current in coil 1:

$$N_2\Phi_2 = M I_1$$

The constant $M$ is the **mutual inductance** of the pair, measured in **henry** (H), just like self-inductance. And by Faraday's law, changing $I_1$ induces an emf in the *other* coil:

$$\varepsilon_2 = -M\frac{dI_1}{dt}$$

Two things are worth pinning down. First, $M$ is a property of the **pair**, not of either coil: drive coil 2 instead and you get the same number, $M_{12} = M_{21} = M$. Second, $M$ depends only on geometry and on what is between the coils — the turns, the shared area, the separation and the alignment — never on the current.

![Three schematic side views of a driving coil and a pick-up coil: aligned and close, lifted apart, and slid to one side, with fewer field lines through the pick-up coil each time](figures/mutual_inductance/coupling-and-alignment.svg "Slide the pick-up coil sideways or lift it away and less of the driving coil's flux passes through it, so M falls — and with it the induced emf.")

That is Sneha's three centimetres. Moving the phone changes $M$ itself.

The case you must be able to calculate is **two coaxial solenoids**: a long outer solenoid of $N_1$ turns and length $l$, with a shorter coil of $N_2$ turns wound around its middle, enclosing cross-sectional area $A$.

![A long outer solenoid carrying a changing current with a shorter inner coil wound coaxially inside it, connected to a galvanometer](figures/mutual_inductance/coaxial-solenoids.svg "The outer solenoid's field threads the inner coil, so a changing current in one induces an emf in the other — and M is the same whichever one you drive.")

Inside a long solenoid the field is uniform, $B = \mu_0 N_1 I_1 / l$. All of it passes through the inner coil, so each of its $N_2$ turns links a flux $BA$:

$$N_2\Phi_2 = N_2 \cdot \frac{\mu_0 N_1 I_1}{l} \cdot A \qquad\Longrightarrow\qquad M = \frac{\mu_0 N_1 N_2 A}{l}$$

This holds for a **long** air-cored solenoid — length much greater than its radius — with the inner coil near the middle, so end effects are negligible and the whole of $A$ sits in the uniform field.

## Worked example

**Given:** an outer solenoid with $N_1 = 500$ turns over a length $l = 0.50\,\text{m}$, and an inner coil of $N_2 = 100$ turns enclosing $A = 4\times10^{-4}\,\text{m}^2$ (about the area of a large postage stamp).
**Find:** $M$, and the emf induced in the inner coil when the outer current changes by $2.0\,\text{A}$ in $0.010\,\text{s}$.

**Step 1 — the geometry factor.** Everything except $\mu_0$ is geometry:

$$\frac{N_1 N_2 A}{l} = \frac{500 \times 100 \times 4\times10^{-4}}{0.50} = 40\,\text{m}$$

**Step 2 — the mutual inductance.** Multiply by $\mu_0 = 4\pi\times10^{-7}\,\text{T}\,\text{m}/\text{A}$:

$$M = 4\pi\times10^{-7} \times 40 \approx 5\times10^{-5}\,\text{H}$$

That is $50\,\mu\text{H}$ — a small coupling, which is what you expect from two coils you could hold in one hand.

**Step 3 — how fast the current changes.** $\Delta I_1/\Delta t = 2.0\,\text{A} \div 0.010\,\text{s} = 200\,\text{A/s}$.

**Step 4 — the emf.**

$$|\varepsilon_2| = M\frac{\Delta I_1}{\Delta t} = (5\times10^{-5})(200) = 0.010\,\text{V}$$

Ten millivolts — about a hundredth of a torch cell, far too little to light anything, but easily read on a meter.

**Sanity check:** a tiny coupling and a fairly gentle change should give a small voltage, and it does.

## Where the picture breaks

The coaxial formula assumes the *whole* of the outer solenoid's flux crosses the inner coil. Two flat coils on a table are nothing like that: most of the pad's flux misses the phone entirely, which is exactly why alignment matters so much and why $M$ is far smaller than a coaxial pair of the same size would give. How well two coils share flux has its own measure, the coupling coefficient — you'll meet it later.

A real charging pad is also more than two coils. It must run on **alternating** current, since a steady current induces nothing however large it is; it uses tuned circuits to improve the transfer; and the pad stays off until it senses a phone. Some of the energy that does cross the gap ends up as eddy-current heat in nearby metal, not in the battery.

And the cricket here is setting, not analogy. The pavilion table is simply where you meet two coupled coils.

## Key takeaway

Mutual inductance $M$ measures how well two coils share flux: $N_2\Phi_2 = MI_1$, and a changing current in one induces $\varepsilon_2 = -M\,dI_1/dt$ in the other. It is a property of the pair — the same value whichever coil you drive — and it depends only on geometry, not on current. For two coaxial solenoids, $M = \mu_0 N_1 N_2 A / l$.
