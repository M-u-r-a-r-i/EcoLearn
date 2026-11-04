---
concept_id: self_inductance
interest: smartphones
format: explain
title: The coil inside a power bank that looks like useless wire
check:
  question: |-
    Two long air-cored solenoids have the same length and the same cross-sectional area. Solenoid Q has **twice as many turns** as solenoid P. How does the self-inductance of Q compare with that of P?
  options:
    A: |-
      Four times as large
    B: |-
      Twice as large
    C: |-
      The same, since neither coil is carrying any current yet
    D: |-
      Half as large
  answer: A
  explanation: |-
    For a long solenoid $L = \mu_0 N^2 A / l$. Doubling $N$ doubles the field made by each ampere **and** doubles the number of turns that field threads, so $L$ goes up by $2^2 = 4$.
  misconceptions:
    B: |-
      Treats $L$ as proportional to $N$; it goes as $N^2$, because more turns both strengthen the field and catch it more times.
    C: |-
      Thinks inductance depends on the current flowing; $L$ is fixed by the coil's geometry, even when no current flows.
    D: |-
      Imagines the same flux being shared between more turns; in fact the extra turns make more flux, and every turn links all of it.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk at night with a phone on a wireless charging pad, a shake torch, a hand-crank charger, wired earbuds and a coin beside the pad](scenes/smartphones/electromagnetic_induction.svg "Every gadget on this desk depends on changing magnetic fields. This lesson is about a coil that reacts to changes in its own current.")

Riya's power bank died a week after its warranty ran out, so she and her friend Sameer do the obvious thing: they open it up.

Inside are the flat battery cells, a green circuit board, a small black chip — and, right next to the chip, a little coil of thick copper wire, wound tight and soldered in place.

"That's just wire," Sameer says. "Wire in a loop is still wire. For a steady current it does basically nothing — it's almost a short circuit. Why would anyone waste space on it?"

Riya looks it up. The chip, it turns out, switches the current through that coil on and off hundreds of thousands of times every second. And somehow this does-nothing coil is what lets a battery of about $3.7\,\text{V}$ push out the $5\,\text{V}$ a USB port needs.

What can a coil of wire do that a straight piece of the same wire cannot?

## The physics

When a current $I$ flows in a coil, it makes a magnetic field, and that field threads the coil's **own** turns. So the coil has a flux linkage $N\Phi_B$ of its own, and it is proportional to the current:

$$N\Phi_B = LI$$

The constant $L$ is the coil's **self-inductance**, measured in **henry** (H), where $1\,\text{H} = 1\,\text{Wb/A}$.

Now change the current. The flux linkage changes, so by Faraday's law an emf is induced — in the very coil carrying the current:

$$\varepsilon = -L\frac{dI}{dt}$$

By Lenz's law this **back emf** opposes the change. Switch the current on and the coil holds back its rise; switch it off and the coil tries to keep it flowing. A steady current, however large, meets no back emf at all — which is exactly why Sameer thought the coil did nothing.

![A coil connected to a battery through a switch, with a graph showing the current rising gradually to its final value instead of jumping instantly](figures/self_inductance/solenoid-back-emf.svg "A coil fights any change in its own current: it slows the rise when the switch closes, and tries to keep the current going when it opens.")

**For a long solenoid** of $N$ turns, length $l$ and cross-sectional area $A$, the field inside is uniform, $B = \mu_0 N I / l$. Every turn links a flux $BA$, so

$$N\Phi_B = N\cdot\frac{\mu_0 N I}{l}\cdot A \qquad\Longrightarrow\qquad L = \frac{\mu_0 N^2 A}{l}$$

This holds for an **air-cored** solenoid much longer than its radius, ignoring the weaker field near its ends. Notice $L$ depends only on geometry, and on $N^2$: more turns make more field **and** catch it more times.

In the power bank, the chip lets current build up in the coil, then suddenly cuts it off. The current is now falling very fast, so the back emf is large, and it adds to the battery's voltage to push charge out towards the USB port at a higher voltage.

## Worked example

**Given:** an air-cored test coil with $N = 200$ turns wound over a length $l = 0.05\,\text{m}$, enclosing an area $A = 1\times10^{-5}\,\text{m}^2$ (a pencil-thin tube, much longer than it is wide).
**Find:** $L$, and the back emf when the current falls by $0.5\,\text{A}$ in $1\,\mu\text{s}$.

**Step 1 — the geometry.**

$$\frac{N^2 A}{l} = \frac{200^2 \times 1\times10^{-5}}{0.05} = 8\,\text{m}$$

**Step 2 — the inductance.** Multiply by $\mu_0 = 4\pi\times10^{-7}\,\text{T}\,\text{m/A}$:

$$L = 4\pi\times10^{-7}\times 8 \approx 1.0\times10^{-5}\,\text{H} = 10\,\mu\text{H}$$

**Step 3 — how fast the current changes.** $\Delta I/\Delta t = 0.5 \div (1\times10^{-6}) = 5\times10^{5}\,\text{A/s}$.

**Step 4 — the back emf.**

$$|\varepsilon| = L\frac{\Delta I}{\Delta t} = 1.0\times10^{-5}\times 5\times10^{5} = 5\,\text{V}$$

A tiny coil, a modest half an ampere — and the same voltage as a USB port, simply because the change is so fast.

**Sanity check:** switch the same current off a million times more slowly, over a whole second, and the back emf drops to a few microvolts; the speed of the change is doing all the work.

## Where the picture breaks

The coil in a real power bank is short and fat, not a long thin solenoid, and it is wound on a **ferrite** core. The core multiplies the inductance many times over, so $\mu_0 N^2 A/l$ only gives the right idea of how $L$ scales, not the real value.

A real converter is also more than a coil. Diodes or transistors steer the current, and capacitors smooth the output, so the $5\,\text{V}$ stays steady instead of arriving in spikes.

And Sameer was half right. The coil's wire has a small resistance, so even a steady current loses a little energy in it as heat. What steady current never meets is the back emf.

## Key takeaway

A coil opposes changes in its **own** current: $N\Phi_B = LI$ and $\varepsilon = -L\,\dfrac{dI}{dt}$, with $L$ in henry. A steady current feels no back emf; a fast change can produce a large one. For a long air-cored solenoid, $L = \mu_0 N^2 A / l$ — set by geometry alone, and growing as the **square** of the number of turns.
