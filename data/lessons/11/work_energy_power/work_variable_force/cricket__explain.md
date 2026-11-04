---
concept_id: work_variable_force
interest: cricket
format: explain
title: The work done by a keeper's soft hands
check:
  question: |-
    A groundsman starts pushing a heavy roller. Along the direction of motion, his push grows uniformly from $0$ to $80\,\text{N}$ over the first $0.50\,\text{m}$, then stays at $80\,\text{N}$ for the next $0.50\,\text{m}$. How much work does his push do over the whole $1.0\,\text{m}$?
  options:
    A: |-
      $60\,\text{J}$
    B: |-
      $80\,\text{J}$
    C: |-
      $40\,\text{J}$
    D: |-
      $20\,\text{J}$
  answer: A
  explanation: |-
    Work is the area under the force-displacement graph: a triangle, $\tfrac{1}{2} \times 0.50 \times 80 = 20\,\text{J}$, plus a rectangle, $0.50 \times 80 = 40\,\text{J}$, giving $60\,\text{J}$.
  misconceptions:
    B: |-
      Uses the largest force as if it acted over the whole distance ($80 \times 1.0$); the force was smaller than $80\,\text{N}$ during the first half, so the true area is less.
    C: |-
      Averages only the first and last force values, $(0 + 80)/2 = 40\,\text{N}$, and multiplies by $1.0\,\text{m}$; that shortcut works only when the force changes uniformly over the whole distance, which it doesn't here.
    D: |-
      Finds the area of only the sloping (triangular) part and ignores the part where the force is constant; work keeps adding up over every stretch of the displacement.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground by day: a batter watches a ball climb high, a fielder waits under it, a player runs up the stadium steps and a groundsman pushes a roller](scenes/cricket/work_energy_power.svg "Every catch on this ground ends with a force that stops the ball.")

Tanvi keeps wicket for her state's under-19 side, and her coach at the academy has a new toy: a thin force sensor fitted inside a practice glove, linked to a laptop.

"Catch five from the bowling machine," he says. "Then we'll look."

On the screen, each catch is a graph: the force on the ball, plotted against how far her gloves travelled back after the ball arrived. Her best catches look the same. The force climbs quickly, stays roughly level while her hands give, then fades as the ball comes to rest.

"How much work did your gloves do on the ball?" the coach asks.

Tanvi knows $W = Fd\cos\theta$. But which $F$? It was zero, then $120\,\text{N}$, then zero again. There isn't one force to multiply. So how do you find the work done by a force that keeps changing?

## The physics

The trick is to cut the displacement into many small pieces of width $\Delta x$. Over one tiny piece, the force hardly changes, so the work done there is approximately

$$\Delta W \approx F(x)\,\Delta x$$

That is the area of a thin rectangle of height $F(x)$ and width $\Delta x$ on the force-displacement graph. Adding up all the rectangles gives the total work. As $\Delta x \to 0$, the rectangles fit the curve exactly, and the sum becomes the **area under the force-displacement graph**:

$$W = \lim_{\Delta x \to 0} \sum F(x)\,\Delta x = \int_{x_i}^{x_f} F(x)\,dx$$

For a graph made of straight segments, you don't need calculus. Just split the area into triangles and rectangles.

Two rules about sign:

- $F(x)$ here is the component of the force **along** the displacement. Where that component is negative, the area counts as negative work.
- For a constant force the "area" is a rectangle, $F \times d$ — the familiar result is just a special case.

In Tanvi's catch, the glove pushes the ball forwards, towards the bowler, while the ball moves backwards into her hands. The force opposes the displacement, so the glove does **negative** work on the ball.

![A force-displacement graph: force rises from 0 to 120 newtons over 0.05 metres, stays at 120 newtons until 0.25 metres, then falls to zero at 0.30 metres; dashed strips 0.05 metres wide approximate the area](figures/work_variable_force/area-under-force-displacement.svg "The area under the red line is the work. The dashed strips show the method: add up force times width, strip by strip.")

## Worked example

**Given** (illustrative, as in the graph above): the size of the glove's force rises uniformly from $0$ to $120\,\text{N}$ over the first $0.05\,\text{m}$, stays at $120\,\text{N}$ until $0.25\,\text{m}$, then falls uniformly to $0$ at $0.30\,\text{m}$. The force points opposite to the ball's displacement throughout.
**Find:** the work done by the glove on the ball.

Split the area into three pieces:

$$\text{rise: } \tfrac{1}{2} \times 0.05 \times 120 = 3\,\text{J}$$

$$\text{flat: } (0.25 - 0.05) \times 120 = 0.20 \times 120 = 24\,\text{J}$$

$$\text{fall: } \tfrac{1}{2} \times 0.05 \times 120 = 3\,\text{J}$$

Total area $= 30\,\text{J}$. Because the force opposes the motion,

$$W_\text{glove} = -30\,\text{J}$$

**Sanity check:** use the dashed strips, each $0.05\,\text{m}$ wide, at the force in the middle of each strip: $60, 120, 120, 120, 120, 60\,\text{N}$. The sum is $0.05 \times 600 = 30\,\text{J}$ — the same. Also, the average force over the $0.30\,\text{m}$ is $30/0.30 = 100\,\text{N}$, which sensibly lies between $0$ and $120\,\text{N}$.

## Where the picture breaks

A real force trace is not three neat straight lines; it wobbles, and you would find its area by counting squares or by software. The ball also squashes a little and sinks into the glove's padding, so the ball's displacement is not exactly the glove's travel. And the graph only tells you the work — not what that work does to the ball's motion. Linking the $-30\,\text{J}$ to the ball's speed is the job of kinetic energy and the work-energy theorem, coming next.

## Key takeaway

When a force changes as a body moves, the work it does is the area under its force-displacement graph, $W = \int F(x)\,dx$. Split the area into simple shapes (or thin strips) and add them. Area counts as negative work where the force opposes the displacement.
