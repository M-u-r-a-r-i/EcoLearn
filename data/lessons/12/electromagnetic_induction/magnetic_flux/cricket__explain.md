---
concept_id: magnetic_flux
interest: cricket
format: explain
title: The tiffin lid that only sets off the gate alarm one way up
check:
  question: |-
    A flat rectangular coil of area $0.02\,\text{m}^2$ sits in a uniform field of $0.5\,\text{T}$. The coil is turned until its plane is **parallel** to the field. What is the flux through it now?
  options:
    A: |-
      $0.01\,\text{Wb}$
    B: |-
      $0$
    C: |-
      $0.005\,\text{Wb}$
    D: |-
      $25\,\text{Wb}$
  answer: B
  explanation: |-
    When the plane of the coil is parallel to $\vec{B}$, the normal to the coil is at $90^\circ$ to the field, and $\Phi = BA\cos 90^\circ = 0$. No field lines pass through the loop.
  misconceptions:
    A: |-
      Uses $\Phi = BA$ regardless of orientation — the maximum value, which only applies when the field is along the normal, not along the plane.
    C: |-
      Takes "parallel to the field" to mean an angle of $60^\circ$ and halves the answer; the angle in $\cos\theta$ is between the field and the **normal**, not the plane.
    D: |-
      Divides $B$ by $A$ instead of multiplying, which also gives the wrong units ($\text{T/m}^2$, not weber).
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![An evening cricket ground with a walk-through metal-detector arch at the gate, LED bails charging on a pad, and a bowling machine](scenes/cricket/electromagnetic_induction.svg "Three machines at one ground — a gate detector, a charging pad and a motor — and all three work because a magnetic field is changing somewhere inside them.")

Aarav is in the queue at the gate for a day-night match, holding his mother's steel tiffin box. The security guard waves him through the metal-detector arch. Nothing. He steps back, embarrassed — he was sure it would beep — and walks through again, this time carrying the tiffin flat, like a tray.

The alarm goes off at once.

Same box, same arch, same walk. The only thing Aarav changed was the way he was *holding* it. The guard grins and says it happens twenty times an evening.

So what does the arch actually sense? It cannot be "how much metal", because the amount of metal never changed. Something about the box's **orientation** in the arch's magnetic field has to matter — and that something has a name.

## The physics

The arch has coils in its pillars that fill the gap with a magnetic field. What the detector reacts to is how much of that field passes *through* the metal object — its **magnetic flux**.

For a flat surface of area $A$ in a uniform magnetic field $\vec{B}$, the magnetic flux is the dot product

$$\Phi_B = \vec{B} \cdot \vec{A} = BA\cos\theta$$

- $B$ is the magnetic field strength, in tesla (T).
- $A$ is the area of the surface, in $\text{m}^2$.
- $\theta$ is the angle between $\vec{B}$ and the **normal** to the surface — the line sticking straight out of it, not the surface itself.
- $\Phi_B$ is measured in **weber** (Wb), and $1\,\text{Wb} = 1\,\text{T}\,\text{m}^2$.

Flux is a scalar. A useful picture: it counts the number of field lines threading the surface.

![Three panels showing a flat loop edge-on in a uniform field at 0, 60 and 90 degrees, with the flux falling from BA to half of BA to zero](figures/magnetic_flux/flux-vs-tilt.svg "Turning the loop changes nothing about the field or the area — but the flux falls to half at 60 degrees and to zero when the field skims along the plane.")

That is Aarav's tiffin. Held edge-on, the field skimmed along the lid: $\theta = 90^\circ$, $\cos\theta = 0$, almost no flux. Held flat, the field ran straight through the lid: $\theta$ near $0^\circ$, flux near its maximum.

This formula assumes $\vec{B}$ is **uniform** over the surface and the surface is **flat**. If the field varies, you add up $\vec{B}\cdot d\vec{A}$ over the surface instead.

Three things can change the flux, and only these three: change $B$, change $A$, or change the angle $\theta$. Hold that list — the whole of this chapter is built on it.

## Worked example

**Given:** a flat search coil of area $A = 0.02\,\text{m}^2$ (about the size of the tiffin lid) in a uniform field $B = 0.5\,\text{T}$.
**Find:** the flux when the coil faces the field squarely, and when it is tilted to $\theta = 60^\circ$.

Facing the field squarely means $\theta = 0$ and $\cos 0 = 1$:

$$\Phi_B = BA = 0.5 \times 0.02 = 0.01\,\text{Wb}$$

That is the most this coil can ever get in this field — every field line that can go through, does.

Now tilt it to $\theta = 60^\circ$, where $\cos 60^\circ = 0.5$:

$$\Phi_B = BA\cos 60^\circ = 0.01 \times 0.5 = 0.005\,\text{Wb}$$

Half the flux, from a tilt of just $60^\circ$ — and the coil never moved from the field.

**Sanity check:** the flux has to sit between $0.01\,\text{Wb}$ and zero as the tilt goes from $0^\circ$ to $90^\circ$, and $0.005\,\text{Wb}$ is right in the middle of that range.

## Where the picture breaks

"Counting field lines" is a picture, not a definition — field lines are drawn by us, and you can always draw twice as many. Flux is the quantity $BA\cos\theta$; the lines are just a way to feel it.

The real gate arch is also more subtle than one flat lid in a uniform field. Its field is not uniform across the whole doorway, a tiffin box is a three-dimensional object rather than a flat sheet, and a practical detector responds to the *changing* currents induced in the metal, not to flux alone. What survives all of that is the one idea you need here: orientation matters as much as size.

And note the cricket connection is the setting, not an analogy. There is no "flux" of runs or wickets; the arch is simply a place where this physics genuinely happens.

## Key takeaway

Magnetic flux through a flat surface is $\Phi_B = BA\cos\theta$, measured in weber, where $\theta$ is the angle between the field and the **normal** to the surface. It is largest when the surface faces the field squarely and zero when the field skims along it. Flux changes in exactly three ways: change $B$, change $A$, or turn the surface.
