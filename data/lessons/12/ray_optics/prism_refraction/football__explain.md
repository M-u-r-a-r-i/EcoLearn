---
concept_id: prism_refraction
interest: football
format: explain
title: The glass wedge that fell out of the scout's binoculars
check:
  question: |-
    A prism of refracting angle $60^\circ$ is found to give a minimum deviation of $30^\circ$. At that setting, what is the angle of incidence at the first face?
  options:
    A: |-
      $15^\circ$
    B: |-
      $30^\circ$
    C: |-
      $60^\circ$
    D: |-
      $45^\circ$
  answer: D
  explanation: |-
    At minimum deviation the ray passes symmetrically, so $i = e$ and $\delta_m = i + e - A = 2i - A$. Hence $i = \dfrac{A + \delta_m}{2} = \dfrac{60 + 30}{2} = 45^\circ$.
  misconceptions:
    A: |-
      Halves the deviation alone. The prism angle belongs in the relation too: it is $\dfrac{A + \delta_m}{2}$, not $\dfrac{\delta_m}{2}$.
    B: |-
      Assumes the angle of incidence equals the deviation. They are different angles measured from different lines — the deviation is between the incoming and outgoing rays, not between a ray and a normal.
    C: |-
      Assumes the angle of incidence equals the refracting angle of the prism. What equals $A$ at minimum deviation is $r_1 + r_2$, the two angles *inside* the glass.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground in afternoon sun with a convex dome mirror on a post at the tunnel mouth, a broadcast camera with a long lens, an optical-fibre cable, and a rainbow in the sprinkler spray](scenes/football/ray_optics.svg "The sunbeam crossing the pitch is about to meet a wedge of glass — and a wedge treats light quite differently from a flat window.")

Rukmini scouts for a district youth side, and she watches from the top of the stand with a pair of binoculars older than she is. Midway through the second half one barrel starts to rattle. At the final whistle she unscrews the end plate, and a small wedge of glass drops into her palm: a triangular block, clear as water.

She holds it up between her eye and the far goal. The goal jumps sideways — the whole goalmouth shifted off its posts, as if someone had picked it up and moved it two metres along the line.

Then she rolls the wedge slowly between her fingers. The shift changes as she turns it. It shrinks, reaches a smallest value where the goal sits nearest its true place, and then grows again as she keeps turning.

A flat window would have done none of this. Why should turning a wedge of glass have a *least* setting at all?

## The physics

A **prism** is a block with two flat faces meeting at an angle $A$, the **refracting angle**. Light refracts on the way in and again on the way out, and because the faces are tilted with respect to each other, the two bends do not cancel — they add up to a net turn called the **angle of deviation** $\delta$.

![A ray passing through a triangular prism: it enters at angle i, travels inside at r1 and r2, leaves at e, and the extensions of the incoming and outgoing rays meet at the angle of deviation](figures/prism_refraction/prism-deviation.svg "Four angles and two relations. The geometry of the triangle gives A = r1 + r2, and the deviation is what the ray has turned through in total.")

Two relations come straight from the geometry of the triangle:

$$A = r_1 + r_2, \qquad \delta = i + e - A$$

and Snell's law holds at each face, $\sin i = n \sin r_1$ and $n \sin r_2 = \sin e$ for a prism in air.

Now turn the prism, as Rukmini did, and plot $\delta$ against $i$:

![A graph of the angle of deviation against the angle of incidence for an equilateral prism, falling to a shallow minimum and rising again](figures/prism_refraction/deviation-vs-incidence.svg "The curve has one minimum, and it is flat there — which is why the prism has a setting you can find by eye, and why the measurement is a reliable one.")

The curve falls, bottoms out, and rises. The minimum is not an accident of the glass: light paths are reversible, so any deviation other than the smallest one can be produced by **two** different angles of incidence — one where the ray tilts one way inside the prism, one the other. Those two solutions can only merge at one place, the symmetric path, where

$$i = e, \qquad r_1 = r_2 = \frac{A}{2}$$

and the ray inside runs parallel to the base. There, $\delta_m = 2i - A$, so $i = \dfrac{A + \delta_m}{2}$, and Snell's law at the first face gives the **prism formula**:

$$n = \frac{\sin\!\left(\dfrac{A + \delta_m}{2}\right)}{\sin\!\left(\dfrac{A}{2}\right)}$$

This is the standard laboratory method for measuring a refractive index, and it is accurate precisely because the curve is flat at the bottom: a small error in aiming the prism barely changes $\delta_m$.

## Worked example

**Given:** an equilateral glass prism, so $A = 60^\circ$, set at minimum deviation, where $\delta_m$ is measured as $30^\circ$.
**Find:** the refractive index of the glass.

**Step 1 — the angle of incidence at that setting.**

$$i = \frac{A + \delta_m}{2} = \frac{60^\circ + 30^\circ}{2} = 45^\circ$$

**Step 2 — the angle inside the glass.** The path is symmetric, so

$$r_1 = \frac{A}{2} = 30^\circ$$

**Step 3 — Snell's law at the first face.**

$$n = \frac{\sin 45^\circ}{\sin 30^\circ} = \frac{0.707}{0.500} = 1.41$$

**Sanity check:** $1.41$ is a believable value for glass — above water's $1.33$, near the $1.5$ of ordinary window glass — and any $n$ below $1$ would have been impossible.

## Where the picture breaks

One prism, one number: the formula assumes a single wavelength. Rukmini's wedge deviates violet light slightly more than red, so the edge of the goalmouth she sees is fringed with colour, and a careful measurement has to say which colour of light was used. That is the whole subject of the next lesson.

The relations also assume the ray goes through both faces. Tilt the prism far enough and the light meets the second face beyond the critical angle, is totally internally reflected, and never emerges — which is not a failure but the trick the rest of her binoculars rely on.

The football here is setting, not analogy. A ball deflected off a defender's shin and then off a post turns twice, like the ray, but the resemblance stops there: the ball's deflections depend on speed and spin, while the ray's depend only on angles and $n$.

## Key takeaway

For a prism, $A = r_1 + r_2$ and $\delta = i + e - A$. As the prism is turned, the deviation passes through a single minimum, reached on the symmetric path where $i = e$ and $r_1 = r_2 = A/2$. That setting gives the standard way of measuring a refractive index: $n = \sin\!\left(\frac{A + \delta_m}{2}\right) \big/ \sin\!\left(\frac{A}{2}\right)$.
