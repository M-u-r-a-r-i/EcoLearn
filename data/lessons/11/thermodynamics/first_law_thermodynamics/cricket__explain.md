---
concept_id: first_law_thermodynamics
interest: cricket
format: explain
title: Where the sun's energy goes in a bowling machine's cylinder
check:
  question: |-
    Groundstaff refill a bowling machine's cylinder with a hand pump. During one stroke, $120\,\text{J}$ of work is done on the air, and the air gives out $30\,\text{J}$ of heat to the cylinder walls. Using $\Delta Q = \Delta U + \Delta W$, what is the change in the air's internal energy?
  options:
    A: |-
      $-150\,\text{J}$
    B: |-
      $+150\,\text{J}$
    C: |-
      $+90\,\text{J}$
    D: |-
      $-90\,\text{J}$
  answer: C
  explanation: |-
    Heat given out: $\Delta Q = -30\,\text{J}$. Work done on the air: $\Delta W = -120\,\text{J}$. So $\Delta U = \Delta Q - \Delta W = -30 - (-120) = +90\,\text{J}$; the air warms up.
  misconceptions:
    A: |-
      Gets both signs right but adds them, using $\Delta U = \Delta Q + \Delta W$. In NCERT's form, $\Delta W$ is work done by the gas and is subtracted.
    B: |-
      Treats every energy amount as a gain and adds the magnitudes, ignoring that the $30\,\text{J}$ of heat left the air.
    D: |-
      Reverses the sign convention, counting heat given out as positive and work done on the gas as negative, so the answer comes out with the wrong sign.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A hot afternoon at a cricket ground: blazing sun, a board showing 38 degrees, a bowler polishing the ball, a generator with hot exhaust and an ice box of drinks](scenes/cricket/thermodynamics.svg "Lunch on a scorching day. Anything left in that sun takes in energy.")

At lunch on a scorching training day, Meher notices something odd about the academy's spare air cylinder, the one used for the bowling machine. It has been left on the grass in full sun, and its piston, which slides freely, has crept outwards by a few centimetres all by itself.

"The sun pushed it," she tells her coach, Balwinder.

"The sun heated the air," he says. "The air pushed it. So did all the sun's energy go into pushing the piston?"

"Obviously," says Meher. Then she touches the cylinder. It's warm, and the stick-on thermometer strip on its side reads well above this morning's value. So some of the energy stayed in the air as well.

Balwinder smiles. "Then it's a sharing problem. The sun gives the air some energy. Some leaves as work on the piston. Some stays behind and warms the air. Is there a rule for how it's shared?"

## The physics

The **first law of thermodynamics** is energy conservation applied to heat, work and internal energy. For a system such as the air in the cylinder, in NCERT's form:

$$\Delta Q = \Delta U + \Delta W$$

- $\Delta Q$ is the **heat supplied to** the system: positive when heat flows in, negative when heat flows out.
- $\Delta U$ is the **change in internal energy** of the system: positive if it increases.
- $\Delta W$ is the **work done by** the system on its surroundings: positive when the gas expands and pushes, negative when the gas is compressed (work is done on it).

![A cylinder of gas: heat supplied to the gas is Delta Q greater than zero; work done by the gas as it expands is Delta W greater than zero; Delta Q equals Delta U plus Delta W](figures/first_law_thermodynamics/sign-convention.svg "Heat in and work out are positive. Reverse either direction and flip its sign.")

In words: the heat supplied is shared between raising the internal energy and doing work. Rearranged, $\Delta U = \Delta Q - \Delta W$.

Two facts make the law powerful. First, $\Delta U$ depends only on the start and end states, even though $\Delta Q$ and $\Delta W$ separately depend on the path; their difference does not. Second, for an ideal gas, $U$ depends only on temperature, so the sign of $\Delta U$ tells you whether the gas warmed or cooled.

Some books write the law as $\Delta U = Q + W$ with $W$ the work done **on** the gas. It is the same physics with the opposite sign for work. Stick to one convention; mixing them is the most common way to get these problems wrong.

In Meher's cylinder: the sun supplies heat ($\Delta Q > 0$), the air expands and pushes the piston ($\Delta W > 0$), and the air warms ($\Delta U > 0$). Heat in is shared between the two.

## Worked example

**Given (illustrative):** during lunch, the sun supplies $500\,\text{J}$ of heat to the air, and the air does $200\,\text{J}$ of work pushing the piston out. In the evening, the air loses $350\,\text{J}$ of heat to the cooling surroundings while the outside air pushes the piston back in, doing $100\,\text{J}$ of work on the gas.
**Find:** $\Delta U$ for each stage.

**Lunch:** $\Delta Q = +500\,\text{J}$ (heat in), $\Delta W = +200\,\text{J}$ (work by the gas).

$$\Delta U = \Delta Q - \Delta W = 500 - 200 = +300\,\text{J}$$

The air warms, as Meher felt.

**Evening:** $\Delta Q = -350\,\text{J}$ (heat out), $\Delta W = -100\,\text{J}$ (work done on the gas).

$$\Delta U = -350 - (-100) = -250\,\text{J}$$

The air cools.

**Sanity check:** in the evening the air receives $100\,\text{J}$ as work and gives out $350\,\text{J}$ as heat, a net loss of $250\,\text{J}$; that matches.

## Where the picture breaks

We treated the air as a closed system with a single temperature and pressure. A real cylinder also heats its own metal walls, and if the valve leaks, air, and its energy, escapes; the first law in this simple form needs a fixed amount of gas. The sun heats the cylinder unevenly, so the "slow, even" process is an idealisation. Finally, the cricket here is only the setting: a gas cylinder obeys this law whether it's at a ground or in a laboratory.

## Key takeaway

The first law is energy conservation: $\Delta Q = \Delta U + \Delta W$. Heat supplied to a gas is shared between raising its internal energy and the work it does. Heat in and work done by the gas are positive; heat out and work done on the gas are negative. Get the signs right first, then the arithmetic is easy.
