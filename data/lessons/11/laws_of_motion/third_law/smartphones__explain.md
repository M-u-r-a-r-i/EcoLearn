---
concept_id: third_law
interest: smartphones
format: explain
title: What actually holds a hovering drone up
check:
  question: |-
    A phone lies at rest on a table. By Newton's third law, which force is the reaction partner of the Earth's gravitational pull on the phone?
  options:
    A: |-
      The table's upward push on the phone
    B: |-
      The phone's downward push on the table
    C: |-
      The phone's upward gravitational pull on the Earth
    D: |-
      There is none, because the phone is not moving
  answer: C
  explanation: |-
    A third-law pair is the same kind of interaction between the same two bodies, acting on each other. The Earth pulls the phone down by gravity, so the phone pulls the Earth up by gravity, with an equal force.
  misconceptions:
    A: |-
      Picks the force that is equal and opposite to the weight. It is, but it acts on the *same* body (the phone) and is a contact force; those two balance by the first law, they are not a third-law pair.
    B: |-
      Picks a genuine third-law force, but the wrong pair: the phone pushing on the table is the partner of the *table's* push on the phone, not of gravity.
    D: |-
      Thinks the third law applies only during motion or collisions. Every force, at rest or not, is one half of an interaction and always has its partner.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A study room at night: a camera drone hovers pushing air down, a phone tumbles off a shelf towards the tiles, and a power bank dangles off a desk by its cable](scenes/smartphones/laws_of_motion.svg "The drone on the left is the story. Look at the two arrows: one on the drone, one on the air.")

At the school tech club, Farhan has brought his camera drone, and it is hovering at head height in the classroom, perfectly still, humming. Sneha walks right under it and her hair blows flat.

"Okay, so what's holding it up?" she asks.

"The motors," Farhan says. "Obviously."

"The motors are *part* of the drone," says Sneha. "You can't lift yourself by pulling on your own shoelaces. Something outside the drone has to be pushing it up."

Farhan thinks about it and points at her hair. "The air, then."

"Why would air push anything up? Air doesn't push *me* up."

Their teacher, Mr Joseph, leans back in his chair, clearly enjoying this. Neither of them is wrong, exactly — but neither has the full answer. What pushes on the drone, what does the drone push on, and how do the two forces relate?

## The physics

**Newton's third law:** *when body A exerts a force on body B, body B exerts a force on body A that is equal in magnitude and opposite in direction.*

$$\vec{F}_\text{AB} = -\vec{F}_\text{BA}$$

The two forces form an **action–reaction pair**, and three properties identify one:

- they act on **two different bodies** — one on each;
- they are the **same kind** of force (both contact, both gravitational…) and arise from one interaction;
- they are equal and opposite **at every instant**, whether or not anything is moving or accelerating.

Because they act on different bodies, **a third-law pair can never cancel.** Cancelling only makes sense for forces on the same body.

![While in contact, body A pushes body B one way and B pushes A the other way with an equal force; each force acts on a different body](figures/third_law/action-reaction-pair.svg "One force on each body. Here A is the spinning propeller and B is the air it throws down.")

Now the drone. The spinning propellers push a stream of air downwards — that is the wind on Sneha's hair. By the third law, the air pushes the propellers upwards with an equal force. That upward push is the outside force Sneha was asking for. Farhan was right that the air holds it up, and Sneha was right that the drone can't lift itself: it lifts itself *by pushing on something else*.

## Worked example

**Given:** the drone's mass is $0.50\,\text{kg}$ and it hovers at rest (illustrative). Take $g = 9.8\,\text{m/s}^2$.
**Find:** the forces on the drone, and each one's third-law partner.

1. *Weight.* The Earth pulls the drone down with
$$W = mg = 0.50 \times 9.8 = 4.9\,\text{N}$$
about the weight of half a litre of water.

2. *Air's push.* The drone is at rest, so by the *first* law the net force on it is zero. The air must push it up with $4.9\,\text{N}$.

3. *The partners.* The air's upward $4.9\,\text{N}$ on the drone pairs with the drone's downward $4.9\,\text{N}$ on the air. The Earth's downward $4.9\,\text{N}$ on the drone pairs with the drone's upward $4.9\,\text{N}$ pull on the *Earth*.

So the drone has two forces on it, equal and opposite — and they are **not** a third-law pair. They act on the same body and are of different kinds. They are equal only because the drone happens to be hovering.

**Sanity check:** if Farhan makes the drone speed up upwards, the air's push on the drone becomes bigger than its weight; the pair "drone on air, air on drone" is still exactly equal, because the third law never depends on how things move.

## Where the picture breaks

"The propellers push the air" is a simplification: the air moves along the blade surfaces and the push is spread over them, so a real drone's thrust varies with blade speed, air density and whether it is close to the floor. The drone's pull on the Earth is perfectly real, but the Earth's mass is so enormous that the resulting acceleration is unmeasurably small — that is why we never notice half of every gravity pair.

## Key takeaway

Forces always come in pairs: if A pushes or pulls B, then B pushes or pulls A equally hard in the opposite direction. The pair acts on two different bodies, so it never cancels. A hovering drone stays up because it pushes air down and the air pushes it up.
