---
concept_id: photoelectric_observations
interest: smartphones
format: explain
title: The photocell that ignored a bright red screen
check:
  question: |-
    A phone flashlight shines on a photocell and produces a photocurrent. The light's frequency is above threshold. The flashlight is then made twice as intense, with its colour unchanged. What happens?
  options:
    A: |-
      The stopping potential doubles, because each electron now receives twice as much energy; the saturation current stays the same.
    B: |-
      The saturation current and the stopping potential both double, because the beam carries twice the energy.
    C: |-
      Nothing changes, because only the frequency of the light can affect the photoelectric effect.
    D: |-
      The saturation current doubles, but the stopping potential stays the same.
  answer: D
  explanation: |-
    Intensity sets how many electrons are emitted each second, so the saturation current is proportional to it. The maximum kinetic energy of each electron, and hence the stopping potential, depends only on the frequency, which has not changed.
  misconceptions:
    A: |-
      This is the wave-theory prediction: brighter light shakes each electron harder, so each should leave faster. Experiment shows the opposite — the stopping potential does not depend on intensity at all.
    B: |-
      Right about the current, wrong about the energy. Twice the energy in the beam goes into twice as many electrons, not into faster ones.
    C: |-
      Overcorrects: frequency alone sets the electrons' maximum energy, but intensity still decides how many come out, so the current does change.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A phone beside a sunny window, its screen showing a UV-index meter, its flashlight beam drawn half as a wave and half as a stream of packets, and a magnified camera pixel where light frees electrons](scenes/smartphones/dual_nature.svg "A phone gives out light in two very different ways: the coloured glow of its screen and the white beam of its flashlight.")

Meera and Kabir have borrowed an old vacuum photocell from their school lab in Kochi for the science exhibition. It is a glass bulb with a curved metal plate inside, wired to a microammeter. Light on the plate should move the needle.

Meera switches on her phone's flashlight and holds it close. The needle jumps.

Kabir has a better idea. He opens a plain red image on his phone, turns the screen to full brightness and presses it right against the bulb. The whole cell glows red. The needle does not move — not a flicker.

Meera, laughing, walks to the far end of the table and points her flashlight at the cell from there. It is much dimmer now. The needle still moves, less than before, but instantly.

A bright red screen, pressed right against the cell, does nothing. A dim flashlight from across the table works at once. How can dimmer light do more?

## The physics

The photocell is a vacuum tube with two electrodes. Light falls on the **emitter** (the curved plate); electrons knocked out cross the vacuum to the **collector**. A microammeter measures the **photocurrent**, and a battery with a sliding contact lets you set the collector's potential, positive or negative, relative to the emitter.

![A labelled diagram of a photocell: light through a quartz window onto the emitter, electrons crossing to the collector, with a microammeter, a voltmeter and a battery with a sliding contact](figures/photoelectric_observations/photocell-apparatus.svg "Three things you can change independently: the brightness, the frequency, and the plate voltage.")

Experiments with a cell like this give four results.

1. **Threshold frequency.** For each metal there is a minimum frequency $\nu_0$. Below it there is no emission at all, however intense the light. Kabir's red screen was below the threshold of this emitter.
2. **Intensity sets the current.** Above $\nu_0$, the photocurrent is proportional to the intensity. Make the collector more positive and the current rises to a **saturation current**, when every emitted electron is collected. Double the intensity and the saturation current doubles.
3. **Frequency sets the energy.** Make the collector negative and fewer electrons reach it. At the **stopping potential** $V_0$ even the fastest are turned back, so $K_\text{max} = eV_0$. $V_0$ does *not* depend on intensity, but it rises steadily with frequency.
4. **No delay.** Emission starts within about $10^{-9}\,\text{s}$ of the light arriving, even when the light is very dim.

![Two graphs of photocurrent against collector potential: on the left, two brightnesses of the same colour reaching different plateaus but the same stopping potential; on the right, two frequencies reaching the same plateau but different stopping potentials](figures/photoelectric_observations/photocurrent-vs-potential.svg "Left: brightness moves the plateau, not the intercept. Right: frequency moves the intercept, not the plateau.")

**Why the wave theory fails.** A light wave's energy is spread over the whole wavefront and grows with intensity. So the wave theory predicts that brighter light should give faster electrons (result 3 says no), that any frequency should work if it is bright enough (result 1 says no), and that dim light should need time for an electron to soak up enough energy (result 4 says no). All three predictions fail. The next lesson explains why.

## Worked example

**Given:** Meera's flashlight at a fixed distance gives a saturation current of $2.0\,\mu\text{A}$ and a stopping potential of $0.5\,\text{V}$ (illustrative values). She moves it closer until the light is twice as intense.
**Find:** the fastest electrons' kinetic energy, and the new current and stopping potential.

The fastest electrons first. They are just stopped by $0.5\,\text{V}$, so

$$K_\text{max} = eV_0 = 0.5\,\text{eV} = 0.5 \times 1.6\times10^{-19} = 8.0\times10^{-20}\,\text{J}$$

That is the energy of the fastest electron leaving the plate.

Next, how many electrons arrive each second at saturation:

$$\frac{2.0\times10^{-6}\,\text{A}}{1.6\times10^{-19}\,\text{C}} = 1.25\times10^{13}\ \text{per second}$$

Twice the intensity means twice as many electrons, so the saturation current becomes $4.0\,\mu\text{A}$.

The stopping potential stays at $0.5\,\text{V}$: the colour has not changed, so neither has the energy of the fastest electrons.

**Sanity check:** Meera made the light brighter, not bluer, so more electrons come out but none come out faster — just what result 3 says.

## Where the picture breaks

A phone flashlight is a white LED: its light is a spread of colours, with a strong blue part. The emitter responds only to the part above its threshold, so here the blue light does all the work and the stopping potential belongs to the bluest light present. With a single-colour source the graphs would be cleaner.

The red screen was not "too dim" — it was the wrong colour. Even a very bright red lamp would leave the needle still. That is the whole puzzle, and why it cannot be explained by energy spreading out through a wave.

Finally, this photocell has a metal plate in a vacuum. The camera in the same phone uses silicon and never lets electrons out of the material, so it responds to red light as well. Different device, different threshold.

## Key takeaway

Photoelectric emission needs light above a **threshold frequency**, whatever the intensity. Above it, the **intensity** sets how many electrons come out (the saturation current), the **frequency** sets their maximum energy (the stopping potential, $K_\text{max} = eV_0$), and emission is instantaneous. The wave theory predicted the opposite on all three counts.
