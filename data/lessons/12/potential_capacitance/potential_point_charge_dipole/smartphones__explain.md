---
concept_id: potential_point_charge_dipole
interest: smartphones
format: explain
title: The earbud case that pulled lint from across the desk
check:
  question: |-
    A charge of $+4.0\,\text{nC}$ sits $0.20\,\text{m}$ from a point P, and a charge of $-2.0\,\text{nC}$ sits $0.10\,\text{m}$ from P, in a different direction. What is the potential at P? Take $\dfrac{1}{4\pi\varepsilon_0} = 9.0\times10^{9}\,\text{N m}^2\text{C}^{-2}$.
  options:
    A: |-
      $+360\,\text{V}$
    B: |-
      $-900\,\text{V}$
    C: |-
      It cannot be found without knowing the angle between the two directions.
    D: |-
      $0\,\text{V}$
  answer: D
  explanation: |-
    Potentials add as plain numbers with their signs: $9.0\times10^{9}\left(\dfrac{4.0\times10^{-9}}{0.20} - \dfrac{2.0\times10^{-9}}{0.10}\right) = 180 - 180 = 0\,\text{V}$.
  misconceptions:
    A: |-
      Drops the sign of the negative charge and adds the two sizes, $180 + 180$. A negative charge makes a negative potential, so its contribution is subtracted.
    B: |-
      Uses $1/r^2$, the rule for the field, instead of $1/r$. Potential from a point charge falls as $1/r$.
    C: |-
      Treats potential as a vector that needs directions to combine. Potential is a scalar: only the distances and the signs matter, never the directions.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a rainy window: a phone with raindrops on its screen being tapped by a finger, a metal biscuit tin with its lid off, a breadboard with two supercapacitor cells wired in a chain, a stylus and a fitness band with a small display](scenes/smartphones/potential_capacitance.svg "Dry winter air, plastic gadgets and a wool sweater: the perfect recipe for charges that stay put.")

It is a dry December morning in Shimla, and Siddharth has been fidgeting with his plastic earbud case during an online class, rubbing it against the sleeve of his wool sweater. When he sets it down on the desk, a few specks of lint and a torn corner of a paper tissue drift towards it from several centimetres away.

His sister Naina, who is in Class 12, holds the case up and moves it slowly over the desk. Lint lifts off the wood when the case is close; from twenty centimetres away, nothing happens.

"It's charged," she says. "The sweater took some electrons, the case lost them."

"Fine. But how much does its effect fall off? Half as much at double the distance? A quarter? And the sweater's charged too, the opposite way — do the two just cancel?"

Naina starts to answer and stops. She knows the field falls off one way. But the question was about potential.

## The physics

**A point charge.** Bring a unit positive charge from infinity to a distance $r$ from a point charge $q$. Adding up the work against Coulomb's force gives

$$V = \frac{1}{4\pi\varepsilon_0}\,\frac{q}{r}$$

So the potential falls as $1/r$ — double the distance, half the potential — while the field falls as $1/r^2$. $V$ is positive near a positive charge, negative near a negative one, and zero at infinity.

![Two graphs for a 1.0 nC charge: the potential falls as 1 over r, from 9.0 V at 1 m to 4.5 V at 2 m; the field falls as 1 over r squared, from 9.0 V/m to 2.25 V/m](figures/potential_point_charge_dipole/point-charge-v-and-e.svg "From 1 m to 2 m the potential halves, but the field drops to a quarter. V goes as 1/r, E as 1/r².")

**A system of charges.** Potential is a scalar, so the potential of several charges is just the **sum** of each one's potential, with signs:

$$V = \frac{1}{4\pi\varepsilon_0}\left(\frac{q_1}{r_1} + \frac{q_2}{r_2} + \dots\right)$$

No angles, no components — which is what makes potential so much easier to add than field.

**A dipole.** Charges $+q$ and $-q$ a distance $2a$ apart have dipole moment $p = q \times 2a$, pointing from $-q$ to $+q$. At distance $r$ from the centre, at angle $\theta$ to $\vec{p}$, and for $r \gg a$:

$$V = \frac{1}{4\pi\varepsilon_0}\,\frac{p\cos\theta}{r^2}$$

A dipole's potential falls as $1/r^2$, faster than a single charge's, because the $+$ and $-$ contributions nearly cancel far away. On the equatorial line ($\theta = 90^\circ$) it is exactly zero.

![A dipole with minus q and plus q separated by 2a, moment p from minus to plus, and a point P at distance r and angle theta](figures/potential_point_charge_dipole/dipole-potential.svg "The dipole formula needs r to be much larger than a. Every point on the equatorial line is at zero potential.")

## Worked example

Treat Siddharth's case as a point charge of $+2.0\,\text{nC}$ (illustrative), and use $\dfrac{1}{4\pi\varepsilon_0} = 9.0\times10^9\,\text{N m}^2\text{C}^{-2}$.

**Step 1 — potential $10\,\text{cm}$ away.**

$$V = \frac{9.0\times10^9 \times 2.0\times10^{-9}}{0.10} = 180\,\text{V}$$

**Step 2 — potential $20\,\text{cm}$ away.** Double the distance, half the potential: $90\,\text{V}$. (The field there is a quarter of its $10\,\text{cm}$ value.)

**Step 3 — add the sweater.** Say the sleeve carries $-2.0\,\text{nC}$ and lies $20\,\text{cm}$ from the case. At the point exactly halfway, each is $10\,\text{cm}$ away:

$$V = 180\,\text{V} + (-180\,\text{V}) = 0\,\text{V}$$

The potentials cancel. The *fields* do not: both point from the case towards the sleeve there, so they add.

**Sanity check:** a hundred-odd volts from a rubbed plastic case is the right size — static shocks you can feel start in the thousands.

## Where the picture breaks

A rubbed case is not a point: the charge spreads over its surface, so $kq/r$ is good only at distances large compared with the case. The lint moves because of the **field** (and the lint's own polarisation), not because of the potential itself — a zero potential at the midpoint does not mean a zero force there. And charge slowly leaks away into the air, faster when it is humid, so the numbers only hold for a moment.

## Key takeaway

A point charge gives $V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r}$, falling as $1/r$. For several charges, add the potentials as signed numbers. A dipole gives $V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{p\cos\theta}{r^2}$ far away, falling as $1/r^2$ and zero on its equatorial line.
