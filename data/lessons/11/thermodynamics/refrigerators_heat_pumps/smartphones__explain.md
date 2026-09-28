---
concept_id: refrigerators_heat_pumps
interest: smartphones
format: explain
title: The air conditioner app that seems to get more out than it puts in
check:
  question: |-
    A fridge that reports to a phone app removes $1200\,\text{J}$ of heat from its inside while its compressor uses $400\,\text{J}$ of electrical work. What is its coefficient of performance as a refrigerator?
  options:
    A: |-
      $3.0$
    B: |-
      $4.0$
    C: |-
      $0.33$
    D: |-
      $0.75$
  answer: A
  explanation: |-
    A refrigerator's job is to remove heat from the cold space, so $\alpha = Q_2/W = 1200/400 = 3.0$. It releases $Q_1 = 1200 + 400 = 1600\,\text{J}$ into the kitchen.
  misconceptions:
    B: |-
      Uses the heat released into the kitchen, $Q_1/W = 1600/400 = 4.0$. That is the coefficient of performance of a heat pump, whose job is to deliver heat, not of a refrigerator.
    C: |-
      Inverts the ratio, computing $W/Q_2 = 400/1200$ as if it were an efficiency (output over input) that must be less than 1. The coefficient of performance is heat removed per unit of work, and it is often greater than 1.
    D: |-
      Divides the heat removed by the heat released, $Q_2/Q_1 = 1200/1600$. The coefficient of performance compares the heat removed with the work it costs.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A sunny room: a phone sealed in a puffed-up waterproof pouch on a windowsill, a phone charging on a desk seen through a clip-on thermal camera, an icy can of compressed air, and a wall air conditioner controlled from a phone app](scenes/smartphones/thermodynamics.svg "On the right: an air conditioner, and the phone app that reports what it is doing.")

The Iyer family in Chennai has just had a new split air conditioner fitted, the kind you control from a phone app. Pooja, in Class 11, spends the first evening exploring the app. One screen shows two live numbers, side by side: *Cooling: 2.0 kW* and *Power used: 0.5 kW*.

She shows her brother Arjun, who is doing engineering. "Look, it takes out four times more energy than it uses. That's impossible. Is the app lying?"

"It isn't," says Arjun. "Go and stand next to the outdoor unit on the balcony."

She does. A fan is blowing air out of it that is hotter than the warm Chennai night.

Pooja comes back puzzled. Heat flows from hot to cold; everyone knows that. The room is at $24\,^\circ\text{C}$ and the night outside is warmer. How can a machine push heat out of a cool room into hotter air, and how can it move more energy than it uses?

## The physics

Heat flows naturally from hot to cold. A **refrigerator** makes it go the other way, taking heat out of a cold space and dumping it somewhere hotter, and that needs work. An air conditioner is a refrigerator for a room. It is a **heat engine run in reverse**:

- the working substance (the **refrigerant**) absorbs heat $Q_2$ from the cold space at temperature $T_2$ (the room, through the indoor unit);
- external work $W$ is done on it (by the compressor in the outdoor unit, powered by electricity);
- it releases heat $Q_1$ to the hot surroundings at $T_1$ (the outside air, blown out by the outdoor unit's fan).

![Energy flow in a refrigerator: heat Q2 taken from the cold inside, electrical work W put in, and heat Q1 equal to Q2 plus W released to the room](figures/refrigerators_heat_pumps/refrigerator-energy-flow.svg "Everything taken from the cold space, plus all the work put in, comes out on the hot side. Widths to scale for Q2 = 600, W = 300, Q1 = 900.")

The refrigerant runs in a cycle, so $\Delta U = 0$ each cycle, and energy conservation gives

$$Q_1 = Q_2 + W$$

The heat released outside is always *more* than the heat removed from the room. That is why the balcony air felt so hot.

A refrigerator's job is to remove $Q_2$, and what that costs is $W$, so its performance is measured by the **coefficient of performance**:

$$\alpha = \frac{Q_2}{W}$$

$\alpha$ is not an efficiency, and it is often greater than 1. The AC does not *make* the $2.0\,\text{kW}$ of heat it removes; it only *moves* it, and moving heat can take less work than the amount of heat moved. That is what the app shows, and nothing is being created. But $\alpha$ can never be infinite, because some work is always needed ($W \neq 0$); the second law of thermodynamics, coming next, says why.

A **heat pump** is the same machine used for the opposite purpose: to warm a space by pumping heat in from colder surroundings. Many ACs sold for colder parts of India can run in reverse as heat pumps in winter. A heat pump's useful output is $Q_1$, so its coefficient of performance is $Q_1/W$.

## Worked example

**Given (the app's illustrative numbers):** every second, the AC removes $Q_2 = 2.0\,\text{kJ}$ of heat from the room, and the compressor uses $W = 0.5\,\text{kJ}$ of electrical work.
**Find:** its coefficient of performance, and the heat released on the balcony.

**Step 1: the coefficient of performance.**

$$\alpha = \frac{Q_2}{W} = \frac{2.0}{0.5} = 4$$

Every joule of electricity moves four joules of heat out of the room.

**Step 2: the heat released.**

$$Q_1 = Q_2 + W = 2.0 + 0.5 = 2.5\,\text{kJ per second}$$

That is $2.5\,\text{kW}$ of heat pouring out of the outdoor unit, about as much as two small electric kettles running at once.

**Step 3: the same machine as a heat pump.** Run in reverse on a cold night with the same heat and work per second, it would deliver $Q_1/W = 2.5/0.5 = 5$ joules of heat for every joule of electricity.

**Sanity check:** $Q_1 - Q_2 = 2.5 - 2.0 = 0.5\,\text{kJ} = W$, just as energy conservation requires.

## Where the picture breaks

A room is not a fixed cold reservoir. Sunlight, people, phones and laptops keep adding heat, which is why the AC keeps running. The coefficient of performance also changes with the temperatures: the bigger the gap between room and outside, the more work each joule of heat costs, so the same AC does worse on a scorching afternoon. The app's numbers are estimates the unit calculates, and they include losses in fans and electronics. The figures here are round and illustrative, not those of any real product.

## Key takeaway

A refrigerator or AC is a heat engine run in reverse: it uses work $W$ to take heat $Q_2$ from a cold space and releases $Q_1 = Q_2 + W$ to hotter surroundings. Its coefficient of performance is $\alpha = Q_2/W$, often greater than 1 because heat is moved, not made. A heat pump is the same machine valued for the heat it delivers, $Q_1/W$.
