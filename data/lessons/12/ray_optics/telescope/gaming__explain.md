---
concept_id: telescope
interest: gaming
format: explain
title: The zoom slider that turns out to be a box of eyepieces
check:
  question: |-
    You want a magnifying power of $30$ from a refracting telescope whose objective has a focal length of $120\,\text{cm}$, used in normal adjustment. What focal length must the eyepiece have?
  options:
    A: |-
      $4.0\,\text{cm}$
    B: |-
      $90\,\text{cm}$
    C: |-
      $3600\,\text{cm}$
    D: |-
      $0.25\,\text{cm}$
  answer: A
  explanation: |-
    In normal adjustment $m = f_o/f_e$, so $f_e = f_o/m = 120 \div 30 = 4.0\,\text{cm}$. A short-focus eyepiece is what gives a high magnification.
  misconceptions:
    B: |-
      Subtracts, treating the magnification as a length to be taken off the objective. Magnifying power is a ratio of two angles and so is a pure number; you cannot subtract it from a distance.
    C: |-
      Multiplies instead of dividing. That would mean a longer eyepiece magnified more, which is backwards: the eyepiece is the short lens precisely because $f_e$ sits in the denominator.
    D: |-
      Inverts the ratio to $m/f_o$. Checking the size would catch it — an eyepiece with a focal length of a quarter of a centimetre would have to be pressed against your eyeball.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk at night with a monitor, a coolant reservoir, a cut-away VR headset, a glass prism, a glowing optical cable, a hand lens over a controller board and a wall-mounted dome mirror](scenes/gaming/ray_optics.svg "Two lenses a fixed distance apart, and nothing but air in between. That is the whole instrument this lesson is about.")

Aryan has put ninety hours into a space simulator, most of them at the observatory: point the dish, pick a target, drag the zoom slider, wait for the image to sharpen.

His neighbour from the astronomy club lends him a real telescope — a white tube a little shorter than a metre, a big lens at the far end, a small one at his eye, a tripod, and a shoebox of little metal cylinders.

Two things stop him within a minute. The Moon is **upside down** — not tilted, properly inverted, so he has to rebuild his map of the craters from scratch. And there is no zoom: to magnify more, you unscrew the lens at your eye and screw in a different one from the shoebox. That is the entire mechanism.

The Moon has not moved and is no brighter than it ever was. Two pieces of glass, most of a metre apart, made it readable. How can *separating* two lenses do that — and why does the picture arrive the wrong way up?

## The physics

A distant object sends rays that are, for practical purposes, **parallel** when they arrive. The trouble is not that they are weak: the object subtends only a tiny angle $\alpha$ at your eye, and the eye cannot resolve detail inside a small angle. A telescope does not enlarge the object. It enlarges the **angle**.

![Ray diagram of a refracting telescope in normal adjustment: parallel light from a distant object is focused by the objective into the shared focal plane, and the eyepiece sends it out parallel again at a much larger angle](figures/telescope/refracting-telescope.svg "The objective makes a small real image in its focal plane; the eyepiece, with its focal point at the same place, turns that image back into parallel light — but at a far steeper angle.")

The long-focus **objective** brings the parallel bundle to a small real, inverted image in its focal plane, a distance $f_o$ behind it. The short-focus **eyepiece** is then set so that its own focal point falls on that same image. Light therefore leaves the eyepiece parallel again, which a relaxed eye can focus with no effort — this setting is **normal adjustment**. Two results follow:

$$m = \frac{\beta}{\alpha} = \frac{f_o}{f_e}, \qquad \text{tube length} = f_o + f_e$$

where $\alpha$ and $\beta$ are the angles subtended at the eye before and after, both small enough for the small-angle approximation.

That answers Aryan's second puzzle. There is no zoom because $m$ is fixed by the two focal lengths, and only one of them is easy to change — hence the shoebox. It also explains why serious telescopes are long: a big $m$ needs a big $f_o$.

The inversion is not a fault either. The objective's real image is inverted, and the eyepiece, working as a magnifier, leaves it that way; for astronomy nobody minds. A terrestrial telescope adds prisms to turn the picture back up the right way, at the cost of some light.

Objectives are made wide not for magnification but to gather more light and resolve finer detail. Past a certain size a lens sags under its own weight, so large instruments use a concave mirror instead:

![Schematic of a Cassegrain reflecting telescope: a concave primary mirror reflects light to a small convex secondary, which sends it back through a hole in the primary to the eyepiece](figures/telescope/reflecting-telescope.svg "A mirror can be supported across its whole back, and reflection does not depend on wavelength — so there is no colour fringing to correct.")

A **reflecting telescope** replaces the objective lens with a concave mirror. Reflection is identical for every wavelength, so there is no chromatic aberration at all, and the mirror can be supported from behind — which is why every large telescope is a reflector. The magnifying power is still $f_o/f_e$, with $f_o$ now belonging to the primary mirror.

## Worked example

**Given:** the borrowed telescope has an objective of focal length $f_o = 80\,\text{cm}$, and the eyepiece Aryan screws in first has $f_e = 4.0\,\text{cm}$. It is used in normal adjustment.
**Find:** the magnifying power and the length of the tube.

**Step 1 — the magnifying power.**

$$m = \frac{f_o}{f_e} = \frac{80}{4.0} = 20$$

So the Moon covers an angle $20$ times larger than it does to the naked eye — the same apparent size it would have from twenty times closer.

**Step 2 — the length.** In normal adjustment the eyepiece's focal point sits on the objective's image, so the two lenses are

$$f_o + f_e = 80 + 4.0 = 84\,\text{cm}$$

apart: a tube a little shorter than a metre, which is what Aryan is holding.

**Sanity check:** a tube under a metre long giving a couple of dozen times magnification is the right order for a beginner's telescope. Had the arithmetic given $2$ or $2000$, something would be wrong.

## Where the picture breaks

"Normal adjustment" is one particular setting: push the eyepiece in slightly and the final image forms at the near point instead, giving a little more magnification, $m = \dfrac{f_o}{f_e}\left(1 + \dfrac{f_e}{D}\right)$, at the cost of a tired eye.

The formula also says nothing about brightness or sharpness, which is what actually decides whether Aryan sees anything. Halving $f_e$ doubles $m$ but spreads the same light over four times the area, so the view gets dimmer and blurrier — "empty magnification". The objective's width, not the eyepiece, sets the real limit, and that is the number the shoebox cannot change.

And the simulator is not a telescope. A zoom slider narrows the rendered field of view and redraws the scene from stored data; nothing is focused and no light is gathered, so it can "magnify" as far as the artwork allows. A real telescope has no such freedom — which is exactly why Aryan found the shoebox surprising.

## Key takeaway

A telescope magnifies the *angle* a distant object subtends, not the object. In normal adjustment the objective's focal plane and the eyepiece's focal plane coincide, giving $m = f_o/f_e$ and a tube of length $f_o + f_e$: a long objective and a short eyepiece. Mirrors replace the objective in large instruments because they can be supported from behind and bend every colour identically.
