---
concept_id: work_energy_theorem
interest: cricket
format: explain
title: Will the drive reach the rope
check:
  question: |-
    A $0.16\,\text{kg}$ ball runs along the outfield at $15\,\text{m/s}$. Over the next stretch of grass, the net work done on it is $-10\,\text{J}$. What is its speed at the end of that stretch?
  options:
    A: |-
      $5.0\,\text{m/s}$
    B: |-
      $10\,\text{m/s}$
    C: |-
      $12.7\,\text{m/s}$
    D: |-
      $18.7\,\text{m/s}$
  answer: B
  explanation: |-
    Initial $K = \tfrac{1}{2} \times 0.16 \times 15^2 = 18\,\text{J}$. By the work-energy theorem, final $K = 18 - 10 = 8\,\text{J}$, so $v = \sqrt{2 \times 8/0.16} = \sqrt{100} = 10\,\text{m/s}$.
  misconceptions:
    A: |-
      Subtracts the work (in joules) straight from the speed (in m/s); work changes the kinetic energy, not the speed directly.
    C: |-
      Uses $K = mv^2$ without the factor of one half; that gives an initial energy of $36\,\text{J}$ and the wrong final speed.
    D: |-
      Adds the $10\,\text{J}$ instead of subtracting it, ignoring the sign; negative net work takes energy away, so the ball must slow down.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground by day: a batter watches a ball climb high, a fielder waits under it, a player runs up the stadium steps and a groundsman pushes a roller](scenes/cricket/work_energy_power.svg "A ball on the grass slows down every metre it travels. The question is whether it runs out of energy before the rope.")

It rained all morning, but the outfield has dried by the afternoon. Farhan leans into a straight drive and the ball shoots off along the grass, past the bowler, towards the long-on rope about $65\,\text{m}$ away.

Aditi sprints after it from mid-on. In the dugout, the team's analyst watches the ball slow down, metre after metre. "It left the bat at about $72\,\text{km/h}$," he mutters. "The grass is slowing it. Will it even reach the rope?"

His friend shrugs. "If the grass were still wet, it would have died halfway."

Both of them are right, but neither can say how fast the ball will be going when it gets there. The grass pushes back on the ball the whole way. Is there a way to go straight from that backward push to the ball's final speed, without working out the motion second by second?

## The physics

The **work-energy theorem** says:

$$W_\text{net} = K_f - K_i = \Delta K$$

The **net work** done on a body — the sum of the work done by every force on it, which equals the work done by the net force — equals the change in its kinetic energy.

**Why it's true (constant force).** For a constant net force $F$ along the motion, $a = F/m$ and $v^2 - u^2 = 2ad$. Multiply both sides by $\tfrac{1}{2}m$:

$$\tfrac{1}{2}mv^2 - \tfrac{1}{2}mu^2 = mad = Fd = W_\text{net}$$

For a force that varies, cut the path into small pieces where the force is nearly constant and add the results. The theorem still holds, with the work taken as the area under the force-displacement graph.

What it tells you:

- $W_\text{net} > 0$: the body speeds up.
- $W_\text{net} < 0$: it slows down.
- $W_\text{net} = 0$: its speed doesn't change (its direction still can).

For Farhan's drive on level ground, gravity and the normal force are perpendicular to the motion and do no work. The only work is done by the resistance from the grass, which acts against the motion all the way. So $W_\text{net}$ is negative, and the ball loses exactly that much kinetic energy.

![A ball moves from A to B along the ground while a resistive force acts backwards on it; bar charts show its kinetic energy at B is lower than at A by the net work done](figures/work_energy_theorem/net-work-changes-ke.svg "The drop in the kinetic-energy bar is exactly the negative work done by the resistive force.")

## Worked example

**Given** (illustrative): ball mass $m = 0.16\,\text{kg}$; initial speed $u = 72\,\text{km/h} = 20\,\text{m/s}$; an average resistive force from the grass of $f = 0.30\,\text{N}$; distance to the rope $d = 65\,\text{m}$.
**Find:** the ball's speed at the rope.

$$K_i = \tfrac{1}{2} \times 0.16 \times 20^2 = 32\,\text{J}$$

$$W_\text{net} = -fd = -0.30 \times 65 = -19.5\,\text{J}$$

$$K_f = K_i + W_\text{net} = 32 - 19.5 = 12.5\,\text{J}$$

$$v = \sqrt{\frac{2K_f}{m}} = \sqrt{\frac{2 \times 12.5}{0.16}} = \sqrt{156.25} = 12.5\,\text{m/s}$$

The ball reaches the rope at $12.5\,\text{m/s}$, or $45\,\text{km/h}$ — Aditi needs to be quick. How far could it roll on this grass? It stops when all $32\,\text{J}$ is gone: $32/0.30 \approx 107\,\text{m}$. On the wet morning grass, if the resistance were double ($0.60\,\text{N}$), it would stop after $32/0.60 \approx 53\,\text{m}$ — short of the rope, just as the friend said.

**Sanity check:** with kinematics, $a = -0.30/0.16 = -1.875\,\text{m/s}^2$, and $v^2 = 20^2 - 2 \times 1.875 \times 65 = 400 - 243.75 = 156.25$. That gives the same $12.5\,\text{m/s}$.

## Where the picture breaks

A ball on grass bounces at first and then rolls. A rolling ball also has energy of rotation, which a single "sliding" $\tfrac{1}{2}mv^2$ ignores. The resistance isn't really constant either: it depends on the length and wetness of the grass, and on the ball's speed. So $0.30\,\text{N}$ is an effective average, chosen to match how far balls actually roll. The theorem itself is exact. It's the single-number force that is the simplification.

## Key takeaway

The net work done on a body equals its change in kinetic energy: $W_\text{net} = \tfrac{1}{2}mv^2 - \tfrac{1}{2}mu^2$. Add up the work of every force, and you get the change in speed directly — no need to follow the motion moment by moment.
