---
concept_id: heat_engines
interest: cricket
format: explain
title: The generator that kept the floodlights on
check:
  question: |-
    In each cycle, the engine of a ground's standby generator absorbs $40\,\text{kJ}$ of heat from burning fuel and rejects $30\,\text{kJ}$ of heat to the surroundings. What is its efficiency?
  options:
    A: |-
      $75\%$
    B: |-
      $33\%$
    C: |-
      $100\%$, because energy is conserved
    D: |-
      $25\%$
  answer: D
  explanation: |-
    Work per cycle $W = Q_1 - Q_2 = 40 - 30 = 10\,\text{kJ}$, so $\eta = W/Q_1 = 10/40 = 0.25 = 25\%$.
  misconceptions:
    A: |-
      Computes $Q_2/Q_1$, the fraction of heat wasted, instead of the fraction turned into work. Efficiency is $1 - Q_2/Q_1$.
    B: |-
      Divides the work by the heat rejected ($10/30$) instead of by the heat absorbed; efficiency compares output to the energy put in, $Q_1$.
    C: |-
      Mixes up energy conservation with efficiency. All the energy is accounted for, but the $30\,\text{kJ}$ rejected as heat is not useful work.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A hot afternoon at a cricket ground: blazing sun, a board showing 38 degrees, a bowler polishing the ball, a generator with hot exhaust and an ice box of drinks](scenes/cricket/thermodynamics.svg "On the right, by the boundary: the standby generator, and the hot exhaust it can't avoid.")

A club final under lights, and with two overs to go the whole neighbourhood loses power. The floodlights die, the crowd groans, and then, from behind the sightscreen, comes a rattle and a roar. The club's diesel generator has kicked in. Within a minute the lights are back.

Sameer, the club's scorer, goes to check on it after the match. The generator is ticking as it cools, far too hot to touch, and the air blasting from its exhaust and radiator is scorching. He does a rough sum in his head: all the fuel it burned, all that heat, and the lights needed only a fraction of it.

"Why does it throw so much heat away?" he asks the electrician, Pradeep. "Couldn't a better machine turn all of the fuel's heat into electricity?"

Pradeep shrugs. "Every engine I've ever worked on gets hot. I've never seen one that doesn't."

Is that just bad engineering, or is it built into what an engine is?

## The physics

A **heat engine** is a device that takes in heat and turns part of it into work, over and over, by running a **working substance** (a gas, say) through a **cycle** that returns it to its starting state. Every heat engine has three parts:

- a **hot reservoir** at temperature $T_1$, from which it absorbs heat $Q_1$ (in the generator, the burning fuel);
- the **working substance**, which does work $W$ on the surroundings;
- a **cold reservoir** at a lower temperature $T_2$, to which it rejects heat $Q_2$ (the surrounding air, via the exhaust and radiator).

![A hot reservoir above an engine and a cold reservoir below: heat Q1 flows in, work W comes out to the side, heat Q2 flows down to the cold reservoir](figures/heat_engines/engine-energy-flow.svg "Heat in splits into useful work and rejected heat; the arrow widths are drawn to scale for Q1 = 50, W = 15, Q2 = 35.")

Because the working substance ends each cycle in its starting state, $\Delta U = 0$ for a whole cycle, and the first law gives

$$W = Q_1 - Q_2$$

The **efficiency** $\eta$ is the fraction of the heat absorbed that comes out as work:

$$\eta = \frac{W}{Q_1} = 1 - \frac{Q_2}{Q_1}$$

$\eta$ could equal 1 (100%) only if $Q_2 = 0$, with no heat rejected. No engine ever achieves that; the second law of thermodynamics, coming next, explains why it is impossible, not just difficult.

On a $p$–$V$ diagram, the cycle is a closed loop. Run clockwise, the gas does more work expanding at high pressure than is done on it while being compressed at low pressure, and the net work per cycle is the **area enclosed** by the loop.

![A rectangular cycle on a p-V diagram, A to B to C to D: expansion at 2 x 10^5 Pa, compression at 1 x 10^5 Pa; enclosed area 200 J](figures/heat_engines/cycle-net-work.svg "The gas does 400 J expanding and has 200 J done on it while compressed; the net 200 J is the enclosed area.")

If this gas absorbs, say, $1000\,\text{J}$ of heat per cycle, its efficiency is $200/1000 = 20\%$, and it rejects $800\,\text{J}$.

## Worked example

**Given (illustrative):** each second, the generator's engine absorbs $Q_1 = 50\,\text{kJ}$ from burning fuel and rejects $Q_2 = 35\,\text{kJ}$ through its exhaust and radiator.
**Find:** the work output per second, the efficiency, and the power.

$$W = Q_1 - Q_2 = 50 - 35 = 15\,\text{kJ per second}$$

$$\eta = \frac{W}{Q_1} = \frac{15}{50} = 0.30 = 30\%$$

Work of $15\,\text{kJ}$ every second is a mechanical power of $15\,\text{kW}$, which the generator then converts to electricity (with some further loss).

**Sanity check:** $1 - Q_2/Q_1 = 1 - 35/50 = 1 - 0.70 = 0.30$, the same answer by the other formula.

## Where the picture breaks

A diesel generator is an internal combustion engine: the fuel burns inside the cylinder and fresh air is drawn in each cycle, so it does not literally shuttle one fixed gas between two reservoirs. The reservoir model is an idealisation that captures the energy accounting. Its losses also include friction and incomplete burning, which are engineering problems. Rejecting heat to a colder place is different: every heat engine must do it, however well it is built.

## Key takeaway

A heat engine runs a working substance through a cycle, absorbing heat $Q_1$ from a hot reservoir, doing work $W$ and rejecting heat $Q_2$ to a cold one. Over a cycle, $W = Q_1 - Q_2$, and the efficiency is $\eta = W/Q_1 = 1 - Q_2/Q_1$. Since $Q_2$ is never zero, $\eta$ is always less than 1.
