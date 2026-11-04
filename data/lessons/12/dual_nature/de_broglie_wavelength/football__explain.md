---
concept_id: de_broglie_wavelength
interest: football
format: explain
title: The wavelength of a football
check:
  question: |-
    A proton and an electron both start from rest and are accelerated through the same potential difference. Which of them ends up with the longer de Broglie wavelength?
  options:
    A: |-
      The proton, because the same voltage gives a heavier particle more kinetic energy.
    B: |-
      The proton, because $\lambda = h/mv$ grows with mass.
    C: |-
      The electron, because at the same kinetic energy the lighter particle carries the smaller momentum.
    D: |-
      Neither — their wavelengths are equal, because they were given the same energy.
  answer: C
  explanation: |-
    Both carry the same size of charge, so both gain the same kinetic energy $eV$. At equal $K$ the momentum is $p = \sqrt{2mK}$, so the far lighter electron has the far smaller momentum and hence the far longer wavelength $\lambda = h/p$.
  misconceptions:
    A: |-
      Assumes a heavier particle picks up more energy from the same voltage. The energy gained is $qV$, and $q$ has the same magnitude for both, so the kinetic energies are identical.
    B: |-
      Reads mass as raising the wavelength. Mass sits in the denominator through $p = mv$, so a heavier particle at the same energy has a *shorter* wavelength.
    D: |-
      Treats equal kinetic energy as equal momentum. They are different quantities: $p = \sqrt{2mK}$, so equal energies give very unequal momenta when the masses differ by a factor of about $1800$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night, with an inset panel drawing the same beam once as a wave and once as a stream of packets, a goal-line camera on a pole, a goalkeeper and a ball](scenes/football/dual_nature.svg "The light off the towers is both wave and packet. This lesson asks whether the ball is allowed the same trick.")

Prerna came out of the physics lab repeating one sentence: everything that moves is a wave. Her teacher had said it flatly — an electron, a bus, a football.

Ashwin plays at the back for the school team and did not enjoy being told his sport was imaginary. He walked her out to the pitch, set the ball down twenty metres from goal and stood two friends up as a wall with a gap of about half a metre between them.

"Sound spreads out through a doorway," he said. "Waves bend round edges. So if the ball is a wave, it should fan out when it goes through that gap. Nobody could ever pass through a wall on purpose."

He hit it through. It went dead straight and thumped the post.

"Explain that."

## The physics

For a photon the last lesson gave $p = h/\lambda$. In 1924 Louis de Broglie proposed reading that equation backwards and applying it to *matter*: anything with momentum $p$ has a wavelength

$$\lambda = \frac{h}{p} = \frac{h}{mv}$$

called its **de Broglie wavelength**, with $h = 6.63 \times 10^{-34}\,\text{J s}$, $p$ in $\text{kg m/s}$ and $\lambda$ in metres. It applies to any particle moving well below the speed of light, which covers everything in this syllabus.

Read the equation before using it. Planck's constant on top is unimaginably small and momentum sits underneath, so the heavier or faster the object, the *shorter* its wavelength. A wavelength is not something a particle has more of when it moves fast; it is the exact opposite.

![A logarithmic scale of de Broglie wavelengths, marking an everyday object, a speck of dust and an electron accelerated through 100 volts, against the size of a nucleus and the spacing of atoms in a crystal](figures/de_broglie_wavelength/wavelength-scale-ladder.svg "Three moving things on one scale. Only the lightest of them lands anywhere near a size that matters.")

For a charged particle it is easier to control the energy than the speed. An electron starting from rest and accelerated through a potential difference $V$ gains kinetic energy $eV$, so $\tfrac{1}{2}mv^2 = eV$ and $p = \sqrt{2meV}$, giving

$$\lambda = \frac{h}{\sqrt{2meV}}$$

Putting in $h$, the electron mass $m = 9.1 \times 10^{-31}\,\text{kg}$ and $e = 1.6 \times 10^{-19}\,\text{C}$ collapses this to a shortcut worth remembering:

$$\lambda = \frac{1.227}{\sqrt{V}}\ \text{nm} \qquad (V\text{ in volts})$$

At $V = 100\,\text{V}$ that is $\lambda = 0.12\,\text{nm}$ — about the spacing between atoms in a solid, which is the whole reason electrons are useful for probing matter.

Now Ashwin's challenge. A wave only bends noticeably around an obstacle or through a gap whose size is comparable to its wavelength. Sound has a wavelength of about a metre, so it spills round doorways. Light has a wavelength of half a micrometre, so it casts sharp shadows instead. The comparison is between two lengths, and nothing else.

![Two panels showing the same gap: a short wavelength passing straight through with a sharp shadow, and a wavelength comparable to the gap fanning out beyond it](figures/de_broglie_wavelength/diffraction-needs-matching-wavelength.svg "Nothing about the opening changed. Diffraction is a comparison between two lengths, not a property of the gap.")

## Worked example

**Given:** a match ball of mass $0.45\,\text{kg}$ driven through the wall at $20\,\text{m/s}$ (illustrative, but a realistic pass).

**Find:** its de Broglie wavelength, and whether any gap on the pitch could reveal it.

Its momentum first:

$$p = mv = 0.45 \times 20 = 9.0\,\text{kg m/s}$$

An ordinary, sturdy number — roughly what a goalkeeper's hands have to absorb holding a shot like that.

Now the wavelength:

$$\lambda = \frac{h}{p} = \frac{6.63 \times 10^{-34}}{9.0} = 7.4 \times 10^{-35}\,\text{m}$$

To feel how small that is, compare it with the smallest thing physics knows of. A nucleus is about $10^{-15}\,\text{m}$ across, so the ball's wavelength is about $10^{19}$ times smaller than a nucleus — ten billion billion times.

Ashwin's gap was half a metre; the goal itself is $7.32\,\text{m}$ wide. There is no opening on a football pitch, or anywhere in the universe, narrow enough to make that ball diffract.

**Sanity check:** dividing a number as small as $h$ by an everyday momentum was never going to give anything but an absurdly tiny length — and it did.

## Where the picture breaks

The ball's wave is not "too weak to notice". It is exactly as real as an electron's; it is just $10^{-35}\,\text{m}$ long, and diffraction needs an obstacle of that size to show itself. Nothing is being hidden — there is simply nothing fine enough to test it against.

The matter wave is also not a wave *of* anything material. The ball is not rippling, and the wave is not made of ball. What it describes is where the particle is likely to be found, an idea you will meet properly in later study. Push the water-wave image beyond the diffraction comparison and it will mislead you.

Two limits on the formula: $\lambda = h/mv$ uses the everyday momentum $mv$, so it needs $v$ well below $c$; and a diffraction pattern is built up from very many particles arriving one at a time, never from watching one particle spread out.

## Key takeaway

Every moving particle has a wavelength $\lambda = h/p = h/mv$. Because $h$ is some $10^{34}$ times smaller than an everyday momentum, anything with the mass of a ball has a wavelength far too short ever to be detected. Make the particle light enough — an electron — and the wavelength climbs to the size of an atom, where it can finally be caught.
