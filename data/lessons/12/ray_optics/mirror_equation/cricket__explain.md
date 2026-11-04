---
concept_id: mirror_equation
interest: cricket
format: explain
title: The ball that turns upside down in the dressing-room mirror
check:
  question: |-
    The convex mirror on the side of the team bus has a focal length of $+30\,\text{cm}$. A kit bag stands $60\,\text{cm}$ from it. What is the magnification of its image?
  options:
    A: |-
      $-\dfrac{1}{3}$
    B: |-
      $+3$
    C: |-
      $+\dfrac{1}{3}$
    D: |-
      $-3$
  answer: C
  explanation: |-
    With $u = -60\,\text{cm}$ and $f = +30\,\text{cm}$, the mirror equation gives $1/v = 1/30 + 1/60 = 1/20$, so $v = +20\,\text{cm}$. Then $m = -v/u = -(+20)/(-60) = +1/3$: erect, virtual and one-third the size — which is what every convex mirror does.
  misconceptions:
    A: |-
      Gets the size right but leaves the image inverted. A convex mirror always forms a virtual, erect image, so $m$ must be positive; the minus sign here comes from forgetting that $u$ is itself negative.
    B: |-
      Inverts the ratio, using $m = -u/v$ instead of $m = -v/u$. Magnification is image distance over object distance.
    D: |-
      Both errors: the ratio inverted and the sign wrong. A convex mirror cannot magnify.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A sunlit cricket ground with the sun's rays, a broadcast camera with a long lens, a stump camera, a fielder in curved sunglasses, and a small rainbow in the sprinkler spray](scenes/cricket/ray_optics.svg "Every curved surface here forms an image — the camera lens, the sunglasses, even the stump camera's tiny window.")

Kavya, the reserve wicketkeeper, is waiting for the rain to stop. To pass the time she holds a cricket ball in front of the round shaving mirror above the dressing-room basin — the one that curves inwards — and slowly walks backwards with it.

Up close, the ball in the mirror is huge and the right way up; she can see every stitch on the seam. She keeps stepping back. Halfway across the room the reflection smears into a blur so wide she can't tell what it is. Two steps further back and the ball is there again — but small, and hanging **upside down**.

She checks the ball in her hand. Still the right way up, obviously. She steps forward and back twice more, and the reflection flips each time, at the same place in the room.

A flat mirror never does this. Why should moving a ball backwards turn its reflection over — and why does the flip always happen at that one spot?

## The physics

For a spherical mirror, the object distance $u$, the image distance $v$ and the focal length $f$ are tied together by the **mirror equation**

$$\frac{1}{v} + \frac{1}{u} = \frac{1}{f}$$

with every distance measured from the pole under the Cartesian sign convention, and $f = R/2$. The size of the image comes from the **linear magnification**

$$m = \frac{h'}{h} = -\frac{v}{u}$$

where $h$ is the object's height and $h'$ the image's. The signs carry the meaning: $m$ negative means an **inverted** image (which for a mirror is a real one, formed by rays that actually cross), $m$ positive means an **erect, virtual** image behind the glass. $|m| > 1$ magnifies, $|m| < 1$ shrinks.

![Two ray diagrams: a concave mirror with the object beyond C giving a real inverted smaller image, and a convex mirror giving a virtual erect smaller image behind the mirror](figures/mirror_equation/ray-diagrams-concave-convex.svg "Two standard rays fix the image: one parallel to the axis, one through the focus. Where they cross is the image; where their dashed extensions cross is a virtual image.")

Now Kavya's mirror. It is concave, so $f$ is negative. While the ball is nearer than the focus, the mirror cannot make the rays converge; they still spread as they leave, and the reflection is a magnified, erect, virtual image behind the glass — the "every stitch" view. When the ball is exactly at the focus, the reflected rays come out parallel and form no image at all: that is her blur. Past the focus, the rays do cross, and the image is real and inverted — the upside-down ball.

That is the answer to her question: the flip happens at the focus, and it happens at the same spot every time because $f$ belongs to the mirror, not to the ball.

Both formulae assume paraxial rays and a thin, truly spherical mirror.

## Worked example

**Given:** the dressing-room mirror is concave with a radius of curvature of $40\,\text{cm}$, so $f = -20\,\text{cm}$. Kavya holds the ball $60\,\text{cm}$ in front of it, so $u = -60\,\text{cm}$.
**Find:** where the image is, and how big.

**Step 1 — the image distance.** Rearranging the mirror equation,

$$\frac{1}{v} = \frac{1}{f} - \frac{1}{u} = \frac{1}{-20} - \frac{1}{-60} = \frac{-3 + 1}{60} = \frac{-2}{60}$$

$$v = -30\,\text{cm}$$

Negative means in *front* of the mirror: the image floats in the air $30\,\text{cm}$ out, about a hand-span from the glass, between Kavya and the mirror.

**Step 2 — the magnification.**

$$m = -\frac{v}{u} = -\frac{-30}{-60} = -0.5$$

The minus sign says inverted; the $0.5$ says half size. So the ball's reflection is a real image, upside down, and about as wide as a golf ball.

**Sanity check:** the object is beyond the centre of curvature ($60 > 40\,\text{cm}$), and that always gives a real, inverted, diminished image — exactly what came out.

## Where the picture breaks

A real shaving mirror is not perfectly spherical and its aperture is wide, so rays from the edge focus slightly closer than paraxial rays — the image Kavya sees is a little softer than the equation promises. The equation also assumes a point-by-point image of a flat object; a cricket ball is a sphere, so different parts of it are at different distances and the reflection is subtly distorted. And the cricket here is scenery: a ball reflected in a mirror behaves like any other object. Don't push it — there is no useful analogy between a ball bouncing off a bat and light bouncing off a mirror, because the ball's direction depends on its spin and on how much it squashes, and light's does not.

## Key takeaway

For any spherical mirror, $1/v + 1/u = 1/f$ with $f = R/2$, and $m = -v/u$. Put in every distance with its sign and the equation tells you the position, the size and the nature of the image in one go: a negative $m$ means real and inverted, a positive $m$ means virtual and erect. For a concave mirror the object crossing the focus is what flips the image over.
