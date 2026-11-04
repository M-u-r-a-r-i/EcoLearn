---
concept_id: connected_bodies
interest: gaming
format: explain
title: The rope meter that read less than the bucket weighed
check:
  question: |-
    In a puzzle game with realistic physics, a $3.0\,\text{kg}$ crate on a frictionless ledge is tied by a light rope over a smooth pulley to a $2.0\,\text{kg}$ bucket hanging freely. Taking $g = 9.8\,\text{m/s}^2$, what is the tension in the rope while they move?
  options:
    A: |-
      $11.8\,\text{N}$
    B: |-
      $19.6\,\text{N}$
    C: |-
      $29.4\,\text{N}$
    D: |-
      $7.84\,\text{N}$
  answer: A
  explanation: |-
    $a = \dfrac{m_2 g}{m_1 + m_2} = \dfrac{2.0 \times 9.8}{5.0} = 3.92\,\text{m/s}^2$. The rope is the only horizontal force on the crate, so $T = m_1 a = 3.0 \times 3.92 \approx 11.8\,\text{N}$.
  misconceptions:
    B: |-
      Assumes the tension equals the bucket's weight. That is only true if nothing accelerates; the bucket speeds up downwards, so its weight must be bigger than the tension.
    C: |-
      Uses the crate's weight. The crate's weight is balanced by the ledge's normal force and does not pull along the rope.
    D: |-
      Writes $T = m_2 a$ for the bucket, forgetting that its weight also acts on it. For the bucket, $m_2 g - T = m_2 a$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a racing game on the monitor and a zero-gravity game on a tablet](scenes/gaming/laws_of_motion.svg "A physics engine handles one body at a time, then lets ropes and contacts link them. That is also how you solve these problems.")

Zoya is building a puzzle for her gaming club's level-design contest. A wooden crate sits on a sheet of ice at the edge of a cliff, frictionless in the game. A rope runs from the crate, over a pulley at the cliff edge, down to a bucket hanging in mid-air. The player drops stones into the bucket until it is heavy enough to drag the crate across the ice and onto a switch.

She has turned on the editor's debug overlay, which shows a live number beside the rope: its tension, in newtons.

Her teammate Imran leans in to predict. "Easy one. The bucket's weight is 49 newtons, so the rope meter will say 49 the moment you let go. The rope's holding the bucket."

Zoya releases it. The bucket drops, the crate slides, and the meter reads a steady number well below 49.

"Bug," says Imran. Zoya isn't so sure. Is the rope really holding less than the bucket's weight? And if so, how much less?

## The physics

When bodies are joined, solve them **one body at a time**, each with its own free-body diagram, and let the rope link the equations.

For a **light, inextensible rope** over a **smooth, light pulley**:

- the **tension** $T$ is the same all along the rope;
- the rope can't stretch, so both bodies have the **same size of acceleration** $a$: the crate along the ice, the bucket downwards.

Then apply $F_\text{net} = ma$ to each body along its own direction of motion.

![Left: a body m1 on a smooth horizontal surface tied by a string over a pulley at the edge to a hanging body m2, with acceleration arrows. Right: free-body diagrams of m1 (N up, m1 g down, T towards the pulley) and m2 (T up, m2 g down, longer than T)](figures/connected_bodies/block-and-hanging-mass.svg "The crate is m1 and the bucket is m2. For the bucket, the weight arrow is longer than the tension, because the bucket speeds up downwards.")

**Crate** ($m_1$), horizontally: the only horizontal force is the tension.

$$T = m_1 a$$

(Vertically the ice's normal force balances the crate's weight: $N = m_1 g$.)

**Bucket** ($m_2$), taking downwards as positive: weight down, tension up.

$$m_2 g - T = m_2 a$$

Add the two equations and $T$ cancels:

$$a = \frac{m_2 g}{m_1 + m_2}, \qquad T = m_1 a = \frac{m_1 m_2}{m_1 + m_2}\,g$$

This settles the argument. The bucket accelerates downwards, so the net force on it points down, so its weight must be **bigger** than the tension. The rope carries **less** than the bucket's weight. Only if the bucket were held still would the meter read $m_2 g$.

## Worked example

**Given (illustrative values):** crate $m_1 = 15\,\text{kg}$ on frictionless ice; bucket with stones $m_2 = 5.0\,\text{kg}$ (weight $49\,\text{N}$, Imran's number); light rope, smooth pulley; $g = 9.8\,\text{m/s}^2$.
**Find:** the acceleration and the tension the meter shows.

$$a = \frac{m_2 g}{m_1 + m_2} = \frac{5.0 \times 9.8}{15 + 5.0} = \frac{49}{20} = 2.45\,\text{m/s}^2$$

$$T = m_1 a = 15 \times 2.45 \approx 36.8\,\text{N}$$

The meter reads about $36.8\,\text{N}$, three quarters of the bucket's $49\,\text{N}$ weight. Not a bug.

**Sanity check:** from the bucket's equation, $T = m_2(g - a) = 5.0 \times (9.8 - 2.45) = 5.0 \times 7.35 \approx 36.8\,\text{N}$ ✓. Limiting cases: if the crate had no mass, $a = g$ and $T = 0$ (the bucket free-falls); if the crate were enormous, $a \to 0$ and $T \to m_2 g$ (the bucket barely moves and the rope takes its full weight). Our answer sits between the two.

## Where the picture breaks

Real ice isn't frictionless, a real pulley has friction in its axle and a mass of its own, and a real rope stretches and has weight. Each of these changes the numbers: friction lowers the acceleration, and a heavy pulley makes the tension differ on its two sides. A game engine may also model a rope as a chain of short links that stretch slightly, so its meter might wobble around the ideal value. None of this changes the method: one free-body diagram per body, then solve them together.

## Key takeaway

For bodies joined by a light, inextensible rope, draw a free-body diagram for each, use the same tension $T$ and the same size of acceleration $a$ throughout, and write $F_\text{net} = ma$ for each body. For a body on a smooth surface pulled by a hanging body, $a = \dfrac{m_2 g}{m_1 + m_2}$ and $T = \dfrac{m_1 m_2 g}{m_1 + m_2}$, always less than the hanging weight while things accelerate.
