---
concept_id: impulse
interest: gaming
format: explain
title: Why one controller cracked and the other survived
check:
  question: |-
    A $0.20\,\text{kg}$ controller falls and hits a foam floor mat at $5.0\,\text{m/s}$. The mat brings it to rest, without a bounce, in $0.025\,\text{s}$. What is the average net force on the controller while it stops?
  options:
    A: |-
      $40\,\text{N}$
    B: |-
      $0.025\,\text{N}$
    C: |-
      $200\,\text{N}$
    D: |-
      $1.0\,\text{N}$
  answer: A
  explanation: |-
    The change in momentum is $\Delta p = 0.20 \times 5.0 = 1.0\,\text{kg m/s}$, so $F_\text{avg} = \dfrac{\Delta p}{\Delta t} = \dfrac{1.0}{0.025} = 40\,\text{N}$, directed upwards.
  misconceptions:
    B: |-
      Multiplies the change in momentum by the time instead of dividing. Impulse is force times time, so force is impulse divided by time.
    C: |-
      Divides the speed by the time and forgets the mass. That gives an acceleration ($200\,\text{m/s}^2$), not a force; multiply by $0.20\,\text{kg}$.
    D: |-
      Reports the impulse ($1.0\,\text{N s}$) as if it were the force. Impulse and force are different quantities with different units.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a racing game on the monitor and a zero-gravity game on a tablet](scenes/gaming/laws_of_motion.svg "The desk is where the games happen. The floor below it is where controllers go to die.")

It happens in the final round. Rehan jumps up to celebrate a win, his elbow catches his controller, and it slides off the desk. It hits the tiled floor with a sharp *crack*. When he picks it up, a thin split runs along the plastic shell.

Two weeks later, the same thing happens to his sister Aisha at her desk in the next room. Same desk height, same kind of controller. But her floor is covered with the squashy foam mat she put down for her gaming chair. The controller lands with a soft *thud* and works perfectly.

"Lucky," says Rehan.

"Not luck," says Aisha. "Physics."

Rehan isn't having it. Both controllers fell from the same height, so they hit the floor at the same speed. Both ended up lying still on the floor. The same stop from the same speed. So how could one floor hit so much harder than the other?

## The physics

From Newton's second law, the average net force over a time $\Delta t$ is $\vec{F}_\text{avg} = \dfrac{\Delta\vec{p}}{\Delta t}$. Multiply both sides by $\Delta t$:

$$\vec{J} = \vec{F}_\text{avg}\,\Delta t = \Delta\vec{p}$$

Force multiplied by the time it acts is the **impulse**, $\vec{J}$. It is a vector along the force, and its SI unit is the newton second, $\text{N s}$, which is the same as $\text{kg m/s}$. In words:

**impulse = change in momentum.**

Now look at the two controllers. Each arrives at the same speed and ends at rest, so each has the **same change in momentum**, and so needs the **same impulse** from the floor. Rehan was right about that. But impulse is a product. The tiles barely give, so they stop the controller in a tiny time and the force is large. The foam squashes, so the stop lasts much longer and the average force is much smaller:

$$F_\text{avg} = \frac{\Delta p}{\Delta t}$$

When the force changes during the impact, as it always does, the impulse is the **area under the force–time graph**. Equal areas can be a tall, narrow spike or a low, wide hump. The shell cracks when the force is too big, not when the impulse is.

![Force–time graph: a tall narrow triangle lasting 20 ms with a peak of 480 N, and a low wide triangle lasting 100 ms with a peak of 96 N; both have an area of 4.8 N s](figures/impulse/force-time-stiff-vs-soft.svg "Drawn for a different impact, but the idea is the tiles against the foam: equal areas mean equal impulses, and stretching the time cuts the force in the same proportion.")

Phone cases, the foam inside a VR headset's box, and the padding in gaming chairs all use the same idea: lengthen the time of an impact so the same change in momentum needs less force.

## Worked example

**Given (illustrative values):** a $0.25\,\text{kg}$ controller hits the floor at $4.0\,\text{m/s}$ (about what a fall of $0.8\,\text{m}$ gives) and stops without bouncing. Tiles stop it in $0.0020\,\text{s}$; the foam mat in $0.020\,\text{s}$.
**Find:** the impulse on the controller and the average net force in each case.

Take downwards as positive: $u = +4.0\,\text{m/s}$, $v = 0$.

$$J = \Delta p = m(v - u) = 0.25 \times (0 - 4.0) = -1.0\,\text{N s}$$

The minus sign says the impulse points upwards, against the motion. Its size is $1.0\,\text{N s}$ on both floors.

$$F_\text{tiles} = \frac{1.0}{0.0020} = 500\,\text{N} \qquad F_\text{foam} = \frac{1.0}{0.020} = 50\,\text{N}$$

The foam's force is ten times smaller. (These are *net* forces; the floor also has to hold up the controller's weight, $0.25 \times 9.8 \approx 2.5\,\text{N}$, which is small by comparison.)

**Sanity check:** the stopping time went up by a factor of $10$, so the force should fall by $10$: $500/10 = 50$ ✓. Reverse it: $50\,\text{N} \times 0.020\,\text{s} = 1.0\,\text{N s}$, the same impulse ✓.

## Where the picture breaks

The force in a real impact is not steady, and its peak is higher than the average that $\Delta p/\Delta t$ gives. Most dropped controllers bounce, and a bounce reverses the momentum, which makes the change in momentum, and the impulse, bigger than a plain stop. Whether plastic cracks also depends on where it lands (a corner concentrates the force on a small area) and on the material, not on force alone. The physics tells you why the foam helps; it can't promise any particular drop is safe.

## Key takeaway

Impulse is force times the time it acts, $\vec{J} = \vec{F}_\text{avg}\,\Delta t$, and it equals the change in momentum, $\Delta\vec{p}$. When the change in momentum is fixed, as in stopping a falling object, stretching the collision time reduces the average force in the same proportion. That is why soft floors, padding and cases protect things.
