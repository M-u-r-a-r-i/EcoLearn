---
concept_id: dispersion
interest: gaming
format: explain
title: The graphics setting named after a flaw in glass
check:
  question: |-
    A thin prism of refracting angle $3^\circ$ is made of glass with $n_\text{violet} = 1.53$ and $n_\text{red} = 1.50$. What is the angular dispersion it produces?
  options:
    A: |-
      $0.03^\circ$
    B: |-
      $0.09^\circ$
    C: |-
      $1.55^\circ$
    D: |-
      $3.09^\circ$
  answer: B
  explanation: |-
    For a thin prism each colour is deviated by $\delta = (n-1)A$, so the angular dispersion is $\theta = (n_\text{violet} - n_\text{red})A = (0.03)(3^\circ) = 0.09^\circ$.
  misconceptions:
    A: |-
      Stops at the difference between the refractive indices and calls it an angle. A refractive index has no units at all; it only becomes an angle after it is multiplied by the prism's angle $A$.
    C: |-
      Works out the mean deviation, $(n_\text{mean} - 1)A$ — how far the whole beam is bent — instead of the dispersion, which is how far the colours are pulled *apart*. Deviation and dispersion are different quantities.
    D: |-
      Adds the two deviations instead of subtracting them. Both colours are bent the same way, so the spread between them is the difference; adding would mean red and violet left on opposite sides of the beam.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk at night with a monitor, a coolant reservoir, a cut-away VR headset, a glass prism, a glowing optical cable, a hand lens over a controller board and a wall-mounted dome mirror](scenes/gaming/ray_optics.svg "The prism on the desk is the honest version of what a graphics engine only pretends to do.")

Varun is doing what he always does on a new install: turning off every graphics setting he does not understand, one by one, to claw back frames.

Halfway down the list is one he has never noticed. **Chromatic aberration.** He toggles it off, and a faint orange-and-blue smear along every hard edge near the border of the picture quietly disappears. The middle of the screen looks identical.

This confuses him. Someone was *paid* to put that smear in. Why would a studio spend effort making a picture worse, then give you a switch to undo it?

Later he picks up his cheap VR viewer, and at the very edge of the lens is the same thing: the white menu text carrying a thin orange rim on one side and a blue-violet one on the other. He toggles everything in the settings menu. The rim stays.

One of these fringes is a deliberate imitation. The other is real, and no setting removes it. Where does a real one come from, and can you say in advance how bad a piece of glass will be?

## The physics

White light is not one thing. It is a mixture of wavelengths, and the refractive index of a medium is **not the same for all of them**. For ordinary glass $n$ is largest at the violet end of the spectrum and smallest at the red end:

![A graph of refractive index against wavelength for a typical crown glass, falling smoothly from about 1.531 at 400 nm to about 1.513 at 700 nm](figures/dispersion/refractive-index-vs-wavelength.svg "The change looks tiny — the third decimal place — but the whole of dispersion lives in it. Violet, with the shortest wavelength, has the largest index.")

Since Snell's law contains $n$, each colour is refracted through a slightly different angle. Send white light through a prism and the colours emerge along slightly different directions, spread into a spectrum. This splitting of white light by wavelength is **dispersion**.

![White light entering a glass prism and leaving as a fan of colours, with red deviated least and violet most](figures/dispersion/white-light-through-prism.svg "The prism does not add colour to the light. The colours were in the white light all along; different refractive indices pull them apart.")

For a **thin prism** — one whose refracting angle $A$ is a few degrees, small enough that every sine may be replaced by the angle itself — the deviation simplifies to

$$\delta = (n - 1)A$$

and it no longer depends on the angle of incidence. Apply that to the two ends of the spectrum and subtract. The **angular dispersion** between violet and red is

$$\theta = \delta_\text{violet} - \delta_\text{red} = (n_\text{violet} - n_\text{red})A$$

This is where Varun's real fringe comes from. A lens is not a prism, but away from its centre its two surfaces are inclined to each other like a shallow wedge, so it disperses light exactly as a thin prism does. Violet comes to a focus slightly nearer the lens than red, and the edge of the image carries a colour rim. Opticians call it **chromatic aberration** — and it is worst at the edge of the field and absent at the centre, which is exactly what he saw through the viewer.

That is also the answer to his first question. The setting in the game is imitating a real camera lens, because for decades every photograph and every film frame carried a trace of this, and our eyes read it as "this was filmed, not drawn". The engine paints the fringe on afterwards; it costs frames and it is optional. The one in the viewer is the genuine article.

## Worked example

**Given:** a thin prism of refracting angle $A = 6^\circ$, made of glass with $n_\text{violet} = 1.54$ and $n_\text{red} = 1.52$.
**Find:** the angular dispersion, and how far apart the two colours land on a wall $2.0\,\text{m}$ away.

**Step 1 — deviate each colour.**

$$\delta_\text{violet} = (1.54 - 1)(6^\circ) = 3.24^\circ, \qquad \delta_\text{red} = (1.52 - 1)(6^\circ) = 3.12^\circ$$

Both are bent the same way, towards the base — violet just a little more.

**Step 2 — the gap between them.**

$$\theta = 3.24^\circ - 3.12^\circ = 0.12^\circ$$

About a quarter of the width of the full Moon in the sky: small, but not invisible.

**Step 3 — picture it on the wall.** In radians, $0.12^\circ = 2.1 \times 10^{-3}\,\text{rad}$, so across $2.0\,\text{m}$ the two colours separate by

$$(2.1 \times 10^{-3})(2.0\,\text{m}) \approx 4\,\text{mm}$$

**Sanity check:** a patch of light a couple of metres from a small prism shows colour only at its edges, a few millimetres wide — about the thickness of a pencil line held at arm's length. That is exactly what you see when a lamp shines through a glass ornament, so the size is right.

## Where the picture breaks

Calling the spectrum "violet to red" hides how it works. $n$ changes smoothly with wavelength, so the colours form a continuous band, not a set of stripes. Newton's list of seven names is a convention, not a count of anything physical.

The thin-prism formula $\delta = (n-1)A$ is a small-angle approximation. For a $60^\circ$ prism it fails badly, and the dispersion there has to be worked out from the full minimum-deviation formula, colour by colour.

And the game's version is not this physics at all. It is a shader shifting the red, green and blue channels of an already-rendered image by a few pixels — a drawing of the effect, not the effect. A real lens splits *every* wavelength continuously and does it more strongly further from the axis; a channel shift does neither. A good headset cancels the real fringe in hardware instead, with elements of two different glasses chosen so that one's dispersion largely undoes the other's.

## Key takeaway

Refractive index depends on wavelength — larger for violet, smaller for red — so a single refraction splits white light into a spectrum. That is dispersion. For a thin prism each colour is deviated by $(n-1)A$, and the spread between violet and red is $\theta = (n_\text{violet} - n_\text{red})A$: a fraction of a degree for ordinary glass, but enough to put a coloured rim on the edge of every uncorrected image.
