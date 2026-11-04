---
concept_id: coulombs_law
interest: cricket
format: explain
title: One coulomb at each end of the pitch
check:
  question: |-
    Two small charged spheres, $0.20\,\text{m}$ apart, repel each other with a force of $0.36\,\text{N}$. They are moved apart until they are $0.40\,\text{m}$ apart, with their charges unchanged. What is the force between them now?
  options:
    A: |-
      $0.18\,\text{N}$, still repulsive
    B: |-
      $0.72\,\text{N}$, still repulsive
    C: |-
      $0.36\,\text{N}$, still repulsive
    D: |-
      $0.090\,\text{N}$, still repulsive
  answer: D
  explanation: |-
    Coulomb's force goes as $1/r^2$. Doubling $r$ divides the force by $2^2 = 4$: $0.36/4 = 0.090\,\text{N}$. The charges keep their signs, so it is still repulsion.
  misconceptions:
    A: |-
      Treats the force as inversely proportional to distance ($1/r$) instead of the square of the distance.
    B: |-
      Thinks the force grows with separation, as if the charges were joined by a stretched spring.
    C: |-
      Thinks the force depends only on the size of the charges, not on how far apart they are.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A storm over a cricket ground: dark clouds, distant lightning, players walking off, groundstaff dragging a plastic cover and a team bus waiting](scenes/cricket/electric_charges_fields.svg "A lightning flash moves several coulombs of charge. Just how big is a coulomb?")

Thunder rumbles in the distance, and the academy's under-17 girls shelter under the pavilion roof. Their weekend coach, Mr Dutta, teaches physics on weekdays, and he can't resist.

"That lightning," he says, "moves several coulombs of charge. Here's a question. Put one coulomb on this ball at the bowler's end, and one coulomb on the stumps at the far end, 22 yards away. How hard do they push each other apart?"

Sneha, the team's opening bowler, shrugs. "Twenty metres is a long way. Not much, surely. A few newtons?"

"Loser buys the samosas," says Mr Dutta.

Sneha thinks about it. Charges push and pull without touching, across empty space. But how does that push depend on how much charge there is, and on how far apart the charges are? Before she can settle the bet, she needs the rule.

## The physics

**Coulomb's law** (Charles-Augustin de Coulomb, 1785, measured with a torsion balance) gives the force between two **point charges** $q_1$ and $q_2$ a distance $r$ apart, at rest:

$$F = k\,\frac{|q_1 q_2|}{r^2}, \qquad k = \frac{1}{4\pi\varepsilon_0} \approx 9.0 \times 10^{9}\,\text{N m}^2\,\text{C}^{-2}$$

Here $\varepsilon_0 = 8.854 \times 10^{-12}\,\text{C}^2\,\text{N}^{-1}\,\text{m}^{-2}$ is the **permittivity of free space**. The law has three parts:

- **Size:** proportional to the product of the charges, and inversely proportional to the **square** of the distance. Double $r$ and the force drops to a quarter.
- **Direction:** along the line joining the charges; **repulsive** for like charges, **attractive** for unlike.
- **Pairs:** the force on $q_1$ due to $q_2$ is equal and opposite to the force on $q_2$ due to $q_1$, as Newton's third law requires.

![Like charges repel and unlike charges attract; in each pair the two forces are equal in size, opposite in direction and along the line joining the charges](figures/coulombs_law/force-pairs.svg "Equal and opposite, along the joining line: repulsion for like charges, attraction for unlike.")

In vector form, the force on $q_2$ due to $q_1$ is

$$\vec{F}_{21} = \frac{1}{4\pi\varepsilon_0}\,\frac{q_1 q_2}{r^2}\,\hat{r}_{21}$$

where $\hat{r}_{21}$ is the unit vector pointing **from $q_1$ to $q_2$**. Put the charges in *with* their signs: if $q_1 q_2$ is positive, the force on $q_2$ points away from $q_1$ (repulsion); if negative, towards it (attraction). The signs do the direction work for you.

**Conditions:** the charges must be small compared with $r$ (point charges) and at rest, and the law as written is for vacuum; air makes almost no difference.

## Worked example

**Part 1 (the bet).** $q_1 = q_2 = 1.0\,\text{C}$, $r = 20.12\,\text{m}$ (the length of the pitch).

$$F = \frac{9.0 \times 10^9 \times 1.0 \times 1.0}{(20.12)^2} = \frac{9.0 \times 10^9}{404.8} \approx 2.2 \times 10^{7}\,\text{N}$$

That is the weight of about $2.2 \times 10^7 / 9.8 \approx 2.3 \times 10^6\,\text{kg}$: over two thousand tonnes. Sneha buys the samosas. A coulomb is an enormous amount of charge to hold on an object; lightning can move several coulombs only because it's a flow of charge, not charge sitting on a ball.

**Part 2 (a realistic charge).** $q_1 = +20\,\text{nC}$, and $q_2 = -30\,\text{nC}$ sits $r = 0.10\,\text{m}$ to its east. Find the force on $q_2$.

Convert: $20\,\text{nC} = 2.0 \times 10^{-8}\,\text{C}$, $30\,\text{nC} = 3.0 \times 10^{-8}\,\text{C}$. Take east as positive; $\hat{r}_{21}$ points east.

$$F_{21} = \frac{9.0 \times 10^9 \times (2.0 \times 10^{-8})(-3.0 \times 10^{-8})}{(0.10)^2} = \frac{-5.4 \times 10^{-6}}{0.010} = -5.4 \times 10^{-4}\,\text{N}$$

The minus sign means west: $q_2$ is pulled towards $q_1$, as unlike charges should be. The force on $q_1$ is $5.4 \times 10^{-4}\,\text{N}$ east.

**Sanity check:** $5.4 \times 10^{-4}\,\text{N}$ is about the weight of $55\,\text{mg}$, the sort of force that lifts a scrap of paper, which matches what small charges do in a lab.

## Where the picture breaks

A ball and a set of stumps are not point charges: charge would spread over their surfaces, and the stumps are hammered into the earth, so any charge would simply drain away. The one-coulomb bet is a thought experiment to feel the size of a coulomb, not something that could happen. Coulomb's law is exact for point charges at rest; for extended bodies you add up the contributions of many small pieces, which comes next.

## Key takeaway

Two point charges exert equal and opposite forces along the line joining them, $F = \dfrac{1}{4\pi\varepsilon_0}\dfrac{|q_1 q_2|}{r^2}$: like charges repel, unlike attract. The force follows an inverse-square law, so doubling the distance quarters it. Keep the signs in the vector form and they give you the direction.
