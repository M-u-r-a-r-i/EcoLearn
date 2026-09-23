---
concept_id: magnetic_flux
interest: football
format: explain
title: The gate pass that works flat but not edge-on
check:
  question: |-
    A flat coil of area $0.004\,\text{m}^2$ sits in a uniform field of $0.05\,\text{T}$. It is turned until the **normal** to the coil makes $60^\circ$ with the field. What is the flux through it?
  options:
    A: |-
      $2\times10^{-4}\,\text{Wb}$
    B: |-
      $1.7\times10^{-4}\,\text{Wb}$
    C: |-
      $1\times10^{-4}\,\text{Wb}$
    D: |-
      $0$
  answer: C
  explanation: |-
    $\Phi_B = BA\cos\theta = 0.05 \times 0.004 \times \cos 60^\circ = 2\times10^{-4} \times 0.5 = 1\times10^{-4}\,\text{Wb}$.
  misconceptions:
    A: |-
      Uses $\Phi = BA$ and ignores the tilt. That is the maximum flux, which you only get when the field runs along the normal ($\theta = 0$).
    B: |-
      Takes $60^\circ$ as the angle between the field and the **plane** of the coil, so uses $\cos 30^\circ$. In $\Phi = BA\cos\theta$, $\theta$ is measured from the normal.
    D: |-
      Reads any tilt as "the field skims the coil". The flux is zero only at $\theta = 90^\circ$, when the field lies entirely in the plane of the coil.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening football training ground with a contactless card reader at the turnstile, a magnetic-brake training bike on the touchline and a floodlight transformer cabinet](scenes/football/electromagnetic_induction.svg "Three machines around one ground — a gate reader, a brake with nothing touching it, and a transformer — and every one of them works because a magnetic field is changing somewhere inside it.")

Meera is late for the evening session and the queue at Gate 3 is not moving because of her. Her pass is in her hand, she is holding it against the reader, and the little light stays red.

The volunteer behind her leans over. "Turn it flat."

Meera has been holding the card on its edge, like a knife, pressed right against the reader panel. She lays it flat instead, barely touching, and the light goes green immediately.

She steps through, then steps back and tries it edge-on again, out of pure irritation. Red. Flat. Green. Edge-on. Red.

The card never moved further away. Nothing about the card changed. There is no battery in it and no contact anywhere. So what does the reader actually care about — and why does *turning* the card switch it off?

## The physics

Inside the reader panel is a coil that fills the space in front of it with a magnetic field. Inside the plastic of the card is another coil — a few loops of very fine wire around its edge. The card wakes up only when enough of the reader's field passes **through** that loop. The quantity that measures "how much field passes through a loop" is **magnetic flux**.

For a flat surface of area $A$ in a uniform magnetic field $\vec{B}$,

$$\Phi_B = \vec{B} \cdot \vec{A} = BA\cos\theta$$

- $B$ is the field strength, in tesla (T).
- $A$ is the area of the surface, in $\text{m}^2$.
- $\theta$ is the angle between $\vec{B}$ and the **normal** to the surface — the line sticking straight out of the card's face, not a line drawn along it.
- $\Phi_B$ is measured in **weber** (Wb), with $1\,\text{Wb} = 1\,\text{T}\,\text{m}^2$.

Flux is a scalar, not a vector. A useful picture is that it counts the field lines threading the loop.

![Three panels showing a flat loop edge-on in a uniform field at 0, 60 and 90 degrees, with the flux falling from BA to half of BA to zero](figures/magnetic_flux/flux-vs-tilt.svg "The field and the area never change across these three panels — only the tilt does. Half the flux is gone by 60 degrees, and all of it by 90 degrees.")

That is Meera's card. Flat against the panel, the field runs straight through the loop: $\theta$ near $0^\circ$, flux near its maximum. Edge-on, the field skims along the card without crossing the loop: $\theta = 90^\circ$, $\cos 90^\circ = 0$, no flux, no power, red light.

The formula assumes $\vec{B}$ is **uniform** over the surface and the surface is **flat**. If the field varies from place to place you must add up $\vec{B}\cdot d\vec{A}$ over the surface instead.

And notice what the formula allows. There are exactly three ways to change the flux through a loop: change $B$, change $A$, or turn the loop to change $\theta$. Keep that list — the rest of this chapter is built on it.

## Worked example

**Given:** a flat coil the size of a gate pass, $A = 0.005\,\text{m}^2$, held in a uniform field $B = 0.02\,\text{T}$ (the field of a school lab magnet; a real reader's field is far weaker).
**Find:** the flux when the coil faces the field squarely, and when it is tilted to $\theta = 60^\circ$.

Facing the field squarely means $\theta = 0$ and $\cos 0 = 1$:

$$\Phi_B = BA = 0.02 \times 0.005 = 1\times10^{-4}\,\text{Wb}$$

That is the most this coil can get in this field — every line that can thread it, does. A tenth of a milliweber sounds tiny, and it is: a weber is an enormous amount of flux.

Now tilt it to $\theta = 60^\circ$, where $\cos 60^\circ = 0.5$:

$$\Phi_B = BA\cos 60^\circ = 1\times10^{-4} \times 0.5 = 5\times10^{-5}\,\text{Wb}$$

Half the flux is gone, and the coil never moved out of the field — it was only turned.

**Sanity check:** the answer has to lie between the full $1\times10^{-4}\,\text{Wb}$ at $0^\circ$ and zero at $90^\circ$, and $60^\circ$ landing halfway is exactly what $\cos 60^\circ = 0.5$ says.

## Where the picture breaks

"Counting field lines" is a picture, not a definition. We draw the lines, and we could always draw twice as many. Flux is the number $BA\cos\theta$; the lines are only a way to feel it.

The gate is also more subtle than one flat loop in a uniform field. The reader's field spreads and weakens fast, so distance matters as much as angle — which is why the card must be close *and* flat. A real pass also uses an **alternating** field, because as you will see next, a steady flux does nothing at all; and the card's electronics, not just its coil, decide whether the light turns green.

The football here is the setting, not an analogy. There is no "flux" of passes or possession — a turnstile is simply a place where this physics genuinely happens.

## Key takeaway

Magnetic flux through a flat surface is $\Phi_B = BA\cos\theta$, in weber, where $\theta$ is measured between the field and the **normal** to the surface. It is largest when the surface faces the field squarely and zero when the field skims along it. Only three things can change it: $B$, $A$, or the angle.
