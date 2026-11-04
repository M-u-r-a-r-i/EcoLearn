---
concept_id: dispersion
interest: football
format: explain
title: The band of colour in the half-time sprinklers
check:
  question: |-
    A thin prism of refracting angle $6^\circ$ is made of glass with $n_\text{red} = 1.51$ and $n_\text{violet} = 1.53$. What is the angular dispersion between red and violet?
  options:
    A: |-
      $0.12^\circ$
    B: |-
      $3.12^\circ$
    C: |-
      $0.02^\circ$
    D: |-
      $6.24^\circ$
  answer: A
  explanation: |-
    Angular dispersion is the difference of the two deviations: $(n_V - n_R)A = (1.53 - 1.51) \times 6^\circ = 0.02 \times 6^\circ = 0.12^\circ$.
  misconceptions:
    B: |-
      Calculates the mean deviation $(n - 1)A$ with $n = 1.52$ instead of the *spread* between the colours. Deviation is how far the whole beam turns; dispersion is how far apart its ends land.
    C: |-
      Stops at $n_V - n_R$ and calls it an angle. That difference is a pure number; it only becomes an angle after multiplying by the prism's refracting angle.
    D: |-
      Adds the two deviations, $3.18^\circ + 3.06^\circ$, instead of subtracting them. Dispersion is the gap between where violet and red arrive.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground in afternoon sun with a convex dome mirror on a post at the tunnel mouth, a broadcast camera with a long lens, an optical-fibre cable, and a rainbow in the sprinkler spray](scenes/football/ray_optics.svg "The rainbow sitting in the sprinkler spray on the right is the whole of this lesson — a colour separation that the water did not put there.")

The sprinklers come on at half-time and throw a wide fan of spray across the far corner of the pitch. Zoya, warming up as a substitute, stops mid-stride: hanging in the mist, low down near the grass, there is a short arc of colour — red on the outside, violet on the inside, all of it perfectly ordered.

"The floodlights are doing it," she says. "They must have colour filters."

The groundsman, Ratan, shakes his head and points at the low sun behind her. He says the colours were in the sunlight the whole time; the water only sorted them out.

Zoya is not convinced by that either. Water is colourless. Sunlight looks white. Neither of them is red or violet, and neither of them is arranged in an order. So where does the order come from — and why does it always come out the same way round?

## The physics

The refractive index of a material is not one number. It is slightly larger for short wavelengths than for long ones: violet light travels a little more slowly in glass or water than red light does, so it has a larger $n$.

![A graph of the refractive index of a typical glass against wavelength: it falls steadily from violet at the short-wavelength end to red at the long-wavelength end](figures/dispersion/refractive-index-vs-wavelength.svg "A change of only about 0.02 across the visible range — tiny, but it is the whole reason a prism splits white light.")

Because Snell's law depends on $n$, each colour is bent through a slightly different angle. In a **thin** prism (refracting angle $A$ small, light entering near the normal) the deviation simplifies to

$$\delta = (n - 1)A$$

so each colour gets its own deviation. Since $n_V > n_R$, violet is deviated most and red least. That splitting is **dispersion**, and the gap between the extreme colours is the **angular dispersion**:

$$\theta = \delta_V - \delta_R = (n_V - n_R)A$$

![White light entering a glass prism and leaving spread into a fan of colours, with red deviated least and violet most](figures/dispersion/white-light-through-prism.svg "The order is fixed by the graph above: the larger the refractive index, the larger the deviation, so violet always ends up furthest from the incoming direction.")

The band of colours is the **spectrum**, and it shows that white light was a mixture all along — the prism sorts, it does not create. Newton proved exactly this by passing one colour from the spectrum through a second prism: it came out deviated but still the same colour, unsplittable.

It is useful to compare the spread with the overall bend. **Dispersive power** is that ratio,

$$\omega = \frac{n_V - n_R}{n_Y - 1}$$

with $n_Y$ the index for a middle, yellow wavelength. It depends only on the material, not on $A$ — which is what lets lens designers cancel colour fringing by combining two glasses of different $\omega$.

## Worked example

**Given:** a thin prism of refracting angle $A = 5^\circ$, made of glass with $n_V = 1.53$ and $n_R = 1.51$ (illustrative values).
**Find:** the angular dispersion, and the deviation of the middle of the beam.

**Step 1 — the spread between the ends of the spectrum.**

$$\theta = (n_V - n_R)A = (1.53 - 1.51) \times 5^\circ = 0.02 \times 5^\circ = 0.10^\circ$$

A tenth of a degree — about a fifth of the width of the Moon in the sky, and the reason a spectrum must be cast on a distant screen before the colours look separate.

**Step 2 — where the beam as a whole goes.** Take the middle of the visible range as $n_Y = 1.52$:

$$\delta_Y = (n_Y - 1)A = 0.52 \times 5^\circ = 2.6^\circ$$

So the whole beam swings through about $2.6^\circ$, and the colours fan out across only $0.10^\circ$ inside that.

**Sanity check:** the spread is far smaller than the bend — about one part in twenty-six — which matches everyday experience: a glass of water shifts what you see much more obviously than it colours it.

## Where the picture breaks

The arc in the sprinkler spray is not a prism. A raindrop disperses light at the surface, yes, but it also reflects it once inside before it comes back out, and that is what bends the light back towards the sun and fixes the rainbow at a particular angle of about $42^\circ$ from the direction opposite the sun. Dispersion explains the *order* of the colours in Zoya's arc; it does not by itself explain the *arc*.

The thin-prism formula is also a small-angle approximation. Use it on a chunky equilateral prism and it is wrong — there you need the full minimum-deviation relation from the last lesson, applied colour by colour.

Finally, a caution about the numbers: indices vary from glass to glass, so the values above are illustrative. And football is scenery here. Nothing about a ball splits into components the way white light does.

## Key takeaway

White light is a mixture, and a material's refractive index is slightly larger for violet than for red. So a prism deviates each colour differently — violet most, red least — and sorts the mixture into a spectrum. For a thin prism, $\delta = (n-1)A$ and the angular dispersion is $(n_V - n_R)A$, while the ratio $\omega = \dfrac{n_V - n_R}{n_Y - 1}$ describes the glass itself.
