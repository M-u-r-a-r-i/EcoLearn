---
concept_id: work_energy_theorem
interest: football
format: explain
title: Will the knee slide stop before the photographers
check:
  question: |-
    A $0.45\,\text{kg}$ ball is passed along the grass at $20\,\text{m/s}$. Over the next stretch of pitch, the net work done on it is $-67.5\,\text{J}$. What is its speed at the end of that stretch?
  options:
    A: |-
      $5.0\,\text{m/s}$
    B: |-
      $15.8\,\text{m/s}$
    C: |-
      $10\,\text{m/s}$
    D: |-
      $26.5\,\text{m/s}$
  answer: C
  explanation: |-
    Initial $K = \tfrac{1}{2} \times 0.45 \times 20^2 = 90\,\text{J}$. By the work-energy theorem, final $K = 90 - 67.5 = 22.5\,\text{J}$, so $v = \sqrt{2 \times 22.5/0.45} = \sqrt{100} = 10\,\text{m/s}$.
  misconceptions:
    A: |-
      Assumes the speed falls by the same fraction as the kinetic energy (both by three quarters); energy depends on $v^2$, so losing three quarters of the energy only halves the speed.
    B: |-
      Uses $K = mv^2$ without the factor of one half; that makes the starting energy $180\,\text{J}$ and gives the wrong final speed.
    D: |-
      Adds the $67.5\,\text{J}$ instead of subtracting it; negative net work takes energy away, so the ball must slow down.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A football training ground by day: a player drags a weighted sled on a strap, a striker lofts the ball in a high arc, and the goalkeeper dives to catch it](scenes/football/work_energy_power.svg "Anything moving across this grass is slowed by it, whether it is a ball, a sled or a player.")

It has rained all afternoon, and the district final is level with two minutes left. Then Ishaan, a substitute who has been on the pitch for ten minutes, bundles the ball over the line. He sprints towards the corner flag, arms wide, and drops to his knees on the soaking grass.

He slides. And slides.

Crouched by the corner are three photographers with their cameras, about $14\,\text{m}$ ahead of where his knees hit the grass. On the bench, the kit manager, Joel, grabs his head. "On this wet grass he's going to take them all out!"

The assistant coach is calmer. "The grass is still pulling him back the whole way. He'll stop."

Ishaan hit the ground running fast, and the grass pushes back on him every centimetre of the slide. Is there a way to go straight from that backward push to how fast he's moving at any point, and where he stops, without working out his motion second by second?

## The physics

The **work-energy theorem** says:

$$W_\text{net} = K_f - K_i = \Delta K$$

The **net work** done on a body, the sum of the work done by every force acting on it (equal to the work done by the net force), equals the change in its kinetic energy.

**Why it's true (constant force).** For a constant net force $F$ along the motion, $a = F/m$ and $v^2 - u^2 = 2ad$. Multiply both sides by $\tfrac{1}{2}m$:

$$\tfrac{1}{2}mv^2 - \tfrac{1}{2}mu^2 = mad = Fd = W_\text{net}$$

For a force that varies, cut the path into small pieces where the force is nearly constant and add them. The theorem still holds, with the work found as the area under the force-displacement graph.

What it tells you:

- $W_\text{net} > 0$: the body speeds up.
- $W_\text{net} < 0$: it slows down.
- $W_\text{net} = 0$: its speed doesn't change (its direction still can).

In Ishaan's slide on level ground, his weight and the normal force are perpendicular to the motion and do no work. The only force doing work is friction from the wet grass, pointing backwards all the way. So $W_\text{net}$ is negative, and he loses exactly that much kinetic energy.

![A body moves from A to B while a resistive force acts backwards on it; bar charts show its kinetic energy at B is lower than at A by the net work done](figures/work_energy_theorem/net-work-changes-ke.svg "The drop in the kinetic-energy bar is exactly the negative work done by the resistive force.")

## Worked example

**Given** (illustrative): Ishaan's mass $m = 60\,\text{kg}$; speed when his knees touch the grass $u = 8.0\,\text{m/s}$; friction from the wet grass $f = 150\,\text{N}$, taken as constant; photographers $14\,\text{m}$ ahead.
**Find:** his speed after sliding $6.0\,\text{m}$, and how far he slides in all.

$$K_i = \tfrac{1}{2} \times 60 \times 8.0^2 = 30 \times 64 = 1920\,\text{J}$$

After $6.0\,\text{m}$:

$$W_\text{net} = -fd = -150 \times 6.0 = -900\,\text{J}$$

$$K_f = 1920 - 900 = 1020\,\text{J} \quad\Rightarrow\quad v = \sqrt{\frac{2 \times 1020}{60}} = \sqrt{34} \approx 5.8\,\text{m/s}$$

He stops when all his kinetic energy is gone, $f\,d_\text{stop} = K_i$:

$$d_\text{stop} = \frac{1920}{150} = 12.8\,\text{m}$$

He comes to rest about $1.2\,\text{m}$ short of the photographers. On dry grass, where the friction might be double ($300\,\text{N}$), he would stop after only $1920/300 = 6.4\,\text{m}$.

**Sanity check:** with kinematics, $a = -150/60 = -2.5\,\text{m/s}^2$. Then $v^2 = 8.0^2 - 2 \times 2.5 \times 6.0 = 64 - 30 = 34$, the same answer, and the stopping distance is $64/(2 \times 2.5) = 12.8\,\text{m}$.

## Where the picture breaks

Friction on wet grass isn't truly constant: it changes with the grass length, the puddles and how Ishaan leans back, so $150\,\text{N}$ is an effective average. He also isn't a rigid block. His arms swing and his body shifts during the slide, so parts of him move differently from others. The theorem itself is exact for each part; it is the single-number friction that is the simplification. (Knee slides on a dry pitch also burn skin, which is where that energy goes: into heat.)

## Key takeaway

The net work done on a body equals its change in kinetic energy: $W_\text{net} = \tfrac{1}{2}mv^2 - \tfrac{1}{2}mu^2$. Add up the work of every force and you get the change in speed directly, with no need to follow the motion moment by moment.
