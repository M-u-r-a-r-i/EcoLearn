---
concept_id: potential_point_charge_dipole
interest: cricket
format: explain
title: The riddle of the charged stumps
check:
  question: |-
    In the coach's riddle, a charge $+q$ sits at one set of stumps and $-q$ at the other, $20.12\,\text{m}$ apart. At the exact middle of the pitch, which statement is correct?
  options:
    A: |-
      The potential is zero and the electric field is zero.
    B: |-
      The potential is zero, but the field is not zero; it points towards the $-q$ end.
    C: |-
      The potential is $2kq/(10.06\,\text{m})$, the two contributions added together.
    D: |-
      The potential is large and positive, because the field is strongest there.
  answer: B
  explanation: |-
    Potentials add as signed scalars: $kq/r - kq/r = 0$. Fields add as vectors, and both charges' fields at the middle point towards the $-q$ end, so they add instead of cancelling.
  misconceptions:
    A: |-
      Assumes zero potential means zero field. The field depends on how fast $V$ changes with position, not on the value of $V$ at the point.
    C: |-
      Adds the sizes of the two contributions and ignores the sign of the charge. The potential of a negative charge is negative.
    D: |-
      Confuses potential with field strength, as if a strong field must mean a high potential.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground under a storm cloud with lightning in the distance, a floodlight tower, a curator on the pitch, a car by the boundary and a photographer's flash](scenes/cricket/potential_capacitance.svg "The pitch: 20.12 m from one set of stumps to the other. Today it becomes the setting for a thought experiment.")

Practice is over and the under-17 squad is helping roll the pitch. Mrs Deshpande teaches physics in the mornings and coaches them in the afternoons. She leans on the roller and sets a riddle.

"Imagine a tiny positive charge fixed on the middle stump at this end," she says, "and an equal negative charge on the middle stump at the far end. Twenty-two yards apart. What is the potential exactly halfway down the pitch?"

Tanmay answers at once. "Huge. The field is strongest between two opposite charges, everyone knows that."

Meera shakes her head. "Zero. They cancel."

"Loser carries the kit bags to the bus," Tanmay says.

Mrs Deshpande only smiles. "And while you're at it, work out the potential anywhere else on the pitch too. Then tell me what a spectator a hundred metres away would measure."

Who carries the kit bags?

## The physics

**A point charge.** Bringing a unit positive charge from infinity to a distance $r$ from a point charge $q$ takes work against the field. Adding up that work gives the potential:

$$V = \frac{1}{4\pi\varepsilon_0}\,\frac{q}{r} = \frac{kq}{r}, \qquad k = \frac{1}{4\pi\varepsilon_0} \approx 9.0 \times 10^{9}\,\text{N m}^2/\text{C}^2$$

Three things follow from this formula:

- $V$ has the **sign of the charge**. It is positive near a positive charge and negative near a negative one.
- $V$ falls as $1/r$, more slowly than the field, which falls as $1/r^2$. Double the distance and the potential halves, while the field drops to a quarter.
- $V \to 0$ as $r \to \infty$. That is the reference we chose.

![Two graphs for a 1.0 nC charge: the potential falls as 1 over r, from 9.0 V at 1 m to 4.5 V at 2 m; the field falls as 1 over r squared, from 9.0 V/m to 2.25 V/m](figures/potential_point_charge_dipole/point-charge-v-and-e.svg "From 1 m to 2 m the potential halves, but the field drops to a quarter. V goes as 1/r, E as 1/r².")

**A system of charges.** Potential is a scalar, so for several charges you simply add the individual potentials, with their signs:

$$V = k\left(\frac{q_1}{r_1} + \frac{q_2}{r_2} + \dots\right)$$

There are no components and no directions to resolve. This is what makes potential easier to work with than field.

**A dipole.** Charges $+q$ and $-q$ separated by $2a$ form a dipole with moment $p = q \times 2a$, pointing from $-q$ to $+q$. At a distance $r$ from its centre, at an angle $\theta$ to its axis, with $r \gg a$:

$$V = \frac{1}{4\pi\varepsilon_0}\,\frac{p\cos\theta}{r^2}$$

On the axis ($\theta = 0$) this becomes $V = kp/r^2$. On the equatorial line ($\theta = 90^\circ$), $V = 0$ everywhere. A dipole's potential falls as $1/r^2$, faster than a single charge's, because far away the two opposite charges nearly cancel.

![A dipole with minus q and plus q separated by 2a, moment p from minus to plus, and a point P at distance r and angle theta](figures/potential_point_charge_dipole/dipole-potential.svg "The dipole formula needs r to be much larger than a. Every point on the equatorial line is at zero potential.")

## Worked example

**Given:** $+2.0\,\mu\text{C}$ at one set of stumps and $-2.0\,\mu\text{C}$ at the other, $d = 20.12\,\text{m}$ apart. These charges are illustrative.
**Find:** the potential (a) at the middle of the pitch; (b) $2.0\,\text{m}$ from the positive charge, along the pitch; (c) $100\,\text{m}$ away on the line of the pitch, beyond the positive end.

Note that $kq = 9.0 \times 10^9 \times 2.0 \times 10^{-6} = 1.8 \times 10^4\,\text{V m}$.

(a) Both charges are $10.06\,\text{m}$ away: $V = \dfrac{1.8 \times 10^4}{10.06} - \dfrac{1.8 \times 10^4}{10.06} = 0$.
The field is **not** zero there. Each charge contributes $\dfrac{1.8 \times 10^4}{10.06^2} \approx 178\,\text{N/C}$, and both point towards the negative end, so $E \approx 3.6 \times 10^2\,\text{N/C}$.

(b) Here $r_+ = 2.0\,\text{m}$ and $r_- = 18.12\,\text{m}$:

$$V = 1.8 \times 10^4\left(\frac{1}{2.0} - \frac{1}{18.12}\right) = 1.8 \times 10^4 \times 0.4448 \approx 8.0 \times 10^3\,\text{V}$$

(c) Here $r = 100\,\text{m}$ is about ten times $a = 10.06\,\text{m}$, so try the dipole formula. $p = 2.0 \times 10^{-6} \times 20.12 = 4.02 \times 10^{-5}\,\text{C m}$:

$$V \approx \frac{kp}{r^2} = \frac{9.0 \times 10^9 \times 4.02 \times 10^{-5}}{100^2} \approx 36\,\text{V}$$

**Sanity check:** the exact sum gives $1.8 \times 10^4\left(\dfrac{1}{89.94} - \dfrac{1}{110.06}\right) \approx 36.6\,\text{V}$. The dipole formula is within about 1%, and it improves as $r$ grows.

Meera wins the bet. Tanmay carries the bags.

## Where the picture breaks

This is a thought experiment on a cricket pitch, not something that happens at a match. No one fixes charges to stumps, and a real stump in damp ground would let charge leak away. The formulas assume **point** charges in empty space. Near real, spread-out objects you must add up the contributions of every part. The dipole formula is an approximation that holds only for $r \gg a$. Close to the pitch you must use the exact sum.

## Key takeaway

A point charge gives $V = kq/r$, with the sign of $q$. For many charges, add the potentials as signed numbers: $V = k\sum q_i/r_i$. A dipole gives $V = p\cos\theta/(4\pi\varepsilon_0 r^2)$ far away. Zero potential does not mean zero field.
