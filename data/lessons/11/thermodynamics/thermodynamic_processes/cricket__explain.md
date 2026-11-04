---
concept_id: thermodynamic_processes
interest: cricket
format: explain
title: Why the bowling machine's pump gets hot and its valve gets cold
check:
  question: |-
    An ideal gas in a bowling machine's cylinder is supplied with heat. In which kind of process does all of the heat supplied go into work done by the gas?
  options:
    A: |-
      Adiabatic, because the gas exchanges no heat with its surroundings.
    B: |-
      Isothermal, because the internal energy of the gas does not change.
    C: |-
      Isochoric, because the volume is held fixed while heat goes in.
    D: |-
      Isobaric, because the gas pushes the piston at a steady pressure.
  answer: B
  explanation: |-
    At constant temperature an ideal gas's internal energy is unchanged, $\Delta U = 0$, so the first law gives $\Delta Q = \Delta W$: all the heat supplied comes out as work.
  misconceptions:
    A: |-
      Confuses "no heat exchanged" with "all heat turned into work". In an adiabatic process $\Delta Q = 0$, so there is no heat supplied to convert; the work comes from internal energy.
    C: |-
      At constant volume the gas does no work at all ($\Delta W = 0$); all the heat goes into internal energy, the opposite of the claim.
    D: |-
      At constant pressure the gas does work $p\,\Delta V$, but its temperature rises too, so only part of the heat becomes work and the rest raises $U$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A hot afternoon at a cricket ground: blazing sun, a board showing 38 degrees, a bowler polishing the ball, a generator with hot exhaust and an ice box of drinks](scenes/cricket/thermodynamics.svg "A hot day at the ground, but the surprises in this story come from air being squeezed and released.")

Before evening nets, the groundsman, Gurpreet, has to fill the bowling machine's air reservoir using a hand pump. He's in a hurry, so he pumps fast: forty quick strokes. When he's done, Anika, the youngest player in the squad, grabs the pump to move it and yelps. The bottom of the barrel is hot.

"There's no flame in there," she says. "How did it heat up?"

Ten minutes later she gets a second surprise. Gurpreet lets some air out through the bleed valve in one long hiss, and when Anika touches the valve, it feels cold.

The next day, Gurpreet pumps slowly, taking his time between strokes. The barrel barely warms at all.

Same air, same pump. Squeezing it can heat it, letting it rush out can cool it, and doing it slowly changes everything. What decides which happens?

## The physics

Every change a gas goes through is a **process**, and the first law $\Delta Q = \Delta U + \Delta W$ applies to all of them. What differs is which quantity is held fixed. For an ideal gas, $U$ depends only on temperature, and the work is the area under the $p$–$V$ curve.

![A p-V diagram with four processes starting from the same state A: a horizontal isobaric line, a vertical isochoric line, a falling isothermal curve and a steeper falling adiabatic curve](figures/thermodynamic_processes/four-processes-pv.svg "From the same start: isobaric is flat, isochoric is vertical, and the adiabatic curve falls more steeply than the isothermal one.")

**Isothermal** (constant temperature). The gas is in good thermal contact with its surroundings and changes slowly. $pV = \text{constant}$. Since $T$ is fixed, $\Delta U = 0$, so $\Delta Q = \Delta W$. For $\mu$ moles expanding from $V_1$ to $V_2$ at temperature $T$:
$$W = \mu R T \ln\frac{V_2}{V_1}$$
Gurpreet's slow pumping is close to this: heat has time to leak out, so the air barely warms.

**Adiabatic** (no heat exchanged, $\Delta Q = 0$). The gas is insulated, or the change is too fast for heat to flow. Then $\Delta U = -\Delta W$, and $pV^\gamma = \text{constant}$, where $\gamma = C_p/C_v$ (about $1.4$ for air). Compressing the gas ($\Delta W < 0$) raises $U$, so it heats: the fast pump. Expanding it ($\Delta W > 0$) lowers $U$, so it cools: the hissing valve. For work done by the gas, $W = \dfrac{\mu R (T_1 - T_2)}{\gamma - 1}$. The adiabatic curve is steeper than the isothermal one because pressure falls both from expansion and from cooling.

**Isochoric** (constant volume). $\Delta W = 0$, so $\Delta Q = \Delta U$: all heat goes into internal energy. Air in the machine's rigid reservoir warming in the sun is isochoric.

**Isobaric** (constant pressure). $W = p(V_2 - V_1)$, and $\Delta Q = \Delta U + p\,\Delta V$: heat is shared between warming the gas and doing work.

**Cyclic.** The gas returns to its starting state, so $\Delta U = 0$ over the cycle and the net heat absorbed equals the net work done, which is the area enclosed by the loop on the $p$–$V$ diagram.

## Worked example

**Given (illustrative):** $\mu = 0.20\,\text{mol}$ of air, $R = 8.314\,\text{J mol}^{-1}\text{K}^{-1}$.
(a) It expands isothermally at $300\,\text{K}$ from $2.0\,\text{L}$ to $4.0\,\text{L}$.
(b) Air in the rigid reservoir absorbs $150\,\text{J}$ from the sun.
(c) One fast pump stroke does $90\,\text{J}$ of work on the air, with no time for heat to escape.
**Find:** $\Delta Q$, $\Delta W$ and $\Delta U$ for each.

(a) $W = \mu RT \ln(V_2/V_1) = 0.20 \times 8.314 \times 300 \times \ln 2 = 498.8 \times 0.693 \approx 346\,\text{J}$. $\Delta U = 0$, so $\Delta Q = 346\,\text{J}$.

(b) Isochoric: $\Delta W = 0$, $\Delta Q = +150\,\text{J}$, so $\Delta U = +150\,\text{J}$.

(c) Adiabatic: $\Delta Q = 0$, $\Delta W = -90\,\text{J}$, so $\Delta U = 0 - (-90) = +90\,\text{J}$. The air heats up: Anika's hot pump.

**Sanity check for (a):** the volume doubled at constant temperature, so the pressure halved; the work, $346\,\text{J}$, lies between $p_2\,\Delta V$ and $p_1\,\Delta V$ ($\mu RT/V_1 = 2.49 \times 10^5\,\text{Pa}$, so these are about $249\,\text{J}$ and $499\,\text{J}$).

## Where the picture breaks

Real processes are only close to these ideals. No pump stroke is perfectly adiabatic or perfectly isothermal; the truth lies between, depending on speed. Part of the pump's heat also comes from friction between the piston and barrel, which the ideal-gas model ignores. The cold valve involves air escaping, so the amount of gas is not fixed. The trend is right: fast squeezing warms the gas, fast expansion cools it.

## Key takeaway

Apply $\Delta Q = \Delta U + \Delta W$ with one quantity fixed. Isothermal: $\Delta U = 0$, so $\Delta Q = \Delta W$. Adiabatic: $\Delta Q = 0$, so compression heats and expansion cools. Isochoric: $\Delta W = 0$, so $\Delta Q = \Delta U$. Isobaric: $W = p\,\Delta V$. Cyclic: $\Delta U = 0$, and net work is the enclosed area.
