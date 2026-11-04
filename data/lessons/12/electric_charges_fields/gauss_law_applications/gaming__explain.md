---
concept_id: gauss_law_applications
interest: gaming
format: explain
title: Why the graphics card travels in a silver bag
check:
  question: |-
    A thin spherical shell of radius $0.20\,\text{m}$ carries $+40\,\text{nC}$ spread uniformly over it. The field at $0.40\,\text{m}$ from its centre is $2250\,\text{N/C}$. What is the field at a point $0.10\,\text{m}$ from the centre?
  options:
    A: |-
      $36\,000\,\text{N/C}$, sixteen times bigger, since the field follows $1/r^2$
    B: |-
      $9000\,\text{N/C}$, the value the field has just outside the shell's surface
    C: |-
      Zero
    D: |-
      $2250\,\text{N/C}$, unchanged, since there is nothing inside to weaken it
  answer: C
  explanation: |-
    A sphere of radius $0.10\,\text{m}$ lies inside the shell and encloses no charge, so $E(4\pi r^2) = 0$ and, by the spherical symmetry, $E = 0$ everywhere inside.
  misconceptions:
    A: |-
      Uses $E = kQ/r^2$ inside as well, treating the shell as a point charge at the centre. That replacement is valid only *outside* the shell.
    B: |-
      Thinks the field inside is frozen at its surface value. At the charged surface the field jumps straight from $9000\,\text{N/C}$ to zero.
    D: |-
      Assumes the field just carries on unchanged into the empty interior, instead of being set by the charge enclosed by a surface drawn there.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night during a PC build: a monitor running a field sandbox with two charges, a plasma globe, an antistatic bag sparking to a fingertip, and an open PC case with a graphics card going in](scenes/gaming/electric_charges_fields.svg "The silver bag on the desk is the one thing in this picture that was designed around this chapter.")

Ira has sold her old graphics card to a friend three states away, and the two of them are arguing about packing it.

She has kept the silver-grey bag the card came in, folded in a drawer for two years. Her younger brother thinks this is ridiculous. "It's a plastic bag," he says, holding it up to the light. "A shiny one. Bubble wrap is what stops it breaking."

Ira remembers the technician at school clipping his wrist strap on before he would even open a case, and taking the card out of exactly this kind of bag. "It's not for the bumps," she says. "It's a shield."

Her brother is unconvinced, and honestly so is she. A bag is a bag. If someone walks across a carpet nearby and builds up a few thousand volts on themselves, how can a thin closed wrapper decide what happens to the space *inside* it?

## The physics

Gauss's law, $\oint \vec{E} \cdot d\vec{S} = q_\text{enc}/\varepsilon_0$, is true for every closed surface — but it hands you the *field* only when symmetry guarantees that $\vec{E}$ has the same size everywhere the flux crosses your surface, and is perpendicular to it. Then the integral collapses to $E \times \text{area}$. The whole skill is **choosing a Gaussian surface that matches the symmetry**.

![Three Gaussian surfaces: a cylinder around a long charged wire, a small box straddling an infinite charged sheet, and spheres drawn inside and outside a thin charged spherical shell](figures/gauss_law_applications/three-gaussian-surfaces.svg "Each dashed surface is picked so that E is the same size and perpendicular wherever flux crosses it. On the cylinder's flat ends and the box's sides, E runs along the surface and contributes nothing.")

**1. A long straight wire** with uniform linear charge density $\lambda$ (C/m). By symmetry $\vec{E}$ points radially outwards (for $\lambda > 0$). Take a coaxial cylinder of radius $r$ and length $l$: the flat ends catch no flux, the curved side has area $2\pi r l$, and the charge inside is $\lambda l$:

$$E(2\pi r l) = \frac{\lambda l}{\varepsilon_0} \quad\Rightarrow\quad E = \frac{\lambda}{2\pi\varepsilon_0 r}$$

Note the $1/r$ — a line of charge spreads its field over a cylinder, not a sphere, so it falls off more slowly than a point charge's.

**2. An infinite plane sheet** with uniform surface charge density $\sigma$ (C/m²). By symmetry $\vec{E}$ is perpendicular to the sheet on both sides. Take a small box straddling it with faces of area $A$; only those two faces catch flux, and the box encloses $\sigma A$:

$$2EA = \frac{\sigma A}{\varepsilon_0} \quad\Rightarrow\quad E = \frac{\sigma}{2\varepsilon_0}$$

There is no $r$ in it at all: the field does not weaken with distance, because the lines stay parallel and never spread.

**3. A thin spherical shell** of radius $R$ carrying $Q$ spread uniformly. Use a concentric sphere of radius $r$, on which the field is radial and everywhere the same size.

- **Outside** ($r > R$): the sphere encloses all of $Q$, so $E(4\pi r^2) = Q/\varepsilon_0$, giving $E = \dfrac{Q}{4\pi\varepsilon_0 r^2}$ — exactly as if the whole charge sat at the centre.
- **Inside** ($r < R$): the sphere encloses nothing, so $E(4\pi r^2) = 0$, giving $E = 0$.

The inside result needs the symmetry as much as the law. Zero flux on its own would only say that inward and outward contributions cancel; it is the spherical symmetry — radial field, same size all round — that forces $E$ itself to vanish.

These wire and sheet results assume a truly infinite wire and sheet. For real ones they hold well at points much closer to the object than to its ends or edges.

## Worked example

**Given (illustrative):** a thin shell of radius $R = 0.20\,\text{m}$ carrying $Q = +40\,\text{nC}$, with $\dfrac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\,\text{N m}^2/\text{C}^2$.
**Find:** the field at $0.10\,\text{m}$ and at $0.30\,\text{m}$ from the centre.

**Step 1 — inside, at $r = 0.10\,\text{m}$.** This sphere is inside the shell, so it encloses no charge:

$$E = 0$$

Not "small". Exactly zero, anywhere in the interior.

**Step 2 — outside, at $r = 0.30\,\text{m}$.** Here the sphere encloses all $40\,\text{nC}$, and the shell behaves like a point charge at the centre:

$$E = \frac{9.0 \times 10^9 \times 40 \times 10^{-9}}{(0.30)^2} = \frac{360}{0.090} = 4.0 \times 10^{3}\,\text{N/C}$$

![A graph of field strength against distance for a thin charged shell: zero out to 0.20 m, jumping to 9000 N/C at the surface, then falling as one over r squared, passing 4000 N/C at 0.30 m](figures/gauss_law_applications/shell-e-vs-r.svg "Inside the shell the field is flat zero; outside it falls like a point charge's. The jump happens at the charged surface itself.")

**Sanity check:** move out to $0.60\,\text{m}$, twice as far, and the field should fall to a quarter — $1000\,\text{N/C}$, which is what $360/0.36$ gives. The inverse-square behaviour outside is intact.

## Where the picture breaks

A shielding bag is not a thin, uniformly charged sphere, and the person scuffing across the carpet nearby is not a charge at rest. A real bag works because its conducting layer is a **closed conductor**: charges in it rearrange themselves to cancel any outside field in the space within. That full argument belongs to the next chapter, on conductors — as does the reason a metal car or aircraft is a good place to be in a thunderstorm.

What the shell result proves exactly is the seed of the idea: charge spread evenly over a closed sphere makes no field at all anywhere inside it. The wire and the sheet, meanwhile, are idealisations no real object quite meets — every real wire has ends, and every real sheet has edges.

## Key takeaway

Pick a Gaussian surface that matches the symmetry and Gauss's law becomes a one-line calculation. A long wire gives $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$, falling as $1/r$; an infinite sheet gives $E = \dfrac{\sigma}{2\varepsilon_0}$ at every distance; a thin shell gives $E = \dfrac{Q}{4\pi\varepsilon_0 r^2}$ outside and exactly zero inside.
