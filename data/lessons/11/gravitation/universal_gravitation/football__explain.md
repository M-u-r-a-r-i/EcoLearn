---
concept_id: universal_gravitation
interest: football
format: explain
title: Does a big centre-back really pull the ball towards him
check:
  question: |-
    Two footballs with centres a distance $d$ apart attract each other with a gravitational force $F$. One ball is replaced by a medicine ball with $3$ times its mass, and the distance between the centres is doubled to $2d$. What is the new force?
  options:
    A: |-
      $\tfrac{3}{2}F$
    B: |-
      $\tfrac{1}{2}F$
    C: |-
      $\tfrac{3}{4}F$
    D: |-
      $12F$
  answer: C
  explanation: |-
    $F = Gm_1m_2/r^2$. Tripling one mass multiplies the force by $3$; doubling the distance divides it by $2^2 = 4$. The new force is $3F/4$.
  misconceptions:
    A: |-
      Divides by the distance instead of its square, missing the inverse-square law.
    B: |-
      Adds the masses instead of multiplying them: the total mass goes from $2m$ to $4m$, a factor of $2$, which divided by $4$ gives $F/2$.
    D: |-
      Multiplies by the square of the distance instead of dividing, as if the pull grew stronger with separation.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: the goalkeeper's long kick at the top of its arc, the Moon and a satellite overhead, and a dish on the stand roof aimed at the satellite](scenes/football/gravitation.svg "The ball falls back to the pitch because the Earth pulls it. Do the players pull it too?")

Sameer is the biggest player in the squad, a centre-back who wins every header. Before training, the ball rolls slowly across the grass and stops right at his boots.

"See?" he tells Riya, the team's left-back. "Gravity. I'm so massive the ball comes to me."

Riya laughs, but she has just finished the gravitation chapter. "Actually, you're half right. Newton says every mass pulls every other mass. So you *are* pulling the ball."

"Told you."

"But then the goalposts pull it too. And the stands. And me. So why does it just sit there?" She picks the ball up and lets go. It drops straight to the grass. "The Earth wins every time."

How strong is Sameer's pull on the ball, really, and how does it compare with the Earth's?

## The physics

**Newton's law of universal gravitation:** every particle in the universe attracts every other particle with a force proportional to the product of their masses and inversely proportional to the square of the distance between them:

$$F = \frac{G\,m_1 m_2}{r^2}$$

- $m_1$ and $m_2$ are the masses in kg; $r$ is the distance between them in m. For uniform spheres, like a football or (nearly) the Earth, $r$ is measured **between the centres**, and each sphere acts as if all its mass sat at its centre.
- $G = 6.67 \times 10^{-11}\,\text{N m}^2/\text{kg}^2$ is the **universal gravitational constant**, the same for every pair of masses everywhere.
- The force is always **attractive** and acts **along the line joining the centres**.
- The forces on the two bodies are a **Newton's third law pair**: the ball pulls Sameer exactly as hard as Sameer pulls the ball.

Because it's an inverse-square law, doubling the distance cuts the force to a quarter, and tripling it cuts the force to a ninth.

![Two spheres pulling each other with equal and opposite red arrows; below, bars show the pull falling to a quarter at twice the distance and a ninth at three times](figures/universal_gravitation/force-pair-inverse-square.svg "The two pulls are equal and opposite. Double the distance and the force drops to a quarter; triple it and it drops to a ninth.")

Newton set out this law in 1687 in the *Principia*, where one rule explained both a falling object and the Moon's orbit.

![The Latin title page of Newton's Principia Mathematica, printed in London in 1687](famous/newton-principia-title-page.jpg "Newton published universal gravitation in the Principia (1687). Public domain, via Wikimedia Commons.")

## Worked example

**Given:** a ball of mass $0.43\,\text{kg}$ (within the allowed $410$–$450\,\text{g}$); Sameer, mass $80\,\text{kg}$ (illustrative), treated roughly as a point mass $1.0\,\text{m}$ from the ball's centre. Earth: $M = 6.0 \times 10^{24}\,\text{kg}$, $R = 6.4 \times 10^{6}\,\text{m}$.
**Find:** (a) Sameer's pull on the ball; (b) the Earth's pull on the ball.

(a)
$$F = \frac{6.67 \times 10^{-11} \times 80 \times 0.43}{(1.0)^2} = 6.67 \times 10^{-11} \times 34.4 \approx 2.3 \times 10^{-9}\,\text{N}$$

(b) The Earth acts as a point mass at its centre, a distance $R$ away:

$$F = \frac{6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times 0.43}{(6.4 \times 10^{6})^2} = \frac{1.72 \times 10^{14}}{4.10 \times 10^{13}} \approx 4.2\,\text{N}$$

**Sanity check:** (b) should be the ball's weight, $mg = 0.43 \times 9.8 = 4.2\,\text{N}$, and it is. The Earth's pull is about $4.2 / (2.3 \times 10^{-9}) \approx 2 \times 10^{9}$ times Sameer's. If Sameer stepped back to $2.0\,\text{m}$, his pull would drop to a quarter, about $5.7 \times 10^{-10}\,\text{N}$.

## Where the picture breaks

A player is not a sphere, so treating Sameer as a point mass $1\,\text{m}$ away only gives the right order of magnitude. The exact rule "use the centre-to-centre distance" holds for spherically symmetric bodies. A football is close to that, a person is not.

The ball also didn't roll to Sameer because of gravity. A pull of a few billionths of a newton is far smaller than the rolling resistance of grass or the push of a light breeze; the ball simply ran out of speed near his feet. Pulls this small can be measured only with delicate apparatus such as a torsion balance.

## Key takeaway

Any two masses attract with $F = Gm_1m_2/r^2$, along the line joining their centres, with equal and opposite forces on the two bodies. Because $G$ is so small, the pull is noticeable only when at least one mass is enormous: the Earth pulls a football with about $4.2\,\text{N}$, while a player pulls it with only about $10^{-9}\,\text{N}$.
