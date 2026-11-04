---
concept_id: mutual_inductance
interest: gaming
format: explain
title: The drawing pen that has never needed charging
check:
  question: |-
    The tablet's coil is driven by a **steady** direct current of $2.0\,\text{A}$ instead of an alternating one. The pen rests on the glass, well coupled, with $M = 25\,\mu\text{H}$. What emf is induced in the pen's coil?
  options:
    A: |-
      Zero, because the current is not changing.
    B: |-
      $2.0\,\text{V}$, because the pen's coil sees the same voltage as the tablet's coil.
    C: |-
      $5\times10^{-5}\,\text{V}$, worked out as $M I_1$.
    D: |-
      A small steady emf, which gets smaller as the pen is lifted away.
  answer: A
  explanation: |-
    $\varepsilon_2 = -M\,dI_1/dt$, and a steady current has $dI_1/dt = 0$. However large the current and however good the coupling, an unchanging current induces nothing.
  misconceptions:
    B: |-
      Treats two coupled coils as if they passed voltage straight across, like a wire. They respond only to *change* — this is exactly why a transformer fed with direct current gives nothing out.
    C: |-
      Uses $N_2\Phi_2 = MI_1$ as though flux linkage were an emf. That product is a flux linkage in weber; the emf is its rate of change.
    D: |-
      Assumes geometry alone can make an emf. $M$ only says how much emf a given *rate of change* produces — with nothing changing, there is nothing for $M$ to multiply.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming corner at night: a pinball game on the monitor, a headset charging on a pad, a controller cut away at its rumble motor, a tablet pen hovering over a tablet, and an arcade coin chute with a magnet](scenes/gaming/electromagnetic_induction.svg "Five gaming machines. This lesson is about two coils that pass energy across a gap without touching — the pen and the tablet on the right of the desk.")

Sana has been drawing sprites for her team's game for two years on the same graphics tablet, and it took a friend's question to make her notice something.

"Where do you charge the pen?"

She turns it over. No port. No battery door. No switch. She has never charged it, never changed a cell in it, and it has never once gone flat.

Then she notices something stranger. She holds the pen a few millimetres above the glass, not touching it, and the cursor still follows her hand across the screen. Lift it to about the height of a matchbox and the cursor freezes where it was. Bring it back down and it wakes up instantly, every time, at the same sort of height.

Nothing is touching. Nothing is stored in the pen. Yet the tablet is powering something in there — and it cares, to the centimetre, exactly how far away the pen is.

## The physics

Under the tablet's surface is a grid of coils. Inside the pen is another coil. That is the whole trick.

Send a current $I_1$ through the tablet's coil and it makes a magnetic field, so some of its flux passes through the pen's coil. Double the current and you double the field everywhere, so you double that flux. The flux linkage of coil 2 is therefore proportional to the current in coil 1:

$$N_2\Phi_2 = M I_1$$

The constant $M$ is the **mutual inductance** of the pair, measured in **henry** (H), just like self-inductance. And by Faraday's law, changing $I_1$ induces an emf in the *other* coil:

$$\varepsilon_2 = -M\frac{dI_1}{dt}$$

Two points are worth pinning down. First, $M$ belongs to the **pair**, not to either coil: drive the pen's coil instead and you would get the same number, $M_{12} = M_{21} = M$. Second, $M$ depends only on geometry and on what lies between the coils — turns, shared area, separation, alignment — and never on the current.

![Three schematic side views of a driving coil and a pick-up coil: aligned and close, lifted apart, and slid to one side, with fewer field lines through the pick-up coil each time](figures/mutual_inductance/coupling-and-alignment.svg "Lift the pick-up coil away or slide it sideways and less of the driving coil's flux passes through it, so M falls — and with it the induced emf.")

That is Sana's matchbox height. Lifting the pen does not change the tablet's current; it changes $M$ itself, until the emf in the pen is too small to run it.

The case you must be able to calculate is **two coaxial solenoids**: a long outer solenoid of $N_1$ turns and length $l$, with a shorter coil of $N_2$ turns wound around its middle, enclosing cross-sectional area $A$.

![A long outer solenoid carrying a changing current with a shorter inner coil wound coaxially inside it, connected to a galvanometer](figures/mutual_inductance/coaxial-solenoids.svg "The outer solenoid's field threads the inner coil, so a changing current in one induces an emf in the other — and M is the same whichever one you drive.")

Inside a long solenoid the field is uniform, $B = \mu_0 N_1 I_1 / l$, and all of it passes through the inner coil, so each of its $N_2$ turns links a flux $BA$:

$$N_2\Phi_2 = N_2 \cdot \frac{\mu_0 N_1 I_1}{l} \cdot A \qquad\Longrightarrow\qquad M = \frac{\mu_0 N_1 N_2 A}{l}$$

This holds for a **long** air-cored solenoid, with the inner coil near the middle so that end effects are negligible.

## Worked example

**Given:** an outer solenoid of $N_1 = 800$ turns over a length $l = 0.40\,\text{m}$, and an inner coil of $N_2 = 50$ turns enclosing $A = 2\times10^{-4}\,\text{m}^2$ (about the area of a postage stamp).
**Find:** $M$, and the emf induced in the inner coil when the outer current changes by $1.0\,\text{A}$ in $0.005\,\text{s}$.

**Step 1 — the geometry factor.** Everything except $\mu_0$ is geometry:

$$\frac{N_1 N_2 A}{l} = \frac{800 \times 50 \times 2\times10^{-4}}{0.40} = \frac{8}{0.40} = 20\,\text{m}$$

**Step 2 — the mutual inductance.** Multiply by $\mu_0 = 4\pi\times10^{-7}\,\text{T}\,\text{m}/\text{A}$:

$$M = (4\pi\times10^{-7})(20) \approx 2.5\times10^{-5}\,\text{H}$$

That is $25\,\mu\text{H}$ — a small coupling, which is what two coils you could hold in one hand should give.

**Step 3 — the emf.** The current changes at $1.0\,\text{A} \div 0.005\,\text{s} = 200\,\text{A/s}$, so

$$|\varepsilon_2| = M\frac{\Delta I_1}{\Delta t} = (2.5\times10^{-5})(200) = 5.0\times10^{-3}\,\text{V}$$

Five millivolts — a hundredth of a small cell, far too little to light anything, but easy to read on a meter.

**Sanity check:** a small coupling and a gentle change should give a small voltage, and it does.

## Where the picture breaks

The coaxial formula assumes the *whole* of the outer solenoid's flux crosses the inner coil. A flat grid under glass and a pen coil a few millimetres wide are nothing like that: most of the tablet's flux misses the pen entirely, which is exactly why alignment and height matter so much and why $M$ is far smaller than a coaxial pair would give. How well two coils share flux has its own measure, the coupling coefficient — you will meet it later.

A real tablet is also more than two coils. The pen's coil sits in a tuned circuit that rings back at the tablet, and the tablet switches rapidly between the wires of its grid to work out where the pen is. All of it depends on an **alternating** drive: a steady current, however large, would induce nothing at all.

And "no battery" does not mean no energy. Every bit of it comes from the tablet's own supply, across the gap, the moment the pen is close enough.

The gaming here is the setting, not an analogy — a tablet is simply where game art gets drawn, and where two coupled coils happen to live.

## Key takeaway

Mutual inductance $M$ measures how well two coils share flux: $N_2\Phi_2 = MI_1$, and a changing current in one induces $\varepsilon_2 = -M\,dI_1/dt$ in the other. It is a property of the pair — the same value whichever coil you drive — and it depends only on geometry, never on the current. For two coaxial solenoids, $M = \mu_0 N_1 N_2 A / l$.
