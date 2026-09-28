---
concept_id: capacitor_energy
interest: smartphones
format: explain
title: The stylus that fills up in twenty seconds
check:
  question: |-
    A capacitor stores $2.0\,\text{J}$ when it is charged to $2.0\,\text{V}$. How much energy does the same capacitor store when charged to $4.0\,\text{V}$?
  options:
    A: |-
      $4.0\,\text{J}$
    B: |-
      $16\,\text{J}$
    C: |-
      $2.0\,\text{J}$
    D: |-
      $8.0\,\text{J}$
  answer: D
  explanation: |-
    $U = \tfrac{1}{2}CV^2$ with $C$ fixed, so doubling $V$ multiplies $U$ by $2^2 = 4$: $4 \times 2.0 = 8.0\,\text{J}$.
  misconceptions:
    A: |-
      Thinks the energy is proportional to the voltage. Doubling $V$ doubles the charge *and* doubles the voltage each bit of charge is pushed through, so the energy goes up four times.
    B: |-
      Thinks the capacitance also doubles because the capacitor holds more charge. $C$ is fixed by the capacitor's construction; only $Q$ and $V$ change, and $U = \tfrac{1}{2}CV^2$ rises by four, not eight.
    C: |-
      Thinks a capacitor has a fixed energy "size", like a tank. The energy depends on how far it is charged; a capacitor has a fixed capacitance, not a fixed energy.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a rainy window: a phone with raindrops on its screen being tapped by a finger, a metal biscuit tin with its lid off, a breadboard with two supercapacitor cells wired in a chain, a stylus and a fitness band with a small display](scenes/smartphones/potential_capacitance.svg "The stylus lying on the desk has no battery inside it. Something else is doing the storing.")

Ananya uses a budget stylus to take notes on her tablet, and she loves one thing about it: when it dies, she plugs it in, counts to twenty, and it works again. Her roommate Sneha's stylus, with a battery, needs an hour.

One evening they watch a teardown video of Ananya's model. Inside there is no battery at all — only a small cylinder the presenter calls a **supercapacitor**.

"So it's better," Sneha says. "Charges in seconds. Why do batteries even exist?"

But Ananya knows the catch: after twenty seconds on the cable, her stylus lasts about half an hour of writing. Sneha's lasts for days.

So a capacitor can take energy in almost instantly, yet runs dry fast. What decides how much energy a charged capacitor is actually holding — and why can't it just hold more?

## The physics

Charging a capacitor means moving charge from one plate to the other **against** the voltage that has already built up. That takes work, and the work is stored as energy.

**The derivation.** When the capacitor already holds charge $q$, the voltage is $v = q/C$. Moving a little more charge $dq$ costs $dW = v\,dq = \dfrac{q}{C}\,dq$. Adding up from $0$ to $Q$:

$$U = \int_0^Q \frac{q}{C}\,dq = \frac{Q^2}{2C}$$

Using $Q = CV$, the same energy can be written three ways:

$$U = \frac{Q^2}{2C} = \frac{1}{2}CV^2 = \frac{1}{2}QV$$

**Why the half.** The voltage rises steadily from $0$ to $V$ as charge goes in, so on average each bit of charge was pushed through only $V/2$. On a $V$–$Q$ graph, the energy is the **area of the triangle** under the line.

![A straight line from the origin to 45 mC at 300 V, with a dashed line at the average voltage of 150 V](figures/capacitor_energy/v-q-line.svg "The energy stored is the triangle's area under the line, ½QV. The charge went in at an average of half the final voltage.")

**Energy density.** For parallel plates, $C = \varepsilon_0 A/d$ and $V = Ed$, so

$$U = \frac{1}{2}\frac{\varepsilon_0 A}{d}(Ed)^2 = \left(\frac{1}{2}\varepsilon_0 E^2\right)(Ad)$$

$Ad$ is the volume between the plates, so the energy can be pictured as stored **in the field**, with energy per unit volume

$$u = \frac{1}{2}\varepsilon_0 E^2$$

That is the limit Ananya is up against: you can only store more by raising $E$, and every insulator breaks down if the field gets too strong.

## Worked example

Take the stylus's supercapacitor as $C = 1.0\,\text{F}$, charged to $V = 2.0\,\text{V}$ (illustrative values).

**Step 1 — the charge it holds.**

$$Q = CV = 1.0 \times 2.0 = 2.0\,\text{C}$$

**Step 2 — the energy stored.** The charge went in at an average of $1.0\,\text{V}$:

$$U = \tfrac{1}{2}QV = \tfrac{1}{2} \times 2.0 \times 2.0 = 2.0\,\text{J}$$

About the energy needed to lift a $1\,\text{kg}$ bag of sugar $20\,\text{cm}$.

**Step 3 — how much room that would take with air.** Air breaks down near $E = 3\times10^6\,\text{V/m}$, so the most it can hold is

$$u = \tfrac{1}{2} \times 8.85\times10^{-12} \times (3\times10^6)^2 \approx 40\,\text{J/m}^3$$

Storing $2.0\,\text{J}$ would need about $0.05\,\text{m}^3$ of field — a 50-litre bucket. The real part is the size of a fingertip, which is why supercapacitors don't use air at all.

**Sanity check:** $\tfrac{1}{2}CV^2 = \tfrac{1}{2} \times 1.0 \times 2.0^2 = 2.0\,\text{J}$, the same answer by the other formula.

## Where the picture breaks

A supercapacitor packs its charge into a layer only molecules thick at the surface of a hugely porous material, so it reaches farads in a small space — but it is still limited to a few volts per cell, and $U = \tfrac{1}{2}CV^2$ still caps its energy at a few joules. A battery stores energy in chemical reactions instead, and holds thousands of joules in the same space; that chemistry is outside this chapter. Also, the stylus can't use all $2.0\,\text{J}$: its electronics stop working once the voltage falls below some minimum, and whatever energy is still left at that point stays unused.

## Key takeaway

A charged capacitor stores $U = \tfrac{1}{2}CV^2 = \dfrac{Q^2}{2C} = \tfrac{1}{2}QV$ — the half because the charge was pushed through an average of half the final voltage. The energy lives in the field, at density $u = \tfrac{1}{2}\varepsilon_0 E^2$. Since $U \propto V^2$, doubling the voltage stores four times the energy.
