---
concept_id: equipotential_surfaces
interest: smartphones
format: explain
title: The multimeter that read zero all around a phone's frame
check:
  question: |-
    In a region of space the equipotential surfaces are flat, parallel planes at $10\,\text{V}$, $20\,\text{V}$ and $30\,\text{V}$, each $5.0\,\text{mm}$ from the next. What is the electric field there?
  options:
    A: |-
      $2000\,\text{V/m}$, perpendicular to the planes, pointing from the $30\,\text{V}$ plane towards the $10\,\text{V}$ plane.
    B: |-
      $2000\,\text{V/m}$, perpendicular to the planes, pointing from the $10\,\text{V}$ plane towards the $30\,\text{V}$ plane.
    C: |-
      $2000\,\text{V/m}$, parallel to the planes.
    D: |-
      $2\,\text{V/m}$, perpendicular to the planes, pointing from the $30\,\text{V}$ plane towards the $10\,\text{V}$ plane.
  answer: A
  explanation: |-
    The field is perpendicular to equipotentials and points the way potential falls. Its size is $\Delta V/d = 10\,\text{V} / 5.0\times10^{-3}\,\text{m} = 2000\,\text{V/m}$.
  misconceptions:
    B: |-
      Thinks the field points towards higher potential. It points the way potential decreases, the direction a positive charge would be pushed.
    C: |-
      Thinks field lines run along the equipotentials. If the field had any component along a surface, moving a charge along it would take work and the surface could not be at one potential.
    D: |-
      Divides by $5.0$ instead of $5.0\times10^{-3}$, forgetting to convert millimetres to metres.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a rainy window: a phone with raindrops on its screen being tapped by a finger, a metal biscuit tin with its lid off, a breadboard with two supercapacitor cells wired in a chain, a stylus and a fitness band with a small display](scenes/smartphones/potential_capacitance.svg "Every metal part on this desk — the tin, the phone's frame, the tracks on the breadboard — has one thing in common that this lesson is about.")

Kabir has taken his phone, dead after a fall, to a repair stall in a busy electronics market. The technician, Mrs Fernandes, opens the back, flips on her multimeter and starts poking.

First she touches both probes to the metal frame — one at the top corner, one at the bottom. The screen reads **0.00 V**. She moves them: side and top, corner and corner. **0.00 V** every time.

Then one probe on the frame, the other on a tiny gold pin by the battery. **3.8 V**.

"Battery's fine," she says. "Frame's fine. Something else."

Kabir is puzzled. The frame is a big piece of metal wrapped all the way round the phone, and the battery is sitting right inside it. Surely some parts of the frame are "closer to the battery" than others? Why does every pair of points on it read exactly the same — and what would a map of these voltages look like?

## The physics

An **equipotential surface** is a surface on which every point has the same potential. Moving a charge anywhere along it takes **no work**, because $W = q\,\Delta V$ and $\Delta V = 0$.

That fact fixes how equipotentials meet field lines. If the field had any component along the surface, a charge moved that way would be pushed and work would be done — impossible on an equipotential. So:

> **The electric field is always perpendicular to equipotential surfaces**, and it points from higher to lower potential.

Where equipotentials drawn at equal steps of $V$ are close together, the potential changes quickly with distance, so the field is strong: $E = \Delta V/\Delta r$, measured along the field.

The shapes you should be able to sketch:

- **Point charge:** concentric spheres, crowded near the charge; field lines radial.
- **Uniform field:** parallel planes, equally spaced, perpendicular to the field.
- **Dipole:** closed, egg-shaped surfaces round each charge, with the flat plane halfway between them at $V = 0$.

![Three panels: concentric circles around a point charge with radial field lines; parallel planes at 50, 40, 30, 20, 10 V in a uniform field; distorted circles and a zero-potential midline for a dipole](figures/equipotential_surfaces/equipotentials-three-cases.svg "In every case the field lines (purple) cross the equipotentials (orange) at right angles. The dipole's midline is the V = 0 surface.")

Mrs Fernandes's reading is the same idea. In electrostatics the surface of a conductor is an equipotential (the next lesson but one shows why), so every point on the frame sits at one potential, and the meter reads zero between any two of them.

## Worked example

Inside a circuit board, two flat copper layers run parallel, one at $0\,\text{V}$ and one at $6\,\text{V}$, $3.0\,\text{mm}$ apart (illustrative values). Treat the field between them as uniform.

**Step 1 — the field.**

$$E = \frac{\Delta V}{d} = \frac{6\,\text{V}}{3.0\times10^{-3}\,\text{m}} = 2000\,\text{V/m}$$

It points straight from the $6\,\text{V}$ layer to the $0\,\text{V}$ layer.

**Step 2 — where the $1\,\text{V}$ steps lie.** The equipotentials are planes parallel to the layers. Six equal steps in $3.0\,\text{mm}$ means one every $0.5\,\text{mm}$ — like six evenly spaced sheets of paper in a stack.

**Step 3 — work on a $1\,\mu\text{C}$ charge.** Sliding it $1\,\text{cm}$ along the $2\,\text{V}$ plane: $\Delta V = 0$, so $W = 0$. Carrying it from the $2\,\text{V}$ plane to the $5\,\text{V}$ plane: $W = q\,\Delta V = 1\times10^{-6} \times 3 = 3\times10^{-6}\,\text{J}$, whatever path it takes.

**Sanity check:** only the change in potential matters, so the sideways centimetre adds nothing — just as walking along a contour line on a hill map never takes you uphill.

## Where the picture breaks

A working phone is not electrostatic: currents flow in its circuits, so tiny voltage drops do exist along a frame carrying current — they are just far too small for a repair meter to show. The frame reads zero mainly because it is a good conductor tied to the circuit's common "ground". The clean planes in the example also assume layers much wider than their gap; near the edges the equipotentials bend, and there the field is no longer uniform.

## Key takeaway

An equipotential surface is one where $V$ is the same everywhere, so moving a charge along it takes no work. The field is always perpendicular to equipotentials and points towards lower potential; closer spacing means a stronger field. Point charges give spheres, a uniform field gives parallel planes, and the surface of a conductor in electrostatics is always an equipotential.
