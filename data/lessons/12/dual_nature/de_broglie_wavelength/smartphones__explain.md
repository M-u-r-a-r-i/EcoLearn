---
concept_id: de_broglie_wavelength
interest: smartphones
format: explain
title: Why chip makers look at phone chips with electrons
check:
  question: |-
    An electron microscope accelerates electrons from rest through a potential difference $V$. The operator raises the voltage to $4V$. What happens to the electrons' de Broglie wavelength?
  options:
    A: |-
      It becomes one-quarter as long.
    B: |-
      It becomes four times as long.
    C: |-
      It stays the same, because the wavelength depends only on the electron's mass.
    D: |-
      It becomes half as long.
  answer: D
  explanation: |-
    The kinetic energy $eV$ goes up four times, so the momentum $p = \sqrt{2meV}$ doubles, and $\lambda = h/p$ halves. In short, $\lambda \propto 1/\sqrt{V}$.
  misconceptions:
    A: |-
      Treats $\lambda$ as inversely proportional to $V$. The wavelength depends on momentum, and momentum grows only as the square root of the kinetic energy.
    B: |-
      Gets the direction wrong, as if more energy meant a longer wave. Faster particles have more momentum and therefore a shorter wavelength.
    C: |-
      Thinks the wavelength is a fixed property of the particle, like its charge. It depends on how fast the particle is moving, through $\lambda = h/mv$.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A phone beside a sunny window, its screen showing a UV-index meter, its flashlight beam drawn half as a wave and half as a stream of packets, and a magnified camera pixel where light frees electrons](scenes/smartphones/dual_nature.svg "Light behaves as a wave and as packets. This lesson asks whether electrons — and phones — get the same double life.")

Ishita is watching a video about how the chip inside her phone is made. The narrator says the smallest features on it are only tens of nanometres across — far smaller than the wavelength of visible light, which runs from about $400$ to $700\,\text{nm}$. So an ordinary microscope just shows a blur. To check the chips, the factory uses an **electron microscope**, which "sees" with a beam of electrons instead of light.

"That makes no sense," she tells her cousin Nikhil. "Seeing needs a wave. Electrons are particles."

Nikhil tosses her his phone across the sofa. "If electrons get to be waves, then so does this, right? Why isn't it spreading out and bending round the cushions?"

Ishita catches it. She has no answer to either question. Why would a beam of particles make a sharper picture than light — and if they are waves, why is the phone so ordinary?

## The physics

In 1924 Louis de Broglie turned the photon idea around. If light, a wave, carries momentum $p = h/\lambda$, perhaps matter, made of particles, has a wavelength. He proposed that any particle with momentum $p$ has a **de Broglie wavelength**

$$\lambda = \frac{h}{p} = \frac{h}{mv}$$

where $h = 6.63\times10^{-34}\,\text{J s}$. The same formula covers photons and electrons; only the way you work out $p$ differs.

For an electron of mass $m$ and charge $e$, accelerated from rest through a potential difference $V$, the kinetic energy is $K = eV$. Since $K = \dfrac{p^2}{2m}$, the momentum is $p = \sqrt{2meV}$, so

$$\lambda = \frac{h}{\sqrt{2meV}}$$

Putting in the electron's mass and charge gives a handy shortcut, valid for electrons at speeds well below $c$:

$$\lambda = \frac{1.227}{\sqrt{V}}\ \text{nm}$$

**Why you never notice it.** Wave effects such as diffraction show up only when the wavelength is comparable to the size of the gap or obstacle the wave meets. Because $h$ is so tiny, anything with an everyday momentum has a wavelength far smaller than any gap that exists.

![A logarithmic scale of de Broglie wavelengths, marking an everyday object, a speck of dust and an electron accelerated through 100 volts, against the size of a nucleus and the spacing of atoms in a crystal](figures/de_broglie_wavelength/wavelength-scale-ladder.svg "Three moving things on one scale. Only the lightest of them lands anywhere near a size that matters.")

![Two panels showing the same gap: a short wavelength passing straight through with a sharp shadow, and a wavelength comparable to the gap fanning out beyond it](figures/de_broglie_wavelength/diffraction-needs-matching-wavelength.svg "Nothing about the opening changed. Diffraction is a comparison between two lengths, not a property of the gap.")

An electron is so light that even a modest voltage gives it a wavelength near the size of an atom. That is also why an electron microscope can show detail far finer than a light microscope: the finest detail any microscope can pick out is set roughly by the wavelength it uses.

## Worked example

**Given:** Nikhil's phone, about $0.2\,\text{kg}$, flies across the sofa at $5\,\text{m/s}$. An electron in the microscope is accelerated through $100\,\text{V}$.
**Find:** the de Broglie wavelength of each.

The phone's momentum first:

$$p = mv = 0.2 \times 5 = 1.0\,\text{kg m/s}$$

So its wavelength is

$$\lambda = \frac{h}{p} = \frac{6.63\times10^{-34}}{1.0} \approx 6.6\times10^{-34}\,\text{m}$$

A nucleus is about $10^{-15}\,\text{m}$ across. The phone's wavelength is less than $10^{-18}$ of even that — there is no gap anywhere that small for it to diffract through.

Now the electron, using the shortcut:

$$\lambda = \frac{1.227}{\sqrt{100}} = \frac{1.227}{10} \approx 0.12\,\text{nm}$$

That is about the spacing between atoms, and roughly $4000$ times shorter than green light at $500\,\text{nm}$.

**Sanity check:** the phone is about $10^{29}$ times heavier than an electron, so it is no surprise its wavelength is unimaginably shorter.

## Where the picture breaks

"Seeing with electrons" is not like seeing with light in every way. An electron microscope uses magnetic and electric lenses to focus the beam, works in a vacuum because air would scatter the electrons, and builds the image from electrons, not colours. The claim this lesson relies on is narrower: its resolving power comes from a short wavelength.

The phone does have a de Broglie wavelength; the formula applies to everything. What it lacks is any situation where that wavelength could matter.

And a matter wave is not a ripple of the electron's substance. Its intensity tells you where the electron is *likely* to be found. You will meet that idea properly in later courses.

## Key takeaway

Every moving particle has a de Broglie wavelength $\lambda = h/p = h/mv$. For an electron accelerated through $V$, $\lambda = h/\sqrt{2meV} \approx 1.227/\sqrt{V}$ nm, about the spacing of atoms, which is why electrons can image features too small for light. For an everyday object, $h$ is so tiny that $\lambda$ is absurdly small, so no diffraction can ever be seen.
