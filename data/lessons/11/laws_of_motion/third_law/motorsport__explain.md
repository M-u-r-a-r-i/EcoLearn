---
concept_id: third_law
interest: motorsport
format: explain
title: What actually pushes a car forwards
check:
  question: |-
    A car accelerates away from a standing start. Its driven tyres push backwards on the road with a force of $5000\,\text{N}$. The road therefore:
  options:
    A: |-
      pushes forwards on the car with less than $5000\,\text{N}$, because the road cannot move
    B: |-
      pushes forwards on the car with exactly $5000\,\text{N}$
    C: |-
      pushes forwards on the car with exactly $5000\,\text{N}$, which cancels the tyres' push, so the car cannot accelerate
    D: |-
      pushes backwards on the car with $5000\,\text{N}$, opposing its motion
  answer: B
  explanation: |-
    By Newton's third law the two forces are equal in size and opposite in direction. The tyres' push acts on the road; the road's push acts on the car, and it is that forward push which accelerates the car.
  misconceptions:
    A: |-
      Thinks the heavier or immovable body gives the smaller force. The pair is always equal in size, however massive or fixed either body is.
    C: |-
      Puts both forces of the pair on the same body. Forces cancel only when they act on the *same* body; these two act on different bodies and never cancel.
    D: |-
      Reads "reaction" as "resistance". The reaction is opposite to the *action*, not opposite to the car's motion — a backward push on the road pairs with a forward push on the car.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race car in a braking zone with glowing brake discs, a skid mark and tyre smoke, a tyre barrier along the wall and a marshal with a yellow flag](scenes/motorsport/laws_of_motion.svg "The only thing touching this car is the road. Everything the car does, the road does to it.")

The club's paddock is a field, and it has rained all night. By lunchtime the car that towed the trailer in will not move. Nikhil, who did Newton's third law in school last week, volunteers to drive while Tara pushes from behind.

He gives it throttle. The rear wheels spin, mud sprays backwards in a long brown fan, and the car creeps forward about ten centimetres.

"There," says Tara, scraping her jeans. "It goes forward because it throws mud backwards."

Nikhil isn't having it. "That can't be right. Third law: the tyre pushes the ground backwards, the ground pushes the tyre forwards, equal and opposite. Equal and opposite means they cancel. So the car shouldn't move at all — and on dry tarmac it should be just as stuck, which it obviously isn't."

Two forces, equal and opposite, and yet cars accelerate every day. Where is the mistake?

## The physics

**Newton's third law:** whenever body A exerts a force on body B, body B exerts a force on body A that is equal in size and opposite in direction.

$$\vec{F}_\text{AB} = -\vec{F}_\text{BA}$$

Here $\vec{F}_\text{AB}$ means the force *on A by B*. The two forces are an **action–reaction pair**, and they have four properties:

- **Equal in size, opposite in direction** — always, whatever the two masses are and whether the bodies are still, moving or accelerating.
- **Simultaneous.** "Action" and "reaction" are only labels; neither happens first.
- **The same kind of force** (here both are contact forces from friction at the tyre).
- **They act on different bodies.** This is where Nikhil goes wrong.

Forces cancel only when you add up the forces acting on **one** body. The tyre's push acts on the *road*. The road's push acts on the *car*. To work out how the car moves, you add only the forces on the car, and the road's forward push is the big one. It is the road, not the engine, that pushes a car along — the engine's job is to make the tyres push the road backwards hard enough.

![Two bodies drawn slightly apart, with a red arrow on one labelled force on B by A and an equal, opposite red arrow on the other labelled force on A by B](figures/third_law/action-reaction-pair.svg "Read A as the tyre and B as the road. Each arrow sits on a different body, which is exactly why the pair cannot cancel.")

That also explains the mud. Loose wet mud cannot push back hard: it simply flies off backwards instead of resisting. A small reaction on the car means a small forward force, so the car barely moves. Dry tarmac can push back thousands of newtons, and the same engine launches the car hard.

Two more pairs from the same weekend:

- **Downforce.** A rear wing deflects the air flowing over it **upwards**; by the third law the air pushes the wing **downwards**. That downward push is what presses the tyres into the road.
- **A car parked in the paddock.** Earth pulls the car down (its weight) and the car pulls Earth up — that is one pair. The car presses down on the ground and the ground pushes up on the car (the normal force) — that is a *different* pair. Weight and normal force are equal here, but they are **not** an action–reaction pair: they act on the same body and are different kinds of force.

## Worked example

**Given:** on a dry launch the road pushes forward on the driven tyres with $6000\,\text{N}$ (illustrative). The car's mass is $1200\,\text{kg}$; Earth's mass is about $6.0 \times 10^{24}\,\text{kg}$.
**Find:** the force the tyres exert on the road, and the acceleration that each of these two forces alone would give its own body.

*Third law.* The tyres push backwards on the road — and so on Earth — with $6000\,\text{N}$.

*The car,* using $a = F/m$:

$$a_\text{car} = \frac{6000}{1200} = 5.0\,\text{m/s}^2$$

*Earth,* using the same $6000\,\text{N}$:

$$a_\text{Earth} = \frac{6000}{6.0 \times 10^{24}} = 1.0 \times 10^{-21}\,\text{m/s}^2$$

**Sanity check:** the forces are identical and the accelerations differ by a factor of about $10^{21}$, purely because the masses do — which is why nobody has ever noticed the planet being nudged by a car pulling away.

## Where the picture breaks

The car is not a free body: air drag, rolling resistance and the undriven tyres all act on it too, so $5.0\,\text{m/s}^2$ is what the drive force *alone* would give, not the real acceleration. The road is bolted to a planet, so the reaction is shared out through the whole Earth rather than moving a patch of tarmac. We drew the two bodies apart so both arrows could be seen; in reality they touch, which is precisely when the forces exist. And when a wheel spins on mud the rubber really is sliding, so the friction there is kinetic and smaller — the pair is still exactly equal, it is just smaller on both sides.

## Key takeaway

Forces always come in pairs: if A pushes B, then B pushes A equally hard the other way, $\vec{F}_\text{AB} = -\vec{F}_\text{BA}$. The two forces act on **different bodies**, so they never cancel. To find how one body moves, add up only the forces acting on that body — which is why a car goes forwards when its tyres push the road backwards.
