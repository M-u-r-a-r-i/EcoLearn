---
concept_id: work_energy_theorem
interest: smartphones
format: explain
title: The phone slid across the canteen table
check:
  question: |-
    A $3.0\,\text{kg}$ robot vacuum is rolling at $0.40\,\text{m/s}$. Over the next $0.50\,\text{m}$ the net force on it is a steady $0.60\,\text{N}$ forward. What is its speed at the end of that $0.50\,\text{m}$?
  options:
    A: |-
      $0.45\,\text{m/s}$
    B: |-
      $0.60\,\text{m/s}$
    C: |-
      $0.85\,\text{m/s}$
    D: |-
      $0.54\,\text{m/s}$
  answer: B
  explanation: |-
    $K_i = \tfrac{1}{2} \times 3.0 \times 0.40^2 = 0.24\,\text{J}$ and $W_\text{net} = 0.60 \times 0.50 = 0.30\,\text{J}$, so $K_f = 0.54\,\text{J}$. Then $v = \sqrt{2K_f/m} = \sqrt{2 \times 0.54 / 3.0} = \sqrt{0.36} = 0.60\,\text{m/s}$.
  misconceptions:
    A: |-
      Turns the $0.30\,\text{J}$ of work into a speed as if the vacuum started from rest ($\sqrt{2 \times 0.30/3.0} \approx 0.45$). The work *changes* the kinetic energy; it must be added to the $0.24\,\text{J}$ already there.
    C: |-
      Finds the speed the work alone would give, $0.45\,\text{m/s}$, and adds it to $0.40\,\text{m/s}$. Speeds don't add like that — energies do, because $K$ goes as $v^2$.
    D: |-
      Gets the final kinetic energy right, $0.54\,\text{J}$, then reports it as the speed. Energy and speed are different quantities; take $v = \sqrt{2K/m}$.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![A living room in the evening: a camera drone climbs straight up, a phone falls from a shelf towards a cushion, an earbuds case is whirled on a lanyard in a vertical circle, and a robot vacuum rolls towards a sofa leg](scenes/smartphones/work_energy_power.svg "Anything sliding or rolling in this room is being slowed by the surface under it.")

In the college canteen, Kiran asks to see the video Ananya shot at the fest. Instead of getting up, Ananya does what everybody does: she lays her phone flat on the table and gives it a flick.

It glides across the laminate, slows down, and stops a hand's width short of Kiran.

"Weak," says Kiran.

"The table's sticky," says Ananya. She tries to judge it better next time and wonders: if she knew how hard the table drags on the phone, could she work out in advance how fast it would still be going when it reached Kiran? She doesn't want to worry about acceleration or time — just how hard she flicks, and how far it has to go.

Is there a way to go straight from forces and distances to speed?

## The physics

The **work–energy theorem** says: the **net work** done on a body by all the forces acting on it equals the change in its kinetic energy.

$$W_\text{net} = K_f - K_i = \tfrac{1}{2}mv^2 - \tfrac{1}{2}mu^2$$

where $u$ and $v$ are the initial and final speeds. It follows from Newton's second law, and it holds for constant *and* variable forces, since $W_\text{net}$ can always be found as an area.

- Positive net work speeds a body up; negative net work slows it down; zero net work leaves its speed unchanged.
- It links force and distance directly to speed — no time, no acceleration needed.

![A body moves from A to B while a resistive force acts backwards on it; bar charts show its kinetic energy at B is lower than at A by exactly the net work done](figures/work_energy_theorem/net-work-changes-ke.svg "The drop in the kinetic-energy bar is exactly the negative work done by the resistive force — for Ananya's phone, the table's friction.")

On the sliding phone, three forces act: its weight (down), the table's normal push (up) and friction (backwards). Weight and normal force are perpendicular to the motion, so they do no work. Only friction does, and it does **negative** work: $W = -fd$.

## Worked example

**Given:** phone mass $m = 0.20\,\text{kg}$; on her second, harder flick it leaves Ananya's hand at $u = 2.0\,\text{m/s}$; the table's friction is a steady $f = 0.30\,\text{N}$ (illustrative); Kiran is $d = 1.0\,\text{m}$ away.
**Find:** the phone's speed when it reaches Kiran.

1. *Energy at the start:* $K_i = \tfrac{1}{2} \times 0.20 \times 2.0^2 = 0.10 \times 4.0 = 0.40\,\text{J}$.
2. *Net work over the metre:* only friction works, against the motion: $W_\text{net} = -0.30 \times 1.0 = -0.30\,\text{J}$.
3. *Energy at Kiran:* $K_f = 0.40 - 0.30 = 0.10\,\text{J}$ — a quarter of what it started with.
4. *Speed at Kiran:* $v = \sqrt{2K_f/m} = \sqrt{2 \times 0.10 / 0.20} = \sqrt{1.0} = 1.0\,\text{m/s}$.

Three quarters of the energy is gone, yet the phone is still moving at *half* its starting speed — a gentle walking pace, easy for Kiran to catch.

**Sanity check:** the phone has lost energy and slowed, as negative work should do; and since $K \propto v^2$, a quarter of the energy means half the speed.

## Where the picture breaks

The phone on the table is a real case, not an analogy, but friction is rarely as neat as a single steady $0.30\,\text{N}$. A phone with a camera bump may rock and scrape, a rubbery case grips far more than bare glass, and a spot of spilt tea changes everything. The theorem still holds — the net work always equals the change in kinetic energy — but you would need the true force at every point to find it. Our calculation also treats the phone as a point that slides without spinning; a flicked phone often rotates too.

## Key takeaway

The net work done on a body equals its change in kinetic energy: $W_\text{net} = \tfrac{1}{2}mv^2 - \tfrac{1}{2}mu^2$. Add up the work done by every force, add it to the starting kinetic energy, and you have the final speed — without needing time or acceleration.
