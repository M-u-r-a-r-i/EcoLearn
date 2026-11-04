---
concept_id: de_broglie_wavelength
interest: cricket
format: explain
title: The wavelength of a cricket ball
check:
  question: |-
    Two identical cricket balls are thrown along the same line, one at $10\,\text{m/s}$ and the other at $30\,\text{m/s}$. How do their de Broglie wavelengths compare?
  options:
    A: |-
      The faster ball's wavelength is three times longer than the slower ball's.
    B: |-
      The faster ball's wavelength is one-third of the slower ball's.
    C: |-
      Their wavelengths are equal, because the two balls have the same mass.
    D: |-
      The faster ball's wavelength is one-ninth of the slower ball's.
  answer: B
  explanation: |-
    $\lambda = h/p = h/mv$, so at the same mass the wavelength is inversely proportional to the speed. Tripling $v$ divides $\lambda$ by three.
  misconceptions:
    A: |-
      Treats a faster particle as a bigger wave, reading $\lambda \propto v$. Speed sits in the denominator: more momentum always means a shorter wavelength.
    C: |-
      Remembers that $m$ appears in $\lambda = h/mv$ but forgets that $v$ does too. It is the momentum $mv$ that fixes the wavelength, not the mass alone.
    D: |-
      Uses $\lambda \propto 1/v^2$, carrying over the squared speed from kinetic energy $\tfrac{1}{2}mv^2$. The de Broglie relation is built on momentum, which is linear in $v$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit cricket ground at night, with a light beam drawn half as a wave and half as a stream of packets, an umpire holding a light meter and a tracking camera on a tripod](scenes/cricket/dual_nature.svg "The light coming off the towers is both wave and packet. The lesson asks whether the ball is allowed the same trick.")

Sameer's class had spent a full week on the photoelectric effect, and by Friday he had had enough.

"So light is really little packets," he said. "Then why does everybody still call it a wave?"

His teacher's answer made it worse. She said that in 1924 a French research student had turned the question around: if a wave can behave like a particle, why should a particle not behave like a wave? And that he had written down a wavelength for *everything that moves* — an electron, a bus, a cricket ball.

Sameer repeated all of this to Ritika on the way to the nets. Ritika said nothing, marked her run-up, and bowled one hard at his pads.

"That ball," she said, "is a wave. So it should bend around the edge of the gate on the way out, the way sound does. Spread out a bit. Why doesn't it?"

Sameer had no answer. If the wavelength is real, where has it gone?

## The physics

For a photon the last lesson gave $p = h/\lambda$. Louis de Broglie's proposal was to read that equation backwards and apply it to *matter*: anything with momentum $p$ has a wavelength

$$\lambda = \frac{h}{p} = \frac{h}{mv}$$

called its **de Broglie wavelength**, with $h = 6.63 \times 10^{-34}\,\text{J s}$, $p$ in $\text{kg m/s}$ and $\lambda$ in metres. It holds for any particle moving well below the speed of light, which covers everything in this syllabus.

Read the equation before using it. Planck's constant on top is unimaginably small, and momentum is on the bottom — so the heavier or faster the object, the *shorter* its wavelength. A wavelength is not something a particle has a lot of when it is moving fast; it is the opposite.

![A logarithmic scale of de Broglie wavelengths, marking an everyday object, a speck of dust and an electron accelerated through 100 volts, against the size of a nucleus and the spacing of atoms in a crystal](figures/de_broglie_wavelength/wavelength-scale-ladder.svg "Three moving things on one scale. Only the lightest of them lands anywhere near a size that matters.")

For a charged particle it is easier to control the energy than the speed. An electron starting from rest and accelerated through a potential difference $V$ gains kinetic energy $eV$, so $\tfrac{1}{2}mv^2 = eV$ and $p = \sqrt{2meV}$, giving

$$\lambda = \frac{h}{\sqrt{2meV}}$$

Putting in $h$, the electron mass $m = 9.1 \times 10^{-31}\,\text{kg}$ and $e = 1.6 \times 10^{-19}\,\text{C}$ collapses this to a shortcut worth remembering:

$$\lambda = \frac{1.227}{\sqrt{V}}\ \text{nm} \qquad (V \text{ in volts})$$

At $V = 100\,\text{V}$ that gives $\lambda = 0.12\,\text{nm}$ — about the spacing between atoms in a solid, which is the whole reason electrons are useful for this.

Now Ritika's question. A wave only bends noticeably around an obstacle whose size is comparable to its wavelength. Sound has a wavelength of about a metre, so it spills round doorways; light has a wavelength of half a micrometre, so it casts sharp shadows instead.

![Two panels showing the same gap: a short wavelength passing straight through with a sharp shadow, and a wavelength comparable to the gap fanning out beyond it](figures/de_broglie_wavelength/diffraction-needs-matching-wavelength.svg "Nothing about the opening changed. Diffraction is a comparison between two lengths, not a property of the gap.")

## Worked example

**Given:** a cricket ball of mass $0.16\,\text{kg}$ bowled at $30\,\text{m/s}$ (illustrative, but a realistic pace).
**Find:** its de Broglie wavelength, and whether anything on the ground could reveal it.

Its momentum first:

$$p = mv = 0.16 \times 30 = 4.8\,\text{kg m/s}$$

That is an ordinary, sturdy number — roughly the momentum a fielder absorbs in the hands taking a catch.

Now the wavelength:

$$\lambda = \frac{h}{p} = \frac{6.63 \times 10^{-34}}{4.8} = 1.4 \times 10^{-34}\,\text{m}$$

To see what that means, compare it with the smallest object physics knows of. A nucleus is about $10^{-15}\,\text{m}$ across, so the ball's wavelength is about $10^{19}$ times smaller than a nucleus — ten billion billion times. There is no gate, no gap between two fielders, and no opening anywhere in the universe narrow enough for the ball to diffract through.

**Sanity check:** dividing a number as small as $h$ by an everyday momentum was never going to give anything but an absurdly tiny length, and it did.

## Where the picture breaks

The ball's wave is not "too weak to notice". It is exactly as real as an electron's — it is just $10^{-34}\,\text{m}$ long, and diffraction needs an obstacle of that size to show itself. Nothing is being hidden; there is simply nothing fine enough to test it against.

The matter wave is also not a wave *of* anything material. The ball is not rippling, and the wave is not made of ball. What the wave describes is where the particle is likely to be found — an idea you will meet properly in later study. Pushing the water-wave image any further than the diffraction comparison will mislead you.

Two limits on the formula: $\lambda = h/mv$ uses the everyday momentum $mv$, so it needs $v$ well below $c$; and a diffraction pattern is built up from very many particles arriving one at a time, never from watching one particle spread out.

## Key takeaway

Every moving particle has a wavelength $\lambda = h/p = h/mv$. Because $h$ is some $10^{34}$ times smaller than an everyday momentum, anything with the mass of a ball has a wavelength far too short to ever be detected. Make the particle light enough — an electron — and the wavelength climbs to the size of an atom, where it can finally be caught.
