---
concept_id: thermodynamic_processes
interest: motorsport
format: explain
title: Why a diesel engine needs no spark plug
check:
  question: |-
    On the out-lap, the air sealed inside a race tyre absorbs $120\,\text{J}$ of heat from the warming rubber. Treat the tyre's volume as fixed. Which statement about the air is correct?
  options:
    A: |-
      $\Delta U = 0$, because the heat going in is balanced by the air doing $120\,\text{J}$ of work.
    B: |-
      $\Delta U = 0$, because no work is done, so the internal energy cannot change.
    C: |-
      $\Delta U = +120\,\text{J}$, and the air also does $120\,\text{J}$ of work pushing on the tyre.
    D: |-
      $\Delta U = +120\,\text{J}$, because at fixed volume $\Delta W = 0$ and all the heat raises the internal energy.
  answer: D
  explanation: |-
    This is an isochoric process: the volume does not change, so $\Delta W = 0$ and the first law gives $\Delta U = \Delta Q = +120\,\text{J}$. The air gets hotter, which is why the tyre's pressure rises.
  misconceptions:
    A: |-
      Treats it as isothermal. The air is not held at constant temperature, and with no change in volume it cannot do any work, so the heat cannot leave as work.
    B: |-
      Thinks internal energy can change only through work. Heat is the other way to change it; with $\Delta W = 0$, all of $\Delta Q$ goes into $\Delta U$.
    C: |-
      Counts the same $120\,\text{J}$ twice. Energy is conserved: it cannot all raise $U$ and also all come out as work, and at fixed volume the work is zero anyway.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A pit lane in the afternoon sun: a stack of tyres in electric tyre blankets with a probe thermometer, a race car with a glowing front brake disc and a hot exhaust, and a compressed-air bottle feeding a wheel gun](scenes/motorsport/thermodynamics.svg "On the right: the air bottle that powers the wheel gun. Watch what happens to air that rushes out of it.")

Kavya has just joined a truck-racing team as a trainee mechanic, and on her first morning she asks Suresh, the engine specialist, where the spark plugs are.

"There aren't any," he says. "It's a diesel. We squeeze the air so hard and so fast that it gets hot enough to set the fuel alight all by itself."

Kavya doesn't believe him. Squeezing something makes it hot enough to burn?

At the pit stop practice that afternoon she gets a second surprise. After a dozen wheel changes, she touches the exhaust port of the air-powered wheel gun. It's cold, much colder than the air around it.

And when she asks why the gun's big air bottle doesn't go cold as well, Suresh says: "It does, if you empty it in a rush. Let it out slowly and it barely changes."

Squeezing air can heat it, letting it rush out can cool it, and doing it slowly changes everything. What decides which happens?

## The physics

Every change a gas goes through is a **process**, and the first law $\Delta Q = \Delta U + \Delta W$ applies to all of them. What differs is which quantity is held fixed. For an ideal gas, $U$ depends only on temperature, and the work is the area under the $p$–$V$ curve.

![A p-V diagram with four processes starting from the same state A: a horizontal isobaric line, a vertical isochoric line, a falling isothermal curve and a steeper falling adiabatic curve](figures/thermodynamic_processes/four-processes-pv.svg "From the same start: isobaric is flat, isochoric is vertical, and the adiabatic curve falls more steeply than the isothermal one.")

**Isothermal** (constant temperature). The gas is in good thermal contact with its surroundings and changes slowly, so $pV = \text{constant}$. Since $T$ is fixed, $\Delta U = 0$, so $\Delta Q = \Delta W$: all the heat taken in comes out as work. For $\mu$ moles going from $V_1$ to $V_2$ at temperature $T$, $W = \mu R T \ln(V_2/V_1)$. Letting the air bottle out slowly is close to this.

**Adiabatic** (no heat exchanged, $\Delta Q = 0$). The gas is insulated, or the change is too fast for heat to flow. Then $\Delta U = -\Delta W$, and $pV^\gamma = \text{constant}$, where $\gamma = C_p/C_v$ (about $1.4$ for air). Compressing the gas ($\Delta W < 0$) raises $U$, so it heats: the diesel's compression stroke. Expanding it ($\Delta W > 0$) lowers $U$, so it cools: the wheel gun's cold exhaust. The adiabatic curve is steeper than the isothermal one because the pressure falls both from expanding and from cooling.

**Isochoric** (constant volume). $\Delta W = 0$, so $\Delta Q = \Delta U$: all the heat goes into internal energy. Air sealed in a stiff tyre, warmed by the rubber, is nearly isochoric.

**Isobaric** (constant pressure). $W = p(V_2 - V_1)$, and $\Delta Q = \Delta U + p\,\Delta V$: heat is shared between warming the gas and doing work.

**Cyclic.** The gas returns to its starting state, so $\Delta U = 0$ over the cycle, and the net heat absorbed equals the net work done: the area enclosed by the loop on the $p$–$V$ diagram. Every engine runs in cycles.

## Worked example

**Given (illustrative):** for each case, find $\Delta Q$, $\Delta W$ and $\Delta U$ for the gas.
(a) Air in the rigid air bottle, left in the sun, absorbs $200\,\text{J}$.
(b) One diesel compression stroke does $500\,\text{J}$ of work on the air, too fast for heat to escape.
(c) Gas expands slowly at constant temperature, doing $150\,\text{J}$ of work.

**(a) Isochoric.** $\Delta W = 0$ and $\Delta Q = +200\,\text{J}$, so $\Delta U = +200\,\text{J}$. The bottle's air warms and its pressure rises.

**(b) Adiabatic.** $\Delta Q = 0$ and $\Delta W = -500\,\text{J}$, so $\Delta U = 0 - (-500) = +500\,\text{J}$. All the piston's work stays in the air as internal energy, which is why the air ends up hot enough to ignite the diesel fuel.

**(c) Isothermal.** $\Delta U = 0$ and $\Delta W = +150\,\text{J}$, so $\Delta Q = +150\,\text{J}$. To do work without cooling down, the gas has to draw exactly as much heat from its surroundings.

**Sanity check:** in each case, $\Delta Q$ equals $\Delta U + \Delta W$: $200 = 200 + 0$, $0 = 500 - 500$, $150 = 0 + 150$.

## Where the picture breaks

Real processes are only close to these ideals. No compression stroke is perfectly adiabatic (a little heat always leaks into the cylinder walls), and no "slow" release is perfectly isothermal; the truth lies between, depending on speed. A tyre's volume grows slightly as it warms, so it isn't exactly isochoric either. The wheel gun and the emptying bottle involve air flowing out, so the amount of gas is not fixed. The trend is right all the same: fast squeezing heats a gas, fast expansion cools it, and slow changes let heat flow to keep the temperature steady.

## Key takeaway

Apply $\Delta Q = \Delta U + \Delta W$ with one quantity fixed. Isothermal: $\Delta U = 0$, so $\Delta Q = \Delta W$. Adiabatic: $\Delta Q = 0$, so compression heats and expansion cools. Isochoric: $\Delta W = 0$, so $\Delta Q = \Delta U$. Isobaric: $W = p\,\Delta V$. Cyclic: $\Delta U = 0$, and the net work is the area enclosed.
