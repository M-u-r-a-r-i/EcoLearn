---
concept_id: inertia_first_law
interest: motorsport
format: explain
title: The helmet that kept going after the van stopped
check:
  question: |-
    A car travels along a straight, level motorway at a constant $100\,\text{km/h}$. Which statement about the forces on it is correct?
  options:
    A: |-
      The net force on it is forwards, because the car is moving forwards.
    B: |-
      The net force on it is zero: the driving force from the road balances drag and friction.
    C: |-
      The net force is zero only when the engine is switched off and the car is coasting.
    D: |-
      The driving force must be bigger than the drag, or the car would not keep moving.
  answer: B
  explanation: |-
    Constant velocity means zero acceleration, so by Newton's first law the net force is zero. The road's forward push on the driven tyres exactly balances air drag and rolling resistance.
  misconceptions:
    A: |-
      The "impetus" idea: thinks motion itself needs a net force in the direction of travel. A net force would change the velocity; at a steady speed nothing is changing.
    C: |-
      Thinks a running engine always means a leftover net force. A driving force can be exactly cancelled by drag, and then the net force is zero even at $100\,\text{km/h}$.
    D: |-
      Confuses keeping a speed with gaining speed. If the driving force exceeded the drag, the car would accelerate; holding a steady speed needs them equal.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race car in a braking zone with glowing brake discs, a skid mark and tyre smoke, a tyre barrier along the wall and a marshal with a yellow flag](scenes/motorsport/laws_of_motion.svg "Everything in this picture is about one idea: motion does not stop by itself, and it does not start by itself either.")

Devika's first proper karting session starts at ten, and her father is driving the club van to the track with four karts on the trailer. On the back seat beside her, her new helmet sits loose on top of her bag.

Two kilometres from the gate, a stray dog wanders onto the road. Her father brakes hard. The van stops in a couple of seconds — and the helmet does not. It slides forward off the bag, thumps into the back of the front seat and drops into the footwell.

Devika picks it up and turns it over. Nobody pushed it. Nothing was pulling it forwards.

An hour later the instructor hauls her kart harness so tight she can barely lean forward, and she starts to see why. But the puzzle stays. Why did stopping the van not stop the helmet — and what was stopping the van?

## The physics

Turn the question round. The helmet did not need a force to **keep** going. It needed a force to **stop**.

**Newton's first law:** a body stays at rest, or keeps moving with constant velocity — the same speed in the same straight line — unless a net external force acts on it.

The property behind this is **inertia**: every body resists a change in its state of motion. Mass measures it. A heavy touring car is harder to get moving, harder to stop and harder to turn than a kart, with the same forces available.

Two things to read carefully:

- It is the **net** force that counts. On top of the bag, two forces act on the helmet: its weight $W = mg$ downwards and the **normal force** $N$ from the bag upwards. They cancel. With the bag's surface slippery and air drag negligible, nothing horizontal is left over, so $\vec{F}_\text{net} = 0$ and the velocity cannot change.
- "Zero net force" does **not** mean "at rest". It means **no change** in velocity. A kart parked in the paddock stays parked; a helmet travelling at $12\,\text{m/s}$ keeps travelling at $12\,\text{m/s}$.

![Top row: a body on a very smooth surface photographed every second, covering equal distances, with its weight and normal force cancelling. Bottom row: on a rough surface an unbalanced friction force makes the gaps shrink](figures/inertia_first_law/zero-net-force-constant-velocity.svg "Equal gaps in equal times is what zero net force looks like. Shrinking gaps mean a net force — here friction — acting against the motion.")

The van, meanwhile, had plenty of unbalanced force: friction from the road on four braking tyres, pointing backwards. That is what slowed the van. Nothing like it acted on the helmet, so the helmet carried on.

![The Latin title page of Newton's Principia Mathematica, printed in London in 1687](famous/newton-principia-title-page.jpg "Newton opened the Principia (1687) with the first law. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** the helmet, $m = 1.0\,\text{kg}$ (illustrative), resting on a slippery bag; the van is doing $12\,\text{m/s}$ and brakes uniformly to rest in $2.0\,\text{s}$. Treat the bag's surface as level and frictionless, and take $g = 9.8\,\text{m/s}^2$.
**Find:** the net force on the helmet, its velocity when the van stops, and how far it slides forward relative to the van.

*Forces.* Weight $W = mg = 1.0 \times 9.8 = 9.8\,\text{N}$, down. The helmet neither sinks nor lifts, so $N = 9.8\,\text{N}$, up. Nothing horizontal. So $\vec{F}_\text{net} = 0$.

*Velocity.* Zero net force means no change in velocity: the helmet is still doing $12\,\text{m/s}$ forwards when the van is standing still.

*Distance.* In those $2.0\,\text{s}$ the helmet covers $12 \times 2.0 = 24\,\text{m}$, while the van, slowing steadily from $12\,\text{m/s}$ to zero, averages $6.0\,\text{m/s}$ and covers $12\,\text{m}$. The helmet ends up $12\,\text{m}$ further on — about three car lengths.

**Sanity check:** a real back seat is nowhere near $12\,\text{m}$ long, so the helmet hits the front seat almost at once, still doing close to $12\,\text{m/s}$ — which is exactly why loose objects in a braking vehicle are dangerous.

## Where the picture breaks

A bag is slippery, not frictionless, so a real helmet does lose a little speed as it slides; perfectly constant velocity is the ideal the situation approaches. The helmet also tumbles as it goes, and we treated it as a single point — spin belongs to rotational motion, later. Most importantly, the first law holds only in an **inertial frame**, one that is not itself accelerating. From inside the braking van the helmet seems to be flung forwards by nothing at all; from the road it is simply carrying on as before, and the van is the thing that changed.

## Key takeaway

Inertia is a body's resistance to any change in its motion, and mass is the measure of it. Newton's first law says that when the net force on a body is zero, its velocity stays constant: at rest stays at rest, and moving keeps moving in a straight line at the same speed. Force is what changes motion, not what maintains it.
