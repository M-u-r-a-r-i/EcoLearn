---
concept_id: refraction_spherical_surface
interest: gaming
format: explain
title: The arcade button whose label floats above the plastic
check:
  question: |-
    A long acrylic rod ($n = 1.5$) in air has a domed end of radius of curvature $8.0\,\text{cm}$, bulging towards the incoming light. A small lamp on the axis sits $40\,\text{cm}$ in front of the dome. Measured from the pole, where is the image?
  options:
    A: |-
      $27\,\text{cm}$ inside the acrylic
    B: |-
      $40\,\text{cm}$ inside the acrylic
    C: |-
      $17\,\text{cm}$ inside the acrylic
    D: |-
      $8.0\,\text{cm}$ inside the acrylic
  answer: B
  explanation: |-
    $\dfrac{n_2}{v} = \dfrac{n_2 - n_1}{R} + \dfrac{n_1}{u} = \dfrac{0.5}{8.0} + \dfrac{1}{-40} = 0.0625 - 0.025 = 0.0375\,\text{cm}^{-1}$, so $v = 1.5 \div 0.0375 = +40\,\text{cm}$: a real image $40\,\text{cm}$ inside the rod.
  misconceptions:
    A: |-
      Leaves $n_2$ off the left-hand side and writes $1/v = 0.0375$, giving $27\,\text{cm}$. The refractive index of the medium the light ends up in always sits on top of $v$ — that is the whole point of the formula.
    C: |-
      Substitutes $u = +40\,\text{cm}$. A real object sits on the side the light comes from, which is against the direction of travel, so $u$ is always negative for it.
    D: |-
      Assumes the rays are focused at the centre of curvature. The centre of curvature only fixes the direction of the normal at each point; where the image lands depends on both refractive indices as well.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk at night with a monitor, a coolant reservoir, a cut-away VR headset, a glass prism, a glowing optical cable, a hand lens over a controller board and a wall-mounted dome mirror](scenes/gaming/ray_optics.svg "Every lens on this desk is really just two curved surfaces back to back. Learn one surface and you have the lot.")

Arjun bought a dead arcade cabinet from a scrap dealer for the price of a month's data pack, and he is restoring it one part at a time. Tonight it is the button panel: six clear domed buttons, each with a paper legend and a tiny LED underneath.

He slots the first legend in, clips the dome on and looks down. The word on the paper is bigger than it was in his fingers — and it is not lying flat any more. It is **floating**, up near the top of the dome, as if the label had lifted off and was hanging inside the plastic.

He slides the button sideways. The floating word slides with it and stays floating. He prises the dome off: the paper is flat, the ink is flat, nothing has moved. He turns the dome upside down so the flat face is up, and the effect vanishes.

Only one thing changed: which way the plastic surface curves. A flat sheet shifts what you see a little. A curved one seems to pick the label up bodily and enlarge it. Where exactly has the light put that image, and can you work it out before you look?

## The physics

Strip the problem to its smallest piece: **one** curved boundary between two transparent media. Every lens in this chapter — the VR lens, a camera's front element, Arjun's dome — is built out of this piece.

Take a point object $O$ on the axis in a medium of index $n_1$, and a spherical surface of radius $R$ separating it from a medium $n_2$. Apply Snell's law at the surface to rays that stay close to the axis (**paraxial** rays) and the geometry collapses to one relation:

$$\frac{n_2}{v} - \frac{n_1}{u} = \frac{n_2 - n_1}{R}$$

![A point object in air sends two rays to the domed end of a glass rod; each bends towards the normal drawn through the centre of curvature, and the rays cross again inside the glass](figures/refraction_spherical_surface/single-spherical-surface.svg "Every distance is measured from the pole P, positive in the direction the light travels. The normal at the point of incidence always passes through the centre of curvature C.")

The sign convention is the same **Cartesian** one used for mirrors, and it must not be mixed up:

- all distances are measured from the **pole** $P$, where the surface crosses the axis;
- distances measured **along** the direction the light travels are positive, against it negative — so a real object on the incoming side always gives $u < 0$;
- $R$ is positive when the centre of curvature $C$ lies on the outgoing side, which is the case for a surface bulging towards the incoming light.

Two things are worth pausing on. First, $n_2$ sits above $v$ and $n_1$ above $u$: each index belongs to the side its own ray is on. Second, there is no focal length here. A single surface has no matching pair of foci, because the medium differs on the two sides; its bending power is the single term $(n_2 - n_1)/R$. The relation holds only for paraxial rays, one surface at a time, and a uniform medium on each side.

For Arjun's button the printed legend is very close to the dome, and the image comes out **virtual**: on the same side as the paper, raised and magnified. That is the floating word. Move the object far enough away and the same dome makes a **real** image inside the plastic instead.

## Worked example

**Given:** a long acrylic light pipe of index $n_2 = 1.5$, standing in air ($n_1 = 1$), with a domed end of radius $R = +5.0\,\text{cm}$ bulging towards the incoming light. A small lamp sits on the axis, $20\,\text{cm}$ in front of the dome.
**Find:** where the image forms.

**Step 1 — the surface's own bending power.**

$$\frac{n_2 - n_1}{R} = \frac{0.5}{5.0} = 0.10\,\text{cm}^{-1}$$

Nothing about the lamp is in this number yet; it belongs to the dome alone.

**Step 2 — bring in the lamp.** Light travels left to right, so $u = -20\,\text{cm}$ and $\dfrac{n_1}{u} = -0.05\,\text{cm}^{-1}$. Then

$$\frac{1.5}{v} = 0.10 - 0.05 = 0.05\,\text{cm}^{-1} \quad\Rightarrow\quad v = \frac{1.5}{0.05} = +30\,\text{cm}$$

**Step 3 — read it.** $v$ is positive, so the image is real and lies $30\,\text{cm}$ **inside** the acrylic — about the length of a keyboard, measured into the rod from the dome.

**Sanity check:** if the lamp were infinitely far away the same dome would focus the light at $n_2 R/(n_2 - n_1) = 15\,\text{cm}$ in. A nearby object must give an image *further* in than that, and $30\,\text{cm}$ is further. It fits.

## Where the picture breaks

The button is not one surface but two: light leaves the ink, crosses the flat underside, then the dome. This formula handles one surface at a time, and doing the button properly means applying it twice, using the first image as the object for the second. That is exactly how the lens formula is built in the next lesson, so nothing here is wasted — but a single-surface answer is not the whole story for a real lump of plastic.

The idealisation also assumes paraxial rays. Looking down at the button, your eye takes in wide-angle rays from near the rim of the dome, and those do not land where the formula says, which is why the edges of the floating word look soft and slightly stretched.

And a rod ends. If the calculation puts the image $30\,\text{cm}$ inside but the pipe is only $6\,\text{cm}$ long, the far surface gets there first and the light never reaches that point.

## Key takeaway

One curved boundary between two media obeys $n_2/v - n_1/u = (n_2 - n_1)/R$, with every distance measured from the pole and signed by the direction the light travels. The index of the medium each ray is in sits above its own distance. A single surface has no focal length — its bending power is the one term $(n_2 - n_1)/R$, and that term is the seed the whole lens formula grows from.
