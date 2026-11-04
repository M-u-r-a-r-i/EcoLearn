---
concept_id: gauss_law
interest: gaming
format: explain
title: The scanner that ignored everything outside
check:
  question: |-
    A closed surface in Manav's simulation encloses a single charge $+q$, and the scanner reports a net flux $q/\varepsilon_0$. He then doubles the radius of the surface and slides a second charge, $+2q$, to a point just **outside** it. What does the scanner report now?
  options:
    A: |-
      $q/\varepsilon_0$, unchanged
    B: |-
      A quarter as much, because the field at the surface is now four times weaker
    C: |-
      $3q/\varepsilon_0$, because the new charge's field also crosses the surface
    D: |-
      Half as much, because the same field lines are now spread over twice the radius
  answer: A
  explanation: |-
    Gauss's law gives $\Phi = q_\text{enc}/\varepsilon_0$. The enclosed charge is still $+q$, the size of the surface never mattered, and the charge outside sends every line that enters back out again, for zero net contribution.
  misconceptions:
    B: |-
      Notices that the field is four times weaker but forgets that the area is four times bigger. The two changes cancel exactly — that is the whole content of Gauss's law for a point charge.
    C: |-
      Counts charges outside the surface. Their field really does pass through it, but each line that enters also leaves, so the net flux they add is zero.
    D: |-
      Thinks flux thins out with distance the way field strength does. Flux counts lines crossing the surface, and no line is lost on the way out.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night during a PC build: a monitor running a field sandbox with two charges, a plasma globe, an antistatic bag sparking to a fingertip, and an open PC case with a graphics card going in](scenes/gaming/electric_charges_fields.svg "Draw an imaginary closed bubble anywhere in that sandbox. What crosses it?")

Manav's sandbox has grown a new tool. You drag out a closed bubble anywhere on the grid, and the program samples the field over the whole of the bubble's skin, multiplies each patch by the bit of field crossing it outwards, and adds everything up.

He builds it expecting a messy number that changes with every drag. Instead the readout sticks. He shrinks the bubble to a pinprick around one charge: same number. He blows it up to fill the screen: same number. He drags one corner until the bubble looks like a squashed balloon: same number.

Then he drags a second charge across the grid from the far side. Nothing on the readout moves — until the moment the charge crosses the skin and goes inside, when the number jumps.

Manav files a bug against his own code. His teacher reads it over his shoulder and laughs. "That isn't a bug," she says. "You've just measured Gauss's law." So what is it about a closed surface that makes its size, its shape and everything outside it simply not count?

## The physics

The flux through one small patch is $\vec{E} \cdot \Delta\vec{S}$, and on a **closed** surface the area vector always points **outwards**. Add up every patch and you have the total flux, written $\oint \vec{E} \cdot d\vec{S}$.

**Gauss's law.** The total electric flux through any closed surface equals the net charge enclosed, divided by $\varepsilon_0$:

$$\Phi = \oint \vec{E} \cdot d\vec{S} = \frac{q_\text{enc}}{\varepsilon_0}$$

with $\varepsilon_0 = 8.854 \times 10^{-12}\,\text{C}^2/(\text{N m}^2)$. The closed surface you choose is called a **Gaussian surface**; it is imaginary, and you may put it wherever you like.

**Why it is true, for a point charge.** Put $q$ at the centre of a sphere of radius $r$. Everywhere on that sphere the field points straight out along the normal, with the same size $E = \dfrac{q}{4\pi\varepsilon_0 r^2}$. So

$$\Phi = E \times 4\pi r^2 = \frac{q}{4\pi\varepsilon_0 r^2} \times 4\pi r^2 = \frac{q}{\varepsilon_0}$$

The $r^2$ cancels: a bigger sphere has a weaker field spread over a larger area, and the two changes match exactly because the field obeys an inverse-square law. Deform the sphere into any other closed shape and the same lines still have to get out, so the total is unchanged — which is precisely what Manav's bubble kept reporting.

![A closed Gaussian surface containing a plus 3.0 nC and a minus 1.0 nC charge, with a plus 5.0 nC charge outside whose field line enters the surface and leaves again](figures/gauss_law/closed-surface-charges.svg "Only the charge inside counts. The outside charge's line enters (negative flux) and leaves again (positive flux), for nothing. Here the flux is 2.0 nC divided by ε₀.")

Three things to read carefully in the law.

- **$q_\text{enc}$ is an algebraic sum.** Negative charge inside means inward lines, which count as negative flux, so equal and opposite charges inside give zero total.
- **Charges outside contribute nothing to the net flux**, because every line of theirs that enters also leaves.
- **But $\vec{E}$ in the integral is the total field**, from every charge inside *and* outside. Zero flux does not mean zero field on the surface; it means the inward and outward parts cancel.

The surface must not pass through a point charge, where the field is undefined. Gauss's law holds for any closed surface and any charges at rest.

## Worked example

**Given (illustrative):** a Gaussian surface encloses charges of $+3.0\,\text{nC}$ and $-1.0\,\text{nC}$. A charge of $+5.0\,\text{nC}$ sits just outside it.
**Find:** the net flux through the surface, and what happens to it if the surface is stretched to twice the size.

**Step 1 — the enclosed charge.** Add the inside charges with their signs, and ignore the outside one:

$$q_\text{enc} = +3.0 - 1.0 = +2.0\,\text{nC}$$

**Step 2 — the flux.**

$$\Phi = \frac{q_\text{enc}}{\varepsilon_0} = \frac{2.0 \times 10^{-9}}{8.854 \times 10^{-12}} \approx 2.3 \times 10^{2}\,\text{N m}^2/\text{C}$$

The flux is positive, so on balance the lines point outwards — as they should, with a net positive charge inside.

**Step 3 — stretch the surface.** Nothing changes. As long as the same charges stay inside, $\Phi$ is still $2.3 \times 10^{2}\,\text{N m}^2/\text{C}$.

**Sanity check a second way:** $\Phi = 4\pi k\,q_\text{enc} = 4\pi \times 9.0 \times 10^9 \times 2.0 \times 10^{-9} = 4\pi \times 18 \approx 226$, agreeing with the first route to the precision of the rounded $k$.

## Where the picture breaks

Manav's scanner only *looks* like Gauss's law. It samples the field at a finite number of patches and adds them up, so its answer is an approximation that gets better as the patches get smaller, while the law itself is exact. Drag the bubble so its skin passes exactly through a charge and his program will happily print a number; the law simply does not apply there.

And the tool tempts you into one real misreading. Because the readout depends only on the inside, it is easy to conclude that outside charges do not matter at all. They matter enormously — they change $\vec{E}$ at every point of the surface. They just cannot change the *total* of $\vec{E} \cdot d\vec{S}$.

## Key takeaway

Gauss's law says the total flux out of any closed surface is the net charge inside divided by $\varepsilon_0$: $\oint \vec{E} \cdot d\vec{S} = q_\text{enc}/\varepsilon_0$. The size and shape of the surface make no difference, charges outside add nothing to the net flux, and the enclosed charge is counted with its sign.
