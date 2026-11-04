---
concept_id: photoelectric_observations
interest: cricket
format: explain
title: The bright red lamp the light meter ignored
check:
  question: |-
    Light of a fixed frequency, well above the threshold, falls on the emitter of a photocell. The brightness of the light is then doubled, with nothing else changed. What happens?
  options:
    A: |-
      Both the saturation current and the stopping potential double.
    B: |-
      The stopping potential doubles; the saturation current stays the same.
    C: |-
      The saturation current doubles; the stopping potential stays the same.
    D: |-
      Neither changes — only a change of frequency changes anything.
  answer: C
  explanation: |-
    Doubling the brightness doubles the number of photons arriving each second, so twice as many electrons are freed and the saturation current doubles. Each photon still carries the same energy, so the fastest electron is no faster and the stopping potential is unchanged.
  misconceptions:
    A: |-
      The wave-theory idea that brighter light means more energetic electrons as well as more of them. Brightness sets how many, frequency sets how fast.
    B: |-
      Swaps the two roles entirely, treating intensity as the thing that controls electron energy. It is frequency that fixes the stopping potential.
    D: |-
      Over-corrects the rule "only frequency matters". Frequency controls the *energy* of each electron; the *number* of electrons still follows the brightness.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit cricket ground at night, with a light beam drawn half as a wave and half as a stream of packets, an umpire holding a light meter and a tracking camera on a tripod](scenes/cricket/dual_nature.svg "The umpire's meter turns light into a current — and it is very fussy about which light.")

Practice was called off for bad light, and Rehan is annoyed. "It's not even dark. The umpires just want their tea."

Sana, who helps in the physics lab, has an idea. She borrows the demonstration photocell — a small evacuated bulb wired to a meter — and sets it on the bench beside the nets.

Rehan grabs his bike's red lamp, the brightest thing in his bag, and shines it straight at the cell from a few centimetres away. The needle does not move. He moves closer. Still nothing.

Sana takes out a keychain torch with a faint violet LED, holds it a good metre away, and the needle swings across the dial.

Rehan stares. His lamp is obviously brighter. Hers is barely visible. So why does only hers make a current?

## The physics

Sana's photocell is the standard photoelectric apparatus in miniature: light enters an evacuated tube through a quartz window (ordinary glass absorbs ultraviolet) and strikes an **emitter** plate. Electrons knocked out of it cross to a **collector** plate, and a microammeter reads the resulting **photocurrent**. A battery with a sliding contact sets the voltage between the plates, and it can be made either sign.

![A labelled diagram of a photocell: light through a quartz window onto the emitter, electrons crossing to the collector, with a microammeter, a voltmeter and a battery with a sliding contact](figures/photoelectric_observations/photocell-apparatus.svg "Three things you can change independently: the brightness, the frequency, and the plate voltage.")

Turn those three dials and you get four results, and they are stubborn.

**1. Brightness controls how many.** For a fixed frequency above threshold, the photocurrent is proportional to the intensity. Make the collector positive enough and every emitted electron is swept across, so the current levels off at a **saturation current** — double the brightness, double that plateau.

**2. Brightness does not control how fast.** Make the collector *negative* and it repels the electrons. At a particular retarding voltage even the fastest electron is turned back and the current falls to zero. That voltage is the **stopping potential** $V_0$, and

$$K_\text{max} = eV_0$$

Doubling the brightness does not shift $V_0$ by even a millivolt.

![Two graphs of photocurrent against collector potential: on the left, two brightnesses of the same colour reaching different plateaus but the same stopping potential; on the right, two frequencies reaching the same plateau but different stopping potentials](figures/photoelectric_observations/photocurrent-vs-potential.svg "Left: brightness moves the plateau, not the intercept. Right: frequency moves the intercept, not the plateau.")

**3. Frequency controls how fast — and whether anything happens at all.** Each metal has a **threshold frequency** $\nu_0$. Below it, no electrons are emitted however bright the light or however long you wait. Above it, $V_0$ rises steadily with frequency.

**4. Emission is immediate.** The current appears within about $10^{-9}\,\text{s}$ of the light arriving, even for very faint light.

Now compare that with the wave theory of light, which treats a light wave's energy as spread smoothly over the whole wavefront. It predicts the opposite on every count: a brighter wave should shake electrons out faster (it doesn't), any frequency should work if you wait long enough for enough energy to pile up (it doesn't), and faint light should show a measurable delay while that energy accumulates (it doesn't).

Rehan's red lamp was below the threshold frequency of that emitter. Brightness could not rescue it.

## Worked example

**Given:** light of one fixed frequency on a photocell gives a stopping potential of $V_0 = 1.5\,\text{V}$.
**Find:** the maximum kinetic energy of the emitted electrons, and what happens to $V_0$ if the lamp is made twice as bright.

The stopping potential is the retarding voltage that just turns back the fastest electron, so

$$K_\text{max} = eV_0 = 1.5\,\text{eV}$$

In joules that is $1.5 \times 1.6 \times 10^{-19} = 2.4 \times 10^{-19}\,\text{J}$ — the whole energy budget of one escaping electron.

Now double the brightness. Twice as many photons arrive each second, so twice as many electrons are freed and the saturation current doubles. But each packet of light is unchanged, so the fastest electron is no faster: $V_0$ stays at $1.5\,\text{V}$.

**Sanity check:** a single torch cell could stop these electrons dead, which tells you how small a photoelectron's energy really is.

## Where the picture breaks

The photocell on the bench is a stripped-down version of what sits inside a real light meter; most modern meters use semiconductor photodiodes, where light frees charges inside a solid rather than into a vacuum. The physics of a threshold is the same; the details are not.

Two honest limits on the observations themselves. "No emission below $\nu_0$" is a statement about ordinary light sources — with an extremely intense laser two photons can occasionally act together, which is outside this syllabus. And $\nu_0$ is not a property of light alone: change the emitter metal and the same red lamp might work perfectly well.

Cricket supplies the setting, not an analogy. A light meter at a ground is a real photoelectric device, and that is the whole of the connection.

## Key takeaway

Intensity fixes **how many** photoelectrons come out; frequency fixes **how fast** the fastest one is, through $K_\text{max} = eV_0$. Below the threshold frequency $\nu_0$ nothing at all comes out, however bright the light, and above it emission starts instantly. A wave spread smoothly over space cannot explain any of that.
