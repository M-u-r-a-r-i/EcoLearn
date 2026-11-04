---
concept_id: microscope
interest: gaming
format: explain
title: Finding a cracked solder joint on a drifting controller
check:
  question: |-
    A hand lens of focal length $10\,\text{cm}$ is used as a simple microscope, with the final image formed at the near point, $D = 25\,\text{cm}$. What is its magnifying power?
  options:
    A: |-
      $2.5$
    B: |-
      $0.4$
    C: |-
      $3.5$
    D: |-
      about $250$
  answer: C
  explanation: |-
    For the final image at the near point, $m = 1 + \dfrac{D}{f} = 1 + \dfrac{25}{10} = 3.5$.
  misconceptions:
    A: |-
      Uses $m = D/f$, which is the formula for the *relaxed-eye* setting with the image at infinity. The extra $1$ belongs to the near-point adjustment, and the question specifies that one.
    B: |-
      Inverts the ratio to $f/D$. A magnifying power below $1$ would mean the lens made things smaller, which should be the alarm bell — a converging lens used this way always magnifies.
    D: |-
      Mixes the units, putting $D = 25\,\text{cm}$ over $f = 0.10\,\text{m}$. Both lengths must be in the same unit; the ratio $D/f$ is a pure number, so a mismatch inflates it by a factor of a hundred.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk at night with a monitor, a coolant reservoir, a cut-away VR headset, a glass prism, a glowing optical cable, a hand lens over a controller board and a wall-mounted dome mirror](scenes/gaming/ray_optics.svg "Bottom right: a hand lens held over a controller board. Everything this lesson is about is the question of what happens when that lens is not enough.")

Prisha's controller has developed a drift. Left alone on the desk, the character strolls slowly to the left until it walks into a wall. She has already tried every calibration menu there is.

So she opens it. Fourteen screws, a ribbon cable, and there is the little board with the analogue stick on it. She borrows her father's reading magnifier, clamps a desk lamp over the board and starts hunting for a bad joint.

Through the lens the solder blobs look like grey hills. But the joint she suspects — a hair-fine crack, if it is there at all — refuses to resolve. She moves the lens closer: bigger and hopelessly blurred. Further: sharp and small. She cannot have both.

The repair shop under the flyover charges fifty rupees to look. The man there puts the board under a stubby brass microscope, and Prisha, peering in after him, sees the crack instantly — a black line across a silver hill, obvious as a crack in a road.

Those lenses are no bigger than her father's magnifier, and the whole instrument is shorter than her forearm. So where did the extra magnification come from, if not from a stronger piece of glass?

## The physics

Start with the magnifier. A **simple microscope** is a single convex lens held so that the object lies inside its focal length, which gives an erect, magnified, virtual image the eye can focus on.

![A convex lens used as a magnifying glass, with the object inside the focal length and an enlarged upright virtual image behind it on the same side](figures/microscope/simple-magnifier.svg "The rays leaving the lens still spread apart. The eye traces them straight back and sees a large image on the same side as the object.")

Its **magnifying power** is the ratio of the angle the image subtends at the eye to the angle the object would subtend if you simply brought it to the **near point** $D$ — the closest distance a normal eye can focus comfortably, taken as $25\,\text{cm}$. That gives

$$m = 1 + \frac{D}{f} \quad \text{(final image at the near point)}, \qquad m = \frac{D}{f} \quad \text{(final image at infinity)}$$

So a lens of $f = 5\,\text{cm}$ gives about $6\times$ at the near point. To reach $50\times$ you would need $f$ of about half a centimetre — a bead of glass with a focus so short your eyelashes would touch it, and aberrations that would ruin the image anyway. That is Prisha's wall, and it is the wall for every single lens.

A **compound microscope** gets past it by magnifying **twice**. The object is placed just outside the focal point of a short-focus **objective**, which forms a real, inverted, magnified image inside the tube. That image is then viewed through the **eyepiece**, used exactly as a simple magnifier.

![Ray diagram of a compound microscope: the objective forms a real inverted image inside the tube at the focal point of the eyepiece, which sends the light out parallel](figures/microscope/compound-microscope.svg "Two stages in a line. The eyepiece never sees the object — it magnifies the image the objective has already made.")

Because the second stage works on the first stage's output, the magnifications **multiply**:

$$m = m_o \times m_e = \frac{v_o}{u_o} \times \left(\frac{D}{f_e}\ \text{ or }\ 1 + \frac{D}{f_e}\right)$$

depending on whether the final image sits at infinity (relaxed eye) or at the near point. All distances use the Cartesian convention, so a real object gives $u_o < 0$ and the negative magnification that results simply records that the final image is inverted — which is why a board shifts the "wrong" way under a microscope. All of this assumes thin lenses, paraxial rays and a normal eye with $D = 25\,\text{cm}$.

## Worked example

**Given:** an objective of focal length $f_o = 2.0\,\text{cm}$ with the controller board $2.5\,\text{cm}$ in front of it, and an eyepiece of $f_e = 5.0\,\text{cm}$, adjusted so the final image sits at the near point, $D = 25\,\text{cm}$.
**Find:** the magnifying power.

**Step 1 — where the objective puts its image.** With $u_o = -2.5\,\text{cm}$,

$$\frac{1}{v_o} = \frac{1}{2.0} + \frac{1}{-2.5} = 0.50 - 0.40 = 0.10\,\text{cm}^{-1} \quad\Rightarrow\quad v_o = 10\,\text{cm}$$

**Step 2 — how much bigger that first image is.**

$$m_o = \frac{v_o}{u_o} = \frac{10}{-2.5} = -4$$

Four times life size and upside down, floating in the air $10\,\text{cm}$ up the tube. Nobody ever sees it directly.

**Step 3 — the eyepiece magnifies that image.** At the near point,

$$m_e = 1 + \frac{D}{f_e} = 1 + \frac{25}{5.0} = 6$$

so

$$m = m_o \times m_e = -4 \times 6 = -24$$

Twenty-four times, inverted.

**Sanity check:** a crack half a millimetre long would appear about $12\,\text{mm}$ across — the width of a fingernail. That is about what a bench microscope shows on its lowest setting, so the answer is the right size.

## Where the picture breaks

Magnification is not the same as usefulness. You can multiply the two stages as high as you like and end up with a big, dim, fuzzy blob. The real limit is **resolution** — the ability to show two close things as two — and that is set by the wavelength of light and the width of the objective, not by the lens formula. Past about $1000\times$ an optical microscope shows nothing new however the numbers multiply, which is the whole reason electron microscopes exist.

The numbers above also treat the lenses as thin. A real objective is short, fat and made of several cemented elements, and its stated magnification comes from measurement, not from $v_o/u_o$.

And be careful with the story's conclusion. A visible crack is not automatically the fault; plenty of drift comes from a worn sensor that looks perfect under any magnification. Seeing more is not the same as diagnosing.

## Key takeaway

A single lens magnifies by $1 + D/f$ at the near point, or $D/f$ for a relaxed eye, and getting a large number that way needs an impractically short focal length. A compound microscope splits the job in two: a short-focus objective makes a real magnified image inside the tube, and the eyepiece magnifies *that* image again — so the two magnifying powers multiply, $m = m_o \times m_e$.
