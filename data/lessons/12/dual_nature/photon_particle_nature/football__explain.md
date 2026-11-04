---
concept_id: photon_particle_nature
interest: football
format: explain
title: Can a beam of light push a football
check:
  question: |-
    A beam of light of power $P$ falls straight onto a surface. If the surface absorbs the beam completely it feels a steady force $P/c$. If an identical beam instead falls on a mirror that reflects it straight back, what force does the mirror feel?
  options:
    A: |-
      $P/c$ — the same, because the beam delivers the same power either way.
    B: |-
      $2P/c$ — twice as much.
    C: |-
      $P/2c$ — half as much, because the mirror does not keep the light.
    D: |-
      Zero — a reflected beam carries its momentum away again, so nothing is transferred.
  answer: B
  explanation: |-
    An absorbed photon's momentum goes from $p$ to $0$, a change of $p$. A reflected photon's goes from $+p$ to $-p$, a change of $2p$. Twice the momentum change each second means twice the force.
  misconceptions:
    A: |-
      Assumes the push depends only on the energy delivered. Force is the rate of momentum transfer, and reflecting a photon transfers twice as much momentum as stopping it does.
    C: |-
      Reads reflection as a weaker, partial interaction because the light is not kept. Reversing something's motion is a bigger change than merely stopping it, not a smaller one — which is exactly why solar sails are mirrors.
    D: |-
      Confuses momentum carried away with momentum transferred. The photon leaves in the opposite direction, so by conservation of momentum the mirror must have gained twice the photon's original momentum.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night, with an inset panel drawing the same beam once as a wave and once as a stream of packets, a goal-line camera on a pole, a goalkeeper and a ball](scenes/football/dual_nature.svg "Four towers pouring light onto the pitch all evening. Ask whether all that light does anything mechanical to the ball.")

The referee stopped the game in the second half. Somewhere high in the stand, somebody was playing a red laser pointer across the goalkeeper's face — a dot the size of a grain of rice, sliding over his gloves and then his eyes. Stewards went up. Play restarted four minutes later.

On the bus home Gagan would not let it go. "That thing reached the keeper from the back of the stand. If it can do that, it must be hitting him with *something*."

Lavanya was not having it. "Light has no mass. You cannot push anything with something that weighs nothing."

"Then explain the spacecraft," Gagan said. "There are probes that sail on sunlight. No fuel. Just light."

Lavanya pointed up at the floodlights, still burning over the empty pitch. "Fine. Then those are pushing the ball too. Every corner, every goal kick. And nobody in the history of the game has ever noticed."

Light either pushes things or it does not. Which is it — and if it does, by how much?

## The physics

A beam of light of frequency $\nu$ is a stream of **photons**, each carrying energy

$$E = h\nu = \frac{hc}{\lambda}$$

with $h = 6.63 \times 10^{-34}\,\text{J s}$ and $c = 3.00 \times 10^{8}\,\text{m/s}$.

A photon also carries **momentum**. Relativity relates energy and momentum by $E^2 = p^2c^2 + m^2c^4$; a photon has zero rest mass, so the last term vanishes and $E = pc$. (You are not expected to derive that here — take the result.) Therefore

$$p = \frac{E}{c} = \frac{h\nu}{c} = \frac{h}{\lambda}$$

Momentum without mass sounds like a contradiction, but $p = mv$ is the rule for an object that *has* mass. A photon is a different kind of thing.

![A side-by-side comparison of a particle with mass and a photon, listing mass, speed, momentum and energy for each](figures/photon_particle_nature/particle-vs-photon.svg "The left column is everything you learned in Class 11. The right column is what replaces it when the rest mass is zero.")

The rest of the photon's description follows. It always travels at $c$ and can never be slowed, only absorbed. It is electrically neutral, so electric and magnetic fields do not bend it. And the **intensity** of a beam fixes how many photons arrive each second, never how much energy each one carries.

The evidence for this picture is the whole of the last three lessons: a sharp threshold frequency, emission with no measurable delay, and a $K_\text{max}$ that ignores brightness entirely. All three are impossible for energy spread smoothly over a wavefront and automatic for one-photon-one-electron. (A collision experiment called the Compton effect later showed photon *momentum* being conserved too; that is beyond this chapter.)

Now the push. If $N$ photons are absorbed each second and each hands over $p$, the surface feels a steady force

$$F = Np = \frac{P}{c}$$

where $P$ is the power arriving. A *mirror* feels twice that, $2P/c$, because each photon's momentum is reversed rather than merely stopped — which is why solar sails are made shiny.

![A lamp sending a stream of photons onto a black plate, with the resulting force on the plate marked in red](figures/photon_particle_nature/photon-stream-push.svg "The push is real. Dividing by c, a number with eight zeros in it, is what makes it so small.")

## Worked example

**Given:** a red pointer of wavelength $620\,\text{nm}$ delivering $3.0\,\text{mW}$, absorbed completely by the ball.

**Find:** the energy and momentum of one photon, and the force on the ball.

Using $E\,(\text{eV}) = 1240/\lambda\,(\text{nm})$ from the previous lesson:

$$E = \frac{1240}{620} = 2.0\,\text{eV} = 3.2 \times 10^{-19}\,\text{J}$$

That is one photon's entire energy — about what it takes to free a single electron from a metal. At $3.0\,\text{mW}$, roughly $10^{16}$ of them arrive every second, which is why the beam looks like a steady dot and not a hail of pellets.

Its momentum:

$$p = \frac{E}{c} = \frac{3.2 \times 10^{-19}}{3.0 \times 10^{8}} = 1.1 \times 10^{-27}\,\text{kg m/s}$$

And the force on the ball:

$$F = \frac{P}{c} = \frac{3.0 \times 10^{-3}}{3.0 \times 10^{8}} = 1.0 \times 10^{-11}\,\text{N}$$

A match ball weighs about $4.4\,\text{N}$, so the beam pushes with roughly a millionth of the weight of a single grain of sand.

**Sanity check:** every watt of light becomes only a few nanonewtons of push, so a few milliwatts giving a hundredth of a nanonewton is exactly the right size. Gagan and Lavanya are both right: the push is real and it is nothing.

## Where the picture breaks

A photon is not a tiny ball. It has no size and no path you could trace, and the same light that behaves like packets here still diffracts through a slit. The particle picture is one face of light, not a replacement for the wave picture.

"Zero rest mass" does not mean "nothing there". Energy and momentum are real properties of a photon; mass is simply not the only way to have them.

The evenly spaced arrows in the diagram are a fiction of timing. Photons arrive at random moments, so $F = P/c$ is an average — which only matters when very few photons are involved.

And a solar sail works because in space nothing else is acting: a tiny force applied for months builds up real speed. On a pitch, gravity, air drag, boot and grass are each billions of times larger, so the floodlights change nothing anyone could ever measure. The pointer dazzled the keeper because his eye is a superb *detector*, not because the beam shoved him.

## Key takeaway

A photon carries energy $E = h\nu = hc/\lambda$ and momentum $p = h/\lambda = E/c$, with zero rest mass and speed $c$. Light therefore does push what absorbs it, with force $P/c$ — doubled to $2P/c$ if the surface reflects instead. Dividing by the speed of light turns a watt into a few nanonewtons, which is why the push matters for a fuel-free spacecraft over months and never for a ball over ninety minutes.
