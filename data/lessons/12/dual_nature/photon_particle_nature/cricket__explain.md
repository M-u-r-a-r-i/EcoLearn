---
concept_id: photon_particle_nature
interest: cricket
format: explain
title: Why light can push a spacecraft but not a cricket ball
check:
  question: |-
    A red beam of wavelength $800\,\text{nm}$ and a blue beam of wavelength $400\,\text{nm}$ each deliver the same power — the same energy every second. Comparing the blue beam with the red one, what is true?
  options:
    A: |-
      The blue beam delivers twice as many photons per second, each carrying twice the momentum.
    B: |-
      The two beams deliver the same number of photons per second, because they carry the same power.
    C: |-
      The blue beam delivers half as many photons per second, each carrying half the momentum.
    D: |-
      The blue beam delivers half as many photons per second, each carrying twice the momentum.
  answer: D
  explanation: |-
    A blue photon has half the wavelength, so $E = hc/\lambda$ is doubled and $p = h/\lambda$ is doubled. To deliver the same energy each second with photons that are twice as energetic, the blue beam needs only half as many of them.
  misconceptions:
    A: |-
      Gets the momentum right but assumes a shorter wavelength also means more photons. At a fixed power, more energy per photon must mean fewer photons each second — not more.
    B: |-
      Treats the photon count as fixed by the power alone. Power is energy per second, which is the number of photons per second multiplied by the energy of each; change one and the other must change.
    C: |-
      Uses $p \propto \lambda$ instead of $p = h/\lambda$, inverting the relation, so a shorter wavelength is wrongly read as less momentum.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit cricket ground at night, with a light beam drawn half as a wave and half as a stream of packets, an umpire holding a light meter and a tracking camera on a tripod](scenes/cricket/dual_nature.svg "Four towers pouring light onto the ground all evening. Ask whether all that light does anything mechanical to the ball.")

The floodlights came on at six, and Farhan's net session turned into an argument.

Divya had spent the afternoon reading about solar sails — spacecraft driven along by nothing but sunlight, carrying no fuel at all. She mentioned it between overs.

Farhan refused to believe it. "Light has no mass. You cannot push anything with something that weighs nothing."

"They have flown," Divya said. "It is not a theory."

Farhan pointed up at the towers. "Fine. Then those lights are pushing the ball too. Every single delivery. So the ball should drift towards the sight screen — and in the whole history of the game nobody has ever noticed."

They both look at the ball in Divya's hand, lit white against the dark.

Light either pushes things or it does not. Which is it, and if it does, by how much?

## The physics

A beam of light of frequency $\nu$ is a stream of **photons**, each carrying

$$E = h\nu = \frac{hc}{\lambda}$$

with $h = 6.63 \times 10^{-34}\,\text{J s}$ and $c = 3.00 \times 10^{8}\,\text{m/s}$.

A photon also carries **momentum**. Relativity relates energy and momentum by $E^2 = p^2c^2 + m^2c^4$; a photon has zero rest mass, so the last term vanishes and $E = pc$. (You are not expected to derive that relation here — take the result.) So

$$p = \frac{E}{c} = \frac{h\nu}{c} = \frac{h}{\lambda}$$

Momentum without mass sounds wrong, but $p = mv$ is the rule for an object *with* mass. A photon is a different kind of thing.

![A side-by-side comparison of a particle with mass and a photon, listing mass, speed, momentum and energy for each](figures/photon_particle_nature/particle-vs-photon.svg "The left column is everything you learned in Class 11. The right column is what replaces it when the rest mass is zero.")

The rest of the photon's description follows: it always travels at $c$ and can never be slowed, only absorbed; it is electrically neutral, so electric and magnetic fields do not bend it; and the **intensity** of a beam fixes how many photons arrive each second, never how much energy each one carries.

The evidence for this picture is the whole of the last three lessons — a threshold frequency, emission with no delay, and a $K_\text{max}$ that ignores brightness. All three are impossible for a spread-out wave and automatic for one-photon-one-electron. (A collision experiment called the Compton effect later showed photon *momentum* being conserved as well; that is beyond this chapter.)

Absorb $N$ photons per second and each hands over $p$, so a surface that swallows a beam of power $P$ feels a steady force

$$F = Np = \frac{P}{c}$$

![A lamp sending a stream of photons onto a black plate, with the resulting force on the plate marked in red](figures/photon_particle_nature/photon-stream-push.svg "The push is real. Dividing by c, a number with eight zeros in it, is what makes the push so small.")

## Worked example

**Given:** orange-red light of wavelength $620\,\text{nm}$, and a lamp delivering $1.0\,\text{W}$ of it onto a ball that absorbs all of it.
**Find:** the energy and momentum of one photon, and the force on the ball.

Using $E\,(\text{eV}) = 1240/\lambda\,(\text{nm})$ from the previous lesson:

$$E = \frac{1240}{620} = 2.0\,\text{eV} = 3.2 \times 10^{-19}\,\text{J}$$

That is one photon's whole energy — about what it takes to free one electron from a metal.

$$p = \frac{E}{c} = \frac{3.2 \times 10^{-19}}{3.0 \times 10^{8}} = 1.1 \times 10^{-27}\,\text{kg m/s}$$

Now how many arrive each second, if the lamp puts out $1.0\,\text{J}$ every second:

$$N = \frac{1.0}{3.2 \times 10^{-19}} = 3.1 \times 10^{18}\ \text{photons per second}$$

Three billion billion of them — which is why light normally looks smooth.

$$F = Np = 3.1 \times 10^{18} \times 1.1 \times 10^{-27} = 3.3 \times 10^{-9}\,\text{N}$$

Check it the short way: $F = P/c = 1.0 / (3.0 \times 10^{8}) = 3.3 \times 10^{-9}\,\text{N}$. Same answer.

**Sanity check:** the ball's own weight is about $1.6\,\text{N}$, so the light pushes with roughly half a billionth of the ball's weight — thousands of times less than the weight of a single grain of sand. Divya and Farhan are both right.

## Where the picture breaks

A photon is not a tiny ball. It has no size and no path you could trace, and the same light that behaves like packets here still diffracts through a slit. The particle picture is one face of light, not a replacement for the wave picture.

"Zero rest mass" does not mean "nothing there". Energy and momentum are real properties; mass is simply not the only way to have them.

The neat arrows in the diagram are a fiction of timing. Photons arrive at random moments, so $F = P/c$ is an average — a fact that only matters when very few photons are involved.

And solar sails are not pushed by absorbing light; they reflect it, which reverses each photon's momentum and doubles the force to $2P/c$. They work in space because nothing else is acting. On a cricket ground, gravity, air drag and the bat are each billions of times larger, so the floodlights change nothing you could ever measure.

## Key takeaway

A photon carries energy $E = h\nu = hc/\lambda$ and momentum $p = h/\lambda = E/c$, with zero rest mass and speed $c$. Light therefore does push what absorbs it, with a force $P/c$ — but dividing by the speed of light turns a watt into a few nanonewtons, which is why the push matters for a fuel-free spacecraft over months and never for a ball over an over.
