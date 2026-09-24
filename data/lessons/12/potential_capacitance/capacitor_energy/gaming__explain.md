---
concept_id: capacitor_energy
interest: gaming
format: explain
title: Why the power light fades instead of blinking out
check:
  question: |-
    A $50\,\mu\text{F}$ capacitor is charged to $40\,\text{V}$. How much energy does it store?
  options:
    A: |-
      $8.0 \times 10^{-2}\,\text{J}$
    B: |-
      $1.0 \times 10^{-3}\,\text{J}$
    C: |-
      $4.0 \times 10^{-2}\,\text{J}$
    D: |-
      $4.0 \times 10^{4}\,\text{J}$
  answer: C
  explanation: |-
    $U = \tfrac{1}{2}CV^2 = \tfrac{1}{2} \times 50\times10^{-6} \times (40)^2 = \tfrac{1}{2} \times 5.0\times10^{-5} \times 1600 = 4.0\times10^{-2}\,\text{J}$.
  misconceptions:
    A: |-
      Uses $CV^2$ and drops the $\tfrac{1}{2}$, as if every coulomb had been carried across at the full $40\,\text{V}$. The voltage climbs from zero while charging, so the average is only $V/2$.
    B: |-
      Uses $\tfrac{1}{2}CV$ and forgets to square the voltage. Raising $V$ raises the charge *and* the voltage each bit of charge is pushed through, so the energy goes as $V^2$.
    D: |-
      Substitutes $50$ for the capacitance without converting microfarads to farads, making the answer a million times too big.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk with a monitor showing rings of equal potential around a charge, a phone with a fingertip on its screen, an old picture tube on the bench and an opened power supply with two big capacitors](scenes/gaming/potential_capacitance.svg "Two fat cylinders inside that opened power supply. After the plug comes out, they are the only things on the desk still holding energy.")

Neha's home arcade cabinet has been rewired about four times this year, and tonight she is pulling the plug on it mid-argument to prove a point to Dhruv.

She yanks the cable out of the wall. The screen dies instantly. But the little white power light on the front panel does not: it holds for a moment, dims, and fades out over about two seconds.

"Leftover electricity draining out of the wires," Dhruv says.

Neha doesn't buy it. The wires inside are short, and they are just copper. She has also seen the warning label pasted on the power supply: *do not open, capacitors may hold a charge*. Two fat cylinders in there are the only things that look like they could be storing anything.

So where was the energy for those two seconds of glow being kept, and how much of it is there — enough to light a lamp, or enough to hurt?

## The physics

Charging a capacitor means dragging charge from one plate to the other **against** the voltage that has already built up between them. That takes work, and the work is stored.

**The derivation.** Suppose the capacitor already holds charge $q$, so the voltage across it is $v = q/C$. Moving one more small charge $dq$ across costs

$$dW = v\,dq = \frac{q}{C}\,dq$$

Adding from $q = 0$ up to $q = Q$:

$$U = \int_0^Q \frac{q}{C}\,dq = \frac{Q^2}{2C}$$

and with $Q = CV$ the same energy can be written three ways:

$$U = \frac{Q^2}{2C} = \frac{1}{2}CV^2 = \frac{1}{2}QV$$

**Where the half comes from.** The voltage rises steadily from $0$ to $V$ as the charge goes in, so on average each bit of charge crossed only $V/2$ — not the final $V$. On a graph of $V$ against $q$ the stored energy is the **area of the triangle** under the straight line.

![A straight line from the origin to 45 mC at 300 V, with a dashed line at the average voltage of 150 V](figures/capacitor_energy/v-q-line.svg "The energy stored is the triangle's area under the line, ½QV. The charge went in at an average of half the final voltage.")

**Energy density.** For parallel plates, $C = \varepsilon_0 A/d$ and $V = Ed$, so

$$U = \frac{1}{2}\frac{\varepsilon_0 A}{d}(Ed)^2 = \left(\frac{1}{2}\varepsilon_0 E^2\right)\times (Ad)$$

The bracket is energy per unit volume and $Ad$ is the volume between the plates, where the field is. So the energy can be regarded as living **in the electric field itself**, at

$$u = \frac{1}{2}\varepsilon_0 E^2$$

a result that holds for any electrostatic field in vacuum, capacitor or not.

## Worked example

Take the cabinet's bulk capacitor as $C = 1000\,\mu\text{F} = 1.0\times10^{-3}\,\text{F}$, charged to $V = 20\,\text{V}$ (illustrative values), and let the power light fade over about $2.0\,\text{s}$.

**Find:** the stored energy, and the average power it delivers while fading.

**Step 1 — the charge it holds.**

$$Q = CV = 1.0\times10^{-3} \times 20 = 0.020\,\text{C}$$

**Step 2 — the energy.** Using $U = \tfrac{1}{2}QV$, since the charge went in at an average of $10\,\text{V}$:

$$U = \tfrac{1}{2} \times 0.020 \times 20 = 0.20\,\text{J}$$

**Step 3 — the average power over the fade.**

$$P_\text{avg} = \frac{U}{t} = \frac{0.20\,\text{J}}{2.0\,\text{s}} = 0.10\,\text{W}$$

A tenth of a watt is about right for a small indicator light — so Neha's two-second glow is exactly the size of thing this capacitor could pay for.

**Sanity check:** $\tfrac{1}{2}CV^2 = \tfrac{1}{2}\times1.0\times10^{-3}\times400 = 0.20\,\text{J}$, the same number by a different route. And $0.2\,\text{J}$ is roughly the work of lifting a school bag one centimetre — enough for a light, nowhere near enough to hurt at $20\,\text{V}$.

## Where the picture breaks

The fade is not the neat constant-power drain that Step 3 assumes: as charge leaves, $V$ falls, so the light dims rather than switching off, and $0.10\,\text{W}$ is only an average over the two seconds. The capacitor is also not alone — the supply has a circuit around it that keeps working for a moment after the plug comes out. And the warning label is about a *different* capacitor from the one in this example: the ones on the mains side of a power supply sit at hundreds of volts, and since $U \propto V^2$, the same capacitance at $300\,\text{V}$ holds over two hundred times the energy of the same part at $20\,\text{V}$. That is the one to respect. One more subtlety for later: when a battery charges a capacitor through a resistance, the source supplies $QV$ but only $\tfrac{1}{2}QV$ ends up stored — the other half is lost as heat on the way.

## Key takeaway

A charged capacitor stores $U = \tfrac{1}{2}CV^2 = Q^2/2C = \tfrac{1}{2}QV$. The half is there because the charge was moved through an average of only half the final voltage. The energy can be pictured as sitting in the field, with density $u = \tfrac{1}{2}\varepsilon_0 E^2$ — and because $U$ goes as $V^2$, doubling the voltage quadruples the stored energy.
