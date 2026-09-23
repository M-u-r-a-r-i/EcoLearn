---
concept_id: electric_field_lines
interest: football
format: explain
title: Why field lines are not like the arrows on a tactics board
check:
  question: |-
    In a field-line diagram, two lines are drawn crossing at a point P. What does that tell you?
  options:
    A: |-
      The field at P is twice as strong as it is where a single line passes.
    B: |-
      The diagram is wrong: the field at a point has only one direction.
    C: |-
      The field at P is zero, because the two lines cancel there.
    D: |-
      A charge released at P would travel along both lines at once.
  answer: B
  explanation: |-
    The tangent to a field line gives the direction of $\vec{E}$ at that point. Two lines crossing would give the field two different directions at the same point, which is impossible — so field lines never cross.
  misconceptions:
    A: |-
      Reads a crossing as lines "adding". Field strength is shown by how *closely packed* the lines are, not by lines meeting; the fields of several charges are added before the lines are drawn, never after.
    C: |-
      Confuses a crossing with a neutral point. Where the net field is zero, no line passes at all — lines stop dead or curve away, they do not intersect.
    D: |-
      Treats field lines as paths that a charge follows. A line shows the direction of the *force* at each point; a released charge picks up velocity and generally curves away from the line it started on.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit ground as a storm arrives: lightning above the stand, rain falling, a player peeling off a crackling nylon bib, and two players heading for the metal-roofed dugout](scenes/football/electric_charges_fields.svg "Every charge in this picture — cloud, bib, ball — has a field around it. Could you draw it?")

Dhruv's coach fills the tactics board before every match: a dozen arrows curling out of the midfield, two of them crossing at the edge of the box, one doubling back on itself. Dhruv can read it in a second — a crossing just means two players run through the same patch of grass at different times.

On Monday his physics teacher draws something that looks almost identical: curved arrows, spreading out, labelled with plus and minus signs. Dhruv copies the style he knows. He sketches two charges, runs a line out of each, and has them cross neatly in the gap between.

The teacher stops at his desk and circles the crossing.

"On your coach's board, that's fine," she says. "Here it's the one thing that can never happen. Why not?"

Dhruv looks at the two lines meeting at a single point, and at the charge he has drawn sitting there. If a line tells you which way that charge gets pushed, then at that point it is being told two different things.

## The physics

A **field line** is a curve drawn so that the **tangent at every point gives the direction of $\vec{E}$ there**. Faraday introduced them to make an invisible field visible, and they obey strict rules.

1. **Direction:** lines start on positive charges and end on negative charges (or run off to infinity). The arrow shows the direction of the force on a positive charge.
2. **Strength is shown by crowding:** the closer the lines are packed, the stronger the field. Where they spread out, the field is weak.
3. **Lines never cross.** A crossing would give $\vec{E}$ two directions at one point, and the field has exactly one.
4. **Continuous, never closed:** in the space between charges an electrostatic field line has no breaks and no loops — it cannot return to where it started.
5. **They are not trajectories.** A released charge follows a line only if it starts at rest and the line is straight; otherwise its inertia carries it across the lines.

![Field lines for a single positive charge (radial, outwards), a dipole (lines leave the positive charge and curve round to the negative one) and two equal positive charges (lines push apart, with a neutral point midway)](figures/electric_field_lines/field-line-patterns.svg "Three patterns to know. In (c) the two sets of lines never meet; midway between the charges the field is zero.")

Rule 2 is worth more than it looks. Take a point charge and imagine a fixed number of lines leaving it. They spread over a sphere of area $4\pi r^2$, so the number crossing each square metre falls as $1/r^2$ — the same inverse-square law Coulomb measured. The picture and the formula agree because the lines have nowhere else to go.

## Worked example

**Given:** two equal charges of $+4.0\,\text{nC}$, held $0.40\,\text{m}$ apart (pattern (c) in the figure).
**Find:** the field exactly midway between them.

**Step 1 — the distance from each charge.** The midpoint is $0.20\,\text{m}$ from both.

**Step 2 — the field from one charge there.**

$$E_1 = \frac{9.0 \times 10^9 \times 4.0 \times 10^{-9}}{(0.20)^2} = \frac{36}{0.040} = 900\,\text{N/C}$$

pointing away from that charge — that is, towards the other one.

**Step 3 — add the second.** The other charge is equal and equally far, so its field is also $900\,\text{N/C}$, pointing the opposite way. The two cancel exactly:

$$E_\text{net} = 900 - 900 = 0$$

This is the **neutral point**, and it is why no field line passes through the middle of pattern (c). The lines do not cross there; they stay away.

**Sanity check:** the cancellation is exact only because the charges are equal. Nudge one charge up and the neutral point simply shifts towards the weaker charge — it never disappears.

## Where the picture breaks

A tactics board is the wrong instinct in three ways. Its arrows are paths, showing where a player goes; field lines only show a direction at each point. Its arrows can cross, because two players occupy the same grass at different times; a field has one value at each point at each instant. And its arrows are countable — eleven players, eleven runs — while the number of field lines you draw is entirely your choice. Only the *relative* spacing carries meaning, which is why you must never read "twice as many lines" as "twice the field" unless you drew them consistently in the first place.

## Key takeaway

A field line's tangent gives the direction of $\vec{E}$, and how tightly the lines are packed gives its strength. Lines run from positive to negative charge, never form loops, and **never cross** — because the field has exactly one direction at every point. They are a map of a field, not a set of paths for a charge to follow.
