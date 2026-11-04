---
concept_id: superposition_of_forces
interest: football
format: explain
title: Pulled two ways at the cone
check:
  question: |-
    A small charge sitting at a cone feels a force of $0.80\,\text{N}$ due east from one nearby charge and $0.60\,\text{N}$ due north from another. Rehan says the total is $1.40\,\text{N}$. What is the net force actually?
  options:
    A: |-
      $1.40\,\text{N}$ — the two forces simply add.
    B: |-
      $0.20\,\text{N}$ — the difference between the two forces.
    C: |-
      $0.70\,\text{N}$ — the average of the two forces.
    D: |-
      $1.0\,\text{N}$, pointing $37^\circ$ north of east.
  answer: D
  explanation: |-
    The forces are perpendicular, so they add as vectors: $\sqrt{0.80^2 + 0.60^2} = 1.0\,\text{N}$, at $\tan^{-1}(0.60/0.80) = 37^\circ$ from the eastward force.
  misconceptions:
    A: |-
      Adds the sizes as plain numbers. That is only right when both forces point the same way; at right angles the total is always less than the sum.
    B: |-
      Subtracts them, as if two forces in different directions must partly cancel. Cancellation happens only for forces with opposite components, not perpendicular ones.
    C: |-
      Averages the two forces. Averaging is never how forces combine — two pushes always give more than either alone, unless they oppose each other.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit ground as a storm arrives: lightning above the stand, rain falling, a player peeling off a crackling nylon bib, and two players heading for the metal-roofed dugout](scenes/football/electric_charges_fields.svg "A rain-off means cones on the clubhouse floor and physics instead of a session.")

Rehan lays out the passing drill he knows best: one cone at the corner, one cone $30$ steps along the touchline, one cone $40$ steps up the pitch, a clean right angle. Then the rain wins and the session moves indoors, and Mr Bakshi redraws the same triangle on the whiteboard with charges on the cones instead of players.

"Same shape," he says. "Charge at the corner. One charge over here pushes it with $0.60$ newtons. One charge up there pulls it with $0.45$ newtons. What does the charge at the corner actually do?"

"One-point-nought-five newtons," says Rehan at once. "Point six plus point four five."

Mr Bakshi draws two arrows at the corner — one pointing along the touchline, one pointing up the pitch — and leaves them there without answering.

Rehan looks at his own diagram. The two arrows are not pointing the same way. So what does adding them even mean?

## The physics

The **superposition principle** for electrostatic forces says this: the force between any two charges is completely unaffected by the presence of others. To find the total force on a charge, work out the Coulomb force from **each** other charge separately, as if it were the only one there, then add those forces **as vectors**.

$$\vec{F}_\text{net} = \vec{F}_1 + \vec{F}_2 + \vec{F}_3 + \dots$$

Two things follow, and both matter:

- **Each pair is independent.** A third charge in between does not "shield" or weaken the force between the first two. Nothing gets used up.
- **Vectors, not numbers.** Forces in different directions are combined head to tail, or by splitting each into $x$ and $y$ components and adding those separately. Only when the forces lie along the same line do the sizes simply add (same direction) or subtract (opposite).

For two perpendicular forces, the vector sum is the diagonal of the rectangle they make:

$$F_\text{net} = \sqrt{F_1^2 + F_2^2}, \qquad \tan\theta = \frac{F_2}{F_1}$$

For a **continuous** charge distribution — a charged rod, a charged sheet — the same principle applies: split it into pieces so small that each counts as a point charge $dq$, find each piece's contribution, and add. The adding becomes an integral, but the idea does not change.

## Worked example

**Given:** $q_0 = +2.0\,\mu\text{C}$ at the corner cone $O$; $q_1 = +3.0\,\mu\text{C}$ a distance $0.30\,\text{m}$ to its right; $q_2 = -4.0\,\mu\text{C}$ a distance $0.40\,\text{m}$ directly above it. Take $k = 9.0 \times 10^9\,\text{N m}^2\,\text{C}^{-2}$.
**Find:** the net force on $q_0$.

**Step 1 — the force from $q_1$ alone.** Both charges are positive, so $q_1$ pushes $q_0$ away, i.e. to the **left**:

$$F_1 = \frac{9.0 \times 10^9 \times (2.0 \times 10^{-6})(3.0 \times 10^{-6})}{(0.30)^2} = \frac{0.054}{0.090} = 0.60\,\text{N}$$

**Step 2 — the force from $q_2$ alone.** Unlike charges, so $q_2$ pulls $q_0$ **upwards**:

$$F_2 = \frac{9.0 \times 10^9 \times (2.0 \times 10^{-6})(4.0 \times 10^{-6})}{(0.40)^2} = \frac{0.072}{0.16} = 0.45\,\text{N}$$

These two are at right angles — left and up — so neither cancels any part of the other.

**Step 3 — add them as vectors.**

$$F_\text{net} = \sqrt{(0.60)^2 + (0.45)^2} = \sqrt{0.5625} = 0.75\,\text{N}, \qquad \tan\theta = \frac{0.45}{0.60} = 0.75 \Rightarrow \theta = 37^\circ$$

so $0.75\,\text{N}$, pointing up and to the left, $37^\circ$ above the leftward direction.

![The corner charge feels 0.60 N to the left from the right-hand charge and 0.45 N upwards from the upper charge; the net force is 0.75 N up and to the left at 37 degrees](figures/superposition_of_forces/right-angle-superposition.svg "Each force is worked out on its own, then added head-to-tail. The net force points in neither of the original directions.")

**Sanity check:** $0.75\,\text{N}$ is less than Rehan's $1.05\,\text{N}$ but more than either force alone — exactly what a diagonal of a rectangle must be.

## Where the picture breaks

Cones and players are a way of fixing the geometry in your head, nothing more: a player at the corner is not pushed by the other cones, and a real drill has no forces in it at all. The physics picture also assumes the three charges are held in place; released, they would accelerate and every distance — and so every force — would change from instant to instant. And superposition is exact only for the forces: it does not let you add *distances* or *angles*, which is the slip behind almost every wrong answer here.

## Key takeaway

Each pair of charges acts as though the others were not there, so the total force is the **vector** sum of the individual Coulomb forces: $\vec{F}_\text{net} = \vec{F}_1 + \vec{F}_2 + \dots$. Work out one force at a time, draw each arrow with its correct direction, then combine — for perpendicular forces, $F_\text{net} = \sqrt{F_1^2 + F_2^2}$.
