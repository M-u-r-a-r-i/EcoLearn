---
concept_id: thin_lenses
interest: football
format: explain
title: The set-piece diagram that lands upside down on the clubhouse wall
check:
  question: |-
    A biconvex lens is ground from glass of refractive index $1.5$, and both of its faces have a radius of curvature of $30\,\text{cm}$. What is its focal length?
  options:
    A: |-
      $15\,\text{cm}$
    B: |-
      $30\,\text{cm}$
    C: |-
      $60\,\text{cm}$
    D: |-
      Infinite — the two curved faces cancel and the lens does not focus
  answer: B
  explanation: |-
    For a biconvex lens $R_1 = +30\,\text{cm}$ and $R_2 = -30\,\text{cm}$, so $\dfrac{1}{f} = (1.5-1)\left(\dfrac{1}{30} - \dfrac{1}{-30}\right) = 0.5 \times \dfrac{2}{30} = \dfrac{1}{30}$, giving $f = +30\,\text{cm}$.
  misconceptions:
    A: |-
      Drops the $(n - 1)$ factor. The glass only bends light because its index differs from the surrounding air, and $(n-1)$ is exactly that difference — halving the power here.
    C: |-
      Counts only one surface. A lens has two refracting surfaces and both bend the light the same way for a biconvex shape, so their contributions add.
    D: |-
      Takes both radii as $+30\,\text{cm}$. The two centres of curvature lie on opposite sides of a biconvex lens, so $R_1$ and $R_2$ must carry opposite signs.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground in afternoon sun with a convex dome mirror on a post at the tunnel mouth, a broadcast camera with a long lens, an optical-fibre cable, and a rainbow in the sprinkler spray](scenes/football/ray_optics.svg "The camera's long lens and the clubhouse projector are the same device pointed in opposite directions — one shrinks the pitch onto a sensor, the other blows a small picture up onto a wall.")

The Monday review has moved into the clubhouse because it is raining, and the coach, Aparna, is fighting with an ancient projector. She slides in the first transparency — the corner routine, four arrows and a curved run — and on the wall the whole thing appears upside down and back to front.

The squad enjoys this more than the corner routine. Aparna flips the sheet over, and the diagram comes up correctly.

Then she wheels the trolley back to make the picture bigger. It grows, and goes soft; she turns the ring on the front of the lens a little, and it snaps sharp again. Someone at the back asks the good question: the sheet is the same, the wall is the same, the bulb is the same. Only two distances changed, and one lump of glass. What decides where a sharp picture can appear at all?

## The physics

A **thin lens** is two refracting spherical surfaces close together. Apply the single-surface relation twice — once at each face, feeding the first image in as the object for the second — and everything collapses into two clean results.

First the lens itself. Its focal length depends only on the glass and the two curvatures, through the **lens maker's formula**:

$$\frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

valid for a thin lens in air, with paraxial rays.

![A biconvex lens on its axis: the centre of curvature of the first face lies to the right so R1 is positive, and that of the second lies to the left so R2 is negative](figures/thin_lenses/lens-maker-radii.svg "Signs first, always. For a biconvex lens the two centres of curvature sit on opposite sides, so R1 and R2 get opposite signs and their effects add.")

Then the imaging. For an object at $u$ and an image at $v$, both measured from the optical centre in the Cartesian convention:

$$\frac{1}{v} - \frac{1}{u} = \frac{1}{f}, \qquad m = \frac{h'}{h} = \frac{v}{u}$$

**Watch the differences from mirrors.** The mirror equation adds $1/u$; the lens equation subtracts it. Mirror magnification is $-v/u$; lens magnification is $+v/u$. And the signs mean the opposite things, because light goes *through* a lens: $v$ **positive** now means the image is on the far side, where the light really goes, so it is **real**. A negative $m$ still means inverted.

![Ray diagram for a convex lens with the object beyond twice the focal length: a ray parallel to the axis leaves through the far focus, a ray through the optical centre goes straight on, and they cross to form a real inverted image](figures/thin_lenses/convex-lens-ray-diagram.svg "Two rays are enough: parallel in, through the focus out; and straight through the centre. Where they cross, a screen will show a sharp picture.")

That is why Aparna's diagram lands inverted: a real image formed by a single convex lens is always inverted, so the transparency has to go in upside down. And moving the projector back changes $v$, which forces $u$ to change too if $f$ is fixed — that is what the focusing ring does, sliding the lens a few millimetres.

## Worked example

**Given:** the projector's lens is biconvex, made of glass with $n = 1.5$, with both faces of radius $20\,\text{cm}$. The transparency sits $25\,\text{cm}$ in front of it.
**Find:** the focal length, and where the wall must be for a sharp picture.

**Step 1 — the focal length, from the shape of the glass.** $R_1 = +20\,\text{cm}$, $R_2 = -20\,\text{cm}$:

$$\frac{1}{f} = 0.5 \times \left(\frac{1}{20} + \frac{1}{20}\right) = 0.5 \times 0.10 = 0.050\,\text{cm}^{-1} \quad\Rightarrow\quad f = +20\,\text{cm}$$

**Step 2 — where the image goes.** The transparency is in front of the lens, so $u = -25\,\text{cm}$:

$$\frac{1}{v} = \frac{1}{f} + \frac{1}{u} = 0.050 - 0.040 = 0.010\,\text{cm}^{-1} \quad\Rightarrow\quad v = +100\,\text{cm}$$

The wall has to be a metre beyond the lens — about two long strides.

**Step 3 — how big.**

$$m = \frac{v}{u} = \frac{100}{-25} = -4$$

Four times taller and inverted, so a $10\,\text{cm}$ arrow on the transparency becomes a $40\,\text{cm}$ arrow on the wall.

**Sanity check:** the transparency sits only a little outside the focus, and that is exactly the setting that throws a large image a long way off — which is why every projector's slide sits just past $f$.

## Where the picture breaks

"Thin" is doing real work in these formulas. The projector's lens is a centimetre or more thick, so the two surfaces are not at one point and the true focal length differs slightly from the calculation.

The formulas also assume paraxial rays and one wavelength. Neither holds for a projector: the wide cone of light softens the edges of the picture (spherical aberration), and because $n$ is slightly larger for violet than for red, the edges of the arrows carry faint colour fringes (chromatic aberration). Real lenses fight both with several glass elements, which is why a camera's long lens weighs what it does.

The football is scenery here. There is no analogy hidden in the pitch — the lesson is simply that the club's projector and the broadcast camera are the same physics.

## Key takeaway

A thin lens is two refracting surfaces in one: its focal length comes from $\dfrac{1}{f} = (n-1)\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right)$, and its imaging from $\dfrac{1}{v} - \dfrac{1}{u} = \dfrac{1}{f}$ with $m = v/u$. Positive $v$ means a real image on the far side, and a single convex lens's real image is always inverted. Note the sign differences from the mirror equation — they come from light passing through the glass instead of bouncing off it.
