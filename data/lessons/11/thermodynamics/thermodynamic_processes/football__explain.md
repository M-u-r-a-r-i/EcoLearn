---
concept_id: thermodynamic_processes
interest: football
format: explain
title: The ball that got harder in the back of the van
check:
  question: |-
    A sealed ball is left in a hot van. Its casing is stiff, so the volume of the air inside does not change while the air absorbs $200\,\text{J}$ of heat. Which statement is correct?
  options:
    A: |-
      All $200\,\text{J}$ becomes internal energy; the air does no work, and its pressure rises.
    B: |-
      The air does $200\,\text{J}$ of work pushing outwards on the casing, so its temperature does not change.
    C: |-
      The process is adiabatic, because the ball is sealed and no air gets in or out.
    D: |-
      Half the heat becomes work and half becomes internal energy, as in any isobaric process.
  answer: A
  explanation: |-
    At constant volume $\Delta W = 0$, so the first law gives $\Delta Q = \Delta U$: every joule of heat raises the internal energy. For a fixed amount of gas in a fixed volume, a higher temperature means a higher pressure.
  misconceptions:
    B: |-
      Confuses pressure with work. The air pushes harder on the casing, but the casing does not move, so no work is done — force alone is not work.
    C: |-
      Confuses "sealed" with "adiabatic". Adiabatic means no *heat* crosses the boundary; a sealed ball still lets heat through its casing, which is exactly what happens here.
    D: |-
      Invents a fixed split. How the heat divides depends on the process, and even in an isobaric process the split is set by $p\,\Delta V$, not by a half-and-half rule.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground on a hot day: a board reading 36 degrees Celsius, an ice box of drinks, a player inflating a ball with a hand pump, and a mower with a hot exhaust](scenes/football/thermodynamics.svg "A 36 °C day. The same air behaves in completely different ways depending on how you change it.")

The referee, Vandana, checks the match balls at nine in the morning and writes the gauge readings on a slip of paper. Then the balls go back into the closed van, which spends the day parked in full sun.

At three o'clock, before the final, she checks again. Every ball reads high — over her limit. Tarun, the captain, is baffled. "Nobody has touched them. The van was locked."

Vandana shrugs and starts bleeding them down to the right pressure, pressing the needle valve on each one. Tarun holds the third ball while she does it, with his thumb near the valve, and pulls his hand back. "That's cold. The air coming out is *cold*."

Same balls, same air, same afternoon. Locked in a hot van, the air pushes harder. Let out in a hiss, it turns cold. And when Tarun pumps a ball back up slowly, taking his time, the pump barely warms at all.

What decides which of these happens?

## The physics

Any change a gas goes through is a **process**, and the first law $\Delta Q = \Delta U + \Delta W$ applies to every one of them. What changes from process to process is which quantity is held fixed. Two facts do the heavy lifting: for an ideal gas $U$ depends only on temperature, and the work is the area under the $p$–$V$ curve.

![A p-V diagram with four processes starting from the same state A: a horizontal isobaric line, a vertical isochoric line, a falling isothermal curve and a steeper falling adiabatic curve](figures/thermodynamic_processes/four-processes-pv.svg "From the same start: isobaric is flat, isochoric is vertical, and the adiabatic curve falls more steeply than the isothermal one.")

**Isochoric** (constant volume). $\Delta W = 0$, so $\Delta Q = \Delta U$. All the heat goes into internal energy, the temperature rises, and for a fixed amount of gas the pressure rises with it. This is the balls in the hot van: a stiff casing holds the volume fixed while the sun warms the air inside.

**Adiabatic** (no heat exchanged, $\Delta Q = 0$). Either the system is insulated or the change is too fast for heat to flow. Then $\Delta U = -\Delta W$, and $pV^\gamma = \text{constant}$, where $\gamma = C_p/C_v$ (about $1.4$ for air). Compress the gas and $\Delta W < 0$, so $U$ rises and it heats: a fast pump stroke. Let it expand quickly and $\Delta W > 0$, so $U$ falls and it cools: Tarun's cold valve. The work done by the gas is $W = \dfrac{\mu R(T_1 - T_2)}{\gamma - 1}$. The adiabatic curve falls more steeply than the isotherm through the same point, because the pressure drops both from the expansion *and* from the cooling.

**Isothermal** (constant temperature). The gas stays in good thermal contact with its surroundings and changes slowly, so $pV = \text{constant}$. Since $T$ is fixed, $\Delta U = 0$ and $\Delta Q = \Delta W$: every joule of heat supplied comes straight back out as work. For $\mu$ moles going from $V_1$ to $V_2$ at temperature $T$,
$$W = \mu R T \ln\frac{V_2}{V_1}$$
Tarun's slow pumping is close to this: heat has time to leak away, so the barrel hardly warms.

**Isobaric** (constant pressure). $W = p(V_2 - V_1)$, and $\Delta Q = \Delta U + p\,\Delta V$: the heat is shared between warming the gas and doing work. The air inside a ball springing back off a boot is close to this over its small volume change.

**Cyclic.** The gas returns to its starting state, so $\Delta U = 0$ over the whole cycle and the net heat absorbed equals the net work done — the area enclosed by the loop.

## Worked example

**Given (illustrative):** (a) in the van, the air in a ball of fixed volume absorbs $200\,\text{J}$ of heat. (b) One quick pump stroke does $60\,\text{J}$ of work on the air in the barrel, too fast for heat to escape.
**Find:** $\Delta Q$, $\Delta W$ and $\Delta U$ for each.

**(a) Isochoric.** The volume cannot change, so $\Delta W = 0$.

$$\Delta U = \Delta Q - \Delta W = 200 - 0 = +200\,\text{J}$$

The air is hotter, so it presses harder — Vandana's high gauge readings.

**(b) Adiabatic.** No heat crosses the boundary, so $\Delta Q = 0$, and work done *on* the gas means $\Delta W = -60\,\text{J}$.

$$\Delta U = 0 - (-60) = +60\,\text{J}$$

The air heats up, with nothing but Tarun's arm to thank for it.

And for comparison: if that same ball's air expanded slowly at constant temperature while absorbing $200\,\text{J}$, then $\Delta U = 0$ and all $200\,\text{J}$ would leave again as work.

**Sanity check:** in (a) nothing moved, so no energy could leave as work; in (b) nothing flowed as heat, so the work had nowhere to go but internal energy. Each time, energy ends up in the only channel left open.

## Where the picture breaks

Real processes only approach these ideals. No pump stroke is perfectly adiabatic and no slow one is perfectly isothermal; where a real stroke lands between the two depends on how fast you push. A ball's casing is stiff but not rigid, so the "constant volume" in the van is an approximation, and some of the warmth in a pump comes from piston friction, which the ideal-gas model does not include. The cold valve is the loosest of all: air is escaping, so the amount of gas is not fixed and this is not a closed system at all. The direction of every effect is right; the labels are idealisations.

## Key takeaway

Use $\Delta Q = \Delta U + \Delta W$ and ask what is held fixed. Isochoric: $\Delta W = 0$, so $\Delta Q = \Delta U$. Adiabatic: $\Delta Q = 0$, so compression heats and expansion cools. Isothermal: $\Delta U = 0$, so $\Delta Q = \Delta W$. Isobaric: $W = p\,\Delta V$. Cyclic: $\Delta U = 0$, and the net work is the area enclosed on the $p$–$V$ diagram.
