---
concept_id: potential_energy_conservative_forces
interest: football
format: explain
title: The ball that keeps rolling down to the road
check:
  question: |-
    A goalkeeper's kick sends a $0.44\,\text{kg}$ ball up to a peak $15\,\text{m}$ high. It follows a curving path about $60\,\text{m}$ long and lands back on the pitch at the same height it was kicked from. Taking $g = 9.8\,\text{m/s}^2$, how much work does gravity do on the ball over the whole flight?
  options:
    A: |-
      $0\,\text{J}$
    B: |-
      $-64.7\,\text{J}$
    C: |-
      $-259\,\text{J}$
    D: |-
      $+64.7\,\text{J}$
  answer: A
  explanation: |-
    Gravity is conservative, so its work depends only on the start and end heights: $W = -mg\,\Delta h$. The ball lands at the height it started from, so $\Delta h = 0$ and $W = 0$. Gravity's $-64.7\,\text{J}$ on the way up is exactly cancelled by $+64.7\,\text{J}$ on the way down.
  misconceptions:
    B: |-
      Counts only the climb to the peak ($-0.44 \times 9.8 \times 15$) and forgets that gravity does an equal amount of positive work while the ball falls back down.
    C: |-
      Multiplies by the length of the path ($0.44 \times 9.8 \times 60$); for a conservative force like gravity, only the change in height matters, not the route.
    D: |-
      Counts only the fall from the peak and forgets the negative work gravity did while the ball was rising.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A football training ground by day: a player drags a weighted sled on a strap, a striker lofts the ball in a high arc, and the goalkeeper dives to catch it](scenes/football/work_energy_power.svg "A lofted ball climbs and falls. What gravity does to it depends only on where it starts and where it ends.")

In their hill town, Lhamo and Bikash play on the only flat ground there is: a terrace cut into the hillside. Every few minutes a stray shot bounces off the edge and rolls all the way down to the road, $8\,\text{m}$ below.

This time, both boys go down. Bikash, fed up, lofts the ball straight back up with one huge kick. It soars well above the terrace before dropping onto it. Lhamo takes the other ball the long way, dribbling it up the zig-zag footpath, about $50\,\text{m}$ of winding slope.

At the top, they argue. "Your kick had to fight gravity much more," says Lhamo. "It went way higher than the terrace."

"Rubbish," says Bikash. "Your ball was on that slope five times longer. Gravity was pulling on it the whole way."

They can't both be right. Does the route change how much work gravity does on the ball?

## The physics

A force is **conservative** if the work it does on a body moving between two points depends only on those points, not on the path taken. Equivalently, its work around any **closed path** is zero. Gravity and the ideal spring force are conservative.

A force is **non-conservative** if its work depends on the path. Friction and air resistance always oppose the motion, so a longer route means more negative work, and even a round trip leaves negative work behind.

Only a conservative force has a **potential energy** $U$, an energy of position. Its change is minus the work the force does:

$$\Delta U = -W_\text{conservative}$$

Near the Earth's surface, where $g$ is effectively constant (heights much smaller than the Earth's radius), raising a mass $m$ through a height $h$ by any route means gravity does work $-mgh$. So

$$U = mgh$$

You choose where $h = 0$. Only **changes** in $U$ have physical meaning.

![Two paths from A up to B: a short straight one and a long winding one. Gravity does work minus m g h on both; friction does more negative work on the longer path](figures/potential_energy_conservative_forces/path-independence.svg "Gravity only counts the height gained. Friction charges for every metre of the route.")

So Lhamo and Bikash are both wrong. On Bikash's lofted kick, gravity does extra negative work climbing above the terrace, but gives exactly that back on the way down. On Lhamo's slope, only the part of gravity along the slope does work, and over the whole winding path that adds up to the same $-mgh$.

## Worked example

**Given:** ball mass $m = 0.43\,\text{kg}$; terrace $h = 8.0\,\text{m}$ above the road; $g = 9.8\,\text{m/s}^2$. Bikash's kick peaks $14\,\text{m}$ above the road. Lhamo's path is $50\,\text{m}$ long with a rolling resistance of $0.40\,\text{N}$ (illustrative), and he dribbles at a steady pace.
**Find:** the work done by gravity on each route, and the work Lhamo's feet do on his ball.

The ball's weight is $mg = 0.43 \times 9.8 \approx 4.21\,\text{N}$.

*Bikash's kick:* up $14\,\text{m}$, then down $6\,\text{m}$ to the terrace:

$$W_g = -4.21 \times 14 + 4.21 \times 6 = -59.0 + 25.3 = -33.7\,\text{J}$$

*Lhamo's path:* only the height gained counts:

$$W_g = -mgh = -4.21 \times 8.0 \approx -33.7\,\text{J}$$

The same, so the gain in potential energy is $\Delta U = +33.7\,\text{J}$ on both routes.

Rolling resistance on Lhamo's ball does $-0.40 \times 50 = -20\,\text{J}$. The ball's speed is steady, so the net work is zero (work-energy theorem), and his feet must supply

$$W_\text{feet} = 33.7 + 20 \approx 54\,\text{J}$$

**Sanity check:** choose the terrace as $h = 0$ instead. Then $U_\text{road} = -33.7\,\text{J}$ and $U_\text{terrace} = 0$. The values change, but $\Delta U = +33.7\,\text{J}$ does not.

## Where the picture breaks

Bikash's kick also loses a little energy to air drag, a non-conservative force, so the air takes its own share along the flight. Lhamo's dribble isn't a steady push either; it's a series of taps. The formula $mgh$ assumes constant $g$, excellent on a hillside but not for satellites; that needs the general gravitational potential energy in the Gravitation chapter. And "energy stored in the ball" is a shorthand: strictly, potential energy belongs to the ball–Earth system.

## Key takeaway

A conservative force (gravity, an ideal spring) does work that depends only on the start and end points; a non-conservative force (friction, drag) does work that depends on the path. Only conservative forces have a potential energy, with $\Delta U = -W_\text{conservative}$. Near the Earth, $U = mgh$.
