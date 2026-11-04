---
concept_id: connected_bodies
interest: football
format: explain
title: The ball cart that was meant to be a brake
check:
  question: |-
    A $7.0\,\text{kg}$ ball cart on a smooth, level floor is tied by a light rope over a smooth pulley to a $3.0\,\text{kg}$ bag hanging freely. Ignoring friction and taking $g = 9.8\,\text{m/s}^2$, what is the tension in the rope while they move?
  options:
    A: |-
      $29.4\,\text{N}$
    B: |-
      $20.6\,\text{N}$
    C: |-
      $68.6\,\text{N}$
    D: |-
      $8.82\,\text{N}$
  answer: B
  explanation: |-
    $a = \dfrac{m_2 g}{m_1 + m_2} = \dfrac{3.0 \times 9.8}{10} = 2.94\,\text{m/s}^2$. The rope is the only horizontal force on the cart, so $T = m_1 a = 7.0 \times 2.94 \approx 20.6\,\text{N}$.
  misconceptions:
    A: |-
      Assumes the tension equals the hanging bag's weight. That is true only if nothing accelerates; the bag speeds up downwards, so its weight must be bigger than the tension.
    C: |-
      Uses the weight of the cart. The cart's weight is balanced by the floor's normal force and plays no part in its horizontal motion.
    D: |-
      Writes $T = m_2 a$ for the hanging bag, forgetting that its weight also acts on it. For the bag, $m_2 g - T = m_2 a$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![Under floodlights, a striker follows through after a shot while the ball flies towards the goalkeeper](scenes/football/laws_of_motion.svg "Before any match, somebody has to get the kit to the pitch, and the same laws apply.")

The kit room at the club ground is on the first floor of the old stand, with a loading door that opens straight over the pitch-side path. An old pulley is still fixed above the door. It's matchday, and Leela, the kit manager, needs a net bag of twenty training balls down on the path.

Her assistant, Joseph, has a clever idea. He ties the bag to one end of a rope, runs the rope over the pulley, and ties the other end to the heavy wheeled ball cart standing on the smooth floor behind them. "The cart is three times heavier than the bag," he says. "It'll act as a brake. The bag will just hang there until we lower it."

He eases the bag out of the door and lets go. The bag drops, and the cart rolls across the floor towards the door. Leela grabs it just in time.

"But the cart is much heavier!" Joseph says. "Why didn't it hold?" And how hard was that old rope actually pulling?

## The physics

For bodies tied together, solve one body at a time, each with its own free-body diagram, and let the string link the equations.

For a **light, inextensible string** over a **smooth, light pulley**:

- the **tension** $T$ is the same all along the string;
- the string can't stretch, so both bodies move with the **same size of acceleration** $a$: the cart along the floor, the bag downwards.

Then apply $F_\text{net} = ma$ to each body along its own direction of motion.

![Left: a body m1 on a smooth horizontal surface tied by a string over a pulley at the edge to a hanging body m2, with acceleration arrows. Right: free-body diagrams of m1 (N up, m1 g down, T towards the pulley) and m2 (T up, m2 g down, longer than T)](figures/connected_bodies/block-and-hanging-mass.svg "The cart is m1 and the bag is m2. One diagram per body; for the bag, the weight arrow is longer than the tension because the bag speeds up downwards.")

**Cart** ($m_1$), horizontally: the only horizontal force is the tension.

$$T = m_1 a$$

(Vertically, $N = m_1 g$: the cart's weight is balanced by the floor and does not resist horizontal motion at all.)

**Bag** ($m_2$), with downwards as positive: weight down, tension up.

$$m_2 g - T = m_2 a$$

Add the two equations and $T$ drops out:

$$a = \frac{m_2 g}{m_1 + m_2}, \qquad T = m_1 a = \frac{m_1 m_2}{m_1 + m_2}\,g$$

This answers Joseph. On a smooth floor, the cart's mass only *slows* the acceleration; it can never make it zero, because nothing horizontal holds the cart back. A brake needs a horizontal force, such as friction, and a heavy cart on smooth wheels supplies almost none. And because the bag accelerates downwards, its weight must be bigger than the tension: the rope carries **less** than the bag's full weight.

## Worked example

**Given:** cart $m_1 = 27\,\text{kg}$ on a smooth level floor; bag of balls $m_2 = 9.0\,\text{kg}$ hanging (illustrative values: twenty balls of about $0.43\,\text{kg}$ plus the net). Friction, rope mass and pulley friction neglected; $g = 9.8\,\text{m/s}^2$.
**Find:** the acceleration and the tension.

$$a = \frac{m_2 g}{m_1 + m_2} = \frac{9.0 \times 9.8}{27 + 9.0} = \frac{88.2}{36} = 2.45\,\text{m/s}^2$$

$$T = m_1 a = 27 \times 2.45 \approx 66\,\text{N}$$

The bag weighs $88.2\,\text{N}$, so the rope carries only about $75\%$ of it while things accelerate.

**Sanity check:** from the bag's equation, $T = m_2(g - a) = 9.0 \times (9.8 - 2.45) = 9.0 \times 7.35 \approx 66\,\text{N}$ ✓. Limiting cases: if $m_1 = 0$, then $a = g$ and $T = 0$, and the bag simply free-falls; if $m_1$ is enormous, $a \to 0$ and $T \to m_2 g$, so the bag barely moves and the rope holds its full weight. Our answer sits between the two.

## Where the picture breaks

A real cart has rolling friction in its wheels and the old pulley has friction in its axle, so the real acceleration is a bit smaller, and the tension on the two sides of the pulley differs slightly. With enough friction the cart really could act as a brake, which is why a friction lesson comes next. A real rope stretches a little and has mass, and a net of balls is not a rigid block. None of that changes the method: one free-body diagram per body, then solve together. (Don't try this at a real stand: a bag dropping from a first floor is dangerous to anyone below.)

## Key takeaway

For bodies joined by a light, inextensible string, draw a free-body diagram for each, use the same tension $T$ and the same size of acceleration $a$ for all, and write $F_\text{net} = ma$ for each body. For a body on a smooth table pulled by a hanging body, $a = \dfrac{m_2 g}{m_1 + m_2}$ and $T = \dfrac{m_1 m_2 g}{m_1 + m_2}$, which is always less than the hanging weight while the system accelerates.
