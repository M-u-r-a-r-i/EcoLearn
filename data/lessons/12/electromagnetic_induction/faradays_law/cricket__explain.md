---
concept_id: faradays_law
interest: cricket
format: explain
title: The torch with no battery at the nets
check:
  question: |-
    A coil of $20$ turns is wound on the handle of a shake torch. As the magnet slides through, the flux through **each turn** changes by $0.01\,\text{Wb}$ in $0.10\,\text{s}$. What is the average emf induced?
  options:
    A: |-
      $0.01\,\text{V}$
    B: |-
      $0.20\,\text{V}$
    C: |-
      $2.0\,\text{V}$
    D: |-
      $20\,\text{V}$
  answer: C
  explanation: |-
    $|\varepsilon| = N\dfrac{\Delta\Phi}{\Delta t} = 20 \times \dfrac{0.01}{0.10} = 2.0\,\text{V}$.
  misconceptions:
    A: |-
      Reports the flux change itself as the emf, forgetting both the number of turns and the division by time — emf is a *rate*, not an amount of flux.
    B: |-
      Multiplies by the number of turns but not by $1/\Delta t$ (or divides by $0.10$ twice over in the wrong place); the $0.10\,\text{s}$ must divide the flux change.
    D: |-
      Divides by $0.01\,\text{s}$ instead of $0.10\,\text{s}$ — a decimal slip that makes the answer ten times too large.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening cricket ground with a walk-through metal-detector arch at the gate, LED bails charging on a pad, and a bowling machine](scenes/cricket/electromagnetic_induction.svg "Three machines at one ground. The physics in this lesson is what makes all three of them possible.")

The floodlights at the practice nets cut out at eight o'clock sharp, and the whole maidan goes dark. Rohan, the youngest in the group, still has twenty balls left to bowl.

His coach pulls a fat plastic torch out of her bag and starts shaking it — not tapping it, not switching it on, just shaking it back and forth like a shaker. After a few seconds the torch glows, bright enough to see the popping crease.

Rohan opens it later. No battery. Just a magnet that slides up and down a tube, a coil of wire around the middle, and a small bulb.

Here is the strange part. When the coach stopped shaking and held the torch dead still — with the magnet sitting right inside the coil, as close as it ever gets — the light went out at once. The magnet was still there. The coil was still there. So why does standing still switch it off?

## The physics

A coil sitting in a magnetic field, however strong, produces nothing. What produces an emf is a **change** in the magnetic flux through the coil.

**Faraday's law of induction:** the emf induced in a closed loop equals the negative rate of change of magnetic flux through it. For a coil of $N$ tightly wound turns,

$$\varepsilon = -N\frac{d\Phi_B}{dt}$$

- $\varepsilon$ is the induced emf, in volts.
- $\Phi_B = BA\cos\theta$ is the flux through **one** turn, in weber.
- $N$ multiplies the effect because the turns are in series: each one contributes its own emf.
- The minus sign gives the *direction*: the induced emf opposes the change that caused it. That is Lenz's law, which you meet next; for the size of the emf you can work with $|\varepsilon| = N\,|\Delta\Phi_B/\Delta t|$.

![A bar magnet being pushed into a coil connected to a galvanometer, with the needle kicking; below, the magnet resting inside the coil with the needle at zero](figures/faradays_law/magnet-into-coil.svg "The needle kicks while the magnet moves and reads zero while it sits still inside the coil — flux alone does nothing, only a changing flux does.")

Since $\Phi_B = BA\cos\theta$, you can induce an emf by moving a magnet (changing $B$ at the coil), by squashing or stretching the loop (changing $A$), or by rotating the coil (changing $\theta$). A generator uses the third.

The graph below is the whole law in one picture: what matters is the **slope** of the flux, not its height.

![A graph of flux and induced emf against time: flux ramps up, stays constant, then falls steeply, while the emf is a step that follows the slope](figures/faradays_law/flux-and-emf-vs-time.svg "Where the flux is steady — even at its largest — the emf is zero. The steepest fall in flux gives the biggest emf.")

So the torch is answered. Shaking it drives the magnet through the coil, so the flux swings rapidly and $d\Phi_B/dt$ is large. Hold it still and the flux is large but constant, the slope is zero, and the bulb goes dark.

## Worked example

**Given:** the torch's coil has $N = 20$ turns. One shake pushes the magnet past it, changing the flux through each turn by $0.01\,\text{Wb}$, and the pass takes $0.10\,\text{s}$.
**Find:** the average induced emf.

Faraday's law with average values:

$$|\varepsilon| = N\frac{\Delta\Phi_B}{\Delta t} = 20 \times \frac{0.01\,\text{Wb}}{0.10\,\text{s}}$$

Take the rate for a single turn first: $0.01/0.10 = 0.1\,\text{V}$ per turn — small, about a tenth of a torch cell.

Now all twenty turns act in series:

$$|\varepsilon| = 20 \times 0.1 = 2.0\,\text{V}$$

That is roughly the voltage of a single small cell — enough to light an LED, which is exactly what the torch does.

**Sanity check:** shake faster and the same flux change happens in less time, so the emf rises — which matches the fact that the torch glows brighter when you shake it harder.

## Where the picture breaks

The example treats the flux change as steady, giving one average emf. In a real shake torch the magnet speeds up and slows down, so the emf rises and falls through each pass and even reverses — the torch flickers at the shaking rate, and the average value hides that.

The "$N$ turns in series" step assumes every turn links the same flux. That is only true for a tightly wound coil; in a loosely wound one, the outer turns catch less.

And the cricket here is the setting, not an analogy. A torch at the nets is a place where induction genuinely happens — there is no deeper likeness between bowling and flux.

## Key takeaway

An emf appears only while the flux through a circuit is *changing*: $\varepsilon = -N\,d\Phi_B/dt$. A steady flux, however large, induces nothing. Faster change means bigger emf, and more turns multiply it.
