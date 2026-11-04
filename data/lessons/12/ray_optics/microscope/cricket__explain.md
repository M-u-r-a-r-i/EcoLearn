---
concept_id: microscope
interest: cricket
format: explain
title: Why the curator's hand lens runs out of magnification
check:
  question: |-
    In a compound microscope the objective forms a real image magnified $20$ times, and the eyepiece has a focal length of $5.0\,\text{cm}$. The instrument is adjusted so that the final image is at infinity, for a relaxed eye with a near point of $25\,\text{cm}$. What is its magnifying power?
  options:
    A: |-
      $25$
    B: |-
      $100$
    C: |-
      $120$
    D: |-
      $4$
  answer: B
  explanation: |-
    With the final image at infinity the eyepiece contributes $m_e = D/f_e = 25/5 = 5$, and the two stages multiply: $m = m_o \times m_e = 20 \times 5 = 100$.
  misconceptions:
    A: |-
      Adds the two magnifications instead of multiplying them. The eyepiece works on the image the objective has already made, so each stage multiplies what reaches it — magnifications compound, they do not accumulate.
    C: |-
      Uses the near-point eyepiece formula $1 + D/f_e = 6$ although the question says the final image is at infinity. Both formulas are correct, for different adjustments; the extra $1$ belongs only to the near-point setting.
    D: |-
      Divides the two numbers, as if the eyepiece's focal length reduced the objective's magnification. A short-focus eyepiece magnifies more, not less — $f_e$ belongs in a denominator with $D$ on top, not underneath $m_o$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A sunlit cricket ground with the sun's rays, a broadcast camera with a long lens, a stump camera, a fielder in curved sunglasses, and a small rainbow in the sprinkler spray](scenes/cricket/ray_optics.svg "Look at the camera's long lens: several lenses in a line, each working on what the one before it produced.")

Two days before the match, the curator is crouched over the middle with a small hand lens on a string, moving it over the surface an inch at a time. Aditi, who is doing her school project on pitch preparation, crouches beside him.

Through the lens the cracks look like canyons and she can count the individual blades of the cut grass. She asks whether she can see the soil grains too. He shakes his head and hands her the lens: however she holds it, the picture either gets bigger and hopelessly blurred, or sharp and small. She cannot have both.

"Take some back to school," he says, and cuts a plug of turf for her. In the school lab she puts a single grass blade under the old brass microscope, and there are the cells — a honeycomb, sharp and enormous.

The microscope's lenses are no thicker than the curator's hand lens. It is not even much longer than her forearm. So where does the extra magnification come from, if not from a stronger piece of glass?

## The physics

Start with the hand lens. A **simple microscope** is one convex lens held so that the object is inside its focal length, which gives an erect, magnified, virtual image the eye can focus on.

![A convex lens used as a magnifying glass, with the object inside the focal length and an enlarged upright virtual image behind it on the same side](figures/microscope/simple-magnifier.svg "The rays leaving the lens still diverge. The eye traces them straight back and sees a large image on the same side as the object.")

Its magnifying power is the ratio of the angle the image subtends at the eye to the angle the object would subtend if you simply brought it to the **near point** $D$, the closest distance a normal eye can focus comfortably — taken as $25\,\text{cm}$. That gives

$$m = 1 + \frac{D}{f} \quad \text{(final image at the near point)}, \qquad m = \frac{D}{f} \quad \text{(final image at infinity)}$$

So a lens of $f = 5\,\text{cm}$ gives about $6\times$ at the near point. To reach $50\times$ you would need $f$ of about half a centimetre — a bead of glass a few millimetres across, with a focus so short you would have to press your eyelash against it, and aberrations that ruin the image. That is the curator's wall.

A **compound microscope** gets past it by magnifying twice. The object is placed just outside the focal point of a short-focus **objective**, which forms a real, inverted, magnified image inside the tube. That image is then viewed through the **eyepiece**, which is used exactly as a simple magnifier.

![Ray diagram of a compound microscope: the objective forms a real inverted image inside the tube at the focal point of the eyepiece, which sends the light out parallel](figures/microscope/compound-microscope.svg "Two stages in a line. The eyepiece never sees the object — it magnifies the image the objective has already made.")

Because the second stage works on the first stage's output, the magnifications **multiply**:

$$m = m_o \times m_e = \frac{v_o}{u_o} \times \left(\frac{D}{f_e}\ \text{or}\ 1 + \frac{D}{f_e}\right)$$

depending on whether the final image is at infinity (relaxed eye) or at the near point. The final image is inverted with respect to the object — which is why slides move the "wrong" way under a microscope. All of this assumes thin lenses, paraxial rays and a normal eye with $D = 25\,\text{cm}$.

## Worked example

**Given:** an objective of focal length $f_o = 1.0\,\text{cm}$ with the grass blade $1.1\,\text{cm}$ in front of it, and an eyepiece of $f_e = 5.0\,\text{cm}$, adjusted for a relaxed eye ($D = 25\,\text{cm}$).
**Find:** the magnifying power.

**Step 1 — what the objective does.** With $u_o = -1.1\,\text{cm}$ and $f_o = 1.0\,\text{cm}$,

$$\frac{1}{v_o} = \frac{1}{1.0} + \frac{1}{-1.1} = 0.091\,\text{cm}^{-1} \quad\Rightarrow\quad v_o = 11\,\text{cm}$$

**Step 2 — how much bigger that first image is.**

$$m_o = \frac{v_o}{u_o} = \frac{11}{-1.1} = -10$$

Ten times life size, upside down — and it is floating in the air inside the tube, $11\,\text{cm}$ up from the objective.

**Step 3 — the eyepiece magnifies that.** For a relaxed eye, $m_e = D/f_e = 25/5.0 = 5$, so

$$m = 10 \times 5 = 50 \ \text{(inverted)}$$

**Sanity check:** a grass fibre a tenth of a millimetre across would look about $5\,\text{mm}$ wide — a pencil line seen close up. That is about what a school microscope on its lowest setting actually shows, so the answer is the right size.

## Where the picture breaks

Magnification is not the same as usefulness. You can multiply the two stages as high as you like and end up with a big, dim, fuzzy blob: the real limit is **resolution**, the ability to show two close things as two, and that is set by the wavelength of light and the width of the objective, not by the lens formula. Beyond about $1000\times$ an optical microscope shows nothing new, however the numbers multiply. That is the idea behind an electron microscope.

The numbers above also assume the light-gathering is perfect and the lenses are thin, which real objectives — short, fat and made of several elements — are not.

And a caution about the setting: the hand lens on the curator's string is genuinely a simple microscope, but nothing else here is a cricket analogy. The two-stage trick has no counterpart on the field, and forcing one would only get in the way.

## Key takeaway

A single lens magnifies by $1 + D/f$ (near point) or $D/f$ (relaxed eye), and getting a large number that way needs an impractically short focal length. A compound microscope splits the job in two: a short-focus objective makes a real magnified image, and the eyepiece magnifies that image again, so the magnifying powers multiply, $m = m_o \times m_e$.
