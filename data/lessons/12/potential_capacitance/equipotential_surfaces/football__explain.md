---
concept_id: equipotential_surfaces
interest: football
format: explain
title: Why the safety officer made everyone shuffle off the pitch
check:
  question: |-
    A map of the wet grass round a fallen live cable shows equipotential circles of $200\,\text{V}$, $100\,\text{V}$ and $50\,\text{V}$ at $1.0\,\text{m}$, $2.0\,\text{m}$ and $4.0\,\text{m}$ from the contact point. Where is the field along the ground strongest, and which way does it point?
  options:
    A: |-
      Strongest far out, where the circles are furthest apart, and pointing inwards towards the cable.
    B: |-
      Strongest close in, where the circles are crowded, and pointing outwards, crossing them at right angles.
    C: |-
      The same everywhere, because each circle differs from the next by the same step of potential.
    D: |-
      Strongest close in, but pointing along the circles, the way the potential stays constant.
  answer: B
  explanation: |-
    $E = \Delta V/\Delta d$, so crowded equipotentials mean a strong field: $100\,\text{V}$ across $1.0\,\text{m}$ near the cable, but only $50\,\text{V}$ across $2.0\,\text{m}$ further out. The field is always perpendicular to the equipotentials and points towards lower potential — here, outwards.
  misconceptions:
    A: |-
      Reads the spacing backwards, as if widely spaced equipotentials meant a strong field, and takes the field to point towards the source rather than towards lower potential.
    C: |-
      Looks only at the equal steps of potential and forgets the distance in $E = \Delta V/\Delta d$. Equal steps spread over larger gaps mean a weaker field.
    D: |-
      Thinks the field runs along the equipotentials. Moving along one takes no work, so the field can have no component in that direction.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground at dusk with a floodlight pylon, an electric fence and its energiser box along the far side, a coach holding a touchscreen tablet, a water bowser and an AED cabinet](scenes/football/potential_capacitance.svg "A floodlight pylon carries a heavy feed cable down its length. After a storm, that cable is the thing to worry about.")

The storm cuts the session short, and the squad is still on the pitch when something whips down from the pylon and lands on the grass by the corner flag, throwing sparks. One bank of floodlights dies. The feed cable is down, and the grass is soaked.

Karthik is thirty metres away and does the obvious thing — he turns to sprint for the tunnel.

"Stop." Jasleen, who is both the club's safety officer and an electrician, has both arms up. "Nobody runs. Feet together. Shuffle. Little steps, heels never past your toes."

Nobody moves for a second, because it makes no sense. The cable is over there. Running puts distance between you and it faster than shuffling does.

"The cable isn't what gets you," Jasleen says, watching the grass rather than the sparks. "The grass is."

Karthik looks down at his own two boots, planted a stride apart on ordinary wet turf, and cannot see what could possibly be different about them.

## The physics

An **equipotential surface** is a surface on which every point has the same potential $V$.

**No work along it.** Moving a charge $q$ between two points on the surface takes $W = q(V_A - V_B) = q \times 0 = 0$.

**So the field is perpendicular to it.** For a small step $\Delta \vec{l}$ along the surface, the work done by the field is $qE\,\Delta l \cos\phi$. If that is to vanish for *every* direction along the surface, then $\cos\phi = 0$: the field meets the surface at $90^\circ$ everywhere, pointing the way $V$ falls fastest.

**Spacing shows strength.** Draw surfaces in equal steps of $\Delta V$. Where they crowd together the potential changes quickly with distance, so the field is strong:

$$E = \frac{\Delta V}{\Delta d}$$

**Two equipotentials never cross**, because the crossing point would have to hold two different potentials at once.

![Three panels: concentric circles round a point charge with radial field lines; parallel planes at 50, 40, 30, 20 and 10 V in a uniform field; distorted closed curves and a zero-potential midline for a dipole](figures/equipotential_surfaces/equipotentials-three-cases.svg "In all three cases the field lines (purple) cross the equipotentials (orange) at right angles. Round a point charge the surfaces are spheres; in a uniform field, parallel planes.")

Now the grass. Charge is spilling from the cable's contact point out into the wet ground in every direction, so the potential of the ground is highest at that point and falls away from it — roughly as $1/r$, as it does round a point charge. The equipotentials are circles drawn round the contact point.

That is Jasleen's whole argument. Your two boots stand on two *different* circles, and what a current cares about is the potential difference between them. Feet together means both boots on almost the same circle. A stride means two circles far apart — and a running stride is the worst of all.

## Worked example

Take the potential of the ground as $200\,\text{V}$ at $1.0\,\text{m}$ from the contact point, falling as $1/r$ (illustrative values). So $V = (200\,\text{V m})/r$.

**Find** the potential difference between your feet if you (a) take a long stride, (b) shuffle, (c) stand still on one circle.

**(a)** A stride puts one boot at $1.0\,\text{m}$ and the other at $2.0\,\text{m}$:

$$\Delta V = 200 - \frac{200}{2.0} = 200 - 100 = 100\,\text{V}$$

A hundred volts, across your own two legs.

**(b)** A shuffle moves the front boot only about $10\,\text{cm}$, from $1.0\,\text{m}$ to $1.1\,\text{m}$:

$$\Delta V = 200 - \frac{200}{1.1} = 200 - 182 = 18\,\text{V}$$

Same place, same hazard, same distance from the cable — and about a fifth of the voltage across you.

**(c)** Both boots on the same circle are at the same potential, so $\Delta V = 0$. That is what an equipotential *means*.

**Sanity check:** nothing about the cable changed between (a) and (b); the only thing that changed is how many equipotential circles your stride spans. That is the whole point of drawing them.

## Where the picture breaks

Be honest about one thing: this is not electrostatics. Charge is *flowing* through the wet ground, so it is a current problem, and the potential pattern is set by the soil as well as by the cable. What carries across unchanged is the geometry — surfaces of equal potential, a field at right angles to them, and $E = \Delta V/\Delta d$ — which is why the picture is worth drawing either way. Two more limits: real ground is patchy, so the circles are only tidy in a textbook, and a $1/r$ fall assumes a small contact point on uniform ground. And the numbers here are illustrative. The real rule is the simple one: shuffle, and stay far away.

## Key takeaway

An equipotential surface joins points at the same potential. No work is done moving a charge along it, so the field must cross it at right angles, pointing towards lower potential. Crowded equipotentials mean a strong field, since $E = \Delta V/\Delta d$; widely spaced ones mean a weak field. Two equipotentials can never cross.
