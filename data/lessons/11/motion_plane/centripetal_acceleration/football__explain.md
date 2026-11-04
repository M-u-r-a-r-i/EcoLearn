---
concept_id: centripetal_acceleration
interest: football
format: explain
title: Why a sprinter can't take a tight curve round a defender
check:
  question: |-
    A player runs round the centre circle, radius $9.15\,\text{m}$, at a steady $6.0\,\text{m/s}$. What is the player's acceleration?
  options:
    A: |-
      About $0.66\,\text{m/s}^2$, towards the centre of the circle
    B: |-
      About $3.9\,\text{m/s}^2$, outwards, away from the centre
    C: |-
      About $3.9\,\text{m/s}^2$, towards the centre of the circle
    D: |-
      Zero, because the speed is not changing
  answer: C
  explanation: |-
    $a_c = v^2/r = 6.0^2/9.15 = 36/9.15 \approx 3.9\,\text{m/s}^2$, pointing towards the centre of the circle, because the velocity keeps turning inwards.
  misconceptions:
    A: |-
      Uses $v/r$ instead of $v^2/r$. That gives the angular speed in rad/s, not an acceleration.
    B: |-
      Follows the "thrown outwards" feeling on a bend and puts the acceleration outwards. The acceleration of a body moving in a circle points inwards.
    D: |-
      Thinks acceleration means only a change of speed. A change in the direction of the velocity is also an acceleration.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A player lofts the ball in an arc over the goalkeeper while a teammate jogs round the centre circle](scenes/football/motion_plane.svg "Curved runs are everywhere in football. The faster the run, the harder the curve is to hold.")

Ishaan is the fastest winger in his academy. In a practice match he knocks the ball past a defender and tries to swerve round him at full sprint, on a tight curve. His studs skid, his feet go from under him, and he ends up on the grass while the defender strolls away with the ball.

"I've done that curve a hundred times," he complains to his coach, Ms Kaur. "Same curve, no problem."

"At jogging pace," she says. "Today you were going twice as fast. Going round the same curve at twice the speed doesn't ask twice as much of your legs. It asks four times as much."

Ishaan frowns. Twice as fast, four times as hard? And what exactly is "it" — what is changing as you go round a curve at a steady speed?

## The physics

In the last lesson you saw that a body in uniform circular motion is accelerating, because its velocity keeps changing direction. This acceleration is called **centripetal acceleration** ("centre-seeking").

**Direction.** Compare the velocity at two nearby moments. Both arrows have the same length $v$, but the later one has turned a little. The change $\Delta\vec{v}$ joins their heads, and it points **towards the centre** of the circle. Since $\vec{a} = \Delta\vec{v}/\Delta t$, the acceleration points towards the centre too, at every instant, at right angles to the velocity.

![Left: a circle with three points, each showing a tangent velocity arrow and an acceleration arrow pointing to the centre. Right: velocity vectors at two nearby moments drawn tail to tail, with the change in velocity pointing inwards](figures/centripetal_acceleration/acceleration-towards-centre.svg "The velocity turns, so the change in velocity, and so the acceleration, points to the centre. The speed stays the same; only the direction changes.")

**Size.** The triangle formed by the two velocity arrows has the same shape as the triangle formed by the two position vectors, since both have two equal sides with an angle $\Delta\theta$ between them. So $|\Delta\vec{v}|/v = |\Delta\vec{r}|/r$. Over a short interval $|\Delta\vec{r}| \approx v\,\Delta t$, which gives $|\Delta\vec{v}|/\Delta t = v^2/r$:

$$a_c = \frac{v^2}{r} = \omega^2 r$$

using $v = \omega r$. Here $v$ is the speed, $r$ the radius of the circle and $\omega$ the angular speed; $a_c$ is in $\text{m/s}^2$. This holds for **uniform** circular motion, at constant speed.

That is Ms Kaur's point. Because $a_c$ depends on $v^2$, doubling the speed on the same curve means **four times** the acceleration. And a tighter curve, smaller $r$, at the same speed needs more still. Whatever turns Ishaan, the grip of his studs on the grass, has to supply it. You'll meet that force in Laws of Motion.

## Worked example

**Given:** the centre circle, $r = 9.15\,\text{m}$. Ishaan runs round it at a steady $4.0\,\text{m/s}$, then at $8.0\,\text{m/s}$. Then a tight curve round a defender, $r = 4.0\,\text{m}$, at $8.0\,\text{m/s}$ (illustrative).
**Find:** the centripetal acceleration in each case, and its direction.

$$a_1 = \frac{4.0^2}{9.15} = \frac{16}{9.15} \approx 1.75\,\text{m/s}^2$$

$$a_2 = \frac{8.0^2}{9.15} = \frac{64}{9.15} \approx 7.0\,\text{m/s}^2$$

$$a_3 = \frac{8.0^2}{4.0} = \frac{64}{4.0} = 16\,\text{m/s}^2$$

Each points towards the centre of the curve. Doubling the speed multiplied the acceleration by $7.0/1.75 = 4$. The tight curve at sprint speed needs $16\,\text{m/s}^2$, more than $1.6$ times $g$. That's a big ask of studs on grass, and it's why Ishaan slipped.

**Sanity check (a second way):** for the first case, $\omega = 4.0/9.15 \approx 0.437\,\text{rad/s}$, so $\omega^2 r = 0.191 \times 9.15 \approx 1.75\,\text{m/s}^2$. Same answer.

## Where the picture breaks

A real swerve is not a perfect circle at constant speed. Ishaan's curve tightens and loosens, and he slows down into it, so his acceleration also has a part along his path, not only towards the centre. The formula gives the inward part at each instant, using the local radius of the curve. A player is also not a point: he leans into the bend, and the grip acts at his feet, not at his middle. That's a question for Laws of Motion, not for this formula.

## Key takeaway

A body moving in a circle at constant speed has a **centripetal acceleration** $a_c = v^2/r = \omega^2 r$, always pointing towards the centre, at right angles to the velocity. Constant speed does not mean zero acceleration. Because $a_c$ grows with $v^2$, the same curve at twice the speed needs four times the acceleration.
