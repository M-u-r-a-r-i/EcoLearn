---
concept_id: universal_gravitation
interest: cricket
format: explain
title: Why new cricket balls don't roll towards each other
check:
  question: |-
    Two cricket balls, each of mass $0.16\,\text{kg}$, sit with their centres $0.20\,\text{m}$ apart. Taking $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$, what is the gravitational force between them?
  options:
    A: |-
      $8.5 \times 10^{-12}\,\text{N}$
    B: |-
      $4.3 \times 10^{-5}\,\text{N}$
    C: |-
      $4.3 \times 10^{-11}\,\text{N}$
    D: |-
      $5.3 \times 10^{-10}\,\text{N}$
  answer: C
  explanation: |-
    $F = Gm_1m_2/r^2 = 6.67 \times 10^{-11} \times 0.16 \times 0.16 / (0.20)^2 = 1.71 \times 10^{-12}/0.040 \approx 4.3 \times 10^{-11}\,\text{N}$.
  misconceptions:
    A: |-
      Divides by $r$ instead of $r^2$, missing the inverse-square dependence on distance.
    B: |-
      Substitutes the masses in grams ($160\,\text{g}$) instead of kilograms, a unit slip that makes the force a million times too large.
    D: |-
      Adds the two masses instead of multiplying them; the force is proportional to the product $m_1m_2$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: a ball skied above a fielder, the Moon and a satellite overhead, and a broadcast van's dish aimed at the sky](scenes/cricket/gravitation.svg "The ball, the Moon and the satellite all feel the same kind of pull, from the same Earth.")

The club has just received a box of new balls, and Ananya, the team's wicketkeeper, is unpacking them onto the dressing-room table. Rohan, who has just finished a physics chapter, picks one up and grins.

"Our textbook says every mass in the universe pulls every other mass. So these balls are pulling each other right now."

"Then why aren't they rolling together?" Ananya asks. She places two balls a hand's width apart on the smooth table. They sit perfectly still.

Rohan tosses a third ball into the air. It comes straight back down into his palm. "The Earth pulls it, no problem."

So which is it? If every ball pulls every other ball, why does Earth's pull win so completely? How strong is the pull between two cricket balls, really?

## The physics

**Newton's law of universal gravitation:** every particle in the universe attracts every other particle with a force that is directly proportional to the product of their masses and inversely proportional to the square of the distance between them:

$$F = \frac{G\,m_1 m_2}{r^2}$$

- $m_1$, $m_2$ are the masses (kg) and $r$ is the distance between them (m). For uniform spheres, like cricket balls or (nearly) the Earth, $r$ is measured **between the centres**, and each sphere acts as if all its mass were at its centre.
- $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$ is the **universal gravitational constant**. It is the same everywhere, for every pair of masses.
- The force is always **attractive** and acts **along the line joining the two centres**.
- The two forces form a **Newton's third law pair**: the ball pulls the Earth exactly as hard as the Earth pulls the ball.

![Two spheres pulling each other with equal and opposite red arrows; below, bars show the pull falling to a quarter at twice the distance and a ninth at three times](figures/universal_gravitation/force-pair-inverse-square.svg "The pulls on the two masses are equal and opposite. Double the distance and the pull drops to a quarter; triple it and it drops to a ninth.")

Newton published this law in 1687 in the *Principia*, and used it to explain both a falling apple and the Moon's orbit with one rule. The same law explains how Rohan's ball falls back to his hand and why the Moon stays in orbit round the Earth.

![The Latin title page of Newton's Principia Mathematica, printed in London in 1687](famous/newton-principia-title-page.jpg "Newton set out universal gravitation in the Principia (1687). Public domain, via Wikimedia Commons.")

## Worked example

**Given:** two balls of mass $m = 0.16\,\text{kg}$ each, centres $r = 0.10\,\text{m}$ apart; $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$. Earth: $M = 6.0 \times 10^{24}\,\text{kg}$, $R = 6.4 \times 10^{6}\,\text{m}$.
**Find:** (a) the pull between the balls; (b) the Earth's pull on one ball.

(a)
$$F = \frac{6.67 \times 10^{-11} \times 0.16 \times 0.16}{(0.10)^2} = \frac{1.71 \times 10^{-12}}{0.010} \approx 1.7 \times 10^{-10}\,\text{N}$$

(b) The Earth acts as a point mass at its centre, $R$ from the ball:

$$F = \frac{6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times 0.16}{(6.4 \times 10^{6})^2} = \frac{6.40 \times 10^{13}}{4.10 \times 10^{13}} \approx 1.6\,\text{N}$$

**Sanity check:** (b) should equal the ball's weight, $mg = 0.16 \times 9.8 = 1.57\,\text{N}$, and it does. The Earth's pull is about $10^{10}$ times the pull between the balls. The balls do attract each other, but the force is far too small to overcome even a tiny amount of friction on the table.

## Where the picture breaks

A cricket ball is not a perfect uniform sphere: it has a cork core, layers of string and a leather case, and a raised seam. The point-mass rule is exact only for spherically symmetric bodies, but at these distances the error is negligible. The law also applies to real balls only when you use centre-to-centre distance. If two balls touch, $r$ is about one ball's diameter, not zero, so the force doesn't blow up.

On the table, the balls also feel friction, and air currents in the room would push them far harder than their gravity does. That is why their pull on each other can only be measured with very sensitive apparatus, such as a torsion balance.

## Key takeaway

Every pair of masses attracts with $F = Gm_1m_2/r^2$, along the line joining their centres, with equal and opposite forces on the two bodies. Because $G$ is tiny, the pull only becomes noticeable when at least one mass is enormous, like the Earth. That's why the Earth pulls a ball down with about $1.6\,\text{N}$, while two balls pull each other with less than a billionth of a newton.
