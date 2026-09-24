---
concept_id: impulse
interest: motorsport
format: explain
title: Why they stack old tyres in front of a concrete wall
check:
  question: |-
    A $500\,\text{kg}$ single-seater (with driver) hits a barrier at $20\,\text{m/s}$ and is brought to rest in $0.50\,\text{s}$. What is the average force on the car?
  options:
    A: |-
      $1.0 \times 10^4\,\text{N}$
    B: |-
      $2.0 \times 10^5\,\text{N}$
    C: |-
      $2.0 \times 10^4\,\text{N}$
    D: |-
      $40\,\text{N}$
  answer: C
  explanation: |-
    The change in momentum is $500 \times 20 = 1.0 \times 10^4\,\text{kg m/s}$, so $F_\text{avg} = \Delta p / \Delta t = 1.0 \times 10^4 / 0.50 = 2.0 \times 10^4\,\text{N}$.
  misconceptions:
    A: |-
      Works out the impulse, $1.0 \times 10^4\,\text{N s}$, and stops there. Impulse is force multiplied by time, so the force is found by dividing by the time, not by reading the impulse off.
    B: |-
      Uses the kinetic energy $\tfrac{1}{2}mv^2 = 1.0 \times 10^5\,\text{J}$ divided by the time. That gives a power in watts; force comes from momentum, not energy.
    D: |-
      Divides the speed by the time to get the acceleration, $40\,\text{m/s}^2$, and labels it as a force. The mass has to be multiplied in.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race car in a braking zone with glowing brake discs, a skid mark and tyre smoke, a tyre barrier along the wall and a marshal with a yellow flag](scenes/motorsport/laws_of_motion.svg "Look at the tyre stack in front of the wall. It is not decoration.")

At six in the morning, before anyone else reaches the club circuit, Zoya and the other volunteer marshals are pulling old tyres off a truck and strapping them into stacks along the concrete wall at the fast right-hander. It takes three hours.

Manjeet, out for the first time, thinks the whole job is theatre. "It's a wall," he says, heaving another tyre onto the pile. "If a car hits it hard, it stops. Tyres or no tyres, it stops."

At about eleven, a car does exactly that. A front wheel locks on the way in, the car runs wide and buries its nose in the tyre stack. The stack bulges, the straps stretch, loose tyres roll down the track — and the driver climbs out, raises a hand to the grandstand and walks back to the pits.

Manjeet is right about one thing. The car went from full speed to a standstill either way. So what did three hours of stacking tyres actually change?

## The physics

Start from Newton's second law written for an average force over a time $\Delta t$:

$$\vec{F}_\text{avg} = \frac{\Delta \vec{p}}{\Delta t}$$

Multiply both sides by $\Delta t$ and the product of force and time gets its own name, the **impulse** $\vec{J}$:

$$\vec{J} = \vec{F}_\text{avg}\,\Delta t = \Delta \vec{p}$$

It is a vector in the direction of the force, and its SI unit is the newton second, $\text{N s}$, the same thing as $\text{kg m/s}$. In words:

**impulse = change in momentum.**

Now look at the crash. The car arrives with a certain momentum and ends at rest, so the **change in momentum is fixed** — by the car's mass and speed, not by what it hits. The impulse the barrier must deliver is therefore fixed too. But impulse is a *product*, force multiplied by time. Stretch the time and the force must shrink in exactly the same proportion:

$$F_\text{avg} = \frac{\Delta p}{\Delta t}$$

Concrete stops the car in a fraction of a tenth of a second, so the force is enormous. A tyre stack squashes, the straps stretch, the whole pile shoves sideways — and the same momentum is removed over several times as long, with several times less force.

The force during a real impact is not constant, so the exact statement is that the impulse is the **area under the force–time graph**. Two stops of the same car have the same area, but a long low hump is survivable where a tall narrow spike is not.

![Force–time graph with two triangles of equal area: a tall narrow spike over 20 ms and a low wide hump over 100 ms](figures/impulse/force-time-stiff-vs-soft.svg "Both curves enclose the same area, so both deliver the same impulse. Spreading it over five times the time cuts the peak force five times. The numbers shown are for a small object; the shapes are the lesson.")

Crumple zones, helmet liners, gravel traps and the foam inside racing seats all do the same single thing: they lengthen the stop.

## Worked example

**Given:** car plus driver $m = 500\,\text{kg}$ (illustrative), hitting a barrier at $20\,\text{m/s}$ and coming to rest. Against a rigid concrete wall the stop takes $\Delta t_1 = 0.10\,\text{s}$; into the tyre stack it takes $\Delta t_2 = 0.40\,\text{s}$.
**Find:** the impulse, and the average force in each case.

Take the direction of travel as positive, so $u = +20\,\text{m/s}$ and $v = 0$.

$$J = \Delta p = m(v - u) = 500 \times (0 - 20) = -1.0 \times 10^{4}\,\text{N s}$$

The minus sign says the impulse points backwards, against the motion. Its size, $1.0 \times 10^{4}\,\text{N s}$, is the same for both barriers.

*Concrete wall:*

$$F_1 = \frac{1.0 \times 10^{4}}{0.10} = 1.0 \times 10^{5}\,\text{N}$$

That is roughly the weight of a ten-tonne truck, and it corresponds to a deceleration of about $20g$.

*Tyre stack:*

$$F_2 = \frac{1.0 \times 10^{4}}{0.40} = 2.5 \times 10^{4}\,\text{N}$$

Roughly the weight of a small van, and about $5g$ — the difference between a broken driver and a driver who walks away.

**Sanity check:** the stop lasts four times as long, and the force comes out four times smaller, which is exactly what a fixed impulse demands.

## Where the picture breaks

A real impact force rises and falls, so its peak is higher than the average that $\Delta p / \Delta t$ gives. The change in momentum is only fixed if the car really ends at rest: a barrier that *bounces* the car back changes the momentum by more, and so needs a bigger impulse, which is why soft barriers are designed to absorb rather than rebound. Whether a driver survives also depends on how the force is spread over the body and on where the kinetic energy goes, not on force alone. And no barrier is a simple spring — real ones are engineered and tested, not just piled up.

## Key takeaway

Impulse is force multiplied by the time it acts, $\vec{J} = \vec{F}_\text{avg}\,\Delta t$, and it equals the change in momentum, $\Delta\vec{p}$. When the change in momentum is fixed, lengthening the collision time reduces the average force in the same proportion. That single idea is the tyre barrier, the crumple zone and the helmet liner.
