---
concept_id: uniform_circular_motion
interest: smartphones
format: explain
title: The charging puck that flew off the turntable
check:
  question: |-
    A phone sits near the edge of a turntable that spins at a constant rate, so the phone goes round a circle at constant speed. Which statement is correct?
  options:
    A: |-
      Its velocity is constant, because its speed is constant, so it is not accelerating.
    B: |-
      Its velocity points towards the centre of the turntable at every instant.
    C: |-
      If it slid off, it would fly straight outwards, along the radius, away from the centre.
    D: |-
      Its velocity is along the tangent and keeps changing direction, so it is accelerating.
  answer: D
  explanation: |-
    In circular motion the velocity is always along the tangent to the circle. Its size stays the same but its direction keeps turning, and any change in velocity, including a change of direction only, is an acceleration.
  misconceptions:
    A: |-
      Treats speed and velocity as the same thing. Velocity is a vector, so a change in direction alone changes it.
    B: |-
      Confuses the direction of the velocity with the direction of the acceleration. The velocity is along the tangent; it is the change in velocity that points inwards.
    C: |-
      Believes something "flings" objects outwards. Once released, nothing pushes it sideways, so it carries on along the tangent, in the direction it was moving at that instant.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![An evening terrace: a phone showing a map, a drone flying at a slant and an earbud case skidding off a table](scenes/smartphones/motion_plane.svg "Anything moving has a velocity arrow. On a turntable that arrow keeps pointing a new way, even when its length never changes.")

Farhan sells phone accessories online from a small shop in his lane, and today he is filming product videos. A smartwatch sits on a motorised turntable, and a charging puck rests near the edge. The turntable glides round at a slow, perfectly steady pace.

He wants a faster spin, so he turns the dial up. The puck slides, lifts off the edge, and skids across the counter into a box of cables.

"It got flung outwards," says his niece Sana, pointing from the centre of the turntable to the edge. "Straight out, like that."

Farhan replays the phone video frame by frame. The puck did not go straight out from the centre at all. It left along a line that just grazed the turntable's rim.

And something else bothers Sana. Before it flew off, the puck was going round at a constant speed. So was its velocity changing or not?

## The physics

When a body moves round a circle at **constant speed**, the motion is called **uniform circular motion**. The word "uniform" refers to the speed, not the velocity.

At every instant, the **velocity is along the tangent** to the circle, at right angles to the radius. That's the direction the body is heading at that instant. As it goes round, the tangent keeps turning, so the velocity arrow keeps pointing a new way, while its length (the speed $v$) stays fixed.

![A circle with equal-length velocity arrows drawn tangent at six points, and the same six arrows redrawn from one point showing only their directions differ](figures/uniform_circular_motion/velocity-around-circle.svg "Same length, different directions. Drawn from one point, the velocity arrows fan out all the way round: the velocity is never the same twice.")

Velocity is a vector, so a change in direction is a change in velocity, even if the speed never changes. And acceleration is the rate of change of velocity, $\vec{a} = \Delta\vec{v}/\Delta t$. So **a body in uniform circular motion is always accelerating**. The next lesson finds the size and direction of that acceleration.

This also explains Sana's puck. While friction from the turntable held it on the circle, its velocity was turned a little every instant. When friction couldn't keep up, nothing turned it any more, so it carried on in a straight line in the direction it was already going: **along the tangent**, not along the radius. Nothing pushed it outwards.

Useful quantities: for a circle of radius $r$ covered once in time $T$ (the **period**),

$$v = \frac{2\pi r}{T}, \qquad \omega = \frac{2\pi}{T}, \qquad v = \omega r$$

where $\omega$ is the **angular speed** in radians per second.

## Worked example

**Given (illustrative):** the puck sits $r = 0.20\,\text{m}$ from the centre; the turntable makes one full turn every $T = 4.0\,\text{s}$.
**Find:** the puck's speed, and how much its velocity changes in half a turn.

1. **Speed:** $v = \dfrac{2\pi r}{T} = \dfrac{2\pi \times 0.20}{4.0} \approx 0.31\,\text{m/s}$, a slow crawl, about a third of a metre each second.
2. **Half a turn later** (after $2.0\,\text{s}$), the puck is on the opposite side of the circle, moving at the same $0.31\,\text{m/s}$, but in exactly the **opposite direction**.
3. **Change in velocity:** going from $+0.31$ to $-0.31\,\text{m/s}$ along one line is a change of $0.31 - (-0.31) \approx 0.63\,\text{m/s}$. The speed changed by zero; the velocity changed by twice the speed.

**Sanity check:** after a whole turn the velocity is back where it started, so the change over a full turn is zero, even though it was changing all the way round.

## Where the picture breaks

A real turntable takes a moment to speed up and slow down, and while it does, the speed isn't constant, so the motion is only uniform once it has settled. The puck also doesn't leave at one clean instant: it starts sliding, so for a short while it slips while still turning, and it curves slightly before it breaks free. On the counter, friction then slows it down. The tangent rule is exact for the instant it stops being held on the circle.

## Key takeaway

In **uniform circular motion** the speed is constant but the velocity is not: it always points along the tangent, and its direction keeps turning. A change of direction is a change of velocity, so the body is accelerating even at constant speed. Let go, and it leaves along the tangent, not outwards along the radius.
