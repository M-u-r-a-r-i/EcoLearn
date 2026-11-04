---
concept_id: heat_engines
interest: football
format: explain
title: The mower that burns fuel to cut the stripes
check:
  question: |-
    In each cycle, the engine of a pitch mower absorbs $30\,\text{kJ}$ of heat from burning fuel and rejects $24\,\text{kJ}$ of heat to the surrounding air. What is its efficiency?
  options:
    A: |-
      $80\%$
    B: |-
      $20\%$
    C: |-
      $25\%$
    D: |-
      $100\%$, because energy is conserved
  answer: B
  explanation: |-
    Work per cycle $W = Q_1 - Q_2 = 30 - 24 = 6\,\text{kJ}$, so $\eta = W/Q_1 = 6/30 = 0.20 = 20\%$.
  misconceptions:
    A: |-
      Computes $Q_2/Q_1$, the fraction of heat thrown away, instead of the fraction turned into work. Efficiency is $1 - Q_2/Q_1$, which is what is left over.
    C: |-
      Divides the work by the heat rejected ($6/24$) instead of by the heat absorbed. Efficiency compares what you get out with what you paid for, and you paid for $Q_1$.
    D: |-
      Mixes up energy conservation with efficiency. Every joule is accounted for, but the $24\,\text{kJ}$ leaving as heat is not useful work.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground on a hot day: a board reading 36 degrees Celsius, an ice box of drinks, a player inflating a ball with a hand pump, and a mower with a hot exhaust](scenes/football/thermodynamics.svg "On the right: the mower that cuts the stripes, and the hot exhaust it cannot avoid.")

Devika has chosen the wrong week for her school energy project, because the only machine on the ground that burns fuel is the mower, and the groundsman, Prakash, mows at six in the morning.

So she is out there at six, clipboard in hand, walking two steps behind him while he lays the stripes down the pitch. By the time he finishes the second half, she can feel the heat off the engine from a metre away, and the air behind the exhaust is blurry.

"Feel the fins," Prakash says, and she nearly does before she thinks better of it.

Her project is meant to be about where the fuel's energy goes. She can see some of it: the blades spinning, the grass flying. But she can *feel* an enormous amount of it going into the air for nothing at all.

"Couldn't someone build a mower that puts all of the fuel's heat into cutting?" she asks. "Instead of cooking the person pushing it?"

Prakash has worked with engines all his life. "Every one I've ever met gets hot," he says. "Never seen one that doesn't."

Is that bad engineering, or is it what an engine *is*?

## The physics

A **heat engine** takes in heat and turns part of it into work, repeatedly, by running a **working substance** — a gas, usually — around a **cycle** that brings it back to its starting state. Every heat engine has three parts:

- a **hot reservoir** at temperature $T_1$, from which it absorbs heat $Q_1$ (here, the burning petrol);
- the **working substance**, which does work $W$ on the surroundings (the gases in the cylinder, driving the piston and so the blades);
- a **cold reservoir** at a lower temperature $T_2$, into which it rejects heat $Q_2$ (the morning air, through the exhaust and the cooling fins).

![A hot reservoir above an engine and a cold reservoir below: heat Q1 flows in, work W comes out to the side, heat Q2 flows down to the cold reservoir](figures/heat_engines/engine-energy-flow.svg "Heat in splits into useful work and rejected heat; the arrow widths are drawn to scale for Q1 = 50, W = 15, Q2 = 35.")

Because the working substance ends each cycle exactly where it began, $\Delta U = 0$ over a cycle, and the first law reduces to

$$W = Q_1 - Q_2$$

The **efficiency** $\eta$ is the fraction of the absorbed heat that leaves as work:

$$\eta = \frac{W}{Q_1} = 1 - \frac{Q_2}{Q_1}$$

$\eta$ would equal $1$, or $100\%$, only if $Q_2 = 0$ — nothing rejected at all. No engine has ever done it, and the second law of thermodynamics, coming next, shows that it is impossible rather than merely difficult.

On a $p$–$V$ diagram the cycle is a closed loop. Run clockwise, the gas does more work expanding at high pressure than is done on it while being compressed at low pressure, and the net work per cycle is the **area enclosed** by the loop.

![A rectangular cycle on a p-V diagram, A to B to C to D: expansion at 2 x 10^5 Pa, compression at 1 x 10^5 Pa; enclosed area 200 J](figures/heat_engines/cycle-net-work.svg "The gas does 400 J expanding and has 200 J done on it while being compressed; the net 200 J is the enclosed area.")

## Worked example

**Given (illustrative):** each second, the mower's engine absorbs $Q_1 = 20\,\text{kJ}$ from burning fuel and rejects $Q_2 = 15\,\text{kJ}$ through its exhaust and fins.
**Find:** the work done per second and the efficiency.

The work is whatever is left of the heat taken in:

$$W = Q_1 - Q_2 = 20 - 15 = 5\,\text{kJ per second}$$

So three quarters of the fuel's heat leaves as warm air, and one quarter turns the blades.

$$\eta = \frac{W}{Q_1} = \frac{5}{20} = 0.25 = 25\%$$

**Sanity check:** $5\,\text{kJ}$ every second is a mechanical power of $5\,\text{kW}$ — a few horsepower, the right size for a machine one person walks behind, and $\eta = 1 - 15/20 = 0.25$ agrees with the other formula.

## Where the picture breaks

A petrol mower is an internal combustion engine: the fuel burns *inside* the cylinder and fresh air is drawn in each cycle, so it does not literally shuttle one fixed parcel of gas between two reservoirs. The two-reservoir model is an idealisation that gets the energy accounting right. Some of its losses really are engineering problems — friction in the bearings, fuel that does not burn completely, heat leaking out of the exhaust pipe — and better engineering shrinks them. Rejecting heat to a colder place is a different kind of loss: every heat engine must do it, however beautifully it is built.

## Key takeaway

A heat engine takes heat $Q_1$ from a hot reservoir, does work $W$, and rejects heat $Q_2$ to a cold one, with its working substance running in a cycle. Over a cycle $W = Q_1 - Q_2$, and $\eta = W/Q_1 = 1 - Q_2/Q_1$. Because $Q_2$ is never zero, $\eta$ is always less than $1$.
