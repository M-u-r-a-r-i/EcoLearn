---
concept_id: first_law_thermodynamics
interest: gaming
format: explain
title: Why the duster can goes cold and then recovers
check:
  question: |-
    A cycle pump is used to refill a refillable air duster. During one stroke, $90\,\text{J}$ of work is done on the air, and the air passes $30\,\text{J}$ of heat out through the barrel walls. Using $\Delta Q = \Delta U + \Delta W$, what is the change in the air's internal energy?
  options:
    A: |-
      $-120\,\text{J}$
    B: |-
      $+60\,\text{J}$
    C: |-
      $+120\,\text{J}$
    D: |-
      $-60\,\text{J}$
  answer: B
  explanation: |-
    Heat leaves the air, so $\Delta Q = -30\,\text{J}$. The work is done *on* the air, so the work done *by* it is $\Delta W = -90\,\text{J}$. Then $\Delta U = \Delta Q - \Delta W = -30 - (-90) = +60\,\text{J}$, and the air warms — which is why a pump barrel gets hot.
  misconceptions:
    A: |-
      Gets both signs right but adds them, using $\Delta U = \Delta Q + \Delta W$. In NCERT's form $\Delta W$ is the work done *by* the gas, so it is subtracted, not added.
    C: |-
      Treats both amounts as energy gained and adds the magnitudes, ignoring that the $30\,\text{J}$ of heat left the air.
    D: |-
      Reverses the sign convention — heat given out counted as positive, work done on the gas counted as positive — so the size is right but the sign is wrong.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor showing GPU and CPU temperatures, a tower PC with a heat sink and fans, hot air leaving the top and cool air drawn in, a can of compressed-air duster, a mini fridge under the desk and a backup generator outside the window](scenes/gaming/thermodynamics.svg "On the desk, beside the tower: the little can that gets cold when you use it.")

Nikhil's keyboard has reached the stage where the spacebar crunches. His sister Devika hands him a can of compressed-air duster from the shelf and tells him to take it outside.

He holds the trigger down and sweeps along the rows. It works beautifully for about fifteen seconds. Then two things happen at once: the jet goes weak, and the can turns so cold that he has to switch hands. A pale ring of frost has formed around the nozzle.

"It's making cold," says Devika, delighted. "Free air conditioning."

Nikhil puts it down on the step and they go back in. Ten minutes later he picks it up again: room temperature, and the jet is strong once more. Nothing was plugged in. Nobody did anything to it.

So where did the cold come from — and where did it go?

## The physics

The **first law of thermodynamics** is nothing more than energy conservation, written for a system that can exchange both heat and work. In NCERT's form:

$$\Delta Q = \Delta U + \Delta W$$

- $\Delta Q$ is the **heat supplied to** the system: positive when heat flows in, negative when it flows out.
- $\Delta U$ is the **change in internal energy** of the system: positive when it rises.
- $\Delta W$ is the **work done by** the system on its surroundings: positive when the gas expands and pushes, negative when the gas is compressed.

![A cylinder of gas: heat supplied to the gas is Delta Q greater than zero; work done by the gas as it expands is Delta W greater than zero; Delta Q equals Delta U plus Delta W](figures/first_law_thermodynamics/sign-convention.svg "Heat in and work out are the positive directions. Reverse either one and its sign flips.")

Read it as a sharing rule: heat supplied to a gas is split between raising its internal energy and doing work on the outside world. Rearranged for what you usually want,

$$\Delta U = \Delta Q - \Delta W$$

Two things make this law powerful. First, $\Delta U$ depends only on the start and end states, even though $\Delta Q$ and $\Delta W$ each depend on the path taken; their difference does not. Second, for an ideal gas $U$ depends only on temperature, so the sign of $\Delta U$ tells you straight away whether the gas got hotter or colder.

The law holds only for a fixed amount of gas — a closed system. In Nikhil's can, take the system to be the gas that *stays* in the can. As the rest escapes, that gas expands to fill the space behind it, and expanding means doing work.

Some books write the law as $\Delta U = Q + W$, with $W$ the work done **on** the gas. It is the same physics with the opposite sign on the work. Pick one convention and stay in it; mixing the two is the commonest way to lose marks here.

## Worked example

**Given (illustrative):** during the long blast, the gas remaining in the can does $60\,\text{J}$ of work as it expands, and the blast is over so quickly that almost no heat reaches it. Afterwards, standing on the step, the same gas takes in $60\,\text{J}$ of heat from the air while the steel can holds its volume fixed.
**Find:** $\Delta U$ for each stage, and what it does to the temperature.

**During the blast.** No time for heat: $\Delta Q = 0$. The gas expands, so the work it does is positive, $\Delta W = +60\,\text{J}$.

$$\Delta U = \Delta Q - \Delta W = 0 - 60 = -60\,\text{J}$$

The internal energy drops, so the temperature falls. That is Nikhil's frozen fingers: the gas paid for the work out of its own energy, because nothing else was available.

**Afterwards.** The can is rigid, so its volume cannot change and $\Delta W = 0$. Heat flows in: $\Delta Q = +60\,\text{J}$.

$$\Delta U = 60 - 0 = +60\,\text{J}$$

The gas warms back to room temperature, and the jet is strong again.

**Sanity check:** nothing was ever plugged in, so the energy for the blast had to come out of the gas itself, and the only place to get it back was the warm air outside. The two stages are equal and opposite, which is exactly why the can works again after a rest.

## Where the picture breaks

Most duster cans do not hold plain compressed gas: they hold a liquid that boils at low pressure, and a good share of the chill comes from that liquid evaporating and taking its latent heat from the can. Our gas-only account gets the direction and the reasoning right, but for such a can it is not the whole story. Even for a pure-gas can, the escaping gas and the gas left behind are not at one uniform pressure during a fast blast, so the process is only roughly the ideal one. And the "system" shrinks as gas leaves, which is why we were careful to follow only the gas that stayed. After the rest, the gas is back at room temperature but at a lower pressure than it began — some of it is now spread around the veranda.

## Key takeaway

The first law is energy conservation for heat and work: $\Delta Q = \Delta U + \Delta W$, with heat supplied positive and work done *by* the gas positive. Heat going in is shared between internal energy and work done. Do the signs first and the arithmetic second, and a gas that does work with no heat supplied must cool.
