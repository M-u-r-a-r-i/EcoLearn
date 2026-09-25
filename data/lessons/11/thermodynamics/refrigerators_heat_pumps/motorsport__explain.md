---
concept_id: refrigerators_heat_pumps
interest: motorsport
format: explain
title: The car air conditioner that blows heat out of the front
check:
  question: |-
    In one second, a car's air conditioner removes $2000\,\text{J}$ of heat from the cabin while its compressor does $800\,\text{J}$ of work. What is its coefficient of performance as a refrigerator?
  options:
    A: |-
      $3.5$
    B: |-
      $0.40$
    C: |-
      $2.5$
    D: |-
      $0.71$
  answer: C
  explanation: |-
    A refrigerator's job is to remove heat from the cold space, so $\alpha = Q_2/W = 2000/800 = 2.5$. It releases $Q_1 = 2000 + 800 = 2800\,\text{J}$ to the outside air.
  misconceptions:
    A: |-
      Uses the heat released outside, $Q_1/W = 2800/800 = 3.5$. That is the coefficient of performance of a heat pump, whose job is to deliver heat, not of a refrigerator.
    B: |-
      Inverts the ratio, computing $W/Q_2 = 800/2000$ as if it were an efficiency (output over input). The coefficient of performance is heat removed per unit of work, and it is often greater than 1.
    D: |-
      Divides the heat removed by the heat released, $Q_2/Q_1 = 2000/2800$. The coefficient of performance compares the heat removed with the work it costs.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A pit lane in the afternoon sun: a stack of tyres in electric tyre blankets with a probe thermometer, a race car with a glowing front brake disc and a hot exhaust, and a compressed-air bottle feeding a wheel gun](scenes/motorsport/thermodynamics.svg "A blazing afternoon. Inside any closed car here, the air conditioner is fighting the sun.")

It's June in Nagpur, $44\,^\circ\text{C}$ in the shade, and Nikhil and his grandfather, Baldev, a retired truck mechanic, are waiting at a closed railway crossing with the engine idling. Inside, the air conditioner has kept the cabin pleasantly cool. Nikhil steps out to stretch his legs, walks round to the front of the car and holds his hand near the grille. Hot air is pouring out of it, hotter than the scorching afternoon itself.

"The engine's overheating!" he says.

"No," says Baldev. "That's your cool cabin. The AC's heat is coming out there, through a little radiator of its own in front of the big one."

Nikhil isn't convinced. Heat always flows from hot to cold; he learned that in Class 9. The cabin is at $24\,^\circ\text{C}$. The air outside is $44\,^\circ\text{C}$. How can a machine take heat out of the cool cabin and push it into air that's already hotter?

"It can," says Baldev. "But it doesn't do it for free. Watch the fuel gauge next time you drive with the AC off."

What does it cost to make heat flow the wrong way?

## The physics

Heat flows naturally from hot to cold. A **refrigerator** makes it go the other way, taking heat out of a cold space and dumping it somewhere hotter, and that needs work. A refrigerator is a **heat engine run in reverse**:

- the working substance (the **refrigerant**) absorbs heat $Q_2$ from the cold space at temperature $T_2$ (the cabin);
- external work $W$ is done on it (by the compressor, driven by the engine or, in an electric car, by the battery);
- it releases heat $Q_1$ to the hot surroundings at $T_1$ (the outside air, through the small radiator behind the grille, called the condenser).

![Energy flow in a refrigerator: heat Q2 taken from the cold inside, electrical work W put in, and heat Q1 equal to Q2 plus W released to the room](figures/refrigerators_heat_pumps/refrigerator-energy-flow.svg "Everything taken from the cold space, plus all the work put in, comes out on the hot side. Widths to scale for Q2 = 600, W = 300, Q1 = 900.")

The refrigerant runs in a cycle, so $\Delta U = 0$ each cycle, and energy conservation gives

$$Q_1 = Q_2 + W$$

The heat released outside is always *more* than the heat removed from the cabin. That is why the air from the grille felt hotter than the day.

A refrigerator's job is to remove $Q_2$, and what that costs is $W$, so its performance is measured by the **coefficient of performance**:

$$\alpha = \frac{Q_2}{W}$$

$\alpha$ is not an efficiency and is often greater than 1: moving heat can take less work than the amount of heat moved. But $\alpha$ can never be infinite, because some work is always needed ($W \neq 0$); the second law of thermodynamics, coming next, says why.

A **heat pump** is the same machine used for the opposite purpose: to warm a space by pumping heat in from colder surroundings. Many electric cars warm their cabins in winter this way. A heat pump's useful output is $Q_1$, so its coefficient of performance is $Q_1/W$.

## Worked example

**Given (illustrative):** every second, the car's AC removes $Q_2 = 3\,\text{kJ}$ of heat from the cabin, and the compressor does $W = 1\,\text{kJ}$ of work.
**Find:** its coefficient of performance, and the heat released at the front of the car.

**Step 1: the coefficient of performance.**

$$\alpha = \frac{Q_2}{W} = \frac{3}{1} = 3$$

Every joule of work moves three joules of heat out of the cabin.

**Step 2: the heat released.**

$$Q_1 = Q_2 + W = 3 + 1 = 4\,\text{kJ per second}$$

That is $4\,\text{kW}$ of heat blowing out of the grille, about as much as two room heaters on full, which is what Nikhil felt on his hand.

**Step 3: the same machine as a heat pump.** Run to warm the cabin on a cold morning, it would deliver $Q_1/W = 4/1 = 4$ joules of heat for every joule of work.

**Sanity check:** $Q_1 - Q_2 = 4 - 3 = 1\,\text{kJ} = W$, just as energy conservation requires.

## Where the picture breaks

A car's AC does not have fixed reservoirs. The sun keeps heating the cabin, passengers give off heat, and the outside air around the condenser warms up as the car sits still, which is why the AC struggles most in a traffic jam. The coefficient of performance also changes with the temperatures: the bigger the gap between cabin and outside, the more work each joule of heat costs. Real systems lose some energy to friction in the compressor and to the fans. The numbers here are round and illustrative, not those of any real car.

## Key takeaway

A refrigerator is a heat engine run in reverse: it uses work $W$ to take heat $Q_2$ from a cold space and releases $Q_1 = Q_2 + W$ to hotter surroundings. Its coefficient of performance is $\alpha = Q_2/W$, which is often greater than 1 but never infinite. A heat pump is the same machine valued for the heat it delivers, $Q_1/W$.
