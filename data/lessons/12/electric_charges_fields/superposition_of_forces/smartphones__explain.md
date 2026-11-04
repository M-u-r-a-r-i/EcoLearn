---
concept_id: superposition_of_forces
interest: smartphones
format: explain
title: The force arrow that pointed nowhere expected
check:
  question: |-
    In a charge-simulator app, a test charge feels a force of $30\,\mu\text{N}$ to the east from one charge and a force of $30\,\mu\text{N}$ to the north from another. What is the net force on it?
  options:
    A: |-
      $60\,\mu\text{N}$, towards the north-east
    B: |-
      Zero, because the two forces balance
    C: |-
      $30\,\mu\text{N}$, towards the north-east
    D: |-
      About $42\,\mu\text{N}$, towards the north-east
  answer: D
  explanation: |-
    Forces add as vectors. At right angles, the size is $\sqrt{30^2 + 30^2} = 30\sqrt{2} \approx 42\,\mu\text{N}$, and since the two parts are equal it points exactly between them, towards the north-east.
  misconceptions:
    A: |-
      Adds the sizes as plain numbers. That only works when both forces point the same way; at right angles the net force is smaller than their sum.
    B: |-
      Thinks two equal forces always cancel. They cancel only when they point in opposite directions, not at right angles.
    C: |-
      Thinks combining two equal forces keeps the same size and only changes the direction, instead of adding them head-to-tail.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a sunny window with a solar power bank on the sill, an opened phone box with foam beads clinging to the new phone, a film being peeled off a screen with dust jumping up to it, and a phone on a stand running a field-line app](scenes/smartphones/electric_charges_fields.svg "The phone on the stand is running a charge simulator. Jhanvi is about to use one to test a prediction.")

Jhanvi's physics teacher has recommended a free charge-simulator app, and on the bus home she opens it. You drop charges on a grid, and the app draws the force on each one as an arrow.

She places a small positive test charge at one corner. Then she drops a bigger positive charge 3 cm to its right and a negative charge 3 cm straight above it.

Before tapping "show forces", she makes a prediction to her friend Samar: "The negative one pulls hardest. It's opposite. The arrow will point straight up at it."

She taps. The arrow points up *and to the left*, slanting away across the grid towards neither charge. Samar laughs. Jhanvi frowns at the screen. The test charge is feeling two forces at once. How does the app decide on one arrow, and how long should that arrow be?

## The physics

The **superposition principle**: the force on a charge due to several other charges is the **vector sum** of the forces each one would exert on its own. Each pair interacts by Coulomb's law exactly as if the others were not there:

$$\vec{F}_0 = \vec{F}_{01} + \vec{F}_{02} + \vec{F}_{03} + \dots, \qquad \vec{F}_{0i} = \frac{1}{4\pi\varepsilon_0}\,\frac{q_0 q_i}{r_{0i}^2}\,\hat{r}_{i0}$$

where $\hat{r}_{i0}$ is the unit vector from $q_i$ towards $q_0$. The method:

1. Find each force separately: its size from $F = k|q_0 q_i|/r^2$, its direction from the signs (away for like charges, towards for unlike).
2. Add them **as vectors**, head-to-tail or by components. Never add the sizes as plain numbers unless the forces point the same way.

![The corner charge feels a force to the left from the positive charge beside it and a force upwards from the negative charge above it; the net force points up and to the left at 37 degrees](figures/superposition_of_forces/right-angle-superposition.svg "This figure shows the same layout with larger lab charges. Its forces are also in the ratio 4 to 3, so the net force again slants at 37 degrees.")

The principle also covers a **continuous charge distribution**, such as charge smeared along a rod or over a screen. Split it into tiny pieces $dq$ (with $dq = \lambda\,dl$ along a line, $\sigma\,dS$ over a surface, $\rho\,dV$ through a volume), treat each as a point charge, and add all their forces; in the limit the sum becomes an integral.

## Worked example

**Given (Jhanvi's app, illustrative numbers):** test charge $q_0 = +1.0\,\text{nC}$; $q_1 = +4.0\,\text{nC}$ is $3.0\,\text{cm}$ to its right; $q_2 = -3.0\,\text{nC}$ is $3.0\,\text{cm}$ above it. Both distances give $r^2 = 9.0 \times 10^{-4}\,\text{m}^2$.
**Find:** the net force on $q_0$.

**Step 1 — force from $q_1$ (repulsion, to the left).**
$$F_1 = \frac{9.0 \times 10^9 \times (1.0 \times 10^{-9})(4.0 \times 10^{-9})}{9.0 \times 10^{-4}} = 4.0 \times 10^{-5}\,\text{N} = 40\,\mu\text{N}$$

**Step 2 — force from $q_2$ (attraction, upwards).** Same working with $3.0\,\text{nC}$: $F_2 = 30\,\mu\text{N}$. So the negative charge was *not* the stronger one; the bigger positive charge wins.

**Step 3 — add at right angles.**
$$F = \sqrt{40^2 + 30^2} = 50\,\mu\text{N}, \qquad \tan\theta = \frac{30}{40} \Rightarrow \theta \approx 37^\circ$$
The net force is $50\,\mu\text{N}$, pointing up and to the left at $37^\circ$ above the leftward direction, exactly the slanting arrow Jhanvi saw.

**Sanity check:** the net force is bigger than either part but smaller than their sum of $70\,\mu\text{N}$, as it must be for two forces at right angles.

## Where the picture breaks

The app draws perfect point charges fixed in place, so it can apply Coulomb's law exactly. Real charged specks have size, and nearby conductors (like the phone's own metal frame, if these were real charges on a real screen) would rearrange their own charges and add forces of their own. Superposition still holds; there are just more charges to add. It holds because electric forces are linear: one charge's force doesn't change because another charge is present.

## Key takeaway

The net force on a charge is the **vector sum** of the separate Coulomb forces from every other charge, each worked out as if the others weren't there. Find each force's size and direction first, then add them head-to-tail; for a continuous distribution, add up tiny pieces $dq$.
