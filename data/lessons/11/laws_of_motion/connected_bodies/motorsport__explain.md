---
concept_id: connected_bodies
interest: motorsport
format: explain
title: How much is the tow rope really carrying?
check:
  question: |-
    A $1200\,\text{kg}$ car tows a $400\,\text{kg}$ trailer on a level road with a light tow bar. The road's driving force on the car is $3200\,\text{N}$. Ignoring friction and air drag, what is the force in the tow bar?
  options:
    A: |-
      $2400\,\text{N}$
    B: |-
      $1600\,\text{N}$
    C: |-
      $800\,\text{N}$
    D: |-
      $3200\,\text{N}$
  answer: C
  explanation: |-
    For the pair, $a = 3200/(1200+400) = 2.0\,\text{m/s}^2$. The tow bar is the only horizontal force on the trailer, so $T = 400 \times 2.0 = 800\,\text{N}$.
  misconceptions:
    A: |-
      Uses the car's mass ($1200 \times 2.0$) instead of the trailer's. The tow bar has to accelerate the trailer, so it is the trailer's mass that belongs in $T = ma$.
    B: |-
      Halves the driving force, as though the two bodies shared it equally. They share it in proportion to their masses, and the trailer is only a quarter of the total.
    D: |-
      Assumes the link carries the whole driving force. The driving force has to accelerate car *and* trailer; the bar only has to accelerate the trailer.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race car in a braking zone with glowing brake discs, a skid mark and tyre smoke, a tyre barrier along the wall and a marshal with a yellow flag](scenes/motorsport/laws_of_motion.svg "When a car cannot get itself home, something else has to accelerate it — through a rope.")

The club runs a recovery session on a closed stretch of test road every winter: how to hook up a stranded car, how to tow it, how not to wreck both cars in the process. Lakshmi's uncle has brought his old four-wheel drive to do the towing, and the stranded car is a hatchback with its engine switched off on purpose.

Joseph has to shackle on the rope, and he keeps turning it over in his hands, unhappy about a frayed patch near one end.

"That truck can pull four thousand newtons," he says. "So this rope has to take four thousand newtons. It'll snap the moment he opens the throttle."

The four-wheel drive eases away, the rope snaps taut, and both cars accelerate up the road together. Nothing breaks.

Joseph was worried about the right thing. But was he right about the number? Is the rope really carrying the whole of the tow vehicle's pull — or less, or more?

## The physics

When bodies are tied together, solve them **one body at a time**, each with its own free-body diagram, and let the connection link the equations.

For a **light, inextensible** rope (or tow bar, or string over a smooth, light pulley):

- the **tension** $T$ is the same all along it;
- it cannot stretch, so every body joined by it has the **same size of acceleration** $a$.

Then write $F_\text{net} = ma$ for each body along its own direction of motion.

**The tow.** Call the tow vehicle $m_1$ and the towed car $m_2$, and let $F$ be the net forward force the road gives it. Taking forwards as positive:

$$\text{tow vehicle: } F - T = m_1 a \qquad \text{towed car: } T = m_2 a$$

The rope pulls the towed car forwards, and by Newton's third law it pulls the tow vehicle backwards — that is why $T$ appears with opposite signs. Adding the two equations makes $T$ vanish:

$$a = \frac{F}{m_1 + m_2}, \qquad T = m_2 a = \frac{m_2}{m_1 + m_2}\,F$$

So the rope carries only the towed car's **share of the total mass** — always less than the tow vehicle's pull. Joseph's fear was the right instinct applied to the wrong number.

The same method handles the other arrangement you will meet constantly, a body on a table pulled by a hanging body over a pulley:

![A body on a smooth horizontal surface tied by a string over a pulley at the edge to a hanging body, with a separate free-body diagram for each: normal force, weight and tension on one, tension up and a longer weight arrow on the other](figures/connected_bodies/block-and-hanging-mass.svg "One free-body diagram per body, the same tension in both, the same size of acceleration. The hanging body's weight arrow is longer than the tension — that is why it speeds up downwards.")

There, $m_2 g - T = m_2 a$ and $T = m_1 a$, giving $a = \dfrac{m_2 g}{m_1 + m_2}$ and $T = \dfrac{m_1 m_2}{m_1 + m_2}\,g$ — again, less than the hanging weight, for exactly the same reason: a body that is accelerating must have a net force on it.

## Worked example

**Given:** tow vehicle $m_1 = 2000\,\text{kg}$, towed car $m_2 = 1000\,\text{kg}$ (illustrative), joined by a light rope. The net forward force on the tow vehicle is $F = 3000\,\text{N}$. Friction and air drag on the towed car are neglected.
**Find:** the acceleration of the pair, and the tension in the rope.

*The pair together.* The rope's pulls are internal to this system and cancel, so:

$$a = \frac{F}{m_1 + m_2} = \frac{3000}{3000} = 1.0\,\text{m/s}^2$$

Both cars gain one metre per second of speed each second — gentle, about $3.6\,\text{km/h}$ per second.

*The towed car alone.* The rope is the only horizontal force on it:

$$T = m_2 a = 1000 \times 1.0 = 1000\,\text{N}$$

A third of the tow vehicle's pull, which is exactly the towed car's third of the total mass.

**Sanity check:** check it on the tow vehicle instead — $F - T = 3000 - 1000 = 2000\,\text{N}$, and $m_1 a = 2000 \times 1.0 = 2000\,\text{N}$, so both equations agree.

## Where the picture breaks

A real tow rope stretches, has mass, and — worst of all — goes slack and then snatches tight, and the brief force in a snatch can be many times the steady $1000\,\text{N}$ we calculated. That is what actually breaks ropes, and why recovery is done gently. The towed car also has its own rolling resistance and air drag, which the rope must overcome as well, so the real tension is higher than our idealised value. On a slope, part of each car's weight joins in too. None of that changes the method: one free-body diagram per body, one shared tension, one shared acceleration.

## Key takeaway

For bodies joined by a light, inextensible link, use the same tension $T$ and the same size of acceleration $a$ for all of them, and write $F_\text{net} = ma$ for each body separately. For a tow on a level road, $a = \dfrac{F}{m_1 + m_2}$ and $T = \dfrac{m_2}{m_1+m_2}F$; for a hanging mass over a pulley, $a = \dfrac{m_2 g}{m_1 + m_2}$ and $T = \dfrac{m_1 m_2 g}{m_1 + m_2}$. The link never carries the whole driving force while the system is accelerating.
