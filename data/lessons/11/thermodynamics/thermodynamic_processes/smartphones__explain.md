---
concept_id: thermodynamic_processes
interest: smartphones
format: explain
title: Why the inflator gets hot but the slow syringe doesn't
check:
  question: |-
    A small sealed metal can of gas, used in a gadget's cooling test, is rigid, so its volume cannot change. Left in sunlight, the gas inside absorbs $50\,\text{J}$ of heat. Taking $\Delta W$ as the work done by the gas, which is correct?
  options:
    A: |-
      $\Delta U = 0$ and $\Delta W = 50\,\text{J}$
    B: |-
      $\Delta U = 50\,\text{J}$ and $\Delta W = 0$
    C: |-
      $\Delta U = 25\,\text{J}$ and $\Delta W = 25\,\text{J}$
    D: |-
      $\Delta U = 0$ and $\Delta W = 0$
  answer: B
  explanation: |-
    The volume is fixed, so the process is isochoric and $\Delta W = 0$. The first law then gives $\Delta U = \Delta Q = 50\,\text{J}$: all the heat goes into internal energy, and the gas gets hotter.
  misconceptions:
    A: |-
      Confuses isochoric with isothermal, as if heat taken in must come out as work. With the volume fixed, the gas cannot push anything, so it does no work.
    C: |-
      Assumes heat is always shared between internal energy and work. That sharing happens only when the volume changes; here there is nothing for the gas to push.
    D: |-
      Thinks a sealed container exchanges no energy, confusing sealed (no gas gets in or out) with adiabatic (no heat gets in or out). Heat passes through the metal walls easily.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A sunny room: a phone sealed in a puffed-up waterproof pouch on a windowsill, a phone charging on a desk seen through a clip-on thermal camera, an icy can of compressed air, and a wall air conditioner controlled from a phone app](scenes/smartphones/thermodynamics.svg "A room of gas processes: a pouch swelling in the sun, a sealed can, air squeezed and released.")

Kabir is pumping up his football with a cordless inflator before evening practice. The app on his phone shows the pressure climbing; the motor whines for a couple of minutes, then stops. When he unscrews the hose, the metal barrel at the end of the inflator is almost too hot to hold.

"Friction," says his cousin Riya. "All those moving parts."

"Some of it," says Kabir, who has just done a lab on gases. "But the air itself gets hot when you squeeze it. That's what the teacher said."

"Then why didn't the syringe get hot in your lab? You sealed the end, pushed the plunger in as far as it would go, and it stayed cold. You told me so."

Kabir thinks. Same air. Same squeeze, more or less. The only difference he can find is that in the lab he pushed slowly, and the inflator squeezes many times a second.

Why should *speed* decide whether squeezed air heats up?

## The physics

Every change a gas goes through is a **process**, and the first law $\Delta Q = \Delta U + \Delta W$ applies to all of them. What differs is which quantity is held fixed. For an ideal gas, $U$ depends only on temperature, and the work is the area under the $p$–$V$ curve.

![A p-V diagram with four processes starting from the same state A: a horizontal isobaric line, a vertical isochoric line, a falling isothermal curve and a steeper falling adiabatic curve](figures/thermodynamic_processes/four-processes-pv.svg "From the same start: isobaric is flat, isochoric is vertical, and the adiabatic curve falls more steeply than the isothermal one.")

**Isothermal** (constant temperature). The gas is in good thermal contact with its surroundings and changes slowly, so $pV = \text{constant}$. Since $T$ is fixed, $\Delta U = 0$, so $\Delta Q = \Delta W$. When the gas is squeezed slowly, the energy the piston puts in leaks out as heat as fast as it arrives. That is Kabir's lab syringe.

**Adiabatic** (no heat exchanged, $\Delta Q = 0$). The gas is insulated, or the change is too fast for heat to flow. Then $\Delta U = -\Delta W$, and $pV^\gamma = \text{constant}$, where $\gamma = C_p/C_v$ (about $1.4$ for air). Squeezing the gas ($\Delta W < 0$) raises $U$, so it heats: the inflator's fast strokes. Letting it expand quickly ($\Delta W > 0$) lowers $U$, so it cools. The adiabatic curve is steeper than the isothermal one because the pressure changes both from the volume change and from the temperature change.

**Isochoric** (constant volume). $\Delta W = 0$, so $\Delta Q = \Delta U$: all the heat goes into internal energy. Gas sealed in a rigid can, warmed by the sun, is isochoric.

**Isobaric** (constant pressure). $W = p(V_2 - V_1)$, and $\Delta Q = \Delta U + p\,\Delta V$: heat is shared between warming the gas and doing work. A floppy pouch of air swelling in the sun is close to this.

**Cyclic.** The gas returns to its starting state, so $\Delta U = 0$ over the cycle, and the net heat absorbed equals the net work done: the area enclosed by the loop on the $p$–$V$ diagram. The refrigerant in every fridge and air conditioner runs in a cycle.

## Worked example

**Given (illustrative):** in each case, $20\,\text{J}$ of energy crosses the boundary of some air.
(a) The inflator squeezes air so fast that no heat escapes: $20\,\text{J}$ of work is done on it.
(b) The lab syringe is squeezed slowly at constant temperature: again $20\,\text{J}$ of work is done on it.
(c) Air in a rigid sealed can absorbs $20\,\text{J}$ of heat from the sun.
**Find:** $\Delta U$ in each case, and whether the air warms.

**Step 1: adiabatic.** $\Delta Q = 0$ and $\Delta W = -20\,\text{J}$ (work done *on* the gas), so

$$\Delta U = \Delta Q - \Delta W = 0 - (-20) = +20\,\text{J}$$

All the work stays in the air, and it heats up.

**Step 2: isothermal.** $T$ is fixed, so $\Delta U = 0$. Then $\Delta Q = \Delta W = -20\,\text{J}$: the air hands $20\,\text{J}$ of heat to the syringe and Kabir's fingers, and stays cool.

**Step 3: isochoric.** The volume cannot change, so $\Delta W = 0$ and $\Delta U = \Delta Q = +20\,\text{J}$. The air heats, with no squeezing at all.

**Sanity check:** the same $20\,\text{J}$ gave three different outcomes, and in each case it was the quantity held fixed (heat, temperature or volume) that decided where the energy went.

## Where the picture breaks

Real processes are never exactly any of these. The inflator's air loses a little heat to the cylinder walls even on a fast stroke, so it is only nearly adiabatic; and friction in the pump heats the barrel too, as Riya said, so the heat Kabir felt came from both. The lab syringe was never perfectly isothermal: it warmed very slightly before the heat leaked away. "Isothermal" and "adiabatic" are ideal limits, slow and fast, and real devices sit somewhere between them. The numbers are illustrative, not measurements of any inflator.

## Key takeaway

Isothermal: $\Delta U = 0$, so $\Delta Q = \Delta W$. Adiabatic: $\Delta Q = 0$, so $\Delta U = -\Delta W$, and squeezed gas heats. Isochoric: $\Delta W = 0$, so $\Delta Q = \Delta U$. Isobaric: $W = p\,\Delta V$. Cyclic: $\Delta U = 0$, and net work is the area of the loop. Whether a fast or slow change is adiabatic or isothermal depends on whether heat has time to flow.
