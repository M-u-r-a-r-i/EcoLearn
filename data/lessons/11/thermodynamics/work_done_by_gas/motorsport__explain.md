---
concept_id: work_done_by_gas
interest: motorsport
format: explain
title: The push of burning gas in one engine cylinder
check:
  question: |-
    Some racing series fit cars with built-in air jacks. In one jack, compressed air expands at a constant pressure of $5.0 \times 10^5\,\text{Pa}$ from $1.0\,\text{L}$ to $3.0\,\text{L}$, pushing its piston down so the car rises. How much work does the air do?
  options:
    A: |-
      $1.5 \times 10^3\,\text{J}$
    B: |-
      $1.0 \times 10^6\,\text{J}$
    C: |-
      $0\,\text{J}$
    D: |-
      $1.0 \times 10^3\,\text{J}$
  answer: D
  explanation: |-
    At constant pressure the area under the $p$–$V$ graph is a rectangle: $W = p\,\Delta V = (5.0 \times 10^5)(2.0 \times 10^{-3}) = 1.0 \times 10^3\,\text{J}$, since $\Delta V = 2.0\,\text{L} = 2.0 \times 10^{-3}\,\text{m}^3$.
  misconceptions:
    A: |-
      Uses the final volume instead of the change in volume, computing $pV_2$ rather than $p\,\Delta V$. Work depends on how much the volume changes, not on how big it ends up.
    B: |-
      Multiplies by $2.0$ litres without converting to cubic metres ($1\,\text{L} = 10^{-3}\,\text{m}^3$), giving an answer 1000 times too large.
    C: |-
      Thinks work needs the pressure to change. At constant pressure the air still pushes the piston through a distance, so it does work.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A pit lane in the afternoon sun: a stack of tyres in electric tyre blankets with a probe thermometer, a race car with a glowing front brake disc and a hot exhaust, and a compressed-air bottle feeding a wheel gun](scenes/motorsport/thermodynamics.svg "Behind that shimmering exhaust are cylinders where hot gas pushes pistons thousands of times a minute.")

In a college workshop, the motorsport club has taken a small four-stroke engine apart on a bench. Zoya, the club's youngest member, holds a piston in one hand and its connecting rod in the other.

"So this is what actually drives the car," she says. "Fuel burns above the piston, and the hot gas shoves it down."

Their faculty adviser, Mr. Pillai, nods. "Every bit of the car's energy comes from that shove. So: how much work does the gas do in one push?"

Zoya thinks it is easy. Force times distance. The piston's area times the pressure gives the force; the stroke gives the distance.

"Which pressure?" asks Mr. Pillai. He sketches it on the whiteboard. The pressure is huge just after the spark, but as the piston slides down and the gas spreads out, it keeps falling.

How do you add up the work done by a push that keeps getting weaker?

## The physics

Picture gas in a cylinder closed by a piston of area $A$. The gas at pressure $p$ pushes on the piston with a force $F = pA$. If the piston moves out a small distance $\Delta x$, the gas does work

$$\Delta W = F\,\Delta x = pA\,\Delta x = p\,\Delta V$$

because $A\,\Delta x$ is the small increase in volume, $\Delta V$.

![A gas at pressure p pushes a piston of area A outward by a small distance delta x](figures/work_done_by_gas/piston-small-expansion.svg "The gas's force pA acts through the piston's small move; the volume grows by A times delta x.")

If the pressure changes during the expansion, split it into many small steps, each with nearly constant $p$, and add them up. In the limit this is an integral:

$$W = \int_{V_1}^{V_2} p\,dV$$

On a **$p$–$V$ diagram** (pressure up the side, volume along the bottom), that integral is the **area under the curve** between $V_1$ and $V_2$. Three rules follow:

- The gas expands ($V$ increases): $W$ is positive; the gas does work on its surroundings. That is the power stroke.
- The gas is compressed ($V$ decreases): $W$ is negative; the surroundings do work on the gas. That is the compression stroke.
- The volume stays fixed: $W = 0$, however much the pressure changes.

Units: pascals times cubic metres gives $\text{N/m}^2 \times \text{m}^3 = \text{N m} = \text{J}$. Always convert litres first: $1\,\text{L} = 10^{-3}\,\text{m}^3$.

The area picture also shows that **work depends on the path**, not just on where the gas starts and ends.

![A p-V diagram with three paths from A (1 L, 3 x 10^5 Pa) to B (3 L, 1 x 10^5 Pa): an upper path giving 600 J, a straight line giving 400 J and a lower path giving 200 J](figures/work_done_by_gas/three-paths-a-to-b.svg "Same start, same end: a path that keeps the pressure high encloses more area, so the gas does more work.")

## Worked example

**Given (illustrative):** during one power stroke, the gas's volume grows by $0.2\,\text{L}$, and its pressure falls in a straight line on the $p$–$V$ diagram from $3.0 \times 10^6\,\text{Pa}$ to $1.0 \times 10^6\,\text{Pa}$.
**Find:** the work done by the gas.

**Step 1: the change in volume, in SI units.**

$$\Delta V = 0.2\,\text{L} = 0.2 \times 10^{-3}\,\text{m}^3 = 2 \times 10^{-4}\,\text{m}^3$$

**Step 2: the average pressure.** The area under a straight line is a trapezium, which equals the average height times the width. Here the average pressure is halfway between the two ends:

$$p_\text{avg} = \frac{3.0 + 1.0}{2} \times 10^6 = 2.0 \times 10^6\,\text{Pa}$$

**Step 3: the work.**

$$W = p_\text{avg}\,\Delta V = 2.0 \times 10^6 \times 2 \times 10^{-4} = 400\,\text{J}$$

That is roughly the energy needed to lift a $40\,\text{kg}$ bag of cement one metre, delivered in a hundredth of a second or less, by one cylinder, on one stroke.

**Sanity check:** the gas's pressure was always between the two end values, so the answer must lie between $200\,\text{J}$ and $600\,\text{J}$; $400\,\text{J}$ is right in the middle, as a straight line should give.

## Where the picture breaks

This is a simplified model, not any real engine's data. In a real power stroke the pressure does not fall in a straight line; it drops along a curve, steeply at first, so you would need the true area under that curve. The formula also assumes the gas has one pressure throughout at every instant, which is only roughly true when the piston is moving fast. And not all $400\,\text{J}$ reaches the wheels: some goes into pushing the piston against friction, some into the next compression stroke, and some is lost further down the drivetrain.

## Key takeaway

A gas does work $\Delta W = p\,\Delta V$ when it expands a little; for any expansion, $W = \int p\,dV$, the area under the $p$–$V$ curve. Expansion gives positive work, compression negative, fixed volume zero, and the amount depends on the path. Convert litres to cubic metres before you multiply.
