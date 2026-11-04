---
concept_id: electric_dipole
interest: smartphones
format: explain
title: Why raindrops make a touchscreen tap by itself
check:
  question: |-
    A small electric dipole produces a field of $40\,\text{N/C}$ at a point on its axis, a distance $r$ from its centre ($r$ much larger than the dipole's length). What field does it produce at a point on its equatorial line, the same distance $r$ from the centre?
  options:
    A: |-
      $40\,\text{N/C}$, along $\vec{p}$
    B: |-
      $80\,\text{N/C}$, along $\vec{p}$
    C: |-
      $20\,\text{N/C}$, opposite to $\vec{p}$
    D: |-
      $20\,\text{N/C}$, along $\vec{p}$
  answer: C
  explanation: |-
    On the axis $E = \dfrac{2kp}{r^3}$; on the equatorial line $E = \dfrac{kp}{r^3}$, half as much, and pointing opposite to $\vec{p}$. So the field is $20\,\text{N/C}$, antiparallel to the dipole moment.
  misconceptions:
    A: |-
      Assumes the field depends only on distance from the centre, as for a single point charge. A dipole's field also depends on direction, and is twice as strong on the axis.
    B: |-
      Remembers the factor of 2 but puts it on the wrong line: it is the axial field that has the extra factor of 2, so the equatorial field is the smaller one.
    D: |-
      Gets the size right but the direction wrong. On the equatorial line the sideways parts cancel and the leftover parts point from $+q$ towards $-q$, opposite to $\vec{p}$.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a sunny window with a solar power bank on the sill, an opened phone box with foam beads clinging to the new phone, a film being peeled off a screen with dust jumping up to it, and a phone on a stand running a field-line app](scenes/smartphones/electric_charges_fields.svg "The app on the stand shows a + and a − side by side. That pair, a dipole, is the shape of today's lesson.")

It's the first heavy monsoon shower of the year, and Zoya is sheltering under a bus stop, trying to book a ride. Raindrops have spattered her screen, and the phone has gone wild: apps open by themselves, the keyboard types random letters, the map zooms in and out.

"Your phone's possessed," says her friend Neel.

"It's the water," says Zoya, wiping it on her sleeve. "The screen thinks the drops are fingers."

Neel isn't convinced. "A finger is part of a person. A drop of water is just water, with no charge on it. Water is neutral, isn't it?"

He has a point. A neutral object has as much positive charge as negative. Shouldn't the two cancel, leaving no field at all for the screen to feel? And yet the drops are clearly doing *something*. How can a thing with zero total charge still make an electric field?

## The physics

An **electric dipole** is a pair of equal and opposite charges, $+q$ and $-q$, a small distance $2a$ apart. Its total charge is zero, but its field is not, because the two charges are in slightly different places.

Its strength is measured by the **dipole moment**
$$\vec{p} = q \times 2a\,\hat{p}$$
a vector pointing **from $-q$ to $+q$**, with SI unit C m. A water molecule is a natural dipole: its electrons sit slightly closer to the oxygen atom, so that end is a little negative and the hydrogen end a little positive.

![A dipole with minus q on the left and plus q on the right; at a point P on the axis the net field points along p; at a point Q on the equatorial line it points opposite to p](figures/electric_dipole/dipole-axial-equatorial.svg "On the axis the nearer charge wins and E points along p. On the equatorial line the sideways parts cancel and E points opposite to p.")

**On the axis**, at distance $r$ from the centre, the nearer charge's field wins. Adding the two fields gives
$$E_\text{axial} = \frac{1}{4\pi\varepsilon_0}\,\frac{2pr}{(r^2 - a^2)^2} \approx \frac{1}{4\pi\varepsilon_0}\,\frac{2p}{r^3} \quad (r \gg a)$$
pointing **along** $\vec{p}$.

**On the equatorial line** (the perpendicular bisector), both charges are equally far away. Their sideways components cancel and the parts parallel to the axis add:
$$E_\text{eq} = \frac{1}{4\pi\varepsilon_0}\,\frac{p}{(r^2 + a^2)^{3/2}} \approx \frac{1}{4\pi\varepsilon_0}\,\frac{p}{r^3} \quad (r \gg a)$$
pointing **opposite** to $\vec{p}$.

Two things to notice. Far away, a dipole's field falls as $1/r^3$, faster than a single charge's $1/r^2$, because the two charges' fields nearly cancel. And at equal distances, the axial field is **twice** the equatorial field.

## Worked example

**Given (illustrative):** a model dipole of charges $\pm 1.0\,\text{nC}$ held $2.0\,\text{mm}$ apart.
**Find:** $p$, and the field $10\,\text{cm}$ from its centre, on the axis and on the equatorial line.

**Step 1 — the dipole moment.**
$$p = q \times 2a = 1.0 \times 10^{-9} \times 2.0 \times 10^{-3} = 2.0 \times 10^{-12}\,\text{C m}$$

**Step 2 — on the axis.** $r = 0.10\,\text{m}$ is fifty times the $2\,\text{mm}$ gap, so the short forms are fine. $r^3 = 1.0 \times 10^{-3}\,\text{m}^3$:
$$E_\text{axial} = \frac{9.0 \times 10^9 \times 2 \times 2.0 \times 10^{-12}}{1.0 \times 10^{-3}} = 36\,\text{N/C}$$
pointing along $\vec{p}$.

**Step 3 — on the equatorial line.** Half as much: $18\,\text{N/C}$, pointing opposite to $\vec{p}$.

**Sanity check:** the $+1.0\,\text{nC}$ charge alone would give $900\,\text{N/C}$ at $10\,\text{cm}$; the dipole gives only $36\,\text{N/C}$ because its $-1.0\,\text{nC}$ partner, so close by, almost cancels it. Almost, but not quite.

## Where the picture breaks

A raindrop contains an enormous number of water molecules, and on its own they point every which way, so their dipole fields mostly cancel. What matters for the screen is how easily those molecules *turn* to line up with the screen's field (you'll meet this as polarisation and dielectrics), plus the fact that rainwater carries dissolved ions and conducts, a little like a fingertip. The touchscreen senses all of this as a change in capacitance, a later topic. The single dipole here is the building block, not the whole story.

## Key takeaway

An electric dipole is $+q$ and $-q$ a distance $2a$ apart, with moment $\vec{p} = q \times 2a$, pointing from $-q$ to $+q$. Far away its field falls as $1/r^3$: on the axis $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2p}{r^3}$ along $\vec{p}$, and on the equatorial line $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{p}{r^3}$ opposite to $\vec{p}$, half the axial value.
