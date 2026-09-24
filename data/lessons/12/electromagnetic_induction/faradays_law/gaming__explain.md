---
concept_id: faradays_law
interest: gaming
format: explain
title: The earbud that worked as a microphone at 1 a.m.
check:
  question: |-
    Neel winds a second coil of $20$ turns and flicks a magnet past it, so that the flux through **each turn** changes by $0.004\,\text{Wb}$ in $0.02\,\text{s}$. What average emf does the coil produce?
  options:
    A: |-
      $0.08\,\text{V}$
    B: |-
      $0.2\,\text{V}$
    C: |-
      $40\,\text{V}$
    D: |-
      $4.0\,\text{V}$
  answer: D
  explanation: |-
    $|\varepsilon| = N\dfrac{\Delta\Phi_B}{\Delta t} = 20 \times \dfrac{0.004\,\text{Wb}}{0.02\,\text{s}} = 20 \times 0.2 = 4.0\,\text{V}$.
  misconceptions:
    A: |-
      Works out the total flux linkage $N\Delta\Phi_B = 0.08\,\text{Wb}$ and calls it an emf. Emf is a *rate* of change of flux, so the time must divide it.
    B: |-
      Gets the rate per turn right but forgets the $20$ turns. The turns are in series, so each one adds its own emf.
    C: |-
      Divides by $0.002\,\text{s}$ instead of $0.02\,\text{s}$ — a decimal slip that makes the answer ten times too large.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming corner at night: a pinball game on the monitor, a headset charging on a pad, a controller cut away at its rumble motor, a tablet pen hovering over a tablet, and an arcade coin chute with a magnet](scenes/gaming/electromagnetic_induction.svg "Five gaming machines, and in each one a magnetic field is changing. This lesson is about the law that turns that change into a voltage.")

It is nearly one in the morning, Neel's squad is two rounds from the top of the ladder, and his headset microphone has just died.

His teammate, on a call from two streets away, tells him to pull an earbud out of his phone, plug it into the microphone socket and talk into that instead. Neel is fairly sure he is being wound up. He tries it anyway.

They hear him. Quieter and boomier than usual, but every word.

An earbud is a *speaker*. Nobody built it to listen. And here is the part he cannot let go of: the instant he stops talking, the level meter drops flat, even though the tiny magnet and the coil inside the earbud are sitting exactly where they were a moment ago. So where is the signal coming from, and why does it vanish the moment he goes quiet?

## The physics

Inside most earbuds is a **moving-coil driver**: a light coil of wire glued to a thin diaphragm, hanging in the field of a small permanent magnet. Normally you push current through the coil and the diaphragm pushes air. Run it the other way — let sound push the diaphragm — and the coil moves through the magnet's field, so the flux through the coil changes. That is all it takes.

**Faraday's law of induction:** the emf induced in a closed loop equals the negative rate of change of magnetic flux through it. For a coil of $N$ tightly wound turns,

$$\varepsilon = -N\frac{d\Phi_B}{dt}$$

- $\varepsilon$ is the induced emf, in volts.
- $\Phi_B = BA\cos\theta$ is the flux through **one** turn, in weber.
- $N$ multiplies the effect, because the turns sit in series and each contributes its own emf.
- The minus sign fixes the *direction*: the induced emf opposes the change that caused it. That is Lenz's law, coming next; for the size of the emf, use $|\varepsilon| = N\,|\Delta\Phi_B/\Delta t|$.

![A bar magnet being pushed into a coil connected to a galvanometer, with the needle kicking; below, the magnet resting inside the coil with the needle at zero](figures/faradays_law/magnet-into-coil.svg "The needle kicks while the magnet moves and reads zero while it sits still inside the coil — flux on its own does nothing, only a changing flux does.")

Since $\Phi_B = BA\cos\theta$, there are three ways in: move the magnet or coil so $B$ at the coil changes, change the area $A$, or turn the coil so $\theta$ changes. The earbud uses the first.

The graph below is the whole law in one picture — what matters is the **slope** of the flux, not its height.

![A graph of flux and induced emf against time: flux ramps up, stays constant, then falls steeply, while the emf is a step that follows the slope](figures/faradays_law/flux-and-emf-vs-time.svg "Where the flux is steady — even at its largest — the emf is zero. The steepest change in flux gives the biggest emf.")

So Neel's silence is answered. Quiet means a motionless diaphragm, constant flux, zero slope, no emf — with the magnet still right there.

## Worked example

**Given:** Neel wants to see the effect properly, so he winds $N = 100$ turns of wire around a mug. He pulls a strong magnet out of the coil in $\Delta t = 0.05\,\text{s}$, and the flux through each turn falls by $\Delta\Phi_B = 0.001\,\text{Wb}$ (an illustrative value for a small strong magnet).
**Find:** the average emf induced.

Take one turn first. Its flux changes at

$$\frac{\Delta\Phi_B}{\Delta t} = \frac{0.001\,\text{Wb}}{0.05\,\text{s}} = 0.02\,\text{V}$$

Two hundredths of a volt from a single loop of wire — far too little to notice.

Now all one hundred turns act in series:

$$|\varepsilon| = N\frac{\Delta\Phi_B}{\Delta t} = 100 \times 0.02 = 2.0\,\text{V}$$

About the voltage of a small cell, from a mug, some wire and one quick pull.

**Sanity check:** pull the magnet out twice as fast and the same flux change is squeezed into half the time, so the emf doubles — which is exactly why a sharp yank gives a bigger kick on the meter than a slow one.

## Where the picture breaks

The worked example treats the flux as changing steadily, which gives one average emf. Speech does nothing of the sort: the diaphragm wobbles back and forth hundreds of times a second, so the real emf is a rapidly alternating signal whose average over any word is close to zero.

The earbud also produces far less than two volts. Its coil is a few millimetres across and moves by a fraction of a millimetre, so its output is a small fraction of a millivolt, and the microphone input's amplifier does the rest of the work. A speaker run backwards is a genuinely poor microphone — it is built to push air, not to be pushed by it — which is why Neel sounded boomy and quiet.

The step "$N$ turns in series" also assumes every turn links the same flux, which holds only for a tightly wound coil.

And the gaming is the setting, not an analogy. A headset at 1 a.m. is simply a place where a coil and a magnet meet.

## Key takeaway

An emf appears only while the flux through a circuit is *changing*: $\varepsilon = -N\,d\Phi_B/dt$. A steady flux, however large, induces nothing. Faster change means a bigger emf, and more turns multiply it.
