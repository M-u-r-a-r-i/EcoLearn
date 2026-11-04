---
concept_id: connected_bodies
interest: cricket
format: explain
title: Two kit bags, one rope and a pulley
check:
  question: |-
    A $6.0\,\text{kg}$ wheeled kit bag on a smooth, level floor is tied by a light rope over a smooth pulley to a $4.0\,\text{kg}$ bag hanging freely. Ignoring friction and taking $g = 9.8\,\text{m/s}^2$, what is the tension in the rope while they move?
  options:
    A: |-
      $39.2\,\text{N}$
    B: |-
      $23.5\,\text{N}$
    C: |-
      $58.8\,\text{N}$
    D: |-
      $15.7\,\text{N}$
  answer: B
  explanation: |-
    $a = \dfrac{m_2 g}{m_1 + m_2} = \dfrac{4.0 \times 9.8}{10} = 3.92\,\text{m/s}^2$, and the rope is the only horizontal force on the floor bag, so $T = m_1 a = 6.0 \times 3.92 \approx 23.5\,\text{N}$.
  misconceptions:
    A: |-
      Assumes the tension equals the hanging bag's weight. That is true only if nothing accelerates; here the hanging bag speeds up, so its weight must exceed the tension.
    C: |-
      Uses the weight of the bag on the floor. That weight is balanced by the floor's normal force and plays no part in the horizontal motion.
    D: |-
      Writes $T = m_2 a$ for the hanging bag, forgetting that its weight also acts on it. For the hanging bag, $m_2 g - T = m_2 a$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A batter drives the ball back past the bowler in a floodlit stadium](scenes/cricket/laws_of_motion.svg "Behind every match day is a lot of kit being hauled about, and the same laws govern that too.")

The club's old pavilion has a small pulley bolted to the edge of its first-floor balcony, left over from the days when equipment was hauled up by rope. After practice, Dev and Farhan are packing up. Dev has an idea to save a trip down the stairs: tie his wheeled kit bag, lying on the smooth balcony floor, to Farhan's lighter bag with the old rope, run the rope over the pulley, and let Farhan's bag hang over the edge.

The moment Farhan lets go, the hanging bag drops and drags Dev's bag rolling across the floor towards the rail.

"Stop!" Farhan shouts, too late. "That rope's ancient. It's carrying the whole weight of my bag — it'll snap!"

It doesn't snap. But was Farhan right about the tension? Is the rope really holding the full weight of the falling bag, or less, or more?

## The physics

When bodies are tied together, solve them one body at a time — each with its own free-body diagram — and let the string link the equations.

For a **light, inextensible string** over a **smooth, light pulley**:

- the **tension** $T$ is the same all along the string;
- the string can't stretch, so both bodies move with the **same size of acceleration** $a$ (one along the floor, one downwards).

Apply $F_\text{net} = ma$ to each body along its own direction of motion.

![Left: a body m1 on a smooth horizontal surface tied by a string over a pulley at the edge to a hanging body m2, with acceleration arrows. Right: free-body diagrams of m1 (N up, m1 g down, T towards the pulley) and m2 (T up, m2 g down, longer than T)](figures/connected_bodies/block-and-hanging-mass.svg "Separate diagrams for each body. For the hanging body, the weight arrow is longer than the tension, because it speeds up downwards.")

**Bag on the floor** ($m_1$), horizontally: the only horizontal force is the tension.

$$T = m_1 a$$

(Vertically, $N = m_1 g$: the floor supports it and it doesn't accelerate up or down.)

**Hanging bag** ($m_2$), taking downwards as positive: weight down, tension up.

$$m_2 g - T = m_2 a$$

Add the two equations and $T$ drops out:

$$a = \frac{m_2 g}{m_1 + m_2}, \qquad T = m_1 a = \frac{m_1 m_2}{m_1 + m_2}\,g$$

This answers Farhan. Because the hanging bag accelerates downwards, the net force on it must point down, so its weight must be **bigger** than the tension. The rope carries **less** than the full weight of the hanging bag. Only if the system were held still would the tension equal $m_2 g$.

## Worked example

**Given:** Dev's bag $m_1 = 12\,\text{kg}$ on the floor; Farhan's bag $m_2 = 8.0\,\text{kg}$ hanging (illustrative values). Friction, rope mass and pulley friction neglected; $g = 9.8\,\text{m/s}^2$.
**Find:** the acceleration and the tension.

$$a = \frac{m_2 g}{m_1 + m_2} = \frac{8.0 \times 9.8}{12 + 8.0} = \frac{78.4}{20} = 3.92\,\text{m/s}^2$$

$$T = m_1 a = 12 \times 3.92 \approx 47\,\text{N}$$

The weight of the hanging bag is $78.4\,\text{N}$, so the rope carries only about $60\%$ of it.

**Sanity check:** use the hanging bag's equation instead: $T = m_2(g - a) = 8.0 \times (9.8 - 3.92) = 8.0 \times 5.88 \approx 47\,\text{N}$ ✓. Limiting cases: if $m_1 = 0$, then $a = g$ and $T = 0$ (the bag just free-falls); if $m_1$ is huge, $a \to 0$ and $T \to m_2 g$ (the bag barely moves and the rope holds its full weight). Our answer sits sensibly in between.

## Where the picture breaks

A real wheeled bag has rolling friction and the old pulley has friction in its axle, so the real acceleration is smaller and the tension on the two sides of the pulley differs slightly. A real rope stretches a little and has mass. And a real bag isn't a rigid block: its contents shift as it starts moving. None of these changes the method — one free-body diagram per body, then solve together — only the numbers. (Please don't try this with real kit: a bag dropping off a balcony is a hazard to anyone below.)

## Key takeaway

For bodies joined by a light, inextensible string, draw a free-body diagram for each body, use the same tension $T$ and the same size of acceleration $a$ for all of them, and write $F_\text{net} = ma$ for each. For a body on a smooth table pulled by a hanging body, $a = \dfrac{m_2 g}{m_1 + m_2}$ and $T = \dfrac{m_1 m_2 g}{m_1 + m_2}$, always less than the hanging weight while things accelerate.
