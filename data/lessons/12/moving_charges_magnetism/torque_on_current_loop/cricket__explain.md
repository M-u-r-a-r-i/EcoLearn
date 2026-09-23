---
concept_id: torque_on_current_loop
interest: cricket
format: explain
title: The motor that winds the covers
check:
  question: |-
    A rectangular current-carrying loop is placed in a **uniform** magnetic field with its magnetic moment $\vec{m}$ pointing along $\vec{B}$. What does the loop experience?
  options:
    A: |-
      The maximum possible torque, and no net force.
    B: |-
      A net force dragging it along the field lines.
    C: |-
      Neither a net force nor a torque.
    D: |-
      Half of the maximum torque, and no net force.
  answer: C
  explanation: |-
    $\tau = mB\sin\theta$ with $\theta = 0$ gives zero torque, and in a uniform field the forces on opposite sides cancel exactly, so there is no net force either. This is the loop's stable, aligned position.
  misconceptions:
    A: |-
      Mixes up the angle. The torque is largest when $\vec{m}$ is **perpendicular** to $\vec{B}$ (the field lying in the loop's plane), and zero when they are lined up.
    B: |-
      Expects the loop to be pulled the way a compass needle is pulled towards a magnet. That pull needs a *non-uniform* field; in a uniform field the two forces are equal and opposite and cancel.
    D: |-
      Treats "aligned" as some in-between case. $\sin 0° = 0$ exactly — there is no leftover torque at all.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground with an electric roller, a compass lying on a thick power cable, a bowling machine and a loudspeaker on a pole](scenes/cricket/moving_charges_magnetism.svg "The roller, the bowling machine and the covers winch all contain the same thing: a coil turning in a magnetic field.")

Rain, and the covers have to go on fast. The club's winch does it in ninety seconds — a green button, a rising whine, and the heavy roll walks itself across the square.

Nikhil has always assumed there is something like a petrol engine in that grey box. When the winch jams on a stone and the motor has to be opened up, he finds out otherwise. Inside is a curved magnet on each side and, between them, a drum wound with coils of copper. That is it. No pistons, no fuel, no spring.

He has just learnt that a magnetic field pushes a current-carrying wire sideways — that is how the loudspeaker on the pole shoves its cone. But this coil doesn't shoot sideways out of the magnet. It *spins*, and it keeps spinning, and it can drag a soaked cover across a square.

Why does the same force push one coil and turn another?

## The physics

Because in the motor the two sides of the loop are pushed in **opposite** directions.

Take a rectangular loop of $N$ turns and area $A$, carrying current $I$, in a uniform field $\vec{B}$. Current runs one way along one side and the opposite way along the other. By $\vec{F} = I\vec{L}\times\vec{B}$, those two sides feel forces of the same size in opposite directions — but they act along **different lines**, one on each side of the axis. Equal, opposite, and not in line: that is a **couple**, and a couple does not move an object, it twists it.

![A current loop seen edge on in a uniform field, with one side pushed up and the other pushed down; and the magnetic moment m at an angle theta to B](figures/torque_on_current_loop/torque-on-loop.svg "Equal and opposite forces that are not in line make a couple. The net force is zero — only a twist survives.")

Working out the moment of the couple gives

$$\tau = NIAB\sin\theta$$

where $\theta$ is the angle between $\vec{B}$ and the **normal** to the loop's plane. It is tidier to bundle the loop's own properties into one vector, the **magnetic dipole moment**:

$$\vec{m} = NI\vec{A}\,, \qquad \text{so} \qquad \vec{\tau} = \vec{m} \times \vec{B}, \quad \tau = mB\sin\theta$$

The direction of $\vec{m}$ is the direction your right thumb points when your fingers curl along the current around the loop, and its unit is $\text{A}\,\text{m}^{2}$. With that one quantity, a current loop behaves exactly like a small bar magnet.

Two limits are worth checking:

- $\theta = 90°$ (field lying in the plane of the loop): $\sin\theta = 1$, maximum twist.
- $\theta = 0°$ ($\vec{m}$ along $\vec{B}$): no twist at all. The loop has turned as far as it wants to and settles there.

And in a **uniform** field the net force on the loop is exactly zero, whatever the angle. A current loop in a uniform field twists; it does not get dragged anywhere.

## Worked example

**Given:** a motor coil of $50$ turns, each enclosing an area of $0.020\,\text{m}^{2}$, carrying $2.0\,\text{A}$ in a field of $0.10\,\text{T}$, with the field lying in the plane of the coil.
**Find:** the magnetic moment of the coil, and the torque on it.

**Step 1 — the magnetic moment.**

$$m = NIA = (50)(2.0)(0.020) = 2.0\,\text{A}\,\text{m}^{2}$$

This one number now stands in for the whole coil: fifty turns, two amperes and all.

**Step 2 — the torque.** The field is in the plane of the coil, so $\vec{m}$ is perpendicular to $\vec{B}$ and $\sin\theta = 1$:

$$\tau = mB = (2.0)(0.10) = 0.20\,\text{N}\,\text{m}$$

That is about the twist you put into a stiff tap — or the turning effect of hanging a $200\,\text{g}$ weight on the end of a $10\,\text{cm}$ spanner.

**Sanity check:** a fraction of a newton-metre from one small coil is modest, which is why a winch runs the coil through gearing rather than pulling the cover directly.

## Where the picture breaks

A single loop in a fixed field would be useless as a motor. It would swing round to $\theta = 0$, overshoot, swing back and stop — one twitch, not rotation. A real motor reverses the current in the coil every half turn, using a split-ring commutator, so the twist is always in the same sense. That mechanism is a topic of its own; here, only the torque is.

The uniform field in the diagram is also not what is in the winch. Those curved pole pieces make the field **radial**, so the field always lies in the coil's plane and $\sin\theta$ stays at $1$ all the way round. Without that, the torque would sag to zero twice per revolution. The next lesson uses the same trick for a quite different purpose.

Finally, "no net force" holds only in a uniform field. In a non-uniform one the two sides sit in different field strengths, the forces no longer cancel, and the loop is dragged as well as twisted — which is how a magnet attracts a piece of iron at all.

## Key takeaway

A current loop in a uniform magnetic field feels no net force but a **couple**: $\tau = NIAB\sin\theta = mB\sin\theta$, where $\vec{m} = NI\vec{A}$ is the loop's magnetic dipole moment, measured in $\text{A}\,\text{m}^{2}$. The twist is greatest when $\vec{m}$ is perpendicular to $\vec{B}$ and zero when they are aligned.
