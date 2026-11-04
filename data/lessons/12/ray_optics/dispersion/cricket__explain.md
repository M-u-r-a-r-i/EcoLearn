---
concept_id: dispersion
interest: cricket
format: explain
title: The orange and blue edge on a white sightscreen
check:
  question: |-
    A thin prism of refracting angle $4^\circ$ is made of glass with $n_\text{violet} = 1.54$ and $n_\text{red} = 1.52$. What is the angular dispersion it produces?
  options:
    A: |-
      $0.08^\circ$
    B: |-
      $0.02^\circ$
    C: |-
      $2.12^\circ$
    D: |-
      $4.24^\circ$
  answer: A
  explanation: |-
    For a thin prism each colour is deviated by $\delta = (n-1)A$, so the angular dispersion is $\theta = (n_\text{violet} - n_\text{red})A = (0.02)(4^\circ) = 0.08^\circ$.
  misconceptions:
    B: |-
      Stops at the difference of the refractive indices and calls it an angle. A refractive index has no units at all; it only becomes an angle after multiplying by the prism's angle $A$.
    C: |-
      Calculates the mean deviation $(n_\text{mean} - 1)A$ — how far the whole beam is bent — instead of the dispersion, which is how far the colours are spread *apart*. Deviation and dispersion are different quantities.
    D: |-
      Adds the two deviations instead of subtracting them. Both colours are bent the same way, so the spread between them is the difference; adding would mean the red and violet rays left on opposite sides of the beam.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A sunlit cricket ground with the sun's rays, a broadcast camera with a long lens, a stump camera, a fielder in curved sunglasses, and a small rainbow in the sprinkler spray](scenes/cricket/ray_optics.svg "The small rainbow in the sprinkler spray on the right is the same effect as the one this lesson is about.")

Sanjana is doing the boundary count from the pavilion balcony and there are two pairs of binoculars on the shelf: a heavy old brass pair and the coach's newer ones.

Through the new pair the white sightscreen at the far end is plain white, with a clean straight edge against the dark green behind it. Through the old pair, the same edge carries a thin coloured rim — orange along the top side, a faint blue-violet along the bottom. She thinks the eyepiece is dirty, wipes it, looks again. The rim is still there. It is strongest at the edge of the view and disappears if she centres the sightscreen.

Later, filling the drinks bottles, she notices the groundsman's sprinkler throwing a short arc of colour across the outfield — the same order of colours, red on the outside, violet on the inside.

Nothing on the sightscreen is orange and nothing in the water is coloured. The colour is being made somewhere between the object and her eye. Where does it come from, and can you say in advance how much of it a piece of glass will produce?

## The physics

White light is not one thing. It is a mixture of wavelengths, and the refractive index of a medium is **not the same for all of them**. For ordinary glass, $n$ is largest at the violet end of the spectrum and smallest at the red end:

![A graph of refractive index against wavelength for a typical crown glass, falling smoothly from about 1.531 at 400 nm to about 1.513 at 700 nm](figures/dispersion/refractive-index-vs-wavelength.svg "The change looks small — the third decimal place — but the whole of dispersion lives in it. Violet, with the shortest wavelength, has the largest index.")

Since Snell's law contains $n$, each colour is refracted through a slightly different angle. Send white light through a prism and the colours come out along slightly different directions, spread into a spectrum. This splitting of white light by wavelength is **dispersion**.

![White light entering a glass prism and leaving as a fan of colours, with red deviated least and violet most](figures/dispersion/white-light-through-prism.svg "The prism does not add colour to the light. The colours were in the white light all along; different refractive indices pull them apart.")

For a **thin prism** — one whose refracting angle $A$ is a few degrees, small enough that every sine may be replaced by the angle itself — the deviation simplifies to

$$\delta = (n - 1)A$$

and it no longer depends on the angle of incidence. Apply that to the two ends of the spectrum and subtract. The **angular dispersion** between violet and red is

$$\theta = \delta_\text{violet} - \delta_\text{red} = (n_\text{violet} - n_\text{red})A$$

This is where Sanjana's coloured rim comes from. A lens is not a prism, but away from its centre its two surfaces are inclined to each other like a shallow wedge, so it disperses light exactly like one. Violet comes to a focus slightly nearer the lens than red, and the edge of the image carries a colour fringe. Opticians call it **chromatic aberration**, and the reason her newer binoculars are clean is that their lenses are made of two glasses cemented together, chosen so that one's dispersion largely cancels the other's.

The sprinkler rainbow is the same physics in water droplets, with a reflection inside each drop as well.

## Worked example

**Given:** a thin glass prism of refracting angle $A = 5^\circ$, with $n_\text{violet} = 1.53$ and $n_\text{red} = 1.51$.
**Find:** the angular dispersion, and how far apart the two colours land on a wall $10\,\text{m}$ away.

**Step 1 — deviate each colour.**

$$\delta_\text{violet} = (1.53 - 1)(5^\circ) = 2.65^\circ, \qquad \delta_\text{red} = (1.51 - 1)(5^\circ) = 2.55^\circ$$

Both are bent the same way, towards the base — violet just a little more.

**Step 2 — the gap between them.**

$$\theta = 2.65^\circ - 2.55^\circ = 0.10^\circ$$

A tenth of a degree: about a fifth of the width of the full Moon in the sky.

**Step 3 — picture it on a wall.** In radians $0.10^\circ = 1.75 \times 10^{-3}\,\text{rad}$, so across $10\,\text{m}$ the two colours separate by

$$(1.75 \times 10^{-3})(10\,\text{m}) \approx 1.7\,\text{cm}$$

**Sanity check:** a patch of light a few metres from a small prism shows colour only at its edges, a centimetre or two wide — which is exactly what you see when sunlight comes through a glass ornament. The size is right.

## Where the picture breaks

Calling the spectrum "violet to red" hides how it really works: $n$ changes smoothly with wavelength, so the colours are a continuous band, not seven stripes. Newton's list of seven names is a convention, not a count of anything physical.

The thin-prism formula $\delta = (n-1)A$ is a small-angle approximation. For the $60^\circ$ trophy prism of the previous lesson it fails badly, and dispersion there must be worked out from the full minimum-deviation formula, colour by colour.

Finally, the sprinkler's arc is not a prism at all. It needs refraction *and* an internal reflection inside each droplet, and the angle it appears at ($42^\circ$ from the anti-solar direction) comes from that geometry, not from any wedge of glass. The shared idea is only the wavelength-dependent index.

## Key takeaway

Refractive index depends on wavelength — larger for violet, smaller for red — so a single refraction splits white light into a spectrum. That is dispersion. For a thin prism each colour is deviated by $(n-1)A$, and the spread between violet and red is $\theta = (n_\text{violet} - n_\text{red})A$: a fraction of a degree for ordinary glass, but enough to put a coloured rim on every uncorrected image.
