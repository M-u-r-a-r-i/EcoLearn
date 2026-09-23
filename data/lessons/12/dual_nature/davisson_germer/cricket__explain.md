---
concept_id: davisson_germer
interest: cricket
format: explain
title: The broken bottle that proved electrons are waves
check:
  question: |-
    In the Davisson-Germer experiment the electron beam was fired at a nickel crystal rather than at a finely ruled grating. Why?
  options:
    A: |-
      Its atoms are spaced about $0.1\,\text{nm}$ apart, matching the electrons' wavelength, which no ruled grating comes close to.
    B: |-
      Nickel is a metal, so it supplies the electrons that the detector goes on to count.
    C: |-
      A crystal reflects electrons cleanly, whereas a ruled grating would simply absorb them.
    D: |-
      A crystal surface is far smoother, so the beam is not scattered off in random directions.
  answer: A
  explanation: |-
    Diffraction only shows up when the spacing of the scatterers is comparable to the wavelength. Electrons at $54\,\text{V}$ have $\lambda \approx 0.17\,\text{nm}$, and the atomic planes of a crystal are the only regularly spaced structure that fine.
  misconceptions:
    B: |-
      Confuses the target with the source. The electrons come from the heated filament in the gun; the nickel's only job is to scatter the beam that arrives.
    C: |-
      Treats the effect as ordinary reflection. Any smooth surface reflects a beam; what makes a crystal special is a regular repeat at the right spacing, which lets the scattered waves interfere.
    D: |-
      Thinks the result depends on surface polish. Diffraction depends on the regular spacing of the scattering centres, not on how smooth the surface looks.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit cricket ground at night, with a light beam drawn half as a wave and half as a stream of packets, an umpire holding a light meter and a tracking camera on a tripod](scenes/cricket/dual_nature.svg "Every claim in this chapter so far has been an argument. This lesson is about the measurement that settled one.")

Rain stopped play at Meghna's school match with the scores level, and the ground staff got the covers on late. One end of the square took the shower; then the sun came out hard for an hour and baked the wet patch dry.

When play restarted the ball began to grip and turn off that patch, sharply and unmistakably. The spinners had a wonderful afternoon. Nobody had planned any of it — a mistake with the covers had produced a surface nobody would have dared prepare on purpose.

Her coach called it a fluke and forgot about it. Her physics teacher, hearing the story on Monday, laughed and said it reminded him of the most productive accident in the history of physics: a bottle broke in a laboratory in 1925, and two years later the wreckage had proved that electrons are waves.

Meghna could not see the connection. How does breaking a bottle prove anything about an electron?

## The physics

De Broglie's claim was testable in principle: fire electrons at a grating whose spacing is comparable to $\lambda$ and they must diffract. The catch is the number. Electrons of a few tens of electron volts have $\lambda$ of about $0.1\,\text{nm}$, and no grating has ever been ruled that finely. The only rulings that fine are the ones nature makes: the planes of atoms inside a crystal.

Clinton Davisson and Lester Germer were not looking for this. They were studying how electrons bounce off a nickel target when, in 1925, a bottle of liquid air burst and let air into their vacuum tube. The hot nickel oxidised. To clean it they baked the target for a long time at high temperature — and the baking turned the many tiny crystals of the original block into a few large ones. From then on, their target was effectively a single crystal, and the scattered electrons started doing something new.

![The Davisson-Germer apparatus: an electron gun firing a beam down onto a nickel crystal, with a detector on a movable arc measuring electrons scattered at an angle phi](figures/davisson_germer/apparatus.svg "Three things under the experimenters' control: the accelerating voltage, the angle of the detector, and nothing else.")

The apparatus, in vacuum, is simple: a heated filament releases electrons by thermionic emission, an accelerating voltage $V$ gives each of them kinetic energy $eV$, a collimator makes a narrow beam, and the beam strikes the crystal face. A detector that can be swung along a circular arc counts the electrons arriving at each scattering angle $\varphi$.

If electrons were simply little bullets, the count would fall away smoothly as the detector moved round. Instead, at $V = 54\,\text{V}$, a sharp bump appeared at $\varphi = 50^\circ$ — a direction the electrons clearly preferred. That is a diffraction maximum, and only waves make those.

![Two parallel waves scattering from atoms in successive crystal planes, showing the extra path length two d sine theta travelled by the deeper one](figures/davisson_germer/crystal-planes-interference.svg "Waves scattered from successive planes reinforce only where the extra path is a whole number of wavelengths. That is why the count peaks at one particular angle.")

Waves scattered from successive atomic planes a distance $d$ apart differ in path by $2d\sin\theta$, where $\theta$ is measured from the planes, and they reinforce when $2d\sin\theta = n\lambda$. For nickel, $d = 0.091\,\text{nm}$, and this geometry puts $\theta = 65^\circ$ when $\varphi = 50^\circ$. So the *measured* wavelength was

$$\lambda = 2d\sin\theta = 2 \times 0.091 \times \sin 65^\circ = 0.165\,\text{nm}$$

That number came entirely from angles and crystal spacing. Not one part of it used de Broglie's formula. So it can be used to test it.

## Worked example

**Given:** electrons accelerated from rest through $V = 54\,\text{V}$.
**Find:** the de Broglie wavelength predicted for them, and how it compares with the $0.165\,\text{nm}$ the diffraction measured.

Use the shortcut from the previous lesson, $\lambda = 1.227/\sqrt{V}$ nm:

$$\lambda = \frac{1.227}{\sqrt{54}} = \frac{1.227}{7.35} = 0.167\,\text{nm}$$

That is the prediction — made from Planck's constant, the electron's mass and charge, and nothing else.

Now compare. The measurement gave $0.165\,\text{nm}$, so the two differ by $0.002\,\text{nm}$:

$$\frac{0.002}{0.165} \approx 1\%$$

Two numbers arrived at by completely separate routes agree to within one per cent.

**Sanity check:** the predicted wavelength is about the spacing between atoms, which is exactly why a crystal — and nothing coarser — was able to reveal it.

## Where the picture breaks

Be honest about the frame of the story: cricket supplies the shape of this lesson, an accident that taught somebody something, and nothing more. No part of a cricket ground diffracts electrons, and the grip off a dry patch has nothing to do with crystal planes. Where physics genuinely lives in this chapter is in the light meters and cameras of the earlier lessons; here it lives only in a laboratory.

The model has limits too. Treating the crystal as a stack of mirrors is a convenient picture; the beam actually penetrates several atomic layers and scatters from the full three-dimensional lattice, and the baked nickel was a few large crystals rather than one perfect one, so the peaks were broader than an X-ray pattern's. And the experiment measures a wavelength — it never shows you an electron spread out. What the detector does is count arrivals, one at a time, and the pattern is what those arrivals add up to.

In the same year, working independently and with a quite different method, G. P. Thomson sent faster electrons through thin metal foils and got diffraction rings. The two shared the 1937 Nobel Prize in Physics.

## Key takeaway

Davisson and Germer fired electrons of a known energy at a nickel crystal and found a sharp peak in the scattered beam at one particular angle — diffraction, which particles cannot do. Reading the wavelength off that angle gave $0.165\,\text{nm}$, against de Broglie's predicted $0.167\,\text{nm}$ for $54\,\text{V}$ electrons. Matter waves stopped being a proposal and became a measurement.
