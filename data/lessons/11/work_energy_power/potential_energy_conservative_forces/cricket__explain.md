---
concept_id: potential_energy_conservative_forces
interest: cricket
format: explain
title: The kit bag, the stairs and the long ramp
check:
  question: |-
    A batter hits a six. The $0.16\,\text{kg}$ ball follows a curving flight about $90\,\text{m}$ long and lands in a seat $10\,\text{m}$ higher than where it left the bat. Taking $g = 9.8\,\text{m/s}^2$, how much work did gravity do on the ball during the flight?
  options:
    A: |-
      $+15.7\,\text{J}$
    B: |-
      $-141\,\text{J}$
    C: |-
      $0\,\text{J}$
    D: |-
      $-15.7\,\text{J}$
  answer: D
  explanation: |-
    Gravity is conservative, so its work depends only on the change in height, not on the path: $W = -mgh = -0.16 \times 9.8 \times 10 = -15.7\,\text{J}$. It is negative because the ball ends up higher.
  misconceptions:
    A: |-
      Gets the sign wrong: the ball gains potential energy, so gravity (which pulls down while the ball ends up higher) does negative work, $W_g = -\Delta U$.
    B: |-
      Multiplies by the length of the flight path ($0.16 \times 9.8 \times 90$); for a conservative force like gravity only the start and end heights matter.
    C: |-
      Thinks gravity does no net work because the ball goes up and then comes down; that is only true for a round trip back to the same height, and this ball finishes $10\,\text{m}$ higher.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground by day: a batter watches a ball climb high, a fielder waits under it, a player runs up the stadium steps and a groundsman pushes a roller](scenes/cricket/work_energy_power.svg "The stands rise high above the field, and everything carried up there has to be lifted against gravity.")

The match is over, and Priya, the team's kit manager, has one last job: get the $15\,\text{kg}$ kit bag from the boundary up to the dressing room, $12\,\text{m}$ above the field. There are two routes. The concrete stairs go almost straight up. The long service ramp zig-zags back and forth for about $60\,\text{m}$, and the bag has wheels.

Her teammate Siddharth is sure the ramp is worse. "Five times as long. You'll do five times as much work against gravity."

"Rubbish," says Priya. "The ramp is *easier*. So it must take less energy."

They both sound convincing, and they can't both be right. Does the route change how much work you do against gravity? And if the ramp really is easier, where does the difference go?

## The physics

A force is **conservative** if the work it does on a body moving between two points depends only on those two points, not on the path taken. Equivalently, its work around any **closed path** is zero. Gravity and the ideal spring force are conservative.

A force is **non-conservative** if its work depends on the path. Friction and air resistance always oppose the motion, so a longer path means more negative work, and a round trip still leaves negative work.

Only for a conservative force can we define a **potential energy** $U$, an energy of position. Its change is minus the work the force does:

$$\Delta U = -W_\text{conservative}$$

Near the Earth's surface, where $g$ is effectively constant (heights much smaller than the Earth's radius), raising a mass $m$ through a height $h$ means gravity does work $-mgh$ on any path, so

$$U = mgh$$

The zero of height is yours to choose. Only **changes** in $U$ have physical meaning.

![Two paths from A up to B: a short straight one and a long winding one. Gravity does work minus m g h on both; friction does more negative work on the longer path](figures/potential_energy_conservative_forces/path-independence.svg "Gravity only cares about the height gained. Friction charges you for every metre of the route.")

So Siddharth is wrong about gravity: both routes involve exactly the same work against gravity. Priya is wrong about the energy: the ramp needs a **smaller force**, but over a longer distance. On top of that, the wheels' resistance does extra negative work over all $60\,\text{m}$.

## Worked example

**Given:** $m = 15\,\text{kg}$, height gained $h = 12\,\text{m}$, $g = 9.8\,\text{m/s}^2$; ramp length $60\,\text{m}$ with a rolling resistance of $10\,\text{N}$ (illustrative); Priya wheels the bag up at steady speed.
**Find:** the gain in potential energy on each route, and the work Priya does on the ramp.

Either route:

$$\Delta U = mgh = 15 \times 9.8 \times 12 = 1764\,\text{J} \approx 1.8\,\text{kJ}$$

So gravity does $-1764\,\text{J}$ on both routes.

On the ramp, the resistance does $-10 \times 60 = -600\,\text{J}$. The speed is steady, so the net work is zero (work-energy theorem), and Priya's work must cancel both:

$$W_\text{Priya} = 1764 + 600 = 2364\,\text{J} \approx 2.4\,\text{kJ}$$

Her force along the ramp is only $2364/60 \approx 39\,\text{N}$, compared with lifting the bag's weight of $15 \times 9.8 = 147\,\text{N}$ on the stairs. The ramp is easier, but it costs **more** energy, not less.

**Sanity check:** the ramp rises $12\,\text{m}$ in $60\,\text{m}$, so the component of gravity along it is $mg \times 12/60 = 147 \times 0.2 = 29.4\,\text{N}$. Add $10\,\text{N}$ of resistance and you get $39.4\,\text{N}$, which gives $39.4 \times 60 = 2364\,\text{J}$.

## Where the picture breaks

On the stairs, Priya also lifts her own body, and her muscles waste much of their chemical energy as heat. So "how tired she feels" is not $mgh$. The formula $mgh$ also assumes constant $g$, which is excellent for a stadium but fails for rockets and satellites. That needs the general gravitational potential energy, coming in the Gravitation chapter. And "the energy is stored in the bag" is a convenient shorthand: strictly, potential energy belongs to the bag–Earth system.

## Key takeaway

A conservative force (gravity, an ideal spring) does work that depends only on the start and end points; a non-conservative force (friction, drag) does work that depends on the path. Only conservative forces have a potential energy, with $\Delta U = -W_\text{conservative}$. Near the Earth, $U = mgh$.
