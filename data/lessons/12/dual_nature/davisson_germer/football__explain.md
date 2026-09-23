---
concept_id: davisson_germer
interest: football
format: explain
title: The broken bottle that proved electrons are waves
check:
  question: |-
    What makes the Davisson-Germer result *evidence for de Broglie's hypothesis*, rather than just an interesting scattering measurement?
  options:
    A: |-
      The electrons were scattered by a metal target, which shows that electrons and metals interact.
    B: |-
      The count of scattered electrons fell away smoothly as the detector was swung round, just as a stream of particles would.
    C: |-
      The peak appeared only at one accelerating voltage, which shows that electrons can exist only at certain energies.
    D: |-
      The wavelength read off the diffraction angle matched the $h/p$ predicted from the voltage, by two independent routes.
  answer: D
  explanation: |-
    The angle and the crystal spacing give a wavelength using only $2d\sin\theta = n\lambda$, with no reference to de Broglie. Comparing that measured wavelength with $h/\sqrt{2meV}$ is a genuine test, and the two agreed.
  misconceptions:
    A: |-
      Mistakes the apparatus for the result. Any electron beam interacts with a metal; what mattered was the *pattern* of the scattering, not that scattering happened.
    B: |-
      Describes what particles would have done, which is the opposite of what was seen. A smooth fall-off with angle is exactly the result that would have refuted de Broglie.
    C: |-
      Reads the special voltage as a property of electrons instead of the geometry. Electrons in a beam can be given any energy you like; $54\,\text{V}$ simply happened to place a strong maximum at a convenient angle.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night, with an inset panel drawing the same beam once as a wave and once as a stream of packets, a goal-line camera on a pole, a goalkeeper and a ball](scenes/football/dual_nature.svg "Every claim in this chapter so far has been an argument. This lesson is about the measurement that settled one.")

A valve on the training-ground sprinklers stuck open on a Friday night, and by Saturday morning one corner of Nitya's pitch was a swamp while the rest was bone dry. Then the sun came out hard and baked that corner flat.

Nobody planned any of it. But for the next fortnight the ball skidded low off that patch instead of sitting up, and her coach — who had been complaining about the surface for two seasons — finally worked out what the difference actually was. A broken valve taught him more than the groundsman's reports had.

Her physics teacher, hearing the story on Monday, laughed and said it reminded him of the most productive accident in the history of physics: a bottle broke in a laboratory in 1925, and two years later the wreckage had proved that electrons are waves.

Nitya could not see it. How does breaking a bottle prove anything about an electron?

## The physics

De Broglie's claim was testable in principle: fire electrons at a grating whose spacing is comparable to $\lambda$ and they must diffract. The catch is the number. Electrons of a few tens of electronvolts have $\lambda$ near $0.1\,\text{nm}$, and no grating has ever been ruled that finely. The only rulings that fine are the ones nature makes — the planes of atoms inside a crystal.

Clinton Davisson and Lester Germer were not looking for this. They were studying how electrons bounce off a nickel target when, in 1925, a bottle of liquid air burst and let air into their vacuum tube. The hot nickel oxidised. To clean it they baked the target for a long time at high temperature — and the baking turned the many tiny crystals of the original block into a few large ones. From then on their target was effectively a single crystal, and the scattered electrons began doing something new.

![The Davisson-Germer apparatus: an electron gun firing a beam down onto a nickel crystal, with a detector on a movable arc measuring electrons scattered at an angle phi](figures/davisson_germer/apparatus.svg "Three things under the experimenters' control: the accelerating voltage, the angle of the detector, and nothing else.")

The apparatus, all in vacuum, is simple. A heated filament releases electrons by thermionic emission; an accelerating voltage $V$ gives each of them kinetic energy $eV$; a collimator makes a narrow beam; the beam strikes the crystal face. A detector that swings along a circular arc counts the electrons arriving at each scattering angle $\varphi$.

If electrons were simply small bullets, the count would fall away smoothly as the detector moved round. Instead, at $V = 54\,\text{V}$, a sharp bump appeared at $\varphi = 50^\circ$ — a direction the electrons clearly preferred. That is a diffraction maximum, and only waves make those.

![Two parallel waves scattering from atoms in successive crystal planes, showing the extra path length two d sine theta travelled by the deeper one](figures/davisson_germer/crystal-planes-interference.svg "Waves scattered from successive planes reinforce only where the extra path is a whole number of wavelengths. That is why the count peaks at one particular angle.")

Waves scattered from successive atomic planes a distance $d$ apart differ in path by $2d\sin\theta$, with $\theta$ measured from the planes, and they reinforce when $2d\sin\theta = n\lambda$. For nickel $d = 0.091\,\text{nm}$, and this geometry puts $\theta = 65^\circ$ when $\varphi = 50^\circ$, so the *measured* wavelength was

$$\lambda = 2d\sin\theta = 2 \times 0.091 \times \sin 65^\circ = 0.165\,\text{nm}$$

That number came entirely from an angle and a crystal spacing. Not one part of it used de Broglie's formula — which is exactly what makes it a test of it.

![Two men in suits standing beside laboratory apparatus](famous/davisson-and-germer.jpg "Clinton Davisson (left) and Lester Germer with their apparatus, 1927. Their electron beam scattered off a nickel crystal into a pattern only waves can make. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** the diffraction measured a wavelength of $0.165\,\text{nm}$.

**Find:** the accelerating voltage de Broglie's relation says would produce it, and how that compares with the $54\,\text{V}$ actually used.

Start from the shortcut of the previous lesson, $\lambda = 1.227/\sqrt{V}$ nm, and turn it round to give the voltage:

$$V = \left(\frac{1.227}{\lambda}\right)^2$$

Substituting the measured wavelength in nanometres:

$$V = \left(\frac{1.227}{0.165}\right)^2 = (7.44)^2 \approx 55\,\text{V}$$

Now compare. The experimenters had set their supply to $54\,\text{V}$, so the theory's answer and the dial on the bench agree to within about one volt — under $3\%$.

**Sanity check:** two numbers reached by completely separate routes — one from a scattering angle and a crystal spacing, the other from Planck's constant and the electron's mass and charge — landing within a few per cent of each other is not something a coincidence does.

## Where the picture breaks

Be honest about the frame of this lesson: football supplies its *shape* — an accident that taught somebody something — and nothing more. No part of a pitch diffracts electrons, and a baked-dry corner has nothing to do with crystal planes. Where physics genuinely lives in this chapter is in the cameras and sensors of the earlier lessons; here it lives only in a laboratory.

The model has limits too. Treating the crystal as a stack of mirrors is a convenient picture; the beam actually penetrates several atomic layers and scatters from the full three-dimensional lattice. The baked nickel was a few large crystals rather than one perfect one, so the peaks were broader than an X-ray pattern's. And the experiment measures a *wavelength* — it never shows you an electron spread out. The detector counts arrivals, one at a time, and the pattern is what those arrivals add up to.

In the same year, working independently and quite differently, G. P. Thomson sent faster electrons through thin metal foils and got diffraction rings. The two shared the 1937 Nobel Prize in Physics.

## Key takeaway

Davisson and Germer fired electrons of a known energy at a nickel crystal and found a sharp peak in the scattered beam at one particular angle — diffraction, which particles cannot do. The wavelength read off that angle, $0.165\,\text{nm}$, corresponds to an accelerating voltage of about $55\,\text{V}$, against the $54\,\text{V}$ they had actually applied. Matter waves stopped being a proposal and became a measurement.
