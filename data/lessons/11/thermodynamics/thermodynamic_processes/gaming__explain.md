---
concept_id: thermodynamic_processes
interest: gaming
format: explain
title: Why a fast pump gets hot and a slow one does not
check:
  question: |-
    Imran pumps up the mattress slowly, resting between strokes, and the barrel stays close to room temperature throughout. Which process best describes the air in the barrel, and what does the first law then say about it?
  options:
    A: |-
      Adiabatic: $\Delta Q = 0$, so all the work done on the air goes into raising its internal energy.
    B: |-
      Isochoric: $\Delta W = 0$, so the heat supplied all goes into internal energy.
    C: |-
      Isothermal: $\Delta U = 0$, so the work done on the air leaves it again as heat passed to the surroundings.
    D: |-
      Isobaric: the pressure stays constant, so the work is $p\,\Delta V$ and the temperature cannot change.
  answer: C
  explanation: |-
    Slow compression in good thermal contact with the surroundings keeps the temperature constant, so for an ideal gas $\Delta U = 0$ and $\Delta Q = \Delta W$. The work done on the air is passed straight out as heat, which is why the barrel never builds up a temperature rise.
  misconceptions:
    A: |-
      Describes the *fast* stroke, not the slow one. Adiabatic means no time for heat to flow; here there is plenty of time, which is the whole point of pumping slowly.
    B: |-
      A pump barrel's volume obviously changes — that is what a pump does. Isochoric applies to a rigid sealed container, such as the duster can on a dashboard.
    D: |-
      The pressure in a pump rises as you push; it is not constant. This option also smuggles in the idea that constant pressure means constant temperature, which is false — an isobaric expansion heats the gas.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor showing GPU and CPU temperatures, a tower PC with a heat sink and fans, hot air leaving the top and cool air drawn in, a can of compressed-air duster, a mini fridge under the desk and a backup generator outside the window](scenes/gaming/thermodynamics.svg "The desk is where the evening ends; the surprises in this story happen in a pump barrel and a parked car.")

Six people, four laptops, one flat, and an all-night tournament that starts at ten. Sneha's job is the bedding, which means the two air mattresses and one foot pump.

She is in a hurry, so she pumps hard and fast: sixty strokes without stopping. When she reaches down to move the pump, the metal barrel is hot enough to make her let go.

"There's no flame in there," she says. "It's just air."

An hour later Imran inflates the second mattress. He is watching the group stage on someone's screen while he does it, so he pumps slowly, a stroke every few seconds. When he finishes, the barrel is barely warm.

Same pump, same air, same mattress. And earlier that day, the duster can that had been sitting on a parked car's dashboard sprayed harder than the one in the bag. Squeeze air and it heats; let it out and it chills; do it slowly and almost nothing happens.

What decides which?

## The physics

Every change a gas goes through is a **process**, and the first law $\Delta Q = \Delta U + \Delta W$ applies to all of them. What changes from one to the next is which quantity is held fixed. Two facts do most of the work: for an ideal gas $U$ depends only on temperature, and $\Delta W$ is the area under the $p$–$V$ curve.

![A p-V diagram with four processes starting from the same state A: a horizontal isobaric line, a vertical isochoric line, a falling isothermal curve and a steeper falling adiabatic curve](figures/thermodynamic_processes/four-processes-pv.svg "From one starting state: isobaric is flat, isochoric is vertical, and the adiabatic curve always falls more steeply than the isothermal one.")

**Isothermal** — constant temperature. The gas stays in good thermal contact with its surroundings and changes slowly enough to keep up with them. Then $pV = \text{constant}$, and since $T$ is fixed, $\Delta U = 0$, so $\Delta Q = \Delta W$. For $\mu$ moles going from $V_1$ to $V_2$ at temperature $T$:
$$W = \mu R T \ln\frac{V_2}{V_1}$$
Imran's slow pumping is close to this: every joule he puts in has time to leak out as heat, so the barrel never gains a temperature.

**Adiabatic** — no heat exchanged, $\Delta Q = 0$. Either the gas is insulated, or the change is too fast for heat to flow. Then $\Delta U = -\Delta W$, and $pV^{\gamma} = \text{constant}$ with $\gamma = C_p/C_v$, about $1.4$ for air. Compress the gas and $\Delta W$ is negative, so $U$ rises and it heats: Sneha's burning fingers. Let it expand and $\Delta W$ is positive, so $U$ falls and it chills: the duster can. For the work done by the gas, $W = \dfrac{\mu R(T_1 - T_2)}{\gamma - 1}$. The adiabatic curve is steeper than the isotherm because the pressure falls for two reasons at once — more room *and* a falling temperature.

**Isochoric** — constant volume. $\Delta W = 0$, so $\Delta Q = \Delta U$: every joule of heat goes into internal energy. The sealed duster can on the dashboard, warming in the sun inside its rigid steel, is isochoric — which is why its pressure climbs.

**Isobaric** — constant pressure. $W = p(V_2 - V_1)$, so $\Delta Q = \Delta U + p\,\Delta V$: the heat is shared between warming the gas and pushing. A chair's gas lift raising a seat against a steady load is close to this.

**Cyclic** — the gas returns to its starting state. Then $\Delta U = 0$ over the whole cycle, so the net heat absorbed equals the net work done, which is the area enclosed by the loop.

## Worked example

**Given (illustrative):** (a) one of Sneha's fast strokes does $90\,\text{J}$ of work on the air in the barrel, with no time for heat to escape; (b) the sealed duster can on the dashboard absorbs $120\,\text{J}$ of heat from the sun.
**Find:** $\Delta U$ in each case, and what happens to the temperature.

**(a) Adiabatic compression.** No heat flows, so $\Delta Q = 0$. The work is done *on* the gas, so the work done *by* it is negative: $\Delta W = -90\,\text{J}$.

$$\Delta U = \Delta Q - \Delta W = 0 - (-90) = +90\,\text{J}$$

The internal energy rises by $90\,\text{J}$, so the air gets hotter. Every joule Sneha's foot put in stayed in the gas, because there was no other way out.

**(b) Isochoric heating.** Steel will not stretch, so the volume is fixed and $\Delta W = 0$, while $\Delta Q = +120\,\text{J}$.

$$\Delta U = 120 - 0 = +120\,\text{J}$$

All of the sun's heat goes into internal energy — none of it is spent pushing anything — so the temperature, and with it the pressure, climbs. That is the harder spray.

**Sanity check:** in each case the gas kept everything it was given, because one of the two exits was shut — no heat could leave in (a), and no work could be done in (b).

## Where the picture breaks

Real processes sit somewhere between these ideals; the labels are the two extremes. No pump stroke is perfectly adiabatic and no pumping is perfectly isothermal — how close you get depends only on speed. Part of the heat in Sneha's barrel also comes from friction between the piston seal and the wall, which the ideal-gas picture leaves out entirely. The duster can's contents are usually a liquid and its vapour rather than an ideal gas, so the isochoric formula is a guide to the direction, not a precise prediction. And a can whose pressure climbs in a hot car is a real hazard, which is why the label tells you not to leave it there.

## Key takeaway

Apply $\Delta Q = \Delta U + \Delta W$ with one quantity held fixed. Isothermal: $\Delta U = 0$, so $\Delta Q = \Delta W$. Adiabatic: $\Delta Q = 0$, so compression heats and expansion cools. Isochoric: $\Delta W = 0$, so $\Delta Q = \Delta U$. Isobaric: $W = p\,\Delta V$. Cyclic: $\Delta U = 0$, and the net work is the area enclosed.
