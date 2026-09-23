---
concept_id: work_energy_theorem
interest: gaming
format: explain
title: How much speed the ice patch steals
check:
  question: |-
    A $2\,\text{kg}$ object in a game slides at $5\,\text{m/s}$. Over the next stretch the net work done on it is $-16\,\text{J}$. How fast is it moving at the end of that stretch?
  options:
    A: |-
      $3\,\text{m/s}$
    B: |-
      $6.4\,\text{m/s}$
    C: |-
      $5.8\,\text{m/s}$
    D: |-
      $4.1\,\text{m/s}$
  answer: A
  explanation: |-
    $K_i = \tfrac{1}{2}(2)(5)^2 = 25\,\text{J}$, so $K_f = 25 - 16 = 9\,\text{J}$, and $9 = \tfrac{1}{2}(2)v^2$ gives $v = 3\,\text{m/s}$.
  misconceptions:
    B: |-
      Adds the work instead of subtracting it ($25 + 16 = 41\,\text{J}$); negative net work means energy is being taken out, so the object must end up slower, not faster.
    C: |-
      Drops the factor $\tfrac{1}{2}$ and uses $K = mv^2$ ($50 - 16 = 34\,\text{J}$); kinetic energy is $\tfrac{1}{2}mv^2$.
    D: |-
      Writes $v_f^2 = v_i^2 + W/m$ instead of $v_f^2 = v_i^2 + 2W/m$, losing the factor of 2 that comes from the $\tfrac{1}{2}$ in the kinetic energy.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor shows a physics sandbox with a spring launcher, a kart at the top of a loop and a crate being dragged by a rope, beside a force-feedback racing wheel and a controller](scenes/gaming/work_energy_power.svg "Anything sliding across a surface in this sandbox is being slowed by it, frame after frame.")

Rudra is stuck on the ice level, and the clock on his speedrun attempt is still running. The jump is not the problem. The problem is the long rough patch of ice before it: he sprints in, slides across, and arrives at the edge too slow to clear the gap.

His friend Harleen, watching over his shoulder, has a theory. "The patch is $40\,\text{m}$ long and there's a wind machine halfway. Just enter faster."

"I've tried faster. Sometimes I clear it, sometimes I don't, and I can't tell the difference while I'm sliding."

What he wants is a number: enter at *this* speed, leave at *that* speed. The forces on the ice are dull and steady — no jumps, no bounces, just a drag backwards all the way across. There ought to be a way to skip the whole middle of the slide and go straight from the entry speed to the exit speed. Is there?

## The physics

For a constant net force on a body of mass $m$ moving in a straight line, $v^2 = u^2 + 2as$ with $a = F_\text{net}/m$. Multiply through by $\tfrac{1}{2}m$:

$$\tfrac{1}{2}mv^2 = \tfrac{1}{2}mu^2 + F_\text{net}s$$

Rearranged, that is the **work–energy theorem**:

$$W_\text{net} = K_f - K_i = \Delta K$$

**The net work done on a body equals the change in its kinetic energy.** Positive net work speeds it up; negative net work slows it down; zero net work leaves the speed unchanged, whatever happened in between.

![A body moves from A to B while a resistive force acts backwards on it; bar charts show its kinetic energy at B is lower than at A by exactly the net work done](figures/work_energy_theorem/net-work-changes-ke.svg "The drop in the kinetic-energy bar is exactly the negative work done by the resistive force.")

Three things make it powerful:

- **It skips the middle.** You never need the time taken, or the speed halfway across — only the total work and the two end points.
- **"Net" means all the forces.** Add the work done by each: friction, the wind machine, gravity, everything. Forces perpendicular to the motion (here the character's weight and the ice's normal force) contribute nothing.
- **It holds even when the force varies**, as long as you take the work as the area under the force–displacement graph. It fails only if mass changes or speeds approach that of light.

## Worked example

**Given** (illustrative game values): a character of mass $m = 50\,\text{kg}$ enters the rough ice at $u = 10\,\text{m/s}$ and crosses $d = 40\,\text{m}$, with the ice dragging back on her with a steady $40\,\text{N}$.
**Find:** her speed at the far edge.

**Step 1 — the energy she starts with.**

$$K_i = \tfrac{1}{2} \times 50 \times 10^2 = 25 \times 100 = 2500\,\text{J}$$

**Step 2 — the work the ice does.** The drag opposes the motion all the way, so its work is negative:

$$W_\text{net} = -40 \times 40 = -1600\,\text{J}$$

Weight and the normal force are perpendicular to the slide, so they add nothing. The ice removes $1600\,\text{J}$ — nearly two-thirds of what she had.

**Step 3 — the energy left.**

$$K_f = 2500 - 1600 = 900\,\text{J}$$

**Step 4 — turn it back into a speed.** From $K_f = \tfrac{1}{2}mv^2$:

$$v^2 = \frac{2 \times 900}{50} = 36 \quad\Rightarrow\quad v = 6\,\text{m/s}$$

She leaves the ice at $6\,\text{m/s}$ — still about the speed of a fast run.

**Sanity check:** the energy fell to about a third, but the speed only fell from $10$ to $6\,\text{m/s}$, because speed is the square root of energy. Losing most of your energy costs you much less of your speed than it feels like.

## Where the picture breaks

Real ice does not drag with one steady force: the friction changes with the surface, and once the character stops pushing off, air resistance grows with speed instead of staying fixed. The theorem also tells you nothing about *when* — Rudra learns his exit speed but not how many seconds the slide takes, which is what his speedrun timer cares about. And it treats the character as a single point of mass; arms, legs and a spinning body carry energy of their own that this one equation quietly ignores.

## Key takeaway

The work–energy theorem says $W_\text{net} = \Delta K = K_f - K_i$: the net work done on a body equals the change in its kinetic energy. Add up the work done by every force, and you can jump straight from the starting speed to the final speed without touching the motion in between.
