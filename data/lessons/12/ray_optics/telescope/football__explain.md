---
concept_id: telescope
interest: football
format: explain
title: Finding the dead lamp on the floodlight pylon
check:
  question: |-
    A refracting telescope is used in normal adjustment. Which single change would **double** its magnifying power?
  options:
    A: |-
      Double the diameter of the objective lens
    B: |-
      Double the focal length of the eyepiece
    C: |-
      Halve the focal length of the eyepiece
    D: |-
      Halve the focal length of the objective
  answer: C
  explanation: |-
    In normal adjustment $m = f_o/f_e$, so halving $f_e$ doubles $m$ (and shortens the tube slightly, since its length is $f_o + f_e$).
  misconceptions:
    A: |-
      Confuses aperture with magnification. A wider objective gathers more light and resolves finer detail, giving a brighter, sharper view — but the magnifying power depends only on the two focal lengths.
    B: |-
      Inverts the ratio. The eyepiece's focal length is in the denominator, so a longer eyepiece gives *less* magnification, not more.
    D: |-
      Inverts the ratio the other way. The objective's focal length is on top, so halving it halves the magnifying power.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground in afternoon sun with a convex dome mirror on a post at the tunnel mouth, a broadcast camera with a long lens, an optical-fibre cable, and a rainbow in the sprinkler spray](scenes/football/ray_optics.svg "Long lenses point at things that are far away and refuse to look bigger. So does a telescope — it is the same idea in a plainer tube.")

One lamp in the bank on the south-west pylon has failed, and from the ground nobody can tell which. They are forty metres up in a cluster, all identical, and all dark until the whole bank is switched on. Climbing the pylon to find the dead one means an hour in a harness.

Prakash, the electrician, does not climb. He unpacks a scratched little telescope, rests it on the fence rail, and in under a minute he has the answer: third from the left, upper row, the glass blackened.

Sneha has stayed behind to finish her sprints and comes over to look. Later, when it is properly dark, Prakash swings the tube up at the Moon, and she finds she is looking at the edges of craters — and that everything in the eyepiece is upside down.

The lamps are the same distance away as they always were, and no extra light has appeared. Two pieces of glass a tube's length apart made a blackened lamp obvious. How does separating two lenses do that, and why does the picture have to arrive the wrong way up?

## The physics

A distant object sends rays that arrive essentially **parallel**. The problem is not that they are faint or small; it is that the whole lamp cluster subtends only a tiny angle $\alpha$ at your eye, and an eye cannot separate detail inside a small angle. A telescope does not enlarge the object. It enlarges the **angle**.

![Ray diagram of a refracting telescope in normal adjustment: parallel light from a distant object is brought to a focus by the objective, and the eyepiece, with its focal point at the same place, sends the light out parallel at a much larger angle](figures/telescope/refracting-telescope.svg "The objective makes a small real image in its focal plane; the eyepiece, sharing that focal plane, turns it back into parallel light — but tilted far more steeply.")

The long-focus **objective** brings the parallel bundle to a small, real, inverted image in its focal plane, $f_o$ behind it. The short-focus **eyepiece** is then set so that its own focal point falls on that image. Light therefore leaves the eyepiece parallel again, which a relaxed eye focuses without effort — this setting is **normal adjustment**, and it gives

$$m = \frac{\beta}{\alpha} = \frac{f_o}{f_e}, \qquad \text{tube length} = f_o + f_e$$

where $\alpha$ and $\beta$ are the angles subtended before and after, both small enough for the small-angle approximation. Magnifying power is a ratio of two angles, so it is a pure number.

So the design is a long objective and a short eyepiece — which is why serious telescopes are long. The inversion follows too: the objective's real image is inverted, and the eyepiece leaves it that way. A terrestrial telescope adds a third lens or a pair of prisms to turn the view upright, losing a little light in exchange.

Making the objective **wide** is a different matter from making it long. A wide objective gathers more light and resolves finer detail; it does nothing to $m$. Past a certain size a lens sags under its own weight, so large instruments use a concave mirror instead:

![Schematic of a Cassegrain reflecting telescope: a concave primary mirror sends light to a small convex secondary, which reflects it back through a hole in the primary to the eyepiece](figures/telescope/reflecting-telescope.svg "A mirror can be supported across its whole back, and reflection treats every wavelength alike — so there is no colour fringing to correct.")

A **reflecting telescope** replaces the objective lens with a concave mirror. Reflection is identical for every colour, so there is no chromatic aberration at all, and the mirror can be held from behind — which is why every large telescope in the world is a reflector. The magnifying power is still $f_o/f_e$, with $f_o$ now the primary mirror's focal length.

## Worked example

**Given:** Prakash's telescope has an objective of focal length $f_o = 90\,\text{cm}$ and an eyepiece of $f_e = 6.0\,\text{cm}$, in normal adjustment.
**Find:** the magnifying power and the length of the tube.

**Step 1 — the magnifying power.**

$$m = \frac{f_o}{f_e} = \frac{90}{6.0} = 15$$

The lamp cluster covers an angle fifteen times larger than it does to the naked eye — the same apparent size it would have from fifteen times closer, which is a little under three metres away.

**Step 2 — the length.** In normal adjustment the eyepiece's focal point sits on the objective's image, so the two lenses are

$$f_o + f_e = 90 + 6.0 = 96\,\text{cm}$$

apart — a tube a little under a metre, about the length of an outstretched arm.

**Sanity check:** roughly a metre of tube giving about fifteen times is exactly what a small hand-held scope does; an answer of $1.5$ or $1500$ would have meant an arithmetic slip.

## Where the picture breaks

The lamps are forty metres away, not at infinity, so the light from them is not quite parallel and Prakash has to push the eyepiece out a few millimetres to focus. "Normal adjustment" is an idealisation for genuinely distant objects — for the Moon it is exact enough, for the pylon it is not.

The formula also says nothing about brightness or sharpness, which is what actually decides whether he can see the blackened glass. Doubling $m$ with a shorter eyepiece spreads the same light over four times the area and gives a dimmer, blurrier view — "empty magnification". The objective's width, not the eyepiece, sets the real limit.

And there is no football analogy here at all. A telescope does not bring the pylon closer in any physical sense: nothing moves, and the light arriving at the objective is exactly the light that was always arriving.

## Key takeaway

A telescope magnifies the **angle** a distant object subtends, not the object. In normal adjustment the objective's focal plane coincides with the eyepiece's, giving $m = f_o/f_e$ and a tube of length $f_o + f_e$: long objective, short eyepiece, inverted image. Large instruments replace the objective with a concave mirror, which can be supported from behind and bends no colour differently from any other.
