---
concept_id: work_variable_force
interest: gaming
format: explain
title: The arcade lever that never pushes the same twice
check:
  question: |-
    A sensor records the force on a game's launch lever as it is pushed: the force starts at $40\,\text{N}$ and falls steadily to zero over a push of $2\,\text{m}$. How much work is done on the lever?
  options:
    A: |-
      $80\,\text{J}$
    B: |-
      $40\,\text{J}$
    C: |-
      $0$
    D: |-
      $-40\,\text{J}$
  answer: B
  explanation: |-
    The graph is a triangle, so the work is its area: $\tfrac{1}{2} \times 2\,\text{m} \times 40\,\text{N} = 40\,\text{J}$. A steadily falling force is the same as a constant force of the average value, $20\,\text{N}$, over $2\,\text{m}$.
  misconceptions:
    A: |-
      Multiplies the largest force by the whole displacement, as though the force stayed at $40\,\text{N}$ all the way; that is the area of the rectangle around the triangle, which is twice too big.
    C: |-
      Sees that the force ends at zero and concludes no work was done; what matters is the force acting over the whole push, not its final value.
    D: |-
      Reads a *decreasing* force as a negative force; the force still points along the motion the whole time, so every strip of area is positive work.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor shows a physics sandbox with a spring launcher, a kart at the top of a loop and a crate being dragged by a rope, beside a force-feedback racing wheel and a controller](scenes/gaming/work_energy_power.svg "The launcher on the left of the screen does not push with the same force all the way — it builds up, holds, then fades.")

Nikhil's game-dev club has built a real arcade cabinet for the college fest: a metal lever you slam to launch a ball up a ramp, with a force sensor glued under the handle. On the screen above, the cabinet proudly prints **ENERGY: 30 J** after every launch.

His teammate Farhan is unimpressed. "Your own sensor peaks at $120\,\text{N}$, and the lever travels $0.30\,\text{m}$. That's $120 \times 0.30 = 36\,\text{J}$. Either your sensor is wrong or your code is."

Nikhil pulls up the log the sensor writes sixty times a second. The force is nowhere near $120\,\text{N}$ for most of the push: it climbs from nothing as the lever takes up slack, holds steady through the middle, then dies away as the lever bottoms out.

So which number is the real energy delivered — and how do you multiply a force by a distance when the force keeps changing?

## The physics

$W = Fd\cos\theta$ works only while $F$ is constant. When the force changes with position, split the push into slices so thin that the force is nearly constant across each one. Over a slice of width $\Delta x$ the work is about $F(x)\,\Delta x$, and the total is the sum

$$W \approx \sum F(x)\,\Delta x$$

Each term $F\,\Delta x$ is the area of a thin strip under the force–displacement graph. Make the strips narrower and narrower and the sum becomes exact:

$$W = \int_{x_i}^{x_f} F(x)\,dx = \text{area under the } F\text{–}x \text{ graph}$$

**Work is the area under the force–displacement graph.** Area above the axis counts as positive work; area below it (a force pointing backwards) counts as negative.

![A force–displacement graph: the force rises from 0 to 120 newtons over the first 0.05 metres, stays at 120 newtons until 0.25 metres, then falls to zero at 0.30 metres, with dashed strips 0.05 metres wide approximating the area](figures/work_variable_force/area-under-force-displacement.svg "The work is the area under the red line. The dashed strips show the method: force times width, strip by strip, added up.")

This is exactly what Nikhil's cabinet already does, and what a game's physics engine does every frame: at each step it takes the force acting right now, multiplies by the small distance moved in that step — typically the $1/60\,\text{s}$ worth of motion — and adds it to a running total. A sum of thin strips *is* an integral, computed with a calculator instead of algebra.

## Worked example

**Given** (the sensor's log): the force rises straight from $0$ to $120\,\text{N}$ over the first $0.05\,\text{m}$, holds at $120\,\text{N}$ until $0.25\,\text{m}$, then falls straight back to zero at $0.30\,\text{m}$.
**Find:** the work done on the lever.

**Step 1 — the build-up.** A triangle, $0.05\,\text{m}$ wide and $120\,\text{N}$ tall:

$$W_1 = \tfrac{1}{2} \times 0.05 \times 120 = 3\,\text{J}$$

**Step 2 — the steady middle.** A rectangle, $0.20\,\text{m}$ wide:

$$W_2 = 0.20 \times 120 = 24\,\text{J}$$

Most of the energy comes from here, where the force is at full strength for the longest stretch.

**Step 3 — the fade.** Another triangle the same size as the first, so $W_3 = 3\,\text{J}$.

**Step 4 — add the areas.**

$$W = 3 + 24 + 3 = 30\,\text{J}$$

The cabinet is right and Farhan is wrong. $30\,\text{J}$ is roughly the energy of a cricket ball thrown at a friend across a room.

**Sanity check:** $36\,\text{J}$ would be the answer only if the lever pushed at its peak force the whole way, which it plainly does not, so the true value has to be a little smaller — and it is.

## Where the picture breaks

The sensor reads sixty times a second, so the "curve" is really sixty dots joined by straight lines; anything that happens between two readings is invisible. Here the straight-line shape made the strips exact, but for a curved graph strips of finite width always over- or under-shoot slightly, and you need narrower strips for a better answer. The graph also says nothing about *when* the force acted — two launches with the same area deliver the same energy even if one takes twice as long.

## Key takeaway

When a force varies, the work it does is the area under its force–displacement graph, $W = \int F\,dx$ — the limit of adding up $F\,\Delta x$ over thin slices. Split the area into triangles and rectangles when the shape allows, and count area below the axis as negative work.
