---
concept_id: electric_dipole
interest: cricket
format: explain
title: The dew that makes the ball slippery
check:
  question: |-
    Far from a small electric dipole, the field at a point on its axis, a distance $r$ from its centre, is $80\,\text{N/C}$. What is the field at a point on the axis at distance $2r$?
  options:
    A: |-
      $20\,\text{N/C}$
    B: |-
      $10\,\text{N/C}$
    C: |-
      $40\,\text{N/C}$
    D: |-
      $0\,\text{N/C}$
  answer: B
  explanation: |-
    Far from a dipole, $E_\text{axis} \approx \dfrac{2p}{4\pi\varepsilon_0 r^3}$, so the field goes as $1/r^3$. Doubling $r$ divides it by $2^3 = 8$: $80/8 = 10\,\text{N/C}$.
  misconceptions:
    A: |-
      Uses the inverse-square law of a single point charge. A dipole's two fields nearly cancel far away, so its field falls faster, as $1/r^3$.
    C: |-
      Treats the field as inversely proportional to distance, halving it when the distance doubles.
    D: |-
      Thinks a dipole has no field because its total charge is zero. The two charges are at different places, so their fields don't cancel exactly.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A storm over a cricket ground: dark clouds, distant lightning, players walking off, groundstaff dragging a plastic cover and a team bus waiting](scenes/cricket/electric_charges_fields.svg "After a storm, the evening air is heavy with moisture, and dew will settle on the outfield.")

The storm has passed, the covers are off, and the day-night match restarts under a damp evening sky. By the second innings, dew is settling on the outfield. Every time the ball skids across the grass, it comes back to Meera, the leg-spinner, wet and slippery.

She keeps rubbing it on the towel tucked into her waistband, but within an over the film of water is back. The ball won't grip, and her googly stops turning.

At the drinks break, her team-mate Aditya, who is doing chemistry at school, offers a theory. "Water molecules are neutral, but they're lopsided: the oxygen end is slightly negative and the hydrogen end slightly positive. That's partly why water clings to things."

Meera frowns. "If a molecule has zero total charge, how can it make any electric field at all? And if it does, how strong is it?"

## The physics

A pair of equal and opposite charges, $+q$ and $-q$, separated by a distance $2a$, is called an **electric dipole**. Its total charge is zero, but because the two charges sit at different places, their fields don't cancel exactly.

The **dipole moment** is a vector:

$$\vec{p} = q \times 2a\,\hat{p}$$

with magnitude $p = q(2a)$, directed **from $-q$ to $+q$** along the dipole's axis. Its unit is the coulomb metre, $\text{C m}$. A water molecule has a permanent dipole moment of about $6.2 \times 10^{-30}\,\text{C m}$; molecules like this are called **polar**.

![A dipole with minus q on the left and plus q on the right; at a point P on the axis the net field points along p; at a point Q on the equatorial line it points opposite to p](figures/electric_dipole/dipole-axial-equatorial.svg "On the axis, the nearer charge wins and E points along p. On the equatorial line, the sideways parts cancel and E points opposite to p.")

**Field on the axis**, at distance $r$ from the centre, on the side of $+q$. The nearer charge $+q$ is at distance $r - a$ and the farther one at $r + a$:

$$E = \frac{q}{4\pi\varepsilon_0}\left[\frac{1}{(r-a)^2} - \frac{1}{(r+a)^2}\right] = \frac{1}{4\pi\varepsilon_0}\,\frac{2pr}{(r^2 - a^2)^2}$$

pointing **along $\vec{p}$**. For $r \gg a$, this becomes $E \approx \dfrac{2p}{4\pi\varepsilon_0 r^3}$.

**Field on the equatorial line** (the perpendicular bisector), at distance $r$ from the centre. Both charges are at distance $\sqrt{r^2 + a^2}$, so the two fields are equal in size. Their components perpendicular to the axis cancel; their components parallel to the axis add, both pointing from $+q$ towards $-q$:

$$E = \frac{1}{4\pi\varepsilon_0}\,\frac{p}{(r^2 + a^2)^{3/2}}$$

pointing **opposite to $\vec{p}$**. For $r \gg a$, $E \approx \dfrac{p}{4\pi\varepsilon_0 r^3}$.

Two results to remember: far away, a dipole's field falls as $1/r^3$, faster than a point charge's $1/r^2$, because the two opposite fields nearly cancel. And at the same large distance, the axial field is **twice** the equatorial field.

## Worked example

**Given:** a model dipole with charges $\pm 2.0\,\text{nC}$ held $2.0\,\text{cm}$ apart, so $a = 0.010\,\text{m}$.
**Find:** $p$, and the field at $r = 0.20\,\text{m}$ on the axis and on the equatorial line.

$$p = q(2a) = 2.0 \times 10^{-9} \times 0.020 = 4.0 \times 10^{-11}\,\text{C m}$$

Axis (exact):

$$E = \frac{2 \times 9.0 \times 10^9 \times 4.0 \times 10^{-11} \times 0.20}{(0.040 - 0.0001)^2} = \frac{0.144}{0.001592} \approx 90\,\text{N/C}$$

along $\vec{p}$. The approximation $2kp/r^3 = 0.72/0.0080 = 90\,\text{N/C}$ agrees closely, because $r = 20a$.

Equatorial (exact):

$$E = \frac{9.0 \times 10^9 \times 4.0 \times 10^{-11}}{(0.0401)^{3/2}} = \frac{0.36}{0.00803} \approx 45\,\text{N/C}$$

opposite to $\vec{p}$: half the axial value.

**Sanity check:** a single $2.0\,\text{nC}$ charge alone would give $9.0 \times 10^9 \times 2.0 \times 10^{-9}/(0.20)^2 = 450\,\text{N/C}$ at this distance. The dipole's field is five to ten times weaker, because the partner charge nearly cancels it, as it should.

## Where the picture breaks

A water molecule is not two point charges on a stick: its charge is spread out in electron clouds, and at the tiny distances between molecules $r \gg a$ is not true, so these formulas don't give the forces that hold dew to leather. They describe the field **far** from a dipole. Why water wets a ball also depends on the leather's surface, the wax and polish on it and the roughness of the seam, not on dipoles alone. The dew sets the scene; the physics is about the dipole.

## Key takeaway

An electric dipole is $+q$ and $-q$ separated by $2a$, with dipole moment $p = q(2a)$ pointing from $-q$ to $+q$. On the axis $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2pr}{(r^2-a^2)^2}$, along $\vec{p}$; on the equatorial line $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{p}{(r^2+a^2)^{3/2}}$, opposite to $\vec{p}$. Far away both fall as $1/r^3$, with the axial field twice the equatorial.
