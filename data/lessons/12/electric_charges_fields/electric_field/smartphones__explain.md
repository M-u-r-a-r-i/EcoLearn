---
concept_id: electric_field
interest: smartphones
format: explain
title: How a screen feels a finger that isn't touching it
check:
  question: |-
    At point P near a small charged patch, a test charge of $+1.0\,\text{nC}$ feels a force showing that the field there is $900\,\text{N/C}$ towards the east. The test charge is replaced by one of $-2.0\,\text{nC}$ at the same point. What is the electric field at P now?
  options:
    A: |-
      $900\,\text{N/C}$, towards the east
    B: |-
      $1800\,\text{N/C}$, towards the west
    C: |-
      $900\,\text{N/C}$, towards the west
    D: |-
      $450\,\text{N/C}$, towards the east
  answer: A
  explanation: |-
    The field at P is set by the patch's charge and the distance to it, not by the test charge. It stays $900\,\text{N/C}$ east. Only the *force* changes: $F = qE = 2.0 \times 10^{-9} \times 900 = 1.8 \times 10^{-6}\,\text{N}$, pointing west because the charge is negative.
  misconceptions:
    B: |-
      Thinks the field grows with the test charge and flips with its sign. That describes the force $\vec{F} = q\vec{E}$, not the field, which is force per unit charge.
    C: |-
      Thinks the field's direction depends on the sign of the charge placed there. The field direction is defined by the force on a positive test charge, whatever is actually placed there.
    D: |-
      Thinks a bigger test charge "uses up" or weakens the field, dividing it by the test charge's size.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a sunny window with a solar power bank on the sill, an opened phone box with foam beads clinging to the new phone, a film being peeled off a screen with dust jumping up to it, and a phone on a stand running a field-line app](scenes/smartphones/electric_charges_fields.svg "The dust in the middle starts moving before anything touches it. Something is already in the space above that screen.")

Diya's aunt has a phone that does a trick Diya can't stop playing with: hold a finger just above a video thumbnail, not touching, and a preview pops up.

"It's a camera," says her friend Omkar. "It sees your finger."

"Then why does it stop working when I wear gloves?" Diya asks. "And why does it work in the dark?"

Her aunt, who repairs phones for a living, says only this: "Under the glass there are charged electrodes. Your finger is a conductor. The screen isn't looking at you, it's *feeling* you."

Diya tries it again, slowly lowering her finger. At a couple of centimetres, nothing. At a few millimetres, the preview appears. But her finger never touches anything. How can charges under the glass affect something in empty space above it? What is actually there, in the gap?

## The physics

A charge changes the space around it. At every point it sets up an **electric field** $\vec{E}$, which is there whether or not anything is placed in it. Put another charge there and the field pushes or pulls it.

To measure the field at a point, place a small **positive test charge** $q_0$ there and measure the force on it:
$$\vec{E} = \frac{\vec{F}}{q_0}$$
The field is **force per unit positive charge**. Its SI unit is the **newton per coulomb** (N/C). The test charge must be small so it doesn't disturb the charges that make the field; strictly, $\vec{E}$ is the limit of $\vec{F}/q_0$ as $q_0 \to 0$.

Once you know $\vec{E}$, the force on **any** charge $q$ at that point is $\vec{F} = q\vec{E}$: along $\vec{E}$ for a positive charge, opposite to it for a negative one.

For a **point charge** $Q$, Coulomb's law with $q_0$ divided out gives
$$E = \frac{1}{4\pi\varepsilon_0}\,\frac{|Q|}{r^2}$$
pointing **radially away** from a positive $Q$ and **towards** a negative $Q$. It depends only on $Q$ and on the distance $r$, never on the test charge.

![Field vectors around a positive charge point outwards and around a negative charge point inwards; at twice the distance they are a quarter as long](figures/electric_field/field-vectors-point-charges.svg "The field has a size and direction at every point, away from +Q and towards −Q. At twice the distance it is a quarter as strong.")

In Diya's aunt's screen, the electrodes' charges fill the space above the glass with a field. A finger entering that field disturbs it, and the phone detects the change. Close to the glass the field is strong, so the change is big; at a couple of centimetres it has faded too much to notice.

## Worked example

**Given (illustrative):** model a small charged patch on a screen as a point charge $Q = +4.0\,\text{nC}$.
**Find:** the field at $10\,\text{cm}$ and $20\,\text{cm}$, and the force on a dust speck carrying $-0.50\,\text{nC}$ at $10\,\text{cm}$.

**Step 1 — field at 10 cm.**
$$E = \frac{9.0 \times 10^9 \times 4.0 \times 10^{-9}}{(0.10)^2} = \frac{36}{0.010} = 3600\,\text{N/C}$$
pointing away from the patch. Every coulomb placed here would feel $3600\,\text{N}$.

**Step 2 — field at 20 cm.** Twice as far, so a quarter as strong: $3600/4 = 900\,\text{N/C}$.

**Step 3 — force on the speck at 10 cm.**
$$F = qE = 0.50 \times 10^{-9} \times 3600 = 1.8 \times 10^{-6}\,\text{N}$$
The speck is negative, so the force is opposite to $\vec{E}$: it is pulled towards the patch.

**Sanity check:** a couple of micro-newtons is roughly the weight of a speck a fifth of a milligram in mass, enough to lift fine dust but not a crumb, which matches what charged screens actually collect.

## Where the picture breaks

A touchscreen's electrodes are a fine grid of transparent conducting strips, not a single point charge, and they are driven by a changing voltage; the phone measures how much charge the finger's presence lets the electrodes hold, an idea you'll meet with capacitance. So the point-charge formula here describes the idea, not the screen's actual field pattern. And the dust speck is not a perfectly small test charge: a larger one would disturb the patch's charge, which is why the definition needs $q_0 \to 0$.

## Key takeaway

A charge fills the space around it with an electric field, defined as the force per unit positive test charge, $\vec{E} = \vec{F}/q_0$, in N/C. For a point charge $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{|Q|}{r^2}$, pointing away from $+Q$ and towards $-Q$. Any charge $q$ placed there then feels $\vec{F} = q\vec{E}$.
