---
concept_id: photon_particle_nature
interest: gaming
format: explain
title: The solar sail level the physics coder refused to build
check:
  question: |-
    Ishita's game code already stores each photon's energy $E$. To work out the push on a sail it also needs each photon's momentum. Which line should she write?
  options:
    A: |-
      $p = 0$, because a photon has no mass and momentum is mass times velocity.
    B: |-
      $p = \dfrac{E}{c}$
    C: |-
      $p = Ec$
    D: |-
      $p = \dfrac{E}{c^2}$, the mass equivalent of the photon's energy.
  answer: B
  explanation: |-
    A photon has zero rest mass, so the relation $E^2 = p^2c^2 + m^2c^4$ collapses to $E = pc$, giving $p = E/c = h/\lambda$.
  misconceptions:
    A: |-
      Assumes that no mass means no momentum. $p = mv$ is the rule for objects that *have* mass; a photon carries momentum without it, and reflecting light off a mirror demonstrably pushes the mirror.
    C: |-
      Multiplies by $c$ instead of dividing. Checking units settles it: $\text{J} \times \text{m/s}$ is not $\text{kg m/s}$, while $\text{J} / (\text{m/s})$ is.
    D: |-
      Borrows $m = E/c^2$ from $E = mc^2$ and calls that a momentum. That expression has the units of mass, not of momentum, and dividing by $c^2$ makes the answer smaller than the true momentum by a factor of $c$.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming room shown in three stages: a cut-away retro CRT cabinet with a glowing filament and an electron beam, a flat monitor whose light leaves as a wave and then as packets, and a camera sensor feeding a current to a meter](scenes/gaming/dual_nature.svg "The monitor pours light into the room all evening. Ask whether all that light does anything mechanical to what it lands on.")

Ishita's team is three weeks into a space game, and the level everyone likes best has no engine in it at all. Your ship is a sail. You steer by angling a sheet of foil into the sunlight and letting the light push you along.

Dhruv, who writes the physics code, has refused to build it.

"Light has no mass," he says. "Momentum is mass times velocity. Zero times anything is zero. Sails are fantasy — bolt a rocket on it like a normal game."

Ishita has read that sails have actually flown, with no fuel at all. She also knows Dhruv's engine updates every object sixty times a second, and that if light genuinely pushes things then strictly it should push the crates, the dropped helmets and the player too, in every single one of those frames.

So: does light push anything at all — and if it does, why has nobody ever watched a torch beam shove a crate across a floor?

## The physics

A beam of light of frequency $\nu$ is a stream of **photons**, each carrying

$$E = h\nu = \frac{hc}{\lambda}$$

with $h = 6.63 \times 10^{-34}\,\text{J s}$ and $c = 3.00 \times 10^{8}\,\text{m/s}$.

A photon also carries **momentum**. Relativity ties energy and momentum together by $E^2 = p^2c^2 + m^2c^4$; a photon has zero rest mass, so the last term vanishes, leaving $E = pc$. (You are not expected to derive that relation here — take the result.) Therefore

$$p = \frac{E}{c} = \frac{h\nu}{c} = \frac{h}{\lambda}$$

Momentum without mass sounds like a contradiction, and that is Dhruv's whole objection. The answer is that $p = mv$ is the rule for an object *with* mass. A photon is a different kind of thing, and the relation that covers both is the one above.

![A side-by-side comparison of a particle with mass and a photon, listing mass, speed, momentum and energy for each](figures/photon_particle_nature/particle-vs-photon.svg "The left column is everything you learned in Class 11. The right column is what replaces it when the rest mass is zero.")

The rest of the photon's description follows: it always travels at $c$ and can never be slowed, only absorbed; it is electrically neutral, so fields do not bend it; and the **intensity** of a beam fixes how many photons arrive each second, never how much energy each one carries.

The evidence for this picture is the whole of the last three lessons — a sharp threshold frequency, emission with no measurable delay, and a $K_\text{max}$ that flatly ignores brightness. All three are impossible for energy spread smoothly through a wave, and automatic for one photon meeting one electron. (A collision experiment, the Compton effect, later showed photon *momentum* being conserved too; that is beyond this chapter.)

Absorb $N$ photons per second, each handing over $p$, and a surface swallowing a beam of power $P$ feels a steady force

$$F = Np = \frac{P}{c}$$

![A lamp sending a stream of photons onto a black plate, with the resulting force on the plate marked in red](figures/photon_particle_nature/photon-stream-push.svg "The push is real. Dividing by c, a number with eight zeros in it, is what makes the push so small.")

## Worked example

**Given:** blue light of wavelength $400\,\text{nm}$, and a lamp delivering $2.0\,\text{W}$ of it onto a surface that absorbs all of it.
**Find:** the energy and momentum of one photon, and the steady force on the surface.

One photon's energy, using $E\,(\text{eV}) = 1240/\lambda\,(\text{nm})$:

$$E = \frac{1240}{400} = 3.1\,\text{eV} = 5.0 \times 10^{-19}\,\text{J}$$

That is about what it takes to free one electron from a metal — the scale this whole chapter lives on.

Its momentum:

$$p = \frac{E}{c} = \frac{5.0 \times 10^{-19}}{3.0 \times 10^{8}} = 1.7 \times 10^{-27}\,\text{kg m/s}$$

Now how many arrive each second, if the lamp puts out $2.0\,\text{J}$ every second:

$$N = \frac{2.0}{5.0 \times 10^{-19}} = 4.0 \times 10^{18}\ \text{photons per second}$$

Four billion billion of them, which is exactly why light looks smooth and continuous to us. The force is that many handovers per second:

$$F = Np = 4.0 \times 10^{18} \times 1.7 \times 10^{-27} \approx 6.8 \times 10^{-9}\,\text{N}$$

Check it the short way: $F = P/c = 2.0 / (3.0 \times 10^{8}) = 6.7 \times 10^{-9}\,\text{N}$. The same answer, to the rounding.

**Sanity check:** a wireless controller weighs roughly $2.5\,\text{N}$, so this push is a few billionths of the weight of a controller — real, and utterly unnoticeable. Ishita and Dhruv are each half right.

## Where the picture breaks

A photon is not a tiny ball. It has no size and no path you could trace, and the same light that behaves like packets here still diffracts through a slit. The particle picture is one face of light, not a replacement for the wave picture.

"Zero rest mass" does not mean "nothing there". Energy and momentum are real properties; mass is simply not the only way to have them.

The neat evenly spaced arrows in the diagram are a fiction of timing. Photons arrive at random moments, so $F = P/c$ is an average — which only matters when very few photons are involved.

And a real sail is not pushed by absorbing light; it reflects it, reversing each photon's momentum and doubling the force to $2P/c$. Sails work in space because nothing else is acting and the push runs for months. Inside Dhruv's engine, one frame of $1/60\,\text{s}$ under a $2\,\text{W}$ lamp would deliver an impulse of about $10^{-10}\,\text{N s}$ — so he is right to leave light pressure out of the crates, and wrong to leave out the sail.

## Key takeaway

A photon carries energy $E = h\nu = hc/\lambda$ and momentum $p = h/\lambda = E/c$, with zero rest mass and speed $c$. Light really does push whatever absorbs it, with a force $P/c$ — but dividing by the speed of light turns a couple of watts into a few nanonewtons, which is why the push matters for a fuel-free spacecraft over months and never for a torch beam over an evening.
