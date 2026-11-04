---
concept_id: mirror_equation
interest: gaming
format: explain
title: The dome mirror that shrinks twelve gaming rigs to a postcard
check:
  question: |-
    A concave mirror has a focal length of $20\,\text{cm}$, so $f = -20\,\text{cm}$. A controller stands $30\,\text{cm}$ in front of it. Where is the image, and what is it like?
  options:
    A: |-
      $60\,\text{cm}$ behind the mirror, virtual and erect, twice the size
    B: |-
      $12\,\text{cm}$ in front of the mirror, real and inverted, $0.4$ times the size
    C: |-
      $60\,\text{cm}$ in front of the mirror, real and inverted, twice the size
    D: |-
      $60\,\text{cm}$ in front of the mirror, real and inverted, half the size
  answer: C
  explanation: |-
    With $u = -30\,\text{cm}$ and $f = -20\,\text{cm}$, $\dfrac{1}{v} = \dfrac{1}{f} - \dfrac{1}{u} = -\dfrac{1}{20} + \dfrac{1}{30} = -\dfrac{1}{60}$, so $v = -60\,\text{cm}$ — in front of the mirror, hence real. Then $m = -v/u = -(-60)/(-30) = -2$: inverted and twice as large.
  misconceptions:
    A: |-
      Treats a negative $v$ as "behind the mirror". In the Cartesian convention negative means *against* the incoming light, which is the side the object is on — so a negative $v$ is a real image out in front.
    B: |-
      Rearranges the mirror equation to $1/v = 1/f + 1/u$ instead of $1/f - 1/u$. The term $1/u$ has to be moved across the equals sign, and moving it changes its sign.
    D: |-
      Inverts the magnification ratio, using $m = -u/v$ instead of $m = -v/u$. Magnification is image distance over object distance, in that order.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk at night with a monitor, a coolant reservoir, a cut-away VR headset, a glass prism, a glowing optical cable, a hand lens over a controller board and a wall-mounted dome mirror](scenes/gaming/ray_optics.svg "Top right: the dome mirror on the wall. The whole room is inside it, and it never turns anything upside down.")

Ananya has a two-hour slot booked at the gaming café near the bus stand, and her match does not start for twenty minutes. She is bored, so she watches the big dome mirror bolted high on the wall behind the counter — the one the owner uses to see every rig at once.

Twelve machines, a queue at the counter, the ceiling fan, all of it is in there, squashed into a patch the size of a postcard. She waves. The small Ananya waves back, the right way up.

Then she tries something. She holds her controller out towards the dome and walks towards it, slowly, all the way until the controller nearly touches the glass. The reflection grows a little — but it never gets big, and it never, ever flips over.

She knows the café's streaming booth has a round magnifying mirror clamped by the webcam, and she knows that one *does* flip your face if you lean back far enough. Same shape of glass, opposite behaviour. And where is that tiny image anyway? It does not look like it is on the wall; it looks like it is floating just inside it.

## The physics

One equation answers both questions. For any spherical mirror the object distance $u$, the image distance $v$ and the focal length $f$ are linked by the **mirror equation**

$$\frac{1}{v} + \frac{1}{u} = \frac{1}{f}$$

with every distance measured from the pole in the **Cartesian sign convention** — light drawn travelling left to right, distances along the light positive, against it negative — and $f = R/2$. The size comes from the **linear magnification**

$$m = \frac{h'}{h} = -\frac{v}{u}$$

where $h$ is the object's height and $h'$ the image's. The signs carry the meaning. A negative $m$ means an **inverted** image, and for a mirror that also means a **real** one, formed where rays genuinely cross. A positive $m$ means an **erect, virtual** image, which is light that only appears to come from behind the glass. $|m| > 1$ enlarges, $|m| < 1$ shrinks.

![Two ray diagrams: a concave mirror with the object beyond C giving a real inverted smaller image, and a convex mirror giving a virtual erect smaller image behind the mirror](figures/mirror_equation/ray-diagrams-concave-convex.svg "Two standard rays fix the image: one parallel to the axis, one through the focus. Solid lines crossing means a real image; dashed extensions crossing means a virtual one.")

Now Ananya's dome. It is convex, so $f$ is **positive**, and here is the consequence: whatever positive number you feed in for the object distance, $1/v = 1/f - 1/u$ comes out positive and smaller than $1/f$. So $v$ is always positive — always behind the glass — and always less than $f$. The image is virtual, erect and diminished, every single time. There is no distance she could have walked to make it flip.

The booth's magnifying mirror is concave, $f$ is negative, and that mirror does have a switch: while the object is nearer than $|f|$ the image is virtual and erect, and once it goes past, the image turns real and inverted.

Both formulae assume paraxial rays and a thin, truly spherical mirror.

## Worked example

**Given:** the café's dome mirror is convex with a focal length of $50\,\text{cm}$, so $f = +50\,\text{cm}$. The nearest row of machines stands $2.0\,\text{m}$ in front of it, so $u = -200\,\text{cm}$.
**Find:** where the image of that row sits, and how big it is.

**Step 1 — the image distance.**

$$\frac{1}{v} = \frac{1}{f} - \frac{1}{u} = \frac{1}{50} + \frac{1}{200} = \frac{4 + 1}{200} = \frac{1}{40}$$

$$v = +40\,\text{cm}$$

Positive means behind the glass. The little picture of the row is floating about $40\,\text{cm}$ inside the wall — which is exactly why it does not look painted on the surface.

**Step 2 — the magnification.**

$$m = -\frac{v}{u} = -\frac{+40}{-200} = +0.20$$

Positive, so erect; $0.20$, so one-fifth of life size. A machine a metre tall becomes a smear about $20\,\text{cm}$ tall — roughly the height of a controller held upright.

**Sanity check:** a convex mirror's image is always closer to the glass than its focus, and $40\,\text{cm}$ is less than $50\,\text{cm}$. It fits.

## Where the picture breaks

A real security dome is usually not a piece of a sphere at all: they are shaped to widen the field of view still further, so the middle and the edges have different curvatures and the equation only roughly describes what Ananya sees. Even a truly spherical dome this wide breaks the paraxial condition badly at its rim, which is why the machines at the far edges of the reflection look stretched.

The equation also assumes a flat object at one distance. The café is a room several metres deep, so every part of it has its own $u$ and its own $v$, and what looks like one little picture is really a stack of images at slightly different depths.

And nothing here is a gaming analogy. A mirror does not "render" a scene the way a graphics card does; there is no frame, no refresh, no processing. The light simply arrives, reflects, and carries on.

## Key takeaway

For any spherical mirror, $1/v + 1/u = 1/f$ with $f = R/2$, and $m = -v/u$. Substitute every distance with its Cartesian sign and one calculation gives you position, size and nature together: negative $m$ means real and inverted, positive $m$ means virtual and erect. Because $f$ is positive for a convex mirror, its image is always virtual, erect and smaller — which is exactly what a security dome is for.
