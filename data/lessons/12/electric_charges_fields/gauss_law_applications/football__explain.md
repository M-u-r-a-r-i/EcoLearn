---
concept_id: gauss_law_applications
interest: football
format: explain
title: Three charged objects, three different reaches
check:
  question: |-
    A thin hollow sphere of radius $0.10\,\text{m}$ carries a positive charge spread uniformly over its surface. Where is the electric field strongest?
  options:
    A: |-
      At the centre, where the contributions from all round the sphere meet.
    B: |-
      Halfway out to the surface, closer to the charge than the centre is.
    C: |-
      Nowhere in particular — the field has the same strength everywhere, inside and outside, because the charge is spread uniformly.
    D: |-
      Just outside the surface; everywhere inside the shell the field is exactly zero.
  answer: D
  explanation: |-
    A concentric Gaussian sphere drawn anywhere inside encloses no charge, so $E = 0$ throughout the cavity. Outside, $E = Q/(4\pi\varepsilon_0 r^2)$, which is largest at the smallest possible $r$ — just outside the surface.
  misconceptions:
    A: |-
      Treats the shell as focusing its field on the centre. The contributions from opposite sides point in opposite directions and cancel, and Gauss's law shows the cancellation is exact everywhere inside, not just at the centre.
    B: |-
      Assumes that being nearer the charge always means a stronger field. Inside the shell you are nearer to one part of it and further from the rest, and the two effects cancel exactly at every interior point.
    C: |-
      Confuses a uniform *charge distribution* with a uniform *field*. A uniform spread of charge is what makes the field zero inside and fall as $1/r^2$ outside; it is only an infinite flat sheet whose field is the same at every distance.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit ground as a storm arrives: lightning above the stand, rain falling, a player peeling off a crackling nylon bib, and two players heading for the metal-roofed dugout](scenes/football/electric_charges_fields.svg "After the storm the ground is empty, the air is dry, and everything left out on the grass rubs up a charge.")

The storm has passed and the pitch is empty except for Tanvi, Anand and a cardboard box of physics-club junk. Their detector is a strip of foil on a thread taped to a bamboo cane: bring it near anything charged and it leans.

They rub three things with the same nylon cloth, the same number of strokes each. The long polypropylene rope that marks out the training pitch, pulled tight down one side. The big flat plastic sheet they use to cover the goalmouth. And a football.

Anand's bet is simple. More charge means more reach, so the rope should win.

They test. Two steps back from the ball, the foil hangs dead straight. Two steps back from the rope, it still twitches. Two steps back from the sheet, it leans over exactly as far as it did at arm's length — no fading at all.

Same cloth, same strokes, three completely different fall-offs. Tanvi keeps walking backwards from the sheet, waiting for it to weaken, and it refuses. Why should the *shape* of a charged object decide how fast its field dies away?

## The physics

Gauss's law, $\oint \vec{E} \cdot d\vec{S} = q_\text{enc}/\varepsilon_0$, is true for every closed surface — but it hands you the *field* only when symmetry guarantees that $\vec{E}$ has the same size everywhere flux crosses your surface and is perpendicular to it. Then the integral collapses to $E \times \text{area}$. So the whole skill is choosing a **Gaussian surface that matches the symmetry of the charge**.

![Three Gaussian surfaces: a cylinder around a long wire, a small box straddling an infinite sheet, and spheres inside and outside a thin shell](figures/gauss_law_applications/three-gaussian-surfaces.svg "Each dashed surface is picked so that E is the same size and perpendicular wherever flux crosses. On the cylinder's flat ends and the box's sides, E runs along the surface and contributes nothing.")

**1. A long straight wire** with uniform linear charge density $\lambda$ (C/m). Symmetry makes $\vec{E}$ radial. Wrap it in a coaxial cylinder of radius $r$ and length $l$: the flat ends catch no flux, the curved side has area $2\pi r l$, and the charge inside is $\lambda l$.

$$E(2\pi r l) = \frac{\lambda l}{\varepsilon_0} \quad\Rightarrow\quad E = \frac{\lambda}{2\pi\varepsilon_0 r}$$

The field falls as $1/r$, because the lines spread over a cylinder, which grows only with $r$.

**2. An infinite plane sheet** with uniform surface charge density $\sigma$ (C/m²). Symmetry makes $\vec{E}$ perpendicular to the sheet on both sides. Straddle it with a small box whose two faces have area $A$; only those faces catch flux, and the box encloses $\sigma A$.

$$2EA = \frac{\sigma A}{\varepsilon_0} \quad\Rightarrow\quad E = \frac{\sigma}{2\varepsilon_0}$$

No $r$ survives. The lines never spread out at all, so the field is the same at every distance — which is Tanvi's stubborn sheet.

**3. A thin spherical shell** of radius $R$ carrying $Q$ spread evenly. Use a concentric sphere of radius $r$; the field is radial with one size all over it.

- **Outside** ($r > R$): the sphere encloses $Q$, so $E(4\pi r^2) = Q/\varepsilon_0$ and $E = \dfrac{Q}{4\pi\varepsilon_0 r^2}$, exactly as if all of $Q$ sat at the centre.
- **Inside** ($r < R$): no charge is enclosed, so $E = 0$ everywhere in the cavity.

Zero flux on its own would only say that inward and outward contributions cancel; it is the spherical symmetry that forces $E$ itself to vanish.

![Field of a thin charged shell against distance: zero out to the shell's radius, jumping at the surface and then falling as one over r squared](figures/gauss_law_applications/shell-e-vs-r.svg "Drawn for a shell of radius 0.20 m carrying 40 nC. Inside, the field is exactly zero; outside, it falls like a point charge's, so the strongest field of all is just outside the surface.")

The wire and sheet results assume a truly infinite wire and sheet; for real ones they hold well close to the object and far from its ends or edges.

## Worked example

**Given (illustrative):** the rope carries $\lambda = 100\,\text{nC/m}$ along its length. Take $\dfrac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\,\text{N m}^2/\text{C}^2$.
**Find:** the field $0.20\,\text{m}$ from the rope, and then $0.60\,\text{m}$ from it.

**Step 1 — the constant part of the formula.** Since $\dfrac{\lambda}{2\pi\varepsilon_0} = 2 \times (9.0 \times 10^9) \times \lambda$:

$$2 \times 9.0 \times 10^9 \times 1.0 \times 10^{-7} = 1800\,\text{N m/C}$$

Everything about the rope is now in one number; only the distance is left to vary.

**Step 2 — at $0.20\,\text{m}$.**

$$E = \frac{1800}{0.20} = 9.0 \times 10^{3}\,\text{N/C}$$

**Step 3 — at $0.60\,\text{m}$.** Three times further out:

$$E = \frac{1800}{0.60} = 3.0 \times 10^{3}\,\text{N/C}$$

A third of the field, not a ninth. Had the sheet been charged this way instead, the reading would have been identical at both distances; had it been the ball, it would have dropped to a ninth.

**Sanity check:** dry air only breaks down and sparks at around $3 \times 10^{6}\,\text{N/C}$, so a few thousand N/C is the right size for something that tugs a foil strip and does nothing more dramatic.

## Where the picture breaks

None of the three objects is the ideal in the textbook. A training rope is a few tens of metres long, so the $1/r$ law holds only near its middle; a goalmouth cover is finite, so step far enough back and its field does eventually fade, as the edges start to matter. The rubbed charge on a plastic rope is also patchy rather than uniform, and it leaks away into damp air over minutes. The football is the weakest fit of all: a leather ball is an insulator, so rubbing leaves charge stuck where you put it rather than spread evenly, and only an even spread gives $E = 0$ inside. The measurements are real; the clean formulas belong to idealised shapes.

## Key takeaway

Match the Gaussian surface to the symmetry and Gauss's law becomes a one-line calculation. A long wire gives $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$, falling as $1/r$; an infinite sheet gives $E = \dfrac{\sigma}{2\varepsilon_0}$ at every distance; a thin shell gives $E = \dfrac{Q}{4\pi\varepsilon_0 r^2}$ outside and exactly zero inside. The geometry of the charge, not its amount, decides how fast the field dies away.
