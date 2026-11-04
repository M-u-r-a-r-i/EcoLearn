---
concept_id: capacitor_dielectric
interest: cricket
format: explain
title: How the curator's moisture meter feels water it never touches
check:
  question: |-
    A parallel-plate capacitor is charged by a battery, then **disconnected**. A dielectric slab with $K = 3$ is slid in so that it completely fills the gap. What happens?
  options:
    A: |-
      The charge stays the same and the voltage falls to one-third.
    B: |-
      The voltage stays the same and the charge triples.
    C: |-
      The charge stays the same and the voltage triples.
    D: |-
      The charge and the voltage both stay the same; only the capacitance changes.
  answer: A
  explanation: |-
    Once disconnected, the charge has nowhere to go, so $Q$ is fixed. The capacitance becomes $3C_0$, so $V = Q/C$ falls to $V_0/3$.
  misconceptions:
    B: |-
      Applies the battery-connected case. Only while the battery stays connected is $V$ held fixed, so that extra charge flows on.
    C: |-
      Thinks a dielectric strengthens the field. The bound charges oppose the field, so both $E$ and $V$ fall.
    D: |-
      Forgets that $C$, $Q$ and $V$ are linked by $C = Q/V$. If $C$ changes and $Q$ is fixed, $V$ must change.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground under a storm cloud with lightning in the distance, a floodlight tower, a curator on the pitch, a car by the boundary and a photographer's flash](scenes/cricket/potential_capacitance.svg "Match morning after a stormy night: the curator's first job is to find out how wet the pitch is underneath.")

Six in the morning on match day, after a night of rain. The covers have just come off, and Lakshmi, the curator, walks out to a good-length spot on the pitch. She pushes the twin metal prongs of a handheld moisture meter into the surface. The display flickers and settles.

"Still damp underneath," she says. "The seamers will like the first hour."

Joel, her new assistant, crouches beside her. The prongs are coated and sealed, and the electronics sit in a plastic handle. "How does it *know* there's water down there? None of it touches the circuit."

"The type I use measures capacitance," Lakshmi says. "Wet soil and dry soil give different readings."

Joel frowns. He thought capacitance was about the size of the plates and the gap between them. Neither of those changes when the pitch gets wet. So what does water have to do with it?

## The physics

**Filling the gap.** Start with a parallel-plate capacitor, $C_0 = \varepsilon_0 A/d$, holding charge $\pm Q$. Fill the gap with a dielectric of dielectric constant $K$. The dielectric polarises, and its bound surface charges reduce the field between the plates from $E_0$ to $E_0/K$. The voltage $V = Ed$ also falls by a factor $K$ for the same $Q$. So $C = Q/V$ rises by a factor $K$:

$$C = K C_0 = \frac{K\varepsilon_0 A}{d}$$

Joel's point is right: $A$ and $d$ don't change. But the material between the plates is part of what sets $C$. Air has $K \approx 1$. Dry soil has a small $K$, only a few. Water has $K \approx 80$ at room temperature. The meter's prongs act as the "plates", the soil between them is the dielectric, and more water means a larger capacitance.

**A slab that only partly fills the gap.** Put a slab of thickness $t$ (less than $d$) between the plates. The field is $E_0$ in the air and $E_0/K$ in the slab:

$$V = E_0(d - t) + \frac{E_0}{K}\,t \quad\Rightarrow\quad C = \frac{\varepsilon_0 A}{d - t + t/K}$$

As far as capacitance goes, the slab behaves like a layer of air only $t/K$ thick.

![A capacitor with plates 4.0 mm apart and a 2.0 mm slab with K = 4 in the middle; the field is E-nought in the air gaps and E-nought over K in the slab](figures/capacitor_dielectric/slab-partial.svg "The slab weakens the field inside it, so it counts as only t/K of air. Here the effective gap drops from 4.0 mm to 2.5 mm.")

**Battery connected, or not?** What changes depends on what is held fixed.

| When the dielectric fills the gap | $C$ | $Q$ | $V$ | $E$ | $U$ |
|---|---|---|---|---|---|
| Battery still connected ($V$ fixed) | $\times K$ | $\times K$ | same | same | $\times K$ |
| Battery disconnected ($Q$ fixed) | $\times K$ | same | $\div K$ | $\div K$ | $\div K$ |

## Worked example

**Given:** an air-filled capacitor with $C_0 = 10\,\text{pF}$ and $d = 4.0\,\text{mm}$ (illustrative values).
**Find:** $C$ (a) with a slab $t = 2.0\,\text{mm}$ thick, $K = 4.0$; (b) completely filled with that material; (c) completely filled with water. Then (d): with only air in the gap, it is charged to $12\,\text{V}$ and disconnected, and a $K = 4.0$ slab is slid in to fill the gap. Find the new voltage and energy.

(a) Effective gap $= d - t + t/K = 4.0 - 2.0 + 0.5 = 2.5\,\text{mm}$. Since $C \propto 1/(\text{effective gap})$:

$$C = 10\,\text{pF} \times \frac{4.0}{2.5} = 16\,\text{pF}$$

(b) $C = KC_0 = 4.0 \times 10 = 40\,\text{pF}$.

(c) $C \approx 80 \times 10 = 800\,\text{pF}$. The water makes a huge difference, which is why the meter can sense it.

(d) Charge before: $Q = C_0V_0 = 10 \times 10^{-12} \times 12 = 1.2 \times 10^{-10}\,\text{C}$. That charge is trapped. With $C = 40\,\text{pF}$:

$$V = \frac{Q}{C} = \frac{1.2 \times 10^{-10}}{40 \times 10^{-12}} = 3.0\,\text{V}$$

Energy before: $\tfrac{1}{2}QV_0 = \tfrac{1}{2} \times 1.2 \times 10^{-10} \times 12 = 7.2 \times 10^{-10}\,\text{J}$. Energy after: $\tfrac{1}{2} \times 1.2 \times 10^{-10} \times 3.0 = 1.8 \times 10^{-10}\,\text{J}$. The energy dropped by a factor of $4 = K$. The field did work pulling the slab in.

**Sanity check:** in (a), $K = 1$ gives an effective gap of $4.0\,\text{mm}$ and $C = C_0$. A slab of air changes nothing. And $16\,\text{pF}$ lies between $10$ (no slab) and $40\,\text{pF}$ (full), as it should.

## Where the picture breaks

The meter is a real device, but soil is not a neat slab between flat plates. The field around two prongs is non-uniform and spreads out, so $\varepsilon_0 A/d$ doesn't apply directly. Real meters are **calibrated** against soil samples of known moisture, not calculated from a formula. Water's $K \approx 80$ also depends on temperature and on how fast the meter's voltage alternates. Salts dissolved in the water let a small current flow, which can distort the reading. The physics idea — more water, more polarisation, more capacitance — is what the meter relies on.

## Key takeaway

A dielectric filling the gap multiplies the capacitance by $K$: $C = K\varepsilon_0 A/d$. A slab of thickness $t$ gives $C = \varepsilon_0 A/(d - t + t/K)$. With the battery connected, $V$ stays fixed and $Q$ rises. With it disconnected, $Q$ stays fixed and $V$, $E$ and $U$ all fall by a factor $K$.
