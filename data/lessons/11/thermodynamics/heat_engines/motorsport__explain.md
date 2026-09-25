---
concept_id: heat_engines
interest: motorsport
format: explain
title: The radiator fan that roars at the toll plaza
check:
  question: |-
    In each cycle, a car engine's working gas absorbs $500\,\text{kJ}$ of heat from burning fuel and rejects $400\,\text{kJ}$ of heat through the radiator and exhaust. What is its efficiency?
  options:
    A: |-
      $20\%$
    B: |-
      $80\%$
    C: |-
      $25\%$
    D: |-
      $100\%$, because energy is conserved
  answer: A
  explanation: |-
    Work per cycle $W = Q_1 - Q_2 = 500 - 400 = 100\,\text{kJ}$, so $\eta = W/Q_1 = 100/500 = 0.20 = 20\%$.
  misconceptions:
    B: |-
      Computes $Q_2/Q_1$, the fraction of heat rejected, instead of the fraction turned into work. Efficiency is $1 - Q_2/Q_1$.
    C: |-
      Divides the work by the heat rejected ($100/400$) instead of by the heat absorbed; efficiency compares the output to the energy put in, $Q_1$.
    D: |-
      Mixes up energy conservation with efficiency. All the energy is accounted for, but the $400\,\text{kJ}$ rejected as heat is not useful work.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A pit lane in the afternoon sun: a stack of tyres in electric tyre blankets with a probe thermometer, a race car with a glowing front brake disc and a hot exhaust, and a compressed-air bottle feeding a wheel gun](scenes/motorsport/thermodynamics.svg "The hot exhaust in the middle of the scene: every car engine, racing or road, has to throw heat away.")

Pranav and his mother, Sunita, are driving home from a karting weekend, stuck in a long queue at a highway toll plaza on a hot May afternoon. The car is barely moving, yet from under the bonnet comes a steady roar. The radiator fan has switched on.

"Why does it need a fan when we're not even moving?" Pranav asks.

"Because the engine is still making heat," says Sunita, who designs cooling systems for a living. "Lots of it. If the fan couldn't get rid of it, the engine would cook itself."

Pranav does a rough sum in his head. They paid for a full tank of fuel. The car only needs a fraction of that energy to push them along the highway. The rest goes out of the radiator and the exhaust pipe as heat.

"Then the engine is badly designed," he says. "A better one would turn all of the fuel's heat into motion."

Sunita smiles. "People have been trying for two hundred years. Is it just bad engineering, or is it built into what an engine is?"

## The physics

A **heat engine** is a device that takes in heat and turns part of it into work, over and over, by running a **working substance** (a gas, say) through a **cycle** that returns it to its starting state. Every heat engine has three parts:

- a **hot reservoir** at temperature $T_1$, from which it absorbs heat $Q_1$ (in a car, the burning fuel);
- the **working substance**, which does work $W$ on the surroundings (the gas pushing the pistons);
- a **cold reservoir** at a lower temperature $T_2$, to which it rejects heat $Q_2$ (the outside air, reached through the radiator and exhaust).

![A hot reservoir above an engine and a cold reservoir below: heat Q1 flows in, work W comes out to the side, heat Q2 flows down to the cold reservoir](figures/heat_engines/engine-energy-flow.svg "Heat in splits into useful work and rejected heat; the arrow widths are drawn to scale for Q1 = 50, W = 15, Q2 = 35. The rejected share is never zero.")

Because the working substance ends each cycle in its starting state, $\Delta U = 0$ for the whole cycle, and the first law gives

$$W = Q_1 - Q_2$$

The **efficiency** $\eta$ is the fraction of the heat absorbed that comes out as work:

$$\eta = \frac{W}{Q_1} = 1 - \frac{Q_2}{Q_1}$$

$\eta$ could equal 1 (100%) only if $Q_2 = 0$, with no heat rejected at all. No engine has ever managed that, and the second law of thermodynamics, coming next, shows why it is impossible, not just difficult.

On a $p$–$V$ diagram, a cycle is a closed loop. Run clockwise, the gas does more work while expanding at high pressure than is done on it while being compressed at low pressure, and the net work per cycle is the **area enclosed** by the loop.

![A rectangular cycle on a p-V diagram, A to B to C to D: expansion at 2 x 10^5 Pa, compression at 1 x 10^5 Pa; enclosed area 200 J](figures/heat_engines/cycle-net-work.svg "The gas does 400 J expanding and has 200 J done on it while compressed; the net 200 J is the enclosed area.")

## Worked example

**Given (illustrative):** at a steady highway speed, the engine's gas absorbs $Q_1 = 200\,\text{kJ}$ of heat from the fuel every second and rejects $Q_2 = 150\,\text{kJ}$ every second through the radiator and exhaust.
**Find:** the work output each second, the efficiency, and the power.

**Step 1: the work.**

$$W = Q_1 - Q_2 = 200 - 150 = 50\,\text{kJ per second}$$

**Step 2: the efficiency.**

$$\eta = \frac{W}{Q_1} = \frac{50}{200} = 0.25 = 25\%$$

So only one quarter of the fuel's heat moves the car; three quarters warms the air around it. That is the heat Pranav's radiator fan was fighting.

**Step 3: the power.** Doing $50\,\text{kJ}$ of work every second is a power of $50\,\text{kW}$, a sensible figure for an ordinary family car's engine.

**Sanity check:** the other formula gives $1 - 150/200 = 1 - 0.75 = 0.25$, the same answer.

## Where the picture breaks

A car engine is an internal combustion engine: the fuel burns inside the cylinder, and fresh air is drawn in on every cycle and pushed out as exhaust. It does not literally shuttle one fixed gas between two reservoirs. The reservoir model is an idealisation that gets the energy accounting right. A real engine also loses energy to friction and to incomplete burning, which better engineering can reduce. Rejecting heat to a colder place is different: every heat engine must do it, however well it is built. And the numbers above are illustrative, not the data of any real car.

## Key takeaway

A heat engine runs a working substance through a cycle, absorbing heat $Q_1$ from a hot reservoir, doing work $W$, and rejecting heat $Q_2$ to a cold one. Over a cycle $W = Q_1 - Q_2$, and the efficiency is $\eta = W/Q_1 = 1 - Q_2/Q_1$. Because $Q_2$ is never zero, $\eta$ is always less than 1.
