---
concept_id: magnetic_flux
interest: smartphones
format: explain
title: The phone that stops charging when you stand it up
check:
  question: |-
    A flat receiver coil of area $40\,\text{cm}^2$ sits in a uniform magnetic field of $0.05\,\text{T}$. The coil is tilted so that its **plane** makes an angle of $30^\circ$ with the field. What is the magnetic flux through it?
  options:
    A: |-
      $2\times10^{-4}\,\text{Wb}$
    B: |-
      $1.7\times10^{-4}\,\text{Wb}$
    C: |-
      $1\times10^{-4}\,\text{Wb}$
    D: |-
      $1\,\text{Wb}$
  answer: C
  explanation: |-
    The angle in $\Phi = BA\cos\theta$ is measured from the **normal**. The plane is at $30^\circ$ to the field, so the normal is at $60^\circ$: $\Phi = 0.05 \times 0.004 \times \cos 60^\circ = 1\times10^{-4}\,\text{Wb}$.
  misconceptions:
    A: |-
      Uses $\Phi = BA$ and ignores the tilt; that maximum value only applies when the field runs along the normal to the coil.
    B: |-
      Puts the angle between the field and the **plane** into $\cos\theta$ ($\cos 30^\circ$); the angle must be measured from the normal, which here is $60^\circ$.
    D: |-
      Forgets to convert $40\,\text{cm}^2$ to $0.004\,\text{m}^2$, so the answer comes out ten thousand times too big.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk at night with a phone lying on a wireless charging pad, a shake torch, a hand-crank charger, wired earbuds and a coin beside the pad](scenes/smartphones/electromagnetic_induction.svg "Every gadget on this desk works because a magnetic field is changing somewhere inside it. This lesson starts with the phone on the pad.")

Ananya's online physics class starts in two minutes and her phone is at nine per cent. She drops it on the wireless charging pad, the little lightning bolt appears, and she relaxes.

Then she realises she can't see the teacher's slides lying flat. So she stands the phone up on its long edge, leaning it against her pen stand, its bottom edge still resting right in the middle of the pad.

The lightning bolt disappears.

She lays it flat again: charging. Stands it up: nothing. The phone is still touching the pad. It is still sitting in the pad's magnetic field — the same pad, the same field, the same distance, give or take a few centimetres. The only thing she changed is which way the phone is *facing*.

Why should a charger care which way a phone faces?

## The physics

The pad contains a flat coil that fills the space above it with a magnetic field. The phone contains a second flat coil, just under its back cover. What matters for charging is how much of the pad's field passes **through** the phone's coil — the **magnetic flux**.

For a flat surface of area $A$ in a uniform field $\vec{B}$, the magnetic flux is

$$\Phi_B = \vec{B}\cdot\vec{A} = BA\cos\theta$$

- $B$ is the magnetic field strength, in tesla (T).
- $A$ is the area of the surface, in $\text{m}^2$. The area vector $\vec{A}$ points along the **normal** — the line sticking straight out of the surface.
- $\theta$ is the angle between $\vec{B}$ and that normal.
- $\Phi_B$ is a scalar, measured in **weber** (Wb), with $1\,\text{Wb} = 1\,\text{T}\,\text{m}^2$.

A helpful picture: flux counts the field lines threading the loop.

![Three panels showing a flat loop edge-on in a uniform field at 0, 60 and 90 degrees, with the flux falling from BA to half of BA to zero](figures/magnetic_flux/flux-vs-tilt.svg "Same field, same loop, only the tilt changes: the flux falls to half at 60 degrees and to zero when the field skims along the plane of the loop.")

Now map it onto Ananya's desk. Near the middle of the pad the field points roughly straight up. Lying flat, the phone's coil faces it squarely: its normal points up too, $\theta \approx 0^\circ$, $\cos\theta \approx 1$, maximum flux. Standing on its edge, the coil's normal points sideways, $\theta \approx 90^\circ$, $\cos\theta \approx 0$ — the field lines slide past the coil instead of through it.

This formula assumes a **uniform** field over a **flat** surface. If $\vec{B}$ varies across the surface, you add up $\vec{B}\cdot d\vec{A}$ piece by piece instead.

Notice the list hiding in the formula. Flux can change in exactly three ways: change $B$, change $A$, or change $\theta$. The rest of this chapter is about what happens when one of them does.

## Worked example

**Given:** a phone's receiver coil of area $A = 0.002\,\text{m}^2$ (a circle about $5\,\text{cm}$ across) in a uniform field of, say, $B = 0.01\,\text{T}$ pointing straight up.
**Find:** the flux when the phone lies flat, and when it is tipped up to $\theta = 60^\circ$.

**Step 1 — lying flat.** The coil faces the field squarely, so $\theta = 0$ and $\cos 0 = 1$:

$$\Phi_B = BA = 0.01 \times 0.002 = 2\times10^{-5}\,\text{Wb}$$

This is the most flux this coil can ever catch in this field.

**Step 2 — tipped to $60^\circ$.** Now $\cos 60^\circ = 0.5$:

$$\Phi_B = BA\cos 60^\circ = 2\times10^{-5} \times 0.5 = 1\times10^{-5}\,\text{Wb}$$

Half the flux — and the coil is still sitting in exactly the same field.

**Sanity check:** tip the phone all the way up to $90^\circ$ and $\cos 90^\circ = 0$, so the flux must fall to zero; $1\times10^{-5}\,\text{Wb}$ sits sensibly halfway between the flat and the upright case.

## Where the picture breaks

A real pad's field is **not uniform** and does not point straight up everywhere: it spreads out and curves back around the edges of the pad's coil. That is why an upright phone may still catch a little flux, and why a phone slid off-centre charges badly even when flat.

The pad's field is also not steady. It alternates, reversing direction over a hundred thousand times a second, and it is the *changing* flux that charges the phone — the subject of the next lesson. The worked example treats one instant, as if the field were frozen.

And "counting field lines" is only a picture. We draw the lines, and we could always draw twice as many. Flux is the quantity $BA\cos\theta$; the lines just help you feel it.

## Key takeaway

Magnetic flux through a flat surface is $\Phi_B = BA\cos\theta$, in weber, where $\theta$ is the angle between the field and the **normal** to the surface. It is largest when the surface faces the field squarely and zero when the field skims along it. Flux can change in only three ways: change $B$, change $A$, or turn the surface.
