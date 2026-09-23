---
concept_id: faradays_law
interest: football
format: explain
title: Pedalling to keep the lamp on at five-a-side
check:
  question: |-
    A generator coil has $200$ turns. The flux through **each turn** changes by $0.005\,\text{Wb}$ in $0.05\,\text{s}$. What is the average emf induced across the coil?
  options:
    A: |-
      $20\,\text{V}$
    B: |-
      $1.0\,\text{V}$
    C: |-
      $0.1\,\text{V}$
    D: |-
      $2.0\,\text{V}$
  answer: A
  explanation: |-
    $|\varepsilon| = N\dfrac{\Delta\Phi_B}{\Delta t} = 200 \times \dfrac{0.005}{0.05} = 200 \times 0.1 = 20\,\text{V}$.
  misconceptions:
    B: |-
      Works out $N\Delta\Phi_B = 200 \times 0.005$ and stops there, forgetting that emf is a *rate* — the flux change must be divided by the time it takes.
    C: |-
      Finds the rate for one turn correctly but never multiplies by the $200$ turns, which are in series and each contribute their own emf.
    D: |-
      Divides by $0.5\,\text{s}$ instead of $0.05\,\text{s}$ — a decimal slip that makes the answer ten times too small.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening football training ground with a contactless card reader at the turnstile, a magnetic-brake training bike on the touchline and a floodlight transformer cabinet](scenes/football/electromagnetic_induction.svg "Three machines around one ground. The physics in this lesson is what makes all three of them possible.")

The lights over the five-a-side cage go out at half past eight, mid-move, and the whole lane goes black. Nikhil has been waiting all week for this game and there are ten minutes left in it.

The caretaker wheels out something odd: an old bicycle frame bolted to a stand, with a small metal drum pressed against the back wheel and two wires running to a work lamp hung on the fence. He tells Nikhil to pedal.

Nikhil pedals. The lamp comes up, dim at first, then bright enough to play by. He pedals harder and it gets brighter still. He stops to catch his breath — and the lamp dies instantly.

He checks the drum. There is a magnet in there, and a coil of wire, and they are still sitting exactly where they were when the lamp was bright. Neither has gone anywhere. So why does *standing still* switch it off?

## The physics

A coil sitting in a magnetic field, however strong, produces nothing at all. What produces an emf is a **change** in the magnetic flux through the coil.

**Faraday's law of induction:** the emf induced in a closed loop equals the negative rate of change of magnetic flux through it. For a coil of $N$ tightly wound turns,

$$\varepsilon = -N\frac{d\Phi_B}{dt}$$

- $\varepsilon$ is the induced emf, in volts.
- $\Phi_B = BA\cos\theta$ is the flux through **one** turn, in weber.
- $N$ multiplies the effect: the turns are in series, so each one adds its own emf.
- The minus sign fixes the *direction* — the induced emf opposes the change that caused it. That is Lenz's law, coming next. For the size alone you can use $|\varepsilon| = N\,|\Delta\Phi_B/\Delta t|$.

![A bar magnet being pushed into a coil connected to a galvanometer, with the needle kicking; below, the magnet resting inside the coil with the needle at zero](figures/faradays_law/magnet-into-coil.svg "The needle kicks while the magnet is moving and sits at zero while the magnet rests inside the coil — flux by itself does nothing, only changing flux does.")

Because $\Phi_B = BA\cos\theta$, there are three ways to induce an emf: move a magnet so $B$ at the coil changes, squash or stretch the loop so $A$ changes, or rotate the coil so $\theta$ changes. A generator like the caretaker's uses the third: spinning the drum swings each turn's flux up and down, over and over.

The graph below is the whole law in one picture. What matters is the **slope** of the flux curve, not its height.

![A graph of flux and induced emf against time: flux ramps up, stays constant, then falls steeply, while the emf is a step that follows the slope](figures/faradays_law/flux-and-emf-vs-time.svg "Where the flux is flat — even where it is largest — the emf is zero. The steepest part of the flux curve gives the biggest emf.")

So Nikhil is answered. Pedalling spins the coil, the flux through it changes fast, and $d\Phi_B/dt$ is large. Freewheel, and the flux settles to a constant value: the slope is zero, and so is the emf. Pedal harder and the same flux swing happens in less time, so the emf — and the brightness — goes up.

## Worked example

**Given:** the generator's coil has $N = 50$ turns. Each half-turn of the drum changes the flux through one turn by $\Delta\Phi_B = 0.004\,\text{Wb}$, and at Nikhil's pedalling rate that takes $\Delta t = 0.02\,\text{s}$.
**Find:** the average emf.

Start with a single turn, so there is only one number to hold:

$$\frac{\Delta\Phi_B}{\Delta t} = \frac{0.004\,\text{Wb}}{0.02\,\text{s}} = 0.2\,\text{V}$$

One loop of wire, on its own, would give a fifth of a volt — not enough to light anything.

Now the $50$ turns act in series, each adding its own share:

$$|\varepsilon| = N\frac{\Delta\Phi_B}{\Delta t} = 50 \times 0.2 = 10\,\text{V}$$

Ten volts, which is about what a small work lamp wants — from nothing but a boy pedalling.

**Sanity check:** pedal twice as fast and the same flux change is squeezed into half the time, so the emf doubles. That matches what Nikhil saw: harder pedalling, brighter lamp.

## Where the picture breaks

Treating the flux change as steady gives one average emf. In the real generator the flux swings smoothly up and down as the coil turns, so the emf rises, falls and reverses many times a second — an alternating voltage, which the average value hides completely. The lamp does not care, but a meter would.

The step from one turn to $N$ turns assumes every turn links the same flux. That holds for a tightly wound coil; in a loose one the outer turns catch less.

And the football here is the setting, not an analogy. A bicycle generator behind a five-a-side cage is a real place to meet induction, not a likeness to anything on the pitch.

## Key takeaway

An emf appears only while the flux through a circuit is *changing*: $\varepsilon = -N\,d\Phi_B/dt$. A steady flux, however large, induces nothing. Faster change means a bigger emf, and more turns multiply it.
