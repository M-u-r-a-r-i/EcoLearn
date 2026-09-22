---
concept_id: electric_flux
interest: cricket
format: explain
title: Why slanting rain soaks the sightscreen
check:
  question: |-
    A flat surface of area $0.20\,\text{m}^2$ sits in a uniform electric field of $500\,\text{N/C}$. The field lines make an angle of $30^\circ$ with the plane of the surface itself. What is the electric flux through the surface?
  options:
    A: |-
      $87\,\text{N m}^2/\text{C}$
    B: |-
      $100\,\text{N m}^2/\text{C}$
    C: |-
      $50\,\text{N m}^2/\text{C}$
    D: |-
      $2500\,\text{N m}^2/\text{C}$
  answer: C
  explanation: |-
    The angle in $\Phi = EA\cos\theta$ is measured from the normal. If the field is at $30^\circ$ to the surface, it is at $60^\circ$ to the normal, so $\Phi = 500 \times 0.20 \times \cos 60^\circ = 50\,\text{N m}^2/\text{C}$.
  misconceptions:
    A: |-
      Puts the angle to the surface into the formula ($\cos 30^\circ$), but $\theta$ is the angle between $\vec{E}$ and the normal to the surface.
    B: |-
      Uses $\Phi = EA$ and ignores the tilt, as if the field always crossed the surface head-on.
    D: |-
      Divides the field by the area; flux is field times area (times the cosine), not field per unit area.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A storm over a cricket ground: dark clouds, distant lightning, players walking off, groundstaff dragging a plastic cover and a team bus waiting](scenes/cricket/electric_charges_fields.svg "Rain on the covers: how much of it lands on a sheet depends on the angle.")

Harpreet is in her first season on the groundstaff, and today she learns what the head groundsman means by "the wrong kind of rain".

In the morning, a heavy shower falls straight down on a windless ground. The flat covers over the square catch all of it; the tall white sightscreen at the end of the ground barely gets wet.

In the afternoon, a second storm arrives on a strong wind, and the rain drives in at a steep slant. Now the sightscreen, standing upright, is drenched, and the flat covers catch less than before, even though it's raining just as hard.

Harpreet sketches it in her notebook. Same rain, same sheets, very different amounts getting through, all because of the angle. Physicists count the electric field crossing a surface in exactly this way. What's the rule that connects the angle to the amount?

## The physics

The quantity that measures "how much field passes through a surface" is the **electric flux**.

For a flat surface of area $\Delta S$ in a **uniform** field $\vec{E}$, we define an **area vector** $\Delta\vec{S}$: its magnitude is the area, and its direction is along the **normal** (perpendicular) to the surface. Then

$$\Delta\Phi = \vec{E} \cdot \Delta\vec{S} = E\,\Delta S\cos\theta$$

where **$\theta$ is the angle between $\vec{E}$ and the normal**, not between $\vec{E}$ and the surface. Flux is a scalar, and its unit is the $\text{N m}^2/\text{C}$.

![A flat surface seen edge-on in a uniform field: facing the field all six lines pass through; tilted with its normal at 60 degrees only three pass through; edge-on none pass through](figures/electric_flux/flux-tilted-area.svg "The flux is largest when the surface faces the field, half as big at 60 degrees, and zero when the field slides along the surface.")

- $\theta = 0^\circ$: the surface faces the field head-on, and $\Phi = EA$, the maximum.
- $\theta = 60^\circ$: $\Phi = EA\cos 60^\circ = EA/2$.
- $\theta = 90^\circ$: the field runs parallel to the surface, and $\Phi = 0$.
- $\theta > 90^\circ$: $\cos\theta$ is negative, so the flux is negative: the field crosses the surface against the chosen normal.

**Flux as a count of lines.** Field lines are drawn so that their density (lines per unit area across them) is proportional to $E$. So $E\,\Delta S\cos\theta$ is proportional to the **number of field lines crossing the surface**. That's why the tilted surface in the figure catches only half the lines: its "shadow" across the field, $\Delta S\cos\theta$, is half its area.

**Sign convention.** For an open surface you choose which side the normal points. For a **closed** surface the normal always points **outwards**, so lines leaving count as positive flux and lines entering as negative.

If the field varies, or the surface is curved, split the surface into small pieces, find $\vec{E} \cdot \Delta\vec{S}$ for each, and add: $\Phi = \sum \vec{E} \cdot \Delta\vec{S}$.

## Worked example

**Given:** a flat rectangular sheet $2.0\,\text{m} \times 1.5\,\text{m}$ in a uniform field of $400\,\text{N/C}$ (illustrative values), its normal at $60^\circ$ to the field.
**Find:** the flux, and how it changes if the sheet faces the field or is turned edge-on.

$$A = 2.0 \times 1.5 = 3.0\,\text{m}^2$$

$$\Phi = EA\cos\theta = 400 \times 3.0 \times \cos 60^\circ = 400 \times 3.0 \times 0.50 = 600\,\text{N m}^2/\text{C}$$

Facing the field ($\theta = 0^\circ$): $\Phi = 400 \times 3.0 = 1200\,\text{N m}^2/\text{C}$.
Edge-on ($\theta = 90^\circ$): $\Phi = 0$.

**Sanity check:** the tilted value is exactly half the head-on value, as $\cos 60^\circ = 0.5$ says. Units: $(\text{N/C}) \times \text{m}^2 = \text{N m}^2/\text{C}$. Correct.

## Where the picture breaks

Rain is a genuine flow: water actually moves through the surface, and a bucket measures how much. An electric field doesn't flow. Nothing travels along field lines, and "flux" here only borrows the word. The comparison works because both quantities are *something per unit area* × *area* × $\cos\theta$. Also, rain falls on only one side of a cover, but field flux can be positive or negative depending on which way the lines cross, and for a closed surface that sign is essential.

## Key takeaway

Electric flux through a flat surface in a uniform field is $\Phi = \vec{E} \cdot \Delta\vec{S} = EA\cos\theta$, where $\theta$ is measured from the **normal**. It's proportional to the number of field lines crossing the surface: largest face-on, zero edge-on. For closed surfaces, the normal points outwards.
