---
concept_id: dimensional_formulae
interest: cricket
format: challenge
title: Are newton-seconds and kilogram metres per second the same thing
check:
  question: |-
    The coaching app also reports "power", defined as work done divided by the time taken. What is the dimensional formula of power?
  options:
    A: |-
      $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$
    B: |-
      $[\text{M}\,\text{L}\,\text{T}^{-3}]$
    C: |-
      $[\text{M}\,\text{L}^2\,\text{T}^{-3}]$
    D: |-
      $[\text{M}\,\text{L}^2\,\text{T}^{-1}]$
  answer: C
  explanation: |-
    Work is $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$. Dividing by time lowers the power of T by one: $[\text{M}\,\text{L}^2\,\text{T}^{-2}] / [\text{T}] = [\text{M}\,\text{L}^2\,\text{T}^{-3}]$.
  misconceptions:
    A: |-
      Forgets to divide by time. $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$ is work or energy, not the rate of doing work.
    B: |-
      Starts from force instead of work, missing the extra length that work (force $\times$ displacement) carries.
    D: |-
      Multiplies work by time instead of dividing, so the power of T goes up instead of down.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch; a speed display shows 142 km/h](scenes/cricket/units_measurement.svg "Two units that look nothing alike. Are they measuring the same kind of thing?")

Twins Dhruv and Diya both play for their school, and they both love numbers — but they never agree about them.

After a session, the academy's coaching app shows Dhruv's best drive: *bat impulse 11 N s*. The app's help page defines impulse as the force of the bat multiplied by the contact time.

Diya has worked out the same shot in her physics notebook, using the ball's speeds before and after: *change in momentum of ball = 11.2 kg m/s*.

"Different units, different things," Dhruv says. "Yours is kilograms and metres. Mine is newtons and seconds. Nothing in common."

"But the numbers are almost the same," Diya says. "That can't be a coincidence."

Is it? How could you tell, without knowing any more physics, whether "newton-seconds" and "kilogram metres per second" measure the same kind of quantity?

## The challenge

Using only the dimensions of M, L and T, find the dimensional formula of:

1. impulse, defined as force $\times$ time;
2. momentum, defined as mass $\times$ velocity.

Do they have the same dimensions? Then, for contrast, find the dimensions of force $\times$ *distance*. Is that the same as the other two?

## Think first

Dhruv thinks the units look so different that the quantities can't be related. Diya suspects a connection. What do you expect: two different dimensional formulas, or one? And if you multiply force by a distance instead of a time, should the answer stay the same? Write your guesses down.

## The reveal

Build each formula from its definition.

**Force** first, since impulse needs it: force $=$ mass $\times$ acceleration, and acceleration is $[\text{L}\,\text{T}^{-2}]$, so $[F] = [\text{M}\,\text{L}\,\text{T}^{-2}]$.

**Impulse** $=$ force $\times$ time:

$$[F \times t] = [\text{M}\,\text{L}\,\text{T}^{-2}] \times [\text{T}] = [\text{M}\,\text{L}\,\text{T}^{-1}]$$

**Momentum** $=$ mass $\times$ velocity:

$$[m \times v] = [\text{M}] \times [\text{L}\,\text{T}^{-1}] = [\text{M}\,\text{L}\,\text{T}^{-1}]$$

The same. Diya's hunch was right: $1\,\text{N}\,\text{s} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2} \times \text{s} = 1\,\text{kg}\,\text{m/s}$. The two units are identical once you unpack the newton. (In the chapter on the laws of motion, you'll see why the numbers match: the impulse of the bat *is* the change in the ball's momentum.)

**Force × distance** is different:

$$[F \times s] = [\text{M}\,\text{L}\,\text{T}^{-2}] \times [\text{L}] = [\text{M}\,\text{L}^2\,\text{T}^{-2}]$$

That is work or energy. Multiplying the same force by a *time* or by a *distance* gives quantities of completely different kinds.

![A ladder: velocity, acceleration, force, work and power, each with its dimensional formula](figures/dimensional_formulae/dimension-building-blocks.svg "Multiplying by T raises the power of T; multiplying by L raises the power of L. That is why force times time and force times distance end up in different places.")

If you guessed "different units, so different things", remember that named units like the newton are shorthand. Always unpack them into base quantities before comparing.

## The physics

The **dimensions** of a quantity are the powers of the base quantities in it; for mechanics, mass [M], length [L] and time [T]. Its **dimensional formula** is found by writing its defining equation and replacing every quantity by its dimensions. Pure numbers and angles are dimensionless.

When you multiply quantities, add the powers of each base quantity; when you divide, subtract them. For example, power $=$ work $\div$ time:

$$[\text{M}\,\text{L}^2\,\text{T}^{-2}] \div [\text{T}] = [\text{M}\,\text{L}^2\,\text{T}^{-3}]$$

Quantities with different dimensions can never be equal or added. Quantities with the same dimensions *can* be compared, though having the same dimensions does not by itself prove they are the same physical quantity.

## Key takeaway

Unpack every quantity into M, L and T to see what it is made of. Force × time and mass × velocity are both $[\text{M}\,\text{L}\,\text{T}^{-1}]$, so $\text{N}\,\text{s}$ and $\text{kg}\,\text{m/s}$ are the same unit; force × distance is $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$, a different kind of quantity.
