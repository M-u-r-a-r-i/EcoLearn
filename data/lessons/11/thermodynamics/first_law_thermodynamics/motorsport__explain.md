---
concept_id: first_law_thermodynamics
interest: motorsport
format: explain
title: Where the fuel's energy goes inside an engine cylinder
check:
  question: |-
    A workshop compressor fills the air bottle for a pit crew's wheel gun. During one stroke, $150\,\text{J}$ of work is done on the air, and the air gives out $50\,\text{J}$ of heat to the cylinder walls. Using $\Delta Q = \Delta U + \Delta W$, what is the change in the air's internal energy?
  options:
    A: |-
      $+200\,\text{J}$
    B: |-
      $+100\,\text{J}$
    C: |-
      $-200\,\text{J}$
    D: |-
      $-100\,\text{J}$
  answer: B
  explanation: |-
    Heat given out: $\Delta Q = -50\,\text{J}$. Work done on the air: $\Delta W = -150\,\text{J}$. So $\Delta U = \Delta Q - \Delta W = -50 - (-150) = +100\,\text{J}$; the air warms up.
  misconceptions:
    A: |-
      Treats every energy amount as a gain and adds the magnitudes, ignoring that the $50\,\text{J}$ of heat left the air.
    C: |-
      Gets both signs right but adds them, using $\Delta U = \Delta Q + \Delta W$. In NCERT's form, $\Delta W$ is work done by the gas and is subtracted.
    D: |-
      Reverses the sign convention, counting heat given out as positive and work done on the gas as positive work by the gas, so the answer comes out with the wrong sign.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A pit lane in the afternoon sun: a stack of tyres in electric tyre blankets with a probe thermometer, a race car with a glowing front brake disc and a hot exhaust, and a compressed-air bottle feeding a wheel gun](scenes/motorsport/thermodynamics.svg "Hot exhaust shimmering behind the car: energy from the fuel that never reached the wheels.")

The engine has just finished ten minutes flat out on the test bed, and the workshop is ringing in the sudden quiet. Tejas, an apprentice, walks round to the back and stops. The exhaust pipe is glowing a dull orange, and the air above it wobbles like a mirage.

"That's a lot of wasted fuel," he says.

His supervisor, Harpreet, hands him a notebook. "Is it? Think about one cylinder. Fuel burns, the gas gets a big dose of energy. Some of that energy shoves the piston down; that's what turns the wheels. Is that the whole story?"

Tejas looks back at the glowing pipe. The gas leaving the engine is still scorching. So it kept some of the energy for itself, even after doing its pushing.

"Then the energy gets shared," he says slowly. "Some pushes the piston. Some stays in the gas. But in what proportion? Is there a rule?"

## The physics

The **first law of thermodynamics** is energy conservation applied to heat, work and internal energy. For a system such as the gas in a cylinder, in NCERT's form:

$$\Delta Q = \Delta U + \Delta W$$

- $\Delta Q$ is the **heat supplied to** the system: positive when heat flows in, negative when heat flows out.
- $\Delta U$ is the **change in internal energy** of the system: positive if it increases.
- $\Delta W$ is the **work done by** the system on its surroundings: positive when the gas expands and pushes, negative when the gas is compressed (work is done on it).

![A cylinder of gas: heat supplied to the gas is Delta Q greater than zero; work done by the gas as it expands is Delta W greater than zero; Delta Q equals Delta U plus Delta W](figures/first_law_thermodynamics/sign-convention.svg "Heat in and work out are positive. Reverse either direction and flip its sign.")

In words: the heat supplied is shared between raising the internal energy and doing work. Rearranged, $\Delta U = \Delta Q - \Delta W$.

Two facts make the law powerful. First, $\Delta U$ depends only on the start and end states: $\Delta Q$ and $\Delta W$ each depend on the path, but their difference does not. Second, for an ideal gas, $U$ depends only on temperature, so the sign of $\Delta U$ tells you whether the gas warmed or cooled.

Some books write the law as $\Delta U = Q + W$ with $W$ the work done **on** the gas. It is the same physics with the opposite sign for work. Pick one convention and keep it; mixing the two is the most common way to get these problems wrong.

In Tejas's cylinder: burning fuel supplies heat to the gas ($\Delta Q > 0$), the gas expands and pushes the piston ($\Delta W > 0$), and what's left raises the gas's internal energy ($\Delta U > 0$). That leftover is the heat in the glowing exhaust.

## Worked example

**Given (illustrative):** in one cylinder, (a) the burning fuel supplies $1000\,\text{J}$ of heat to the gas, which then pushes the piston down, doing $400\,\text{J}$ of work. (b) On the compression stroke, the piston does $300\,\text{J}$ of work on the fresh gas, which loses $100\,\text{J}$ of heat to the cylinder walls.
**Find:** $\Delta U$ for each stage.

**(a) Burning and pushing.** $\Delta Q = +1000\,\text{J}$ (heat in), $\Delta W = +400\,\text{J}$ (work by the gas).

$$\Delta U = \Delta Q - \Delta W = 1000 - 400 = +600\,\text{J}$$

More than half the energy stays in the gas. That is Tejas's scorching exhaust.

**(b) Squeezing.** $\Delta Q = -100\,\text{J}$ (heat out), $\Delta W = -300\,\text{J}$ (work done on the gas).

$$\Delta U = -100 - (-300) = +200\,\text{J}$$

The gas warms up even though it is losing heat, because the piston pours in more energy than leaks out.

**Sanity check:** in (b) the gas receives $300\,\text{J}$ as work and gives out $100\,\text{J}$ as heat, a net gain of $200\,\text{J}$, which matches.

## Where the picture breaks

A real engine is not a fixed amount of gas being heated. Fuel and air flow in, burn inside the cylinder (a chemical change, not heat from outside) and flow out as exhaust. Treating the burning as "heat supplied" to a closed gas is an idealisation engineers use to do the energy accounting; the simple first law above needs a fixed amount of gas. The gas also never has one single temperature in a real, fast stroke. And the $1000\,\text{J}$ and $400\,\text{J}$ are round illustrative numbers, not any real engine's figures. The law itself, energy in equals energy stored plus energy out as work, holds regardless.

## Key takeaway

The first law is energy conservation: $\Delta Q = \Delta U + \Delta W$. Heat supplied to a gas is shared between raising its internal energy and the work it does. Heat in and work done by the gas are positive; heat out and work done on the gas are negative. Get the signs right first, then the arithmetic is easy.
