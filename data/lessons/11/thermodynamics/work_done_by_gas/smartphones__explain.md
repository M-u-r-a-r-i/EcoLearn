---
concept_id: work_done_by_gas
interest: smartphones
format: explain
title: The work hidden in every stroke of a cordless tyre inflator
check:
  question: |-
    In a school lab, gas in a cylinder with a freely sliding piston is warmed gently. Aditya films the piston with his phone to read off the volume. The pressure stays at $2.0 \times 10^5\,\text{Pa}$ while the volume grows from $50\,\text{mL}$ to $150\,\text{mL}$. How much work does the gas do?
  options:
    A: |-
      $20\,\text{J}$
    B: |-
      $30\,\text{J}$
    C: |-
      $2.0 \times 10^4\,\text{J}$
    D: |-
      $0\,\text{J}$
  answer: A
  explanation: |-
    At constant pressure the area under the $p$–$V$ graph is a rectangle: $W = p\,\Delta V = (2.0 \times 10^5)(1.0 \times 10^{-4}) = 20\,\text{J}$, since $\Delta V = 100\,\text{mL} = 1.0 \times 10^{-4}\,\text{m}^3$.
  misconceptions:
    B: |-
      Uses the final volume instead of the change in volume, computing $pV_2$ rather than $p\,\Delta V$. Work depends on how much the volume changes, not on how big it ends up.
    C: |-
      Converts millilitres as if they were litres ($1\,\text{mL} = 10^{-3}\,\text{m}^3$). In fact $1\,\text{mL} = 10^{-6}\,\text{m}^3$, so this answer is 1000 times too large.
    D: |-
      Thinks work needs the pressure to change. At constant pressure the gas still pushes the piston through a distance, so it does work.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A sunny room: a phone sealed in a puffed-up waterproof pouch on a windowsill, a phone charging on a desk seen through a clip-on thermal camera, an icy can of compressed air, and a wall air conditioner controlled from a phone app](scenes/smartphones/thermodynamics.svg "Gas and gadgets: from the puffed-up pouch to the can of compressed air, gases pushing and being pushed.")

Aryan's bicycle tyre is flat again, but this time he has a new toy: a cordless tyre inflator that pairs with his phone. He types the target pressure into the app, screws the hose onto the valve, and presses start. The little machine rattles away, the pressure on the screen creeps up, and it switches itself off when it gets there.

His sister Meenal picks it up afterwards and nearly drops it. "It's hot! And your battery went from full to 80% for one tyre."

"There's a tiny piston inside," says Aryan, "going up and down, squeezing air into the tyre. That takes work."

"How much work, though?" asks Meenal. "Force times distance, fine. But the air pushes back harder the more you squeeze it. Which force do you use?"

How do you add up the work on a gas whose push keeps changing?

## The physics

Picture gas in a cylinder closed by a piston of area $A$. The gas at pressure $p$ pushes on the piston with a force $F = pA$. If the piston moves out a small distance $\Delta x$, the gas does work

$$\Delta W = F\,\Delta x = pA\,\Delta x = p\,\Delta V$$

because $A\,\Delta x$ is the small increase in volume, $\Delta V$.

![A gas at pressure p pushes a piston of area A outward by a small distance delta x](figures/work_done_by_gas/piston-small-expansion.svg "The gas's force pA acts through the piston's small move; the volume grows by A times delta x.")

If the pressure changes, split the change into many small steps, each with nearly constant $p$, and add them up. In the limit this is an integral:

$$W = \int_{V_1}^{V_2} p\,dV$$

On a **$p$–$V$ diagram** (pressure up the side, volume along the bottom), that integral is the **area under the curve** between $V_1$ and $V_2$. Three rules follow:

- The gas expands ($V$ increases): $W$ is positive; the gas does work on its surroundings.
- The gas is compressed ($V$ decreases): $W$ is negative; the surroundings do work on the gas. That is the inflator's squeeze.
- The volume stays fixed: $W = 0$, however much the pressure changes.

Units: pascals times cubic metres gives $\text{N/m}^2 \times \text{m}^3 = \text{N m} = \text{J}$. Always convert first: $1\,\text{L} = 10^{-3}\,\text{m}^3$ and $1\,\text{mL} = 10^{-6}\,\text{m}^3$.

The area picture also shows that **work depends on the path**, not just on where the gas starts and ends.

![A p-V diagram with three paths from A (1 L, 3 x 10^5 Pa) to B (3 L, 1 x 10^5 Pa): an upper path giving 600 J, a straight line giving 400 J and a lower path giving 200 J](figures/work_done_by_gas/three-paths-a-to-b.svg "Same start, same end: a path that keeps the pressure high encloses more area, so the gas does more work.")

## Worked example

**Given (illustrative):** in one squeeze, the inflator's piston shrinks the air in its cylinder from $30\,\text{mL}$ to $10\,\text{mL}$, and the pressure rises in a straight line on the $p$–$V$ diagram from $1.0 \times 10^5\,\text{Pa}$ (ordinary air pressure) to $3.0 \times 10^5\,\text{Pa}$.
**Find:** the work done by the air.

**Step 1: the change in volume, in SI units.** The volume falls by $20\,\text{mL}$:

$$\Delta V = -20\,\text{mL} = -20 \times 10^{-6}\,\text{m}^3 = -2 \times 10^{-5}\,\text{m}^3$$

It is negative because the air is being squeezed.

**Step 2: the average pressure.** The area under a straight line is a trapezium, which equals the average height times the width:

$$p_\text{avg} = \frac{1.0 + 3.0}{2} \times 10^5 = 2.0 \times 10^5\,\text{Pa}$$

**Step 3: the work.**

$$W = p_\text{avg}\,\Delta V = 2.0 \times 10^5 \times (-2 \times 10^{-5}) = -4\,\text{J}$$

The air does $-4\,\text{J}$ of work: in plain words, the piston does $4\,\text{J}$ of work *on* the air. That is about the energy needed to lift a phone two metres, spent on every single stroke, many times a second, which is why the battery drains and the cylinder heats up.

**Sanity check:** the pressure was always between $1$ and $3 \times 10^5\,\text{Pa}$, so the size of the work must lie between $2\,\text{J}$ and $6\,\text{J}$; $4\,\text{J}$ sits right in the middle, as a straight line should give.

## Where the picture breaks

This is a simplified model, not any real inflator's data. A fast squeeze does not raise the pressure along a straight line; it follows a curve that gets steeper as the air heats up, so you would need the true area under that curve. Real inflators also open a valve partway through each stroke, pushing air into the tyre, which changes the shape of the path again. The formula assumes the air has one pressure throughout at every instant, which is only roughly true when the piston moves fast. And the battery's energy does not all reach the air: the motor, the gears and the piston's friction waste some as heat too.

## Key takeaway

A gas does work $\Delta W = p\,\Delta V$ when its volume changes a little; for any change, $W = \int p\,dV$, the area under the $p$–$V$ curve. Expansion gives positive work, compression negative, fixed volume zero, and the amount depends on the path. Convert millilitres and litres to cubic metres before you multiply.
