---
concept_id: work_variable_force
interest: football
format: explain
title: How much work a boot does in one kick
check:
  question: |-
    During a kick, the force of a player's boot on the ball, along the ball's motion, rises uniformly from $0$ to $600\,\text{N}$ over the first $10\,\text{cm}$ and falls uniformly back to $0$ over the next $10\,\text{cm}$. How much work does the boot do on the ball?
  options:
    A: |-
      $120\,\text{J}$
    B: |-
      $30\,\text{J}$
    C: |-
      $6000\,\text{J}$
    D: |-
      $60\,\text{J}$
  answer: D
  explanation: |-
    The work is the area under the force-displacement graph, here a triangle with base $0.20\,\text{m}$ and height $600\,\text{N}$: $\tfrac{1}{2} \times 0.20 \times 600 = 60\,\text{J}$.
  misconceptions:
    A: |-
      Uses the peak force as if it acted over the whole $0.20\,\text{m}$ ($600 \times 0.20$); the force was smaller than $600\,\text{N}$ almost everywhere, so the true area is half that rectangle.
    B: |-
      Finds the area of only the rising half of the graph; work keeps adding up while the force falls back to zero.
    C: |-
      Leaves the displacement in centimetres ($\tfrac{1}{2} \times 20 \times 600$); a joule is a newton times a metre, so distances must be in metres.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A football training ground by day: a player drags a weighted sled on a strap, a striker lofts the ball in a high arc, and the goalkeeper dives to catch it](scenes/football/work_energy_power.svg "Every kick on this ground is a short, hard push that changes from moment to moment.")

Kavya takes the penalties for her school team, and this week she got to test her kick at a university sports-science lab. A high-speed camera filmed her striking a stationary ball, thousands of frames a second.

Devendra, the research student running the camera, turns his screen towards her. Software has tracked how far the ball moved during the brief moment her boot was touching it, and how hard the boot was pushing. The result is a graph: force against the ball's displacement. The force leaps up, holds steady for a few centimetres, then drops to zero as the ball leaves her foot.

"So," he says, "how much work did your boot do on the ball?"

Kavya knows $W = Fd$. But the force was zero, then about $1350\,\text{N}$, then zero again. There isn't one force to multiply. How do you find the work done by a force that keeps changing?

## The physics

Cut the displacement into many small pieces of width $\Delta x$. Over one tiny piece the force hardly changes, so the work done there is approximately

$$\Delta W \approx F(x)\,\Delta x$$

That is the area of a thin rectangle of height $F(x)$ and width $\Delta x$ on the force-displacement graph. Add up all the rectangles for the total work. As $\Delta x \to 0$, the rectangles fit the curve exactly, and the sum becomes the **area under the force-displacement graph**:

$$W = \lim_{\Delta x \to 0} \sum F(x)\,\Delta x = \int_{x_i}^{x_f} F(x)\,dx$$

For a graph made of straight segments, you don't need calculus: split the area into triangles and rectangles.

Two rules to keep straight:

- $F(x)$ is the component of the force **along** the displacement. Where that component is negative (the force opposes the motion), the area counts as negative work.
- For a constant force, the area is a rectangle, $F \times d$. The familiar formula is just a special case.

In Kavya's kick, the boot pushes the ball forwards and the ball moves forwards, so the boot does **positive** work on it.

![A force-displacement graph: force rises from 0 to 1350 newtons over 0.02 metres, stays at 1350 newtons until 0.10 metres, then falls to zero at 0.12 metres; dashed strips 0.02 metres wide approximate the area](figures/work_variable_force/short-hard-push.svg "The area under the red line is the work. The dashed strips show the method: add up force times width, strip by strip.")

## Worked example

**Given** (illustrative, as in the graph above): the boot's force along the ball's motion rises uniformly from $0$ to $1350\,\text{N}$ over the first $0.02\,\text{m}$, stays at $1350\,\text{N}$ until $0.10\,\text{m}$, then falls uniformly to $0$ at $0.12\,\text{m}$.
**Find:** the work done by the boot on the ball.

Split the area into three pieces:

$$\text{rise: } \tfrac{1}{2} \times 0.02 \times 1350 = 13.5\,\text{J}$$

$$\text{flat: } (0.10 - 0.02) \times 1350 = 0.08 \times 1350 = 108\,\text{J}$$

$$\text{fall: } \tfrac{1}{2} \times 0.02 \times 1350 = 13.5\,\text{J}$$

$$W_\text{boot} = 13.5 + 108 + 13.5 = 135\,\text{J}$$

**Sanity check:** use the dashed strips, each $0.02\,\text{m}$ wide, at the force in the middle of each strip: $675$, then four of $1350$, then $675\,\text{N}$. The sum is $0.02 \times 6750 = 135\,\text{J}$, the same. The average force over the $0.12\,\text{m}$ is $135/0.12 = 1125\,\text{N}$, sensibly between $0$ and the peak.

## Where the picture breaks

A real force trace is never three neat straight lines; it wobbles, and software finds its area by adding thin strips, exactly as above. The ball also squashes against the boot, so the "displacement" is really that of the ball's centre, and working it out from video is itself an estimate. And the graph tells you only the work, not what that work does to the ball. Turning $135\,\text{J}$ into a speed is the job of kinetic energy and the work-energy theorem, coming next.

## Key takeaway

When a force changes as a body moves, the work it does is the area under its force-displacement graph, $W = \int F(x)\,dx$. Split the area into simple shapes or thin strips and add them up. Area counts as negative work wherever the force opposes the displacement.
