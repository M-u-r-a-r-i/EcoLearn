---
concept_id: refraction_spherical_surface
interest: football
format: explain
title: The whole pitch, upside down inside a glass ball
check:
  question: |-
    A small lamp stands on the axis in air, $40\,\text{cm}$ in front of the domed end of a long glass rod ($n = 1.5$). The dome bulges towards the lamp and has a radius of curvature of $10\,\text{cm}$. Where does the image form?
  options:
    A: |-
      $60\,\text{cm}$ inside the glass
    B: |-
      $40\,\text{cm}$ inside the glass
    C: |-
      $30\,\text{cm}$ inside the glass
    D: |-
      $20\,\text{cm}$ inside the glass
  answer: A
  explanation: |-
    With $u = -40\,\text{cm}$, $R = +10\,\text{cm}$: $\dfrac{1.5}{v} = \dfrac{0.5}{10} + \dfrac{1}{-40} = 0.050 - 0.025 = 0.025\,\text{cm}^{-1}$, so $v = +60\,\text{cm}$ — real, and inside the glass.
  misconceptions:
    B: |-
      Writes $1/v$ instead of $n_2/v$ and gets $v = 40\,\text{cm}$. The refractive index of the medium the light ends up in always sits above $v$, because that is the side the refracted ray is on.
    C: |-
      Uses the parallel-light result $v = n_2 R/(n_2 - n_1) = 30\,\text{cm}$, ignoring the object term. The lamp is $40\,\text{cm}$ away, not at infinity, so $n_1/u$ cannot be dropped.
    D: |-
      Takes $u = +40\,\text{cm}$. A real object always sits against the direction the light travels, so its distance is negative in the Cartesian convention.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground in afternoon sun with a convex dome mirror on a post at the tunnel mouth, a broadcast camera with a long lens, an optical-fibre cable, and a rainbow in the sprinkler spray](scenes/football/ray_optics.svg "The camera's lens is two curved glass surfaces back to back. This lesson does one of them.")

At a school tournament, the photographer Rhea sets a solid glass ball on the touchline paint, the size of a small orange, and crouches until her camera is level with it.

Yuvraj, waiting to come on, wanders over and looks. Inside the ball is the entire pitch: both goals, the halfway line, a defender mid-stretch — the whole scene squeezed into the glass. And every bit of it is **upside down**.

"That's just a bubble effect," he says. Rhea hands him a magnifying glass from her bag. Held close to the touchline paint, it makes the letters bigger and the right way up. Held at arm's length, the pitch flips over in it too.

Same glass, same light, two completely different pictures. Something has to decide which one you get — and it must be decidable before you look. Where does the curved glass actually put the image?

## The physics

Take the smallest possible piece of the problem: **one** curved boundary between two transparent media. Lenses, magnifiers, camera fronts, the glass ball — all of them are this piece, used twice or more.

Put a point object $O$ on the axis in a medium of index $n_1$, facing a spherical surface of radius $R$ with medium $n_2$ beyond it. Apply Snell's law at the surface to **paraxial** rays — rays close to the axis and nearly parallel to it — and the geometry collapses to one relation:

$$\frac{n_2}{v} - \frac{n_1}{u} = \frac{n_2 - n_1}{R}$$

![A point object in air sending two rays to the domed end of a glass rod; each bends towards the normal through the centre of curvature and they cross again on the axis inside the glass](figures/refraction_spherical_surface/single-spherical-surface.svg "The normal at any point of the surface passes through the centre of curvature C. Every distance — u, v and R — is measured from the pole P.")

The sign convention is the Cartesian one you already used for mirrors:

- all distances are measured from the **pole** $P$, where the surface crosses the axis;
- distances measured along the direction the light travels are positive, against it negative — a real object on the left therefore has $u < 0$;
- $R$ is positive when the centre of curvature lies on the outgoing side, which it does for a surface bulging towards the incoming light.

Two features are worth pausing on. Each refractive index sits above the distance on its own side of the surface: $n_2$ over $v$, $n_1$ over $u$. And there is **no focal length** here — a single surface has different media on its two sides, so it has no matching pair of foci. Its bending power is the whole right-hand side, $(n_2 - n_1)/R$.

For Yuvraj's magnifying glass held close to the paint, the object term wins and the image comes out virtual, enlarged and upright. For the ball on the touchline the pitch is far away, the surface term wins, and the image is real and inverted. Same glass, and the formula tells you which, before you look.

The relation holds for paraxial rays, one surface at a time, and one uniform medium on each side.

## Worked example

**Given:** the glass ball has $n_2 = 1.5$ and a radius of curvature $R = +5.0\,\text{cm}$ at its front surface. A corner flag stands on the axis in air ($n_1 = 1$), $20\,\text{cm}$ in front of it.
**Find:** where the front surface alone forms the image.

**Step 1 — the surface's own bending term.**

$$\frac{n_2 - n_1}{R} = \frac{0.5}{5.0} = 0.10\,\text{cm}^{-1}$$

This is everything the glass contributes; nothing about the flag has entered yet.

**Step 2 — the object's term.** The flag is in front, so $u = -20\,\text{cm}$ and

$$\frac{n_1}{u} = \frac{1}{-20} = -0.050\,\text{cm}^{-1}$$

**Step 3 — put them together.**

$$\frac{1.5}{v} = 0.10 - 0.050 = 0.050\,\text{cm}^{-1} \quad\Rightarrow\quad v = +30\,\text{cm}$$

Positive, so the image is real and lies $30\,\text{cm}$ beyond the front of the glass, measured along the direction the light is going.

**Sanity check:** the surface's bending term is twice the size of the object's, so the surface wins and the light really does converge — a real image on the far side is the right kind of answer.

## Where the picture breaks

The ball is not one surface but two, and the answer above ignores the second. Thirty centimetres is far beyond the ball itself, so in reality the light never gets there: the back surface refracts it first and pulls the image in to just behind the glass, which is where Rhea's camera focuses. Doing that properly means applying the same formula twice, using the first image as the object for the second — and that is exactly how the thin-lens equation is built in the next lesson, so nothing here is wasted.

The paraxial assumption is also being stretched. Your eye takes in wide rays from near the rim of the ball, and those cross at a slightly different place, which is why the edge of the little upside-down pitch looks soft and stretched.

Football is the setting here, not an analogy: a glass ball happens to be a lovely photographer's toy, and the physics in it is the physics of any curved glass surface.

## Key takeaway

A single curved boundary obeys $\dfrac{n_2}{v} - \dfrac{n_1}{u} = \dfrac{n_2 - n_1}{R}$, with every distance measured from the pole and signed by the direction the light travels, and each index sitting above the distance on its own side. There is no focal length for one surface; its bending power is $(n_2 - n_1)/R$. Whether the image comes out real and inverted or virtual and upright is decided by which term wins.
