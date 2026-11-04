---
concept_id: work_done_by_gas
interest: football
format: explain
title: The air inside the ball does the pushing
check:
  question: |-
    As a squashed ball springs back into shape, the air inside expands at a nearly constant pressure of $2.0 \times 10^5\,\text{Pa}$ from $5.00\,\text{L}$ to $5.20\,\text{L}$. How much work does the air do?
  options:
    A: |-
      $4.0 \times 10^4\,\text{J}$
    B: |-
      $40\,\text{J}$
    C: |-
      $1.0 \times 10^3\,\text{J}$
    D: |-
      $0\,\text{J}$
  answer: B
  explanation: |-
    At constant pressure the area under the $p$–$V$ graph is a rectangle: $W = p\,\Delta V$. With $\Delta V = 0.20\,\text{L} = 2.0 \times 10^{-4}\,\text{m}^3$, $W = (2.0 \times 10^5)(2.0 \times 10^{-4}) = 40\,\text{J}$.
  misconceptions:
    A: |-
      Multiplies by $0.20$ litres without converting to cubic metres ($1\,\text{L} = 10^{-3}\,\text{m}^3$), so the answer comes out 1000 times too large.
    C: |-
      Uses the final volume instead of the change in volume, computing $pV$ rather than $p\,\Delta V$. Work depends on how far the boundary moves, which means how much the volume changes.
    D: |-
      Thinks a gas only does work when its pressure changes. At constant pressure the gas still pushes the wall outwards through a distance, so it does work.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground on a hot day: a board reading 36 degrees Celsius, an ice box of drinks, a player inflating a ball with a hand pump, and a mower with a hot exhaust](scenes/football/thermodynamics.svg "That pump is filling the ball with the gas this lesson is about — the gas that later pushes back.")

Ifra takes free kicks after every session, and today her coach, Dhruv, films one on a phone at high frame rate. They crouch over the screen afterwards and step through it frame by frame.

For three or four frames, the ball is not a ball at all. It is flattened against her boot like a squashed bun, dented almost a third of the way in. Then it is round again, already climbing away over the wall.

"There," says Dhruv, stopping on the frame where it is flattest. "Your boot has stopped pushing by now. Something inside that ball pushes it back out and throws it off your foot. What?"

Ifra thinks about it. There is no spring in there. There is nothing in there at all — except air, squeezed in with a pump that morning.

"So the air pushes it back," she says. "Can we work out how much that push is worth?"

## The physics

Take the standard picture: a gas in a cylinder closed by a piston of area $A$. The gas at pressure $p$ presses on the piston with force $F = pA$. If the piston moves outwards a small distance $\Delta x$, the gas does work

$$\Delta W = F\,\Delta x = pA\,\Delta x = p\,\Delta V$$

because $A\,\Delta x$ is the small increase in volume $\Delta V$.

![A gas at pressure p pushes a piston of area A outward by a small distance delta x](figures/work_done_by_gas/piston-small-expansion.svg "The gas's force pA acts through the piston's small move; the volume grows by A times delta x.")

The ball has no piston, but it does have a wall that moves: the flattened panel against Ifra's boot. As it springs back out, the air inside pushes that wall outwards and the enclosed volume grows. That is exactly $p\,\Delta V$.

If the pressure changes while the volume changes, chop the process into many small steps, each at nearly constant $p$, and add them:

$$W = \int_{V_1}^{V_2} p\,dV$$

On a **$p$–$V$ diagram** (pressure up, volume across) this integral is the **area under the curve** between $V_1$ and $V_2$. Three rules follow:

- Volume increases: $W$ is positive — the gas does work on its surroundings.
- Volume decreases: $W$ is negative — the surroundings do work on the gas.
- Volume fixed: $W = 0$, however wildly the pressure changes.

Units: $\text{Pa} \times \text{m}^3 = \text{N/m}^2 \times \text{m}^3 = \text{N m} = \text{J}$. Convert litres first, always: $1\,\text{L} = 10^{-3}\,\text{m}^3$.

Because $W$ is an area under a curve, it depends on the *path*, not only on the start and end states.

![A p-V diagram with three paths from A (1 L, 3 x 10^5 Pa) to B (3 L, 1 x 10^5 Pa): an upper path giving 600 J, a straight line giving 400 J and a lower path giving 200 J](figures/work_done_by_gas/three-paths-a-to-b.svg "Same start, same end; the area under each path, and so the work done, is different.")

## Worked example

**Given (illustrative, and rounded):** the ball holds about $5.0\,\text{L}$ of air at roughly $2.0 \times 10^5\,\text{Pa}$. As it springs back off the boot, its volume recovers by $0.20\,\text{L}$, and we treat the pressure as constant through that small change.
**Find:** the work the air does on the ball's casing.

First put the volume change in SI units:

$$\Delta V = 0.20\,\text{L} = 2.0 \times 10^{-4}\,\text{m}^3$$

That is a fortieth of the ball's volume — the dent you saw on the video, not a dramatic change.

At constant pressure the area under the $p$–$V$ graph is a rectangle, so

$$W = p\,\Delta V = (2.0 \times 10^5)(2.0 \times 10^{-4}) = 40\,\text{J}$$

**Sanity check:** $40\,\text{J}$ given to a ball of about $0.4\,\text{kg}$ would launch it at roughly $14\,\text{m/s}$ — a firm pass, not a thunderbolt. That is the right size for the springiness of a ball, and comfortably less than the energy of Ifra's whole kick.

## Where the picture breaks

The air's pressure does not really stay constant while the ball recovers; it falls as the volume grows, so $40\,\text{J}$ is an upper estimate of the rectangle's area. Nor does all of it end up in the ball's flight: the casing itself stretches and springs back, and some energy is lost inside the material, which is why a ball warms slightly during a long session. The formula $W = \int p\,dV$ also assumes the gas has one well-defined pressure at every instant, whereas a boot strike lasts about a hundredth of a second and the air inside is briefly uneven. Treat this as the idealised, slow version of what happened.

## Key takeaway

A gas does work $\Delta W = p\,\Delta V$ in a small expansion, and $W = \int p\,dV$ overall — the area under its $p$–$V$ curve. Expansion gives positive work, compression negative, fixed volume zero, and the value depends on the path between the two states. Convert litres to cubic metres before you multiply.
