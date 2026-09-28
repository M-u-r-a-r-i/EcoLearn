---
concept_id: coulombs_law
interest: smartphones
format: explain
title: Two foam beads that refuse to meet
check:
  question: |-
    Two small charged foam beads repel each other with a force of $20\,\mu\text{N}$. The charge on one bead is doubled, and the beads are moved twice as far apart. What is the force between them now?
  options:
    A: |-
      $20\,\mu\text{N}$, since doubling the charge and doubling the distance cancel out
    B: |-
      $40\,\mu\text{N}$
    C: |-
      $10\,\mu\text{N}$
    D: |-
      $5.0\,\mu\text{N}$
  answer: C
  explanation: |-
    $F \propto q_1 q_2 / r^2$. Doubling one charge doubles $F$; doubling $r$ divides it by $2^2 = 4$. Overall $F$ is multiplied by $2/4 = 1/2$, giving $10\,\mu\text{N}$, still repulsive.
  misconceptions:
    A: |-
      Treats the force as depending on $1/r$ instead of $1/r^2$, so the doubled distance only halves it and seems to undo the doubled charge.
    B: |-
      Accounts for the doubled charge but forgets that the force also depends on the distance between the charges.
    D: |-
      Applies the inverse-square fall to a quarter correctly but forgets that doubling one charge doubles the force.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a sunny window with a solar power bank on the sill, an opened phone box with foam beads clinging to the new phone, a film being peeled off a screen with dust jumping up to it, and a phone on a stand running a field-line app](scenes/smartphones/electric_charges_fields.svg "The white foam beads by the box have been rubbing against the packaging all the way from the factory. They carry charge.")

Tariq's new earbuds came packed in a tray of tiny white foam beads, and the beads have got everywhere. Two of them are stuck to his fingertip.

He flicks them onto his old phone, which is lying flat on the desk, screen up. The glass is smooth and the beads slide easily, and then something strange happens: the two beads skate *away* from each other and stop a few centimetres apart.

He nudges one towards the other with a toothpick. The closer he pushes it, the harder the other bead scoots away. Both beads rubbed against the same foam tray, so they carry the same kind of charge.

Tariq's cousin Ruhi, watching, says, "It's like magnets. The closer, the stronger. Probably twice as strong at half the distance?" Tariq isn't sure. How exactly does the push depend on the charges, and on how far apart they are?

## The physics

**Coulomb's law** gives the force between two **point charges** $q_1$ and $q_2$ at rest, a distance $r$ apart:

$$F = \frac{1}{4\pi\varepsilon_0}\,\frac{|q_1 q_2|}{r^2}, \qquad \frac{1}{4\pi\varepsilon_0} = k \approx 9.0 \times 10^{9}\,\text{N m}^2\,\text{C}^{-2}$$

where $\varepsilon_0 = 8.854 \times 10^{-12}\,\text{C}^2\,\text{N}^{-1}\,\text{m}^{-2}$ is the **permittivity of free space**.

- **Size:** proportional to the **product** of the charges, and to $1/r^2$, an **inverse-square law**. Halve the distance and the force becomes four times as big, not twice.
- **Direction:** along the line joining the charges; **repulsive** for like charges (Tariq's beads), **attractive** for unlike.
- **Pairs:** the two forces are equal in size and opposite in direction, as Newton's third law requires, even if one bead carries more charge than the other.

![Like charges repel and unlike charges attract; in each pair the two forces are equal in size, opposite in direction and along the line joining the charges](figures/coulombs_law/force-pairs.svg "Equal and opposite, along the joining line: repulsion for like charges, attraction for unlike.")

In vector form, the force on $q_2$ due to $q_1$ is
$$\vec{F}_{21} = \frac{1}{4\pi\varepsilon_0}\,\frac{q_1 q_2}{r^2}\,\hat{r}_{21}$$
where $\hat{r}_{21}$ is the unit vector **from $q_1$ towards $q_2$**. Put the charges in with their signs: a positive product means the force on $q_2$ points away from $q_1$ (repulsion), a negative one points towards it (attraction).

**Conditions:** point charges (small compared with $r$), at rest, in vacuum. Air changes the force by less than a tenth of a percent.

## Worked example

**Given (illustrative):** each bead carries $+1.0\,\text{nC}$, and they sit $r = 3.0\,\text{cm}$ apart.
**Find:** the force between them, and the force at half that distance.

**Step 1 — convert.** $q = 1.0 \times 10^{-9}\,\text{C}$, $r = 0.030\,\text{m}$, so $r^2 = 9.0 \times 10^{-4}\,\text{m}^2$.

**Step 2 — the force at 3 cm.**
$$F = \frac{9.0 \times 10^9 \times (1.0 \times 10^{-9})^2}{9.0 \times 10^{-4}} = \frac{9.0 \times 10^{-9}}{9.0 \times 10^{-4}} = 1.0 \times 10^{-5}\,\text{N}$$
Both charges are positive, so this is a repulsion: each bead is pushed directly away from the other.

**Step 3 — push them to 1.5 cm.** Halving $r$ divides $r^2$ by 4, so the force becomes four times bigger: $4.0 \times 10^{-5}\,\text{N}$. Ruhi's guess of "twice" was too small.

**Sanity check:** a foam bead a few millimetres across weighs roughly $10^{-5}\,\text{N}$, so a force of about its own weight is just enough to make it skid across smooth glass, which is what Tariq saw.

## Where the picture breaks

The beads are not perfect point charges: at 3 cm apart they are small enough that the law works well, but pressed almost together, their charge would shift towards their far sides and the simple formula would start to fail. The screen under them is not empty space either; it is glass, which slightly changes the forces near its surface, and friction decides where the beads actually stop. And Ruhi's magnet comparison is only loose: magnets always have two poles, while a single charge can sit on its own.

## Key takeaway

Two point charges push or pull each other along the line joining them with $F = \dfrac{1}{4\pi\varepsilon_0}\dfrac{|q_1 q_2|}{r^2}$: like charges repel, unlike attract, and the two forces are equal and opposite. The force is proportional to each charge and falls as the **square** of the distance, so halving the gap makes it four times stronger.
