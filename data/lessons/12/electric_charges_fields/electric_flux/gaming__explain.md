---
concept_id: electric_flux
interest: gaming
format: explain
title: The dot product her shader forgot
check:
  question: |-
    A flat panel of area $0.40\,\text{m}^2$ sits in a uniform electric field of $500\,\text{N/C}$. The field makes an angle of $60^\circ$ with the **plane of the panel**. What is the electric flux through it?
  options:
    A: |-
      $100\,\text{N m}^2/\text{C}$
    B: |-
      $173\,\text{N m}^2/\text{C}$
    C: |-
      $200\,\text{N m}^2/\text{C}$
    D: |-
      $1250\,\text{N m}^2/\text{C}$
  answer: B
  explanation: |-
    The angle in $\Phi = EA\cos\theta$ is measured from the **normal**. A field at $60^\circ$ to the plane is at $30^\circ$ to the normal, so $\Phi = 500 \times 0.40 \times \cos 30^\circ \approx 173\,\text{N m}^2/\text{C}$.
  misconceptions:
    A: |-
      Puts the angle to the surface straight into the formula as $\cos 60^\circ$, instead of converting to the angle from the normal.
    C: |-
      Uses $\Phi = EA$ and ignores the tilt altogether, as if the field always crossed the panel head-on.
    D: |-
      Divides the field by the area. Flux is field times area times the cosine, not field per unit area.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night during a PC build: a monitor running a field sandbox with two charges, a plasma globe, an antistatic bag sparking to a fingertip, and an open PC case with a graphics card going in](scenes/gaming/electric_charges_fields.svg "The arrows on that screen cross the surfaces in the room at all sorts of angles. How much of the field gets through?")

Aarohi is three weeks into writing her own lighting for a small game, and the corridor level looks wrong in a way she cannot name. The lamp is on the ceiling. The floor beneath it looks right. The side walls, lit at a steep slant, blaze as though the lamp were pointing straight at them.

She shows it to the mentor running her club's Saturday sessions, expecting a long answer.

"You've forgotten the dot product," he says. "Take the surface's normal, take the direction to the light, and multiply by the cosine of the angle between them. A wall edge-on to a lamp should catch almost nothing."

Aarohi adds one line of code and the corridor snaps into place. Then she sits looking at that line, because now she wants the reason. Why should the tilt of a surface change how much of something crosses it — and which angle is the right one to measure, the one to the surface or the one to the line sticking out of it?

## The physics

The quantity that measures "how much field passes through a surface" is the **electric flux**.

For a flat surface of area $\Delta S$ in a **uniform** field $\vec{E}$, define an **area vector** $\Delta\vec{S}$: its magnitude is the area, and its direction is along the **normal** — the line sticking straight out of the surface. Then

$$\Delta\Phi = \vec{E} \cdot \Delta\vec{S} = E\,\Delta S\cos\theta$$

where **$\theta$ is the angle between $\vec{E}$ and the normal**, not the angle between $\vec{E}$ and the surface. That is Aarohi's dot product, written in the language of fields. Flux is a scalar, and its unit is the $\text{N m}^2/\text{C}$.

![A flat surface in a uniform field shown three times: facing the field with all six lines through it, tilted with its normal at 60 degrees and only three lines through it, and edge-on with none](figures/electric_flux/flux-tilted-area.svg "Largest face-on, half as big at 60 degrees from the normal, zero edge-on. The angle is always measured from the normal.")

- $\theta = 0^\circ$: the surface faces the field head-on, $\Phi = EA$ — the maximum.
- $\theta = 60^\circ$: $\Phi = EA\cos 60^\circ = EA/2$.
- $\theta = 90^\circ$: the field slides along the surface and $\Phi = 0$.
- $\theta > 90^\circ$: $\cos\theta$ is negative, so the flux is negative — the field crosses against the chosen normal.

**Flux as a count of lines.** Field lines are drawn so that their density across the field is proportional to $E$. So $E\,\Delta S\cos\theta$ is proportional to the **number of lines crossing the surface**. The tilted surface in the figure catches half the lines because its shadow across the field, $\Delta S\cos\theta$, is half its area — and a wall lit edge-on catches almost nothing for exactly the same geometric reason.

**Sign convention.** For an open surface you choose which way the normal points. For a **closed** surface the normal always points **outwards**, so lines leaving count as positive flux and lines entering as negative.

If the field varies or the surface curves, chop the surface into small patches, work out $\vec{E} \cdot \Delta\vec{S}$ for each, and add them: $\Phi = \sum \vec{E} \cdot \Delta\vec{S}$.

## Worked example

**Given (illustrative):** a flat panel of area $A = 2.0\,\text{m}^2$ in a uniform field $E = 300\,\text{N/C}$, with its normal at $\theta = 60^\circ$ to the field.
**Find:** the flux through it, and what the flux becomes face-on and edge-on.

**Step 1 — the tilted panel.** With $\cos 60^\circ = 0.50$:

$$\Phi = EA\cos\theta = 300 \times 2.0 \times 0.50 = 300\,\text{N m}^2/\text{C}$$

**Step 2 — turn it to face the field.** Now $\theta = 0^\circ$ and the cosine is 1:

$$\Phi = 300 \times 2.0 = 600\,\text{N m}^2/\text{C}$$

Turning the panel has doubled the flux without changing the field or the panel by anything at all.

**Step 3 — turn it edge-on.** At $\theta = 90^\circ$, $\cos\theta = 0$, so $\Phi = 0$: the field slides past and nothing crosses.

**Sanity check:** the tilted value is exactly half the face-on value, which is what $\cos 60^\circ = 0.5$ promised, and the units work out as $(\text{N/C}) \times \text{m}^2 = \text{N m}^2/\text{C}$.

## Where the picture breaks

The shader analogy is a geometric match, not a physical one. Light really does flow: energy leaves the lamp, crosses the wall and is absorbed. An electric field flows nowhere at all, and nothing travels along a field line — "flux" here only borrows a word from fluids.

There is a second difference that matters in this chapter. A renderer clamps the dot product at zero, because a surface facing away from a lamp is simply unlit. Electric flux is allowed to be **negative**, and for a closed surface that sign is the whole point: it is what lets flux in and flux out cancel.

## Key takeaway

Electric flux through a flat surface in a uniform field is $\Phi = \vec{E} \cdot \Delta\vec{S} = EA\cos\theta$, with $\theta$ measured from the **normal** to the surface. It counts the field lines crossing the surface: greatest face-on, zero edge-on, negative when the field crosses against the normal. For a closed surface the normal always points outwards.
