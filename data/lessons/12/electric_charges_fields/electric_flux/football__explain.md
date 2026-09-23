---
concept_id: electric_flux
interest: football
format: explain
title: The goal that shrinks when you move sideways
check:
  question: |-
    A flat rectangular banner of area $1.5\,\text{m}^2$ hangs behind the goal in a uniform electric field of $200\,\text{N/C}$. Its normal makes an angle of $60^\circ$ with the field. What is the electric flux through the banner?
  options:
    A: |-
      $300\,\text{N m}^2/\text{C}$
    B: |-
      $260\,\text{N m}^2/\text{C}$
    C: |-
      $150\,\text{N m}^2/\text{C}$
    D: |-
      $75\,\text{N m}^2/\text{C}$
  answer: C
  explanation: |-
    $\Phi = EA\cos\theta$ with $\theta$ measured from the normal, so $\Phi = 200 \times 1.5 \times \cos 60^\circ = 200 \times 1.5 \times 0.50 = 150\,\text{N m}^2/\text{C}$.
  misconceptions:
    A: |-
      Uses $\Phi = EA$ and drops the angle, as though a tilted surface caught the field head-on. Tilting always reduces the flux, except at $\theta = 0$.
    B: |-
      Uses $\sin 60^\circ$ instead of $\cos 60^\circ$ — the mistake you make if you measure the angle from the plane of the surface rather than from its normal.
    D: |-
      Gets $EA\cos\theta$ right and then halves it again, as if the flux were shared between the banner's two faces. A surface has one area vector, and the flux through it is counted once.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit ground as a storm arrives: lightning above the stand, rain falling, a player peeling off a crackling nylon bib, and two players heading for the metal-roofed dugout](scenes/football/electric_charges_fields.svg "Rain drives in at a slant tonight. How much of it a surface catches depends on which way that surface faces.")

Simran has spent an hour finishing from the penalty mark, and almost everything has gone in. Then the coach walks her out to the byline, two steps from the corner flag, and points at the same goal.

Her first shot flies wide. The second hits the side netting from the outside. The third rolls right across the face of goal without touching a thing.

"The goal got smaller," she says.

Joel, in gloves, holds up his phone from where she is standing. On the screen the two posts have almost slid into one another, and the mouth is a thin slot.

"It's still 7.32 metres wide," the coach says. "You just aren't facing it any more."

Simran walks back towards the penalty mark, and with every step sideways the goal opens up again. Same posts, same width, and yet the amount of it pointing at her keeps changing. Is there a rule for how much of a surface a direction really sees?

## The physics

The quantity that measures how much of a field passes through a surface is the **electric flux**.

For a flat surface of area $\Delta S$ sitting in a **uniform** field $\vec{E}$, give the surface an **area vector** $\Delta\vec{S}$: its size is the area, and it points along the **normal**, perpendicular to the surface. Then

$$\Delta\Phi = \vec{E} \cdot \Delta\vec{S} = E\,\Delta S\cos\theta$$

where **$\theta$ is the angle between $\vec{E}$ and the normal** — not the angle between $\vec{E}$ and the surface itself. Flux is a scalar, and its unit is the $\text{N m}^2/\text{C}$.

That is Simran's goal, exactly. The goal mouth is $\Delta\vec{S}$, with its normal pointing straight out along the pitch. Shooting from the penalty mark means $\theta \approx 0$ and the whole mouth faces you. Walking round to the byline pushes $\theta$ towards $90^\circ$, and what is left facing you is the **projection** $\Delta S\cos\theta$ — the shadow the goal casts across your line of sight.

![A flat surface seen edge-on in a uniform field: face-on, all six lines pass through; with its normal at 60 degrees, only three pass; edge-on, none pass](figures/electric_flux/flux-tilted-area.svg "Same surface, same field, three orientations. What counts is the surface's shadow across the field, and that shadow is A cos θ.")

- $\theta = 0^\circ$: the surface faces the field squarely, $\Phi = EA$, the largest it can be.
- $\theta = 60^\circ$: $\Phi = EA/2$.
- $\theta = 90^\circ$: the field slides along the surface and $\Phi = 0$.
- $\theta > 90^\circ$: $\cos\theta$ is negative, so the flux is negative — the field crosses against the normal you chose.

**Flux counts field lines.** Lines are drawn so that their density is proportional to $E$, so $E\,\Delta S\cos\theta$ is proportional to the **number of lines crossing the surface**. A tilted surface catches fewer lines for the same reason a byline shot has less goal to aim at.

**Choosing the normal.** For an open surface, you pick which side the normal points; for a **closed** surface it always points **outwards**, so lines leaving are positive flux and lines entering are negative. If the field varies or the surface curves, chop it into small flat patches and add: $\Phi = \sum \vec{E} \cdot \Delta\vec{S}$.

## Worked example

**Given (illustrative):** a flat rebound board of area $2.0\,\text{m}^2$ stands in a uniform field of $300\,\text{N/C}$, turned so that its normal is at $60^\circ$ to the field.
**Find:** the flux through it.

**Step 1 — how much of the board faces the field.**

$$A\cos\theta = 2.0 \times \cos 60^\circ = 2.0 \times 0.50 = 1.0\,\text{m}^2$$

Half the board's area is doing any work: its shadow across the field is a square one metre on a side.

**Step 2 — multiply by the field.**

$$\Phi = E \times (A\cos\theta) = 300 \times 1.0 = 300\,\text{N m}^2/\text{C}$$

**Step 3 — swing it square on.** With $\theta = 0$ the whole $2.0\,\text{m}^2$ faces the field, so $\Phi = 600\,\text{N m}^2/\text{C}$ — twice as much. Turn it edge-on and the flux drops to zero.

**Sanity check:** halfway between square-on and edge-on should let through about half, and it does.

## Where the picture breaks

The goal is a good picture of projection, but only from far out. Standing close to the posts, your two eyes see each post at a different angle, and the mouth you can actually hit is set by geometry that $A\cos\theta$ does not describe — $\cos\theta$ is exact for a *uniform* field, whose lines are parallel everywhere, not for lines fanning out from a point a few metres away. A shot is also a single object that either crosses the line or does not, while flux is a smooth, continuous measure. And nothing physically travels through the surface: an electric field does not flow, so "flux" here is a borrowed word, not a delivery of anything.

## Key takeaway

Electric flux through a flat surface in a uniform field is $\Phi = \vec{E} \cdot \Delta\vec{S} = EA\cos\theta$, with $\theta$ measured from the **normal**. It is proportional to the number of field lines crossing the surface: greatest face-on, zero edge-on, negative when the field crosses against the chosen normal. For a closed surface, that normal always points outwards.
