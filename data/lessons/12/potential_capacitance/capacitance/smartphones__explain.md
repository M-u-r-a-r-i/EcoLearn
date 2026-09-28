---
concept_id: capacitance
interest: smartphones
format: explain
title: How a phone knows you turned it sideways
check:
  question: |-
    A parallel-plate capacitor has plates of area $1.0\times10^{-2}\,\text{m}^2$ separated by an air gap of $0.885\,\text{mm}$. It is connected across a $5.0\,\text{V}$ USB supply. How much charge does each plate hold? Take $\varepsilon_0 = 8.85\times10^{-12}\,\text{C}^2\text{N}^{-1}\text{m}^{-2}$.
  options:
    A: |-
      $5.0\times10^{-10}\,\text{C}$
    B: |-
      $2.0\times10^{-11}\,\text{C}$
    C: |-
      $5.0\times10^{-13}\,\text{C}$
    D: |-
      $1.0\times10^{-10}\,\text{C}$
  answer: A
  explanation: |-
    $C = \varepsilon_0 A/d = 8.85\times10^{-12} \times 1.0\times10^{-2} / 8.85\times10^{-4} = 1.0\times10^{-10}\,\text{F}$, so $Q = CV = 1.0\times10^{-10} \times 5.0 = 5.0\times10^{-10}\,\text{C}$.
  misconceptions:
    B: |-
      Divides instead of multiplying, using $Q = C/V$. Capacitance is charge *per volt*, so the charge is $C$ times $V$.
    C: |-
      Leaves the gap in millimetres. $0.885\,\text{mm} = 8.85\times10^{-4}\,\text{m}$; using $0.885$ makes $C$ a thousand times too small.
    D: |-
      Thinks capacitance is the charge the capacitor holds. $1.0\times10^{-10}$ is the capacitance in farads, the charge per volt; the charge also depends on the voltage applied.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a rainy window: a phone with raindrops on its screen being tapped by a finger, a metal biscuit tin with its lid off, a breadboard with two supercapacitor cells wired in a chain, a stylus and a fitness band with a small display](scenes/smartphones/potential_capacitance.svg "Capacitors are everywhere on this desk — in the touchscreen, the breadboard, and hidden inside the phone in places you would not expect.")

Zoya is lying on the sofa watching a cricket highlights clip, phone upright. She turns it on its side and the video swings round to fill the screen. Turns it back; it swings back.

Her dad, Irshad, who repairs phones for a living, is sitting beside her. "You know there's nothing loose in there? No little ball rolling about, no pendulum."

"Then how does it know which way is down?"

"A chip smaller than a grain of rice. It also counts your steps when you walk."

Zoya looks at the phone. A chip is solid silicon, and her physics teacher said chips just switch voltages on and off. Tilting a phone doesn't change any voltage. So what could a sealed, solid chip possibly contain that *feels* which way it is being tilted, and turns that feeling into a number?

## The physics

Put charge $+Q$ on one conductor and $-Q$ on a nearby one. A potential difference $V$ appears between them, and doubling $Q$ doubles $V$. The ratio is fixed by the conductors' shape, size, spacing and the material between them — not by how much charge is on them. That ratio is the **capacitance**:

$$C = \frac{Q}{V}$$

Its SI unit is the **farad**, $1\,\text{F} = 1\,\text{C/V}$. A farad is huge, so real values are usually in $\mu\text{F}$, $\text{nF}$ or $\text{pF}$ ($10^{-12}\,\text{F}$).

**The parallel-plate capacitor.** Two plates of area $A$, a distance $d$ apart, with vacuum (or air) between and $d$ much smaller than the plates' width.

![A parallel-plate capacitor with plates of area A a distance d apart, carrying +Q and −Q, a uniform field between them and slight fringing at the edges](figures/capacitance/parallel-plate-capacitor.svg "Uniform field between the plates, almost none outside. The derivation ignores the slight fringing at the edges.")

1. The surface charge density is $\sigma = Q/A$, and the field between two oppositely charged sheets is uniform: $E = \dfrac{\sigma}{\varepsilon_0} = \dfrac{Q}{\varepsilon_0 A}$.
2. In a uniform field, $V = Ed = \dfrac{Qd}{\varepsilon_0 A}$.
3. So

$$C = \frac{Q}{V} = \frac{\varepsilon_0 A}{d}$$

Bigger plates or a smaller gap mean more capacitance. The edges have a little **fringing** field, which the formula ignores.

**Zoya's chip.** Inside is a tiny slab of silicon held on springy supports, with fixed plates beside it: a capacitor whose gap can change. Tilt the phone and gravity pulls the slab a little closer to one plate. $d$ shrinks, $C$ grows, and the circuit measures the change.

## Worked example

Take a scaled-up model of that sensor: plates of area $A = 1.0\,\text{cm}^2 = 1.0\times10^{-4}\,\text{m}^2$, a gap of $d = 10\,\mu\text{m} = 1.0\times10^{-5}\,\text{m}$ (illustrative), $\varepsilon_0 = 8.85\times10^{-12}\,\text{C}^2\text{N}^{-1}\text{m}^{-2}$.

**Step 1 — the capacitance at rest.**

$$C = \frac{\varepsilon_0 A}{d} = \frac{8.85\times10^{-12} \times 1.0\times10^{-4}}{1.0\times10^{-5}} = 8.85\times10^{-11}\,\text{F} \approx 89\,\text{pF}$$

**Step 2 — the phone is tilted.** Say the slab shifts $1\,\mu\text{m}$ closer, so $d = 9\,\mu\text{m}$. $C \propto 1/d$, so

$$C = 89\,\text{pF} \times \frac{10}{9} \approx 98\,\text{pF}$$

A movement a hundredth of a hair's width changes the capacitance by about a tenth — easily measured.

**Sanity check:** a gap $10\%$ smaller gave a capacitance about $11\%$ bigger, the right way round and the right size for $C \propto 1/d$.

## Where the picture breaks

Real motion sensors are far smaller than this model: comb-shaped fingers of silicon, with capacitances in the femtofarad-to-picofarad range and shifts much smaller than a micrometre. Most use **two** capacitors, one gap closing while the other opens, and measure the difference. The circuit also detects $C$ with a rapidly changing voltage — the chip is not an electrostatic system — but the relation $C = \varepsilon_0 A/d$ for each tiny gap is exactly what the design relies on.

## Key takeaway

Capacitance is charge per volt, $C = Q/V$, measured in farads, and depends only on geometry and the material between the conductors. For parallel plates in air, $C = \varepsilon_0 A/d$ — valid while the gap is small compared with the plates. Change the gap and the capacitance changes, which is how a phone senses tilt.
