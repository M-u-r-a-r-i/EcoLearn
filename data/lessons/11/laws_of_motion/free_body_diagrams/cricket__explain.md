---
concept_id: free_body_diagrams
interest: cricket
format: explain
title: Predicting the pull on a hanging practice ball
check:
  question: |-
    A $0.20\,\text{kg}$ practice ball hangs on a cord. A horizontal string holds it at rest with the cord at $45^\circ$ to the vertical. Taking $g = 9.8\,\text{m/s}^2$, what is the pull in the horizontal string?
  options:
    A: |-
      $1.39\,\text{N}$
    B: |-
      $2.77\,\text{N}$
    C: |-
      $0.20\,\text{N}$
    D: |-
      $1.96\,\text{N}$
  answer: D
  explanation: |-
    Vertically, $T\cos 45^\circ = mg = 1.96\,\text{N}$; horizontally, $F = T\sin 45^\circ$. Dividing, $F = mg\tan 45^\circ = 1.96\,\text{N}$.
  misconceptions:
    A: |-
      Takes the wrong component of the weight ($mg\sin 45^\circ$) instead of resolving the cord's tension. Resolve every force into the same horizontal and vertical directions.
    B: |-
      Gives the tension in the angled cord ($mg/\cos 45^\circ$) instead of the pull in the horizontal string. They are different forces on the free-body diagram.
    C: |-
      Uses the mass in kilograms as if it were the weight in newtons, forgetting to multiply by $g$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A batter drives the ball back past the bowler in a floodlit stadium](scenes/cricket/laws_of_motion.svg "In a match, forces on the ball change every instant. At rest on a practice rig they can be worked out exactly.")

In the corner of the academy's indoor hall, a ball in a mesh bag hangs from a beam on a long cord — the "hanging ball" batters use to groove their drives. Tanvi is about to start her session when her coach, Ravi sir, clips a spring balance onto the ball with a second, horizontal string and pulls sideways until the cord makes $30^\circ$ with the vertical. He holds it there, steady.

"Physics test," he says, covering the dial with his thumb. "Before you bat, tell me what this balance reads."

Tanvi's first instinct is to say "the weight of the ball". Then she hesitates. The ball isn't being lifted; it's being held sideways. And the cord is pulling too, at an angle. Three things are tugging on one ball and it isn't moving at all.

How do you get a number out of that?

## The physics

The tool for this is the **free-body diagram**: a sketch of *one* body, on its own, with an arrow for every force that acts **on** it.

To draw one:

1. **Isolate the body.** Draw the ball alone, as a dot. Leave out the beam, the coach and the balance.
2. **List every force on it.** Anything touching the ball can push or pull it; gravity acts without touching. Here: the weight $W = mg$ downwards, the tension $T$ in the cord pulling *along the cord* towards the beam, and the pull $F$ of the horizontal string.
3. **Draw each force** from the dot, in its true direction. Forces the ball exerts on other things (like its pull on the cord) do **not** go on this diagram; they belong on those bodies' diagrams.
4. **Choose axes** and resolve any angled force into components.

![Left: a ball hanging from a beam on a cord at 30 degrees to the vertical, held aside by a horizontal string to a spring balance. Right: its free-body diagram with tension T up and to the left along the cord, weight W down and pull F to the right, with T's components T cos 30 degrees and T sin 30 degrees dashed](figures/free_body_diagrams/ball-held-aside-fbd.svg "Three forces, one body. The dashed components of T are what you balance against W and F.")

**Equilibrium.** The ball is at rest, so its acceleration is zero and, by the second law, the net force on it is zero. All three forces pass through one point (they are **concurrent**), so the condition is simply that their vector sum is zero:

$$\vec{T} + \vec{W} + \vec{F} = 0$$

In components, each direction must balance separately:

$$\text{vertical: } T\cos\theta = mg \qquad \text{horizontal: } T\sin\theta = F$$

Dividing the second by the first gives a neat result: $F = mg\tan\theta$.

## Worked example

**Given:** ball plus bag, $m = 0.20\,\text{kg}$ (illustrative); cord at $\theta = 30^\circ$ to the vertical; horizontal string; $g = 9.8\,\text{m/s}^2$.
**Find:** the spring-balance reading $F$ and the tension $T$ in the cord.

*Weight:* $W = mg = 0.20 \times 9.8 = 1.96\,\text{N}$.

*Vertical balance:*

$$T = \frac{mg}{\cos 30^\circ} = \frac{1.96}{0.866} \approx 2.26\,\text{N}$$

*Horizontal balance:*

$$F = T\sin 30^\circ = 2.26 \times 0.500 \approx 1.13\,\text{N}$$

So the balance reads about $1.13\,\text{N}$ — a bit over half the ball's weight, not the whole of it. The cord, meanwhile, pulls harder than the ball's weight.

**Sanity check:** $F = mg\tan 30^\circ = 1.96 \times 0.577 = 1.13\,\text{N}$ ✓. Also, $\sqrt{F^2 + W^2} = \sqrt{1.13^2 + 1.96^2} = \sqrt{5.12} \approx 2.26\,\text{N} = T$ ✓. Limiting cases: at $\theta = 0$ the cord hangs straight, $F = 0$ and $T = mg$, as expected; as $\theta$ approaches $90^\circ$, $\tan\theta$ blows up — no finite pull can hold the cord horizontal.

## Where the picture breaks

We treated the ball as a point, so all the forces meet at one spot. A real ball in a mesh bag has size, and if forces don't all pass through one point they can also make it *turn*; that needs torques, which you'll meet with rotational motion. We also took the cord and string as light (massless) and the ball as perfectly still. A real hanging ball sways a little, and the moment it moves, the net force is no longer exactly zero. And a real spring balance has its own mass and its zero may be off; the reading we calculated is the ideal one.

## Key takeaway

A free-body diagram shows one body alone with every force acting **on** it, each drawn in its true direction. If the body is in equilibrium, the vector sum of those forces is zero, so their components balance separately in each direction. For concurrent forces that is enough to find any unknown force: here $F = mg\tan\theta$ and $T = mg/\cos\theta$.
