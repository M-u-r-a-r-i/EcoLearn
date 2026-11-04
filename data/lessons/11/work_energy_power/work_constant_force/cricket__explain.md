---
concept_id: work_constant_force
interest: cricket
format: explain
title: Dragging the covers on before the rain
check:
  question: |-
    During a drinks break, the twelfth player carries a tray of bottles across the ground. His hands push up on the tray with a steady $20\,\text{N}$ while he walks $30\,\text{m}$ in a straight line at constant speed, keeping the tray at the same height. How much work does the upward force of his hands do on the tray?
  options:
    A: |-
      $600\,\text{J}$
    B: |-
      $-600\,\text{J}$
    C: |-
      It depends on how fast he walks.
    D: |-
      $0\,\text{J}$
  answer: D
  explanation: |-
    The hands' force is vertical and the tray's displacement is horizontal, so $\theta = 90^\circ$ and $W = Fd\cos 90^\circ = 0$. Carrying something level does no work on it, however tiring it feels.
  misconceptions:
    A: |-
      Multiplies force by distance without checking the angle between them; work uses only the component of the force along the displacement.
    B: |-
      Thinks the hands' force does negative work because it acts against gravity; the sign of work depends on the force's direction compared with the displacement, not with other forces.
    C: |-
      Thinks work depends on speed or time taken; for a constant force, work depends only on the force, the displacement and the angle between them.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground by day: a batter watches a ball climb high, a fielder waits under it, a player runs up the stadium steps and a groundsman pushes a roller](scenes/cricket/work_energy_power.svg "The groundstaff do some of the hardest physical work at any match.")

The sky over the ground turns grey in minutes. The umpires take the players off, and Harpreet, the head groundsman, is already running. He grabs the rope of the wheeled pitch cover and leans back, hauling it towards the square. The rope rises from the cover to his hands at an angle, and he keeps the cover rolling at a steady walking pace.

His nephew Kiran, helping for the first time, jogs beside him. "Why are you pulling *upwards*? Aren't you wasting half your effort lifting it?" Then he looks at the heavy cover. "And that thing weighs a tonne — its weight must be doing a huge amount of work too."

Harpreet grins and keeps pulling. Kiran has asked two good questions. When a force acts at an angle to the motion, how much of it actually counts? And can a big force, like the cover's weight, do no work at all?

## The physics

For a **constant force** $\vec{F}$ acting on a body while its point of application undergoes a displacement $\vec{d}$, the **work done** by that force is the scalar product

$$W = \vec{F} \cdot \vec{d} = Fd\cos\theta$$

where $\theta$ is the angle between $\vec{F}$ and $\vec{d}$. Only the component of the force along the displacement, $F\cos\theta$, does work. Work is a scalar; its SI unit is the **joule**: $1\,\text{J} = 1\,\text{N m}$.

The sign of $\cos\theta$ sets the sign of the work:

- $0^\circ \le \theta < 90^\circ$: **positive** work. The force helps the motion and gives the body energy. Harpreet's rope does positive work on the cover.
- $\theta = 90^\circ$: **zero** work. The cover's weight (down) and the normal force from the ground (up) are perpendicular to its horizontal motion, so neither does any work, however large.
- $90^\circ < \theta \le 180^\circ$: **negative** work. The force opposes the motion and takes energy away. The resistance at the wheels does negative work.

![Three panels: a block pulled by a force at angle theta does positive work; weight and normal force perpendicular to the displacement do zero work; friction opposite to the displacement does negative work](figures/work_constant_force/work-sign-cases.svg "Compare each force's direction with the displacement. Along it: positive work. Perpendicular: none. Against it: negative.")

Work is also zero if there is no displacement: pushing hard on a heavy roller that doesn't move does no work on it.

## Worked example

**Given** (illustrative): Harpreet pulls with $F = 200\,\text{N}$ along a rope at $\theta = 30^\circ$ above the horizontal, and the cover moves $d = 20\,\text{m}$ horizontally at constant speed.
**Find:** the work done by the rope, by the resistive force at the wheels, by gravity and by the normal force.

Rope:

$$W_\text{rope} = Fd\cos\theta = 200 \times 20 \times \cos 30^\circ = 4000 \times 0.866 \approx 3.46 \times 10^{3}\,\text{J}$$

The speed is constant, so the net horizontal force is zero: the resistive force equals the rope's horizontal component, $f = 200\cos 30^\circ \approx 173\,\text{N}$, pointing backwards ($\theta = 180^\circ$):

$$W_f = fd\cos 180^\circ = -173 \times 20 \approx -3.46 \times 10^{3}\,\text{J}$$

Gravity and the normal force are vertical, at $90^\circ$ to the motion: $W = 0$ for both.

So the net work on the cover is zero — and its speed doesn't change. That link is no coincidence; you'll meet it as the work-energy theorem.

**Sanity check:** only $F\cos\theta \approx 173\,\text{N}$ acts along the motion, and $173 \times 20 \approx 3460\,\text{J}$ — the same answer. The upward part, $F\sin 30^\circ = 100\,\text{N}$, does no work; it only eases the load on the wheels.

## Where the picture breaks

Kiran's worry about "wasted effort" is about how Harpreet feels, not about physics. Muscles use chemical energy even when holding a load still, so tiredness is not a measure of mechanical work. Our numbers also assume a perfectly constant force and a straight path. A real pull is jerky and the angle changes as the rope shortens, so $Fd\cos\theta$ is only an average picture. For a force that changes, you'll need the area under a force-displacement graph.

## Key takeaway

Work done by a constant force is $W = \vec{F} \cdot \vec{d} = Fd\cos\theta$, measured in joules. It is positive when the force has a component along the motion, zero when the force is perpendicular to it (or there is no displacement), and negative when the force opposes the motion.
