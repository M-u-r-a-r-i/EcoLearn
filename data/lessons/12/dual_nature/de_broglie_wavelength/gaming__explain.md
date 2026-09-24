---
concept_id: de_broglie_wavelength
interest: gaming
format: explain
title: The wavelength of a gaming mouse
check:
  question: |-
    A gaming mouse flicked across a desk and an electron accelerated through $150\,\text{V}$ both obey $\lambda = h/p$. Why can the wave nature of only one of them ever be demonstrated?
  options:
    A: |-
      The de Broglie relation applies only to particles smaller than an atom, so it simply does not cover the mouse.
    B: |-
      The mouse's wave is destroyed by collisions with air molecules, while the electron travels in a vacuum.
    C: |-
      Only charged particles have a de Broglie wavelength, and the mouse carries no net charge.
    D: |-
      The mouse's momentum is about $10^{22}$ times the electron's, so its wavelength is that many times shorter — around $10^{-33}\,\text{m}$, far below the size of anything it could diffract around.
  answer: D
  explanation: |-
    $\lambda = h/p$ holds for both. The electron's tiny momentum puts its wavelength at about $0.1\,\text{nm}$, the spacing of atoms in a crystal; the mouse's everyday momentum pushes its wavelength down to about $10^{-33}\,\text{m}$, and nothing that small exists to test it against.
  misconceptions:
    A: |-
      Treats the de Broglie relation as a rule with a size limit built in. It has no such limit — what changes with size is the *value* of $\lambda$, which becomes undetectably small, not the validity of the formula.
    B: |-
      Blames the environment. Even in a perfect vacuum the mouse would show no diffraction, because there is no aperture anywhere near $10^{-33}\,\text{m}$ wide.
    C: |-
      Confuses charge with wave behaviour. Charge only makes an electron *convenient* — it lets you set its momentum with a voltage. Neutral particles such as neutrons diffract perfectly well.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming room shown in three stages: a cut-away retro CRT cabinet with a glowing filament and an electron beam, a flat monitor whose light leaves as a wave and then as packets, and a camera sensor feeding a current to a meter](scenes/gaming/dual_nature.svg "The light leaving the monitor is both wave and packet. This lesson asks whether the mouse on the desk is allowed the same trick.")

The LAN party has reached the hour where nobody is playing well and everybody is arguing. Ishan has just missed a shot he should have hit, and is blaming his mouse.

Nandini, who has spent all week on this chapter, is not helping. She tells him that in 1924 a French research student turned the photon question around: if a wave can behave like a particle, why should a particle not behave like a wave? And that he wrote down a wavelength for *everything that moves*. An electron. A bus. A gaming mouse.

Ishan picks the mouse up and turns it over in his hand.

"So this is a wave," he says. "Then when I drag it through the gap between my keyboard and the monitor stand, it should spread out a bit — the way sound spreads round a doorway. Why doesn't it?"

Nandini has no answer ready. If the wavelength is real, where has it gone?

## The physics

For a photon, the last lesson gave $p = h/\lambda$. Louis de Broglie's proposal was to read that equation backwards and apply it to *matter*: anything with momentum $p$ has a wavelength

$$\lambda = \frac{h}{p} = \frac{h}{mv}$$

its **de Broglie wavelength**, with $h = 6.63 \times 10^{-34}\,\text{J s}$, $p$ in $\text{kg m/s}$ and $\lambda$ in metres. It holds for any particle moving well below the speed of light, which covers everything in this syllabus.

Read the equation before you use it. Planck's constant sits on top and is unimaginably small; momentum sits underneath. So the heavier or the faster the object, the *shorter* its wavelength. A wavelength is not something a thing has more of when it moves faster — it is the exact opposite.

![A logarithmic scale of de Broglie wavelengths, marking an everyday object, a speck of dust and an electron accelerated through 100 volts, against the size of a nucleus and the spacing of atoms in a crystal](figures/de_broglie_wavelength/wavelength-scale-ladder.svg "Three moving things on one scale. Only the lightest of them lands anywhere near a size that matters.")

For a charged particle it is far easier to control the energy than the speed. An electron starting from rest and accelerated through a potential difference $V$ gains kinetic energy $eV$, so $\tfrac{1}{2}mv^2 = eV$ and $p = \sqrt{2meV}$, giving

$$\lambda = \frac{h}{\sqrt{2meV}}$$

Substituting $h$, the electron mass $m = 9.1 \times 10^{-31}\,\text{kg}$ and $e = 1.6 \times 10^{-19}\,\text{C}$ collapses that into a shortcut worth remembering:

$$\lambda = \frac{1.227}{\sqrt{V}}\ \text{nm} \qquad (V \text{ in volts})$$

Accelerate an electron through $150\,\text{V}$ — less than the voltage inside the club's old picture tube — and $\sqrt{150} = 12.25$, so $\lambda = 1.227/12.25 \approx 0.10\,\text{nm}$. That is about the spacing between atoms in a solid, and it is the whole reason electrons are useful for this.

Now Ishan's question. A wave only bends noticeably around an obstacle or opening whose size is comparable to its wavelength. Sound has a wavelength of about a metre, so it spills round doorways; visible light has a wavelength under a micrometre, so it casts sharp shadows instead.

![Two panels showing the same gap: a short wavelength passing straight through with a sharp shadow, and a wavelength comparable to the gap fanning out beyond it](figures/de_broglie_wavelength/diffraction-needs-matching-wavelength.svg "Nothing about the opening changed. Diffraction is a comparison between two lengths, not a property of the gap.")

## Worked example

**Given:** a gaming mouse of mass $0.10\,\text{kg}$ flicked across the desk at $1.0\,\text{m/s}$ (illustrative, but about right for both).
**Find:** its de Broglie wavelength, and whether any gap on that desk could reveal it.

Its momentum first:

$$p = mv = 0.10 \times 1.0 = 0.10\,\text{kg m/s}$$

An ordinary, unremarkable number — roughly the momentum your hand absorbs when the mouse hits the edge of the mat.

Now the wavelength:

$$\lambda = \frac{h}{p} = \frac{6.63 \times 10^{-34}}{0.10} = 6.6 \times 10^{-33}\,\text{m}$$

To see what that means, compare it with the smallest object physics knows well. A nucleus is about $10^{-15}\,\text{m}$ across, so the mouse's wavelength is roughly $10^{17}$ times smaller than a nucleus — a hundred million billion times. The gap by the monitor stand, a few centimetres across, is wider still by some $10^{31}$. There is no opening anywhere in the universe narrow enough for that mouse to diffract through.

**Sanity check:** dividing a number as small as $h$ by an everyday momentum was never going to produce anything but an absurdly tiny length, and it didn't.

## Where the picture breaks

The mouse's wave is not "too weak to notice". It is exactly as real as an electron's — it is simply $10^{-33}\,\text{m}$ long, and diffraction needs an obstacle of that size to show itself. Nothing is being hidden; there is just nothing fine enough to test it against.

A matter wave is also not a wave *of* anything material. The mouse is not rippling, and the wave is not made of mouse. What the wave describes is where the particle is likely to be found — an idea you will meet properly in later study. Push the water-wave image any further than this diffraction comparison and it will mislead you.

Two limits on the formula: $\lambda = h/mv$ uses the everyday momentum $mv$, so it needs $v$ well below $c$; and a diffraction pattern is built up from very many particles arriving one at a time, never from watching a single particle spread out.

## Key takeaway

Every moving particle has a wavelength $\lambda = h/p = h/mv$. Because $h$ is some $10^{34}$ times smaller than an everyday momentum, anything with the mass of a mouse ends up with a wavelength far too short to detect, ever. Make the particle light enough — an electron — and the wavelength climbs to the size of an atom, where it can finally be caught.
