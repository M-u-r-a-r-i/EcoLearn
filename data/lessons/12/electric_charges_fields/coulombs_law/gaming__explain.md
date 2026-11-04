---
concept_id: coulombs_law
interest: gaming
format: explain
title: The repulsion that made her game feel wrong
check:
  question: |-
    Two small charged spheres attract each other with a force of $0.80\,\text{N}$. One of the charges is then doubled, and the separation between the spheres is doubled as well. What is the force now?
  options:
    A: |-
      $0.40\,\text{N}$, still attraction
    B: |-
      $1.6\,\text{N}$, still attraction
    C: |-
      $0.80\,\text{N}$, still attraction
    D: |-
      $0.20\,\text{N}$, still attraction
  answer: A
  explanation: |-
    $F \propto q_1 q_2 / r^2$. Doubling one charge multiplies the force by 2; doubling the separation divides it by $2^2 = 4$. Together: $0.80 \times 2 / 4 = 0.40\,\text{N}$, and the signs are unchanged, so it is still attraction.
  misconceptions:
    B: |-
      Applies the charge change but ignores the distance, as if the force depended only on how much charge there is.
    C: |-
      Treats the force as inversely proportional to $r$ rather than $r^2$, so the doubling of charge and distance seem to cancel out.
    D: |-
      Divides by 4 for the distance but forgets that one charge was doubled as well.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night during a PC build: a monitor running a field sandbox with two charges, a plasma globe, an antistatic bag sparking to a fingertip, and an open PC case with a graphics card going in](scenes/gaming/electric_charges_fields.svg "On the monitor, two charges push and pull across empty space. How strongly?")

Meher has thirty-six hours to finish her game-jam entry. The idea is simple and, on paper, lovely: two glowing orbs that push each other apart, and a player who has to squeeze between them.

She writes the repulsion herself. In her code the push halves when the orbs get twice as far apart — that felt reasonable at two in the morning.

At the playtest table it feels awful. Far apart, the orbs still shove the player around the whole level. Up close, where the level is supposed to be terrifying, the squeeze is barely there. One tester says the orbs feel like they are joined by rubber bands rather than pushing through the air.

Meher stares at her two lines of code. Real charges do push each other apart across empty space. But how, exactly, does that push depend on how much charge there is — and on how far apart the charges are?

## The physics

**Coulomb's law** (Charles-Augustin de Coulomb, 1785, measured with a torsion balance) gives the force between two **point charges** $q_1$ and $q_2$, a distance $r$ apart and at rest:

$$F = k\,\frac{|q_1 q_2|}{r^2}, \qquad k = \frac{1}{4\pi\varepsilon_0} \approx 9.0 \times 10^{9}\,\text{N m}^2\,\text{C}^{-2}$$

where $\varepsilon_0 = 8.854 \times 10^{-12}\,\text{C}^2\,\text{N}^{-1}\,\text{m}^{-2}$ is the **permittivity of free space**. The law says three things.

- **Size:** the force is proportional to the product of the charges, and inversely proportional to the **square** of the distance. That squared is exactly what Meher got wrong: double the separation and the force drops to a **quarter**, not a half.
- **Direction:** along the line joining the charges — repulsive for like charges, attractive for unlike.
- **Pairs:** the force on $q_1$ from $q_2$ is equal and opposite to the force on $q_2$ from $q_1$, as Newton's third law requires.

![Two pairs of point charges: like charges pushed apart and unlike charges pulled together, each pair with two equal and opposite force arrows along the line joining them](figures/coulombs_law/force-pairs.svg "Equal and opposite, always along the joining line: repulsion for like charges, attraction for unlike.")

In vector form, the force on $q_2$ due to $q_1$ is

$$\vec{F}_{21} = \frac{1}{4\pi\varepsilon_0}\,\frac{q_1 q_2}{r^2}\,\hat{r}_{21}$$

with $\hat{r}_{21}$ the unit vector pointing **from $q_1$ towards $q_2$**. Put the charges in *with* their signs: if the product $q_1 q_2$ is positive, the force on $q_2$ points away from $q_1$ (repulsion); if it is negative, towards it (attraction). The algebra then handles the direction for you.

**Conditions:** the charges must be small compared with the distance between them (point charges) and at rest, and the law as written is for vacuum — air changes it by less than a part in a thousand.

## Worked example

**Given (illustrative):** two charged spheres, $q_1 = +2.0\,\mu\text{C}$ and $q_2 = +3.0\,\mu\text{C}$, held $r = 0.30\,\text{m}$ apart.
**Find:** the force between them, and the force when they are moved to $0.60\,\text{m}$.

Convert first: $1\,\mu\text{C} = 10^{-6}\,\text{C}$, so the product of the charges is $2.0 \times 10^{-6} \times 3.0 \times 10^{-6} = 6.0 \times 10^{-12}\,\text{C}^2$.

$$F = \frac{9.0 \times 10^{9} \times 6.0 \times 10^{-12}}{(0.30)^2} = \frac{0.054}{0.090} = 0.60\,\text{N}$$

Both charges are positive, so this is a push, and it is about the weight of a tennis ball sitting in your palm — a force you would certainly feel.

Now double the distance. The force falls by $2^2 = 4$:

$$F = \frac{0.60}{4} = 0.15\,\text{N}$$

Barely a quarter of the shove, from moving just $30\,\text{cm}$ further away. That steep fall-off is what Meher's game was missing.

**Sanity check:** a direct recalculation gives $0.054/0.36 = 0.15\,\text{N}$, the same answer, so the shortcut was used correctly.

## Where the picture breaks

Meher's orbs are drawn as fat glowing balls, but Coulomb's law is exact only for **point** charges — bodies small compared with the gap between them. Push two real charged spheres close together and their charges shift around on the surfaces, and the simple formula starts to fail.

The law is also for charges **at rest**. Her orbs move, and moving charges make magnetic effects too, which this chapter ignores. Fixing the exponent will make her game feel right; it will not make it a simulation.

## Key takeaway

Two point charges push or pull each other along the line joining them with $F = \dfrac{1}{4\pi\varepsilon_0}\dfrac{|q_1 q_2|}{r^2}$ — like charges repel, unlike attract. The force is proportional to each charge and follows an **inverse-square** law, so doubling the separation quarters it. Keep the signs in the vector form and they give you the direction.
