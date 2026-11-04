---
concept_id: inertia_first_law
interest: gaming
format: explain
title: Why the spaceship in your game will not stop drifting
check:
  question: |-
    In a space game, a $1500\,\text{kg}$ ship coasts at $20\,\text{m/s}$ in deep space, far from any planet, with its engines switched off. If the game follows real physics, what does the ship do?
  options:
    A: |-
      It slows down gradually, as the push it got from its engines wears off
    B: |-
      It keeps moving at $20\,\text{m/s}$ in a straight line, because the net force on it is zero
    C: |-
      It stops almost at once, because a force is needed to keep anything moving
    D: |-
      It slows down, because its large inertia acts as a force holding it back
  answer: B
  explanation: |-
    With the engines off and no planet nearby, no net force acts on the ship. By Newton's first law its velocity stays constant: the same speed, in the same straight line.
  misconceptions:
    A: |-
      The "impetus" idea: thinks a moving body stores a force that is gradually used up. No force travels with the ship after the engines stop; it needs no force to keep moving.
    C: |-
      Thinks motion needs a force to continue, so removing the force removes the motion. Forces change motion; they are not needed to maintain it.
    D: |-
      Treats inertia as a force. Inertia is a property of the ship (measured by its mass) that resists changes in motion; it resists slowing down just as much as speeding up.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a racing game on the monitor and a zero-gravity game on a tablet](scenes/gaming/laws_of_motion.svg "Two games, two worlds. On the track the kart needs grip to turn; in zero-g, nothing slows anything down.")

It's the last hour of the school game-dev club, and Ananya is proudly demoing her first space shooter. She taps the thrust key, her little ship leaps forward, and she lets go.

The ship keeps going. And going. It drifts right off the edge of the map.

"It's broken," says Kabir, leaning over her shoulder. "Look at a racing game. Let go of the accelerator and the car slows down and stops. Your ship should do that too. You forgot to switch the engine off properly."

"I did switch it off," says Ananya. "There's no code pushing the ship at all after I let go. It just... keeps going."

Kabir is sure a moving thing needs something to keep it moving. Ananya's game says otherwise. Which of the two games has it right, and what is actually happening to that ship after the thrust stops?

## The physics

Ananya's game is right, and the question turns around. A body doesn't need a force to *keep* moving. It needs a force to *change* its motion.

**Newton's first law:** a body stays at rest, or keeps moving with constant velocity (the same speed in the same straight line), unless an external net force acts on it.

The property behind this is **inertia**: the tendency of every body to resist any change in its state of motion. Its measure is the body's **mass**. A heavy cargo ship is harder to start, stop or turn than a light fighter.

Read the law carefully:

- It is the **net** force that matters. Several forces can act and still cancel. A car cruising at steady speed on a flat road has the engine's drive forwards and air drag and rolling resistance backwards, balanced exactly.
- **Zero net force does not mean "at rest".** It means **no change** in velocity. Ananya's ship, with no force on it, keeps whatever velocity it had when the thrust stopped.

So why does Kabir's racing car stop? Because the racing game adds forces that oppose the motion: air drag and friction from the road on the tyres. Take those away, as in deep space, and nothing is left to change the velocity.

![Top row: a ball on a smooth surface shown at 1-second intervals with equal gaps and equal velocity arrows, its weight and normal force cancelling. Bottom row: on a rough surface the gaps shrink, with an unbalanced friction force](figures/inertia_first_law/zero-net-force-constant-velocity.svg "Top: zero net force, equal gaps in equal times, like Ananya's ship. Bottom: an unbalanced backward force makes the gaps shrink, like the racing car when you release the accelerator.")

Physics engines build the first law into their update rule. Each time step, commonly $1/60\,\text{s}$, the engine changes a body's velocity only by the forces acting on it, then moves it by velocity × time step. With no force, the velocity never changes, and the ship moves the same distance every frame, forever.

The first law was published by Isaac Newton in 1687, building on Galileo's experiments with balls rolling on smooth ramps.

![The Latin title page of Newton's Principia Mathematica, printed in London in 1687](famous/newton-principia-title-page.jpg "Newton's first law opens the Principia (1687), centuries before anyone coded a spaceship. Public domain, via Wikimedia Commons.")

## Worked example

**Given:** a ship of mass $2000\,\text{kg}$ (illustrative) drifts at $12\,\text{m/s}$ in deep space with its engines off, far from any planet. The game runs its physics at $60$ steps per second.
**Find:** its velocity and the distance it covers in the next $5.0\,\text{s}$, and how far it moves in each physics step.

*Forces.* Engines off, no air, gravity from distant bodies negligible: $\vec{F}_\text{net} = 0$.

*First law.* Zero net force, so the velocity stays $12\,\text{m/s}$ in the same direction. The mass doesn't enter: every body, heavy or light, keeps its velocity when the net force is zero.

*Distance.* At constant velocity, $d = vt = 12\,\text{m/s} \times 5.0\,\text{s} = 60\,\text{m}$.

*Per step.* $\Delta t = \dfrac{1}{60}\,\text{s}$, so each step moves the ship $12 \times \dfrac{1}{60} = 0.20\,\text{m}$.

**Sanity check:** $5.0\,\text{s}$ is $5.0 \times 60 = 300$ steps, and $300 \times 0.20\,\text{m} = 60\,\text{m}$ ✓.

## Where the picture breaks

A game is not obliged to obey physics. Many arcade space games deliberately add invisible "damping" so ships slow down when you let go, because it is easier to control. That is a design choice, not how space works. Real deep space is also not perfectly force-free: the Sun and planets pull on everything, weakly. And the first law holds only in an **inertial frame**, one that is not itself accelerating; a camera that follows and turns with the ship can make things appear to drift for no reason. Finally, the engine's fixed steps are an approximation of smooth motion, though with zero force the result is exact.

## Key takeaway

Inertia is a body's resistance to any change in its motion, and mass measures it. Newton's first law says that when the net force on a body is zero, its velocity stays constant: at rest stays at rest, and moving keeps moving in a straight line at the same speed. Forces change motion; they are not needed to keep it going.
