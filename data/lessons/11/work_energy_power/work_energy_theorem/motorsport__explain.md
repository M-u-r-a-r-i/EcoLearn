---
concept_id: work_energy_theorem
interest: motorsport
format: explain
title: How long does the gravel trap have to be
check:
  question: |-
    A car of mass $1000\,\text{kg}$ is travelling at $10\,\text{m/s}$ along a straight when the net force on it does $150\,\text{kJ}$ of work on it. What is its final speed?
  options:
    A: |-
      $17.3\,\text{m/s}$
    B: |-
      $40\,\text{m/s}$
    C: |-
      $20\,\text{m/s}$
    D: |-
      $14.1\,\text{m/s}$
  answer: C
  explanation: |-
    $K_i = \tfrac{1}{2}(1000)(10)^2 = 50\,\text{kJ}$, so $K_f = 50 + 150 = 200\,\text{kJ}$. Then $v_f = \sqrt{2K_f/m} = \sqrt{400} = 20\,\text{m/s}$.
  misconceptions:
    A: |-
      Uses $v = \sqrt{2W/m}$ and forgets the car was already moving. The theorem gives the *change* in kinetic energy, so the starting $50\,\text{kJ}$ must be added in.
    B: |-
      Notices the energy went up four times and multiplies the speed by four. Speed goes as the square root of energy, so four times the energy is only twice the speed.
    D: |-
      Gets $K_f = 200\,\text{kJ}$ right but solves $mv^2 = 2 \times 10^5$, dropping the factor $\tfrac{1}{2}$ on the way back to speed.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race track scene: a car coasts down a hill road onto the circuit, a second car speeds along the straight with a velocity arrow, a third brakes with glowing red discs, and two people push a kart in the foreground](scenes/motorsport/work_energy_power.svg "Behind every corner on a circuit there has to be enough room to stop a car that has stopped steering.")

The club is resurfacing the circuit, and Sharvari has been handed the least glamorous job on the committee: deciding how deep the gravel trap behind the fast right-hander has to be.

There is one measurement to go on. Last season a car spun off there at about $20\,\text{m/s}$ and buried itself $20\,\text{m}$ into the gravel — no damage, driver fine, everyone relieved.

Keshav does the sum in his head. "Cars are coming through that corner at forty now instead of twenty. Double the speed, so double the gravel. Make it forty metres and we're covered."

Sharvari isn't sure. She remembers something about braking distances and squares, and she does not want to be the person who signed off a run-off that was half the length it needed to be.

Who is right — and is there a way to settle it without borrowing a car and crashing it?

## The physics

The **work–energy theorem** connects the two ideas you have just met. For a body of constant mass, the **net work** done on it by *all* the forces acting equals its change in kinetic energy:

$$W_\text{net} = \Delta K = K_f - K_i = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2$$

It follows straight from the second law. For a constant net force along the motion, $W_\text{net} = Fd = mad$, and $v_f^2 - v_i^2 = 2ad$ gives $ad = \tfrac{1}{2}(v_f^2 - v_i^2)$, so $W_\text{net} = \tfrac{1}{2}mv_f^2 - \tfrac{1}{2}mv_i^2$. It holds for varying forces too, provided you take the net work as the area under the force–displacement graph.

![A body moves from A to B along the ground while a resistive force acts backwards on it; bar charts show its kinetic energy at B is lower than at A by the net work done](figures/work_energy_theorem/net-work-changes-ke.svg "The drop in the kinetic-energy bar is exactly the negative work done by the resistive force.")

Two habits make it reliable:

- **Net means all of them.** Add up the work done by every force — engine, friction, drag, gravity — with its own sign. A force perpendicular to the motion contributes nothing.
- **Negative work slows things down.** Gravel, brakes and drag all push backwards, so their work is negative and $\Delta K$ comes out negative.

The theorem's power is that **time never appears**. It links force and *distance* directly to speed, so questions like "how far to stop?" fall out in one line, with no need to know how long the slide lasted or how the force varied moment to moment.

And it contains Sharvari's answer. To stop a car, the trap must remove all of $\tfrac{1}{2}mv^2$. With a roughly steady retarding force $F$, the distance needed is

$$d = \frac{mv^2}{2F}$$

The distance goes as $v^2$, not $v$.

## Worked example

**Given** (illustrative): car plus driver $m = 800\,\text{kg}$ enters the gravel at $v = 20\,\text{m/s}$; the gravel drags it back with a roughly steady $8000\,\text{N}$.
**Find:** the stopping distance, and the distance if the same car arrives at $40\,\text{m/s}$.

*Kinetic energy to be removed at $20\,\text{m/s}$:*

$$K = \tfrac{1}{2}(800)(20)^2 = 400 \times 400 = 160\,000\,\text{J}$$

*Distance.* The gravel's work is $-Fd$, and the car ends at rest, so $-Fd = 0 - K$:

$$d = \frac{160\,000}{8000} = 20\,\text{m}$$

That matches last season's spin exactly, which is a good sign that $8000\,\text{N}$ is the right sort of number for this gravel.

*Now at $40\,\text{m/s}$.* The speed doubles, so the kinetic energy quadruples to $640\,000\,\text{J}$, and with the same retarding force:

$$d = \frac{640\,000}{8000} = 80\,\text{m}$$

Not $40\,\text{m}$. **Four times the gravel, not twice.** In Keshav's $40\,\text{m}$ trap the gravel would have removed $8000 \times 40 = 320\,000\,\text{J}$ — exactly half — leaving the car to reach the barrier still doing about $28\,\text{m/s}$.

**Sanity check:** $20\,\text{m}$ is around five car lengths and $80\,\text{m}$ is around twenty — and anyone who has watched a car plough into gravel knows the fast ones go in a very long way indeed.

## Where the picture breaks

Real gravel does not pull with a constant force. It resists more as the car digs deeper and the wheels submerge, so the force grows through the slide and the true distance is shorter than the constant-force estimate — which is why traps are designed with a safety margin rather than by this one formula. A spinning car also arrives sideways, presenting a much larger area to the gravel, and it may have been braking on tarmac first. And the theorem gives the distance but says nothing about the *deceleration* the driver feels, which is what decides whether they walk away. Energy tells you how far; force tells you how much it hurts.

## Key takeaway

The work–energy theorem says $W_\text{net} = \Delta K = \tfrac{1}{2}mv_f^2 - \tfrac{1}{2}mv_i^2$: the net work done by all forces is exactly the change in kinetic energy. Because kinetic energy goes as $v^2$, the stopping distance under a steady retarding force, $d = mv^2/2F$, quadruples when the speed doubles.
