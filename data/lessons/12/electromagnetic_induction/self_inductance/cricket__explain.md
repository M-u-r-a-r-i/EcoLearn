---
concept_id: self_inductance
interest: cricket
format: explain
title: The blue spark when the roller is switched off
check:
  question: |-
    The current through a coil of self-inductance $0.50\,\text{mH}$ is switched off, falling steadily from $2.0\,\text{A}$ to zero in $1.0\,\text{ms}$. What is the magnitude of the average back emf?
  options:
    A: |-
      $0.0010\,\text{V}$
    B: |-
      $0.50\,\text{V}$
    C: |-
      $1.0\,\text{V}$
    D: |-
      $1000\,\text{V}$
  answer: C
  explanation: |-
    $|\varepsilon| = L\dfrac{\Delta I}{\Delta t} = (0.50\times10^{-3}) \times \dfrac{2.0}{1.0\times10^{-3}} = 1.0\,\text{V}$.
  misconceptions:
    A: |-
      Computes $L \times I$, as if the emf depended on the current itself. A steady current of any size gives no back emf at all — only a *changing* current does.
    B: |-
      Divides $L$ by the time but forgets the current change, giving $L/\Delta t$. The formula needs the full rate $\Delta I/\Delta t$.
    D: |-
      Uses $0.50\,\text{H}$ instead of $0.50\,\text{mH}$ — a missing milli, which makes the answer a thousand times too big.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening cricket ground with a walk-through metal-detector arch at the gate, LED bails charging on a pad, and a bowling machine](scenes/cricket/electromagnetic_induction.svg "Three machines at one ground. Every one of them contains a coil that resists being switched.")

Divya has stayed back after practice to help the groundsman put the heavy roller away. He parks it, reaches up to the old metal switchbox on the wall, and pulls the lever down.

A blue spark snaps across the contacts. Loud enough to make her jump.

"Always does that," he says. "Never when I switch it on. Only when I switch it off."

That is the strange bit, and Divya can't let it go. The switch is *breaking* the circuit. The supply is being disconnected. If anything, there should be less voltage at that moment, not enough to punch a spark through a gap in the air. Where does the extra push come from?

## The physics

A coil carrying a current makes its own magnetic field, so it has its own flux threading its own turns. Change the current and you change that flux — and by Faraday's law, the coil induces an emf **in itself**. This is **self-induction**.

For a coil with no magnetic material nearby, the flux linkage is proportional to the current:

$$N\Phi_B = LI$$

The constant $L$ is the **self-inductance**, measured in **henry** (H), where $1\,\text{H} = 1\,\text{Wb/A}$. It depends only on geometry — the number of turns, the size and shape, and what the coil is wound on.

Putting that into Faraday's law gives the equation you will use:

$$\varepsilon = -L\frac{dI}{dt}$$

The minus sign is Lenz's law again: the induced emf opposes the *change* in current. It is called the **back emf**. Switch on, and it fights the current's growth, so the current climbs to its steady value instead of jumping there. Switch off, and it fights the current's collapse, trying to keep it flowing.

![A solenoid in a circuit with a battery and switch, with the back emf opposing the growing current, and a graph of current rising gradually instead of jumping](figures/self_inductance/solenoid-back-emf.svg "Closing the switch: the coil holds the current back, so it rises gradually. Opening it: the coil tries to keep the current going.")

That is Divya's spark. Opening the switch tries to drive the current to zero in well under a millisecond. With $dI/dt$ enormous, $L\,dI/dt$ can be hundreds of times the supply voltage — easily enough to ionise the air in the widening gap. Switching *on* is gentler, because the supply, not the collapsing field, sets the pace.

For a **long** solenoid — length much greater than its radius — of $N$ turns, length $l$ and cross-sectional area $A$, in air:

$$L = \frac{\mu_0 N^2 A}{l}$$

Notice $N^2$: doubling the turns doubles the flux *and* doubles the number of turns it links, so $L$ goes up four times.

## Worked example

**Given:** a solenoid with $N = 1000$ turns, length $l = 0.5\,\text{m}$ and cross-sectional area $A = 2\times10^{-4}\,\text{m}^2$ (about $2\,\text{cm}^2$), wound on a hollow former.
**Find:** its self-inductance, and the back emf when the current through it changes by $4\,\text{A}$ in $0.01\,\text{s}$.

It is long and thin, so the solenoid formula applies:

$$L = \frac{\mu_0 N^2 A}{l} = \frac{(4\pi\times10^{-7})(1000)^2(2\times10^{-4})}{0.5}$$

Work out the geometry factor first: $N^2 A/l = 10^6 \times 2\times10^{-4} / 0.5 = 400\,\text{m}$. So $L = 4\pi\times10^{-7} \times 400 \approx 5\times10^{-4}\,\text{H}$, that is **half a millihenry** — a small coil you could hold in your palm.

Now the rate of change of current is $4\,\text{A}$ in $0.01\,\text{s}$, or $400\,\text{A/s}$:

$$|\varepsilon| = L\frac{\Delta I}{\Delta t} = (5\times10^{-4})(400) = 0.2\,\text{V}$$

A fifth of a volt — nothing dramatic, because a hundredth of a second is a slow change for a coil.

**Sanity check:** the same current change forced into a thousandth of the time would give a hundred times the emf, which is exactly why the groundsman's fast-opening switch sparks and this gentle change does not.

## Where the picture breaks

The coil is not "storing current" or "having momentum", however much it feels that way. What it stores is energy in its magnetic field, and the back emf is a consequence of Faraday's law, not of inertia. The likeness to mass is a memory aid and nothing more.

The solenoid formula assumes a long, tightly wound, air-cored coil with uniform field inside and negligible end effects. Put an iron core in it — as a real motor has — and $L$ becomes far larger and no longer constant, because iron's response to the field is not linear.

And note the story's honesty limit: a genuine motor switch sparks for several reasons at once, including contact bounce and the arc itself. Self-induction is the main one, not the only one. The cricket here is the setting, not an analogy.

## Key takeaway

A coil opposes changes in its own current: $\varepsilon = -L\,dI/dt$, where the self-inductance $L$ (in henry) depends only on geometry — for a long solenoid, $L = \mu_0 N^2 A/l$. A steady current produces no back emf; a fast-changing one can produce a very large one, which is why switching a coil off makes a spark.
