---
concept_id: refraction_spherical_surface
interest: cricket
format: explain
title: The scorer's glass paperweight lifts the numbers off the page
check:
  question: |-
    A parallel beam of light travelling along the axis in air falls on the domed end of a long glass rod ($n = 1.5$). The dome has a radius of curvature of $20\,\text{cm}$ and bulges towards the light. How far inside the glass does the beam come to a focus?
  options:
    A: |-
      $60\,\text{cm}$
    B: |-
      $40\,\text{cm}$
    C: |-
      $20\,\text{cm}$
    D: |-
      $10\,\text{cm}$
  answer: A
  explanation: |-
    With $u \to \infty$ the term $n_1/u$ vanishes, so $n_2/v = (n_2 - n_1)/R$, giving $v = n_2 R/(n_2 - n_1) = (1.5)(20)/0.5 = 60\,\text{cm}$ inside the glass.
  misconceptions:
    B: |-
      Uses the thin-lens habit $1/v = (n-1)/R$ and forgets that the image forms *inside* the glass, so the left-hand side is $n_2/v$, not $1/v$. The refractive index of the medium the light ends up in always sits on top of $v$.
    C: |-
      Assumes rays are focused at the centre of curvature. That is true for light heading straight at the centre of a mirror, not for refraction at a surface — here the centre of curvature only fixes the direction of the normal.
    D: |-
      Carries the mirror rule $f = R/2$ across to a refracting surface. Mirrors halve the radius; a refracting surface does not, because the answer depends on both refractive indices.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A sunlit cricket ground with the sun's rays, a broadcast camera with a long lens, a stump camera, a fielder in curved sunglasses, and a small rainbow in the sprinkler spray](scenes/cricket/ray_optics.svg "Every lens in this picture is really just two curved surfaces. Learn one surface and you have the lot.")

Meera has been given the scorebook for the afternoon, and a breeze keeps lifting the pages. The scorer hands her a solid glass paperweight — a heavy half-ball, flat underneath, domed on top — and she drops it on the open page.

The overs column jumps at her. The neat printed figures under the dome look bigger, and stranger than that, they look like they are floating just under the glass surface, not lying on the paper at all. She slides the paperweight sideways. The numbers slide with it and stay floating.

She checks with a finger: the paper has not moved, the ink has not moved. She turns the paperweight over so the flat face is up. The magic stops — the figures look ordinary again.

Only one thing changed: which way the glass surface curves. A flat surface of glass shifts what you see a little. A curved one seems to move the page bodily upwards and make it bigger. Where exactly has the light put that image, and can it be predicted before you look?

## The physics

Strip the problem down to its smallest piece: **one** curved boundary between two transparent media. Everything else in this chapter — lenses, magnifiers, the front element of a camera — is built from this piece.

Take a point object $O$ on the axis, in a medium of refractive index $n_1$, and a spherical surface of radius $R$ separating it from a medium $n_2$. Apply Snell's law at the surface to rays that stay close to the axis (**paraxial** rays) and the geometry collapses into one relation:

$$\frac{n_2}{v} - \frac{n_1}{u} = \frac{n_2 - n_1}{R}$$

![A point object in air sends two rays to the domed end of a glass rod; each bends towards the normal drawn through the centre of curvature, and the rays cross again inside the glass](figures/refraction_spherical_surface/single-spherical-surface.svg "Every distance is measured from the pole P, positive in the direction the light travels. The normal at the point of incidence always passes through the centre of curvature C.")

The sign convention is the same Cartesian one you used for mirrors, and you must not mix it up:

- all distances are measured from the **pole** $P$, the point where the surface meets the axis;
- distances measured **along** the direction the light travels are positive, against it negative — so a real object on the left always gives $u < 0$;
- $R$ is positive when the centre of curvature $C$ lies on the outgoing side, as it does for a surface bulging towards the incoming light.

Two things are worth noticing. First, $n_2$ sits on top of $v$ and $n_1$ on top of $u$: each index belongs to the side its ray is on. Second, there is no focal length here. A single surface has no symmetric pair of foci, because the medium is different on the two sides.

The relation holds only for paraxial rays, for a single surface, and for one uniform medium on each side.

For Meera's paperweight the object (the printed ink) is almost touching the glass, so the image comes out **virtual** — on the same side as the page, raised and magnified. That is what she is seeing. Put the object far enough away and the same surface makes a **real** image inside the glass instead.

## Worked example

**Given:** a long glass rod, $n_2 = 1.5$, with a domed end of radius $R = +4.0\,\text{cm}$. A small lamp sits on the axis in air ($n_1 = 1$), $40\,\text{cm}$ in front of the dome.
**Find:** where the image forms.

**Step 1 — the signs.** Light travels left to right, so $u = -40\,\text{cm}$. The dome bulges towards the lamp, which puts $C$ inside the glass, on the outgoing side: $R = +4.0\,\text{cm}$.

**Step 2 — the surface's own term.**

$$\frac{n_2 - n_1}{R} = \frac{0.5}{4.0} = 0.125\,\text{cm}^{-1}$$

This is the whole bending power of the surface: nothing about the lamp is in it yet.

**Step 3 — add the object.** $\dfrac{n_1}{u} = \dfrac{1}{-40} = -0.025\,\text{cm}^{-1}$, so

$$\frac{1.5}{v} = 0.125 - 0.025 = 0.100\,\text{cm}^{-1} \quad\Rightarrow\quad v = 15\,\text{cm}$$

$v$ is positive, so the image is real and lies $15\,\text{cm}$ **inside** the glass — about the length of a bat's handle grip into the rod.

**Sanity check:** a converging surface should pull a far object's image in close, and $15\,\text{cm}$ is much shorter than the $40\,\text{cm}$ the lamp stands away — the right size, and on the right side.

## Where the picture breaks

The paperweight is not one surface but two: light leaves the ink, crosses the flat bottom face, then the dome. Our formula handles one at a time, and to do the paperweight properly you would apply it twice, using the first image as the object for the second. That is exactly how the lens formula is built in the next lesson — so nothing here is wasted, but the single-surface answer alone is not the full story for a real lump of glass.

The idealisation also assumes paraxial rays. Meera's eye takes in wide-angle rays from near the rim of the dome, and those focus slightly differently, which is why the edges of the magnified figures look soft and a little distorted. And a rod, of course, ends: if the calculation puts the image $15\,\text{cm}$ in but the glass is only $5\,\text{cm}$ long, the second surface gets there first and the light never reaches that point.

## Key takeaway

One curved boundary between two media obeys $n_2/v - n_1/u = (n_2 - n_1)/R$, with every distance measured from the pole and signed by the direction the light travels. The index of the medium each ray is in sits above its own distance. A single surface has no focal length — its bending power is $(n_2 - n_1)/R$, and that one term is the seed from which the whole lens formula grows.
