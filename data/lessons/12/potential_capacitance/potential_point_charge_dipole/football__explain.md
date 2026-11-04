---
concept_id: potential_point_charge_dipole
interest: football
format: explain
title: The reading that would not fall away fast enough
check:
  question: |-
    A small charged ball is fixed on an insulating stand at the penalty mark. At $2.0\,\text{m}$ from it the potential is $9.0\,\text{V}$. What is the potential at $6.0\,\text{m}$ from it?
  options:
    A: |-
      $1.0\,\text{V}$
    B: |-
      $4.5\,\text{V}$
    C: |-
      $3.0\,\text{V}$
    D: |-
      $27\,\text{V}$
  answer: C
  explanation: |-
    For a point charge $V = kq/r$, so the potential falls as $1/r$. Tripling the distance divides the potential by three: $9.0/3 = 3.0\,\text{V}$.
  misconceptions:
    A: |-
      Uses an inverse-square law, which is how the **field** falls. The potential of a point charge falls only as $1/r$.
    B: |-
      Halves the potential, as if the distance had doubled. It went from $2.0\,\text{m}$ to $6.0\,\text{m}$, which is three times as far.
    D: |-
      Multiplies by three instead of dividing, treating potential as something that grows with distance. It falls with distance.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground at dusk with a floodlight pylon, an electric fence and its energiser box along the far side, a coach holding a touchscreen tablet, a water bowser and an AED cabinet](scenes/football/potential_capacitance.svg "An empty marked-out pitch is also a ready-made ruler: 11 m to the penalty mark, 9.15 m from the centre spot to the edge of the circle.")

The tournament is rained off, the pitch is out of bounds for boots, and Nivedita has talked the caretaker into letting the physics club use it instead. The markings, she points out, are a free measuring grid.

She stands a small metal ball on an insulating rod at the penalty mark and charges it. Her probe, two steps away, reads a steady number.

"Go to four steps," says Aftab. "Twice as far, so it drops to a quarter. Inverse square, everyone knows that."

She walks back. The reading does drop — to a half.

Aftab checks the rod, the probe, and the wet grass. Nivedita then takes the ball off and stands a plastic straw there instead, positively charged at one end and negatively at the other. Now the reading collapses almost to nothing by the time she reaches the centre circle. And standing out sideways from the straw, level with its middle, the probe reads zero however close she brings it.

Same pitch, same probe. Why do the two objects fade away at such different rates?

## The physics

**A point charge.** Adding up the work done bringing a unit positive charge in from infinity to a distance $r$ from a point charge $q$ gives

$$V = \frac{1}{4\pi\varepsilon_0}\,\frac{q}{r} = \frac{kq}{r}, \qquad k = \frac{1}{4\pi\varepsilon_0} \approx 9.0 \times 10^{9}\,\text{N m}^2/\text{C}^2$$

Three things follow, and they settle Aftab's bet:

- $V$ carries the **sign of the charge** — positive near a positive charge, negative near a negative one.
- $V$ falls as $1/r$, while the field falls as $1/r^2$. Go twice as far and the potential halves but the field drops to a quarter. Aftab used the field's law on the potential.
- $V \to 0$ as $r \to \infty$, which is the zero we chose.

![Two graphs for a 1.0 nC charge: the potential falling as one over r, from 9.0 V at 1 m to 4.5 V at 2 m, and the field falling as one over r squared, from 9.0 V/m to 2.25 V/m](figures/potential_point_charge_dipole/point-charge-v-and-e.svg "From 1 m to 2 m the potential halves while the field drops to a quarter. V goes as 1/r, E as 1/r².")

**Several charges.** Potential is a scalar, so you simply add the separate potentials, keeping their signs:

$$V = k\left(\frac{q_1}{r_1} + \frac{q_2}{r_2} + \dots\right)$$

No components, no directions to resolve. This is what makes potential far easier to handle than field.

**A dipole.** Charges $+q$ and $-q$ a distance $2a$ apart form a dipole of moment $p = q \times 2a$, pointing from $-q$ to $+q$. At a distance $r$ from its centre, at an angle $\theta$ to its axis, and only when $r \gg a$:

$$V = \frac{1}{4\pi\varepsilon_0}\,\frac{p\cos\theta}{r^2}$$

On the axis ($\theta = 0$) that is $V = kp/r^2$. On the equatorial line ($\theta = 90^\circ$), $\cos\theta = 0$, so $V = 0$ everywhere — which is exactly where Nivedita's probe read zero. Far away the two opposite charges very nearly cancel, so a dipole's potential dies as $1/r^2$, faster than a single charge's.

![A dipole with minus q and plus q separated by 2a, the moment p pointing from minus to plus, and a point P at distance r and angle theta from the centre](figures/potential_point_charge_dipole/dipole-potential.svg "The formula holds only for r much larger than a. Every point on the equatorial line sits at zero potential.")

## Worked example

Put $+2.0\,\text{nC}$ on one cone and $-2.0\,\text{nC}$ on another, $4.0\,\text{m}$ apart (illustrative charges). Note first that $kq = 9.0 \times 10^{9} \times 2.0 \times 10^{-9} = 18\,\text{V m}$, so each charge contributes $18/r$ volts.

**Find** the potential (a) midway between the cones; (b) on the line between them, $1.0\,\text{m}$ from the positive cone; (c) $20\,\text{m}$ out along that line, past the positive cone.

**(a)** Both cones are $2.0\,\text{m}$ away, so $V = \dfrac{18}{2.0} - \dfrac{18}{2.0} = 0$. Equal and opposite contributions cancel exactly.

**(b)** Here the distances are $1.0\,\text{m}$ and $3.0\,\text{m}$:

$$V = 18\left(\frac{1}{1.0} - \frac{1}{3.0}\right) = 18 \times \frac{2}{3} = 12\,\text{V}$$

Close to the positive cone the positive term wins, so the potential is positive.

**(c)** Now $r = 20\,\text{m}$ is ten times the pair's half-separation $a = 2.0\,\text{m}$, so the dipole formula applies. With $p = 2.0 \times 10^{-9} \times 4.0 = 8.0 \times 10^{-9}\,\text{C m}$ and $\theta = 0$:

$$V \approx \frac{kp}{r^2} = \frac{9.0 \times 10^{9} \times 8.0 \times 10^{-9}}{20^2} = \frac{72}{400} = 0.18\,\text{V}$$

Twelve volts at a metre, a fifth of a volt at twenty. Step back from a dipole and it all but disappears.

**Sanity check:** the exact sum at that point uses $18\,\text{m}$ and $22\,\text{m}$: $18(1/18 - 1/22) = 0.18\,\text{V}$ to two figures. The approximation has earned its keep.

## Where the picture breaks

The pitch supplies the ruler, not the physics. Charges of a few nanocoulombs on cones are a thought experiment: damp grass and humid air would drain them in seconds, and a real probe held near a charge disturbs the very field it is reading. The formulas treat each object as a **point** charge in empty space; near anything bulky you must add up the contributions of all its parts. And the dipole formula is an approximation, good only for $r \gg a$ — inside the pair, as in part (b), you must use the exact sum.

## Key takeaway

A point charge gives $V = kq/r$, carrying the sign of $q$ and falling as $1/r$ — more slowly than the field's $1/r^2$. For several charges, add the potentials as signed numbers. Far from a dipole, $V = p\cos\theta/(4\pi\varepsilon_0 r^2)$: it falls as $1/r^2$, and it is zero everywhere on the equatorial line.
