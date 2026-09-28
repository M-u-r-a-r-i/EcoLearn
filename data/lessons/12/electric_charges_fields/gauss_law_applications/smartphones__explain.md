---
concept_id: gauss_law_applications
interest: smartphones
format: explain
title: The charging cable that collects dust from far away
check:
  question: |-
    A long, straight, uniformly charged cable produces a field of $1800\,\text{N/C}$ at a distance of $10\,\text{cm}$ from it (far from its ends). What is the field at $30\,\text{cm}$ from the cable?
  options:
    A: |-
      $200\,\text{N/C}$
    B: |-
      $1800\,\text{N/C}$
    C: |-
      $600\,\text{N/C}$
    D: |-
      $5400\,\text{N/C}$
  answer: C
  explanation: |-
    For a long line of charge, Gauss's law with a coaxial cylinder gives $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$, so $E \propto 1/r$. Three times as far away, the field is a third as strong: $1800/3 = 600\,\text{N/C}$.
  misconceptions:
    A: |-
      Uses the point-charge rule $E \propto 1/r^2$. A line of charge spreads its field over a cylinder, whose area grows only as $r$, so the field falls as $1/r$.
    B: |-
      Uses the infinite-sheet result, where the field doesn't depend on distance. That holds for a flat plane of charge, not a line.
    D: |-
      Inverts the relation, as if the field grew with distance from the cable. Moving away from a charge always weakens its field.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a sunny window with a solar power bank on the sill, an opened phone box with foam beads clinging to the new phone, a film being peeled off a screen with dust jumping up to it, and a phone on a stand running a field-line app](scenes/smartphones/electric_charges_fields.svg "The dust leaping up in the middle is reacting to a charged flat film. Flat sheets, long cables and round shells each make a differently shaped field.")

Anika's phone charging cable is two metres long, and it spends its nights dragged across the bedroom carpet. One dry winter morning she lifts it and finds it furry with lint and dust along its whole length.

She runs an experiment. She rubs the cable's plastic sleeve with a woollen scarf, lays it straight on the table, and sprinkles fine talcum powder nearby. Specks jump to the cable from surprisingly far away, much farther than they jumped to a single rubbed foam bead she tried last week.

Her brother Dhruv suggests a reason. "The bead is a point. The cable is a line of charges. Lots of them."

"But most of those charges are far away along the cable," says Anika. "They should barely count."

Both have a point. For a single charge, the field dies away as $1/r^2$. Does a long line of charge fade the same way, or more slowly? And what about a flat charged screen?

## The physics

Gauss's law, $\oint \vec{E} \cdot d\vec{S} = q_\text{enc}/\varepsilon_0$, holds for every closed surface, but it gives you the **field** only when symmetry tells you that $\vec{E}$ has the same size wherever it crosses your surface, and crosses it at right angles. Then the integral becomes simply $E \times \text{area}$. The skill is **choosing a Gaussian surface that matches the symmetry**.

![Three Gaussian surfaces: a cylinder around a long charged wire, a small box straddling an infinite charged sheet, and spheres drawn inside and outside a thin charged spherical shell](figures/gauss_law_applications/three-gaussian-surfaces.svg "Each dashed surface is chosen so E is the same size and perpendicular wherever flux crosses it. On the cylinder's flat ends and the box's sides, E runs along the surface and adds no flux.")

**1. Long straight wire**, uniform **linear charge density** $\lambda$ (C/m). By symmetry $\vec{E}$ points radially out from the wire (for $\lambda > 0$). Take a coaxial cylinder of radius $r$ and length $l$. The flat ends catch no flux; the curved side has area $2\pi r l$ and encloses charge $\lambda l$:
$$E(2\pi r l) = \frac{\lambda l}{\varepsilon_0} \quad\Rightarrow\quad E = \frac{\lambda}{2\pi\varepsilon_0 r}$$
The field falls as $1/r$, more slowly than a point charge's, because a line's field spreads over a cylinder, not a sphere. That is why Anika's cable reaches farther than the bead.

**2. Infinite plane sheet**, uniform **surface charge density** $\sigma$ (C/m²). By symmetry $\vec{E}$ is perpendicular to the sheet on both sides. A small box across the sheet, with end faces of area $A$, catches flux only through those two faces and encloses $\sigma A$:
$$2EA = \frac{\sigma A}{\varepsilon_0} \quad\Rightarrow\quad E = \frac{\sigma}{2\varepsilon_0}$$
There is no $r$: near a large flat sheet the field does not weaken with distance.

**3. Thin spherical shell**, radius $R$, total charge $Q$ spread uniformly. Take a concentric sphere of radius $r$:
- **Outside** ($r > R$): it encloses $Q$, so $E(4\pi r^2) = Q/\varepsilon_0$ and $E = \dfrac{Q}{4\pi\varepsilon_0 r^2}$, as if all the charge sat at the centre.
- **Inside** ($r < R$): it encloses nothing, and by the spherical symmetry $E = 0$ everywhere inside.

The wire and sheet results assume they are infinitely long and wide. For real ones they hold well at distances much smaller than the distance to their ends or edges.

## Worked example

**Given (illustrative):** the rubbed cable carries $\lambda = 10\,\text{nC/m}$; a freshly wiped flat screen carries $\sigma = 17.7\,\text{nC/m}^2$. Use $\dfrac{1}{2\pi\varepsilon_0} = 1.8 \times 10^{10}\,\text{N m}^2/\text{C}^2$ and $\varepsilon_0 = 8.85 \times 10^{-12}\,\text{C}^2/\text{N m}^2$.
**Find:** the cable's field at $10\,\text{cm}$ and $20\,\text{cm}$, and the screen's field just above it.

**Step 1 — cable at 10 cm.**
$$E = \frac{1.8 \times 10^{10} \times 10 \times 10^{-9}}{0.10} = \frac{180}{0.10} = 1800\,\text{N/C}$$

**Step 2 — cable at 20 cm.** Twice as far, so half as strong: $900\,\text{N/C}$. A point charge would have dropped to a quarter.

**Step 3 — the screen.**
$$E = \frac{\sigma}{2\varepsilon_0} = \frac{17.7 \times 10^{-9}}{2 \times 8.85 \times 10^{-12}} = 1000\,\text{N/C}$$
The same at $1\,\text{mm}$ and at $1\,\text{cm}$ above it, as long as you stay close compared with the screen's width.

**Sanity check:** closer to the cable the field must grow, and at $5\,\text{cm}$ it is $3600\,\text{N/C}$, double the $10\,\text{cm}$ value, as $1/r$ requires.

## Where the picture breaks

A cable is not infinitely long and its charge is not spread perfectly evenly: rubbing leaves patches. Within a few centimetres of its middle, far from the plugs, the $1/r$ result is a good guide; near the ends, or a metre away, it is not. A phone screen is only a few centimetres wide, so it acts like an infinite sheet only within a millimetre or so of its surface. And the powder moves because its specks are polarised by the field, so how far it jumps also depends on the field's non-uniformity and on each speck's weight, not just on $E$.

## Key takeaway

Choose a Gaussian surface that matches the symmetry and Gauss's law gives the field in one line. A long wire: $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$, falling as $1/r$. An infinite sheet: $E = \dfrac{\sigma}{2\varepsilon_0}$, the same at every distance. A thin shell: $E = \dfrac{Q}{4\pi\varepsilon_0 r^2}$ outside and exactly zero inside.
