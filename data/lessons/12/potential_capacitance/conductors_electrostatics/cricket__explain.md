---
concept_id: conductors_electrostatics
interest: cricket
format: explain
title: Why a metal car is a good place to wait out the lightning
check:
  question: |-
    A charge $Q$ is placed on a hollow metal sphere of radius $R$ and comes to rest. What is the electric field at the centre of the sphere?
  options:
    A: |-
      $kQ/R^2$, since all the charge is a distance $R$ from the centre
    B: |-
      Zero
    C: |-
      The largest anywhere, because charge on every side pushes inwards
    D: |-
      Zero only if the sphere is solid; a hollow sphere has a field inside
  answer: B
  explanation: |-
    In electrostatic equilibrium the charge sits on the outer surface, and the field inside the metal and in any empty cavity is zero. The pushes from charge on all sides cancel exactly.
  misconceptions:
    A: |-
      Uses the formula for the field just outside the surface. The distance to the charge being $R$ doesn't mean the field is $kQ/R^2$; contributions from opposite sides cancel.
    C: |-
      Thinks the inward pushes from all sides add up. They point in opposite directions and cancel completely.
    D: |-
      Thinks the metal itself must fill the space to block the field. Shielding works for an empty cavity too; this is electrostatic shielding.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground under a storm cloud with lightning in the distance, a floodlight tower, a curator on the pitch, a car by the boundary and a photographer's flash](scenes/cricket/potential_capacitance.svg "The storm arrives. The open stands empty and people head for the car park.")

It is the second innings of a club T20 when the first flash splits the sky over the far stand. Three seconds later, thunder. The umpires take the players off. The announcer asks spectators to leave the open stands and move under cover.

Kabir's father grabs the bag. "To the car. It's the safest place to wait."

Kabir stops dead. "The car? Papa, it's a metal box. Metal *conducts*. If lightning hits it, it's the worst place to be. Shouldn't we stand under that big tree instead?"

His father hesitates. He only knows what everyone says. Around them, other families are also hurrying to their cars. A groundsman runs past and yells, "Not the tree!"

So who is right? How can a shell of metal, the very thing that carries electric charge best, end up protecting the people inside it?

## The physics

A **conductor** such as a metal contains free electrons that move whenever a field acts on them. In **electrostatic equilibrium**, when all charges have stopped moving, this freedom forces five results.

**1. The field inside the conductor's material is zero.** If there were a field inside, free electrons would move. They keep moving, piling up on one side and leaving the other side positive, until the field of these **induced charges** cancels the external field everywhere inside the metal. This happens almost instantly.

**2. Any net charge resides on the outer surface.** Take a Gaussian surface just inside the metal. $E = 0$ everywhere on it, so by Gauss's law the charge it encloses is zero. Any extra charge must sit on the surface.

**3. Just outside, the field is perpendicular to the surface**, with magnitude

$$E = \frac{\sigma}{\varepsilon_0}$$

where $\sigma$ is the local surface charge density. If the field had a component along the surface, surface charges would slide, and there would be no equilibrium.

**4. The whole conductor is an equipotential.** With $E = 0$ inside and no component of $E$ along the surface, no work is done moving a charge anywhere on or in the conductor.

**5. A cavity with no charge inside it has zero field**, whatever the fields and charges outside. This is **electrostatic shielding**.

![A metal sphere with a cavity in a field pointing right: field lines bend to meet the surface at right angles, minus charges on the left, plus charges on the right, and E = 0 in the metal and in the cavity](figures/conductors_electrostatics/conductor-in-field.svg "The induced charges arrange themselves so that their field cancels the outside field everywhere inside, including in the hollow.")

Map this to the car. The metal body is a conducting shell and the people are in its cavity. Fields and charges outside rearrange the charge on the *outside* of the shell. They don't reach in.

## Worked example

**Given:** a hollow metal sphere of radius $R = 0.10\,\text{m}$ carrying $Q = +4.0\,\text{nC}$ (illustrative values).
**Find:** the surface charge density, the field just outside, the field at the centre and the potential of the sphere.

The charge spreads evenly over the outer surface:

$$\sigma = \frac{Q}{4\pi R^2} = \frac{4.0 \times 10^{-9}}{4\pi \times (0.10)^2} = \frac{4.0 \times 10^{-9}}{0.1257} \approx 3.2 \times 10^{-8}\,\text{C/m}^2$$

$$E_\text{outside} = \frac{\sigma}{\varepsilon_0} = \frac{3.18 \times 10^{-8}}{8.85 \times 10^{-12}} \approx 3.6 \times 10^{3}\,\text{N/C}$$

Inside, both in the metal and in the hollow, and so also at the centre: $E = 0$.

The potential at the surface is $V = kQ/R = 9.0 \times 10^9 \times 4.0 \times 10^{-9}/0.10 = 360\,\text{V}$. Because $E = 0$ inside, the potential doesn't change as you go in. The centre is also at $360\,\text{V}$.

**Sanity check:** outside, the sphere acts like a point charge at its centre, so $E = kQ/R^2 = 36/0.010 = 3.6 \times 10^3\,\text{N/C}$. That matches $\sigma/\varepsilon_0$.

## Where the picture breaks

Lightning is **not** electrostatics. It is a huge current lasting a fraction of a second, so the protection a car gives is not exactly the shielding proved above. A metal car body gives the current a path *around* the occupants and on to the ground. That is also why you shouldn't touch metal parts inside during a storm. The protection needs a closed metal body. A soft-top or fibreglass car, or an open window, weakens it. The shielding proof also assumes static fields. Rapidly changing fields, such as radio waves, can still get in through the windows, which is why a phone works inside a car. And Kabir's tree? It is one of the most dangerous places to shelter, because lightning strikes tall objects and can jump from the trunk to someone standing beside it.

## Key takeaway

In electrostatic equilibrium the field inside a conductor is zero, and any net charge sits on its outer surface. Just outside, the field is perpendicular to the surface with $E = \sigma/\varepsilon_0$. The whole conductor is at one potential, and an empty cavity inside it is shielded from outside fields.
