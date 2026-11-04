---
concept_id: second_law
interest: cricket
format: misconception
title: Is a six carrying the force of the shot
check:
  question: |-
    A batter hits a six. While the ball is still rising towards the boundary, which force or forces act on it? (Ignore air resistance.)
  options:
    A: |-
      The force of the hit, and gravity
    B: |-
      Only the force of the hit, which is why it keeps rising
    C: |-
      No force at all — nothing is touching it
    D: |-
      Only gravity, acting downwards
  answer: D
  explanation: |-
    Once the ball leaves the bat, nothing is pushing it forward; the only force (ignoring air) is its weight, $mg$, downwards. Its forward motion continues because of the velocity it already has.
  misconceptions:
    A: |-
      Believes a moving object carries the force that started it ("impetus") — force changes motion, it isn't stored in the ball.
    B: |-
      Holds the impetus idea and also forgets gravity, which acts on the ball at every moment of its flight.
    C: |-
      Thinks forces need contact, missing gravity, which acts without touching.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A batter hits the ball high in a floodlit stadium](scenes/cricket/laws_of_motion.svg "The ball leaves the bat — and then what keeps it going?")

The final is on the TV at Rohan's house, and the whole family is shouting. A batter swings, and the ball sails high over long-on for six. The commentator roars: "Oh, there was *so much force* in that shot — it's still carrying!"

Rohan's grandmother turns to him. "You study physics. Where is that force now? The ball is up in the sky. Is the bat's push still inside it, carrying it along?"

Rohan opens his mouth to say "yes, obviously" — and stops. The bat touched the ball for a thousandth of a second, and now it's forty metres away. What exactly is keeping that ball flying?

## The common belief

A batter middles one and the ball soars over long-on. Ask a room of students what keeps it flying, and many will say: "The force of the shot. A harder hit puts more force into the ball, and that force carries it over the rope. A gentle push has less force in it, so it drops short."

In this picture, a fast ball *has* a lot of force, and a slow ball has a little.

## Why it feels right

Part of this is true: a harder hit really does send the ball farther, and the hit really did involve a large force. And in everyday life, things that are moving fast usually seem powerful — a fast ball stings your hands. It's natural to picture the force of the shot travelling along with the ball and slowly running out, like fuel.

People held this "impetus" idea for centuries. It feels so right that it took Galileo and Newton to overturn it.

## What actually happens

The bat's force acts only while bat and ball touch — about a millisecond. After that, nothing is pushing the ball forward at all. The only force on it (ignoring air) is gravity: its weight, $mg$, straight down.

So why does it keep going forward? Because it already has a forward velocity, and nothing is changing that forward velocity. Force is not what keeps the ball moving; force is what **changes** its motion. Gravity keeps pulling downward, so the ball's upward velocity shrinks, reaches zero at the top of its flight, and then it comes down — while its horizontal velocity carries on unchanged.

![A ball on a curved path, with a red downward arrow for its weight, a blue arrow along the path for its velocity, and a crossed-out grey arrow labelled force of the hit](figures/second_law/forces-on-ball-in-flight.svg "Once the ball leaves the bat, its weight is the only force on it. The velocity arrow shows motion — it is not a force.")

A big six and a gentle dab, once in the air, feel exactly the same force: the same weight, $mg$. The difference between them is their *velocity*, not the force acting on them.

## The physics

Newton's second law relates force to the **change** in motion:

$$\vec{F}_\text{net} = m\vec{a} = m\frac{d\vec{v}}{dt}$$

Velocity itself does not appear in this equation — only its rate of change. A large net force means a large acceleration, not a large speed. A body can move very fast with zero net force (it just keeps moving at constant velocity), or be momentarily at rest with a large net force (like the ball at the very top of a vertical throw, where $\vec{a} = \vec{g}$).

The misconception mixes up force with momentum. The hit *changes* the ball's momentum; the momentum is what the ball carries.

## Worked example

A ball ($0.16\,\text{kg}$) is in flight after two different shots: one moving at $35\,\text{m/s}$, one at $5\,\text{m/s}$. Ignoring air resistance, find the net force and acceleration of each.

The only force on either ball is its weight:

$$F = mg = 0.16 \times 9.8 \approx 1.6\,\text{N} \quad \text{(downwards, for both)}$$

$$a = \frac{F}{m} = \frac{1.57}{0.16} = 9.8\,\text{m/s}^2 \quad \text{(downwards, for both)}$$

Same force, same acceleration — even though one is seven times faster.

(With air resistance the faster ball does feel a larger drag — but drag points *against* its motion and slows it down. It never pushes the ball forward.)

## Key takeaway

A moving ball does not carry the force that launched it. Once it leaves the bat, the only force on it (ignoring air) is gravity. Force causes **acceleration** — a change in velocity — not velocity itself: $\vec{F}_\text{net} = m\vec{a}$.
