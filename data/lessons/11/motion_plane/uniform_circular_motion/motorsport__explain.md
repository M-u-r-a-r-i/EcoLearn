---
concept_id: uniform_circular_motion
interest: motorsport
format: explain
title: Why a kart that loses grip goes straight on
check:
  question: |-
    A kart is going round a constant-radius corner at a steady $12\,\text{m/s}$ when its tyres suddenly lose all grip. With nothing left to turn it, which way does it travel?
  options:
    A: |-
      Straight on along the tangent, in the direction its velocity pointed at that instant.
    B: |-
      Straight outwards along the radius, directly away from the centre of the corner.
    C: |-
      It keeps curving for a while before gradually straightening out.
    D: |-
      Straight towards the centre of the corner, because that is where its acceleration points.
  answer: A
  explanation: |-
    In circular motion the velocity at every instant is along the tangent. Remove whatever was bending it, and the kart simply keeps the velocity it had — a straight line along that tangent.
  misconceptions:
    B: |-
      Treats the outward "thrown-about" feeling in a corner as a real force flinging the kart outwards. Nothing pushes it outwards; it just keeps its tangential velocity while the track curves away beneath it.
    C: |-
      Assumes a body somehow remembers its curved motion. Without a sideways force there is nothing to bend the velocity, so the straightening is instant, not gradual.
    D: |-
      Confuses the direction of the acceleration with the direction of motion. The acceleration points inwards only while something is turning the kart, and it is at right angles to the velocity, never along it.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race circuit seen from above: cars on the straights and one sweeping through a curved corner with a blue arrow showing its velocity along the tangent](scenes/motorsport/motion_plane.svg "Look at the arrow on the cornering car: its velocity points along the track, not across it towards the middle of the corner.")

Vikram is doing his first hour of instructor training at a karting track, and his trainer, Farida, takes him for a walk round the outside of the long left-hander.

She points at the grass beyond the kerb, where tyre marks lead off the track. They are dead straight.

"Every spin-off leaves those," she says. "And every beginner tells me the same thing afterwards: 'the kart threw me outwards, away from the corner.' Look at the marks. If something had thrown them outwards, they would point at the middle of the corner. They don't. They point exactly where the kart was already going."

Vikram stares at the straight grey lines. The kart was travelling in a circle a moment earlier. So which way, exactly, is something moving at each instant when it goes round a bend — and why is that not "outwards"?

## The physics

**Uniform circular motion** is motion along a circle at **constant speed**. A kart held on a constant-radius corner, a point on a spinning wheel rim, a satellite in a circular orbit — all are examples.

At every instant the velocity points along the **tangent** to the circle, at right angles to the radius. If whatever holds the body on the circle stops acting, the body carries straight on along that tangent. It never sets off along the radius, inwards or outwards.

![A circle with velocity arrows drawn tangent to it at several points, all the same length but pointing in different directions, and the same arrows redrawn from a single point fanning out](figures/uniform_circular_motion/velocity-around-circle.svg "Every velocity arrow is the same length, because the speed is constant, but each points a different way. Redrawn from one point they fan out — so the velocity is changing all the time.")

That is the answer to Farida's question. The grip of the tyres is what bends the kart's velocity round the corner. Take the grip away and there is nothing left to bend it, so it keeps exactly the velocity it had at that instant — along the tangent, straight across the grass.

The deeper point is this: **velocity is a vector**. In uniform circular motion its size never changes, but its direction changes continuously, so the velocity itself changes continuously. A changing velocity means the body is **accelerating**, even though the speedometer reads the same number all the way round. The size and direction of that acceleration are the next lesson.

Some terms for describing the motion, on a circle of radius $r$:

- **Period** $T$: the time for one full revolution, $T = \dfrac{2\pi r}{v}$.
- **Frequency** $\nu = 1/T$: revolutions per second.
- **Angular speed** $\omega = \dfrac{2\pi}{T}$, in rad/s: the angle swept per second, with $v = \omega r$.

## Worked example

**Given (illustrative):** a kart circling a constant-radius skid pan of radius $r = 20\,\text{m}$ at a steady $v = 10\,\text{m/s}$ (about $36\,\text{km/h}$).
**Find:** its angular speed, the time for one lap of the circle, and how much its velocity changes over a quarter of a lap.

Angular speed, from $v = \omega r$:
$$\omega = \frac{v}{r} = \frac{10}{20} = 0.50\,\text{rad/s}$$

Period, the time for the full $2\pi$ radians:
$$T = \frac{2\pi}{\omega} = \frac{6.28}{0.50} \approx 13\,\text{s}$$

Now the quarter lap, which takes about $3.1\,\text{s}$. The kart starts heading, say, due north at $10\,\text{m/s}$ and ends heading due east at $10\,\text{m/s}$. Those two velocities are at right angles, so the change between them is

$$|\Delta\vec{v}| = \sqrt{10^2 + 10^2} \approx 14\,\text{m/s}$$

The *speed* changed by zero. The *velocity* changed by about $14\,\text{m/s}$ — more than the kart's speed.

**Sanity check:** $T = 2\pi r/v = 2\pi(20)/10 \approx 13\,\text{s}$ the other way round, which agrees. And over a half lap the velocity simply reverses, giving $|\Delta\vec{v}| = 2v = 20\,\text{m/s}$, the largest change possible — as it should be.

## Where the picture breaks

A real corner is rarely a perfect circle at a perfectly steady speed: drivers ease off on entry and squeeze the throttle on exit, so the motion is not *uniform*, and most corners are not constant-radius. The tangent line is also an idealisation of the first instant only — the sliding kart still touches the ground, so friction slows it and the grass drags on it, and the marks eventually curve and stop. What holds exactly is the rule itself: at the moment grip is lost, the velocity is along the tangent.

## Key takeaway

In uniform circular motion the speed is constant but the velocity is not: it always lies along the tangent, and its direction turns continuously. A changing velocity means an acceleration, so a body going round a bend at a steady speed is accelerating. Remove what was turning it and it leaves along the tangent — straight on, never outwards.
