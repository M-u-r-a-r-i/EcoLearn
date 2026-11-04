---
concept_id: momentum_conservation
interest: smartphones
format: explain
title: Bumper tag with app-controlled cars
check:
  question: |-
    A $0.50\,\text{kg}$ toy car rests on a smooth floor. A spring launcher on its roof fires a $0.050\,\text{kg}$ foam dart forwards at $10\,\text{m/s}$. What is the car's velocity just after the shot?
  options:
    A: |-
      $1.0\,\text{m/s}$, backwards
    B: |-
      $1.0\,\text{m/s}$, forwards
    C: |-
      $10\,\text{m/s}$, backwards
    D: |-
      Zero, because the spring is part of the car
  answer: A
  explanation: |-
    The total momentum starts at zero and stays zero. So $0.050 \times 10 + 0.50\,v = 0$, giving $v = -1.0\,\text{m/s}$: the car recoils backwards at $1.0\,\text{m/s}$.
  misconceptions:
    B: |-
      Gets the size right but loses the sign. For a total of zero, the car's momentum must be opposite to the dart's, so it moves backwards.
    C: |-
      Assumes the two bodies fly apart at equal *speeds*. It is their *momenta* that are equal and opposite; the car is ten times heavier, so it moves ten times slower.
    D: |-
      Thinks an internal force cannot move anything. Internal forces cannot change the *total* momentum, but they can push the parts apart; the spring pushes the dart forwards and the car backwards.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A study room at night: a camera drone hovers pushing air down, a phone tumbles off a shelf towards the tiles, and a power bank dangles off a desk by its cable](scenes/smartphones/laws_of_motion.svg "Gadgets push on each other all the time. When nothing outside interferes, their total momentum never changes.")

Manav and Ishita have two identical toy cars, each driven from a phone app over Bluetooth, with magnetic bumpers on the front and back. Their game is bumper tag on the smooth corridor floor: ram the other car and the magnets latch.

Ishita parks her car in the middle of the corridor and lets go of the controls completely. Manav lines up at the far end, floors it, then — to make it fair, he says — cuts the motor just before impact, so his car is coasting.

"When I hit you, we'll roll away together at my full speed," he says. "Nothing's slowing my car down. The speed has to go somewhere."

Ishita props her phone on the floor to film it in slow motion. Click — the magnets latch, and the pair roll off down the corridor together, clearly slower than Manav's car was going.

Where did the speed go? And is there something that *didn't* change when the two cars locked together?

## The physics

For a **system** of bodies, the forces they exert on each other are **internal** forces; everything else (gravity, the floor, friction, a hand) is **external**. By Newton's third law, internal forces come in equal and opposite pairs, and each pair gives equal and opposite impulses. So internal forces can swap momentum between the bodies, but can never change the total.

That gives the **law of conservation of linear momentum**:

$$\text{If } \vec{F}_\text{ext,net} = 0, \quad \vec{p}_\text{total} = m_1\vec{v}_1 + m_2\vec{v}_2 + \dots = \text{constant}$$

A system with no net external force is called **isolated**. The law applies to three kinds of event you will meet constantly:

- **Recoil and explosions:** bodies start at rest, so the total is zero, and afterwards the momenta are equal and opposite.
- **Sticking (perfectly inelastic) collisions:** bodies join and move with one common velocity.
- **Collisions in general:** the total momentum just before equals the total just after.

![Top: two bodies at rest flying apart with equal and opposite momentum arrows. Bottom: a body moving into a stationary one; afterwards they travel together with the same total momentum](figures/momentum_conservation/recoil-and-sticking-collision.svg "The bottom row is bumper tag: one moving car, one parked car, then both rolling together with the same total momentum as before.")

On the corridor, the weights of the cars are balanced by the floor, and friction on free-rolling wheels is small over the instant of the crash. So the two cars form an isolated system, and Manav's momentum is shared between twice the mass.

## Worked example

**Given:** each car has mass $1.0\,\text{kg}$; Manav's coasts at $2.0\,\text{m/s}$ into Ishita's parked car, and they latch (illustrative).
**Find:** their common velocity, and what it would be if Ishita's were a $3.0\,\text{kg}$ toy truck.

1. *Momentum before.* Taking Manav's direction as positive, only his car is moving:
$$p = 1.0 \times 2.0 = 2.0\,\text{kg m/s}$$

2. *After, with equal cars.* The same $2.0\,\text{kg m/s}$ is carried by $2.0\,\text{kg}$:
$$v = \frac{2.0}{1.0 + 1.0} = 1.0\,\text{m/s}$$
Exactly half the speed — a slow walk instead of a gentle jog.

3. *After, with the truck.* The same momentum, now carried by $4.0\,\text{kg}$:
$$v = \frac{2.0}{1.0 + 3.0} = 0.50\,\text{m/s}$$

**Sanity check:** when a light car latches onto a heavy one the pair should barely move, and a quarter of the original speed for four times the mass fits.

## Where the picture breaks

The corridor is not perfectly isolated: rolling friction and the motors' gearboxes slow the pair down after the crash, so the conservation law applies to the instant just before and just after impact, not to the whole roll. Manav's "the speed has to go somewhere" is a good instinct about *energy*, not speed: kinetic energy is not conserved in a sticking collision — some goes into sound, into flexing the plastic and into heat. You'll meet that in Work, Energy and Power. Momentum is the quantity that survives.

## Key takeaway

When the net external force on a system is zero, its total momentum stays constant: internal forces can only pass momentum between the parts. After a recoil the parts' momenta are equal and opposite; after a sticking collision the joined bodies share the original momentum, $v = \dfrac{m_1 v_1}{m_1 + m_2}$ for a moving body hitting a stationary one.
