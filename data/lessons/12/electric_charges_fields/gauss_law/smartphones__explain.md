---
concept_id: gauss_law
interest: smartphones
format: explain
title: Weighing the charge inside a sealed gift box
check:
  question: |-
    A sealed waterproof phone pouch contains two charged items, $+2.0\,\text{nC}$ and $-2.0\,\text{nC}$. Outside the pouch, a few centimetres away, lies a charged comb carrying $+5.0\,\text{nC}$. What is the net electric flux through the closed surface of the pouch?
  options:
    A: |-
      $5.0\,\text{nC}/\varepsilon_0$
    B: |-
      Zero
    C: |-
      $4.0\,\text{nC}/\varepsilon_0$
    D: |-
      It cannot be found without knowing the pouch's shape and size
  answer: B
  explanation: |-
    Gauss's law says the net flux through a closed surface is $q_\text{enc}/\varepsilon_0$. The enclosed charge is $(+2.0) + (-2.0) = 0$, and the comb outside contributes no net flux, since every line of its field that enters the pouch also leaves it. So the net flux is zero.
  misconceptions:
    A: |-
      Counts the charge outside the surface. An outside charge's field lines enter and leave the surface, so its net flux through it is zero.
    C: |-
      Adds the sizes of the enclosed charges and ignores their signs. Charge is additive with signs, so $+2.0$ and $-2.0\,\text{nC}$ enclose zero.
    D: |-
      Thinks the flux depends on the surface's shape and size. Gauss's law gives the same net flux through every closed surface enclosing the same charge.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a sunny window with a solar power bank on the sill, an opened phone box with foam beads clinging to the new phone, a film being peeled off a screen with dust jumping up to it, and a phone on a stand running a field-line app](scenes/smartphones/electric_charges_fields.svg "The phone box on the left is a closed container. Could you tell how much charge is inside it without ever opening it?")

It's Siddharth's birthday, and his sister Mehak has wrapped a small box containing new wireless earbuds. The earbuds' plastic case rubbed against the foam packing all the way from the shop, so it's charged.

Siddharth, who has just finished his physics chapter, shakes the box and makes a boast. "I don't need to open it. Give me a field meter, and by measuring only on the *outside* of the box, I can tell you exactly how much charge is inside."

"Rubbish," says Mehak. "The case could be in the corner, or in the middle, or tilted. And what about your phone lying next to the box? That's charged too; the meter would pick it up."

It sounds like she's right. The field around the box surely depends on where the case sits, and on everything else nearby. How could anything measured on the outside of a closed box reveal exactly what's inside?

## The physics

**Gauss's law:** the net electric flux through **any closed surface** equals the total charge **enclosed** by it, divided by $\varepsilon_0$:

$$\oint \vec{E} \cdot d\vec{S} = \frac{q_\text{enc}}{\varepsilon_0}$$

The circle on the integral means "over a closed surface", with the normal taken **outwards**. The closed surface is called a **Gaussian surface**; it can be real, like the box's wrapping, or imaginary.

What makes the law so powerful:

- **Only enclosed charge counts.** A charge outside sends field lines *into* the surface (negative flux) and the same lines *out* again (positive flux): net zero. Siddharth's phone next to the box adds nothing to the total.
- **Position inside doesn't matter.** Wherever the case sits in the box, all its field lines must cross the surface once on the way out.
- **Shape and size don't matter.** A shoebox, a sphere or the wrapping paper, however big: the same enclosed charge gives the same net flux.
- **Signs count.** $q_\text{enc}$ is the algebraic sum: $+3\,\text{nC}$ and $-1\,\text{nC}$ enclose $+2\,\text{nC}$.

![A closed surface containing +3.0 nC and −1.0 nC, with a +5.0 nC charge outside whose field line enters the surface and leaves again](figures/gauss_law/closed-surface-charges.svg "Only the charge inside counts. The outside charge's line enters (negative flux) and leaves (positive flux): net zero.")

Mehak is right about one thing: the field *at each point* of the box does depend on where the case sits and on the phone outside. What doesn't change is the **total** flux, added up over the whole closed surface. Gauss's law is about that total.

The law follows from Coulomb's inverse-square law. For a point charge $q$ at the centre of a sphere of radius $r$, $E = \dfrac{q}{4\pi\varepsilon_0 r^2}$ everywhere on it, the sphere's area is $4\pi r^2$, and the product is $q/\varepsilon_0$, with $r$ cancelling out.

## Worked example

**Given (illustrative):** the earbuds case carries $q = +8.85\,\text{nC}$ (chosen so the numbers divide neatly), with $\varepsilon_0 = 8.85 \times 10^{-12}\,\text{C}^2/\text{N m}^2$. Siddharth's phone, carrying $-3.0\,\text{nC}$, lies outside the box.
**Find:** the net flux through the box's wrapping.

**Step 1 — what's enclosed?** Only the case: $q_\text{enc} = +8.85 \times 10^{-9}\,\text{C}$. The phone is outside, so it doesn't count.

**Step 2 — apply Gauss's law.**
$$\Phi = \frac{8.85 \times 10^{-9}}{8.85 \times 10^{-12}} = 1000\,\text{N m}^2/\text{C}$$
Positive, so more field leaves the box than enters it.

**Step 3 — reverse it.** This is Siddharth's trick: measure a net outward flux of $1000\,\text{N m}^2/\text{C}$ over the whole wrapping, multiply by $\varepsilon_0$, and you know $8.85\,\text{nC}$ is inside, without opening the box.

**Sanity check:** put the gift in a box twice as big and the answer stays $1000\,\text{N m}^2/\text{C}$, because the same charge is enclosed.

## Where the picture breaks

No real field meter measures flux over a whole closed surface at once; you would have to measure $\vec{E}$ at a great many points on the wrapping and add up $\vec{E} \cdot d\vec{S}$ over them all. Siddharth's boast is true in principle, not a practical trick. And the earbuds case is not an isolated charge for long: charge leaks through damp air and the cardboard over hours. Gauss's law holds at every instant, for whatever charge is inside at that moment.

## Key takeaway

Gauss's law: the net electric flux through any closed surface equals the enclosed charge divided by $\varepsilon_0$, $\oint \vec{E} \cdot d\vec{S} = q_\text{enc}/\varepsilon_0$. Charges outside add zero net flux, and the shape, size and position of charges inside don't change the total; only the algebraic sum of the enclosed charge does.
