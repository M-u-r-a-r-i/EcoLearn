---
concept_id: gauss_law_applications
interest: cricket
format: explain
title: Why the coach sends everyone into the team bus
check:
  question: |-
    After the storm, Dev's physics teacher sets up three idealised charged objects: a very long, uniformly charged straight wire, a very large, uniformly charged flat sheet, and a thin, uniformly charged spherical shell. You measure the field at a distance $r$ from the wire, at a distance $r$ from the sheet, and at a distance $r$ from the centre of the shell (outside it). Then you double every distance to $2r$. By what factor does each field change, in that order (wire, sheet, shell)?
  options:
    A: |-
      $\tfrac{1}{2}$, unchanged, $\tfrac{1}{4}$
    B: |-
      $\tfrac{1}{4}$, $\tfrac{1}{4}$, $\tfrac{1}{4}$
    C: |-
      $\tfrac{1}{2}$, $\tfrac{1}{2}$, $\tfrac{1}{4}$
    D: |-
      $\tfrac{1}{4}$, unchanged, $\tfrac{1}{4}$
  answer: A
  explanation: |-
    Gauss's law gives $E = \lambda/(2\pi\varepsilon_0 r)$ for the wire (halves), $E = \sigma/(2\varepsilon_0)$ for the sheet (independent of distance) and $E = Q/(4\pi\varepsilon_0 r^2)$ outside the shell (a quarter).
  misconceptions:
    B: |-
      Treats every charged object as a point charge with an inverse-square field. Only the shell (outside) behaves like that; the wire's field falls as $1/r$ and the infinite sheet's doesn't fall at all.
    C: |-
      Assumes the sheet's field weakens with distance the way the wire's does. For an infinite sheet, the field lines stay parallel and never spread out, so $E = \sigma/(2\varepsilon_0)$ at every distance.
    D: |-
      Treats the long wire as a point charge. A line of charge spreads its field over a cylinder of area $2\pi r l$, not a sphere of area $4\pi r^2$, so its field falls only as $1/r$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A storm over a cricket ground: dark clouds, distant lightning, players walking off, groundstaff dragging a plastic cover and a team bus waiting](scenes/cricket/electric_charges_fields.svg "Players leave the field as the storm arrives. Notice the team bus waiting by the boundary.")

The under-19 side is playing an away game at a small ground outside town when the sky splits. A flash, and the thunder comes barely two seconds later. The umpires wave everyone off.

Most of the boys sprint for the big neem tree beside the scoreboard. Coach Fernandes blows her whistle, hard. "Not the tree! Everyone into the bus. Windows shut."

Dev, the opening batter, climbs aboard dripping and annoyed. "Ma'am, the bus is a big metal box. Doesn't metal *attract* lightning? Shouldn't we stay away from it?"

"Being inside a closed metal shell is one of the safest places in a storm," she says. "Ask your physics teacher why."

Dev stares at the steel roof above his seat as the rain hammers on it. If charge piles up on the outside of a closed shell, what does the electric field do in the space inside it?

## The physics

Gauss's law, $\oint \vec{E} \cdot d\vec{S} = q_\text{enc}/\varepsilon_0$, holds for every closed surface. But it gives you the *field* only when symmetry tells you that $\vec{E}$ has the same size everywhere the flux crosses your chosen surface and is perpendicular to it. Then the integral becomes simply $E \times \text{area}$. The trick is to choose a **Gaussian surface that matches the symmetry**.

![Three Gaussian surfaces: a cylinder around a long wire, a small box across an infinite sheet, and spheres inside and outside a thin shell](figures/gauss_law_applications/three-gaussian-surfaces.svg "Each dashed surface is chosen so that E is the same size and perpendicular wherever flux crosses it. On the cylinder's ends and the box's sides, E runs along the surface and gives no flux.")

**1. A long straight wire** with uniform linear charge density $\lambda$ (C/m). By symmetry, $\vec{E}$ points radially outwards (for $\lambda > 0$). Take a coaxial cylinder of radius $r$ and length $l$. The flat ends get no flux, because $\vec{E}$ runs along them. The curved side has area $2\pi r l$, and it encloses charge $\lambda l$:

$$E(2\pi r l) = \frac{\lambda l}{\varepsilon_0} \quad\Rightarrow\quad E = \frac{\lambda}{2\pi\varepsilon_0 r}$$

**2. An infinite plane sheet** with uniform surface charge density $\sigma$ (C/m²). By symmetry, $\vec{E}$ is perpendicular to the sheet, pointing away from it on both sides (for $\sigma > 0$). Take a small box (a "pillbox") straddling the sheet, with faces of area $A$. Only the two faces get flux, and the box encloses $\sigma A$:

$$2EA = \frac{\sigma A}{\varepsilon_0} \quad\Rightarrow\quad E = \frac{\sigma}{2\varepsilon_0}$$

The field doesn't depend on the distance from the sheet at all.

**3. A thin spherical shell** of radius $R$ carrying charge $Q$ spread uniformly. Use a concentric sphere of radius $r$; the field is radial and has the same size everywhere on it.

- **Outside** ($r > R$): the sphere encloses $Q$, so $E(4\pi r^2) = Q/\varepsilon_0$, giving $E = \dfrac{Q}{4\pi\varepsilon_0 r^2}$, as if all the charge were at the centre.
- **Inside** ($r < R$): the sphere encloses no charge, so $E(4\pi r^2) = 0$, giving $E = 0$.

The "inside" result needs the symmetry too. Zero flux alone only says that inward and outward flux cancel; it's the spherical symmetry (radial field, same size all round) that forces $E$ itself to be zero.

These results assume a truly infinite wire and sheet. For real ones, they hold well at points much closer to the object than to its ends or edges.

## Worked example

**Given (illustrative):** a thin shell with $R = 0.20\,\text{m}$ and $Q = +40\,\text{nC}$; a long wire with $\lambda = 2.0\,\text{nC/m}$; a large sheet with $\sigma = 8.85 \times 10^{-9}\,\text{C/m}^2$. Take $\dfrac{1}{4\pi\varepsilon_0} = 9.0 \times 10^9\,\text{N m}^2/\text{C}^2$.
**Find:** the shell's field at $0.10\,\text{m}$ and $0.30\,\text{m}$ from its centre; the wire's field at $0.10\,\text{m}$; the sheet's field.

**Shell.** At $r = 0.10\,\text{m}$ (inside): $E = 0$. At $r = 0.30\,\text{m}$ (outside):

$$E = \frac{9.0 \times 10^9 \times 40 \times 10^{-9}}{(0.30)^2} = \frac{360}{0.090} = 4.0 \times 10^{3}\,\text{N/C}$$

![Field of a thin shell against distance: zero inside up to 0.20 m, jumping to 9000 N/C at the surface and falling as 1 over r squared outside, with 4000 N/C at 0.30 m](figures/gauss_law_applications/shell-e-vs-r.svg "Inside the shell the field is exactly zero; outside it falls like a point charge's. The jump happens at the charged surface itself.")

**Wire.** Since $\dfrac{1}{2\pi\varepsilon_0} = 2 \times 9.0 \times 10^9$:

$$E = \frac{2 \times 9.0 \times 10^9 \times 2.0 \times 10^{-9}}{0.10} = \frac{36}{0.10} = 3.6 \times 10^{2}\,\text{N/C}$$

**Sheet.**

$$E = \frac{\sigma}{2\varepsilon_0} = \frac{8.85 \times 10^{-9}}{2 \times 8.85 \times 10^{-12}} = 5.0 \times 10^{2}\,\text{N/C}$$

at any distance from it.

**Sanity check:** double the distance and the shell's outside field falls to a quarter ($4000 \to 1000\,\text{N/C}$ at $0.60\,\text{m}$), the wire's to half ($180\,\text{N/C}$ at $0.20\,\text{m}$), and the sheet's stays at $500\,\text{N/C}$. Units: $\sigma/\varepsilon_0$ gives $(\text{C/m}^2)/(\text{C}^2\,\text{N}^{-1}\,\text{m}^{-2}) = \text{N/C}$. Correct.

## Where the picture breaks

A bus is not a thin, uniformly charged sphere, and a lightning strike is not charge at rest. The real protection comes from the metal body conducting the lightning current around the outside and down to the ground, and the full reason a closed metal shell screens its inside is part of the next chapter, on conductors. That's also why weather services list a hard-topped metal vehicle with windows shut as safe shelter, and a lone tree as one of the worst places to stand. What the thin-shell result does show exactly is the seed of the idea: charge spread evenly over a closed sphere produces no field anywhere inside it. The wire and sheet results, meanwhile, are idealisations that no real object meets exactly.

## Key takeaway

Choose a Gaussian surface that matches the symmetry, and Gauss's law turns into a one-line calculation. A long wire gives $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$; an infinite sheet gives $E = \dfrac{\sigma}{2\varepsilon_0}$ at every distance; a thin shell gives $E = \dfrac{Q}{4\pi\varepsilon_0 r^2}$ outside and $E = 0$ inside.
