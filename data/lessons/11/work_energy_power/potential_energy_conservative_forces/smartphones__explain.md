---
concept_id: potential_energy_conservative_forces
interest: smartphones
format: explain
title: Stairs or lift, the phone gains the same
check:
  question: |-
    A $0.50\,\text{kg}$ camera drone takes off from the ground, climbs $20\,\text{m}$, flies sideways over a building, then descends $5.0\,\text{m}$ to hover beside a balcony. Taking $g = 9.8\,\text{m/s}^2$, by how much has its gravitational potential energy changed since take-off?
  options:
    A: |-
      $+73.5\,\text{J}$
    B: |-
      $+122.5\,\text{J}$
    C: |-
      $+98\,\text{J}$
    D: |-
      $+7.5\,\text{J}$
  answer: A
  explanation: |-
    Gravity is conservative, so only the net height gained matters: $\Delta h = 20 - 5.0 = 15\,\text{m}$, and $\Delta U = mg\Delta h = 0.50 \times 9.8 \times 15 = 73.5\,\text{J}$. The sideways flight and the route taken don't count.
  misconceptions:
    B: |-
      Adds up the vertical distance flown, $20 + 5.0 = 25\,\text{m}$, as if the descent also stored energy. Potential energy depends only on where the drone ends up, not on how far it travelled.
    C: |-
      Uses the $20\,\text{m}$ climb and ignores the descent. Coming down $5\,\text{m}$ gives back $mg \times 5$ of the stored energy; only the final height above the start counts.
    D: |-
      Multiplies mass by height and forgets $g$ ($0.50 \times 15$). Potential energy is $mgh$; without $g$ the answer isn't even in joules.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A living room in the evening: a camera drone climbs straight up, a phone falls from a shelf towards a cushion, an earbuds case is whirled on a lanyard in a vertical circle, and a robot vacuum rolls towards a sofa leg](scenes/smartphones/work_energy_power.svg "The phone on the shelf and the climbing drone both hold energy just because of where they are.")

The lift in Meera's building is out again. She and her neighbour Farid have both just come home, both with phones in their pockets, both going to the third floor, ten metres up.

Meera takes the main staircase: short, steep, straight up. Farid, who is stubborn, takes the long ramp round the back that the delivery trolleys use. It winds three times round the building before it reaches the same landing.

"My phone went further," Farid says at the top, out of breath. "So it's got more energy stored in it now. If I drop it, it'll hit harder."

Meera's phone is sitting on the same landing, at the same height. Her route was a fraction of the length. Does the longer route really give Farid's phone more stored energy? And why did Farid's walk feel so much harder if it didn't?

## The physics

When a body is lifted, gravity does **negative** work on it. Gravity has a special property: the work it does between two points depends **only on the change in height**, not on the route. Going up $h$ by any path, gravity does $-mgh$; coming back down, it does $+mgh$; round a closed loop, it does zero.

A force with this property is called **conservative**. For such a force we can define a **potential energy** $U$: the work it will give back. Near the Earth's surface, where $g$ is nearly constant,

$$U = mgh$$

with $h$ measured from any level you choose as zero — only *changes* in $U$ matter.

![Two paths from A up to B, one short and straight, one long and winding: gravity does minus m g h on both, while friction does more negative work on the longer path](figures/potential_energy_conservative_forces/path-independence.svg "Gravity only counts the height gained — stairs or ramp. Friction charges you for every metre of the route.")

**Friction is non-conservative.** It always opposes the motion, so its work is $-f \times (\text{path length})$: a longer route means more negative work, and a closed loop still costs energy. There is no "frictional potential energy", because that energy is not stored — it becomes heat.

Gravity is conservative; the spring force is too. Friction and air drag are not.

## Worked example

**Given:** a phone of mass $m = 0.20\,\text{kg}$; the third-floor landing is $h = 10\,\text{m}$ above the ground (illustrative); $g = 9.8\,\text{m/s}^2$.
**Find:** the gain in potential energy of each phone.

1. *Meera's phone, by the stairs:* $\Delta U = mgh = 0.20 \times 9.8 \times 10 = 19.6\,\text{J} \approx 20\,\text{J}$.
2. *Farid's phone, by the ramp:* the same start and the same finish, so the same $\Delta U = 19.6\,\text{J}$. Gravity doesn't care about the route.
3. *Why Farid is tired:* his phone gained no extra stored energy, but he carried his whole body along a much longer path, and his muscles spent energy with every step. That extra energy ended up as heat, not as potential energy — just as friction's losses do.

**Sanity check:** $20\,\text{J}$ is the kinetic energy the phone would have if dropped back down those ten metres (ignoring air) — plenty to crack a screen, which fits experience.

## Where the picture breaks

The phones are real, not an analogy, but we have ignored a few things. $U = mgh$ is only accurate near the Earth's surface; far above it, $g$ weakens and you need a different formula, which you'll meet in Gravitation. Farid's tiredness is mostly biology — muscles turn food energy into heat even when walking on the level — so it is like friction's losses, not literally friction. And a dropped phone never quite gets its $20\,\text{J}$ back as speed, because air drag, a non-conservative force, takes some on the way down.

## Key takeaway

A force is **conservative** if the work it does depends only on the start and end points, not the path; gravity and springs are, friction is not. Only conservative forces have a potential energy, and near the Earth's surface the gravitational one is $U = mgh$.
