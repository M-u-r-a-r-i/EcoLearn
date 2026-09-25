---
concept_id: centripetal_acceleration
interest: smartphones
format: explain
title: What the sensor app felt on the merry-go-round
check:
  question: |-
    A phone rides on a turntable at $0.10\,\text{m}$ from the centre, moving at a steady $0.50\,\text{m/s}$. What is its acceleration?
  options:
    A: |-
      $2.5\,\text{m/s}^2$, towards the centre of the turntable
    B: |-
      $5.0\,\text{m/s}^2$, towards the centre of the turntable
    C: |-
      $2.5\,\text{m/s}^2$, outwards, away from the centre
    D: |-
      Zero, because the speed is not changing
  answer: A
  explanation: |-
    $a_c = v^2/r = 0.50^2/0.10 = 0.25/0.10 = 2.5\,\text{m/s}^2$, directed towards the centre, because that is the way the velocity keeps turning.
  misconceptions:
    B: |-
      Uses $v/r$ instead of $v^2/r$. That combination is the angular speed, in rad/s, not an acceleration: check the units.
    C: |-
      Follows the outward "thrown to the edge" feeling and reverses the direction. The acceleration of a body moving in a circle points inwards, towards the centre.
    D: |-
      Takes acceleration to mean only a change of speed. A change in the direction of the velocity is just as much an acceleration.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![An evening terrace: a phone showing a map, a drone flying at a slant with a blue velocity arrow, and an earbud case skidding off a table](scenes/smartphones/motion_plane.svg "The blue arrows show velocities. On a ride that goes round in a circle, the velocity arrow keeps swinging, and a phone's sensor can feel that swing.")

The mela has come to town, and Divya has talked her older brother Nikhil onto the big merry-go-round. She has a plan: she's opened a free sensor app that shows the phone's acceleration as an arrow on the screen, and she holds the phone flat on her lap as the ride spins up.

Once the ride settles into its steady whirl, the music playing and the lights blurring past, she looks down. The speed isn't changing at all. But the arrow isn't zero. It's steady, fairly large, about half of $g$, and it points sideways.

"Bet it points outwards," says Nikhil. "I can feel myself being thrown to the edge."

Divya turns the phone so he can see. The arrow points the other way: straight at the ride's centre pole.

Why is there any acceleration at all at a steady speed, how big should it be, and why does it point *in*?

## The physics

In the last lesson you saw that a body in uniform circular motion is accelerating, because its velocity keeps changing direction. That acceleration is called **centripetal acceleration**, meaning "centre-seeking".

**Direction.** Take the velocity at two nearby instants. Both arrows have the same length $v$, but the later one has turned a little. The change $\Delta\vec{v}$, drawn from the head of the first to the head of the second when they share a tail, points **towards the centre**. Since $\vec{a} = \Delta\vec{v}/\Delta t$, the acceleration points to the centre too, at every instant, at right angles to the velocity.

![A circle with velocity drawn tangent at several points and acceleration drawn towards the centre, alongside two nearby velocity arrows tail to tail whose difference points inwards](figures/centripetal_acceleration/acceleration-towards-centre.svg "The velocity turns, so the change in velocity, and therefore the acceleration, points to the centre. The speed never changes; only the direction does.")

**Size.** The triangle made by the two velocity arrows has the same shape as the triangle made by the two radii (each has the same small angle $\Delta\theta$ between two equal sides), so $|\Delta\vec{v}|/v = |\Delta\vec{r}|/r$. Over a short interval $|\Delta\vec{r}| \approx v\,\Delta t$, which gives $|\Delta\vec{v}|/\Delta t = v^2/r$:

$$a_c = \frac{v^2}{r} = \omega^2 r$$

using $v = \omega r$. Here $v$ is the speed, $r$ the radius and $\omega$ the angular speed; the unit is $\text{m/s}^2$. This holds for **uniform** circular motion, at constant speed.

Speed counts twice: $a_c$ grows with the **square** of $v$, so doubling the ride's speed at the same radius makes the acceleration four times as big.

Something must supply that inward acceleration. For Divya it is the seat and the pole pushing her inwards. The outward "throw" Nikhil feels is not a force pushing him out; it is his body tending to carry straight on along the tangent while the ride keeps pulling him round.

## Worked example

**Given (illustrative):** Divya's seat is $r = 5.0\,\text{m}$ from the centre pole, moving at a steady $v = 5.0\,\text{m/s}$ (about $18\,\text{km/h}$).
**Find:** her centripetal acceleration and how it compares with $g$.

1. $a_c = \dfrac{v^2}{r} = \dfrac{5.0^2}{5.0} = \dfrac{25}{5.0} = 5.0\,\text{m/s}^2$, pointing horizontally, straight at the pole.
2. Compared with gravity: $\dfrac{5.0}{9.8} \approx 0.5$. So the phone feels about **half a $g$** sideways, the reading on Divya's screen.
3. Direction check: the arrow points inwards, the way the velocity is turning, not outwards the way Nikhil feels pushed.

**Sanity check (a second way):** $\omega = v/r = 5.0/5.0 = 1.0\,\text{rad/s}$, and $\omega^2 r = 1.0^2 \times 5.0 = 5.0\,\text{m/s}^2$. Same answer.

## Where the picture breaks

A phone's sensor chip also feels gravity, so its full reading tilts upward; the sideways part is the one that matches $v^2/r$, and only if the phone is held flat. Different apps also draw the arrow differently: some "g-meter" apps draw the direction you feel thrown, which is outwards, the opposite way, so always check an app's convention. A merry-go-round horse also bobs up and down, adding a changing vertical part, and while the ride is speeding up there is an extra part along the direction of motion. $a_c = v^2/r$ is the inward part, exact for steady circular motion.

## Key takeaway

A body moving in a circle at constant speed has a **centripetal acceleration** $a_c = v^2/r = \omega^2 r$, always pointing towards the centre and at right angles to the velocity. Constant speed does not mean zero acceleration. Because $v$ is squared, going twice as fast round the same circle means four times the acceleration.
