---
concept_id: heat_engines
interest: gaming
format: explain
title: The generator that saved the tournament
check:
  question: |-
    In each cycle, a café's standby generator engine absorbs $24\,\text{kJ}$ of heat from burning fuel and does $6\,\text{kJ}$ of work. What is its efficiency, and how much heat does it reject?
  options:
    A: |-
      $\eta = 33\%$; $18\,\text{kJ}$ rejected
    B: |-
      $\eta = 25\%$; $24\,\text{kJ}$ rejected
    C: |-
      $\eta = 75\%$; $18\,\text{kJ}$ rejected
    D: |-
      $\eta = 25\%$; $18\,\text{kJ}$ rejected
  answer: D
  explanation: |-
    Over a cycle $\Delta U = 0$, so $Q_2 = Q_1 - W = 24 - 6 = 18\,\text{kJ}$, and $\eta = W/Q_1 = 6/24 = 0.25 = 25\%$.
  misconceptions:
    A: |-
      Divides the work by the heat *rejected* ($6/18$). Efficiency compares the useful output with the energy paid for, which is the heat absorbed, $Q_1$.
    B: |-
      Forgets that the work came out of the heat absorbed, so it rejects the whole $24\,\text{kJ}$ as well. That would create $6\,\text{kJ}$ from nothing and break the first law.
    C: |-
      Computes $Q_2/Q_1 = 18/24$, the fraction *wasted*, and calls it the efficiency. The efficiency is what is left over: $1 - Q_2/Q_1$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor showing GPU and CPU temperatures, a tower PC with a heat sink and fans, hot air leaving the top and cool air drawn in, a can of compressed-air duster, a mini fridge under the desk and a backup generator outside the window](scenes/gaming/thermodynamics.svg "Outside the window, on the back lane: the generator that keeps the machines alive when the grid does not.")

Semi-final, four minutes on the clock, and the whole lane goes dark.

Twenty screens die at once. Somebody groans. Then, from the back of the café, comes a cough, a rattle, and a steady roar, and the lights and the machines come back on together. The owner has a diesel generator behind the building for exactly this.

Afterwards, Rohit goes out to look at it. It is still running, ticking and roaring, and he cannot put a hand within a foot of the exhaust. The air coming off it is like the air off a cooking fire.

He does a rough sum. The café was running perhaps twenty machines and the lights. All of that came out of a tank of diesel — and so did this blast of hot air, which is doing nothing for anybody.

"Why does it throw so much of it away?" he asks the owner's brother, who maintains the thing. "Couldn't a better engine turn *all* of the fuel's heat into electricity?"

"Every engine I've ever touched gets hot," he says, wiping his hands. "I've never met one that didn't."

Is that bad engineering — or is it built into what an engine *is*?

## The physics

A **heat engine** takes in heat and turns part of it into work, over and over, by running a **working substance** — usually a gas — through a **cycle** that brings it back to its starting state. Every heat engine has three parts:

- a **hot reservoir** at temperature $T_1$, from which it absorbs heat $Q_1$ (here, the burning diesel);
- the **working substance**, which does work $W$ on the surroundings;
- a **cold reservoir** at a lower temperature $T_2$, into which it rejects heat $Q_2$ (here, the night air, through the exhaust and the radiator).

![A hot reservoir above an engine and a cold reservoir below: heat Q1 flows in, work W comes out to the side, heat Q2 flows down into the cold reservoir](figures/heat_engines/engine-energy-flow.svg "Heat in splits into useful work and rejected heat. The arrow widths are drawn to scale for Q1 = 50, W = 15 and Q2 = 35.")

Because the working substance ends each cycle in exactly the state it began, its internal energy is unchanged over the cycle: $\Delta U = 0$. The first law then gives

$$W = Q_1 - Q_2$$

The **efficiency** $\eta$ is the fraction of the heat absorbed that leaves as work:

$$\eta = \frac{W}{Q_1} = 1 - \frac{Q_2}{Q_1}$$

$\eta$ could reach 1, or 100%, only if $Q_2$ were zero — nothing rejected at all. No engine has ever managed it. The second law of thermodynamics, which comes next, explains why that is impossible rather than merely difficult.

On a $p$–$V$ diagram the cycle is a closed loop. Run clockwise, the gas does more work expanding at high pressure than is done on it while it is compressed at low pressure, and the net work per cycle is the **area enclosed** by the loop.

![A rectangular cycle on a p-V diagram, A to B to C to D: expansion at 2 x 10^5 Pa, compression at 1 x 10^5 Pa, with 200 J enclosed](figures/heat_engines/cycle-net-work.svg "The gas does 400 J expanding and has 200 J done on it while being compressed; the 200 J left over is the area inside the loop.")

## Worked example

**Given (illustrative):** every second, the generator's engine absorbs $Q_1 = 100\,\text{kJ}$ from burning diesel and rejects $Q_2 = 70\,\text{kJ}$ through its exhaust and radiator.
**Find:** the work done each second, the efficiency, and the mechanical power.

Over each cycle the working substance returns to its starting state, so the work is simply the difference between the two heats:

$$W = Q_1 - Q_2 = 100 - 70 = 30\,\text{kJ per second}$$

That fraction of the fuel's heat is the part that actually turns the shaft:

$$\eta = \frac{W}{Q_1} = \frac{30}{100} = 0.30 = 30\%$$

And $30\,\text{kJ}$ every second is a mechanical power of $30\,\text{kW}$ — enough to keep a café full of machines and lights running, with the generator then losing a little more on its way to electricity.

**Sanity check:** seventy per cent of the fuel's heat goes out of the exhaust, which is why Rohit could not hold his hand near it. An engine that felt cool would be the surprising one.

## Where the picture breaks

A diesel generator is an internal combustion engine: the fuel burns *inside* the cylinder and fresh air is drawn in on every cycle, so it does not literally shuttle one fixed parcel of gas between two reservoirs. The two-reservoir model is an idealisation that gets the energy accounting right without describing the hardware. Some of its losses really are engineering problems — friction in the bearings, fuel that does not burn completely, heat leaking through the block — and better engineering shrinks them. Rejecting heat into something colder is a different kind of loss: every heat engine must do it, however beautifully it is built.

## Key takeaway

A heat engine runs a working substance through a cycle, absorbing $Q_1$ from a hot reservoir, doing work $W$, and rejecting $Q_2$ to a cold one. Over a cycle $W = Q_1 - Q_2$, and the efficiency is $\eta = W/Q_1 = 1 - Q_2/Q_1$. Since $Q_2$ is never zero, $\eta$ is always less than 1.
