---
concept_id: work_done_by_gas
interest: cricket
format: explain
title: The work behind an air-cannon bowling machine
check:
  question: |-
    In a bowling machine's cylinder, air expands at a constant pressure of $1.5 \times 10^5\,\text{Pa}$ from $2.0\,\text{L}$ to $5.0\,\text{L}$. How much work does the air do?
  options:
    A: |-
      $450\,\text{J}$
    B: |-
      $4.5 \times 10^5\,\text{J}$
    C: |-
      $750\,\text{J}$
    D: |-
      $0\,\text{J}$
  answer: A
  explanation: |-
    At constant pressure the area under the $p$–$V$ graph is a rectangle: $W = p\,\Delta V = (1.5 \times 10^5)(3.0 \times 10^{-3}) = 450\,\text{J}$, since $3.0\,\text{L} = 3.0 \times 10^{-3}\,\text{m}^3$.
  misconceptions:
    B: |-
      Multiplies by $3.0$ litres without converting to cubic metres ($1\,\text{L} = 10^{-3}\,\text{m}^3$), giving an answer 1000 times too large.
    C: |-
      Uses the final volume instead of the change in volume, computing $pV$ rather than $p\,\Delta V$. Work depends on how much the volume changes.
    D: |-
      Thinks work needs a change in pressure. At constant pressure the gas still pushes the piston through a distance, so it does work.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A hot afternoon at a cricket ground: blazing sun, a board showing 38 degrees, a bowler polishing the ball, a generator with hot exhaust and an ice box of drinks](scenes/cricket/thermodynamics.svg "A hot training day. Away from this square, in the academy nets, compressed air does the bowling.")

At a cricket academy on the edge of the city, Vikram is facing a bowling machine for the first time. This one works on compressed air: a pump fills a cylinder, and when the coach, Neha, presses the trigger, the air expands and drives a piston that launches the ball down the net.

Every time it fires, Vikram hears a sharp *thump*, and the needle on the pressure gauge drops back. Between balls he asks the obvious question. "Where does the energy come from? Nothing's burning. There's just air in there."

Neha taps the gauge. "The air is pushing. Pushing through a distance is work. Tell me how much work the air does in one shot, and I'll tell you why only part of it ends up in the ball."

Vikram looks at the gauge again. The pressure isn't even steady; it falls as the air expands. How do you calculate the work done by a push that keeps weakening?

## The physics

Picture the gas in a cylinder closed by a piston of area $A$. The gas at pressure $p$ pushes on the piston with a force $F = pA$. If the piston moves out by a small distance $\Delta x$, the gas does work

$$\Delta W = F\,\Delta x = pA\,\Delta x = p\,\Delta V$$

because $A\,\Delta x$ is the small increase in volume $\Delta V$.

![A gas at pressure p pushes a piston of area A outward by a small distance delta x](figures/work_done_by_gas/piston-small-expansion.svg "The gas's force pA acts through the piston's small move; the volume grows by A times delta x.")

If the pressure changes during the expansion, split it into many small steps, each with nearly constant $p$, and add them up. In the limit this is an integral:

$$W = \int_{V_1}^{V_2} p\,dV$$

On a **$p$–$V$ diagram** (pressure up the side, volume along the bottom), that integral is the **area under the curve** between $V_1$ and $V_2$. Three rules follow:

- The gas expands ($V$ increases): $W$ is positive; the gas does work on its surroundings.
- The gas is compressed ($V$ decreases): $W$ is negative; the surroundings do work on the gas.
- The volume stays fixed: $W = 0$, however much the pressure changes.

Units: pressure in pascals times volume in cubic metres gives $\text{N/m}^2 \times \text{m}^3 = \text{N m} = \text{J}$. Always convert litres first: $1\,\text{L} = 10^{-3}\,\text{m}^3$.

The area also shows that **work depends on the path**, not just on the start and end states.

![A p-V diagram with three paths from A (1 L, 3 x 10^5 Pa) to B (3 L, 1 x 10^5 Pa): an upper path giving 600 J, a straight line giving 400 J and a lower path giving 200 J](figures/work_done_by_gas/three-paths-a-to-b.svg "Same start, same end; the area under each path, and so the work, is different.")

## Worked example

**Given:** in one shot (illustrative numbers), the air in the cylinder expands from $V_1 = 1.0\,\text{L}$ at $p_1 = 3.0 \times 10^5\,\text{Pa}$ to $V_2 = 3.0\,\text{L}$ at $p_2 = 1.0 \times 10^5\,\text{Pa}$, with the pressure falling in a straight line on the $p$–$V$ diagram (the blue path above).
**Find:** the work done by the air.

The area under a straight line is a trapezium: average pressure times the change in volume.

$$\Delta V = 3.0 - 1.0 = 2.0\,\text{L} = 2.0 \times 10^{-3}\,\text{m}^3$$

$$W = \frac{p_1 + p_2}{2}\,\Delta V = \frac{(3.0 + 1.0) \times 10^5}{2} \times 2.0 \times 10^{-3} = 2.0 \times 10^5 \times 2.0 \times 10^{-3} = 400\,\text{J}$$

**Sanity check:** the answer must lie between the constant-pressure bounds $1.0 \times 10^5 \times 2.0 \times 10^{-3} = 200\,\text{J}$ and $3.0 \times 10^5 \times 2.0 \times 10^{-3} = 600\,\text{J}$. It does: $400\,\text{J}$, halfway, as a straight line should give.

## Where the picture breaks

This is a simplified model, not any real machine's design. The formula assumes the gas has a single, well-defined pressure throughout at every instant; in a fast shot the pressure is uneven, and we are using an idealised, slow version. Nor does all $400\,\text{J}$ reach the ball. The piston also has to shove the outside air out of its way: at atmospheric pressure, about $10^5\,\text{Pa} \times 2.0 \times 10^{-3}\,\text{m}^3 = 200\,\text{J}$. Friction and the piston's own motion take more. A $0.16\,\text{kg}$ ball leaving at, say, $30\,\text{m/s}$ carries only $\tfrac{1}{2}(0.16)(30)^2 = 72\,\text{J}$.

## Key takeaway

A gas does work $\Delta W = p\,\Delta V$ when it expands a little; for any expansion, $W = \int p\,dV$, the area under the $p$–$V$ curve. Expansion gives positive work, compression negative, fixed volume zero, and the amount depends on the path taken. Convert litres to cubic metres before you multiply.
