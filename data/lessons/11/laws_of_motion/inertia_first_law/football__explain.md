---
concept_id: inertia_first_law
interest: football
format: explain
title: The pass that would not stop on the sports-hall floor
check:
  question: |-
    During a rain break, a football is passed across a polished indoor floor at $3.0\,\text{m/s}$. Take friction and air drag as negligible. While it is on the floor, the ball:
  options:
    A: |-
      slows down gradually, because the force of the pass is slowly used up
    B: |-
      keeps rolling at $3.0\,\text{m/s}$ in the same straight line, because the net force on it is zero
    C: |-
      speeds up a little, because there is nothing left to hold it back
    D: |-
      stops as soon as the passer's foot leaves it, because no force is pushing it any more
  answer: B
  explanation: |-
    The ball's weight is balanced by the normal force from the floor, and with friction and drag negligible the net force is zero. By Newton's first law its velocity stays constant: same speed, same direction.
  misconceptions:
    A: |-
      The "impetus" idea: thinks the kick puts a force into the ball that wears off. No force travels with the ball after contact; it slows only if something, like friction, acts on it.
    C: |-
      Thinks removing resistance makes a body speed up. Zero net force means zero acceleration, so the speed cannot increase.
    D: |-
      Thinks motion needs a continuous push to exist at all. A moving body keeps moving with no force; a force is needed only to change its velocity.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![Under floodlights, a striker follows through after a shot while the ball flies towards the goalkeeper](scenes/football/laws_of_motion.svg "Once the ball leaves the striker's boot, nothing is pushing it towards goal. Yet it keeps flying.")

The monsoon has turned the school ground into a swamp, so Coach Pinto moves under-16 practice into the indoor sports hall. The floor is polished wood, and the first pass Tanvir plays is a disaster. He side-foots it gently to Diya, the way he would outdoors, and it keeps going: past Diya, across the whole hall, and thuds into the far wall, barely slower than when it left his foot.

Outside on the dusty ground, the same gentle pass dies after fifteen metres and sits there.

"The floor is giving it extra push," Tanvir says.

"Nothing is touching it but the floor," says Diya. "Floors don't push sideways."

Coach Pinto rolls another ball across the wood and watches it glide. "So which is the strange one," he asks, "the hall, where the ball keeps going, or the ground, where it stops?"

## The physics

The coach's question is the right one. A moving ball does not need a force to *keep* moving. It needs a force to *stop*, speed up or turn.

**Newton's first law:** a body continues in its state of rest, or of uniform motion in a straight line, unless an external net force acts on it.

The property behind this is **inertia**: every body resists any change in its state of motion. The measure of inertia is **mass**. A $0.43\,\text{kg}$ football is easy to set moving; a $70\,\text{kg}$ defender running at you is much harder to stop or turn.

Read the law carefully:

- It is the **net** force that matters. On the hall floor two forces still act on the ball: its weight $W = mg$ downwards and the **normal force** $N$ from the floor upwards. They are equal and opposite, so they cancel. With friction and drag tiny, nothing is left over: $\vec{F}_\text{net} = 0$.
- Zero net force means **no change in velocity**, not "no motion". A ball at rest stays at rest; a ball rolling at $3\,\text{m/s}$ keeps rolling at $3\,\text{m/s}$ in the same line.

On the dusty ground, friction from the rough surface and the grass acts backwards on the ball. That is an unbalanced force, so the ball slows and stops. Tanvir had it backwards: the floor adds nothing. The ground takes motion away, and the polished floor hardly does.

![Top row: a ball on a smooth surface shown at 1-second intervals with equal gaps and equal velocity arrows, its weight and normal force cancelling. Bottom row: on a rough surface the gaps shrink, with an unbalanced friction force](figures/inertia_first_law/zero-net-force-constant-velocity.svg "Top: equal gaps in equal times, like the pass on the wooden floor. Bottom: friction is unbalanced, so the gaps shrink, like the pass on the dusty ground.")

You see inertia on the pitch all the time. A winger sprinting at full speed towards the byline cannot stop dead: the grass must supply a large backward force through the boots, and on a wet pitch it can't, so the player slides on past the line.

Newton published the first law in 1687, building on Galileo's experiments with balls rolling on smooth ramps.

![The Latin title page of Newton's Principia Mathematica, printed in London in 1687](famous/newton-principia-title-page.jpg "The first law of motion opens Newton's Principia (1687). Public domain, via Wikimedia Commons.")

## Worked example

**Given:** a football, $m = 0.43\,\text{kg}$, rolls onto a polished floor at $3.0\,\text{m/s}$. The hall is $12\,\text{m}$ across. Treat friction and drag as negligible; $g = 9.8\,\text{m/s}^2$ (illustrative values).
**Find:** the forces on the ball, its speed at the far wall, and the time to cross.

*Forces.* Weight: $W = mg = 0.43 \times 9.8 \approx 4.2\,\text{N}$, downwards. The ball neither sinks into the floor nor rises off it, so the normal force is $N \approx 4.2\,\text{N}$, upwards. Horizontal forces: negligible. So $\vec{F}_\text{net} = 0$.

*First law.* Zero net force, so constant velocity: the ball reaches the wall at $3.0\,\text{m/s}$, still moving in its original direction.

*Time.* At constant speed, $t = \dfrac{d}{v} = \dfrac{12\,\text{m}}{3.0\,\text{m/s}} = 4.0\,\text{s}$.

**Sanity check:** any friction would slow the ball, so it would arrive below $3.0\,\text{m/s}$ and take *longer* than $4.0\,\text{s}$. Our answer is the ideal limit.

## Where the picture breaks

A polished floor is slippery, not frictionless. A real ball rolling on it still loses a little speed to rolling resistance and air drag, so "constant velocity" is the ideal the floor approaches, not what it achieves. The ball is also *rolling*, which involves spin; you'll meet rotation later, and here we treat the ball as a single point. Finally, the first law holds only in an **inertial frame**, one that is not itself accelerating. Seen from a braking team bus, a ball on the floor seems to roll forward "by itself"; seen from the road, it is simply carrying on as before.

## Key takeaway

Inertia is a body's resistance to any change in its motion, and mass measures it. Newton's first law says that when the net force on a body is zero, its velocity stays constant: at rest stays at rest, and moving keeps moving in a straight line at the same speed. Forces change motion; they are not needed to keep it going.
