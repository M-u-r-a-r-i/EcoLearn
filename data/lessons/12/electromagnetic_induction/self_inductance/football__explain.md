---
concept_id: self_inductance
interest: football
format: explain
title: Why the sprinkler switch only sparks on the way off
check:
  question: |-
    The current through a coil of self-inductance $0.10\,\text{H}$ falls steadily from $2.0\,\text{A}$ to zero in $0.010\,\text{s}$. What is the magnitude of the average back emf?
  options:
    A: |-
      $20\,\text{V}$
    B: |-
      $0.20\,\text{V}$
    C: |-
      $0.02\,\text{V}$
    D: |-
      $200\,\text{V}$
  answer: A
  explanation: |-
    $|\varepsilon| = L\dfrac{\Delta I}{\Delta t} = 0.10 \times \dfrac{2.0}{0.010} = 0.10 \times 200 = 20\,\text{V}$.
  misconceptions:
    B: |-
      Works out $L \times I$, as if the back emf depended on the current itself. A steady current of any size gives no back emf at all — only a *changing* current does.
    C: |-
      Multiplies by the time instead of dividing by it. Emf is a rate of change, so the time must go underneath.
    D: |-
      Uses $0.001\,\text{s}$ instead of $0.010\,\text{s}$ — a decimal slip that makes the answer ten times too large.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening football training ground with a contactless card reader at the turnstile, a magnetic-brake training bike on the touchline and a floodlight transformer cabinet](scenes/football/electromagnetic_induction.svg "Three machines around one ground. Every one of them contains a coil that objects to being switched.")

The pitch is watered at nine, and Gurpreet lets Arnav watch how it is done. Each sprinkler line has a valve held open by an electromagnet — a fat coil of wire wrapped around a steel plunger — and an old manual override switch on the box beside it.

Gurpreet flicks the switch up. A click, and water goes up over the penalty area. Nothing else happens.

Four minutes later he flicks it down. A blue spark snaps across the switch contacts, loud enough that Arnav steps back.

"Every time," Gurpreet says. "Never when it goes on. Only when it goes off." He shows Arnav the contacts: pitted and blackened on one side only.

That is the part Arnav cannot let go. Switching **off** is the moment the supply is being *disconnected*. There should be less voltage there, not more — and certainly not enough to push a spark through a gap in the air. So where does the extra push come from?

## The physics

A coil carrying a current makes its own magnetic field, so its own flux threads its own turns. Change the current and that flux changes — and by Faraday's law the coil induces an emf **in itself**. This is **self-induction**.

For a coil with no magnetic material nearby, the flux linkage is proportional to the current:

$$N\Phi_B = LI$$

The constant $L$ is the **self-inductance**, measured in **henry** (H), where $1\,\text{H} = 1\,\text{Wb/A}$. It depends only on geometry — the number of turns, the size and shape of the coil, and what it is wound on.

Putting that into Faraday's law gives the working equation:

$$\varepsilon = -L\frac{dI}{dt}$$

The minus sign is Lenz's law again: the induced emf opposes the *change* in current, which is why it is called the **back emf**. Switch on, and it fights the current's growth, so the current climbs to its final value instead of jumping there. Switch off, and it fights the collapse, straining to keep the current flowing.

![A solenoid in a circuit with a battery and switch, with the back emf opposing the growing current, and a graph of current rising gradually instead of jumping](figures/self_inductance/solenoid-back-emf.svg "Closing the switch: the coil holds the current back, so it rises gradually. Opening it: the coil fights to keep the current going, and something has to give.")

That is Gurpreet's spark. Opening the switch tries to drive the current to zero in about a millisecond, so $dI/dt$ is enormous and $L\,dI/dt$ can be many times the supply voltage — easily enough to ionise the air in the opening gap. Switching *on* is gentle by comparison, because the supply, not a collapsing field, sets the pace.

For a **long** solenoid — length much greater than its radius — with $N$ turns, length $l$ and cross-sectional area $A$, in air:

$$L = \frac{\mu_0 N^2 A}{l}$$

Notice the $N^2$: doubling the turns doubles the flux *and* doubles the number of turns linking it, so $L$ goes up four times.

## Worked example

**Given:** the valve coil has $N = 1000$ turns over a length $l = 0.10\,\text{m}$, enclosing $A = 1\times10^{-4}\,\text{m}^2$ (that is $1\,\text{cm}^2$).
**Find:** its inductance with nothing inside it, and then the back emf when the real coil, which has a steel plunger in it and measures about $L = 0.20\,\text{H}$, has its current of $0.50\,\text{A}$ cut off in $1.0\,\text{ms}$.

**Step 1 — the geometry, on its own.** It is long and thin, so the solenoid formula applies:

$$\frac{N^2 A}{l} = \frac{(1000)^2 \times 1\times10^{-4}}{0.10} = 1000\,\text{m}$$

$$L_\text{air} = \mu_0 \times 1000 = (4\pi\times10^{-7})(1000) \approx 1.3\times10^{-3}\,\text{H}$$

About $1.3\,\text{mH}$ — small, for a coil you could close your hand around. The steel plunger is what lifts the real coil's inductance to the order of tenths of a henry.

**Step 2 — how fast the current dies.** It falls by $0.50\,\text{A}$ in $1.0\times10^{-3}\,\text{s}$:

$$\frac{\Delta I}{\Delta t} = \frac{0.50}{1.0\times10^{-3}} = 500\,\text{A/s}$$

**Step 3 — the back emf.**

$$|\varepsilon| = L\frac{\Delta I}{\Delta t} = 0.20 \times 500 = 100\,\text{V}$$

A hundred volts, from a coil that runs on a low-voltage supply — which is exactly why the contacts are burnt.

**Sanity check:** slow the switching down a hundred times and the emf drops a hundredfold, to about a volt. That is why a deliberately slow switch, or a component that gives the current somewhere to go, stops the sparking.

## Where the picture breaks

A coil is not "storing current", however much the spark makes it feel that way, and it has no momentum. What it stores is energy in its magnetic field, and the back emf follows from Faraday's law, not from inertia. The likeness to mass is a memory aid, nothing more.

The solenoid formula assumes a long, tightly wound, air-cored coil with a uniform field inside and negligible end effects. Put steel inside it, as every real valve does, and $L$ becomes far larger — and no longer a constant, because iron's response to a field is not linear. The $0.20\,\text{H}$ used above is an illustrative value for such a coil, not something you can get from the air-cored formula.

A real switch also sparks for more than one reason at once, including contact bounce and the arc sustaining itself. Self-induction is the main cause here, not the only one. And the football is the setting, not an analogy.

## Key takeaway

A coil opposes changes in its own current: $\varepsilon = -L\,dI/dt$, where the self-inductance $L$, in henry, depends only on geometry — for a long solenoid, $L = \mu_0 N^2 A / l$. A steady current produces no back emf at all; a fast-changing one can produce a very large one, which is why switching a coil off makes a spark.
