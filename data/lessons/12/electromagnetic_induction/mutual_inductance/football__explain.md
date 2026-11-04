---
concept_id: mutual_inductance
interest: football
format: explain
title: The humming cabinet under the floodlight
check:
  question: |-
    The primary coil of a transformer is connected to a battery and carries a **steady** direct current of $5\,\text{A}$. What emf appears across the secondary?
  options:
    A: |-
      $5M$ volts, since the emf across the secondary is $MI$.
    B: |-
      A large one, because the primary current is large.
    C: |-
      A small one but not zero, because some flux always leaks across.
    D: |-
      Zero, because a steady current means no change of flux.
  answer: D
  explanation: |-
    $\varepsilon_2 = -M\,dI_1/dt$ depends on the *rate of change* of the primary current. A steady current, however large, gives $dI_1/dt = 0$ and so no induced emf — which is why transformers only work on alternating current.
  misconceptions:
    A: |-
      Uses $MI$ instead of $M\,dI/dt$. $MI_1$ is the flux linkage of the secondary, measured in weber, not an emf in volts — the units alone rule it out.
    B: |-
      Assumes a big current must mean a big induced emf. The size of the current is irrelevant; only how fast it changes matters.
    C: |-
      Confuses imperfect coupling with induction. Leakage flux reduces $M$, but a flux that is not changing induces nothing however it is shared.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening football training ground with a contactless card reader at the turnstile, a magnetic-brake training bike on the touchline and a floodlight transformer cabinet](scenes/football/electromagnetic_induction.svg "Three machines around one ground. This lesson is about two coils that pass energy across a gap without touching.")

Nivedita is waiting for her sister's match to start and has nothing to do except listen to the grey cabinet at the corner of the ground. It hums. When the floodlights come on, it hums louder.

The maintenance engineer has the door open, so Nivedita asks what is inside. He shows her: two bundles of wire, wound one on each side of a block of grey steel plates stacked like a pack of cards.

She traces the thick cable coming in. It goes to the first coil, loops round and round, and goes back out the way it came. It never reaches the second coil. The wires going out to the lights come off the *other* coil entirely.

The two coils are not joined. She checks twice.

So the whole power for those floodlights — kilowatts of it — is crossing a gap between two pieces of wire that never touch. How?

## The physics

Send a current $I_1$ through coil 1 and it makes a magnetic field, so some of its flux passes through coil 2. Double the current and you double the field everywhere, so you double that flux. The flux linkage of coil 2 is therefore proportional to the current in coil 1:

$$N_2\Phi_2 = M I_1$$

The constant $M$ is the **mutual inductance** of the pair, measured in **henry** (H), just like self-inductance. And by Faraday's law, changing $I_1$ induces an emf in the *other* coil:

$$\varepsilon_2 = -M\frac{dI_1}{dt}$$

Two points are worth pinning down. First, $M$ belongs to the **pair**, not to either coil: drive coil 2 instead and you get the same number, $M_{12} = M_{21} = M$. Second, $M$ depends only on geometry and on what lies between the coils — the turns, the shared area, the separation and the alignment — never on the current.

![Three schematic side views of a driving coil and a pick-up coil: aligned and close, lifted apart, and slid to one side, with fewer field lines through the pick-up coil each time](figures/mutual_inductance/coupling-and-alignment.svg "Lift the second coil away or slide it sideways and less of the first coil's flux threads it, so M falls. Sharing a steel core is how a transformer keeps M as large as possible.")

That is what the stacked steel plates in the cabinet are for: they carry almost all of the first coil's flux round to the second, so hardly any of it escapes.

The case you must be able to calculate is **two coaxial solenoids**: a long outer solenoid of $N_1$ turns and length $l$, with a shorter coil of $N_2$ turns wound around its middle, enclosing cross-sectional area $A$.

![A long outer solenoid carrying a changing current with a shorter inner coil wound coaxially inside it, connected to a galvanometer](figures/mutual_inductance/coaxial-solenoids.svg "The outer solenoid's field threads the inner coil, so a changing current in either one induces an emf in the other — and M is the same number whichever one you drive.")

Inside a long solenoid the field is uniform, $B = \mu_0 N_1 I_1 / l$. All of it passes through the inner coil, so each of its $N_2$ turns links a flux $BA$:

$$N_2\Phi_2 = N_2 \cdot \frac{\mu_0 N_1 I_1}{l} \cdot A \qquad\Longrightarrow\qquad M = \frac{\mu_0 N_1 N_2 A}{l}$$

This holds for a **long** air-cored solenoid — length much greater than its radius — with the inner coil near the middle, so that end effects are negligible and the whole of $A$ sits in the uniform field.

## Worked example

**Given:** a long solenoid with $N_1 = 1000$ turns over $l = 0.50\,\text{m}$, and a second coil of $N_2 = 200$ turns wound round its middle, enclosing $A = 5\times10^{-4}\,\text{m}^2$.
**Find:** $M$, and the emf induced in the second coil when the first one's current changes by $4.0\,\text{A}$ in $0.020\,\text{s}$.

**Step 1 — the geometry, all in one number.** Everything except $\mu_0$ is geometry:

$$\frac{N_1 N_2 A}{l} = \frac{1000 \times 200 \times 5\times10^{-4}}{0.50} = 200\,\text{m}$$

**Step 2 — the mutual inductance.** Multiply by $\mu_0 = 4\pi\times10^{-7}\,\text{T}\,\text{m}/\text{A}$:

$$M = (4\pi\times10^{-7})(200) \approx 2.5\times10^{-4}\,\text{H}$$

That is a quarter of a millihenry — a modest coupling, which is what you expect from two coils you could hold in one hand.

**Step 3 — how fast the current changes.**

$$\frac{\Delta I_1}{\Delta t} = \frac{4.0\,\text{A}}{0.020\,\text{s}} = 200\,\text{A/s}$$

**Step 4 — the emf.**

$$|\varepsilon_2| = M\frac{\Delta I_1}{\Delta t} = (2.5\times10^{-4})(200) = 0.050\,\text{V}$$

Fifty millivolts: far too little to light anything, but easy to read on a meter.

**Sanity check:** a small coupling and a fairly gentle change should give a small voltage, and they do. Change the current a hundred times faster and you would get about five volts.

## Where the picture breaks

The coaxial formula assumes the *whole* of the first solenoid's flux crosses the second coil. Two coils facing each other across air are nothing like that — most of the flux misses, which is why alignment matters so much and why a steel core is worth the trouble. How well two coils share flux has its own measure, the coupling coefficient, which you will meet later.

The cabinet is also more than two coils. It runs on **alternating** current, because a steady current induces nothing however large it is; its core is built from insulated plates to keep eddy currents down; and some energy is lost as heat in both the windings and the core. The hum itself is the core flexing as the field reverses, which is not part of the ideal picture at all.

And the football here is the setting, not an analogy. A floodlight transformer is simply where you meet two coupled coils.

## Key takeaway

Mutual inductance $M$ measures how well two coils share flux: $N_2\Phi_2 = MI_1$, and a changing current in one induces $\varepsilon_2 = -M\,dI_1/dt$ in the other. It is a property of the pair — the same value whichever coil you drive — and it depends only on geometry, never on the current. For two coaxial solenoids, $M = \mu_0 N_1 N_2 A / l$.
