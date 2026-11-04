---
concept_id: potential_point_charge_dipole
interest: gaming
format: explain
title: The map you can add up with plain numbers
check:
  question: |-
    Two charges, $+4.0\,\text{nC}$ and $-4.0\,\text{nC}$, are held $8.0\,\text{cm}$ apart. What is the electrostatic potential at the midpoint of the line joining them?
  options:
    A: |-
      Zero — although the electric field at that point is not zero.
    B: |-
      $1800\,\text{V}$
    C: |-
      $900\,\text{V}$
    D: |-
      Zero, and so the electric field there must be zero as well.
  answer: A
  explanation: |-
    Each charge is $4.0\,\text{cm}$ from the midpoint and contributes $\pm kq/r = \pm 900\,\text{V}$, so the potentials cancel. The two *fields*, however, point the same way there and add.
  misconceptions:
    B: |-
      Adds the two contributions as sizes and ignores the minus sign of the negative charge. Potential is a signed scalar: a negative charge lowers the potential.
    C: |-
      Counts only one charge, usually the positive one, as if the other were too far away or did not count.
    D: |-
      Assumes that zero potential means zero field. $V$ is a number and $E$ is a vector; at the midpoint of a dipole the two fields point the same way and add to their largest value.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk with a monitor showing rings of equal potential around a charge, a phone with a fingertip on its screen, an old picture tube on the bench and an opened power supply with two big capacitors](scenes/gaming/potential_capacitance.svg "The monitor is showing a map of one number per point, with no arrows in it at all. That is the idea this lesson is about.")

Kavya's stealth game has a problem: her guards are stupid. She wants each one to drift towards trouble, so she is building a **danger map** — a grid over the level where every cell holds one number, glowing red where it is high.

Each alarm on the level dumps some danger into the grid, spread out around it, fading with distance. Her teammate Nikhil watches her fill in the second alarm and stops her.

"You can't just add them. Last month we did the push-forces version and you had to add arrows, remember? Direction mattered. Same thing here."

"It isn't the same thing," Kavya says. "This is one number per cell. I'm adding numbers."

They argue for twenty minutes without settling it. Somewhere underneath the argument is a real question, and it is a physics question: is there a quantity around a charge that you can add up as plain signed numbers — no arrows, no angles — and if there is, how does it fade with distance?

## The physics

**A single point charge.** The potential a distance $r$ from an isolated point charge $q$, with the zero of potential taken at infinity, is

$$V = \frac{1}{4\pi\varepsilon_0}\frac{q}{r} = \frac{kq}{r}, \qquad k = 9.0 \times 10^{9}\,\text{N}\,\text{m}^2/\text{C}^2$$

The sign of $q$ comes along for the ride: a positive charge raises the potential around it, a negative charge lowers it. Notice the $r$, not $r^2$. The **field** of a point charge falls as $1/r^2$; the **potential** falls only as $1/r$.

![Two graphs for a 1.0 nC charge: the potential falls as 1 over r, from 9.0 V at 1 m to 4.5 V at 2 m; the field falls as 1 over r squared, from 9.0 V/m to 2.25 V/m](figures/potential_point_charge_dipole/point-charge-v-and-e.svg "From 1 m to 2 m the potential halves, but the field drops to a quarter. V goes as 1/r, E as 1/r².")

**A system of charges.** This is Kavya's point, and it is the reason potential is worth having. For several charges $q_1, q_2, \dots$ at distances $r_1, r_2, \dots$ from the point of interest,

$$V = k\left(\frac{q_1}{r_1} + \frac{q_2}{r_2} + \dots\right)$$

an ordinary **algebraic sum** — signs included, directions nowhere. The field needs vector addition; the potential does not. That is why physicists often find $V$ first and get $E$ from it afterwards.

**A dipole.** For two equal and opposite charges $\pm q$ a distance $2a$ apart, the dipole moment is $p = q\,(2a)$, pointing from $-q$ to $+q$. At a point far away — $r \gg a$ — at an angle $\theta$ to the dipole axis,

$$V = \frac{kp\cos\theta}{r^{2}}$$

Two things follow. The potential falls as $1/r^2$, faster than a single charge's $1/r$, because the two charges nearly cancel at a distance. And on the **equatorial plane**, where $\theta = 90°$ and $\cos\theta = 0$, the potential is zero everywhere — every point there is equally far from both charges.

![A dipole with minus q and plus q separated by 2a, moment p from minus to plus, and a point P at distance r and angle theta](figures/potential_point_charge_dipole/dipole-potential.svg "The dipole formula needs r to be much larger than a. Every point on the equatorial line is at zero potential.")

## Worked example

Two charges are fixed on a bench: $q_1 = +2.0\,\text{nC}$ and $q_2 = -1.0\,\text{nC}$. A point $P$ is $20\,\text{cm}$ from $q_1$ and $10\,\text{cm}$ from $q_2$.

**Find:** the potential at $P$.

**Step 1 — what the positive charge gives.**

$$V_1 = \frac{kq_1}{r_1} = \frac{9.0 \times 10^{9} \times 2.0 \times 10^{-9}}{0.20} = \frac{18}{0.20} = +90\,\text{V}$$

**Step 2 — what the negative charge gives.** It is half the size, but only half as far away:

$$V_2 = \frac{kq_2}{r_2} = \frac{9.0 \times 10^{9} \times (-1.0 \times 10^{-9})}{0.10} = \frac{-9.0}{0.10} = -90\,\text{V}$$

**Step 3 — add them as numbers.** $V = +90 - 90 = 0\,\text{V}$.

So it takes **no net work at all** to bring a charge from far away to $P$ — not because nothing pushes on it, but because the pushing and the pulling cancel out over the whole journey.

**Sanity check:** since $V$ goes as $q/r$, halving the charge and halving the distance leaves the size of the contribution unchanged — so the two terms were bound to be equal and opposite.

## Where the picture breaks

Kavya's danger map is a designer's invention: she chooses how the danger fades, and she could make it fade as $1/r$, as $1/r^2$ or however the level plays best. Nature does not offer that choice — around a point charge the potential falls as $1/r$ and nothing else. Her map is also never negative, while potential cheerfully is. And the fact that the numbers add is a genuine physical result, not a convenience: it follows from the superposition of forces, which holds for electrostatics and need not hold for every field a game invents. One more limit worth keeping: $V = kq/r$ takes the zero of potential at infinity, so it is not the formula to use for charge spread over an infinite sheet or wire, where "infinitely far away" is not a sensible place to call zero.

## Key takeaway

Around a point charge, $V = kq/r$ — falling as $1/r$, carrying the sign of the charge. For several charges the potentials add as plain signed numbers, with no directions involved, which is what makes potential so much easier to work with than the field. For a dipole at $r \gg a$, $V = kp\cos\theta/r^2$, which is zero everywhere on the equatorial plane.
