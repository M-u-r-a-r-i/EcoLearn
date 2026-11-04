---
concept_id: photon_particle_nature
interest: smartphones
format: explain
title: Does a phone flashlight push the phone backwards
check:
  question: |-
    A photon from a phone's display carries $3.0\,\text{eV}$ of energy. What is its momentum? (Take $1\,\text{eV} = 1.6\times10^{-19}\,\text{J}$ and $c = 3.0\times10^{8}\,\text{m/s}$.)
  options:
    A: |-
      $1.6\times10^{-27}\,\text{kg m/s}$
    B: |-
      $4.8\times10^{-19}\,\text{kg m/s}$
    C: |-
      Zero, because a photon has no mass
    D: |-
      $5.3\times10^{-36}\,\text{kg m/s}$
  answer: A
  explanation: |-
    For a photon $p = E/c$. Here $E = 3.0\times1.6\times10^{-19} = 4.8\times10^{-19}\,\text{J}$, so $p = 4.8\times10^{-19}/3.0\times10^{8} = 1.6\times10^{-27}\,\text{kg m/s}$.
  misconceptions:
    B: |-
      Converts the energy to joules and stops there, giving the energy a momentum unit. Momentum needs one more step: divide by $c$.
    C: |-
      Carries $p = mv$ over from Class 11. A photon has zero rest mass but still carries momentum $p = E/c = h/\lambda$; the recoil of a light-pushed surface is measurable.
    D: |-
      Divides by $c^2$, which turns an energy into a mass, not a momentum. A photon's momentum is $E/c$.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A phone beside a sunny window, its screen showing a UV-index meter, its flashlight beam drawn half as a wave and half as a stream of packets, and a magnified camera pixel where light frees electrons](scenes/smartphones/dual_nature.svg "The flashlight beam, drawn two ways at once. This lesson takes the packet half seriously.")

Diya is on the rooftop of her building in Chennai at 11 p.m., trying to photograph the stars. Her phone's night photos come out grainy, speckled with random dots of colour, and a video she watches says that is partly because the camera is catching light "one photon at a time".

Bored, she switches on the flashlight and points it at the sky. Her little brother Aarav, watching, asks something she cannot answer.

"If light comes in packets, and the packets fly off that way, doesn't the phone get kicked this way? Like a rocket?"

Diya laughs — then stops. Rockets work by throwing stuff out of the back. Her flashlight is throwing out a stream of something. It has been on for a minute, and her hand has felt nothing at all.

Is Aarav's rocket real? And if it is, why can't she feel it?

## The physics

Einstein's explanation of the photoelectric effect treats light as a stream of **photons**. Put together, the evidence gives a clear list of what a photon is.

- **Energy:** $E = h\nu = \dfrac{hc}{\lambda}$, fixed by the frequency alone.
- **Momentum:** $p = \dfrac{h\nu}{c} = \dfrac{h}{\lambda}$.
- **Speed:** always $c$ in vacuum.
- **Rest mass:** zero. A photon cannot be at rest.
- **Charge:** zero, so electric and magnetic fields do not deflect it.
- In a collision with a particle, total energy and momentum are conserved, but photons can be absorbed or created, so their number need not stay the same.
- A brighter beam of the same colour has **more photons per second**, not bigger ones.

![A side-by-side comparison of a particle with mass and a photon, listing mass, speed, momentum and energy for each](figures/photon_particle_nature/particle-vs-photon.svg "The left column is everything you learned in Class 11. The right column is what replaces it when the rest mass is zero.")

Since each photon carries momentum, a stream of photons carries momentum away from the source every second, so the source feels a push backwards. For a beam of power $P$ absorbed by a black surface, the force on it is

$$F = \frac{P}{c}$$

It is the rate at which momentum arrives. The lamp that sent the beam feels the same size of force in the opposite direction.

![A lamp sending a stream of photons onto a black plate, with the resulting force on the plate marked in red](figures/photon_particle_nature/photon-stream-push.svg "The push is real. Dividing by c, a number with eight zeros in it, is what makes the push so small.")

**The evidence for particles.** The photoelectric effect is the main one: a threshold frequency, no time delay and $K_\text{max}$ independent of intensity all need light to arrive in packets of $h\nu$. In the **Compton effect** (beyond this syllabus), X-ray photons bounce off electrons like billiard balls, with energy and momentum both conserved. And very sensitive detectors, including a camera pixel in very dim light, register light as separate, random arrivals — part of the graininess in Diya's night photos.

## Worked example

**Given:** say the flashlight sends out about $1\,\text{W}$ of light (a generous round figure). Treat it all as light of wavelength $600\,\text{nm}$. Take $h = 6.63\times10^{-34}\,\text{J s}$.
**Find:** how many photons leave each second, and the push on the phone.

Energy of one photon:

$$E = \frac{hc}{\lambda} = \frac{6.63\times10^{-34}\times3.0\times10^{8}}{600\times10^{-9}} \approx 3.3\times10^{-19}\,\text{J}$$

Photons per second, to carry $1\,\text{J}$ every second:

$$N = \frac{1}{3.3\times10^{-19}} \approx 3.0\times10^{18}$$

Three billion billion packets leave every second.

Momentum of one photon:

$$p = \frac{h}{\lambda} = \frac{6.63\times10^{-34}}{600\times10^{-9}} \approx 1.1\times10^{-27}\,\text{kg m/s}$$

The push is the momentum carried away per second:

$$F = Np \approx 3.0\times10^{18}\times1.1\times10^{-27} \approx 3.3\times10^{-9}\,\text{N}$$

The same as $P/c = 1/(3.0\times10^8)$. Aarav's rocket is real — with a thrust smaller than the weight of a single grain of fine sand.

**Sanity check:** light pushes on everything it hits all day, and nothing around us moves because of it, so a force of a few billionths of a newton is the right size.

## Where the picture breaks

A flashlight is not a laser: its light spreads out into a cone and has a range of colours. Neither changes the answer much, because the total push depends only on the power, $F = P/c$, and not on how it is shared between photons. Spreading only means part of the push points sideways and cancels.

And "packets" are not tiny marbles. The same light that arrives as separate photons also diffracts and interferes like a wave. Particle and wave are two descriptions of one thing, and each experiment shows you one side of it. The next lesson turns that idea around.

## Key takeaway

A photon of frequency $\nu$ carries energy $E = h\nu$ and momentum $p = h/\lambda = E/c$, travels at $c$ and has zero rest mass. Brighter light means more photons, not more energetic ones. A beam of power $P$ pushes with force $P/c$ — real, but tiny, because $c$ is so large. The photoelectric and Compton effects are the key evidence that light comes in these packets.
