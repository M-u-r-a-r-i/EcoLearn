---
concept_id: centripetal_acceleration
interest: gaming
format: explain
title: The slow hairpin that kept spinning cars out
check:
  question: |-
    In a racing game, a kart takes a circular bend of radius $50\,\text{m}$ at a steady $20\,\text{m/s}$. What is its acceleration?
  options:
    A: |-
      $8.0\,\text{m/s}^2$, towards the centre of the bend
    B: |-
      $0.40\,\text{m/s}^2$, towards the centre of the bend
    C: |-
      $8.0\,\text{m/s}^2$, outwards from the centre of the bend
    D: |-
      $0\,\text{m/s}^2$, because the speed is steady
  answer: A
  explanation: |-
    $a_c = \dfrac{v^2}{r} = \dfrac{20^2}{50} = \dfrac{400}{50} = 8.0\,\text{m/s}^2$. The velocity turns towards the inside of the bend, so the change in velocity, and the acceleration, points towards the centre.
  misconceptions:
    B: |-
      Uses $v/r$ instead of $v^2/r$. The units give it away: $v/r$ has units of $\text{s}^{-1}$, not $\text{m/s}^2$.
    C: |-
      Believes in an outward "centrifugal" acceleration because the driver feels thrown outwards. Seen from the ground, the kart's acceleration points inwards, towards the centre.
    D: |-
      Thinks constant speed means zero acceleration. In a bend the direction of the velocity changes, and that change is an acceleration.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: the monitor shows an artillery game; a tablet shows a top-down minimap of a circular kart track, with the kart's velocity along the track and its acceleration pointing to the centre](scenes/gaming/motion_plane.svg "On the minimap, the green acceleration arrow points to the centre of the circle. How long should that arrow be?")

Aarav is building a racing game with his cousin Meera, and they have written a simple grip rule: if a car's sideways acceleration in a bend goes over a set limit, the tyres lose grip and the car spins out.

Playtesting reveals something strange. The fast, sweeping bend at the end of the long straight, taken flat out, never causes a spin. But the tight hairpin by the harbour, taken at less than half that speed, spins out almost everyone.

"The grip code must be inverted," says Aarav. "Faster should be harder, not easier."

Meera isn't so sure. The hairpin is tiny and the sweeper is huge. Maybe the size of the circle matters as much as the speed.

Both bends are taken at a steady speed. So what exactly is the acceleration of a car in a bend, and how does it depend on the speed and on the radius?

## The physics

In uniform circular motion the velocity keeps turning, so there is an acceleration. Its direction is always **towards the centre** of the circle, which is why it is called **centripetal** ("centre-seeking") acceleration. Its size is

$$a_c = \frac{v^2}{r}$$

where $v$ is the speed and $r$ the radius. Using $v = \omega r$, the same result can be written $a_c = \omega^2 r$.

**Why $v^2/r$?** In a short time $\Delta t$ the object moves through a small angle $\Delta\theta$. Its position vector turns through $\Delta\theta$, and so does its velocity, which stays at right angles to it. The two triangles, one of position vectors and one of velocity vectors, are similar, so $\dfrac{|\Delta\vec{v}|}{v} = \dfrac{|\Delta\vec{r}|}{r}$. For a small angle $|\Delta\vec{r}| \approx v\,\Delta t$, which gives $|\Delta\vec{v}| \approx \dfrac{v^2}{r}\Delta t$. Dividing by $\Delta t$ gives $a_c = v^2/r$. As $\Delta t \to 0$, $\Delta\vec{v}$ points exactly at the centre.

![Left: a circle with three points, each showing a tangent velocity arrow and an acceleration arrow pointing to the centre. Right: velocity vectors at two nearby moments drawn tail to tail, with the change in velocity pointing inwards](figures/centripetal_acceleration/acceleration-towards-centre.svg "The velocity turns, so the change in velocity, and so the acceleration, points to the centre. The speed never changes, only the direction.")

Two things follow. The acceleration grows with the **square** of the speed: double $v$ and $a_c$ goes up four times. And it grows as the radius **shrinks**: a tight bend needs more acceleration than a wide one at the same speed. That is Meera's point, and it settles the argument.

## Worked example

**Given (illustrative):** the hairpin has radius $15\,\text{m}$, taken at $12\,\text{m/s}$; the sweeper has radius $120\,\text{m}$, taken at $30\,\text{m/s}$. The game's grip limit is $9.0\,\text{m/s}^2$.
**Find:** the centripetal acceleration in each bend, and the fastest safe speed through the hairpin.

Hairpin:
$$a_c = \frac{v^2}{r} = \frac{12^2}{15} = \frac{144}{15} = 9.6\,\text{m/s}^2 \quad (\text{over the limit: spin})$$

Sweeper:
$$a_c = \frac{30^2}{120} = \frac{900}{120} = 7.5\,\text{m/s}^2 \quad (\text{under the limit: safe})$$

The grip code isn't inverted. The hairpin's radius is 8 times smaller, which outweighs a speed that is only 2.5 times lower ($2.5^2 = 6.25$, less than $8$).

Fastest safe hairpin speed: set $a_c$ equal to the limit, $v^2 = a_c r$:
$$v_{\max} = \sqrt{9.0 \times 15} = \sqrt{135} \approx 11.6\,\text{m/s}$$

**Sanity check:** units: $(\text{m/s})^2/\text{m} = \text{m/s}^2$. $11.6\,\text{m/s}$ is just below the $12\,\text{m/s}$ that spun out, so a small lift of the throttle is enough, which matches what the playtesters found.

## Where the picture breaks

A real car's grip limit isn't one fixed number: it depends on the tyres, the road surface, the car's weight and any downforce, and the tyres slide gradually rather than all at once. Real racing lines aren't perfect circles either; drivers widen the bend to increase $r$ and so reduce $a_c$. The driver *feels* pushed outwards, but that is their body trying to carry on in a straight line, not an outward acceleration. Seen from the ground, the acceleration always points in. The force that provides it, friction from the tyres, belongs to the laws of motion.

## Key takeaway

An object moving in a circle of radius $r$ at constant speed $v$ has a **centripetal acceleration** $a_c = v^2/r = \omega^2 r$, directed towards the centre. It grows with the square of the speed and gets larger as the circle gets tighter, which is why a slow hairpin can demand more grip than a fast, wide bend.
