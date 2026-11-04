---
concept_id: microscope
interest: football
format: explain
title: Finding out what is killing the grass in the goalmouth
check:
  question: |-
    A compound microscope is used in normal adjustment. Its eyepiece has a focal length of $5.0\,\text{cm}$, and its objective forms a real image $10$ times the size of the object. Taking $D = 25\,\text{cm}$, what is the total magnifying power?
  options:
    A: |-
      $15$
    B: |-
      $50$
    C: |-
      $2.0$
    D: |-
      $60$
  answer: B
  explanation: |-
    In normal adjustment the eyepiece contributes $m_e = D/f_e = 25/5.0 = 5$, and the two stages multiply: $m = 10 \times 5 = 50$.
  misconceptions:
    A: |-
      Adds the two magnifications. Each stage magnifies what the stage before it produced, so their effects multiply, exactly as two successive percentage increases do.
    C: |-
      Divides one magnification by the other. That would make a two-lens instrument weaker than its objective alone, which no microscope is.
    D: |-
      Uses $m_e = 1 + D/f_e = 6$, which is the eyepiece's magnification when the final image is at the near point. That is the other adjustment; in normal adjustment the final image is at infinity and $m_e = D/f_e$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground in afternoon sun with a convex dome mirror on a post at the tunnel mouth, a broadcast camera with a long lens, an optical-fibre cable, and a rainbow in the sprinkler spray](scenes/football/ray_optics.svg "The camera in this picture takes a huge scene and shrinks it. A microscope does the exact opposite to something a millimetre across.")

There is a patch of the goalmouth that will not recover. It came back yellow after the monsoon, then brown, and now it is spreading towards the six-yard line while the rest of the pitch is fine.

Meghna, an agriculture student doing a season with the club, cuts three blades of grass from the edge of the patch. On the bench she holds a hand lens over them: bigger, yes, and she can see the grass is dry at the tip — but nothing that explains anything.

So she takes the blades to her college lab and puts one under a compound microscope. Down the tube, the same blade looks like a landscape, and lying across it is a mesh of pale threads that were completely invisible before.

The hand lens has one lens. The microscope has two, a few centimetres apart, and neither of them is a spectacular piece of glass. Why should two ordinary lenses beat one good one so completely?

## The physics

Your eye cannot focus on anything closer than about $25\,\text{cm}$, the **least distance of distinct vision** $D$. Bring the grass blade nearer and it blurs, so that is the biggest angle a bare eye can ever get from it. Magnification, in this chapter, always means enlarging that **angle**.

A **simple microscope** is one convex lens of short focal length. Put the object just inside the focus and the lens makes an enlarged, erect, virtual image, which the eye views comfortably.

![A convex lens used as a magnifying glass: the object lies inside the focal length, the emerging rays still diverge, and their backward extensions form an enlarged upright virtual image](figures/microscope/simple-magnifier.svg "Nothing lands on a screen here. The eye receives diverging light and sees an image behind the object, larger and the right way up.")

With the object at the focus, the final image is at infinity and a relaxed eye does the work — **normal adjustment**:

$$m = \frac{D}{f}$$

Push the object slightly closer and the image comes to the near point instead, giving a little more, $m = 1 + D/f$, and a more tired eye. Either way, more magnification needs a shorter $f$, and a single lens of a few millimetres' focal length would have to be tiny, steeply curved and hopelessly blurred at the edges. That is the limit Meghna's hand lens ran into.

The **compound microscope** gets round it by magnifying twice. A short-focus **objective** sits just beyond its focal length from the specimen and forms a real, inverted, enlarged image inside the tube. The **eyepiece** then treats that image as its object and works as a simple magnifier on it.

![Ray diagram of a compound microscope: the objective forms a real inverted magnified image inside the tube, which falls at the focal point of the eyepiece so that light leaves parallel](figures/microscope/compound-microscope.svg "Two stages. The objective does the hard work of enlarging; the eyepiece lets a relaxed eye look at the result.")

Because each stage enlarges what the one before it made, the magnifications **multiply**:

$$m = m_o \times m_e = \frac{v_o}{u_o} \times \frac{D}{f_e}$$

in normal adjustment, where $v_o$ and $u_o$ are the objective's image and object distances. The final image is inverted with respect to the specimen — which is why a slide seems to move the wrong way when you push it.

## Worked example

**Given:** the objective has $f_o = 1.0\,\text{cm}$ and the grass blade is placed $1.25\,\text{cm}$ from it. The eyepiece has $f_e = 5.0\,\text{cm}$, and the microscope is in normal adjustment ($D = 25\,\text{cm}$).
**Find:** the total magnifying power.

**Step 1 — where the objective puts its image.** With $u_o = -1.25\,\text{cm}$,

$$\frac{1}{v_o} = \frac{1}{f_o} + \frac{1}{u_o} = 1.00 - 0.80 = 0.20\,\text{cm}^{-1} \quad\Rightarrow\quad v_o = 5.0\,\text{cm}$$

The real image sits $5\,\text{cm}$ up the tube — about the width of three fingers.

**Step 2 — how much the objective enlarged it.**

$$m_o = \frac{v_o}{u_o} = \frac{5.0}{-1.25} = -4$$

Four times as big, and inverted.

**Step 3 — what the eyepiece adds.**

$$m_e = \frac{D}{f_e} = \frac{25}{5.0} = 5$$

**Step 4 — the two stages together.** $m = 4 \times 5 = 20$ in size. A fungal thread $0.05\,\text{mm}$ across therefore subtends the same angle as a $1\,\text{mm}$ object held at the near point — about the thickness of a coin's edge, and no longer invisible.

**Sanity check:** twenty times is a modest, believable figure for a school microscope with these focal lengths; a serious instrument reaches a few hundred by using an objective of a millimetre or two.

## Where the picture breaks

Magnification is not the same as being able to *see* more detail. Two threads closer together than about half a wavelength of light apart blur into one however much you magnify — a limit that comes from diffraction, which you meet in wave optics, and not from any formula in this chapter. Pushing $m$ past that point is "empty magnification": a bigger, blurrier picture with no more information in it.

The formulas here also assume thin lenses, paraxial rays and a specimen in air. Real objectives are multi-element and often work with a drop of oil between lens and slide, precisely to beat the diffraction limit a little.

And football is the setting, not an analogy: a pitch is a living surface that people study with laboratory instruments, so the microscope belongs here — but nothing about the game models the optics.

## Key takeaway

A magnifier enlarges the **angle** an object subtends, measured against the best a bare eye can do at $D = 25\,\text{cm}$. One lens gives $m = D/f$ in normal adjustment. A compound microscope magnifies twice over — a short-focus objective making a real, inverted, enlarged image, and an eyepiece magnifying that — so the magnifications multiply: $m = \dfrac{v_o}{u_o} \times \dfrac{D}{f_e}$.
