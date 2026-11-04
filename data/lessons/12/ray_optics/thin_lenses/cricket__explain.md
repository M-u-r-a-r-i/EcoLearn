---
concept_id: thin_lenses
interest: cricket
format: explain
title: Two old spectacle lenses burn their dots at different heights
check:
  question: |-
    A biconvex lens is made of glass with $n = 1.5$. Both faces are ground to a radius of curvature of $20\,\text{cm}$. What is its focal length in air?
  options:
    A: |-
      $40\,\text{cm}$
    B: |-
      $20\,\text{cm}$
    C: |-
      $10\,\text{cm}$
    D: |-
      about $6.7\,\text{cm}$
  answer: B
  explanation: |-
    With $R_1 = +20\,\text{cm}$ and $R_2 = -20\,\text{cm}$, $1/f = (1.5-1)\left(\tfrac{1}{20} - \tfrac{1}{-20}\right) = 0.5 \times 0.10 = 0.05\,\text{cm}^{-1}$, so $f = 20\,\text{cm}$.
  misconceptions:
    A: |-
      Counts only one surface, $1/f = (n-1)/R$. Light is bent twice inside a lens, once on the way in and once on the way out, and both bends go into the focal length.
    C: |-
      Adds the two surface terms but forgets the factor $(n-1)$, as though the shape alone fixed the focal length. A lens made of a material with $n$ close to $1$ would barely bend light at all, whatever its shape.
    D: |-
      Uses $n$ in place of $(n-1)$. What matters is how much *more* the lens bends light than the surrounding medium does — which is why the same lens has a longer focal length under water.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A sunlit cricket ground with the sun's rays, a broadcast camera with a long lens, a stump camera, a fielder in curved sunglasses, and a small rainbow in the sprinkler spray](scenes/cricket/ray_optics.svg "The camera's long lens and the fielder's curved sunglasses are doing the same job with different amounts of curve.")

The covers are on, the rain has stopped, and there is nothing to do. Vikram finds the lost-property box in the pavilion and tips it out: two pairs of abandoned spectacles, one with thin lenses, one with lenses so thick they look like boiled sweets.

He takes the thin lens outside into the sun, holds it over the back cover of the old scorebook and hunts for the bright dot. It appears when his hand is nearly at arm's length from the cardboard, and after a minute there is a smell of scorching and a brown pinprick.

He swaps to the fat lens. This time the dot arrives with his hand barely a hand's span above the cover, and it is small and fierce and burns almost at once.

Both lenses are glass. Both are the same width across. The only visible difference is how strongly the surfaces bulge. So what exactly sets the height at which the dot appears — and once you know it, can you say where a lens will put the image of anything, not just the Sun?

## The physics

A **thin lens** is two spherical refracting surfaces close enough together that the thickness of the glass between them can be ignored. Apply the single-surface relation at the first face, treat its image as the object for the second face, and the algebra collapses to the **lens maker's formula**:

$$\frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

![A biconvex lens with the centre of curvature of the first surface to its right and of the second surface to its left, so that R1 is positive and R2 negative](figures/thin_lenses/lens-maker-radii.svg "Signs come from the direction the light travels, not from which face looks more curved. For a biconvex lens the two terms add, which is what makes it converging.")

Here $n$ is the index of the lens material relative to its surroundings, $R_1$ is the radius of the surface the light meets first and $R_2$ of the second, both signed by the usual Cartesian rule.

Two features of that formula answer Vikram's question directly. Tighter curvature means smaller $|R|$, larger $1/f$, **shorter** focal length — the fat lens. And the strength depends on $(n-1)$, not $n$: it is the *difference* between the lens and its surroundings that bends light, which is why a glass lens is much weaker in water than in air.

The focal length is defined by parallel light: rays arriving parallel to the axis leave the lens heading for the focus $F'$, at distance $f$. Sunlight is as close to parallel as you will get, so **the bright dot on the scorebook sits at the focal point**, and Vikram measured $f$ with his hand without realising it.

For any other object, the same two rays fix the image:

![Ray diagram for a convex lens with the object beyond twice the focal length, giving a real inverted image between F and 2F on the far side](figures/thin_lenses/convex-lens-ray-diagram.svg "One ray parallel to the axis leaves through F′; one through the optical centre goes straight on. Where they cross is the image.")

$$\frac{1}{v} - \frac{1}{u} = \frac{1}{f}, \qquad m = \frac{v}{u}$$

with the same sign convention as before, distances measured from the optical centre. A negative $m$ means the image is inverted. Note the minus sign in the lens equation, where the mirror equation has a plus — the difference comes from the image forming on the far side of a lens and on the near side of a mirror.

All of this assumes a thin lens, paraxial rays, and a single wavelength.

## Worked example

**Given:** a biconvex lens of glass with $n = 1.5$, each face ground to a radius of $20\,\text{cm}$.
**Find:** its focal length, and where it images a cricket ball held $30\,\text{cm}$ in front of it.

**Step 1 — the focal length.** Light meets the first face bulging towards it, so $R_1 = +20\,\text{cm}$; the second face curves the other way, so $R_2 = -20\,\text{cm}$.

$$\frac{1}{f} = 0.5\left(\frac{1}{20} + \frac{1}{20}\right) = 0.05\,\text{cm}^{-1} \quad\Rightarrow\quad f = 20\,\text{cm}$$

So parallel sunlight would burn its dot $20\,\text{cm}$ below the lens — a little less than the width of the wicket, which is $22.86\,\text{cm}$.

**Step 2 — the ball.** With $u = -30\,\text{cm}$,

$$\frac{1}{v} = \frac{1}{20} + \frac{1}{-30} = \frac{3 - 2}{60} = \frac{1}{60} \quad\Rightarrow\quad v = +60\,\text{cm}$$

A positive $v$ means a real image, $60\,\text{cm}$ beyond the lens, where you could catch it on a sheet of paper.

**Step 3 — how big.** $m = v/u = 60/(-30) = -2$: twice life size and upside down. A ball of about $7\,\text{cm}$ across would appear about $14\,\text{cm}$ across on the paper, seam pointing the wrong way.

**Sanity check:** the ball sits between $f$ and $2f$, so the image must be beyond $2f$ and magnified — and $60\,\text{cm}$ is beyond $2f = 40\,\text{cm}$. It fits.

## Where the picture breaks

The "thin" in thin lens is doing real work. Vikram's fat lens from the lost-property box is thick enough that its own glass thickness matters, and the simple formula starts to drift from the truth. Real optics uses a thick-lens version with the surfaces handled separately.

The lens maker's formula also assumes one refractive index — one colour. Glass bends violet a little more than red, so a single lens has a slightly shorter focal length for violet, and the burnt dot never sharpens to a perfect point. That is chromatic aberration, and you will meet it again in dispersion.

Finally, the cricket here is only the setting. A lens does not "collect" light the way a fielder collects a ball; nothing is being gathered and carried. Each ray is bent independently at the two surfaces, and they happen to arrive at the same point.

## Key takeaway

A thin lens is two refracting surfaces acting in sequence. Its focal length comes from the material and the two radii, $1/f = (n-1)(1/R_1 - 1/R_2)$, and once you have $f$ everything else follows from $1/v - 1/u = 1/f$ with $m = v/u$. Fatter curves and a bigger $(n-1)$ both mean a shorter focal length — a stronger lens.
