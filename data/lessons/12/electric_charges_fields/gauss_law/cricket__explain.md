---
concept_id: gauss_law
interest: cricket
format: explain
title: The sprinkler under the covers and the charge inside a closed surface
check:
  question: |-
    During a rain delay, a closed Gaussian surface is drawn around a charged cricket ball. Inside the surface are charges of $+6.0\,\text{nC}$ and $-2.0\,\text{nC}$; a charge of $+10\,\text{nC}$ sits just outside it. Taking $\varepsilon_0 = 8.85 \times 10^{-12}\,\text{C}^2/(\text{N m}^2)$, what is the net electric flux through the closed surface?
  options:
    A: |-
      $1.6 \times 10^{3}\,\text{N m}^2/\text{C}$
    B: |-
      $9.0 \times 10^{2}\,\text{N m}^2/\text{C}$
    C: |-
      $36\,\text{N m}^2/\text{C}$
    D: |-
      $4.5 \times 10^{2}\,\text{N m}^2/\text{C}$
  answer: D
  explanation: |-
    Only the enclosed charge counts, with its sign: $q_\text{enc} = +6.0 - 2.0 = +4.0\,\text{nC}$, so $\Phi = q_\text{enc}/\varepsilon_0 = 4.0 \times 10^{-9} / 8.85 \times 10^{-12} \approx 4.5 \times 10^{2}\,\text{N m}^2/\text{C}$. The outside charge's field lines enter and leave the surface, adding nothing to the net flux.
  misconceptions:
    A: |-
      Includes the $+10\,\text{nC}$ charge outside the surface. Its field does pass through the surface, but every line that enters also leaves, so its net flux is zero.
    B: |-
      Adds the sizes of the enclosed charges ($6.0 + 2.0 = 8.0\,\text{nC}$) and ignores the sign of the negative one, whose lines point inwards and give negative flux.
    C: |-
      Uses $\Phi = kq_\text{enc}$, forgetting the factor $4\pi$: the flux is $q_\text{enc}/\varepsilon_0 = 4\pi k\,q_\text{enc}$, not $k\,q_\text{enc}$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A storm over a cricket ground: dark clouds, distant lightning, players walking off, groundstaff dragging a plastic cover and a team bus waiting](scenes/cricket/electric_charges_fields.svg "The covers go on the square; what matters for a closed cover is what is inside it.")

It's the night before a four-day match, and Riya is helping the head groundsman, Joseph, water the square. He sets a rotating sprinkler in the middle of the pitch and opens the valve: it throws out a steady 20 litres a minute, and the spray hisses in a circle under the floodlights.

"Here's a puzzle my old coach gave me," Joseph says. "Draw an imaginary bubble around the sprinkler. A small one, just around the nozzle, or a huge one, the size of the whole square. Squash it into a weird shape if you like. How much water crosses the bubble every minute?"

Riya thinks. The small bubble is hit by fast, dense spray; the big one by thin drizzle spread over a vast area. The hose that runs *past* the square, from the tap to the next pitch, pushes water through the bubble too.

Then it's her turn to wonder. A charge sends its electric field out in every direction, just like the spray. Does the total field crossing a closed surface depend on the surface's size and shape, or only on what sits inside it?

## The physics

Recall that the flux through a small patch is $\vec{E} \cdot \Delta\vec{S}$, and for a **closed** surface the area vector always points **outwards**. Add it up over the whole closed surface and you get the total flux, written $\oint \vec{E} \cdot d\vec{S}$.

**Gauss's law.** The total electric flux through any closed surface equals the net charge enclosed by the surface divided by $\varepsilon_0$:

$$\Phi = \oint \vec{E} \cdot d\vec{S} = \frac{q_\text{enc}}{\varepsilon_0}$$

Here $\varepsilon_0 = 8.854 \times 10^{-12}\,\text{C}^2/(\text{N m}^2)$ is the permittivity of free space, and the closed surface you choose is called a **Gaussian surface**.

**Why it's true, for a point charge.** Put a charge $q$ at the centre of a sphere of radius $r$. Everywhere on the sphere the field points straight outwards (along the normal) with size $E = \dfrac{q}{4\pi\varepsilon_0 r^2}$. So

$$\Phi = E \times 4\pi r^2 = \frac{q}{4\pi\varepsilon_0 r^2} \times 4\pi r^2 = \frac{q}{\varepsilon_0}$$

The $r^2$ cancels. A bigger sphere has a weaker field over a larger area, exactly like Joseph's thinner drizzle over the bigger bubble. That cancellation is a direct result of the inverse-square law. Stretch the sphere into any other shape and the same field lines still have to cross it, so the flux stays $q/\varepsilon_0$.

![A closed surface containing +3.0 nC and −1.0 nC, with a +5.0 nC charge outside whose field line enters the surface and leaves again](figures/gauss_law/closed-surface-charges.svg "Only the charge inside counts. The outside charge's line enters (negative flux) and leaves (positive flux): net zero. Here the flux is 2.0 nC divided by ε₀.")

Three things to read carefully in the law:

- **$q_\text{enc}$ is the algebraic sum.** Negative charge inside gives inward lines, which are negative flux. Equal and opposite charges inside give zero total flux.
- **Charges outside contribute zero net flux**, because every line that enters also leaves.
- **But $\vec{E}$ in the integral is the total field, from all charges, inside and outside.** Zero flux does not mean zero field on the surface: it means the inward and outward contributions cancel.

The Gaussian surface must not pass through a point charge, where the field isn't defined. Gauss's law holds for any closed surface and any charges at rest; it is most useful when symmetry lets you find $\vec{E}$ from it, which is the next concept.

## Worked example

**Given:** a charge $q = +3.0\,\text{nC}$ (illustrative) at the centre of a closed cubical kit box.
**Find:** (a) the total flux out of the box; (b) the flux through one face; (c) the total flux if a $-3.0\,\text{nC}$ charge is added inside.

(a) Gauss's law, with $q = 3.0 \times 10^{-9}\,\text{C}$:

$$\Phi = \frac{q}{\varepsilon_0} = \frac{3.0 \times 10^{-9}}{8.854 \times 10^{-12}} \approx 3.4 \times 10^{2}\,\text{N m}^2/\text{C}$$

(b) The charge is at the centre, so by symmetry all six faces get equal shares:

$$\Phi_\text{face} = \frac{339}{6} \approx 56\,\text{N m}^2/\text{C}$$

(c) Now $q_\text{enc} = +3.0 - 3.0 = 0$, so the total flux is **zero**, even though the field at the box's walls is not zero.

**Sanity check:** a sphere around the charge gives $E \times 4\pi r^2 = \dfrac{kq}{r^2} \times 4\pi r^2 = 4\pi \times 9.0 \times 10^9 \times 3.0 \times 10^{-9} = 4\pi \times 27 \approx 339\,\text{N m}^2/\text{C}$, the same answer from a different shape. Units: $\text{C} / (\text{C}^2\,\text{N}^{-1}\,\text{m}^{-2}) = \text{N m}^2/\text{C}$. Correct.

## Where the picture breaks

The sprinkler is a real flow: water moves outwards, and in a real ground some of it soaks into the grass or evaporates before it reaches a big bubble, so its "flux" isn't perfectly conserved. An electric field doesn't flow and isn't lost with distance in that way; the exact $1/r^2$ fall-off is what makes Gauss's law exact. Also, a sprinkler only pushes water out, but charges come in two signs, so a closed surface can have negative flux (more lines going in) or zero flux with strong fields all over it. The cricket ground is only a frame here; the law itself is pure electrostatics.

## Key takeaway

Gauss's law: the total flux out of any closed surface is the net charge inside divided by $\varepsilon_0$, $\oint \vec{E} \cdot d\vec{S} = q_\text{enc}/\varepsilon_0$. The size and shape of the surface don't matter, charges outside add nothing to the net flux, and the enclosed charge is counted with its sign.
