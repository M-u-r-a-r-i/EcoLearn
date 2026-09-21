---
concept_id: si_units
interest: cricket
format: challenge
title: What a watt on the bowling machine is made of
check:
  question: |-
    A groundsman's roller presses on the pitch, and pressure is defined as force per unit area, measured in pascals. Written in SI base units, one pascal is:
  options:
    A: |-
      $1\,\text{kg}\,\text{m}\,\text{s}^{-2}$
    B: |-
      $1\,\text{kg}\,\text{m}^3\,\text{s}^{-2}$
    C: |-
      The pascal is itself a base unit, so it cannot be written in others
    D: |-
      $1\,\text{kg}\,\text{m}^{-1}\,\text{s}^{-2}$
  answer: D
  explanation: |-
    $1\,\text{Pa} = 1\,\text{N}/\text{m}^2 = (\text{kg}\,\text{m}\,\text{s}^{-2})/\text{m}^2 = \text{kg}\,\text{m}^{-1}\,\text{s}^{-2}$. One metre from the newton cancels one of the two in the area.
  misconceptions:
    A: |-
      Leaves out the area altogether — that is the newton, the unit of force, not of force per unit area.
    B: |-
      Multiplies the newton by the area instead of dividing by it, so the metres add instead of cancelling.
    C: |-
      Thinks any unit with its own name is a base unit. Only seven units are base units; the pascal, like the newton and joule, is derived.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![Groundstaff measure the pitch while a ball sits on a scale and a speed display shows 142 km/h](scenes/cricket/units_measurement.svg "The ground is full of units: metres on the tape, grams on the scale, km/h on the display.")

It's a slow Sunday at the club nets, and Farah is feeding balls into the bowling machine for her friend Kunal. Between overs, she crouches to read the metal plate on its motor. Among the small print: a power rating in watts — say $750\,\text{W}$.

"A watt is electrical," Kunal says, leaning on his bat. "It's for bulbs and motors. It's not made of anything. It's just a watt."

Farah grins. She's just finished the chapter on units. "I bet you a cold drink that I can write a watt using only kilograms, metres and seconds. Nothing else."

Kunal shakes her hand. He's sure a unit of power has nothing to do with mass or length. Who's buying the drink?

## The challenge

Starting only from definitions you already know —

- force $=$ mass $\times$ acceleration,
- work $=$ force $\times$ distance,
- power $=$ work done $\div$ time taken,

write $1\,\text{W}$ in terms of SI base units. How many different base units do you need?

## Think first

Is Kunal right that a watt is its own thing — a base unit like the metre? If not, which base units appear, and with what powers? Is it $\text{kg}\,\text{m}\,\text{s}^{-2}$? $\text{kg}\,\text{m}^2\,\text{s}^{-2}$? Something else? Build it one step at a time before you look.

## The reveal

Build up from force, one definition at a time.

**Force.** Acceleration is change of velocity per second, so its unit is $(\text{m/s})/\text{s} = \text{m}\,\text{s}^{-2}$. Then

$$1\,\text{N} = 1\,\text{kg} \times 1\,\text{m}\,\text{s}^{-2} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$$

**Work.** Force times distance adds one more metre:

$$1\,\text{J} = 1\,\text{N} \times 1\,\text{m} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$$

**Power.** Work per second divides by one more second:

$$1\,\text{W} = \frac{1\,\text{J}}{1\,\text{s}} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$$

Farah wins: three base units — kilogram, metre and second — and nothing else.

![The newton, joule and watt shown as coloured blocks of kilogram, metre and second](figures/si_units/derived-units-from-base.svg "Each step adds one factor: a metre to go from newton to joule, one more inverse second to go from joule to watt.")

If you guessed $\text{kg}\,\text{m}^2\,\text{s}^{-2}$, you built the joule and forgot the last step, dividing by time. If you guessed $\text{kg}\,\text{m}\,\text{s}^{-2}$, you stopped at the newton. And Kunal's idea fails because only seven units are base units; the watt isn't one of them. It's true that motors and bulbs are rated in watts — but power means energy per second whatever the source, whether a bowler's arm, a motor or a bulb.

## The physics

The SI has seven **base units**: metre (m), kilogram (kg), second (s), ampere (A), kelvin (K), mole (mol) and candela (cd). Since 20 May 2019, each is defined by fixing the exact value of a constant of nature.

![A table of the seven SI base units with the constant that defines each](figures/si_units/seven-base-units.svg "The seven base units. The watt, newton, joule and pascal are not on this list: they are derived.")

Every other unit is a **derived unit**. To find it, write the defining equation of the quantity and replace each quantity by its unit. Some derived units get their own names (newton, joule, watt, pascal), but a name is only shorthand. For mechanics, the metre, kilogram and second are always enough.

(Electrical quantities bring in the ampere: a watt is also a volt times an ampere. You'll see in the electricity chapters that both routes give the same $\text{kg}\,\text{m}^2\,\text{s}^{-3}$.)

## Key takeaway

Derived units are products of base units, found from the equation that defines the quantity. Step by step: $1\,\text{N} = 1\,\text{kg}\,\text{m}\,\text{s}^{-2}$, $1\,\text{J} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-2}$, $1\,\text{W} = 1\,\text{kg}\,\text{m}^2\,\text{s}^{-3}$. A special name does not make a unit a base unit.
