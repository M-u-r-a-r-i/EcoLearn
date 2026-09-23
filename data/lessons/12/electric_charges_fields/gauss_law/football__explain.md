---
concept_id: gauss_law
interest: football
format: explain
title: Why the size of the ring never changes the count
check:
  question: |-
    A closed Gaussian surface is drawn around a charged ball, and the net flux through it is $\Phi$. Without moving the ball, you redraw the surface twice as far out on every side and make it lumpy and irregular instead of spherical. What is the net flux through the new surface?
  options:
    A: |-
      Still $\Phi$, because the surface encloses exactly the same charge.
    B: |-
      $\Phi/4$, because the field at the new surface is four times weaker.
    C: |-
      $2\Phi$, because the new surface has more area for the field to cross.
    D: |-
      It cannot be found, because the flux formula only works for a sphere.
  answer: A
  explanation: |-
    Gauss's law says $\oint \vec{E} \cdot d\vec{S} = q_\text{enc}/\varepsilon_0$. The enclosed charge is unchanged, so the net flux is unchanged — the size and shape of the surface do not appear in the law at all.
  misconceptions:
    B: |-
      Applies the inverse-square fall-off of $\vec{E}$ to the flux. The field is indeed four times weaker, but it is spread over four times the area, and the two changes cancel exactly.
    C: |-
      Treats flux as "area times something fixed". Flux is field *times* area, and the field falls off exactly as fast as the area grows.
    D: |-
      Confuses the law with the trick used to apply it. Gauss's law is true for every closed surface; only the shortcut $\Phi = EA$ needs the symmetry of a sphere, cylinder or pillbox.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit ground as a storm arrives: lightning above the stand, rain falling, a player peeling off a crackling nylon bib, and two players heading for the metal-roofed dugout](scenes/football/electric_charges_fields.svg "A storm is a huge charge separation overhead. What crosses a closed surface depends only on what is inside it.")

Coach Devika runs the same warm-up every week. She stands on the centre spot with a sack of balls and plays one out, steadily, one every two seconds, to whoever calls for it. The squad jogs round her in a ring.

For the first few minutes the ring is the centre circle itself, and the passes come hard and quick. Then she waves everyone out to the touchlines. Now they arrive slower, softer, more spread out, and someone shouts that the drill has gone easy.

Farhan is on the sideline with an ankle strapped and a stopwatch, and he is the only one counting. Wide ring or tight ring, the number of balls crossing the ring each minute has not budged. It is whatever Devika sends out.

Then a ball from the next pitch comes skidding through: in one side of the ring, out the other. One in, one out. His net count does not move at all.

A charge throws its field out in every direction like that. Does the total crossing a closed surface depend on how big you draw it — or only on what sits inside?

## The physics

The flux through a small patch is $\vec{E} \cdot \Delta\vec{S}$, and on a **closed** surface the area vector always points **outwards**. Add up every patch and you have the total flux, written $\oint \vec{E} \cdot d\vec{S}$.

**Gauss's law.** The net electric flux out of any closed surface equals the net charge it encloses, divided by $\varepsilon_0$:

$$\Phi = \oint \vec{E} \cdot d\vec{S} = \frac{q_\text{enc}}{\varepsilon_0}$$

Here $\varepsilon_0 = 8.854 \times 10^{-12}\,\text{C}^2/(\text{N m}^2)$ is the permittivity of free space, and the closed surface you invent is a **Gaussian surface**. It is imaginary — nothing has to be there.

**Why it comes out that way.** Put a charge $q$ at the centre of a sphere of radius $r$. All over the sphere the field is radial, so it crosses the surface squarely, with size $E = \dfrac{q}{4\pi\varepsilon_0 r^2}$. Then

$$\Phi = E \times 4\pi r^2 = \frac{q}{4\pi\varepsilon_0 r^2} \times 4\pi r^2 = \frac{q}{\varepsilon_0}$$

The $r^2$ cancels: a bigger sphere has a weaker field spread over a larger area, which is Farhan's wide ring exactly. That cancellation happens only because the field obeys an inverse-square law. Push the sphere out of shape and the same lines still have to get out, so the flux is unchanged.

![A closed surface enclosing charges of +3.0 nC and −1.0 nC, with a +5.0 nC charge outside whose field line enters the surface and leaves again](figures/gauss_law/closed-surface-charges.svg "Only the charge inside sets the net flux — here 2.0 nC divided by ε₀. The outside charge's line enters (negative flux) and leaves again (positive flux), for no net contribution.")

Three things to read carefully:

- **$q_\text{enc}$ is an algebraic sum.** Negative charge inside sends lines inwards, which count as negative flux. Equal and opposite charges inside give zero net flux.
- **Charges outside contribute nothing to the net flux** — every line that enters also leaves.
- **But $\vec{E}$ in the integral is the total field**, from every charge, inside and outside. Zero net flux does not mean zero field on the surface.

The law holds for any closed surface and any static charges, as long as the surface does not pass through a point charge, where the field is undefined.

## Worked example

**Given (illustrative):** inside a closed net bag are two charged objects, $+5\,\text{nC}$ and $-2\,\text{nC}$. A third object, $+8\,\text{nC}$, rests just outside the bag.
**Find:** the net electric flux through the bag.

**Step 1 — the charge enclosed.**

$$q_\text{enc} = +5 - 2 = +3\,\text{nC} = 3.0 \times 10^{-9}\,\text{C}$$

The $+8\,\text{nC}$ outside does not appear: its lines enter the bag on one side and leave on the other.

**Step 2 — put it into Gauss's law.**

$$\Phi = \frac{q_\text{enc}}{\varepsilon_0} = \frac{3.0 \times 10^{-9}}{8.854 \times 10^{-12}} \approx 3.4 \times 10^{2}\,\text{N m}^2/\text{C}$$

A net outward flux, because the charge inside is positive.

**Sanity check:** the answer follows the charge inside and nothing else — take the $-2\,\text{nC}$ out and the flux rises, drop a $-3\,\text{nC}$ in and it falls to zero, while squashing or stretching the bag changes nothing.

## Where the picture breaks

Passes are real, countable objects that travel; a field does not flow, and no thing moves along a field line. Devika's ring also works only because she passes at a steady rate — real balls get held, mis-controlled and lost, so the count would drift, while the electric flux is exact. And balls come one way out of the sack, whereas charge has two signs, so a closed surface can have negative net flux, or zero net flux with a strong field all over it. The ring is a way to feel why the law is plausible; the proof is the inverse-square law and nothing else.

## Key takeaway

Gauss's law: the net flux out of **any** closed surface is the enclosed charge divided by $\varepsilon_0$, $\oint \vec{E} \cdot d\vec{S} = q_\text{enc}/\varepsilon_0$. The surface's size and shape make no difference, charges outside add nothing to the net flux, and the charge inside is counted with its sign.
