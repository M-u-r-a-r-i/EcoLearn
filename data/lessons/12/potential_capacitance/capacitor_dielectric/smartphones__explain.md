---
concept_id: capacitor_dielectric
interest: smartphones
format: explain
title: Why raindrops can tap your phone for you
check:
  question: |-
    A parallel-plate capacitor is connected to a battery, and **stays connected** while a slab with dielectric constant $K = 4$ is slid in to fill the gap completely. What happens to the charge on the plates and the voltage across them?
  options:
    A: |-
      The charge becomes four times as large; the voltage stays the same.
    B: |-
      The charge stays the same; the voltage falls to a quarter.
    C: |-
      The charge falls to a quarter; the voltage stays the same.
    D: |-
      The charge stays the same; the voltage becomes four times as large.
  answer: A
  explanation: |-
    The battery holds $V$ fixed. The capacitance becomes $KC_0 = 4C_0$, so $Q = CV$ becomes four times as large — extra charge flows on from the battery.
  misconceptions:
    B: |-
      Applies the disconnected case, where the charge is trapped. With the battery connected it is the voltage that is fixed, and the charge adjusts.
    C: |-
      Thinks an insulator in the gap blocks or soaks up charge. The dielectric raises the capacitance, so the plates hold more charge at the same voltage, not less.
    D: |-
      Thinks a dielectric strengthens the field between the plates. Its bound charges oppose the field, and in any case the connected battery keeps the voltage fixed.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a rainy window: a phone with raindrops on its screen being tapped by a finger, a metal biscuit tin with its lid off, a breadboard with two supercapacitor cells wired in a chain, a stylus and a fitness band with a small display](scenes/smartphones/potential_capacitance.svg "Raindrops on the screen, right next to a fingertip. To the touchscreen, the two are not as different as you might think.")

Pranav is walking home from coaching class in the first heavy rain of the monsoon, phone in hand, maps open. Big drops land on the screen. Suddenly the map zooms out on its own. Then a music app opens. Then the phone starts dialling someone he hasn't called in a year.

He hangs up in a panic, ducks under a shop's awning and wipes the screen on his shirt. Everything behaves again.

At home he tells his sister Lavanya, who is in engineering college. "The screen's meant to feel *fingers*. Raindrops aren't fingers. They don't press anything, they're not me, they're not even attached to anything."

"The screen doesn't feel pressure," she says. "It measures capacitance."

Pranav thought capacitance depended only on the size of the plates and the gap between them. A raindrop sitting on the glass changes neither. So how does a drop of water change what the screen measures?

## The physics

**A full slab.** Start with a parallel-plate capacitor in vacuum, $C_0 = \varepsilon_0 A/d$, carrying $\pm Q$. Fill the gap with a dielectric of constant $K$. The dielectric polarises and its bound charges cut the field from $E_0$ to $E_0/K$. For the same $Q$, the voltage $V = Ed$ also falls by $K$. So $C = Q/V$ rises by $K$:

$$C = KC_0 = \frac{K\varepsilon_0 A}{d}$$

The material in the gap is part of the geometry that sets $C$. Air has $K \approx 1$, glass a few, water about $80$. That is Pranav's answer: water near the sensor's electrodes changes the capacitance a lot.

**A partial slab.** A slab of thickness $t < d$ has field $E_0$ in the air and $E_0/K$ inside it:

$$V = E_0(d - t) + \frac{E_0}{K}\,t \quad\Rightarrow\quad C = \frac{\varepsilon_0 A}{d - t + t/K}$$

The slab counts as a layer of air only $t/K$ thick.

![A capacitor with plates 4.0 mm apart and a 2.0 mm slab with K = 4 in the middle; the field is E-nought in the air gaps and E-nought over K in the slab](figures/capacitor_dielectric/slab-partial.svg "The slab weakens the field inside it, so it counts as only t/K of air. Here the effective gap drops from 4.0 mm to 2.5 mm.")

**What is held fixed matters.**

| Dielectric fills the gap | $C$ | $Q$ | $V$ | $E$ | $U$ |
|---|---|---|---|---|---|
| Battery connected ($V$ fixed) | $\times K$ | $\times K$ | same | same | $\times K$ |
| Battery disconnected ($Q$ fixed) | $\times K$ | same | $\div K$ | $\div K$ | $\div K$ |

## Worked example

Model one touch-sensor cell as an air capacitor with $C_0 = 2.0\,\text{pF}$ and a gap $d = 1.0\,\text{mm}$ (illustrative values).

**Step 1 — slide in a slab** $t = 0.5\,\text{mm}$ thick with $K = 4$. The effective gap is

$$d - t + \frac{t}{K} = 1.0 - 0.5 + 0.125 = 0.625\,\text{mm}$$

**Step 2 — the new capacitance.** $C \propto 1/(\text{effective gap})$, so

$$C = 2.0\,\text{pF} \times \frac{1.0}{0.625} = 3.2\,\text{pF}$$

**Step 3 — fill the whole gap.** With $K = 4$: $C = 4 \times 2.0 = 8.0\,\text{pF}$. With water, $K \approx 80$: $C \approx 160\,\text{pF}$ — eighty times the dry value.

**Sanity check:** the half-filled answer, $3.2\,\text{pF}$, lies between empty ($2.0$) and full ($8.0$), and setting $K = 1$ gives back $2.0\,\text{pF}$, as a slab of air should.

## Where the picture breaks

A touchscreen is not two flat plates with a slab between them. Its electrodes are thin transparent strips side by side under the glass, and the field that matters **fringes** up through the glass into whatever is on top. A drop sitting there is in that fringing field, not filling a neat gap, so the change is far smaller than "eighty times" — but real, and enough to trigger a false touch. Rainwater also carries dissolved salts, so it conducts a little, and a finger changes the reading partly because the body is a conductor connected to the ground. Modern phones fight back with software that ignores drop-shaped patterns — which is why some screens cope with rain better than others.

## Key takeaway

Filling the gap with a dielectric multiplies the capacitance by $K$: $C = K\varepsilon_0 A/d$. A slab of thickness $t$ gives $C = \dfrac{\varepsilon_0 A}{d - t + t/K}$. With a battery connected, $V$ stays fixed and $Q$ rises by $K$; disconnected, $Q$ stays fixed and $V$ falls by $K$.
