---
concept_id: davisson_germer
interest: smartphones
format: explain
title: A grid of dots from a phone screen, and the crystal that did it for electrons
check:
  question: |-
    In the Davisson-Germer experiment, which feature of the data showed that the electrons were behaving as waves?
  options:
    A: |-
      The detector picked up scattered electrons at every angle, showing that the beam had spread out like a wave.
    B: |-
      At $54\,\text{V}$ the count of scattered electrons peaked sharply at one angle, $50^\circ$, where waves from successive atomic planes reinforce.
    C: |-
      The scattered electrons came away from the nickel with less energy than they arrived with, as a wave loses energy when it spreads.
    D: |-
      The nickel gave out electrons only above a certain accelerating voltage, like the threshold in the photoelectric effect.
  answer: B
  explanation: |-
    Particles bouncing off a surface would give a count that changes smoothly with angle. A sharp peak at one angle is a diffraction maximum, which only interfering waves produce, and the wavelength read from it matched $h/p$.
  misconceptions:
    A: |-
      Takes spreading as proof of waves. Particles scattered off atoms also go off in all directions; what only waves do is pick out particular angles where they reinforce.
    C: |-
      Imagines a wave losing energy as the evidence. The key electrons were scattered with their energy essentially unchanged; the evidence was where they went, not how much energy they had.
    D: |-
      Mixes this experiment up with the photoelectric effect. The electrons came from a heated filament and were fired at the nickel; the nickel only scattered them.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A phone beside a sunny window, its screen showing a UV-index meter, its flashlight beam drawn half as a wave and half as a stream of packets, and a magnified camera pixel where light frees electrons](scenes/smartphones/dual_nature.svg "The screen of a phone is a grid of tiny, evenly spaced pixels. To a light wave, that grid is a grating.")

Pooja's elder brother Varun has a red laser pointer left over from a college presentation. One evening in their flat in Lucknow he switches off the lights, lays his phone flat on the table, and shines the laser onto its dark screen at a slant — carefully, never towards anyone's eyes.

On the wall, instead of one red spot, a neat grid of red dots appears, like a tiny constellation.

"The screen is a grid of pixels, all the same distance apart," Varun explains. "Light bouncing off a regular grid only goes out strongly in certain directions. That's how you know light is a wave. Measure the dot spacing and you can even work out the pixel spacing."

Pooja is half-listening; she is revising for her Class 12 exam, where a whole chapter claims that electrons are waves too.

"Then do this with electrons," she says. "Where would you even find a grid fine enough?"

## The physics

De Broglie predicted that an electron accelerated through a few tens of volts has a wavelength of about $0.1\,\text{nm}$. To show diffraction you need a regular grid with spacing near that — and nobody can make one. Nature can: in a crystal, the atoms sit in planes a fraction of a nanometre apart.

Clinton Davisson and Lester Germer were studying electrons scattered off nickel when, in 1925, a bottle of liquid air burst and let air into their vacuum tube. The hot nickel oxidised. Cleaning it meant baking it for a long time at high temperature, which turned the many tiny crystals of their target into a few large ones. After that, their electrons began to behave differently.

![The Davisson-Germer apparatus: an electron gun firing a beam down onto a nickel crystal, with a detector on a movable arc measuring electrons scattered at an angle phi](figures/davisson_germer/apparatus.svg "Three things under the experimenters' control: the accelerating voltage, the angle of the detector, and nothing else.")

The set-up is in vacuum. A heated filament frees electrons (thermionic emission), an accelerating voltage $V$ gives each one kinetic energy $eV$, and a narrow beam strikes the crystal face. A detector swings round a circular arc and counts the electrons scattered at each angle $\varphi$.

Particles bouncing off atoms would give a count that changes smoothly with angle. Instead, at $V = 54\,\text{V}$, there was a sharp peak at $\varphi = 50^\circ$. A peak like that is a diffraction maximum: the same kind of thing as each red dot on Varun's wall.

![Two parallel waves scattering from atoms in successive crystal planes, showing the extra path length two d sine theta travelled by the deeper one](figures/davisson_germer/crystal-planes-interference.svg "Waves scattered from successive planes reinforce only where the extra path is a whole number of wavelengths. That is why the count peaks at one particular angle.")

Waves scattered from planes a distance $d$ apart travel paths that differ by $2d\sin\theta$ ($\theta$ measured from the planes). They reinforce when

$$2d\sin\theta = n\lambda$$

For this nickel crystal, $d = 0.091\,\text{nm}$, and the geometry makes $\theta = 65^\circ$ when $\varphi = 50^\circ$.

![Two men in suits standing beside laboratory apparatus](famous/davisson-and-germer.jpg "Clinton Davisson (left) and Lester Germer with their apparatus, 1927. The peak in their scattered electron count was the first direct sign of a matter wave. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** the peak at $54\,\text{V}$, with $d = 0.091\,\text{nm}$ and $\theta = 65^\circ$ (first order, $n = 1$).
**Find:** the measured wavelength, and compare it with de Broglie's prediction.

The measurement first, from angles and spacing alone:

$$\lambda = 2d\sin\theta = 2\times0.091\times\sin65^\circ \approx 0.165\,\text{nm}$$

No part of this used de Broglie's formula — it is what the crystal says.

The prediction, from $\lambda = 1.227/\sqrt{V}$ nm:

$$\lambda = \frac{1.227}{\sqrt{54}} \approx 0.167\,\text{nm}$$

That used only Planck's constant and the electron's mass and charge.

The difference is $0.002\,\text{nm}$, about $1\%$. Two completely separate routes land on the same number.

**Sanity check:** both answers are about the spacing between atoms, which is why a crystal, and nothing coarser, could reveal the wave.

## Where the picture breaks

Varun's screen and the nickel crystal do the same job, but the screen works as a flat grid while a crystal is three-dimensional; the electrons scatter from many layers of atoms, and the "stack of mirrors" picture is a simplification. The baked nickel was also a few large crystals, not one perfect one, so the peak was broader than an ideal one.

The phone is a frame for this story, not part of the physics: a pixel grid diffracts light, whose wavelength is thousands of times longer, and would do nothing visible to electrons.

And the detector never saw a spread-out electron. It counted electrons arriving one by one; the peak is what those arrivals add up to. In the same year, G. P. Thomson sent faster electrons through thin metal foils and saw diffraction rings. He and Davisson shared the 1937 Nobel Prize in Physics.

## Key takeaway

Davisson and Germer fired $54\,\text{V}$ electrons at a nickel crystal and found a sharp peak in the scattered count at $50^\circ$ — a diffraction maximum, which only waves produce. The wavelength read from the crystal, $0.165\,\text{nm}$, agreed with de Broglie's $h/p$ prediction of $0.167\,\text{nm}$ to about one per cent. Matter waves became a measurement.
