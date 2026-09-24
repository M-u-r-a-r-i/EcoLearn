---
concept_id: centripetal_acceleration
interest: motorsport
format: explain
title: The one g hiding in a fast corner
check:
  question: |-
    A kart goes round a corner of radius $10\,\text{m}$ at a steady $8.0\,\text{m/s}$. What is its acceleration?
  options:
    A: |-
      $0.80\,\text{m/s}^2$, towards the centre of the corner
    B: |-
      $6.4\,\text{m/s}^2$, outwards, away from the centre
    C: |-
      $6.4\,\text{m/s}^2$, towards the centre of the corner
    D: |-
      Zero, because the speed is not changing
  answer: C
  explanation: |-
    $a_c = v^2/r = 8.0^2/10 = 64/10 = 6.4\,\text{m/s}^2$, directed towards the centre of the circle, because that is the way the velocity keeps turning.
  misconceptions:
    A: |-
      Uses $v/r$ instead of $v^2/r$. That combination gives the angular speed in rad/s, not an acceleration — check the units.
    B: |-
      Follows the outward "pushed into the seat" feeling and reverses the direction. The acceleration of a body moving in a circle points inwards, towards the centre.
    D: |-
      Takes acceleration to mean only a change of *speed*. A change in the direction of the velocity is just as much an acceleration.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race circuit seen from above: cars on the straights and one sweeping through a curved corner with a blue arrow showing its velocity along the tangent](scenes/motorsport/motion_plane.svg "In a long, fast corner the speedometer can sit perfectly still — and the car is still accelerating hard.")

Ananya has borrowed her cousin's phone app that plots acceleration, and she has stuck the phone flat on the passenger-side floor of a saloon car for a track-day session. Her cousin Prateek is driving.

Through the long right-hander he holds the speed dead steady — she can see the needle sitting still. But when they come in and open the app, the trace through that corner shows nearly a full $g$.

"Your app is broken," Prateek says. "I didn't touch the brake or the throttle in there. The speed never changed. Nothing accelerated."

Ananya looks at the trace, and at the arrow the app draws alongside it, pointing towards the inside of the corner. A steady speed and an acceleration as big as gravity, pointing sideways. How big is that acceleration really — and why does it point *into* the corner, when everything in her body was being pushed the other way?

## The physics

In the last lesson you saw that a body in uniform circular motion is accelerating, because its velocity keeps changing direction. That acceleration is called **centripetal acceleration**, meaning "centre-seeking".

**Direction.** Compare the velocity at two nearby instants. Both arrows have the same length $v$, but the later one has turned a little. The change $\Delta\vec{v}$ joins their heads, and it points **towards the centre** of the circle. Since $\vec{a} = \Delta\vec{v}/\Delta t$, the acceleration points to the centre too, at every instant, at right angles to the velocity.

![A circle with the velocity drawn tangent at several points and the acceleration drawn towards the centre, alongside two nearby velocity arrows tail to tail whose difference points inwards](figures/centripetal_acceleration/acceleration-towards-centre.svg "The velocity turns, so the change in velocity — and therefore the acceleration — points to the centre. The speed never changes; only the direction does.")

**Size.** The triangle made by the two velocity arrows has the same shape as the triangle made by the two radii (each has an angle $\Delta\theta$ between two equal sides), so $|\Delta\vec{v}|/v = |\Delta\vec{r}|/r$. Over a short interval $|\Delta\vec{r}| \approx v\,\Delta t$, which gives $|\Delta\vec{v}|/\Delta t = v^2/r$:

$$a_c = \frac{v^2}{r} = \omega^2 r$$

using $v = \omega r$. Here $v$ is the speed, $r$ the radius and $\omega$ the angular speed, and the unit is $\text{m/s}^2$. This is for **uniform** circular motion, at constant speed.

Both quantities matter, but not equally: $a_c$ depends on the **square** of the speed. Double the speed round the same corner and the acceleration is four times as big.

That inward acceleration has to be produced by something, and in a car it is friction from the tyres. What Prateek felt pushing him outwards was not a force on the car at all — it was his own body trying to continue in a straight line while the seat pushed him inwards round the bend.

## Worked example

**Given (illustrative):** a car holding a steady $v = 30\,\text{m/s}$ (about $108\,\text{km/h}$) round a corner of constant radius $r = 90\,\text{m}$.
**Find:** its centripetal acceleration, and how that compares with $g$.

$$a_c = \frac{v^2}{r} = \frac{30^2}{90} = \frac{900}{90} = 10\,\text{m/s}^2$$

pointing horizontally, straight at the centre of the corner.

Compared with gravity, $10/9.8 \approx 1.0$, so this is about **one $g$** sideways — as if the car had been tipped on its side and dropped. That is what the app's trace was showing, and exactly what the tyres have to supply through the whole corner.

**Sanity check (a second way):** $\omega = v/r = 30/90 = 0.33\,\text{rad/s}$, so $\omega^2 r = (0.33)^2 \times 90 \approx 10\,\text{m/s}^2$. The same answer. And notice what the square does: taken at $60\,\text{m/s}$, the same corner would demand $3600/90 = 40\,\text{m/s}^2$, about four $g$ — far more grip than ordinary road tyres can give, so the car would simply run wide.

## Where the picture breaks

A real corner is not a perfect arc of constant radius, and no driver holds a perfectly constant speed through one, so $v^2/r$ describes an idealised corner rather than a real lap. When the speed *does* change there is a second, tangential part of the acceleration along the direction of travel, and $a_c = v^2/r$ is only the inward part. Banking the corner, or pressing the car down with aerodynamic downforce, changes how much inward force the tyres can supply — but not the $v^2/r$ that the motion demands.

## Key takeaway

A body moving in a circle at constant speed has a **centripetal acceleration** $a_c = v^2/r = \omega^2 r$, always pointing towards the centre and always at right angles to the velocity. Constant speed does not mean zero acceleration. Because $v$ is squared, going twice as fast round the same corner asks four times as much of the tyres.
