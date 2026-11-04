---
concept_id: inertia_first_law
interest: cricket
format: explain
title: Why a ball on wet covers refuses to slow down
check:
  question: |-
    A return throw sends a cricket ball skidding across a stretch of wet covers at $5\,\text{m/s}$. Take friction and air drag as negligible. While it is on the covers, the ball:
  options:
    A: |-
      keeps moving at $5\,\text{m/s}$ in a straight line, because the net force on it is zero
    B: |-
      slows down steadily, because the force from the throw is gradually used up
    C: |-
      speeds up, because nothing is holding it back any more
    D: |-
      curves down into the covers, because its weight is an unbalanced force
  answer: A
  explanation: |-
    Weight is balanced by the normal force, and with friction and drag negligible the net force is zero. By Newton's first law the velocity stays constant: same speed, same direction.
  misconceptions:
    B: |-
      The "impetus" idea: thinks a moving body carries a force from the throw that wears off. No force travels with the ball once it leaves the hand; motion needs no force to continue.
    C: |-
      Thinks the absence of resistance makes a body speed up. With zero net force there is no acceleration at all, so the speed cannot increase.
    D: |-
      Forgets the normal force from the surface, which balances the weight exactly, so there is no vertical acceleration.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A batter drives the ball back past the bowler in a floodlit stadium](scenes/cricket/laws_of_motion.svg "Once the ball leaves the bat, nothing is pushing it forward any more. Yet it keeps going.")

It has rained all morning at the district ground. The covers are off the pitch at last, but a long plastic sheet still lies glistening near the square, and the groundstaff haven't dragged it away yet.

Meera, fielding at mid-on, chases a push towards the sheet. The ball rolls slowly across the grass, losing speed with every metre. Then it hits the wet plastic and something odd happens: it stops slowing down. It skids across the sheet at almost exactly the speed it arrived, and only starts to die again when it reaches the grass on the other side.

"The shot ran out of force on the grass," says her teammate Rohan, "but on the plastic it got some back?"

Meera isn't convinced. Nothing touched the ball on the sheet. So why did it keep going there — and what was actually stopping it on the grass?

## The physics

The answer turns the question around. The ball doesn't need a force to *keep* moving. It needs a force to *stop*.

**Newton's first law:** a body stays at rest, or keeps moving with constant velocity (the same speed in the same straight line), unless an external net force acts on it.

The property that makes this happen is **inertia**: the tendency of every body to resist a change in its state of motion. Mass is the measure of inertia — a heavier ball is harder to start, stop or turn.

Two points to read carefully:

- It is the **net** force that matters. On the covers, two forces still act on the ball: its weight $W = mg$ downwards and the **normal force** $N$ from the sheet upwards. They are equal and opposite, so they cancel. With friction and air drag negligible, nothing is left over: $\vec{F}_\text{net} = 0$, so the velocity cannot change.
- "Zero net force" does **not** mean "at rest". It means **no change** in velocity. A ball at rest stays at rest; a ball skidding at $4\,\text{m/s}$ keeps skidding at $4\,\text{m/s}$.

On the grass, friction from the turf acts backwards on the ball. That is an unbalanced force, so the ball slows. Rohan's "the shot ran out of force" gets it backwards: the ball never carried a force with it. The grass took its motion away, and the sheet simply didn't.

![Top row: a ball on a smooth surface shown at 1-second intervals with equal gaps and equal velocity arrows, its weight and normal force cancelling. Bottom row: on a rough surface the gaps shrink, with an unbalanced friction force](figures/inertia_first_law/zero-net-force-constant-velocity.svg "Equal gaps in equal times mean constant velocity, which is what zero net force gives. Shrinking gaps show a net force, here friction, acting against the motion.")

You feel inertia yourself on the team bus. When the driver brakes hard, the kit bags on the seats slide forward. No force threw them forward: the bus slowed down, and the bags simply carried on at the old speed until friction or the seat in front stopped them.

The first law was set down by Isaac Newton in 1687, building on Galileo's experiments with balls rolling on smooth ramps.

![The Latin title page of Newton's Principia Mathematica, printed in London in 1687](famous/newton-principia-title-page.jpg "The first law opens Newton's Principia (1687). Public domain, via Wikimedia Commons.")

## Worked example

**Given:** a ball ($m = 0.16\,\text{kg}$) reaches a wet sheet moving at $4.0\,\text{m/s}$. The sheet is $6.0\,\text{m}$ long. Treat friction and air drag on the sheet as negligible; take $g = 9.8\,\text{m/s}^2$.
**Find:** the forces on the ball, its speed as it leaves the sheet, and how long it takes to cross.

*Forces.* Weight: $W = mg = 0.16 \times 9.8 \approx 1.6\,\text{N}$, downwards. The ball doesn't sink into the sheet or rise off it, so the normal force is $N \approx 1.6\,\text{N}$, upwards. Horizontal forces: negligible. So $\vec{F}_\text{net} = 0$.

*Prediction from the first law.* Zero net force means constant velocity, so the ball leaves the sheet at $4.0\,\text{m/s}$, in the same direction it arrived.

*Time.* At constant speed, $t = \dfrac{d}{v} = \dfrac{6.0\,\text{m}}{4.0\,\text{m/s}} = 1.5\,\text{s}$.

**Sanity check:** if friction did act, the ball would slow down, so it would leave the sheet below $4.0\,\text{m/s}$ and take *longer* than $1.5\,\text{s}$. The first-law answer is the fastest the ball could possibly cross.

## Where the picture breaks

A wet plastic sheet is slippery, not perfectly frictionless, and air drag never quite vanishes. A real ball would lose a little speed even on the sheet; "constant velocity" is the ideal the sheet approaches. A rolling ball also has spin, which you'll meet later with rotational motion; here we treat the ball as a single point. And the first law holds only in an **inertial frame** — one that is not itself accelerating. Sitting in a braking bus, the bags seem to lurch forward "by themselves", but viewed from the road they are just carrying on as before.

## Key takeaway

Inertia is a body's resistance to any change in its motion, and mass measures it. Newton's first law says that if the net force on a body is zero, its velocity stays constant: at rest stays at rest, moving stays moving in a straight line at the same speed. Forces are needed to change motion, not to keep it going.
