---
concept_id: photoelectric_observations
interest: football
format: explain
title: The bright red lamp the photocell ignored
check:
  question: |-
    In a photoelectric experiment the collector is made negative and the retarding voltage is raised until the photocurrent just falls to zero, at $1.2\,\text{V}$. The lamp is then moved to twice its original distance from the cell, with nothing else changed, and the measurement is repeated. At what retarding voltage does the current fall to zero now?
  options:
    A: |-
      $1.2\,\text{V}$, exactly as before.
    B: |-
      $0.6\,\text{V}$, because dimmer light gives the electrons less energy.
    C: |-
      $0.3\,\text{V}$, because doubling the distance cuts the intensity to a quarter.
    D: |-
      $0\,\text{V}$, because light that faint cannot free any electrons at all.
  answer: A
  explanation: |-
    The stopping potential is fixed by the frequency of the light and the emitter metal, through $K_\text{max} = eV_0$. Moving the lamp changes how many photons arrive each second — the saturation current — not how much energy each one carries.
  misconceptions:
    B: |-
      The wave-theory idea that dimmer light means slower electrons. Brightness sets how many electrons come out; frequency sets how fast the fastest one is.
    C: |-
      Gets the inverse-square fall of intensity right and then applies it to the wrong quantity. The intensity really does drop to a quarter, and the saturation current with it, but the stopping potential does not depend on intensity at all.
    D: |-
      Assumes there is a minimum brightness below which nothing is emitted. There is a threshold in *frequency*, never in intensity: faint light of the right colour still frees electrons, just fewer of them.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night, with an inset panel drawing the same beam once as a wave and once as a stream of packets, a goal-line camera on a pole, a goalkeeper and a ball](scenes/football/dual_nature.svg "The camera on the pole turns light into a current — and it is very fussy about which light.")

Tejas volunteers on the ticket gate at his club's home matches. His whole job is one small purple lamp: hold a ticket under it and a pattern nobody can otherwise see glows back at him.

Suhani, who runs the school science club, has borrowed the demonstration photocell for the evening — a small evacuated bulb wired to a meter — and has set it on the table beside him.

Tejas tries it first. He fetches the red emergency lamp from the pitch-side first-aid box, the one you can see from the far touchline, and holds it a few centimetres from the cell. The needle does not move. He brings it closer. Still nothing.

Suhani holds her feeble ticket lamp a full arm's length away. The needle swings right across the dial.

Tejas looks from one lamp to the other. His is enormously the brighter. So why is only hers doing anything at all?

## The physics

Suhani's photocell is the standard photoelectric apparatus in miniature. Light enters an evacuated tube through a quartz window — ordinary glass absorbs ultraviolet — and strikes an **emitter** plate. Electrons knocked out of it cross to a **collector** plate, and a microammeter reads the resulting **photocurrent**. A battery with a sliding contact sets the voltage between the plates, and it can be made either sign.

![A labelled diagram of a photocell: light through a quartz window onto the emitter, electrons crossing to the collector, with a microammeter, a voltmeter and a battery with a sliding contact](figures/photoelectric_observations/photocell-apparatus.svg "Three things you can change independently: the brightness, the frequency, and the plate voltage.")

Turn those three controls and you get four results, and they are stubborn.

**1. Brightness controls how many.** At a fixed frequency above threshold, the photocurrent is proportional to the intensity. Make the collector positive enough and every emitted electron is swept across, so the current levels off at a **saturation current** — double the brightness and that plateau doubles.

**2. Brightness does not control how fast.** Make the collector *negative* and it repels the electrons. At one particular retarding voltage even the fastest electron is turned back and the current reaches zero. That voltage is the **stopping potential** $V_0$, and it measures the maximum kinetic energy directly:

$$K_\text{max} = eV_0$$

Dimming the lamp does not shift $V_0$ by a millivolt.

![Two graphs of photocurrent against collector potential: on the left, two brightnesses of the same colour reaching different plateaus but the same stopping potential; on the right, two frequencies with different stopping potentials](figures/photoelectric_observations/photocurrent-vs-potential.svg "Left: brightness moves the plateau, not the intercept. Right: frequency moves the intercept.")

**3. Frequency controls how fast — and whether anything happens at all.** Each emitter metal has a **threshold frequency** $\nu_0$. Below it no electrons come out, however bright the light and however long you wait. Above it, $V_0$ climbs steadily as the frequency rises.

**4. Emission is immediate.** The current appears within about $10^{-9}\,\text{s}$ of the light arriving, even when the light is very faint.

Now set that against the wave theory, which treats a light wave's energy as spread smoothly over the whole wavefront. It predicts the opposite on every count: a brighter wave should shake electrons out faster (it doesn't), any frequency should work if you wait long enough for the energy to pile up (it doesn't), and faint light should show a measurable delay while that happens (it doesn't).

Tejas's red lamp was below the threshold frequency of that emitter. No amount of brightness could rescue it. Suhani's ultraviolet ticket lamp was above it, and a trickle of ultraviolet beat a flood of red.

## Worked example

**Given:** with one lamp at a fixed frequency, the photocell settles at a saturation current of $8.0\,\mu\text{A}$.

**Find:** how many electrons leave the emitter each second, and what the current becomes with a lamp of the same colour that is twice as bright.

Saturation means every emitted electron is being collected, so the current is simply the charge arriving each second:

$$n = \frac{I}{e} = \frac{8.0 \times 10^{-6}}{1.6 \times 10^{-19}} = 5.0 \times 10^{13}\ \text{electrons per second}$$

Fifty million million electrons every second — and a microammeter calls that a *small* current.

Twice as bright means twice as many photons arriving each second at the same energy each, so twice as many electrons:

$$I = 2 \times 8.0 = 16\,\mu\text{A}$$

and the stopping potential is exactly where it was.

**Sanity check:** a few microamps is a tiny current and yet involves an unimaginable number of electrons, which is what you should expect when one electron carries only $1.6 \times 10^{-19}\,\text{C}$.

## Where the picture breaks

The demonstration cell is a stripped-down version of the sensors in a real camera. Most modern light sensors are semiconductor photodiodes, where light frees charges *inside* a solid rather than into a vacuum. There is still a threshold; the details are different.

Two honest limits on the observations themselves. "Nothing below $\nu_0$" is a statement about ordinary light sources — with an intense laser two photons can occasionally act on one electron together, which is outside this syllabus. And $\nu_0$ is a property of the *metal*, not of light: change the emitter and Tejas's red lamp might work perfectly well.

Football supplies the setting, not an analogy. A ticket lamp and a goal-line camera are real devices that really behave this way, and that is the whole of the connection.

## Key takeaway

Intensity fixes **how many** photoelectrons come out; frequency fixes **how fast** the fastest one is, through $K_\text{max} = eV_0$. Below the threshold frequency $\nu_0$ nothing comes out at all, however bright the light, and above it emission begins with no measurable delay. Energy spread smoothly over a wavefront cannot explain any of that.
