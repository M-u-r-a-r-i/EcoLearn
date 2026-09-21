---
concept_id: dimensional_formulae
interest: football
format: challenge
title: Is the pressure in a ball an energy in disguise
check:
  question: |-
    A ball's gauge shows the pressure of the air inside, defined as force per unit area. What is the dimensional formula of pressure?
  options:
    A: |-
      $[\text{M}\,\text{L}\,\text{T}^{-2}]$
    B: |-
      $[\text{M}\,\text{L}^{-1}\,\text{T}^{-2}]$
    C: |-
      $[\text{M}\,\text{L}^3\,\text{T}^{-2}]$
    D: |-
      $[\text{M}\,\text{L}^{-2}\,\text{T}^{-2}]$
  answer: B
  explanation: |-
    Force is $[\text{M}\,\text{L}\,\text{T}^{-2}]$ and area is $[\text{L}^2]$. Dividing subtracts the powers of L: $1 - 2 = -1$, so pressure is $[\text{M}\,\text{L}^{-1}\,\text{T}^{-2}]$.
  misconceptions:
    A: |-
      Leaves out the area. $[\text{M}\,\text{L}\,\text{T}^{-2}]$ is force itself, not force per unit area.
    C: |-
      Multiplies by the area instead of dividing, so the powers of L add ($1 + 2$) instead of subtracting.
    D: |-
      Divides by the area but forgets that force already contains one L, so writes $\text{L}^{-2}$ instead of $\text{L}^{1-2} = \text{L}^{-1}$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A match ball sits on a scale beside a pressure gauge reading 0.9 atm](scenes/football/units_measurement.svg "The gauge measures the push of the air inside the ball. What kind of quantity is that push, really?")

Pranjal and Rukhsar are pumping up balls for Sunday's tournament. The gauge reads in atmospheres; the pump's little manual also gives pressures in pascals, $\text{N/m}^2$.

Rukhsar, flipping through her father's old physics book, finds a line she reads aloud: *"Pressure may also be understood as energy per unit volume."*

"That's nonsense," says Pranjal, squeezing the ball. "Pressure is a push on the skin — newtons per square metre. Energy per volume would be joules per cubic metre. Different units, different things. Your book has a misprint."

Rukhsar isn't sure. A joule is a newton times a metre, isn't it? And a cubic metre is a square metre times a metre? She can feel something cancelling, but she can't quite see it.

Can you settle it, using nothing but M, L and T?

## The challenge

Find the dimensional formula of:

1. pressure, defined as force $\div$ area;
2. energy per unit volume, defined as energy $\div$ volume.

Are they the same? Then, for contrast, find the dimensions of force $\div$ **length** (newtons per metre). Is that the same as the other two?

## Think first

Pranjal says the units look too different to be related. Rukhsar suspects they are secretly the same. What do you expect — two different dimensional formulas, or one? And if you divide force by a length instead of an area, should the result change? Write your guesses down.

## The reveal

Start from force, which both need: force $=$ mass $\times$ acceleration, so $[F] = [\text{M}\,\text{L}\,\text{T}^{-2}]$.

**Pressure** $=$ force $\div$ area, with area $[\text{L}^2]$:

$$\left[\frac{F}{A}\right] = \frac{[\text{M}\,\text{L}\,\text{T}^{-2}]}{[\text{L}^2]} = [\text{M}\,\text{L}^{-1}\,\text{T}^{-2}]$$

**Energy per unit volume.** Energy is force $\times$ distance, $[\text{M}\,\text{L}^2\,\text{T}^{-2}]$; volume is $[\text{L}^3]$:

$$\left[\frac{E}{V}\right] = \frac{[\text{M}\,\text{L}^2\,\text{T}^{-2}]}{[\text{L}^3]} = [\text{M}\,\text{L}^{-1}\,\text{T}^{-2}]$$

Identical. Rukhsar's book is right, dimensionally: $1\,\text{J/m}^3 = 1\,\text{N}\,\text{m}/\text{m}^3 = 1\,\text{N/m}^2 = 1\,\text{Pa}$. The extra metre in the joule cancels the extra metre in the cubic metre. And there's real physics behind it: to push a volume $V$ of air into the ball against a pressure $p$ takes work of the order of $pV$ — you'll meet this properly in the chapters on gases and heat.

**Force per length**, for contrast:

$$\left[\frac{F}{L}\right] = \frac{[\text{M}\,\text{L}\,\text{T}^{-2}]}{[\text{L}]} = [\text{M}\,\text{T}^{-2}]$$

Different — there's no length left at all. Dividing the same force by a length or by an area gives quantities of different kinds.

![A ladder: velocity, acceleration, force, work and power, each with its dimensional formula](figures/dimensional_formulae/dimension-building-blocks.svg "Multiplying by L raises the power of L; dividing lowers it. Energy has one more L than force, and volume one more L than area, so the two ratios match.")

If you guessed "different units, so different things", remember that named units like the joule and the pascal are shorthand. Unpack them into base quantities before comparing.

## The physics

The **dimensions** of a quantity are the powers of the base quantities in it; in mechanics, mass [M], length [L] and time [T]. Its **dimensional formula** comes from its defining equation, replacing every quantity by its dimensions. Pure numbers and angles are dimensionless.

When quantities are multiplied, add the powers of each base quantity; when divided, subtract them. That is all the algebra you need.

Quantities with different dimensions can never be equal or be added. Quantities with the same dimensions *can* be compared — but sharing a dimensional formula doesn't by itself prove two quantities are the same physical thing. Here the link between pressure and energy density is real; for work and torque, which also share a formula, it isn't.

## Key takeaway

Unpack every quantity into M, L and T to see what it's made of. Pressure ($\text{N/m}^2$) and energy per unit volume ($\text{J/m}^3$) are both $[\text{M}\,\text{L}^{-1}\,\text{T}^{-2}]$; force per length is $[\text{M}\,\text{T}^{-2}]$, a different kind of quantity.
