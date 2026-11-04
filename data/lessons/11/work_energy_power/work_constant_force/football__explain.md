---
concept_id: work_constant_force
interest: football
format: explain
title: The sled drill and the strap at an angle
check:
  question: |-
    In a sled drill, a player pulls with a steady $200\,\text{N}$ along a strap held at $60^\circ$ above the horizontal, and the sled moves $10\,\text{m}$ along level grass at constant speed. How much work does the strap's force do on the sled?
  options:
    A: |-
      $1000\,\text{J}$
    B: |-
      $2000\,\text{J}$
    C: |-
      $1732\,\text{J}$
    D: |-
      $0\,\text{J}$
  answer: A
  explanation: |-
    Only the component of the force along the displacement does work: $W = Fd\cos\theta = 200 \times 10 \times \cos 60^\circ = 2000 \times 0.5 = 1000\,\text{J}$.
  misconceptions:
    B: |-
      Multiplies force by distance without the angle; work uses only the part of the force along the displacement, $F\cos\theta$.
    C: |-
      Uses $\sin 60^\circ$ instead of $\cos 60^\circ$, taking the vertical part of the pull; the vertical part is perpendicular to the motion and does no work.
    D: |-
      Thinks that because the speed is constant, no force does any work; the net work is zero, but the strap does positive work while friction does an equal amount of negative work.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A football training ground by day: a player drags a weighted sled on a strap, a striker lofts the ball in a high arc, and the goalkeeper dives to catch it](scenes/football/work_energy_power.svg "On the left, a sled drill: the strap pulls at an angle while the sled slides along the grass.")

Pre-season at the academy means the sled. Arjun, a centre-back, clips the strap to his waist belt, leans forwards and drives his legs. Behind him, a metal sled loaded with weight plates scrapes across the grass at a slow, steady pace.

The physio, Lalitha, walks alongside with a clipboard. "Fifteen metres. Keep it smooth."

Arjun gasps out a complaint between steps. "This strap slopes up to my belt. So half my pull is just lifting the sled, not moving it. That's wasted." Then, looking back: "And those plates must weigh forty kilos. Their weight is doing loads of work against me."

Lalitha smiles and writes something down. Arjun has raised two real questions. When a force acts at an angle to the motion, how much of it counts as work? And can a big force, like the sled's weight, do no work at all?

## The physics

For a **constant force** $\vec{F}$ acting on a body while it undergoes a displacement $\vec{d}$, the **work done** by that force is the scalar product

$$W = \vec{F} \cdot \vec{d} = Fd\cos\theta$$

where $\theta$ is the angle between $\vec{F}$ and $\vec{d}$. Only the component along the displacement, $F\cos\theta$, does work. Work is a scalar, measured in **joules**: $1\,\text{J} = 1\,\text{N m}$.

The sign of $\cos\theta$ fixes the sign of the work:

- $0^\circ \le \theta < 90^\circ$: **positive** work. The force helps the motion and gives the body energy. The strap does positive work on the sled.
- $\theta = 90^\circ$: **zero** work. The sled's weight (down) and the normal force from the ground (up) are perpendicular to its horizontal motion, so neither does any work, however large.
- $90^\circ < \theta \le 180^\circ$: **negative** work. Friction from the grass points backwards and takes energy away.

![Three panels: a force at angle theta to the displacement does positive work; weight and normal force perpendicular to the displacement do zero work; friction opposite to the displacement does negative work](figures/work_constant_force/work-sign-cases.svg "Compare each force with the displacement. Along it: positive work. Perpendicular: none. Against it: negative.")

Work is also zero if nothing moves. Straining against a sled that won't budge does no work on it.

## Worked example

**Given** (illustrative): the strap pulls with $F = 180\,\text{N}$ at $\theta = 20^\circ$ above the horizontal; the sled slides $d = 15\,\text{m}$ along level grass at constant speed.
**Find:** the work done by the strap, by friction, by the sled's weight and by the normal force.

Strap:

$$W_\text{strap} = Fd\cos\theta = 180 \times 15 \times \cos 20^\circ = 2700 \times 0.940 \approx 2.54 \times 10^{3}\,\text{J}$$

The speed is constant, so the net horizontal force is zero. Friction must balance the strap's horizontal component, $f = 180\cos 20^\circ \approx 169\,\text{N}$, pointing backwards ($\theta = 180^\circ$):

$$W_f = fd\cos 180^\circ \approx -169 \times 15 \approx -2.54 \times 10^{3}\,\text{J}$$

Weight and normal force are vertical, at $90^\circ$ to the motion: $W = 0$ for both.

The net work is zero, and the sled's speed doesn't change. That is not a coincidence; it is the work-energy theorem, coming soon.

**Sanity check:** the component along the motion is $180 \times 0.940 \approx 169\,\text{N}$, and $169 \times 15 \approx 2540\,\text{J}$, the same answer. The upward part, $180\sin 20^\circ \approx 62\,\text{N}$, does no work on the sled, but it isn't wasted either. It presses the sled into the grass less, which reduces the friction Arjun has to beat.

## Where the picture breaks

Arjun's "wasted effort" is about how tired he feels, not about mechanical work. Muscles burn chemical energy even when holding still, so tiredness doesn't measure work done on the sled. The numbers also assume a steady pull along a straight line. A real drill is a series of surges, one per stride, so $180\,\text{N}$ is an average. For a force that really changes as the body moves, you need the area under a force-displacement graph.

## Key takeaway

Work done by a constant force is $W = \vec{F} \cdot \vec{d} = Fd\cos\theta$, in joules. It is positive when the force has a component along the motion, zero when the force is perpendicular to the motion (or nothing moves), and negative when the force opposes the motion.
