---
concept_id: spherical_mirrors
interest: football
format: explain
title: The bulging mirror at the tunnel mouth
check:
  question: |-
    A convex mirror on a stadium corridor wall has a focal length of $15\,\text{cm}$ in size. Written with the Cartesian sign convention, what are its focal length and radius of curvature?
  options:
    A: |-
      $f = +15\,\text{cm}$, $R = +30\,\text{cm}$
    B: |-
      $f = -15\,\text{cm}$, $R = -30\,\text{cm}$
    C: |-
      $f = +15\,\text{cm}$, $R = +7.5\,\text{cm}$
    D: |-
      $f = +30\,\text{cm}$, $R = +15\,\text{cm}$
  answer: A
  explanation: |-
    A convex mirror's focus and centre of curvature lie behind the glass, on the far side from the incoming light, so both distances are positive. The centre of curvature is twice as far out as the focus, since $f = R/2$.
  misconceptions:
    B: |-
      Assumes every mirror distance is negative because "the object distance always is". The sign comes from which side of the pole the point lies on, and for a convex mirror both $F$ and $C$ are behind the mirror.
    C: |-
      Inverts the relation to $R = f/2$. The focus is the halfway point, so the radius is the *larger* of the two.
    D: |-
      Swaps the two quantities. $f = R/2$ means the focal length is half the radius, never twice it.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground in afternoon sun with a convex dome mirror on a post at the tunnel mouth, a broadcast camera with a long lens, an optical-fibre cable, and a rainbow in the sprinkler spray](scenes/football/ray_optics.svg "Four curved surfaces in one picture: the dome mirror, the camera's lens, the fibre and the water drops. Start with the easiest one — the mirror.")

Devika plays left-back and she is late. She sprints up the corridor towards the tunnel with her boots in one hand, and stops dead: in the big round mirror bolted above the tunnel mouth she can see the entire corridor behind her — the kit trolley, two coaches, the physio's door, all of it shrunk into something the size of a saucer.

Ten minutes earlier, in the equipment room, she had watched the groundsman unscrew the back of a hand lamp. Inside was a little silver bowl, caved inwards, with the bulb sitting in the middle of it. Everything reflected in that bowl was upside down and huge.

Both are curved mirrors. One swallows a whole corridor, the other blows up a fingertip. The only difference she can see is which way the silver bends. How can that decide so much?

## The physics

A **spherical mirror** is a small slice of a hollow sphere, silvered on one side. If the reflecting side is the caved-in one, the mirror is **concave** — the lamp's bowl. If it is the bulging one, the mirror is **convex** — the tunnel dome.

Four words describe any spherical mirror:

- the **pole** $P$ — the middle of the mirror's surface;
- the **centre of curvature** $C$ — the centre of the sphere the mirror was cut from;
- the **radius of curvature** $R$ — the distance $PC$;
- the **principal axis** — the line through $P$ and $C$.

Send in rays that run parallel to the principal axis and stay close to it. A concave mirror reflects them so they genuinely meet at a point; a convex mirror throws them outwards so they only *seem* to spread from a point behind the glass. Either way that point is the **principal focus** $F$, and it lies halfway from the pole to the centre of curvature:

$$f = \frac{R}{2}$$

![Two panels: a concave mirror reflecting parallel rays through a real focus in front of it, and a convex mirror reflecting the same rays so that they appear to come from a focus behind it](figures/spherical_mirrors/concave-convex-focus.svg "Same rays in, opposite results out. In both cases the focus sits halfway between the pole and the centre of curvature.")

This is true only for **paraxial rays** — rays close to the axis and nearly parallel to it. Rays hitting the rim of a wide mirror cross a little nearer the glass, which is why a large curved mirror never gives a perfectly crisp picture.

To stop signs turning into guesswork, optics fixes them once with the **Cartesian sign convention**: measure every distance from the pole, always draw the light travelling left to right, count distances measured along the incoming light as positive and against it as negative, and heights above the axis as positive.

![A diagram of the Cartesian sign convention: the pole is the origin, distances to the left are negative and to the right positive, heights above the axis positive and below negative](figures/spherical_mirrors/cartesian-sign-convention.svg "Everything starts at the pole. A real object always sits in front of the mirror, so u comes out negative every time.")

So for a concave mirror $F$ and $C$ sit in front of the glass and $f$ and $R$ are **negative**; for a convex mirror they sit behind it and both are **positive**. That single sign is the whole difference between Devika's two mirrors.

## Worked example

**Given:** the tunnel dome is convex with a radius of curvature of $2.0\,\text{m}$; the lamp's bowl is concave with a radius of curvature of $6.0\,\text{cm}$.
**Find:** the focal length of each, with its sign.

**Step 1 — the tunnel dome.** It bulges outwards, so its centre of curvature is behind the wall, in the positive direction: $R = +2.0\,\text{m}$.

$$f = \frac{R}{2} = +1.0\,\text{m}$$

The focus sits a metre *inside the wall*, where nothing physical exists — which is exactly why the corridor's reflection is something you can never catch on a screen.

**Step 2 — the lamp's bowl.** It caves inwards, so $C$ is out in the room, in the negative direction: $R = -6.0\,\text{cm}$, and

$$f = \frac{-6.0}{2} = -3.0\,\text{cm}$$

The focus is $3\,\text{cm}$ out from the silver — about a thumb's length, right where the groundsman had screwed the bulb.

**Sanity check:** the mirror that caves away from you keeps its focus out where you stand, and the one that bulges towards you hides its focus behind the wall. The signs say precisely that.

## Where the picture breaks

Real corridor mirrors are often not spherical at all — many are shaped to widen the view further, and a truly spherical one that wide would blur badly at the rim, where the paraxial condition fails. The lamp reflector is usually a paraboloid for the same reason.

And football is the setting here, not an analogy. Nothing about a ball models light: a ball bouncing off a wall loses energy, and spin changes the angle it leaves at, while a light ray does neither. Reach for the geometry, not for the ball.

## Key takeaway

A spherical mirror is fixed by its pole, centre of curvature and focus, with $f = R/2$ for paraxial rays. Concave mirrors bring parallel light to a real focus in front; convex mirrors make it diverge from a virtual focus behind. In the Cartesian convention, measured from the pole, a concave mirror has $f$ and $R$ negative and a convex mirror has them positive.
