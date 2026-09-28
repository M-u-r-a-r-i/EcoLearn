---
concept_id: electric_field_lines
interest: smartphones
format: explain
title: The simulator that wouldn't let two lines cross
check:
  question: |-
    In a field-line app, Ishita drags charges around, trying to make two field lines cross at some point P. However she arranges the charges, it never happens. Why can field lines never cross?
  options:
    A: |-
      Field lines repel each other, like charges of the same sign
    B: |-
      At a crossing the field would point in two directions at once, but the field has only one direction at each point
    C: |-
      Field lines are the paths charges travel along, and two charges cannot be at the same place
    D: |-
      They can cross in very strong fields; the app simply leaves those cases out
  answer: B
  explanation: |-
    The tangent to a field line at a point gives the direction of $\vec{E}$ there. At a crossing there would be two tangents, meaning two field directions at one point. But the net field at any point is a single vector, so lines can never cross.
  misconceptions:
    A: |-
      Treats field lines as physical objects that push on each other. They are only a drawing of the field's direction and strength.
    C: |-
      Thinks field lines are the paths charges follow. A released charge starts along the line, but once moving it generally leaves it, so lines are not trajectories.
    D: |-
      Thinks the no-crossing rule is an approximation. It follows directly from the field having one value at each point, so it holds everywhere, however strong the field.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a sunny window with a solar power bank on the sill, an opened phone box with foam beads clinging to the new phone, a film being peeled off a screen with dust jumping up to it, and a phone on a stand running a field-line app](scenes/smartphones/electric_charges_fields.svg "On the phone on the stand, lines leave the + charge and curve round to the − charge. Notice that none of them cross.")

Ishita wants a new lock-screen wallpaper, and her little brother Yash has found the perfect source: a free app that draws electric field lines. You drop charges on the screen and it fills with swirling blue curves.

They put down a positive and a negative charge. Lines spring out of the positive one and arch round into the negative one, like a flower. Beautiful. Yash wants something messier. "Make two lines cross. An X would look cool."

Ishita drags the charges closer. The lines bunch up but slide past each other. She adds a third charge, then a fourth. The pattern gets wild, bending and squeezing, but in twenty minutes of trying, not one pair of lines ever crosses. Not once.

"Bug in the app," Yash decides.

Ishita isn't so sure. The app seems to be obeying a rule. What is it, and what other rules are these lines following?

## The physics

**Electric field lines** are curves drawn so that the **tangent** at each point gives the direction of $\vec{E}$ there. They are a map of the field, invented by Michael Faraday; they are not physical objects. They obey these rules:

1. **Start and end.** Lines start on positive charges and end on negative charges. If the charges are not balanced, the extra lines start or end at infinity (very far away).
2. **Number.** The number of lines leaving or entering a charge is drawn **proportional to the size of the charge**.
3. **Density shows strength.** Where lines are crowded, the field is strong; where they spread out, it is weak.
4. **They never cross.** At a crossing there would be two tangents, meaning two directions of $\vec{E}$ at one point, which is impossible because the net field has one direction at each point.
5. **No closed loops** in electrostatics: a line never comes back round to where it started.
6. **Continuous curves** in any region without charge, with no breaks.

![Field lines for a single positive charge (radial, outwards), a dipole (lines leave the positive charge and curve round to the negative one) and two equal positive charges (lines push apart, with a neutral point midway)](figures/electric_field_lines/field-line-patterns.svg "Three patterns to know. In (c) the two sets of lines never meet; midway between the charges the field is zero.")

The spreading of the lines of a single charge also shows the inverse-square law. The lines leaving a point charge cross a sphere of area $4\pi r^2$, so the number per unit area, and hence the field, falls as $1/r^2$.

## Worked example

**Given:** Ishita places $+2Q$ and $-Q$ some distance apart. The app draws **16** lines leaving the $+2Q$ charge.
**Find:** how many lines end on $-Q$, and where the rest go.

**Step 1 — lines per unit charge.** 16 lines for a charge of $2Q$ means 8 lines for every $Q$.

**Step 2 — lines ending on $-Q$.** A charge of size $Q$ gets 8 lines, so 8 of the 16 end on the negative charge.

**Step 3 — the rest.** The other $16 - 8 = 8$ lines have no negative charge to end on, so they curve away and head off to infinity. Far away, the pair looks like a single charge of $+2Q - Q = +Q$, with 8 lines going radially out, which is exactly what those left-over lines do.

**Sanity check:** a single charge of $+Q$ on its own would also send out 8 lines, so the far-away pattern and the count agree.

## Where the picture breaks

The app draws a fixed handful of lines, but the real field exists at every point, including the gaps between the drawn lines. Twenty minutes of dragging charges about is also not a proof; the proof is the argument in rule 4, which holds for any arrangement. And the lines are not paths: a charge released at rest starts off along a line, but once it is moving, its own inertia usually carries it off the line.

## Key takeaway

Field lines map the field: their tangent gives the direction of $\vec{E}$ and their crowding gives its strength. They start on positive charges and end on negative ones (or at infinity), in numbers proportional to the charge, form no closed loops, and never cross, because the field has one direction at every point.
