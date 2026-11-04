---
concept_id: kinetic_energy
interest: smartphones
format: explain
title: Why the drone's sport mode comes with a warning
check:
  question: |-
    A $0.20\,\text{kg}$ phone slips out of a cyclist's pocket and is moving at $18\,\text{km/h}$ just before it hits the road. What is its kinetic energy at that moment?
  options:
    A: |-
      $32.4\,\text{J}$
    B: |-
      $0.50\,\text{J}$
    C: |-
      $5.0\,\text{J}$
    D: |-
      $2.5\,\text{J}$
  answer: D
  explanation: |-
    Convert first: $18\,\text{km/h} = 18/3.6 = 5.0\,\text{m/s}$. Then $K = \tfrac{1}{2}mv^2 = \tfrac{1}{2} \times 0.20 \times 5.0^2 = 0.10 \times 25 = 2.5\,\text{J}$.
  misconceptions:
    A: |-
      Puts the speed in km/h straight into the formula ($0.10 \times 18^2 = 32.4$). The joule is built on metres per second, so convert the speed before squaring.
    B: |-
      Forgets to square the speed ($0.10 \times 5.0$). Kinetic energy grows with the square of speed, not in proportion to it.
    C: |-
      Leaves out the factor of one half ($0.20 \times 5.0^2$). The $\tfrac{1}{2}$ comes from the work needed to build the speed up from rest.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A living room in the evening: a camera drone climbs straight up, a phone falls from a shelf towards a cushion, an earbuds case is whirled on a lanyard in a vertical circle, and a robot vacuum rolls towards a sofa leg](scenes/smartphones/work_energy_power.svg "Everything moving in this room carries energy because it is moving — the drone, the falling phone, the vacuum.")

Rohan's uncle has lent him a small camera drone for a cousin's wedding, on one condition: no sport mode near people.

In the open ground behind the hall, Rohan tries both. Normal mode cruises at a gentle pace, about as fast as a cyclist. Flick the switch and the drone suddenly tears across the ground at double that speed, the motors whining.

"It's only twice as fast," Rohan says, when his uncle frowns at him. "Same drone. Same weight. Why is that such a big deal?"

His uncle doesn't argue; he just points at the propeller guards in the box, and at the line in the manual: at higher speeds, a collision is far more dangerous.

Rohan wants a number. If the speed is doubled, how much more is the drone carrying into anything it hits — twice as much? Something else?

## The physics

A moving body can do work on whatever it hits: bend a propeller guard, push a person back, crack a screen. The energy a body has **because of its motion** is its **kinetic energy**:

$$K = \tfrac{1}{2}mv^2$$

where $m$ is its mass and $v$ its speed. It is a scalar, measured in joules, never negative, and independent of the direction of motion.

**Where it comes from.** Start a body of mass $m$ from rest and give it a constant net force $F$ along a straight line for a distance $d$. Then $a = F/m$ and, from the equations of motion, $v^2 = 2ad$. The work done is

$$W = Fd = (ma)\,d = m \cdot \frac{v^2}{2} = \tfrac{1}{2}mv^2$$

So $\tfrac{1}{2}mv^2$ is exactly the net work needed to bring the body from rest to speed $v$ — and the work that must be taken away to stop it.

Speed enters twice: a faster body needs a larger force, *and* it covers more ground while being stopped. So doubling the speed multiplies $K$ by $2^2 = 4$.

![A curve of kinetic energy against speed, both as multiples of a reference value, marked where doubling the speed gives four times the energy and tripling it gives nine times](figures/kinetic_energy/ke-ratio-vs-speed-ratio.svg "The curve bends upwards because K depends on v squared. Rohan's switch from normal to sport mode is the jump from 1x speed to 2x — and 1x energy to 4x.")

## Worked example

**Given:** the drone's mass is $m = 0.40\,\text{kg}$; normal mode $5.0\,\text{m/s}$, sport mode $10\,\text{m/s}$ (illustrative).
**Find:** the kinetic energy in each mode, and the net work the motors must do to get from hover to sport-mode speed.

1. *Normal mode:* $K = \tfrac{1}{2} \times 0.40 \times 5.0^2 = 0.20 \times 25 = 5.0\,\text{J}$.
2. *Sport mode:* $K = \tfrac{1}{2} \times 0.40 \times 10^2 = 0.20 \times 100 = 20\,\text{J}$ — four times as much, from twice the speed.
3. *From hover:* the drone starts with $K = 0$, so the net work done on it to reach $10\,\text{m/s}$ is $20\,\text{J}$ — and anything that stops it must absorb those same $20\,\text{J}$.

$20\,\text{J}$ is roughly what a $2\,\text{kg}$ brick gains falling from a one-metre-high table: not something you want to take in the face.

**Sanity check:** units give $\text{kg} \times (\text{m/s})^2 = \text{kg m}^2/\text{s}^2 = \text{J}$, and a larger speed gave a much larger energy, as the curve says.

## Where the picture breaks

The drone is a real case, not an analogy, but we left things out. Its propellers spin fast, and a spinning propeller carries extra energy of rotation that $\tfrac{1}{2}mv^2$ doesn't count — you'll meet rotational kinetic energy later. The motors also do far more than $20\,\text{J}$ of work in reaching that speed, because they are fighting air drag and holding the drone up the whole time; $20\,\text{J}$ is only the *net* work. And kinetic energy isn't the same as harm: how much a blow hurts depends on how quickly, and over how small an area, the energy is removed — which is exactly what propeller guards change.

## Key takeaway

Kinetic energy is the energy of motion, $K = \tfrac{1}{2}mv^2$. It equals the net work needed to bring a body from rest to speed $v$, and the work needed to stop it. Because it depends on $v^2$, doubling the speed quadruples the energy.
