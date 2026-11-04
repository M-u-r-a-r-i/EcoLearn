---
concept_id: inertia_first_law
interest: smartphones
format: explain
title: The phone that slid off the metro seat
check:
  question: |-
    A phone lies flat on the floor of a lift that is moving upwards at a steady $2\,\text{m/s}$. Which statement about the forces on the phone is correct?
  options:
    A: |-
      The floor pushes up harder than the weight, because an upward motion needs an upward net force
    B: |-
      The floor pushes up exactly as hard as the weight, so the net force on the phone is zero
    C: |-
      The floor exerts no force at all, because the phone is simply carried along with the lift
    D: |-
      The net force is upwards and equal to the phone's mass times $2\,\text{m/s}$
  answer: B
  explanation: |-
    The phone's velocity is constant, so by Newton's first law the net force on it is zero. The only forces are the weight (down) and the floor's normal force (up), so they must be equal.
  misconceptions:
    A: |-
      Believes a moving body needs a force in its direction of motion. A force is needed to *change* velocity; at a steady $2\,\text{m/s}$ nothing is changing, so no net force is needed.
    C: |-
      Forgets that the phone is pressing on the floor. If the floor pushed with zero force, the weight would be unbalanced and the phone would fall through it; being carried *is* the floor's upward push.
    D: |-
      Multiplies mass by velocity and calls it a force. $mv$ is momentum; force is linked to the *change* in velocity, which here is zero.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A study room at night: a camera drone hovers pushing air down, a phone tumbles off a shelf towards the tiles, and a power bank dangles off a desk by its cable](scenes/smartphones/laws_of_motion.svg "Every gadget in this room is obeying the same three laws — including the ones sitting perfectly still.")

Tanvi is on the evening metro with her cousin Arnav, heading home after a long coaching class. The carriage is half empty, so she drops her phone face-up on the smooth plastic seat beside her while she digs in her bag for earphones.

For five minutes the train runs fast and smooth between stations, and the phone doesn't budge. Arnav even tosses his earbud case straight up a few times, and it lands back in his palm every time, though the train is moving at tens of metres per second.

Then the driver brakes for the next station. Tanvi's phone slides forward along the seat, skids off the end and lands on the floor with a clatter.

"The brakes threw it forward," Arnav says, picking it up.

Tanvi frowns. The brakes act on the wheels, under the floor. Nothing touched her phone. So what pushed it forward — or did anything push it at all?

## The physics

**Newton's first law** says: *a body stays at rest, or keeps moving in a straight line at constant speed, unless an external net force acts on it.* The property it describes is **inertia**: every body resists changes to its velocity, and the more mass it has, the more inertia.

Two consequences matter here.

- **Zero net force means constant velocity**, not "no motion". A body at rest and a body moving at a steady $20\,\text{m/s}$ are in the same situation as far as forces go: in both, the forces on it add to zero.
- **A force is needed to change velocity** — to speed up, slow down or turn — never just to keep going.

![Top row: a body on a very smooth surface shown every second, with equal gaps and its weight and normal force cancelling. Bottom row: on a rough surface an unbalanced friction force makes the gaps shrink](figures/inertia_first_law/zero-net-force-constant-velocity.svg "Top: balanced forces, equal gaps, constant velocity — the phone on a seat of a smoothly running train. Bottom: an unbalanced force changes the velocity.")

Now read the metro. While the train cruises, the phone's weight is balanced by the seat's upward normal force, and no horizontal force is needed, so the phone simply moves along at the train's speed. The same is true of the tossed earbud case: once it leaves Arnav's hand it keeps the train's forward velocity, so it comes down in his palm.

When the brakes come on, a large backward force acts on the *train*. On the phone there is only a little friction from the smooth seat — too small to slow it as fast as the train. So the phone carries on at nearly its old velocity while the seat slows down underneath it. Nothing threw the phone forward. The train dropped back, and the phone didn't.

## Worked example

**Given:** a phone of mass $0.20\,\text{kg}$ lies on a seat in a train running at a steady $20\,\text{m/s}$ in a straight line (illustrative). Take $g = 9.8\,\text{m/s}^2$.
**Find:** the vertical and horizontal forces on the phone, and what it does if the train brakes and the seat is very slippery.

1. *Vertical.* The phone does not move up or down, so the seat's push balances the weight:
$$N = mg = 0.20 \times 9.8 \approx 2.0\,\text{N}$$
That is about the weight of a small bottle of water.

2. *Horizontal.* The velocity is constant, so the net horizontal force is zero. On a level seat that means the friction on the phone is **zero** — no force is needed to keep it going at $20\,\text{m/s}$.

3. *Braking.* If the seat were perfectly smooth, no horizontal force could act on the phone at all. By the first law it would keep moving at $20\,\text{m/s}$ while the train slowed, so it would slide forward relative to the seat.

**Sanity check:** this is exactly why you lurch forward when a bus brakes — your body keeps the old velocity until the seat or a handrail pushes it back.

## Where the picture breaks

A real seat is not perfectly smooth, so a little friction does slow the phone; it slides only because friction can't slow it as quickly as the brakes slow the train. The first law also holds in its simple form only in an **inertial frame** — one that is not accelerating. The ground is a good enough inertial frame; the braking train is not, and from inside it the phone seems to be pushed forward by an invisible force. That "force" has no source. It is just the first law seen from a frame that is itself slowing down.

## Key takeaway

A body keeps its velocity — at rest or moving steadily in a straight line — unless a net external force acts on it. That resistance to change is inertia. When the metro braked, nothing pushed the phone forward: the train slowed, and the phone, with almost no force on it, kept going.
