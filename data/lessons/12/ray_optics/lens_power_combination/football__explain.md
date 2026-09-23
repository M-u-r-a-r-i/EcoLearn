---
concept_id: lens_power_combination
interest: football
format: explain
title: Why the optician talks in numbers, not centimetres
check:
  question: |-
    A converging lens of focal length $25\,\text{cm}$ is held in contact with a diverging lens of focal length $50\,\text{cm}$. What is the power of the combination?
  options:
    A: |-
      $+6.0\,\text{D}$
    B: |-
      $-2.0\,\text{D}$
    C: |-
      $+2.0\,\text{D}$
    D: |-
      $+0.02\,\text{D}$
  answer: C
  explanation: |-
    In metres, $P_1 = 1/0.25 = +4.0\,\text{D}$ and $P_2 = -1/0.50 = -2.0\,\text{D}$. For thin lenses in contact the powers add: $P = 4.0 - 2.0 = +2.0\,\text{D}$, so the pair still converges, with an equivalent focal length of $50\,\text{cm}$.
  misconceptions:
    A: |-
      Adds the sizes of the two powers and ignores the sign of the diverging lens. A diverging lens undoes some of the converging lens's bending, so its power must be subtracted.
    B: |-
      Subtracts the wrong way round, $-4.0 + 2.0$. The stronger lens decides the sign of the result, and here the converging lens is the stronger of the two.
    D: |-
      Uses focal lengths in centimetres. A dioptre is defined as one per **metre**, so $f$ must be converted before taking the reciprocal — a factor-of-100 slip.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground in afternoon sun with a convex dome mirror on a post at the tunnel mouth, a broadcast camera with a long lens, an optical-fibre cable, and a rainbow in the sprinkler spray](scenes/football/ray_optics.svg "Every lens in the picture has a number an optician would recognise — including the camera's.")

Ishita keeps goal, and she wears prescription sports glasses under the floodlights. At the start of the season the optician handed her a slip that said nothing about centimetres or focal lengths. It said, for each eye, a single number with a minus sign in front of it.

Two months later she is sitting on the treatment table while the team doctor, Vikram, digs a fleck of grit out of a graze on her knee. He is peering through a little magnifier that clips onto the front of his own spectacles.

"Two lenses, stacked?" she asks. "Doesn't the first one mess up the second?"

"They just add," he says, without looking up.

Ishita is not convinced. A $20\,\text{cm}$ lens and a $50\,\text{cm}$ lens stacked together certainly do not make a $70\,\text{cm}$ lens — that would be a *weaker* lens than either. So what is it that adds?

## The physics

Focal length is an awkward way to describe how strongly a lens bends light, because a **short** focal length means a **strong** lens. Flip it over and the awkwardness disappears. The **power** of a lens is

$$P = \frac{1}{f}$$

with $f$ in **metres**. The unit of power is the **dioptre** (D): $1\,\text{D} = 1\,\text{m}^{-1}$. A converging lens has positive $f$ and so positive power; a diverging lens has negative $f$ and negative power. Ishita's slip has a minus sign because a short-sighted eye needs a diverging lens.

Power is the natural quantity because of what happens when you put two thin lenses in contact. Send light through the first: it emerges heading for an image at $v_1$, which acts as the object for the second. Write the lens equation for each and add, and $v_1$ cancels straight out:

$$\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2} \qquad\Longleftrightarrow\qquad P = P_1 + P_2$$

![Left: a convex lens converging parallel rays and a concave lens spreading them, with positive and negative power. Right: two thin lenses in contact behaving as a single lens whose power is the sum](figures/lens_power_combination/lenses-in-contact.svg "Powers add; focal lengths do not. That is the whole reason opticians and lens makers count in dioptres.")

That is what Vikram meant. Not the focal lengths — the **powers** add. Stack a $+8\,\text{D}$ loupe on a $-3\,\text{D}$ spectacle lens and you get $+5\,\text{D}$: the pair still magnifies, just less than the loupe alone would.

Two conditions are hiding in that derivation: the lenses must be **thin**, and they must be in **contact**, so there is no room for the beam to spread between them. Separate them and the equivalent power becomes $P = P_1 + P_2 - d\,P_1 P_2$, with $d$ the separation — a formula you will meet if you study optical instruments further. The magnifications, meanwhile, do not add: they multiply, $m = m_1 m_2$.

## Worked example

**Given:** Vikram's spectacle lens has a power of $-3.0\,\text{D}$, and the clip-on loupe resting against it has a power of $+8.0\,\text{D}$.
**Find:** the power and focal length of the combination.

**Step 1 — add the powers.**

$$P = P_1 + P_2 = -3.0 + 8.0 = +5.0\,\text{D}$$

Positive, so the pair converges overall — the loupe more than cancels his own lens.

**Step 2 — turn that back into a focal length.**

$$F = \frac{1}{P} = \frac{1}{5.0} = 0.20\,\text{m} = 20\,\text{cm}$$

So the stack behaves as a single converging lens of focal length $20\,\text{cm}$ — about the length of a hand span, and the distance at which it makes a comfortable magnifier for the graze on Ishita's knee.

**Sanity check:** $+5\,\text{D}$ sits between the two lenses' powers and nearer the stronger one, which is what adding a weak negative to a strong positive has to give.

## Where the picture breaks

"In contact" is an idealisation. A clip-on loupe sits a few millimetres from the spectacle lens, so the true power is a little below $+5\,\text{D}$; for a distance of a few millimetres the correction is small, but for two lenses a hand's width apart it is not.

The formula is also silent about everything except focal length. Stacking lenses stacks their defects too — the colour fringes and edge softness add up, which is why a purpose-ground single lens beats two stacked ones of the same total power.

And an eye is not a lens in air: the cornea and the fluids inside contribute most of the eye's power, so the number on Ishita's slip is only the *correction* her eye needs, not the power of her eye.

## Key takeaway

Power $P = 1/f$ with $f$ in metres, measured in dioptres, and it is positive for a converging lens and negative for a diverging one. For thin lenses in contact, powers add: $P = P_1 + P_2$, equivalently $1/F = 1/f_1 + 1/f_2$. Focal lengths never add — that is exactly why opticians and lens designers work in dioptres.
