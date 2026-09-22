---
concept_id: equipotential_surfaces
interest: cricket
format: explain
title: Why rainwater crosses the outfield's contour lines at right angles
check:
  question: |-
    A field map of a uniform field shows equipotential lines every $5.0\,\text{V}$, spaced $2.5\,\text{cm}$ apart. What is the electric field?
  options:
    A: |-
      $200\,\text{V/m}$, directed along the equipotential lines
    B: |-
      $2.0\,\text{V/m}$, perpendicular to the lines, towards lower potential
    C: |-
      $200\,\text{V/m}$, perpendicular to the lines, towards higher potential
    D: |-
      $200\,\text{V/m}$, perpendicular to the lines, towards lower potential
  answer: D
  explanation: |-
    $E = \Delta V/d = 5.0\,\text{V}/0.025\,\text{m} = 200\,\text{V/m}$. The field is always perpendicular to equipotentials and points the way the potential falls.
  misconceptions:
    A: |-
      Thinks the field runs along the equipotential lines. Moving along an equipotential takes no work, so the field can have no component along it.
    B: |-
      Uses the spacing in centimetres without converting to metres, so the answer is 100 times too small.
    C: |-
      Gets the direction backwards. The field points from high potential to low, just as water flows downhill.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground under a storm cloud with lightning in the distance, a floodlight tower, a curator on the pitch, a car by the boundary and a photographer's flash](scenes/cricket/potential_capacitance.svg "After the storm, the question is where the water goes and which way it runs.")

The storm has passed over the hill-station ground, and Harpreet, the head groundsman, is out on the outfield before anyone else. His daughter Simran, fifteen, follows him with the ground plan, a sheet covered in wavy contour lines. Each line joins points at the same height. This ground slopes gently from the pavilion down to the far boundary.

Rainwater is still trickling off the square in thin silver threads. Simran lays the plan flat on the grass and traces them. Every thread runs straight *across* the contour lines, never along one. Where the lines crowd together, the water runs fastest.

"Why does it always cross them square-on?" she asks. Harpreet shrugs. "Water goes downhill, beta."

That evening her physics homework asks her to "sketch equipotential surfaces and explain why they are always perpendicular to field lines." She looks from the textbook to the ground plan. It's the same picture. But why?

## The physics

An **equipotential surface** is a surface on which every point has the same potential $V$.

**No work along it.** Moving a charge $q$ between two points on the surface takes work $W = q(V_A - V_B) = q \times 0 = 0$.

**So the field is perpendicular to it.** For any small displacement $\Delta \vec{l}$ along the surface, the work done by the field is $q\vec{E}\cdot\Delta\vec{l} = qE\,\Delta l\cos\phi$. For this to be zero for **every** direction along the surface, $\cos\phi = 0$. The field must be at $90^\circ$ to the surface everywhere. It points from higher to lower potential, along the direction in which $V$ falls fastest.

**Spacing shows strength.** Draw surfaces at equal steps $\Delta V$. Where they are close together, the potential changes quickly with distance, so the field is strong: $E = \Delta V/\Delta d$ (for a uniform field, or locally over a small step).

**Two equipotentials never cross.** If they did, the crossing point would have two different potentials, which is impossible.

This is exactly the ground plan. Each contour line is a line of equal **gravitational** potential (equal height). Water feels a force down the steepest slope, which is perpendicular to the contours. Where the contours crowd together, the slope is steep and the force is large. Field lines are the "downhill" directions of electric potential.

![Three panels: concentric circles around a point charge with radial field lines; parallel planes at 50, 40, 30, 20, 10 V in a uniform field; distorted circles and a zero-potential midline for a dipole](figures/equipotential_surfaces/equipotentials-three-cases.svg "In every case the field lines (purple) cross the equipotentials (orange) at right angles. The dipole's midline is the V = 0 surface.")

The three standard shapes:

- **Point charge:** concentric spheres, since $V = kq/r$ depends only on $r$. For equal steps of $V$, the spheres get further apart as you move out, because the field weakens.
- **Uniform field:** parallel planes perpendicular to the field, equally spaced for equal steps of $V$.
- **Dipole:** closed surfaces around each charge, squeezed towards the other charge, and a flat plane of $V = 0$ midway between them.

## Worked example

**Given:** a uniform field whose equipotential planes are drawn every $10\,\text{V}$, $2.0\,\text{cm}$ apart, from $50\,\text{V}$ down to $10\,\text{V}$ (as in the middle panel). A charge $q = +3.0\,\mu\text{C}$.
**Find:** (a) the field; (b) the work the field does when $q$ moves $5.0\,\text{cm}$ along the $30\,\text{V}$ plane; (c) the work the field does when $q$ moves from the $30\,\text{V}$ plane to the $10\,\text{V}$ plane.

(a) $E = \dfrac{\Delta V}{\Delta d} = \dfrac{10\,\text{V}}{0.020\,\text{m}} = 500\,\text{V/m}$. It is perpendicular to the planes and points from the $50\,\text{V}$ side towards the $10\,\text{V}$ side.

(b) Along the plane $\Delta V = 0$, so $W = 0$, however far it goes.

(c) The field does work $W = q(V_\text{start} - V_\text{end}) = 3.0 \times 10^{-6} \times (30 - 10) = 6.0 \times 10^{-5}\,\text{J}$. It is positive, because a positive charge moving "downhill" in potential is pushed along by the field.

**Sanity check** on (c) using force times distance: the planes are $4.0\,\text{cm}$ apart, so $W = qEd = 3.0 \times 10^{-6} \times 500 \times 0.040 = 6.0 \times 10^{-5}\,\text{J}$. The two methods agree.

**Point-charge contrast:** for a $1.0\,\text{nC}$ charge, $V = 9.0/r$ volts. The $9\,\text{V}$, $6\,\text{V}$ and $3\,\text{V}$ surfaces sit at $r = 1.0$, $1.5$ and $3.0\,\text{m}$. The gaps are $0.5\,\text{m}$, then $1.5\,\text{m}$. Wider gaps mean a weaker field further out.

## Where the picture breaks

The ground plan is a genuine analogy: near the ground, gravitational potential energy per unit mass is $gh$, so a contour of equal height is a contour of equal gravitational potential, just as volts are electric potential energy per unit charge. But it has limits. Contour lines live on a two-dimensional ground, while equipotentials are surfaces filling three-dimensional space. Mass only attracts, so there is no "negative" water that would run uphill, whereas a negative charge is pushed *towards* higher potential. And real water has momentum and friction and follows channels in the grass. A moving stream can drift off the steepest line. A field line is defined to follow it exactly.

## Key takeaway

An equipotential surface joins points at the same potential. No work is done moving a charge along it, so the field must be perpendicular to it everywhere. The field points towards lower potential. Crowded equipotentials mean a strong field, since $E = \Delta V/\Delta d$.
