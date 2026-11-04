---
concept_id: davisson_germer
interest: gaming
format: explain
title: The fence glitch and the nickel crystal
check:
  question: |-
    As Davisson and Germer swung their detector round the arc, the electron count rose to a sharp maximum at one particular scattering angle and fell away on either side of it. Which feature of that result is the one that particles alone cannot produce?
  options:
    A: |-
      That electrons reached the detector at all after striking the nickel target.
    B: |-
      That more electrons arrived once the accelerating voltage was increased.
    C: |-
      That the electrons piled up at one preferred angle — a maximum built by scattered waves reinforcing each other.
    D: |-
      That the beam was deflected by the nickel instead of passing straight through it.
  answer: C
  explanation: |-
    Little bullets bouncing off a surface would give a count that falls away smoothly with angle. A sharp maximum at one angle, with fewer arrivals on either side, is a diffraction maximum, and only waves reinforcing along particular directions make those.
  misconceptions:
    A: |-
      Mistakes ordinary scattering for the discovery. Particles bounce off surfaces all the time; the result that mattered was *which directions* they preferred.
    B: |-
      Confuses the accelerating voltage with the beam's intensity. How many electrons leave the gun is set by the heated filament; the voltage sets their energy, and therefore their wavelength and where the peak appears.
    D: |-
      Treats deflection itself as the proof. A hard sphere deflects too — what a sphere cannot do is produce a maximum at one angle and a shortage beside it.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming room shown in three stages: a cut-away retro CRT cabinet with a glowing filament and an electron beam, a flat monitor whose light leaves as a wave and then as packets, and a camera sensor feeding a current to a meter](scenes/gaming/dual_nature.svg "Every claim in this chapter so far has been an argument. This lesson is about the measurement that settled one.")

Zoya is testing her team's build, walking her character slowly towards a wire fence, when the fence stops behaving. At one particular distance the diamonds of the mesh dissolve into broad dark and bright bands that crawl sideways as she moves. Two steps closer and it is an ordinary fence again.

"Bug," says her teammate, and writes it down.

Zoya is not convinced. The bands only appear when the fence's pattern has shrunk on screen to roughly the spacing of the pixels — two regular spacings, nearly matching, and a third pattern nobody drew emerging from the pair.

She mentions it in class on Monday. Her physics teacher laughs: the rule she has stumbled onto — that something new appears only when two regular spacings are comparable — is exactly why a laboratory in 1927 had to fire electrons at a lump of nickel instead of at any grating anyone has ever ruled.

Zoya cannot see the connection. What does a fence in a game have to do with an electron?

## The physics

De Broglie's claim was testable in principle: send electrons at a grating whose spacing is comparable to $\lambda$ and they must diffract. The problem is the number. Electrons of a few tens of electron volts have $\lambda$ of about $0.1\,\text{nm}$, and no grating has ever been ruled that finely. The only rulings that fine are nature's own — the planes of atoms inside a crystal.

Clinton Davisson and Lester Germer were not looking for this. They were studying how electrons bounce off a nickel target when, in 1925, a bottle of liquid air burst and let air into their vacuum tube. The hot nickel oxidised. To clean it they baked the target long and hot, and the baking turned the many tiny crystals of the original block into a few large ones. From then on the target was effectively a single crystal, and the scattered electrons began doing something new.

![The Davisson-Germer apparatus: an electron gun firing a beam down onto a nickel crystal, with a detector on a movable arc measuring electrons scattered at an angle phi](figures/davisson_germer/apparatus.svg "Three things under the experimenters' control: the accelerating voltage, the angle of the detector, and nothing else.")

The apparatus, all in vacuum, is simple. A heated filament releases electrons by thermionic emission — the same process as in the club's old picture tube. An accelerating voltage $V$ gives each electron kinetic energy $eV$, a collimator narrows the beam, and it strikes the crystal face. A detector swinging along a circular arc counts the electrons arriving at each scattering angle $\varphi$.

If electrons were simply little bullets, that count would fall away smoothly as the detector moved round. Instead, at $V = 54\,\text{V}$, a sharp bump appeared at $\varphi = 50^\circ$ — a direction the electrons clearly preferred. That is a diffraction maximum, and only waves make those.

![Two parallel waves scattering from atoms in successive crystal planes, showing the extra path length two d sine theta travelled by the deeper one](figures/davisson_germer/crystal-planes-interference.svg "Waves scattered from successive planes reinforce only where the extra path is a whole number of wavelengths. That is why the count peaks at one particular angle.")

Waves scattered from successive atomic planes a distance $d$ apart differ in path by $2d\sin\theta$, where $\theta$ is measured from the planes, and they reinforce when $2d\sin\theta = n\lambda$. For nickel $d = 0.091\,\text{nm}$, and this geometry puts $\theta = 65^\circ$ when $\varphi = 50^\circ$, so the *measured* wavelength was

$$\lambda = 2d\sin\theta = 2 \times 0.091 \times \sin 65^\circ = 0.165\,\text{nm}$$

That number came entirely out of an angle and a crystal spacing. Not one part of it used de Broglie's formula — which is exactly what makes it a test of it.

![Two men in suits standing beside laboratory apparatus](famous/davisson-and-germer.jpg "Clinton Davisson (left) and Lester Germer with their apparatus, 1927. Their electron beam scattered off a nickel crystal into a pattern only waves can make. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** electrons accelerated from rest through $V = 54\,\text{V}$.
**Find:** the de Broglie wavelength predicted for them, and how it compares with the $0.165\,\text{nm}$ the diffraction angle measured.

Use the shortcut from the previous lesson, $\lambda = 1.227/\sqrt{V}$ nm:

$$\lambda = \frac{1.227}{\sqrt{54}} = \frac{1.227}{7.35} = 0.167\,\text{nm}$$

That is the prediction — built from Planck's constant, the electron's mass and its charge, and nothing else.

Now compare it with the measurement. The two differ by $0.002\,\text{nm}$:

$$\frac{0.002}{0.165} \approx 1\%$$

Two numbers reached by completely separate routes agree to within one per cent.

**Sanity check:** the predicted wavelength comes out at about the spacing between atoms, which is precisely why a crystal, and nothing coarser, was able to reveal it.

## Where the picture breaks

Be honest about the frame. Zoya's fence bands are **moiré**, a beat between the fence's spacing and the pixel grid, produced by sampling rather than by waves reinforcing. No electron is involved and no interference takes place. One rule carries over, and only one: a new pattern appears when two regular spacings are comparable. That rule is why a crystal works as an electron grating and a ruled one does not.

The model has limits too. Treating the crystal as a stack of mirrors is convenient, but the beam penetrates several atomic layers and scatters from the whole three-dimensional lattice, and the baked nickel was a few large crystals rather than one perfect one, so the peaks were broad. And the experiment measures a *wavelength* — it never shows an electron spread out. The detector counts arrivals one at a time, and the pattern is what they add up to.

In the same year, independently and by a different method, G. P. Thomson sent faster electrons through thin metal foils and got diffraction rings. The two shared the 1937 Nobel Prize in Physics.

## Key takeaway

Davisson and Germer fired electrons of a known energy at a nickel crystal and found a sharp peak in the scattered beam at one particular angle — diffraction, which particles cannot do. Reading the wavelength off that angle gave $0.165\,\text{nm}$, against de Broglie's predicted $0.167\,\text{nm}$ for $54\,\text{V}$ electrons. Matter waves stopped being a proposal and became a measurement.
