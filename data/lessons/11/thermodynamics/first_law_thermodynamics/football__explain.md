---
concept_id: first_law_thermodynamics
interest: football
format: explain
title: Where your arm's energy goes when you pump up a ball
check:
  question: |-
    In one downstroke of a ball pump, a player does $40\,\text{J}$ of work on the air in the barrel, and the air gives out $10\,\text{J}$ of heat to the metal. Using $\Delta Q = \Delta U + \Delta W$, what is the change in the air's internal energy?
  options:
    A: |-
      $-50\,\text{J}$
    B: |-
      $+50\,\text{J}$
    C: |-
      $-30\,\text{J}$
    D: |-
      $+30\,\text{J}$
  answer: D
  explanation: |-
    Heat given out: $\Delta Q = -10\,\text{J}$. Work done *on* the air: $\Delta W = -40\,\text{J}$. So $\Delta U = \Delta Q - \Delta W = -10 - (-40) = +30\,\text{J}$, and the air warms.
  misconceptions:
    A: |-
      Gets both signs right but adds them, as if $\Delta U = \Delta Q + \Delta W$. In NCERT's form, $\Delta W$ is the work done *by* the gas, so it is subtracted.
    B: |-
      Treats every energy amount as a gain and adds the magnitudes, ignoring that the $10\,\text{J}$ of heat left the air.
    C: |-
      Reverses the sign convention — counting heat given out as positive and work done on the gas as negative — so the size is right but the sign is wrong, and the air would appear to cool.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground on a hot day: a board reading 36 degrees Celsius, an ice box of drinks, a player inflating a ball with a hand pump, and a mower with a hot exhaust](scenes/football/thermodynamics.svg "Twenty balls to inflate before kick-off. Watch the pump, not the ball.")

There are twenty balls to inflate before the inter-school tournament starts, and Yusuf has drawn the job. He works through them by the fence, pressure gauge in one hand, needle valve in the other, and by the eighth ball his shoulders are burning.

Priya comes to take a turn and grabs the barrel of the pump near the bottom. She lets go straight away. "That's hot."

Yusuf laughs, then stops laughing. There is no flame anywhere near it. He has not plugged it into anything. All that has happened is that his arm has been pushing a handle down, over and over.

"So where's the heat coming from?" says Priya. "Out of your arm?"

Some of his effort clearly went into the balls — twenty of them are firm now. Some of it is sitting in that barrel, warm enough to sting her hand. Is there a rule for how the energy gets shared?

## The physics

The **first law of thermodynamics** is energy conservation, written for a system that can exchange both heat and work. In NCERT's form:

$$\Delta Q = \Delta U + \Delta W$$

- $\Delta Q$ is the **heat supplied to** the system: positive when heat flows in, negative when heat flows out.
- $\Delta U$ is the **change in internal energy**: positive when it rises.
- $\Delta W$ is the **work done by** the system on its surroundings: positive when the gas expands and pushes, negative when the gas is compressed, because then the surroundings do work on it.

![A cylinder of gas: heat supplied to the gas is Delta Q greater than zero; work done by the gas as it expands is Delta W greater than zero; Delta Q equals Delta U plus Delta W](figures/first_law_thermodynamics/sign-convention.svg "Heat in and work out are positive. Reverse either direction and flip its sign.")

In words: heat supplied to a system is shared between raising its internal energy and doing work on the outside world. Rearranged for problems where you know the transfers, $\Delta U = \Delta Q - \Delta W$.

The law is powerful for two reasons. First, $\Delta Q$ and $\Delta W$ each depend on the path taken, but their *difference* does not: $\Delta U$ depends only on the start and end states. Second, for an ideal gas $U$ depends only on temperature, so the sign of $\Delta U$ tells you at once whether the gas warmed or cooled.

The system to watch in Yusuf's pump is the **air trapped in the barrel**, not the pump and not the ball. On a downstroke it is compressed, so work is done on it ($\Delta W$ negative), and it passes a little heat to the metal barrel ($\Delta Q$ negative). If more energy arrives as work than leaves as heat, $\Delta U$ is positive and the air heats up — which the barrel then feels.

Be warned: some books write the law as $\Delta U = Q + W$ with $W$ meaning the work done *on* the gas. Same physics, opposite sign for work. Pick one convention and hold it; mixing them is the single most common way to lose marks here.

## Worked example

**Given (illustrative):** on one downstroke, Yusuf does $30\,\text{J}$ of work on the air in the barrel, and the air passes $5\,\text{J}$ of heat to the metal.
**Find:** the change in the air's internal energy, and what happens later when the pump lies in the shade and that trapped air gives out $25\,\text{J}$ of heat with the handle untouched.

**The downstroke.** Work is done *on* the gas, so in NCERT's convention $\Delta W = -30\,\text{J}$. Heat leaves the gas, so $\Delta Q = -5\,\text{J}$.

$$\Delta U = \Delta Q - \Delta W = -5 - (-30) = +25\,\text{J}$$

The air gains $25\,\text{J}$, so it is hotter than before — that is the warmth Priya felt, carried into the metal.

**Resting in the shade.** The handle does not move, so no work is done at all: $\Delta W = 0$. Heat leaves: $\Delta Q = -25\,\text{J}$.

$$\Delta U = -25 - 0 = -25\,\text{J}$$

The air cools by exactly what it had gained, and is back to its starting state.

**Sanity check:** on the downstroke the air took in $30\,\text{J}$ and passed on $5\,\text{J}$, so $25\,\text{J}$ had to stay behind — there is nowhere else for it to go.

## Where the picture breaks

We treated the barrel's air as a fixed, closed system, but a working pump pushes most of that air out through the valve into the ball, so the amount of gas is not constant; the clean accounting above belongs to one squeeze with the outlet blocked. Part of the warmth in the barrel also comes from friction between the piston seal and the wall, which is not the gas's internal energy at all. And the metal itself is a third body warming up. The first law still holds for each of these pieces — you simply have to say clearly which system you are applying it to.

## Key takeaway

The first law is energy conservation: $\Delta Q = \Delta U + \Delta W$. Heat supplied to a gas is split between raising its internal energy and the work it does. Heat in and work done by the gas count as positive; heat out and work done on the gas count as negative. Fix the signs first, and the arithmetic looks after itself.
