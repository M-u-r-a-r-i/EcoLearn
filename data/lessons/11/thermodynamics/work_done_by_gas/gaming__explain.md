---
concept_id: work_done_by_gas
interest: gaming
format: explain
title: The trapped gas that lifts your chair back up
check:
  question: |-
    The gas in a chair's cylinder is taken from $(0.20\,\text{L},\ 3.0 \times 10^5\,\text{Pa})$ to $(0.40\,\text{L},\ 1.0 \times 10^5\,\text{Pa})$ along a straight line on the $p$–$V$ diagram. How much work does the gas do?
  options:
    A: |-
      $60\,\text{J}$
    B: |-
      $20\,\text{J}$
    C: |-
      $4.0 \times 10^4\,\text{J}$
    D: |-
      $40\,\text{J}$
  answer: D
  explanation: |-
    The area under a straight line is the average pressure times the change in volume: $\bar{p} = \tfrac{1}{2}(3.0 + 1.0) \times 10^5 = 2.0 \times 10^5\,\text{Pa}$ and $\Delta V = 0.20\,\text{L} = 2.0 \times 10^{-4}\,\text{m}^3$, so $W = 40\,\text{J}$.
  misconceptions:
    A: |-
      Uses the starting pressure for the whole expansion, $3.0 \times 10^5 \times 2.0 \times 10^{-4}$. The pressure falls as the gas expands, so this overestimates the area under the curve.
    B: |-
      Uses the final pressure for the whole expansion. That is the *lowest* pressure of the process, so it underestimates the area.
    C: |-
      Never converts litres to cubic metres ($1\,\text{L} = 10^{-3}\,\text{m}^3$), so the answer comes out a thousand times too large.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor showing GPU and CPU temperatures, a tower PC with a heat sink and fans, hot air leaving the top and cool air drawn in, a can of compressed-air duster, a mini fridge under the desk and a backup generator outside the window](scenes/gaming/thermodynamics.svg "Everything at this desk needs energy from somewhere — including the chair you are sitting on.")

Aarav's chair has developed a habit. Twenty minutes into any session it sinks, slowly, until he is squinting up at the monitor from somewhere near the level of the desk drawer. So he does what everyone does: stands up a little, reaches under the seat, pulls the lever, lets the seat spring back to full height, and carries on.

His sister Tara, waiting for her turn, watches him do it for the fourth time in one evening.

"Where's the push coming from?" she asks. "You're not lifting it. You're not winding anything up. You pull a lever and let go, and it rises."

Aarav has never thought about it. He tips the chair over and slides off the plastic sleeve at the base. Underneath is a sealed metal cylinder with a thin rod sliding in and out of it. No motor. No battery. No visible spring. Stamped along the side are two words: *gas pressure*.

So a bottle of trapped gas can lift a seat by itself. How much work does a gas actually do when it pushes?

## The physics

Picture gas sealed in a cylinder behind a piston of area $A$. The gas at pressure $p$ presses on the piston with a force $F = pA$. Let the piston move out by a small distance $\Delta x$. The gas does work

$$\Delta W = F\,\Delta x = pA\,\Delta x = p\,\Delta V$$

because $A\,\Delta x$ is exactly the small increase in volume, $\Delta V$.

![A gas at pressure p pushes a piston of area A outward by a small distance delta x](figures/work_done_by_gas/piston-small-expansion.svg "Force times distance, rewritten: the gas's force pA acting through the piston's small move is the same as p times the extra volume.")

If the pressure changes during the expansion — and in a real cylinder it always does, because the gas gets more room — then split the change into many small steps, each with $p$ nearly constant, and add them up. In the limit that is an integral:

$$W = \int_{V_1}^{V_2} p\,dV$$

On a **$p$–$V$ diagram**, with pressure up the side and volume along the bottom, that integral is the **area under the curve** between $V_1$ and $V_2$. Three consequences follow at once:

- The gas expands, so $V$ increases: $W$ is positive and the gas does work on its surroundings. Aarav's chair.
- The gas is compressed, so $V$ decreases: $W$ is negative — the surroundings do work on the gas. Aarav's weight pushing the seat down.
- The volume does not change: $W = 0$, no matter how much the pressure changes.

Units: pascals times cubic metres is $\text{N/m}^2 \times \text{m}^3 = \text{N m} = \text{J}$. Convert litres before you multiply: $1\,\text{L} = 10^{-3}\,\text{m}^3$.

Because the work is an *area*, it depends on the whole path, not just on where the gas starts and ends.

![A p-V diagram with three paths from A (1 L, 3 x 10^5 Pa) to B (3 L, 1 x 10^5 Pa): an upper path enclosing 600 J, a straight line giving 400 J and a lower path giving 200 J](figures/work_done_by_gas/three-paths-a-to-b.svg "Same start, same end, three different areas: 600 J, 400 J and 200 J. Work is not fixed by the end states.")

## Worked example

**Given (illustrative):** when the lever is released, the gas in Aarav's chair cylinder expands from $0.20\,\text{L}$ to $0.30\,\text{L}$, at a pressure that stays close to $2.0 \times 10^5\,\text{Pa}$.
**Find:** the work done by the gas.

First the change in volume, in SI units:

$$\Delta V = 0.30 - 0.20 = 0.10\,\text{L} = 1.0 \times 10^{-4}\,\text{m}^3$$

That is a tenth of a litre — about half a teacup of extra space inside the cylinder.

The pressure is constant, so the area under the $p$–$V$ line is just a rectangle, $p\,\Delta V$:

$$W = (2.0 \times 10^5)(1.0 \times 10^{-4}) = 20\,\text{J}$$

**Sanity check:** $20\,\text{J}$ is roughly what it takes to lift a $2\,\text{kg}$ textbook from the floor onto the desk. That is the right size for the gentle shove that sends an empty seat back up — and far too small to launch anybody out of the chair.

## Where the picture breaks

The gas in a real chair strut does not hold a steady pressure: as it expands it has more room, so its pressure falls, and the honest answer is the area under a falling curve rather than a neat rectangle. Treating the pressure as constant is an approximation, good only because the volume change here is small. Nor does all $20\,\text{J}$ end up in the seat. The piston also has to shove the outside air out of its way, which at atmospheric pressure costs about $(1.0 \times 10^5)(1.0 \times 10^{-4}) = 10\,\text{J}$, and the sliding seal takes more as friction. Real struts also contain oil to damp the motion, and some use a spring as well, so "a gas cylinder" is a simplification of the hardware — but the physics of the gas inside it is exactly this.

## Key takeaway

A gas that expands by a little does work $\Delta W = p\,\Delta V$; over any expansion, $W = \int p\,dV$, which is the area under the $p$–$V$ curve. Expansion gives positive work, compression negative, constant volume zero — and because it is an area, the answer depends on the path, not just on the end points. Convert litres to cubic metres before multiplying.
