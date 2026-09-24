---
concept_id: magnetic_flux
interest: gaming
format: explain
title: The arcade card that only works one way up
check:
  question: |-
    Vedika's card lies flat on the reader and the flux through its coil is $\Phi$. Which of these changes would leave $\Phi$ exactly as it is?
  options:
    A: |-
      Turning the card until its plane is vertical, edge-on to the reader.
    B: |-
      Sliding the card to the edge of the reader, where the field is weaker.
    C: |-
      Spinning the card in its own plane, about its normal, without tilting it.
    D: |-
      Squashing the coil inside the card to half its area, still lying flat.
  answer: C
  explanation: |-
    $\Phi = BA\cos\theta$ depends on the field, the area and the tilt. Spinning the card about its own normal changes none of the three, so the flux is unchanged.
  misconceptions:
    A: |-
      Treats orientation as irrelevant — but edge-on means $\theta = 90^\circ$ and $\cos 90^\circ = 0$, so the flux falls to zero. Orientation is exactly what does change it.
    B: |-
      Assumes the flux belongs to the card alone. It depends on the field **at the coil**, so moving into a weaker field lowers $B$ and lowers the flux.
    D: |-
      Forgets that area is one of the three things flux depends on. Halve $A$ at the same field and tilt, and the flux halves too.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming corner at night: a pinball game on the monitor, a headset charging on a pad, a controller cut away at its rumble motor, a tablet pen hovering over a tablet, and an arcade coin chute with a magnet](scenes/gaming/electromagnetic_induction.svg "Five gaming machines, one idea: each of them works because a magnetic field somewhere inside is changing. This lesson starts with what a coil actually catches.")

Vedika has twelve minutes of lunch break left and an arcade card with three credits on it. At the racing cabinet she lays the card flat on the reader panel. It beeps, a credit disappears, the game wakes up.

Next cabinet. This time the card is wedged between two fingers and she taps it **edge-on**, the card's thin side pressed against the panel. Nothing. Again, harder, right up against the plastic. Nothing.

Her cousin takes the card off her, drops it flat on the reader, and it beeps first time.

Same card, same reader, same distance — she was pressing *harder* on the attempts that failed. The only thing that changed was which way the card was facing. And the card has no battery, so whatever the reader is offering, the card has to catch it. What is it catching, and why does turning it sideways switch it off?

## The physics

Inside the card is a flat coil of wire, wound round and round just under the plastic. The reader's own coil fills the space above the panel with a magnetic field. What the card can catch is how much of that field passes *through* its coil — the **magnetic flux**.

For a flat surface of area $A$ in a uniform magnetic field $\vec{B}$,

$$\Phi_B = \vec{B} \cdot \vec{A} = BA\cos\theta$$

- $B$ is the magnetic field strength, in tesla (T).
- $A$ is the area of the surface, in $\text{m}^2$.
- $\theta$ is the angle between $\vec{B}$ and the **normal** to the surface — the line sticking straight out of the card's face, not any line drawn on the card.
- $\Phi_B$ is measured in **weber** (Wb), and $1\,\text{Wb} = 1\,\text{T}\,\text{m}^2$.

Flux is a scalar. The useful picture is that it counts the field lines threading the surface.

![Three panels showing a flat loop edge-on in a uniform field at 0, 60 and 90 degrees, with the flux falling from BA to half of BA to zero](figures/magnetic_flux/flux-vs-tilt.svg "The field and the loop's area never change across these three panels — only the tilt. Half the flux is gone at 60 degrees, and all of it at 90 degrees.")

That is Vedika's card. Flat on the panel, the normal points along the field: $\theta \approx 0$, $\cos\theta = 1$, flux at its maximum. Edge-on, the field skims along the card's face: $\theta = 90^\circ$, $\cos 90^\circ = 0$, and the coil catches nothing at all.

The formula assumes $\vec{B}$ is **uniform** across the surface and the surface is **flat**. If the field varies, you add up $\vec{B}\cdot d\vec{A}$ over the surface instead.

Three things can change the flux, and only these three: change $B$, change $A$, or change the angle $\theta$. Keep that list — the whole chapter is built on it.

## Worked example

**Given:** the coil inside the card encloses $A = 0.005\,\text{m}^2$, about the area of the card itself. Just above the reader's surface the field is a few microtesla; take an illustrative $B = 4\times10^{-6}\,\text{T}$.
**Find:** the flux through the coil lying flat, and with the card tilted so the field is at $60^\circ$ to its normal.

Lying flat means $\theta = 0$ and $\cos 0 = 1$:

$$\Phi_B = BA = (4\times10^{-6}) \times 0.005 = 2\times10^{-8}\,\text{Wb}$$

That is the most this coil can catch in this field — every line that can thread it, does. Twenty billionths of a weber is a minute amount, which is why the card's coil has so many turns.

Now tilt the card until $\theta = 60^\circ$, where $\cos 60^\circ = 0.5$:

$$\Phi_B = BA\cos 60^\circ = (2\times10^{-8}) \times 0.5 = 1\times10^{-8}\,\text{Wb}$$

Half the flux, and the card never moved away from the reader.

**Sanity check:** as the tilt runs from $0^\circ$ to $90^\circ$ the flux must slide from its full value down to zero, so a value half-way between the two is exactly what a middling tilt should give.

## Where the picture breaks

"Counting field lines" is a picture, not a definition. Lines are drawn by us and you can always draw twice as many; flux is the quantity $BA\cos\theta$.

The reader's field is also nothing like uniform. It is strongest directly over the reader's coil and falls away quickly, so using one value of $B$ across the whole card is an approximation — the honest version adds up $\vec{B}\cdot d\vec{A}$ over the coil.

And catching flux is not yet enough to run a card. The chip is powered by flux that *changes*, not by flux that merely exists, which is the next lesson. Edge-on there is no flux at any instant, so there is nothing to change either — which is why nothing happened.

The gaming is the setting here, not an analogy: an arcade card is simply a coil you carry in your pocket. There is no "flux" of credits or scores.

## Key takeaway

Magnetic flux through a flat surface is $\Phi_B = BA\cos\theta$, measured in weber, where $\theta$ is the angle between the field and the **normal** to the surface. It is largest when the surface faces the field squarely and zero when the field skims along it. Flux can change in exactly three ways: change $B$, change $A$, or turn the surface.
