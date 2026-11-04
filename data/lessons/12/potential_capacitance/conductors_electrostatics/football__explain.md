---
concept_id: conductors_electrostatics
interest: football
format: explain
title: The hollow goalpost with nothing going on inside it
check:
  question: |-
    A spare goal frame is a hollow aluminium tube. It is given a charge and left until everything has settled. Where does that charge sit, and what is the field inside the metal of the tube?
  options:
    A: |-
      Spread evenly through the metal, with a field inside the metal pointing outwards.
    B: |-
      All on the outer surface, with no field anywhere inside the metal.
    C: |-
      All on the inner surface, because the charges repel and push each other inwards.
    D: |-
      All on the outer surface, but with a field inside the metal pointing inwards from that surface.
  answer: B
  explanation: |-
    In electrostatic equilibrium the free electrons have stopped moving, which requires $E = 0$ everywhere inside the metal. Gauss's law then forces every bit of net charge onto the outer surface.
  misconceptions:
    A: |-
      Pictures charge soaking through the metal like water into a sponge. Free electrons keep moving until the field inside is zero, and that pushes all the net charge to the surface.
    C: |-
      Has the repulsion backwards. Mutual repulsion drives the charges as far apart as they can get, which is the outer surface, not the inner one.
    D: |-
      Puts the charge in the right place but forgets what put it there. Any field left inside the metal would still be pushing free electrons around, so it would not yet be equilibrium.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground at dusk with a floodlight pylon, an electric fence and its energiser box along the far side, a coach holding a touchscreen tablet, a water bowser and an AED cabinet](scenes/football/potential_capacitance.svg "Goal frames, floodlight masts, the bowser's tank — most of what stands around a pitch is hollow metal.")

Behind the changing rooms, the club stores four portable goal frames for the seven-a-side pitch. They are aluminium tubes, hollow, wide enough to put your fist into, with the end caps missing on two of them.

Mr Fernandes teaches physics on weekdays and referees on Sundays, and he has brought his foil-leaf detector down to the store. He charges one frame from a small hand-cranked generator until the detector, held near the crossbar, flies wide open.

Then he passes the detector to Harshita and asks her to slide it into the open end of the tube.

She is sure she knows what will happen. The charge went *in* through that tube; the inside is where it must be most crowded. She pushes the detector in, waits, and pulls it out.

The leaves have not moved at all. Not a flicker.

Outside the tube, plenty. Inside the same piece of charged metal, nothing. Where has all of it gone?

## The physics

A **conductor** such as aluminium is full of free electrons that shift the instant a field acts on them. In **electrostatic equilibrium** — once everything has stopped moving — that freedom forces five results.

**1. The field inside the conductor's material is zero.** If any field remained, free electrons would still be moving. They keep moving, piling up on one side and leaving the other positive, until the field of these **induced charges** cancels everything inside. This takes a tiny fraction of a second.

**2. Any net charge sits on the outer surface.** Draw a Gaussian surface just inside the metal. Since $E = 0$ everywhere on it, Gauss's law says it encloses no charge. So the charge has nowhere to be but the surface. This is Harshita's answer.

**3. Just outside, the field is perpendicular to the surface**, with magnitude

$$E = \frac{\sigma}{\varepsilon_0}$$

where $\sigma$ is the local surface charge density. A field component *along* the surface would slide the surface charges sideways, and then it would not be equilibrium.

**4. The whole conductor is one equipotential.** With $E = 0$ inside and no component along the surface, moving a charge anywhere on or in the conductor takes no work, so $V$ is the same throughout.

**5. An empty cavity inside a conductor has zero field**, whatever is going on outside. This is **electrostatic shielding**, and it is why the detector sat dead inside the tube even while the tube itself was crackling with charge.

![A metal sphere with a hollow cavity sitting in a field that points to the right: the field lines bend to meet the surface at right angles, negative charge gathers on the left, positive on the right, and E is zero in the metal and in the cavity](figures/conductors_electrostatics/conductor-in-field.svg "The induced charges arrange themselves so their field cancels the outside field everywhere inside the metal — and inside the hollow too.")

## Worked example

Take a hollow metal sphere of radius $R = 0.30\,\text{m}$ — about the size of a gym ball — carrying $Q = +30\,\text{nC}$ (illustrative values). **Find** its potential, the field just outside, and the field at its centre.

All the charge sits on the outer surface, and by symmetry it spreads evenly there. Outside, a uniformly charged sphere behaves exactly like a point charge at its centre, so at the surface

$$V = \frac{kQ}{R} = \frac{9.0 \times 10^{9} \times 30 \times 10^{-9}}{0.30} = \frac{270}{0.30} = 900\,\text{V}$$

The field just outside follows from the same point-charge picture:

$$E = \frac{kQ}{R^2} = \frac{270}{0.090} = 3.0 \times 10^{3}\,\text{V/m}$$

pointing straight out, at right angles to the surface.

Inside — in the metal, in the hollow, and so at the centre — $E = 0$. And since no work is needed to walk a charge in from the surface, the centre is at the same $900\,\text{V}$ as the shell.

**Sanity check:** for a uniform field over the radius you would expect $E = V/R = 900/0.30 = 3000\,\text{V/m}$, which is what came out — a good sign, since $V = kQ/R$ and $E = kQ/R^2$ differ by exactly one factor of $R$.

## Where the picture breaks

The tube is a real conductor, but the tidy results above are for a body in **equilibrium**, with its charge at rest. Three limits worth naming. Aluminium goal frames standing on damp ground are earthed, so in practice the charge drains away in moments; the demo needs the frames dry and on something insulating. The field is not the same all over a real frame either — $\sigma$ builds up at corners and sharp ends, so the field just outside is strongest there, not on the flat middle of a tube. And shielding is proved here for *static* fields. Quickly changing fields, such as the radio waves reaching a phone, can leak through gaps and openings, which is why a phone still works inside a metal frame that would block a static field completely.

## Key takeaway

In electrostatic equilibrium the field inside a conductor's material is zero and all its net charge sits on the outer surface. Just outside, the field is perpendicular to the surface with $E = \sigma/\varepsilon_0$. The whole conductor is a single equipotential, and an empty cavity inside it is shielded from outside fields.
