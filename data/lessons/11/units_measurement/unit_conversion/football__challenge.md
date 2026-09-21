---
concept_id: unit_conversion
interest: football
format: challenge
title: Reading a ball pump in an old textbook's units
check:
  question: |-
    In the CGS system the unit of force is the dyne, $1\,\text{g}\,\text{cm}\,\text{s}^{-2}$. Using the dimensional formula of force, $[\text{M}\,\text{L}\,\text{T}^{-2}]$, how many dynes make one newton?
  options:
    A: |-
      $10^3$
    B: |-
      $10^7$
    C: |-
      $10^2$
    D: |-
      $10^5$
  answer: D
  explanation: |-
    $n_2 = 1 \times (1\,\text{kg}/1\,\text{g})^1 (1\,\text{m}/1\,\text{cm})^1 (1\,\text{s}/1\,\text{s})^{-2} = 10^3 \times 10^2 \times 1 = 10^5$. So $1\,\text{N} = 10^5\,\text{dyn}$.
  misconceptions:
    A: |-
      Converts the mass (kilograms to grams) but forgets the length, which also appears in force.
    B: |-
      Squares the length ratio, as for energy ($[\text{M}\,\text{L}^2\,\text{T}^{-2}]$); $10^7$ is the number of ergs in a joule, not dynes in a newton.
    C: |-
      Converts the length (metres to centimetres) but forgets the mass.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A match ball sits on a scale beside a pressure gauge reading 0.9 atm](scenes/football/units_measurement.svg "The gauge reads in atmospheres; the pump's manual in kilopascals. An old textbook would use neither.")

Neha and Arnav are pumping balls for their school team. The gauge shows the pressure of the air inside the ball *above* the air outside: $0.9\,\text{atm}$, which the pump's manual says is about $91\,\text{kPa}$.

Arnav has his grandfather's old physics book in his bag, written in CGS units. In it, atmospheric pressure is given as "about $10^6$ dynes per square centimetre". He wants to compare the ball with the book.

"Easy," he says. "One newton is $10^5$ dynes. So a pascal, a newton per square metre, is $10^5$ dynes per square centimetre."

"You forgot the area," says Neha. "A square metre is $10^4$ square centimetres. So multiply by another $10^4$: a pascal is $10^9$ dynes per square centimetre."

Two confident answers, ten thousand times apart. Can either be right — and how do you convert a pressure between two unit systems without guessing?

## The challenge

Pressure has the dimensional formula $[\text{M}\,\text{L}^{-1}\,\text{T}^{-2}]$. The CGS unit of pressure is the $\text{dyn/cm}^2$, built from the gram, centimetre and second.

1. How many $\text{dyn/cm}^2$ make $1\,\text{Pa}$?
2. What is the ball's $91\,\text{kPa}$ in $\text{dyn/cm}^2$?
3. Does the old book's "$10^6\,\text{dyn/cm}^2$" for the atmosphere ($1\,\text{atm} = 101\,325\,\text{Pa}$) agree?

## Think first

Arnav says $10^5$; Neha says $10^9$. Or is the truth somewhere else entirely? Should the number get bigger or smaller when you switch to CGS? And the length ratio — which way round, and to what power, does it enter? Guess before you work.

## The reveal

Use $n_2 = n_1 (M_1/M_2)^a (L_1/L_2)^b (T_1/T_2)^c$ with $a = 1$, $b = -1$, $c = -2$. System 1 is SI, system 2 is CGS:

$$\frac{M_1}{M_2} = \frac{1\,\text{kg}}{1\,\text{g}} = 10^3 \qquad \frac{L_1}{L_2} = \frac{1\,\text{m}}{1\,\text{cm}} = 10^2 \qquad \frac{T_1}{T_2} = 1$$

**Part 1:**

$$n_2 = 1 \times (10^3)^1 \times (10^2)^{-1} \times (1)^{-2} = 10^3 \times 10^{-2} = 10$$

So $1\,\text{Pa} = 10\,\text{dyn/cm}^2$. Only ten!

**Check by unpacking the units:** $1\,\text{N} = 10^5\,\text{dyn}$ and $1\,\text{m}^2 = 10^4\,\text{cm}^2$, so

$$1\,\text{Pa} = \frac{10^5\,\text{dyn}}{10^4\,\text{cm}^2} = 10\,\text{dyn/cm}^2$$

Arnav converted the force and forgot the area. Neha remembered the area but multiplied by it instead of dividing: the area is in the **denominator**, so it divides. The $\text{L}^{-1}$ in the dimensional formula takes care of both.

![A one-metre square divided into a ten by ten grid and a one-metre cube, showing that a square metre is ten thousand square centimetres](figures/unit_conversion/area-volume-conversion.svg "One square metre holds 10⁴ square centimetres. Spread the same force over that many more units of area and the pressure number shrinks by 10⁴.")

**Part 2:** $91\,\text{kPa} = 9.1 \times 10^4\,\text{Pa} = 9.1 \times 10^5\,\text{dyn/cm}^2$.

**Part 3:** $1\,\text{atm} = 101\,325\,\text{Pa} \approx 1.01 \times 10^6\,\text{dyn/cm}^2$. The old book's "about $10^6$" is right — and it shows at a glance that the ball's extra pressure is a little less than one atmosphere, just as the gauge says.

## The physics

A quantity is $Q = n_1 u_1 = n_2 u_2$. If its dimensional formula is $[\text{M}^a\,\text{L}^b\,\text{T}^c]$, then

$$n_2 = n_1 \left[\frac{M_1}{M_2}\right]^a \left[\frac{L_1}{L_2}\right]^b \left[\frac{T_1}{T_2}\right]^c$$

This works between any two systems — SI, CGS, or one you invent — once you know the sizes of their base units. Negative powers matter as much as positive ones: a length in the denominator, as in pressure or density, divides by its ratio. The two classic errors are forgetting a base quantity and using a ratio with the wrong power or upside down.

## Key takeaway

Let the dimensional formula set every power: pressure is $[\text{M}\,\text{L}^{-1}\,\text{T}^{-2}]$, so $1\,\text{Pa} = 10^3 \times 10^{-2} = 10\,\text{dyn/cm}^2$, and force is $[\text{M}\,\text{L}\,\text{T}^{-2}]$, so $1\,\text{N} = 10^5\,\text{dyn}$. Always check by unpacking the units directly.
