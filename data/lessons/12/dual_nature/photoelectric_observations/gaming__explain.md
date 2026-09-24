---
concept_id: photoelectric_observations
interest: gaming
format: explain
title: The bright red strip the start gate ignored
check:
  question: |-
    A photocell gives a steady photocurrent under a dim blue LED. The blue LED is then replaced by a much brighter red one, whose frequency is below the cell's threshold frequency. What does the meter read?
  options:
    A: |-
      Zero — no current at all, however bright the red LED is and however long he waits.
    B: |-
      A small current at first, growing to the earlier value once enough light energy has piled up on the surface.
    C: |-
      A larger current than before, because the red LED is delivering far more light energy each second.
    D: |-
      The same current as before, but carried by electrons that come out with less kinetic energy.
  answer: A
  explanation: |-
    Below the threshold frequency no single packet of light carries enough energy to free an electron, so no electrons are emitted at all — brightness and patience change nothing.
  misconceptions:
    B: |-
      The wave-theory idea that energy can be collected gradually until it adds up to the escape energy. One electron absorbs one packet; there is no saving up.
    C: |-
      Treats intensity as the thing that decides whether emission happens. Intensity decides *how many* electrons come out, but only once the frequency is above threshold.
    D: |-
      Remembers that frequency sets the electrons' energy but forgets that below $\nu_0$ there are no electrons to slow down. A lower frequency does not mean feebler electrons; past the threshold it means none.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming room shown in three stages: a cut-away retro CRT cabinet with a glowing filament and an electron beam, a flat monitor whose light leaves as a wave and then as packets, and a camera sensor feeding a current to a meter](scenes/gaming/dual_nature.svg "The sensor on the right turns light into a current — and it is startlingly fussy about which light.")

Two days into the college game jam, Kabir's team is building something nobody asked for: a racing game you start by shining a light at a sensor instead of pressing a key. A demonstration photocell — a small evacuated bulb wired to a microammeter — is taped to the edge of the desk. Light on the cell means green flag.

Kabir tests it with the brightest thing in the room: the red LED strip from inside the PC case, turned all the way up, held a few centimetres away. The needle does not move. He brings it closer. Still nothing.

Sneha slides the strip's colour over to blue, drops the brightness almost to nothing, and holds it half a metre back. The needle swings across the dial before she has finished explaining what she is doing.

Kabir's light was many times brighter. Hers is barely visible. So why does only hers count?

## The physics

That photocell is the standard photoelectric apparatus in miniature. Light enters an evacuated tube through a quartz window (ordinary glass absorbs ultraviolet) and lands on an **emitter** plate. Electrons knocked out of the emitter cross to a **collector** plate, and a microammeter reads the resulting **photocurrent**. A battery with a sliding contact sets the voltage between the plates, and that voltage can be made either sign.

![A labelled diagram of a photocell: light through a quartz window onto the emitter, electrons crossing to the collector, with a microammeter, a voltmeter and a battery with a sliding contact](figures/photoelectric_observations/photocell-apparatus.svg "Three things you can change independently: the brightness, the frequency, and the plate voltage.")

Turn those three dials and four results come back, and they are stubborn.

**1. Brightness controls how many.** At a fixed frequency above threshold, the photocurrent is proportional to the intensity. Make the collector positive enough and every emitted electron is swept across, so the current levels off at a **saturation current** — double the brightness and that plateau doubles.

**2. Brightness does not control how fast.** Make the collector *negative* instead and it repels the arriving electrons. At one particular retarding voltage even the fastest electron is turned back and the current falls to zero. That voltage is the **stopping potential** $V_0$, and

$$K_\text{max} = eV_0$$

Doubling the brightness does not shift $V_0$ by a millivolt.

![Two graphs of photocurrent against collector potential: on the left, two brightnesses of one colour reaching different plateaus but the same stopping potential; on the right, two frequencies reaching the same plateau but different stopping potentials](figures/photoelectric_observations/photocurrent-vs-potential.svg "Left: brightness moves the plateau, not the intercept. Right: frequency moves the intercept, not the plateau.")

**3. Frequency controls how fast — and whether anything happens at all.** Every emitter has a **threshold frequency** $\nu_0$. Below it, no electrons come out however bright the light and however long you wait. Above it, $V_0$ climbs steadily with frequency.

**4. Emission is immediate.** The current appears within about $10^{-9}\,\text{s}$ of the light arriving, even for very faint light. A frame at $60$ frames per second lasts about $16.7\,\text{ms}$, so the whole response fits into roughly a ten-millionth of a single frame — this is not a delay any game could notice.

Set that against the wave theory of light, which treats a wave's energy as spread smoothly over the whole wavefront. It predicts the opposite on every count: a brighter wave should shake electrons out with more energy (it doesn't), any frequency should work if you wait for enough energy to accumulate (it doesn't), and very faint light should show a measurable delay while it accumulates (it doesn't).

Kabir's red strip was below the threshold frequency of that emitter. No amount of brightness could rescue it.

## Worked example

**Given:** one blue LED on the photocell gives a saturation current of $4.0\,\mu\text{A}$ and a stopping potential of $V_0 = 2.0\,\text{V}$.
**Find:** the maximum kinetic energy of the emitted electrons, and what a second identical LED alongside the first would change.

The stopping potential is the retarding voltage that just turns back the fastest electron, so

$$K_\text{max} = eV_0 = 2.0\,\text{eV}$$

In joules that is $2.0 \times 1.6 \times 10^{-19} = 3.2 \times 10^{-19}\,\text{J}$ — the whole energy budget of one escaping electron.

Now add the second LED. Twice as much light of the *same* colour arrives, so twice as many packets land each second and twice as many electrons are freed: the saturation current becomes $8.0\,\mu\text{A}$.

But each packet is exactly as energetic as before, so the fastest electron is no faster:

$$V_0 = 2.0\,\text{V}, \ \text{unchanged}$$

**Sanity check:** two lamps give you twice as much light, not fiercer light — and a single torch cell could stop these electrons dead, which tells you how small a photoelectron's energy really is.

## Where the picture breaks

The photocell on the desk is a stripped-down ancestor of what actually sits in a camera sensor. Modern sensors are semiconductor photodiodes, where light frees charges *inside* a solid rather than into a vacuum. The threshold behaviour is the same in spirit; the details and the energies are not.

Two honest limits on the observations themselves. "Nothing below $\nu_0$" is a statement about ordinary light sources — with a tightly focused, very intense laser an electron can occasionally take two photons at once, which is outside this syllabus. And $\nu_0$ belongs to the emitter, not to the light: swap the metal and Kabir's red strip might work perfectly well.

Gaming supplies the setting here, not an analogy. A light-triggered sensor on a desk is a genuine photoelectric device, and that is the whole of the connection — no part of a game mechanic behaves like an electron.

## Key takeaway

Intensity fixes **how many** photoelectrons come out; frequency fixes **how fast** the fastest one is, through $K_\text{max} = eV_0$. Below the threshold frequency $\nu_0$ nothing comes out at all, however bright the source, and above it emission starts with no measurable delay. Light spread smoothly through space as a wave cannot explain a single one of those four results.
