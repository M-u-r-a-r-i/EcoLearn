---
concept_id: resistivity
interest: gaming
format: explain
title: Why the cheap five-metre cable starves the headset
check:
  question: |-
    Two USB cables are the same length and both made of copper, but one has conductors of **twice the diameter** of the other. Compared with the thin cable, the thick cable's conductor resistance is:
  options:
    A: |-
      half as large
    B: |-
      a quarter as large
    C: |-
      twice as large
    D: |-
      the same, because resistivity is a property of copper
  answer: B
  explanation: |-
    $R = \rho L/A$, and the area of a round conductor goes as the *square* of its diameter. Doubling the diameter multiplies $A$ by four, so $R$ falls to a quarter.
  misconceptions:
    A: |-
      Uses the diameter where the formula needs the area. $R$ is inversely proportional to the cross-sectional area, and area scales as diameter squared, not as diameter.
    C: |-
      Reasons that more copper means more resistance. More copper *across* the path gives the charge more lanes to flow through, so a thicker conductor resists less.
    D: |-
      Confuses resistivity with resistance. Resistivity $\rho$ is indeed a property of the material alone, but resistance also depends on the conductor's length and thickness.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A night gaming desk with a monitor showing a frame counter, a controller charging over a USB cable with current arrows, a USB power meter, and an open PC case](scenes/gaming/current_electricity.svg "Two cables can look identical on the outside and be very different conductors.")

Tanvi's VR headset lives in the corner of the room, and the only free socket is on the far wall. She buys a five-metre USB extension — the cheapest on the shelf — and the headset starts behaving like a haunted object: fine for a minute, then a dropout, then a reconnect, then another dropout.

A short cable straight into the socket works perfectly. So does her brother's five-metre cable, which is the same length but visibly thicker and three times the price.

It is not the length by itself, then, and it is not the socket. Then her brother notices what she had missed: after ten minutes of play the cheap cable is warm along its whole length, while his stays cool.

Same metal, same five metres, same socket. One cable warms up and starves the headset; the other does not. What is different inside them?

## The physics

The resistance of a uniform conductor depends on what it is made of **and** on its shape:

$$R = \rho\,\frac{L}{A}$$

where $L$ is its length, $A$ its cross-sectional area, and $\rho$ is the **resistivity** of the material, measured in ohm metres ($\Omega\,\text{m}$). Rearranged, $\rho = RA/L$: resistivity is the resistance of a unit cube of the material measured face to face, so it is a property of the substance alone. Copper's is about $1.7 \times 10^{-8}\,\Omega\,\text{m}$; a good insulator's is larger by something like twenty powers of ten.

![A wire drawn twice: longer at the same thickness, and thicker at the same length, with resistance rising and falling accordingly](figures/resistivity/resistance-and-dimensions.svg "Longer means more resistance; fatter means less — and the area, not the diameter, is what enters the formula.")

Long and thin is the worst combination, and a cheap five-metre cable is exactly that: it saves money by using thinner copper, which multiplies the resistance twice over.

**Temperature.** Resistivity is not fixed. For a metal, over a modest range,

$$\rho_T = \rho_0\left[1 + \alpha\,(T - T_0)\right]$$

where $\alpha$ is the **temperature coefficient of resistivity**, positive for metals. Heat a metal and its ions vibrate harder, the electrons collide more often, the drift falls for the same field — so $\rho$ rises. That is why a filament lamp's $V$–$I$ graph bends, and it is a mildly vicious circle in a cable: more resistance means more heating, which means more resistance still.

![A graph of resistivity against temperature: rising almost linearly for a metal, falling steeply for a semiconductor](figures/resistivity/resistivity-vs-temperature.svg "A metal's resistivity climbs with temperature; a semiconductor's drops sharply, because heating frees many more charge carriers.")

A **semiconductor** does the opposite: heating it frees far more charge carriers than it costs in extra collisions, so $\rho$ falls steeply with temperature. That behaviour is what a thermistor — the little bead that tells a PC how hot its components are, so the fans know when to spin up — is built to exploit.

## Worked example

**Given:** Tanvi's cheap extension is $5\,\text{m}$ long, so the current travels $L = 10\,\text{m}$ of copper in all (out along one conductor and back along the other). Its conductors have a cross-section $A = 0.1\,\text{mm}^2$, and copper has $\rho = 1.7 \times 10^{-8}\,\Omega\,\text{m}$.
**Find:** the resistance of the round trip through the cable.

Convert the area first: $0.1\,\text{mm}^2 = 1.0 \times 10^{-7}\,\text{m}^2$.

$$R = \rho\frac{L}{A} = 1.7\times10^{-8} \times \frac{10}{1.0\times10^{-7}}$$

The shape factor $L/A$ is $1.0 \times 10^{8}\,\text{m}^{-1}$ — huge, because the copper is long and hair-thin. So

$$R = 1.7\,\Omega$$

Under two ohms sounds trivial. It is not: with the headset drawing about an ampere, roughly $1.7\,\text{V}$ of the $5\,\text{V}$ is lost in the cable itself, leaving only about $3.3\,\text{V}$ at the far end — not enough, which is the dropout. Her brother's cable has five times the copper area, so a fifth of the resistance, and loses only a few tenths of a volt.

**Sanity check:** a few metres of household wiring is a small fraction of an ohm, and a heating element is tens of ohms; a thin signal-grade cable sitting between them at a couple of ohms is the right size.

## Where the picture breaks

The calculation treats the cable as one clean cylinder of copper, and a real one is not. Every plug and socket adds a **contact resistance** that can rival the wire's own, especially in a worn or dusty connector — which is why wiggling a cable sometimes "fixes" a device. The two conductors are also assumed identical; cheap cables often skimp on one more than the other.

Dropouts have causes beyond voltage, too. A long cable degrades the *data* signal as well as the power, and USB devices negotiate how much current they may draw — so a real headset may be refusing to run rather than physically unable to. And the linear temperature formula is an approximation valid over a limited range; it fails badly at very low temperatures and says nothing about alloys designed to have almost no temperature coefficient at all.

## Key takeaway

Resistance depends on material and shape together: $R = \rho L/A$, with resistivity $\rho$ a property of the material alone. Doubling the length doubles the resistance; doubling the *diameter* quarters it. Resistivity rises with temperature in a metal and falls sharply in a semiconductor, which is the whole basis of a thermistor.
