---
concept_id: lens_power_combination
interest: cricket
format: explain
title: Why the magnifier gets weaker when you hold it against your glasses
check:
  question: |-
    A converging lens of power $+8.0\,\text{D}$ is held in contact with a diverging lens of power $-3.0\,\text{D}$. What is the focal length of the combination?
  options:
    A: |-
      $-20.8\,\text{cm}$
    B: |-
      $+9.1\,\text{cm}$
    C: |-
      $+20\,\text{cm}$
    D: |-
      $-20\,\text{cm}$
  answer: C
  explanation: |-
    Powers in contact add with their signs: $P = 8.0 - 3.0 = +5.0\,\text{D}$, so $f = 1/P = 0.20\,\text{m} = +20\,\text{cm}$, still converging but weaker than the first lens alone.
  misconceptions:
    A: |-
      Adds the focal lengths ($12.5\,\text{cm}$ and $-33.3\,\text{cm}$) instead of the powers. Focal lengths do not add; their reciprocals do, which is exactly why opticians work in dioptres.
    B: |-
      Adds the sizes of the powers and ignores the minus sign, giving $11\,\text{D}$. A diverging lens subtracts from the combination — that is what its negative power means.
    D: |-
      Gets the size right but assumes that including a concave lens must make the result diverging. The stronger lens wins: $+8.0$ against $-3.0$ still leaves a converging combination.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A sunlit cricket ground with the sun's rays, a broadcast camera with a long lens, a stump camera, a fielder in curved sunglasses, and a small rainbow in the sprinkler spray](scenes/cricket/ray_optics.svg "The fielder's sunglasses and the camera's lens are both stacks of lenses, not single pieces of glass.")

Tanvi analyses the club's practice videos, and she is short-sighted, so there are always glasses on her nose. A new box of balls has arrived and the captain wants the batch code checked — a line of grey print stamped so small on the leather that nobody can read it.

Tanvi borrows a magnifying glass from the first-aid kit and presses it flat against her right spectacle lens, sure that two lenses must beat one. The code comes up blurry and hardly bigger than before.

Irritated, she pulls the glasses off, holds the magnifier by itself at the same distance, and the tiny letters leap out, sharp and large.

The optician who sold her the glasses wrote them down as "minus three", not in centimetres. The magnifier's box says nothing at all. Two lenses, and together they did *less* than one of them did alone. Why would a lens ever subtract — and how do you predict what a stack of lenses will do before you look through it?

## The physics

Focal length is an awkward way to describe a lens, because a *strong* lens has a *small* $f$ and the numbers run backwards. So opticians and physicists use the reciprocal, the **power**:

$$P = \frac{1}{f} \qquad \text{with } f \text{ in metres}$$

The unit of power is the **dioptre**, symbol $\text{D}$, and $1\,\text{D} = 1\,\text{m}^{-1}$. A converging (convex) lens has $f > 0$, so $P > 0$; a diverging (concave) lens has $f < 0$, so $P < 0$. Tanvi's "minus three" means a concave lens of $-3.0\,\text{D}$, focal length $-33\,\text{cm}$, which spreads light out a little before it reaches her eye — the correction a short-sighted eye needs.

![Left: a convex lens converging parallel rays to a real focus with positive power, and a concave lens spreading them with negative power. Right: two thin lenses in contact acting as a single lens whose power is the sum](figures/lens_power_combination/lenses-in-contact.svg "The sign of the power says which way the lens bends light; its size says how strongly. In contact, the two simply add.")

Now put two thin lenses of focal lengths $f_1$ and $f_2$ **in contact**. Treat the image made by the first as the object for the second, and the algebra gives

$$\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2}, \qquad\text{that is}\qquad P = P_1 + P_2$$

Powers add, with their signs. That is the whole reason the dioptre exists: it turns a fiddly reciprocal sum into an addition you can do in your head, and it extends to any number of lenses, $P = P_1 + P_2 + P_3 + \dots$

The condition matters. The lenses must be **thin** and **touching**; separate them by a distance $d$ and the rule changes to $P = P_1 + P_2 - d\,P_1 P_2$, which is why a telescope is not simply the sum of its two lenses.

This is Tanvi's answer. Pressed against her spectacle lens, the magnifier's positive power and her lens's negative power added to something smaller than the magnifier alone. Held on its own, the magnifier kept its full strength.

## Worked example

**Given:** a magnifier of power $+8.0\,\text{D}$ held in contact with a spectacle lens of power $-3.0\,\text{D}$.
**Find:** the power and focal length of the pair.

**Step 1 — add the powers, signs included.**

$$P = (+8.0) + (-3.0) = +5.0\,\text{D}$$

Still positive, so the pair still converges — the diverging lens has weakened it, not reversed it.

**Step 2 — turn that back into a focal length.**

$$f = \frac{1}{P} = \frac{1}{5.0\,\text{m}^{-1}} = 0.20\,\text{m} = 20\,\text{cm}$$

**Sanity check:** the magnifier alone is $f = 1/8.0 = 0.125\,\text{m}$, about $12.5\,\text{cm}$. Adding a diverging lens should stretch the focus further away, and $20\,\text{cm}$ is indeed further than $12.5\,\text{cm}$ — roughly the length of your hand rather than the width of your palm.

## Where the picture breaks

"In contact" is an idealisation. Tanvi's magnifier rests on the curved front of her spectacle lens, so their centres are a few millimetres apart, and strictly the combination is slightly different from $P_1 + P_2$. For a rough answer the gap is ignorable; for a camera or a telescope, where lenses sit centimetres apart, it is not — there the separation term dominates the design.

The power also says nothing about image quality. Two lenses adding to $+5.0\,\text{D}$ may give a much sharper image than one lens of $+5.0\,\text{D}$, because the second lens can be chosen to cancel the first one's colour spreading. That is how a camera's "lens" ends up containing a dozen elements.

And the cricket is a setting here, not an analogy. Nothing about lens powers resembles adding runs or wickets; the only thing being added is the reciprocal of a focal length.

## Key takeaway

Power $P = 1/f$ with $f$ in metres, measured in dioptres, is the useful way to describe a lens: positive for converging, negative for diverging, bigger for stronger. Thin lenses in contact combine by simple addition, $P = P_1 + P_2$ — which is the same statement as $1/F = 1/f_1 + 1/f_2$, but far easier to use.
