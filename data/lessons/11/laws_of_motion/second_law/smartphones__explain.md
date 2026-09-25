---
concept_id: second_law
interest: smartphones
format: explain
title: How hard is the phone holder pushing
check:
  question: |-
    A $3.0\,\text{kg}$ robot vacuum speeds up steadily from rest to $0.60\,\text{m/s}$ in $2.0\,\text{s}$, then cruises at a steady $0.60\,\text{m/s}$ in a straight line. What is the net force on it while it speeds up, and while it cruises?
  options:
    A: |-
      $0.90\,\text{N}$ while speeding up; zero while cruising
    B: |-
      $1.8\,\text{N}$ while speeding up; zero while cruising
    C: |-
      $0.30\,\text{N}$ while speeding up; zero while cruising
    D: |-
      $0.90\,\text{N}$ while speeding up; $0.90\,\text{N}$ while cruising
  answer: A
  explanation: |-
    While speeding up, $a = 0.60/2.0 = 0.30\,\text{m/s}^2$, so $F_\text{net} = ma = 3.0 \times 0.30 = 0.90\,\text{N}$. While cruising the velocity is constant, so the acceleration and the net force are both zero.
  misconceptions:
    B: |-
      Calculates the change in momentum, $3.0 \times 0.60 = 1.8\,\text{kg m/s}$, and calls it a force. Force is the change in momentum *per second*, so divide by the $2.0\,\text{s}$.
    C: |-
      Works out the acceleration, $0.30\,\text{m/s}^2$, and writes it with the unit newton. It only becomes a force after multiplying by the mass.
    D: |-
      Gets the first part right but believes a net force is needed to keep a body moving. At constant velocity the net force is zero; the wheels' drive only has to cancel friction.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A study room at night: a camera drone hovers pushing air down, a phone tumbles off a shelf towards the tiles, and a power bank dangles off a desk by its cable](scenes/smartphones/laws_of_motion.svg "Wherever a gadget speeds up, slows down or turns, a net force is doing it.")

Rhea's father has clipped a new phone holder to the car's air vent, and Rhea, in the passenger seat, has found a sensor app that reads the phone's accelerometer live. At the traffic light the graph sits flat at zero.

The light turns green. Her father pulls away briskly and the forward reading jumps and holds steady for a few seconds, then drops back to zero as the car settles into a steady speed on the flyover.

"How does a phone even know it's accelerating?" she asks. "It's just sitting in a clip."

Her father, who repairs electronics, says the accelerometer chip has a tiny mass inside, hung on microscopic springs. The springs have to push that mass to make it keep up with the phone. The harder they push, the bigger the reading.

Rhea looks at the clip gripping her phone. It must be doing the same job on the whole phone. So how hard is it pushing — and why does the reading fall to zero while the car is still moving fast?

## The physics

Newton's second law says the **net force** on a body equals the rate of change of its momentum:

$$\vec{F}_\text{net} = \frac{d\vec{p}}{dt}$$

When the mass is constant, $\dfrac{d\vec{p}}{dt} = m\dfrac{d\vec{v}}{dt} = m\vec{a}$, which gives the familiar form

$$\vec{F}_\text{net} = m\vec{a}$$

- The force is the **net** force: the vector sum of every force on the body.
- It points the **same way as the acceleration**, which need not be the way the body is moving.
- Its unit is defined by the law: $1\,\text{N} = 1\,\text{kg m/s}^2$.

![Two graphs: with the mass fixed, acceleration rises in a straight line as the net force grows; with the force fixed, acceleration falls along a curve as the mass grows](figures/second_law/force-mass-acceleration.svg "Left: for one phone, twice the acceleration needs twice the net force from the holder. Right: for one force, a heavier body accelerates less.")

In the car, the phone's weight is balanced by the holder's upward grip, so the **net** force on the phone is the holder's forward push. That push is exactly what gives the phone the car's acceleration. The chip inside works on the same law: its springs supply $F = ma$ to the tiny mass, and the chip measures how much the springs are bent. At steady speed on the flyover, $a = 0$, so the net force is zero and the reading falls — even at $60\,\text{km/h}$. The law cares about *changes* in velocity.

## Worked example

**Given:** the phone's mass is $m = 0.20\,\text{kg}$; the app shows a steady forward acceleration $a = 2.0\,\text{m/s}^2$ (illustrative).
**Find:** the net force the holder exerts on the phone, and check it with $F = dp/dt$.

1. *Using $F = ma$.*
$$F_\text{net} = ma = 0.20 \times 2.0 = 0.40\,\text{N}, \text{ forwards}$$
That is about the weight of a $40\,\text{g}$ chocolate bar — gentle, which is why a light clip can manage it.

2. *Using momentum.* The phone gains $2.0\,\text{m/s}$ of speed each second, so each second its momentum grows by
$$\frac{\Delta p}{\Delta t} = \frac{0.20 \times 2.0}{1.0} = 0.40\,\text{kg m/s per second} = 0.40\,\text{N}$$
The same answer, as it must be: for constant mass the two forms are one law.

3. *At steady speed.* $a = 0$, so $F_\text{net} = 0$: the holder only has to hold the phone up.

**Sanity check:** a hard stop in a car can reach several times $2\,\text{m/s}^2$, which is why phones sometimes fly out of weak holders under heavy braking.

## Where the picture breaks

We treated the acceleration as steady; in real driving it rises and falls, so $0.40\,\text{N}$ is an average over those few seconds. The holder's push is also not the only horizontal force if the car is on a slope or turning a corner — then part of the weight or a sideways push joins in, and it is the vector sum that equals $m\vec{a}$. And the accelerometer does not measure acceleration directly; it measures the spring force on its tiny mass and divides by that mass, which is the second law used in reverse.

## Key takeaway

The net force on a body is its rate of change of momentum, $\vec{F}_\text{net} = d\vec{p}/dt$, which for constant mass is $\vec{F}_\text{net} = m\vec{a}$. A phone in a holder needs a net forward force only while the car's velocity is changing; at steady speed, however fast, the net force is zero.
