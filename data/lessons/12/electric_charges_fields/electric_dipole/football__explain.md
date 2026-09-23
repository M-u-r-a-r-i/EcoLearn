---
concept_id: electric_dipole
interest: football
format: explain
title: The water stream that bends towards a rubbed straw
check:
  question: |-
    A short dipole produces a field of $40\,\text{N/C}$ at a point $0.10\,\text{m}$ from its centre, on its axis. What is the field at $0.20\,\text{m}$ from the centre, on the same axis? (Both distances are far larger than the dipole's own length.)
  options:
    A: |-
      $20\,\text{N/C}$, along $\vec{p}$
    B: |-
      $10\,\text{N/C}$, along $\vec{p}$
    C: |-
      $5.0\,\text{N/C}$, along $\vec{p}$
    D: |-
      $5.0\,\text{N/C}$, but now pointing opposite to $\vec{p}$
  answer: C
  explanation: |-
    A short dipole's axial field goes as $1/r^3$: doubling $r$ divides the field by $2^3 = 8$, giving $40/8 = 5.0\,\text{N/C}$, still directed along $\vec{p}$.
  misconceptions:
    A: |-
      Treats the field as falling like $1/r$. A dipole's field falls faster than any single charge's, not slower.
    B: |-
      Uses the point-charge law $1/r^2$. That is right for a lone charge, but a dipole's two charges almost cancel at a distance, and what is left falls as $1/r^3$.
    D: |-
      Mixes up the axial and equatorial directions. On the axis the field points along $\vec{p}$ at every distance; it is on the equatorial line that it points opposite to $\vec{p}$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit ground as a storm arrives: lightning above the stand, rain falling, a player peeling off a crackling nylon bib, and two players heading for the metal-roofed dugout](scenes/football/electric_charges_fields.svg "Charged bibs, wet grass, water bottles: everything in this picture that is 'neutral' is made of dipoles.")

Ayesha, the team physio, has a trick she saves for the youngest squad. She squeezes a water bottle so a thin, steady stream falls into the drain by the touchline. Then she takes a plastic drinking straw, rubs it briskly on a dry nylon bib, and holds it beside the falling water without touching it.

The stream bends. It leans right over towards the straw, a clean curve, and stays bent for as long as she holds the straw there.

"Is the water charged?" asks Kabir.

"Tap water, straight from the bottle," says Ayesha. "Neutral. Same as the straw was two minutes ago."

Kabir has just learned that a charged object attracts a neutral conductor by pushing its free electrons around. But water is not a metal, and nothing is flowing through it — and the stream is still neutral, drop for drop, as it falls.

So what is there inside a neutral molecule for the straw to pull on?

## The physics

An **electric dipole** is a pair of equal and opposite point charges, $+q$ and $-q$, held a fixed distance $2a$ apart. Its strength and direction are carried by one vector, the **dipole moment**:

$$\vec{p} = q\,(2\vec{a}) \qquad \text{directed from } -q \text{ towards } +q$$

with units of coulomb metre, $\text{C m}$. The total charge is zero, so from very far away a dipole looks like nothing at all — but close up the two charges are at different distances from you, and they do not quite cancel.

![A dipole with minus q on the left and plus q on the right; at a point P on the axis the net field points along p; at a point Q on the equatorial line it points opposite to p](figures/electric_dipole/dipole-axial-equatorial.svg "On the axis, the nearer charge wins and E points along p. On the equatorial line, the sideways parts cancel and E points opposite to p.")

For a **short dipole** — one seen from a distance $r \gg a$ — the standard results are:

- **On the axis**, the line through both charges:
  $$E_\text{axial} = \frac{1}{4\pi\varepsilon_0}\,\frac{2p}{r^3} \qquad \text{directed along } \vec{p}$$
- **On the equatorial line**, the perpendicular bisector:
  $$E_\text{equatorial} = \frac{1}{4\pi\varepsilon_0}\,\frac{p}{r^3} \qquad \text{directed opposite to } \vec{p}$$

Two features matter more than the formulas. First, the field falls as $1/r^3$, faster than a single charge's $1/r^2$, because the further you go the more completely the two charges cancel. Second, the axial field is **twice** the equatorial field at the same distance, and the two point in opposite senses relative to $\vec{p}$.

A water molecule is a permanent dipole: its electrons sit closer to the oxygen than to the hydrogens, so one end is slightly negative. The charged straw turns the molecules so their attracted ends face it, and the net pull bends the stream — even though every drop stays neutral.

## Worked example

**Given (illustrative):** a dipole with $q = 2.0\,\text{nC}$ and separation $2a = 1.0\,\text{mm}$.
**Find:** its dipole moment, and the field $0.10\,\text{m}$ away on the axis and on the equatorial line.

**Step 1 — the dipole moment.** In SI units, $q = 2.0 \times 10^{-9}\,\text{C}$ and $2a = 1.0 \times 10^{-3}\,\text{m}$:

$$p = q \times 2a = (2.0 \times 10^{-9})(1.0 \times 10^{-3}) = 2.0 \times 10^{-12}\,\text{C m}$$

**Step 2 — check "short".** We are looking from $0.10\,\text{m}$ at a dipole $1\,\text{mm}$ long: a hundred times longer than the object. The short-dipole formulas are safe.

**Step 3 — the axial field**, with $r^3 = (0.10)^3 = 1.0 \times 10^{-3}\,\text{m}^3$:

$$E_\text{axial} = \frac{2 \times 9.0 \times 10^9 \times 2.0 \times 10^{-12}}{1.0 \times 10^{-3}} = \frac{3.6 \times 10^{-2}}{1.0 \times 10^{-3}} = 36\,\text{N/C}$$

and the equatorial field at the same distance is half of it, $18\,\text{N/C}$, pointing the other way.

**Sanity check:** a lone $2.0\,\text{nC}$ charge at $0.10\,\text{m}$ would give $1800\,\text{N/C}$ — fifty times more. That huge drop is the cancellation doing its work, which is exactly what you should expect from a neutral object.

## Where the picture breaks

The straw and the stream are not a textbook dipole. The straw carries a real charge and is not a $\pm q$ pair; the water molecules are already dipoles but point every which way, and only a small fraction line up at any instant — the rest is thermal jostling. The molecules are also polarised further by the straw's field, so their dipole moments are not fixed. What the demonstration does show honestly is the central idea: an object with zero total charge can still have a dipole moment, and a dipole moment is enough to feel a force in a non-uniform field. Note that word: **non-uniform**. In a uniform field a dipole feels no net force at all, which is the next concept.

## Key takeaway

A dipole is $\pm q$ a distance $2a$ apart, described by $\vec{p} = q(2\vec{a})$, pointing from $-q$ to $+q$. Far away it is almost invisible: its field falls as $1/r^3$, with $E = \dfrac{2kp}{r^3}$ along $\vec{p}$ on the axis and $E = \dfrac{kp}{r^3}$ opposite to $\vec{p}$ on the equatorial line — axial twice equatorial, at the same distance.
