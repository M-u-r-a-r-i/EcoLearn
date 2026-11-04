---
concept_id: telescope
interest: cricket
format: explain
title: The scoreboard across the ground, in a tube longer than a bat
check:
  question: |-
    A refracting telescope has an objective of focal length $100\,\text{cm}$ and an eyepiece of focal length $5.0\,\text{cm}$, used in normal adjustment. What is its magnifying power, and how far apart are the two lenses?
  options:
    A: |-
      $20$, with the lenses $95\,\text{cm}$ apart
    B: |-
      $0.05$, with the lenses $105\,\text{cm}$ apart
    C: |-
      $20$, with the lenses $105\,\text{cm}$ apart
    D: |-
      $500$, with the lenses $105\,\text{cm}$ apart
  answer: C
  explanation: |-
    In normal adjustment $m = f_o/f_e = 100/5.0 = 20$, and the two focal points coincide, so the separation is $f_o + f_e = 105\,\text{cm}$.
  misconceptions:
    A: |-
      Gets the magnification right but subtracts the focal lengths. The image made by the objective sits one focal length behind it and one focal length in front of the eyepiece, so the two lengths add.
    B: |-
      Inverts the ratio to $f_e/f_o$. A magnification below $1$ would mean the telescope made things smaller — the test any answer should survive is whether it is bigger than $1$.
    D: |-
      Multiplies the focal lengths instead of dividing. Magnifying power is a ratio of two angles and so is a pure number; multiplying two lengths gives an area, not a ratio.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A sunlit cricket ground with the sun's rays, a broadcast camera with a long lens, a stump camera, a fielder in curved sunglasses, and a small rainbow in the sprinkler spray](scenes/cricket/ray_optics.svg "The broadcast camera's long lens is doing exactly the telescope's job — gathering light from a narrow strip of the ground far away.")

It is the last session of a day-night game and the scoreboard is at the far end, past the sightscreen. Ritika, keeping the club's paper record, has been squinting at it for an hour.

The groundsman brings out a battered brass spotting scope from the store room and props it on the balcony rail. She puts her eye to it and the scoreboard jumps across the ground: the bowling figures, the little dots of the over-by-over, all readable.

Then she notices two things. The whole view is **upside down** — she has to read the figures by turning her head. And the scope is light: a tube a bit longer than a bat, a small lens at her eye, a bigger one at the far end, and nothing but air between them.

The scoreboard has not moved and the light coming from it has not increased. Two pieces of glass a metre apart made distant lettering readable. How can separating two lenses do that — and why does it have to arrive the wrong way up?

## The physics

A distant object sends rays that are, for practical purposes, **parallel** when they arrive. The trouble is not that they are weak or small; it is that the whole scoreboard subtends only a tiny angle $\alpha$ at your eye, and the eye cannot resolve detail within a small angle. A telescope does not enlarge the object. It enlarges the *angle*.

![Ray diagram of a refracting telescope in normal adjustment: parallel light from a distant object is focused by the objective into the shared focal plane, and the eyepiece sends it out parallel again at a much larger angle](figures/telescope/refracting-telescope.svg "The objective makes a small real image in its focal plane; the eyepiece, with its focal point at the same place, turns that image back into parallel light — but at a far steeper angle.")

The long-focus **objective** brings the parallel bundle to a small real, inverted image in its focal plane, a distance $f_o$ behind it. The short-focus **eyepiece** is then placed so that its own focal point falls on that same image. Light therefore leaves the eyepiece parallel again, which a relaxed eye can focus without effort — this setting is called **normal adjustment**. Two consequences follow:

$$m = \frac{\beta}{\alpha} = \frac{f_o}{f_e}, \qquad \text{tube length} = f_o + f_e$$

where $\alpha$ and $\beta$ are the angles subtended at the eye before and after, both small enough for the small-angle approximation. Magnifying power is a ratio of angles, so it is a pure number.

That formula answers Ritika's first question: a long objective and a short eyepiece. It also explains why serious telescopes are long. And the image is inverted because the objective's real image is inverted and the eyepiece, acting as a magnifier, leaves it that way. For astronomy nobody minds; a terrestrial telescope adds a third lens or a pair of prisms to turn the picture back up the right way, at the cost of some light.

Magnification is not why objectives are made large: a wide objective gathers more light and resolves finer detail. Past a certain size a lens sags under its own weight, so large instruments use a concave mirror instead:

![Schematic of a Cassegrain reflecting telescope: a concave primary mirror reflects light to a small convex secondary, which sends it back through a hole in the primary to the eyepiece](figures/telescope/reflecting-telescope.svg "A mirror can be supported across its whole back, and reflection does not depend on wavelength — so there is no colour fringing to correct.")

A **reflecting telescope** replaces the objective lens with a concave mirror. Reflection is the same for every wavelength, so there is no chromatic aberration at all, and the mirror can be held from behind — which is why every large telescope in the world is a reflector. The magnifying power is still $f_o/f_e$, with $f_o$ now belonging to the primary mirror.

## Worked example

**Given:** a spotting scope with an objective of focal length $f_o = 120\,\text{cm}$ and an eyepiece of $f_e = 4.0\,\text{cm}$, in normal adjustment.
**Find:** the magnifying power and the length of the tube.

**Step 1 — the magnifying power.**

$$m = \frac{f_o}{f_e} = \frac{120}{4.0} = 30$$

So the scoreboard's lettering covers an angle $30$ times larger than it does to the naked eye — the same apparent size it would have from thirty times closer.

**Step 2 — the length.** In normal adjustment the eyepiece's focal point sits on the objective's image, so the lenses are

$$f_o + f_e = 120 + 4.0 = 124\,\text{cm}$$

apart — a tube a bit longer than a full-size bat, which may be at most $96.52\,\text{cm}$.

**Sanity check:** a hand-held scope of a metre or so giving a few tens of times magnification is exactly what you would expect; if the arithmetic had produced $3$ or $3000$, something would be wrong.

## Where the picture breaks

"Normal adjustment" is one particular setting. Push the eyepiece in slightly and the final image comes to the near point instead of infinity, giving a little more magnification, $m = \dfrac{f_o}{f_e}\left(1 + \dfrac{f_e}{D}\right)$, at the cost of a tired eye after an hour of scoring.

The formula also has nothing to say about brightness or sharpness, which is what actually decides whether Ritika can read the figures. Doubling $m$ by fitting a shorter eyepiece spreads the same light over four times the area and makes the view dimmer and blurrier — "empty magnification". The objective's width, not the eyepiece's focal length, sets the real limit.

And a caution about the setting: the broadcast camera's long lens in the scene works on the same principle, but the cricket itself carries no analogy here. A telescope is not "bringing the scoreboard closer" in any physical sense — nothing moves, and the light arriving is exactly the same light.

## Key takeaway

A telescope magnifies the *angle* a distant object subtends, not the object. In normal adjustment the objective's focal plane and the eyepiece's focal plane coincide, giving $m = f_o/f_e$ and a tube of length $f_o + f_e$: a long objective and a short eyepiece. Mirrors replace the objective in large instruments because they can be supported from behind and bend every colour identically.
