---
concept_id: thin_lenses
interest: gaming
format: explain
title: How a VR viewer makes a screen four centimetres away look far away
check:
  question: |-
    A plano-convex lens is moulded from plastic with $n = 1.5$. Its curved face has a radius of curvature of $15\,\text{cm}$ and its other face is flat. What is its focal length in air?
  options:
    A: |-
      $15\,\text{cm}$
    B: |-
      $10\,\text{cm}$
    C: |-
      $30\,\text{cm}$
    D: |-
      $7.5\,\text{cm}$
  answer: C
  explanation: |-
    A flat face has $R = \infty$, so its term is zero: $\dfrac{1}{f} = (1.5 - 1)\left(\dfrac{1}{15} - 0\right) = \dfrac{1}{30}\,\text{cm}^{-1}$, giving $f = 30\,\text{cm}$. It comes out the same whichever way round the lens faces.
  misconceptions:
    A: |-
      Counts the flat face as though it were curved too, giving $(n-1)(1/15 + 1/15)$. A flat surface has an infinite radius of curvature, so $1/R = 0$ and it contributes nothing to the focal length.
    B: |-
      Uses $n$ in place of $(n - 1)$. What bends the light is how much *more* the lens slows light than its surroundings do — which is why the same lens is much weaker under water than in air.
    D: |-
      Carries the mirror rule $f = R/2$ across to a lens. Mirrors halve the radius; a lens does not, because its focal length depends on the refractive index as well as the shape.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk at night with a monitor, a coolant reservoir, a cut-away VR headset, a glass prism, a glowing optical cable, a hand lens over a controller board and a wall-mounted dome mirror](scenes/gaming/ray_optics.svg "The cut-away headset in the middle: a glowing panel, one fat lens, and an eye. That is the whole optical system.")

Ishita's cousin left a cheap VR viewer behind after Diwali — a plastic shell with a slot for a phone and two thick lenses like boiled sweets. Ishita, who is suspicious of anything costing less than a controller, decides it cannot possibly work.

She brings a phone to four centimetres from her eye: a blur of coloured dots. Everyone knows you cannot focus on something that close.

Then she slides the same phone into the viewer, where it sits about that same four centimetres away, and looks in. The screen is **sharp** — and it does not feel like a phone pressed to her face at all. It feels like a wide screen hanging across the room.

She pops a lens out, takes it into the sun and holds it over an old exam pad. The bright dot turns up with her hand a hand-span above the paper, and soon there is a brown pinprick and a smell of burning.

Two plastic discs turned an unfocusable blur into a screen across the room. What is it about their shape that decides all this?

## The physics

A **thin lens** is two spherical refracting surfaces close enough together that the material's thickness can be ignored. Apply the single-surface relation at the first face, treat its image as the object for the second, and the algebra collapses to the **lens maker's formula**:

$$\frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

![A biconvex lens with the centre of curvature of the first surface to its right and of the second surface to its left, so that R1 is positive and R2 negative](figures/thin_lenses/lens-maker-radii.svg "Signs come from the direction the light travels, not from which face looks more curved. For a biconvex lens the two terms add, which is what makes it converging.")

Here $n$ is the index of the lens material relative to its surroundings, $R_1$ belongs to the surface the light meets first and $R_2$ to the second, both signed by the usual **Cartesian** rule: light travelling left to right, distances along it positive, against it negative, measured from the optical centre. Tighter curves mean smaller $|R|$ and a **shorter** focal length; and the strength goes with $(n-1)$, not $n$.

Parallel rays leave the lens heading for the focus $F'$, a distance $f$ away. Sunlight is about as parallel as light gets, so the burnt dot on Ishita's exam pad sat exactly at the focal point — she measured $f$ with her hand without meaning to. For any other object, the same two rays fix the image:

![Ray diagram for a convex lens with the object beyond twice the focal length, giving a real inverted image between F and 2F on the far side](figures/thin_lenses/convex-lens-ray-diagram.svg "One ray parallel to the axis leaves through F′; one through the optical centre goes straight on. Where they cross is the image.")

$$\frac{1}{v} - \frac{1}{u} = \frac{1}{f}, \qquad m = \frac{v}{u}$$

A negative $m$ means an inverted image. Note the minus sign where the mirror equation has a plus: the image forms on the far side of a lens, the near side of a mirror.

Everything changes when the object comes **inside** the focal length. The rays leaving the lens still diverge, so they never cross, and the image is virtual, erect and magnified.

![A convex lens used as a magnifying glass, with the object inside the focal length and an enlarged upright virtual image behind it on the same side](figures/microscope/simple-magnifier.svg "The rays leaving the lens still spread apart. The eye traces them straight back and sees a large image on the same side as the object.")

That is the whole trick of the viewer: park the phone just inside $f$, and the eye is handed an image it can comfortably focus on. All of this assumes a thin lens, paraxial rays and a single wavelength.

## Worked example

**Given:** a viewer lens is biconvex plastic with $n = 1.5$, both faces moulded to a radius of $10\,\text{cm}$. The phone screen sits $8.0\,\text{cm}$ from it.
**Find:** the focal length, and where the eye sees the screen.

**Step 1 — the focal length.** The first face bulges towards the light, so $R_1 = +10\,\text{cm}$; the second curves the other way, $R_2 = -10\,\text{cm}$.

$$\frac{1}{f} = 0.5\left(\frac{1}{10} + \frac{1}{10}\right) = 0.10\,\text{cm}^{-1} \quad\Rightarrow\quad f = 10\,\text{cm}$$

**Step 2 — where the image goes.** With $u = -8.0\,\text{cm}$,

$$\frac{1}{v} = \frac{1}{10} + \frac{1}{-8.0} = \frac{4 - 5}{40} = -\frac{1}{40} \quad\Rightarrow\quad v = -40\,\text{cm}$$

Negative $v$ means the image is on the same side as the phone: virtual, $40\,\text{cm}$ away instead of $8\,\text{cm}$ — about arm's length.

**Step 3 — how big.** $m = v/u = (-40)/(-8.0) = +5$: erect, five times life size. A screen $6\,\text{cm}$ tall becomes an image $30\,\text{cm}$ tall, the height of a small monitor.

**Sanity check:** the phone sits inside the focal length ($8 < 10\,\text{cm}$), and that must give a virtual, erect, magnified image. It did.

## Where the picture breaks

Be careful what "bigger" means. The image is five times taller *and* five times further away, so the angle it fills in Ishita's field of view is barely changed. What the lens really buys her is **focus**: her eye cannot focus at $8\,\text{cm}$, but it can at $40\,\text{cm}$. The sense of a huge screen comes from that, and from the shell blocking out the room — not from the lens enlarging anything her eye could otherwise have seen.

The word "thin" is also doing real work: these moulded lenses are fat enough that their own thickness matters, and the simple formula starts to drift. And one refractive index means one colour — plastic bends violet a little more than red, so the edges of the view carry colour fringes. That is chromatic aberration, and dispersion will come back to it.

## Key takeaway

A thin lens is two refracting surfaces in sequence: $1/f = (n-1)(1/R_1 - 1/R_2)$ gives its focal length, and then $1/v - 1/u = 1/f$ with $m = v/u$ places and sizes any image. Tighter curves and a bigger $(n-1)$ both shorten $f$. Put the object inside $f$ and the image turns virtual, erect and magnified — which is how a screen a few centimetres from your eye becomes something you can actually look at.
