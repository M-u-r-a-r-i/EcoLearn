---
concept_id: free_body_diagrams
interest: football
format: explain
title: The heading ball held back on a rope
check:
  question: |-
    A $0.43\,\text{kg}$ heading-practice ball hangs on a cord. A horizontal rope holds it at rest with the cord at $40^\circ$ to the vertical. Taking $g = 9.8\,\text{m/s}^2$, what is the pull in the horizontal rope? ($\tan 40^\circ = 0.839$, $\sin 40^\circ = 0.643$, $\cos 40^\circ = 0.766$)
  options:
    A: |-
      $4.21\,\text{N}$
    B: |-
      $5.50\,\text{N}$
    C: |-
      $3.54\,\text{N}$
    D: |-
      $2.71\,\text{N}$
  answer: C
  explanation: |-
    Vertically, $T\cos 40^\circ = mg = 4.21\,\text{N}$; horizontally, $F = T\sin 40^\circ$. Dividing, $F = mg\tan 40^\circ = 4.21 \times 0.839 \approx 3.54\,\text{N}$.
  misconceptions:
    A: |-
      Assumes the sideways pull must equal the ball's weight. The rope is horizontal, so it balances only the horizontal part of the cord's tension, not the weight.
    B: |-
      Gives the tension in the angled cord ($mg/\cos 40^\circ$) instead of the pull in the horizontal rope. They are different forces on the free-body diagram.
    D: |-
      Takes a component of the weight ($mg\sin 40^\circ$) instead of resolving the cord's tension into horizontal and vertical parts. Pick one pair of axes and resolve every force along them.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![Under floodlights, a striker follows through after a shot while the ball flies towards the goalkeeper](scenes/football/laws_of_motion.svg "In a match, the forces on the ball change every instant. On a training rig they can be worked out exactly.")

The academy has a heading trainer: a ball in a net pouch, hanging from a tall metal frame on a long cord. Coach Thapa's drill is to pull the ball back with a rope, hold it, and let it swing at the player's head.

Today, Lakshmi is next in line. Coach Thapa hooks a luggage scale into the pull-back rope, draws the ball sideways until the cord makes $30^\circ$ with the vertical, and holds the rope level and steady. He covers the scale's display with his thumb.

"No heading until someone tells me what this reads," he says.

"The weight of the ball?" says Lakshmi. Then she isn't sure. The rope is pulling sideways, not upwards. The cord is pulling too, at a slant. Three pulls on one ball, and it isn't moving at all.

How do you turn that into a number?

## The physics

The tool is the **free-body diagram**: a sketch of *one* body, alone, with an arrow for every force acting **on** it.

To draw one:

1. **Isolate the body.** Draw the ball on its own, as a dot. Leave out the frame, the coach and the scale.
2. **List every force on it.** Things touching it can push or pull; gravity acts without touching. Here: the weight $W = mg$ straight down; the **tension** $T$ in the cord, pulling *along the cord* towards the frame; the pull $F$ of the horizontal rope.
3. **Draw each force** from the dot, in its true direction. Forces the ball exerts on other things, such as its pull on the cord, do **not** go on this diagram.
4. **Choose axes** and resolve any slanted force into components.

![Left: a ball hanging from a beam on a cord at 30 degrees to the vertical, held aside by a horizontal string to a spring balance. Right: its free-body diagram with tension T up and to the left along the cord, weight W down and pull F to the right, with T's components T cos 30 degrees and T sin 30 degrees dashed](figures/free_body_diagrams/ball-held-aside-fbd.svg "The same set-up as the heading trainer, with a spring balance in place of the luggage scale. The dashed parts of T are what balance W and F.")

**Equilibrium.** The ball is at rest, so its acceleration is zero and the net force on it is zero. All three forces act through one point (they are **concurrent**), so the condition is that their vector sum is zero:

$$\vec{T} + \vec{W} + \vec{F} = 0$$

Each direction must then balance on its own:

$$\text{vertical: } T\cos\theta = mg \qquad \text{horizontal: } T\sin\theta = F$$

Dividing the second by the first gives $F = mg\tan\theta$.

## Worked example

**Given:** ball plus pouch $m = 0.45\,\text{kg}$ (illustrative); cord at $\theta = 30^\circ$ to the vertical; pull-back rope horizontal; $g = 9.8\,\text{m/s}^2$.
**Find:** the scale reading $F$ and the cord tension $T$.

*Weight:* $W = mg = 0.45 \times 9.8 = 4.41\,\text{N}$.

*Vertical balance:*

$$T = \frac{mg}{\cos 30^\circ} = \frac{4.41}{0.866} \approx 5.09\,\text{N}$$

*Horizontal balance:*

$$F = T\sin 30^\circ = 5.09 \times 0.500 \approx 2.55\,\text{N}$$

The scale reads about $2.55\,\text{N}$ (a luggage scale would show roughly $0.26\,\text{kg}$), a little over half the ball's weight. The cord, meanwhile, pulls *harder* than the weight.

**Sanity check:** $F = mg\tan 30^\circ = 4.41 \times 0.577 \approx 2.55\,\text{N}$ ✓, and $\sqrt{F^2 + W^2} = \sqrt{2.55^2 + 4.41^2} = \sqrt{25.95} \approx 5.09\,\text{N} = T$ ✓. Limiting cases: at $\theta = 0$ the cord hangs straight, $F = 0$ and $T = mg$; as $\theta$ nears $90^\circ$, $\tan\theta$ grows without limit, so no finite pull could hold the cord horizontal.

## Where the picture breaks

We treated the ball as a point, so every force passes through one spot. A real ball in a pouch has size, and forces that don't meet at one point can also make it *turn*; that needs torques, which you'll meet with rotational motion. We treated the cord and rope as light and perfectly still; the moment the coach's hand wobbles, the ball moves and the net force is no longer exactly zero. And a luggage scale reads in kilograms by assuming $g = 9.8\,\text{m/s}^2$; it is really measuring a force.

## Key takeaway

A free-body diagram shows one body alone with every force acting **on** it, drawn in its true direction. In equilibrium the vector sum of those forces is zero, so their components balance separately along each axis. For the held-back ball, $F = mg\tan\theta$ and $T = mg/\cos\theta$.
