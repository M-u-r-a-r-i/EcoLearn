---
concept_id: heat_engines
interest: smartphones
format: explain
title: The heat engine at the far end of your phone charger
check:
  question: |-
    In each cycle, the steam in a small power-station turbine absorbs $500\,\text{J}$ of heat from the boiler and rejects $400\,\text{J}$ of heat to the cooling water. What is the efficiency of this engine?
  options:
    A: |-
      $80\%$
    B: |-
      $25\%$
    C: |-
      $20\%$
    D: |-
      $100\%$
  answer: C
  explanation: |-
    Over a cycle $\Delta U = 0$, so the work is $W = Q_1 - Q_2 = 500 - 400 = 100\,\text{J}$, and the efficiency is $\eta = W/Q_1 = 100/500 = 0.20 = 20\%$.
  misconceptions:
    A: |-
      Computes $Q_2/Q_1 = 400/500$, the fraction of the heat that is rejected, and mistakes it for the efficiency. Efficiency is the fraction that becomes work.
    B: |-
      Divides the work by the heat rejected, $100/400$. Efficiency compares the useful work with the heat taken in, $Q_1$, not with the heat thrown away.
    D: |-
      Reasons that energy is conserved, so all of it comes out somewhere and the engine must be 100% efficient. Energy is conserved, but efficiency counts only the part that comes out as useful work.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A sunny room: a phone sealed in a puffed-up waterproof pouch on a windowsill, a phone charging on a desk seen through a clip-on thermal camera, an icy can of compressed air, and a wall air conditioner controlled from a phone app](scenes/smartphones/thermodynamics.svg "Follow the charging cable back into the wall, and a long way further, and you reach a heat engine.")

During a school visit to a coal-fired power station near Nagpur, Priya's class stands on a walkway beside the cooling towers. Clouds of warm vapour roll out of their tops into the sky.

Their guide, an engineer called Mrs. Deshpande, points up. "Every time you charge your phone, some of this is for you."

Priya checks her phone: 20%. "So the coal's energy ends up in my battery?"

"Some of it. Burning coal boils water into high-pressure steam. The steam spins a turbine, the turbine spins a generator, and the electricity comes down the wires to your charger. But look up. Most of the coal's heat isn't going into the wires at all. It's going into the sky."

Priya frowns. Why build a gigantic machine that throws most of its heat into the air? Surely the engineers could catch it and turn it into electricity too?

## The physics

A **heat engine** is a device that takes in heat and turns part of it into work, over and over, by running a **working substance** (here, water and steam) through a **cycle** that returns it to its starting state. Every heat engine has three parts:

- a **hot reservoir** at temperature $T_1$, from which it absorbs heat $Q_1$ (the boiler, heated by burning coal);
- the **working substance**, which does work $W$ on the surroundings (the steam pushing the turbine blades);
- a **cold reservoir** at a lower temperature $T_2$, to which it rejects heat $Q_2$ (the cooling water, which carries the heat to the towers and the sky).

![A hot reservoir above an engine and a cold reservoir below: heat Q1 flows in, work W comes out to the side, heat Q2 flows down to the cold reservoir](figures/heat_engines/engine-energy-flow.svg "Heat in splits into useful work and rejected heat; the arrow widths are drawn to scale for Q1 = 50, W = 15, Q2 = 35. The rejected share is never zero.")

Because the working substance ends each cycle in its starting state, $\Delta U = 0$ for the whole cycle, and the first law gives

$$W = Q_1 - Q_2$$

The **efficiency** $\eta$ is the fraction of the heat absorbed that comes out as work:

$$\eta = \frac{W}{Q_1} = 1 - \frac{Q_2}{Q_1}$$

$\eta$ could equal 1 (100%) only if $Q_2 = 0$, with no heat rejected at all. No engine has ever managed that, and the second law of thermodynamics, coming next, shows why it is impossible, not just difficult. The cooling towers are not waste by carelessness; the engine *must* dump heat somewhere colder in order to work.

On a $p$–$V$ diagram, a cycle is a closed loop. Run clockwise, the working substance does more work while expanding at high pressure than is done on it while being compressed at low pressure, and the net work per cycle is the **area enclosed** by the loop.

![A rectangular cycle on a p-V diagram, A to B to C to D: expansion at 2 x 10^5 Pa, compression at 1 x 10^5 Pa; enclosed area 200 J](figures/heat_engines/cycle-net-work.svg "The gas does 400 J expanding and has 200 J done on it while compressed; the net 200 J is the enclosed area.")

## Worked example

**Given (illustrative):** for every $300\,\text{J}$ of heat the steam absorbs from the boiler, it rejects $200\,\text{J}$ to the cooling water. Priya's phone battery stores, say, about $40\,\text{kJ}$ when full.
**Find:** the work per $300\,\text{J}$, the efficiency, and the least heat the power station must take from burning coal to fill the battery.

**Step 1: the work.**

$$W = Q_1 - Q_2 = 300 - 200 = 100\,\text{J}$$

**Step 2: the efficiency.**

$$\eta = \frac{W}{Q_1} = \frac{100}{300} = \frac{1}{3} \approx 33\%$$

One joule of work for every three joules of heat.

**Step 3: the heat for one full charge.** To deliver $40\,\text{kJ}$ of work, the boiler must supply three times as much heat:

$$Q_1 = \frac{W}{\eta} = 40 \times 3 = 120\,\text{kJ}$$

Of that, $80\,\text{kJ}$ goes up the cooling towers so that $40\,\text{kJ}$ can reach Priya's phone.

**Sanity check:** the heat rejected, $80\,\text{kJ}$, plus the work, $40\,\text{kJ}$, adds back up to the $120\,\text{kJ}$ taken in, just as energy conservation requires.

## Where the picture breaks

A real power station is more complicated than one engine with one efficiency. The turbine's work must pass through a generator, transformers, long wires and your charger, and each wastes a little more as heat, so in reality a full charge costs more than $120\,\text{kJ}$ of coal heat. Real steam cycles also have pumps, reheaters and many stages. And the water in a cooling tower leaves partly as evaporated vapour, not just warm air. All the numbers here are round and illustrative, not those of any real station or phone.

## Key takeaway

A heat engine runs a working substance in a cycle, absorbing heat $Q_1$ from a hot reservoir, doing work $W$, and rejecting heat $Q_2$ to a cold one. Over a cycle, $W = Q_1 - Q_2$, and the efficiency is $\eta = W/Q_1 = 1 - Q_2/Q_1$. The rejected heat is never zero, so $\eta$ is always less than 1.
