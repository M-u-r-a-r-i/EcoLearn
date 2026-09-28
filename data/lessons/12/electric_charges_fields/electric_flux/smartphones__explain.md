---
concept_id: electric_flux
interest: smartphones
format: explain
title: Tilting the solar power bank towards the sun
check:
  question: |-
    A flat surface of area $0.010\,\text{m}^2$ sits in a uniform electric field of $400\,\text{N/C}$. The normal to the surface makes an angle of $60^\circ$ with the field. What is the electric flux through the surface?
  options:
    A: |-
      $2.0\,\text{N m}^2/\text{C}$
    B: |-
      $3.5\,\text{N m}^2/\text{C}$
    C: |-
      $4.0\,\text{N m}^2/\text{C}$
    D: |-
      $8.0\,\text{N m}^2/\text{C}$
  answer: A
  explanation: |-
    $\Phi = EA\cos\theta = 400 \times 0.010 \times \cos 60^\circ = 4.0 \times 0.50 = 2.0\,\text{N m}^2/\text{C}$, where $\theta$ is the angle between $\vec{E}$ and the normal.
  misconceptions:
    B: |-
      Uses $\sin 60^\circ$, measuring the angle from the surface itself instead of from its normal. The flux is largest when the field is along the normal.
    C: |-
      Ignores the tilt and uses $EA$, as if the surface faced the field squarely. Only the component of $\vec{E}$ along the normal carries flux through it.
    D: |-
      Divides by $\cos 60^\circ$ instead of multiplying, as if tilting the surface made more field lines pass through it rather than fewer.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a sunny window with a solar power bank on the sill, an opened phone box with foam beads clinging to the new phone, a film being peeled off a screen with dust jumping up to it, and a phone on a stand running a field-line app](scenes/smartphones/electric_charges_fields.svg "The solar power bank on the windowsill is tilted to face the sun. Its surface catches the most when it faces the rays squarely.")

Priya's hostel room has one sunny window, and she has a small solar power bank that she props on the sill every morning before college.

Her roommate Lakshmi lays hers flat on the sill. Priya tilts hers up on a folded notebook so the panel faces the sun. By evening, Priya's charge indicator shows more bars.

"Same sun, same window, same panel," Lakshmi complains. "Why does tilting it matter?"

Priya holds up a notebook in a beam of sunlight and turns it slowly. Face-on, it throws a big shadow on the floor. Tilted, the shadow shrinks. Edge-on, there's hardly any shadow at all. "It's how much of the beam the panel actually catches," she says.

Their physics chapter is on electric fields, and Lakshmi wonders aloud: field lines fill space like sunbeams do. Is there a way to measure how much electric field "passes through" a surface, and does it depend on the tilt in the same way?

## The physics

**Electric flux** measures how much electric field passes through a surface. For a **flat** surface of area $A$ in a **uniform** field $\vec{E}$:

$$\Phi = \vec{E} \cdot \vec{A} = EA\cos\theta$$

Here $\vec{A}$ is the **area vector**: its size is the area and its direction is along the **normal** (perpendicular) to the surface. The angle $\theta$ is between $\vec{E}$ and that normal, **not** between $\vec{E}$ and the surface. Flux is a scalar, with SI unit N m²/C.

- $\theta = 0^\circ$: the surface faces the field squarely, $\Phi = EA$, the maximum.
- $\theta = 60^\circ$: $\Phi = EA/2$.
- $\theta = 90^\circ$: the field slides along the surface, $\Phi = 0$.
- $\theta > 90^\circ$: $\cos\theta < 0$, so the flux is **negative**: the field passes through the "back" of the surface.

![A flat surface seen edge-on in a uniform field: facing the field all six lines pass through; tilted with its normal at 60 degrees only three pass through; edge-on none pass through](figures/electric_flux/flux-tilted-area.svg "The flux is largest when the surface faces the field, half as big at 60 degrees, and zero when the field slides along the surface.")

**Counting lines.** If field lines are drawn so that their number per unit area (perpendicular to them) equals $E$, then flux is simply the **number of lines crossing the surface**. That is why tilting a surface reduces the flux: fewer lines get through it, just as a tilted panel catches fewer sunbeams.

For a curved surface or a varying field, split the surface into tiny pieces $d\vec{S}$ and add: $\Phi = \int \vec{E} \cdot d\vec{S}$. For a **closed** surface the normal is always taken **outwards**, so lines leaving count positive and lines entering count negative. That is the key to the next lesson.

## Worked example

**Given (illustrative):** a uniform field $E = 500\,\text{N/C}$ and a flat rectangle of area $A = 0.010\,\text{m}^2$, about the size of a phone's face.
**Find:** the flux when it faces the field, when its normal is at $60^\circ$, and when it is edge-on.

**Step 1 — face-on ($\theta = 0^\circ$).**
$$\Phi = EA = 500 \times 0.010 = 5.0\,\text{N m}^2/\text{C}$$
This is the most flux this rectangle can ever have in this field.

**Step 2 — tilted ($\theta = 60^\circ$).** $\cos 60^\circ = 0.50$, so
$$\Phi = 5.0 \times 0.50 = 2.5\,\text{N m}^2/\text{C}$$
Half the lines now get through.

**Step 3 — edge-on ($\theta = 90^\circ$).** $\cos 90^\circ = 0$, so $\Phi = 0$: every line slides past.

**Sanity check:** turning the rectangle can only lose flux, never add it, so every answer should lie between $0$ and $5.0\,\text{N m}^2/\text{C}$, and they do.

## Where the picture breaks

Sunlight is energy actually travelling from the sun to the panel; nothing travels along an electric field line, and electric flux is not a flow of anything, despite the name (from the Latin for "flow"). Electric flux can also be negative, while a panel can't catch "negative sunlight". And the power bank's charge also depends on things that have nothing to do with flux, such as heat and the sun's changing angle through the day. What the two ideas genuinely share is the geometry: both depend on $\cos\theta$, the angle between the beam and the normal.

## Key takeaway

Electric flux through a flat surface in a uniform field is $\Phi = \vec{E} \cdot \vec{A} = EA\cos\theta$, where $\theta$ is measured from the **normal**. It counts the field lines crossing the surface: largest face-on, zero edge-on, and negative when the field passes through the back. Its unit is N m²/C.
