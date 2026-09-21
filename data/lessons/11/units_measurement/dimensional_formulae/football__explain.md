---
concept_id: dimensional_formulae
interest: football
format: explain
title: Everything on the match report is built from three things
check:
  question: |-
    The match report lists the momentum of the ball after a hard clearance, defined as mass times velocity. What is the dimensional formula of momentum?
  options:
    A: |-
      $[\text{M}\,\text{L}\,\text{T}^{-1}]$
    B: |-
      $[\text{M}\,\text{L}\,\text{T}^{-2}]$
    C: |-
      $[\text{kg}\,\text{m}\,\text{s}^{-1}]$
    D: |-
      $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$
  answer: A
  explanation: |-
    Momentum $=$ mass $\times$ velocity, and velocity is $[\text{L}\,\text{T}^{-1}]$. So $[p] = [\text{M}] \times [\text{L}\,\text{T}^{-1}] = [\text{M}\,\text{L}\,\text{T}^{-1}]$.
  misconceptions:
    B: |-
      Multiplies mass by acceleration instead of velocity. $[\text{M}\,\text{L}\,\text{T}^{-2}]$ is force, not momentum.
    C: |-
      Writes the SI unit instead of the dimensions. A dimensional formula uses the base quantities M, L and T, not particular units like kg, m and s.
    D: |-
      Confuses momentum with kinetic energy: $mv^2$ has the velocity squared, giving $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A groundsman measures a goal with a tape; a ball sits on a scale and a match clock runs](scenes/football/units_measurement.svg "A tape for length, a scale for mass, a clock for time. Every other number is built from these.")

Anika has a summer internship with her city club's sports-science team. On her first day, Dr. Nair hands her the report from Sunday's match. For every player there's a row of numbers: distance covered, top speed, the sharpest acceleration, the average power of the fastest sprint. For the ball, there's the momentum of the hardest clearance and the force of the strongest header.

"How do you measure all this?" Anika asks. "Power? Momentum? There must be a dozen instruments."

"Three," says Dr. Nair. "The cameras give positions — lengths. The clock gives times. And we weigh the players and the ball — mass. Everything else on that page is calculated."

Anika looks at the columns again. Speed, force, power, momentum: they seem like completely different things. How can all of them come from just mass, length and time? And is there a way to write down exactly what each one is made of?

## The physics

Every physical quantity can be expressed in terms of the base quantities. In mechanics you need three: **mass [M]**, **length [L]** and **time [T]**. (The other base quantities — electric current, temperature, amount of substance and luminous intensity — appear in later chapters.)

The **dimensions** of a quantity are the powers to which the base quantities are raised to represent it. The expression showing them, in square brackets, is its **dimensional formula**. Writing a quantity equal to its dimensional formula, like $[v] = [\text{L}\,\text{T}^{-1}]$, is a **dimensional equation**.

To find a dimensional formula, start from the quantity's defining equation and replace each quantity by its dimensions:

![A ladder: velocity is L T to the minus 1, acceleration L T to the minus 2, force M L T to the minus 2, work and energy M L squared T to the minus 2, power M L squared T to the minus 3](figures/dimensional_formulae/dimension-building-blocks.svg "Each quantity is built from the one above it. Dividing by time lowers the power of T by one; multiplying by a length raises the power of L by one.")

- velocity $=$ displacement $\div$ time: $[\text{L}\,\text{T}^{-1}]$
- acceleration $=$ velocity $\div$ time: $[\text{L}\,\text{T}^{-2}]$
- force $=$ mass $\times$ acceleration: $[\text{M}\,\text{L}\,\text{T}^{-2}]$
- momentum $=$ mass $\times$ velocity: $[\text{M}\,\text{L}\,\text{T}^{-1}]$
- work or energy $=$ force $\times$ displacement: $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$
- power $=$ work $\div$ time: $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$

Pure numbers ($\tfrac{1}{2}$, $2\pi$) and ratios of like quantities (an angle, a percentage) have no dimensions: they are **dimensionless**, $[\text{M}^0\,\text{L}^0\,\text{T}^0]$.

So every column of Dr. Nair's report is a different recipe from the same three ingredients. The header's force is $[\text{M}\,\text{L}\,\text{T}^{-2}]$; the clearance's momentum is $[\text{M}\,\text{L}\,\text{T}^{-1}]$; the sprint's power is $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$.

## Worked example

**Find** the dimensional formula of (a) the air pressure inside the ball, force $\div$ area; (b) a sprinter's power, calculated as force $\times$ velocity.

(a) Area is length × length, $[\text{L}^2]$:

$$[\text{pressure}] = \frac{[\text{M}\,\text{L}\,\text{T}^{-2}]}{[\text{L}^2]} = [\text{M}\,\text{L}^{-1}\,\text{T}^{-2}]$$

(b) Multiply the dimensions, adding the powers of each base quantity:

$$[F\,v] = [\text{M}\,\text{L}\,\text{T}^{-2}] \times [\text{L}\,\text{T}^{-1}] = [\text{M}\,\text{L}^2\,\text{T}^{-3}]$$

**Sanity check:** power was also defined as work $\div$ time: $[\text{M}\,\text{L}^2\,\text{T}^{-2}] \div [\text{T}] = [\text{M}\,\text{L}^2\,\text{T}^{-3}]$. Two routes, same formula — as they must be if both describe power.

## Where the picture breaks

Dimensions tell you what a quantity is *made of*, not *which* quantity it is: different quantities can share a dimensional formula (work and torque, which you'll meet later, are both $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$). And dimensions are not units. A length is $[\text{L}]$ whether the report gives it in metres, kilometres or the yards of the old rulebooks.

## Key takeaway

A dimensional formula shows how a quantity is built from the base quantities: $[\text{M}\,\text{L}\,\text{T}^{-2}]$ for force, $[\text{M}\,\text{L}\,\text{T}^{-1}]$ for momentum. Get it from the defining equation, one step at a time; pure numbers and angles are dimensionless and drop out.
