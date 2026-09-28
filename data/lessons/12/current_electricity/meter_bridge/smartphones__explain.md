---
concept_id: meter_bridge
interest: smartphones
format: explain
title: Measuring a phone speaker's coil with a metre of wire
check:
  question: |-
    In a metre bridge, a known $10\,\Omega$ resistor is in the left gap and an unknown coil in the right gap. The balance point is found $80\,\text{cm}$ from the left end. The coil's resistance is:
  options:
    A: |-
      $2.5\,\Omega$
    B: |-
      $40\,\Omega$
    C: |-
      $2.0\,\Omega$
    D: |-
      $10\,\Omega$
  answer: A
  explanation: |-
    At balance $\dfrac{R}{S} = \dfrac{l}{100 - l}$, so $S = R\,\dfrac{100 - l}{l} = 10 \times \dfrac{20}{80} = 2.5\,\Omega$. The balance point sits close to the coil's end of the wire, so the coil is the *smaller* resistance.
  misconceptions:
    B: |-
      Inverts the ratio, pairing the unknown with the length on the known resistor's side. The length $l$ on the left belongs with the left-gap resistor $R$; the unknown on the right goes with $100 - l$.
    C: |-
      Divides by the whole metre instead of by the other segment, $R(100 - l)/100$. The balance compares the two segments of wire with each other, not one segment with the full length.
    D: |-
      Assumes that at balance the two gaps must hold equal resistances. They are equal only if the balance point is at exactly $50\,\text{cm}$; elsewhere the ratio of lengths sets the ratio of resistances.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A charging corner: a phone on a wall charger, a power bank charging an earbuds case through a small USB meter, and a smartwatch on its charging puck, with current arrows on the cables](scenes/smartphones/current_electricity.svg "Every gadget here hides a coil or a resistor that someone, somewhere, had to measure.")

Aditi's ISC practical exam is next week, and her cousin Manav — who fixes phones for pocket money — has given her something to practise on: the tiny loudspeaker from a phone that went through a washing machine.

"The coil might be fine," he says. "If its resistance is right, I can reuse it. My multimeter's leads are so loose it gives a different answer every time."

In the school lab, Aditi sets up the apparatus the exam will ask for: a metre-long wire stretched along a wooden board beside a ruler, two gaps for resistors, a galvanometer and a sliding contact. She puts a known resistor in one gap and Manav's speaker in the other.

Her lab partner Rehan is doubtful. "You're going to find a resistance with a *ruler*? Where does the number of ohms come from?"

## The physics

A **metre bridge** is a Wheatstone bridge in which two of the four arms are made of wire. A uniform wire AC, exactly $1\,\text{m}$ long, is stretched along a scale. The known resistance $R$ goes in the left gap and the unknown $S$ in the right gap. A galvanometer connects the point between the gaps to a **jockey** — a sliding contact that can touch the wire anywhere along it.

![A metre bridge: a one-metre wire along a scale, a known resistance in the left gap, an unknown in the right gap, and a galvanometer to a jockey on the wire](figures/meter_bridge/metre-bridge-setup.svg "The two stretches of wire on either side of the jockey are the bridge's ratio arms — and their ratio is simply the ratio of their lengths.")

Slide the jockey until the galvanometer reads zero. That point is the **balance point**, a distance $l$ (in cm) from the left end. The bridge is now balanced, so the Wheatstone condition holds, with the two stretches of wire as the ratio arms:

$$\frac{R}{S} = \frac{\text{resistance of length } l}{\text{resistance of length } (100 - l)}$$

Because the wire is **uniform**, every centimetre has the same resistance, so the resistances of the two stretches are in the ratio of their lengths:

$$\frac{R}{S} = \frac{l}{100 - l} \qquad \Longrightarrow \qquad S = R\,\frac{100 - l}{l}$$

That answers Rehan: the ruler gives a *ratio*, and the known resistor turns the ratio into ohms.

Good practice follows from the method itself. Choose $R$ so that the balance point lies near the middle of the wire, where a small misreading of $l$ matters least. Then swap $R$ and $S$ and balance again; the average of the two results cancels the small extra resistance at the wire's ends and in the connecting strips (the **end error**).

## Worked example

**Given:** Aditi uses a known $R = 12\,\Omega$ in the left gap. The galvanometer reads zero with the jockey at $l = 60\,\text{cm}$.
**Find:** the resistance of the speaker coil $S$.

The balance point splits the wire into $60\,\text{cm}$ and $100 - 60 = 40\,\text{cm}$.

$$S = R\,\frac{100 - l}{l} = 12 \times \frac{40}{60} = 8\,\Omega$$

The coil is two-thirds of the known resistor — about $8\,\Omega$, a typical value for a small speaker, so Manav's speaker survived its wash.

**Sanity check:** the balance point is past the middle, on the coil's side, so the coil must be the smaller resistance — and $8\,\Omega$ is indeed less than $12\,\Omega$.

## Where the picture breaks

The speaker is only the thing being measured; the physics is all in the bridge. Two honest limits. First, the method assumes the wire is perfectly uniform; a kinked or unevenly stretched wire makes centimetres unequal and spoils the ratio. Second, a speaker coil is meant to carry changing currents, and in use it behaves differently from its simple steady-current resistance measured here.

On the bench, keep the current small and tap the jockey rather than dragging it, so the wire neither heats up nor gets scraped.

## Key takeaway

A metre bridge is a Wheatstone bridge whose ratio arms are two stretches of one uniform metre of wire, so at balance $R/S = l/(100 - l)$ and $S = R\,(100 - l)/l$. Choose $R$ to bring the balance point near the middle, and swap the two resistors to cancel end errors.
