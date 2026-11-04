---
concept_id: capacitance
interest: cricket
format: explain
title: Two plates that never touch inside a broadcast microphone
check:
  question: |-
    The plate area of a parallel-plate capacitor is doubled and the gap between the plates is halved. What happens to its capacitance?
  options:
    A: |-
      It becomes four times as large.
    B: |-
      It stays the same, because the two changes cancel.
    C: |-
      It becomes twice as large.
    D: |-
      It becomes a quarter as large.
  answer: A
  explanation: |-
    $C = \varepsilon_0 A/d$. Doubling $A$ doubles $C$, and halving $d$ doubles it again, so $C$ becomes $2 \times 2 = 4$ times as large.
  misconceptions:
    B: |-
      Thinks area and gap act in opposite directions, so doubling one and halving the other cancels. In fact both changes increase $C$, because $C$ grows with $A$ and grows as $d$ shrinks.
    C: |-
      Accounts for only one of the two changes, usually the area, and forgets that a smaller gap also increases $C$.
    D: |-
      Inverts the formula, as if a wider gap stored more charge. A smaller gap gives a larger capacitance.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground under a storm cloud with lightning in the distance, a floodlight tower, a curator on the pitch, a car by the boundary and a photographer's flash](scenes/cricket/potential_capacitance.svg "Microphones around the ground, including one in the stumps, pick up every sound of the match.")

Sanya has landed a summer internship with the broadcast crew at the city stadium. Her first job is carrying cable reels. Her second is to watch Mr Bose, the audio engineer, fix a crackling microphone.

He unscrews the head and shows her the capsule inside. A foil thinner than a hair, coated with metal, is stretched a fraction of a millimetre in front of a solid metal disc. The two never touch.

"Condenser type," he says. "Old word for a capacitor. It needs a voltage across those two plates, or it's deaf."

"But they don't touch," Sanya says. "Nothing can flow across the gap. How does it hold any charge? And how does a batter's edge on the ball turn into a signal?"

"Work out what sets how much charge those plates can hold," Mr Bose says, handing the capsule back, "and you'll have your answer."

## The physics

A **capacitor** is any two conductors separated by an insulator. Connect it to a battery and charge $+Q$ collects on one conductor and $-Q$ on the other. No charge crosses the gap. Charge flows *around* the circuit until the potential difference between the conductors matches the battery.

The potential difference $V$ is proportional to $Q$. The ratio is the **capacitance**:

$$C = \frac{Q}{V}$$

Its SI unit is the **farad**: $1\,\text{F} = 1\,\text{C/V}$. A farad is enormous, so you will usually meet $\mu\text{F}$, $\text{nF}$ and $\text{pF}$. Capacitance depends only on the shape and size of the conductors and on the material between them, not on $Q$ or $V$. Double the charge and the voltage doubles, but $C$ stays the same.

**The parallel-plate capacitor.** Take two flat plates, each of area $A$, a distance $d$ apart, with $d$ much smaller than the plates' size. Put vacuum (or air) between them and charge them to $\pm Q$.

1. Surface charge density: $\sigma = Q/A$.
2. Each plate alone gives a field $\sigma/2\varepsilon_0$. Between the plates the two fields point the same way and add. Outside they cancel. So between the plates
$$E = \frac{\sigma}{\varepsilon_0} = \frac{Q}{\varepsilon_0 A}$$
and the field is uniform.
3. Potential difference: $V = Ed = \dfrac{Qd}{\varepsilon_0 A}$.
4. Capacitance:
$$C = \frac{Q}{V} = \frac{\varepsilon_0 A}{d}$$

Here $\varepsilon_0 = 8.85 \times 10^{-12}\,\text{F/m}$. Bigger plates hold more charge at the same voltage. A smaller gap needs less voltage for the same charge. Both raise $C$.

![A parallel-plate capacitor with plates of area A a distance d apart, carrying +Q and −Q, a uniform field between them and slight fringing at the edges](figures/capacitance/parallel-plate-capacitor.svg "Uniform field between the plates, almost none outside. The derivation ignores the slight fringing at the edges.")

In the microphone, the foil and the disc are the two plates. Sound pushes the foil back and forth, which changes $d$. That changes $C$, and with it the voltage between the plates, and that changing voltage is the signal.

## Worked example

**Given** (illustrative values for a small capsule): plate area $A = 2.0\,\text{cm}^2 = 2.0 \times 10^{-4}\,\text{m}^2$; gap $d = 25\,\mu\text{m} = 2.5 \times 10^{-5}\,\text{m}$; charged to $V = 40\,\text{V}$.
**Find:** (a) $C$; (b) $Q$; (c) the voltage when a sound pushes the foil in by $1.0\,\mu\text{m}$, if the charge has no time to change.

(a)
$$C = \frac{\varepsilon_0 A}{d} = \frac{8.85 \times 10^{-12} \times 2.0 \times 10^{-4}}{2.5 \times 10^{-5}} = 7.1 \times 10^{-11}\,\text{F} \approx 71\,\text{pF}$$

(b) $Q = CV = 7.08 \times 10^{-11} \times 40 \approx 2.8 \times 10^{-9}\,\text{C}$.

(c) Now $d = 24\,\mu\text{m}$, so $C = 8.85 \times 10^{-12} \times 2.0 \times 10^{-4}/2.4 \times 10^{-5} \approx 74\,\text{pF}$. Then

$$V = \frac{Q}{C} = \frac{2.83 \times 10^{-9}}{7.38 \times 10^{-11}} \approx 38.4\,\text{V}$$

A $1\,\mu\text{m}$ movement changes the voltage by about $1.6\,\text{V}$. That is the signal.

**Sanity check:** at fixed $Q$, $V = Qd/(\varepsilon_0 A)$ is proportional to $d$, so $V = 40 \times 24/25 = 38.4\,\text{V}$, the same answer. Units: $(\text{F/m}) \times \text{m}^2/\text{m} = \text{F}$.

## Where the picture breaks

The microphone is a real device from the broadcast world, not an analogy. But the model is simplified. A real capsule is circular, its field fringes at the edges, and the foil bows in the middle rather than moving flat. "Charge stays fixed" is an approximation: the capsule is charged through a very large resistance, so its charge changes slowly compared with sound vibrations. Not every microphone is this type either. Some work by electromagnetic induction instead, so don't assume every microphone at a ground is a capacitor.

## Key takeaway

Capacitance is charge stored per volt, $C = Q/V$, measured in farads. It depends only on geometry and the material between the conductors. For a parallel-plate capacitor with vacuum or air between the plates, $C = \varepsilon_0 A/d$: bigger plates and a smaller gap give a larger capacitance.
