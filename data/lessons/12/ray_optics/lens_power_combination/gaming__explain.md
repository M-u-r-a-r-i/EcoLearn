---
concept_id: lens_power_combination
interest: gaming
format: explain
title: What a prescription insert does to a headset lens
check:
  question: |-
    A headset lens of focal length $+5.0\,\text{cm}$ is used in contact with a prescription insert of power $-5.0\,\text{D}$. What is the power of the combination?
  options:
    A: |-
      $+15\,\text{D}$
    B: |-
      $+25\,\text{D}$
    C: |-
      $-6.7\,\text{D}$
    D: |-
      $-4.8\,\text{D}$
  answer: A
  explanation: |-
    The headset lens has $P_1 = 1/f = 1/0.050\,\text{m} = +20\,\text{D}$. Powers in contact add with their signs: $P = 20 - 5.0 = +15\,\text{D}$ — still converging, but weaker than the headset lens alone.
  misconceptions:
    B: |-
      Adds the sizes and ignores the minus sign. A diverging lens *subtracts* from the combination; that is precisely what a negative power means.
    C: |-
      Adds the focal lengths, $5\,\text{cm} + (-20\,\text{cm}) = -15\,\text{cm}$, and converts that. Focal lengths do not add; their reciprocals do, which is the whole reason opticians work in dioptres.
    D: |-
      Forgets that $f$ must be in metres, taking $P_1 = 1/5.0 = 0.2\,\text{D}$. A $5\,\text{cm}$ lens is a strong lens; $0.2\,\text{D}$ would be almost a flat sheet of glass.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk at night with a monitor, a coolant reservoir, a cut-away VR headset, a glass prism, a glowing optical cable, a hand lens over a controller board and a wall-mounted dome mirror](scenes/gaming/ray_optics.svg "The headset in the middle has one lens in the light path. Add a second one against it and the pair behaves as a single lens — with a power you can work out.")

Nikhil is short-sighted, and his optician wrote his prescription as "minus five" — not in centimetres, not in anything he recognised. He has never thought about it again.

Then the college VR club gets a headset, and a queue forms. Nikhil goes in wearing his glasses. The frames jam against the foam, the lenses scratch against the headset lenses, and the whole picture is soft and doubled at the edges. He takes the glasses off and the virtual world is a warm blur.

The club secretary hands him a small clip-on ring of plastic. "Prescription insert. Snaps on right against the headset lens. It's minus five, same as yours."

He clips it on and the world comes into focus, sharp to the edges — and, he notices, everything looks very slightly smaller than his friend reported seeing.

So the insert is not simply "his glasses in a different frame": pressed against the headset lens it has *become part of* the headset lens, and changed it. How do two lenses stuck together make one lens, and what is that shared "minus five" actually measuring?

## The physics

Focal length is a clumsy way to describe a lens, because a **strong** lens has a **small** $f$ and the numbers run backwards. So opticians and physicists use the reciprocal, the **power**:

$$P = \frac{1}{f} \qquad \text{with } f \text{ in metres}$$

The unit is the **dioptre**, symbol $\text{D}$, and $1\,\text{D} = 1\,\text{m}^{-1}$. Using the Cartesian convention, a converging (convex) lens has $f > 0$ and so $P > 0$; a diverging (concave) lens has $f < 0$ and so $P < 0$. Nikhil's "minus five" is a concave lens of $-5.0\,\text{D}$, focal length $-20\,\text{cm}$, which spreads the light slightly before it reaches his eye — the correction a short-sighted eye needs.

![Left: a convex lens converging parallel rays to a real focus with positive power, and a concave lens spreading them with negative power. Right: two thin lenses in contact acting as a single lens whose power is the sum](figures/lens_power_combination/lenses-in-contact.svg "The sign of the power says which way the lens bends light; its size says how strongly. In contact, the two simply add.")

Now put two thin lenses of focal lengths $f_1$ and $f_2$ **in contact**. Treat the image made by the first as the object for the second, and the algebra gives

$$\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2}, \qquad\text{that is}\qquad P = P_1 + P_2$$

Powers add, with their signs, and it extends to any number of lenses: $P = P_1 + P_2 + P_3 + \dots$ That is the whole reason the dioptre exists — it turns a fiddly sum of reciprocals into addition you can do in your head.

The conditions matter. The lenses must be **thin** and **touching**. Separate them by a distance $d$ and the rule becomes $P = P_1 + P_2 - d\,P_1 P_2$, which is why a telescope is not just the sum of its two lenses.

This is Nikhil's answer. Clipped on, the insert's negative power adds to the headset lens's positive power, and the pair is a weaker converging lens than the headset lens alone. Weaker means a longer focal length, which shifts where the image of the panel sits — and that is the slight change of scale he noticed.

## Worked example

**Given:** the headset lens has a focal length of $4.0\,\text{cm}$. The insert clipped flat against it has a power of $-5.0\,\text{D}$.
**Find:** the power and focal length of the pair.

**Step 1 — put the headset lens into dioptres.** Convert first: $f_1 = 4.0\,\text{cm} = 0.040\,\text{m}$, so

$$P_1 = \frac{1}{0.040\,\text{m}} = +25\,\text{D}$$

A strong converging lens, as it must be to sit a few centimetres from a screen.

**Step 2 — add the powers with their signs.**

$$P = (+25) + (-5.0) = +20\,\text{D}$$

Still positive, so the pair still converges; the insert has weakened it, not reversed it.

**Step 3 — back to a focal length.**

$$f = \frac{1}{P} = \frac{1}{20\,\text{m}^{-1}} = 0.050\,\text{m} = 5.0\,\text{cm}$$

**Sanity check:** adding a diverging lens should push the focus further out, and $5.0\,\text{cm}$ is indeed further than the original $4.0\,\text{cm}$ — a shift of about a fingernail's width, which is exactly the size of change that makes a virtual world look subtly rescaled.

## Where the picture breaks

"In contact" is an idealisation. The insert sits on the curved front of the headset lens, so their centres are a few millimetres apart, and strictly the pair is a little different from $P_1 + P_2$. For a rough answer the gap is ignorable; for lenses centimetres apart it is not, and there the separation term takes over.

Power also says nothing about image quality. Two lenses adding to $+20\,\text{D}$ can give a far sharper picture than one lens of $+20\,\text{D}$, because the second can be chosen to cancel the first one's colour spreading. That is why a good headset lens is a stack, not a single disc.

And a caution about eyes. Nikhil's prescription corrects *his* eye, which is itself a lens with its own power; the full optical chain is insert, headset lens and eye together. Treating the first two as one combined lens is right, but the eye is not simply a third term in the same sum — it sits a distance away, and it changes its own power when it focuses.

## Key takeaway

Power $P = 1/f$ with $f$ in metres, measured in dioptres, is the useful way to describe a lens: positive for converging, negative for diverging, bigger for stronger. Thin lenses in contact combine by plain addition, $P = P_1 + P_2$ — the same statement as $1/F = 1/f_1 + 1/f_2$, but far easier to use, and it is why a minus-five insert makes a headset lens measurably weaker.
