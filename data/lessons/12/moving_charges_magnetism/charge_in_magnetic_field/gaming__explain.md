---
concept_id: charge_in_magnetic_field
interest: gaming
format: explain
title: The glowing ring in the glass bulb
check:
  question: |-
    An electron beam crosses a uniform magnetic field at right angles and travels in a circle. The beam's speed is then **doubled**, with the same field. What happens to the radius of the circle and to the time taken for one full turn?
  options:
    A: |-
      The radius doubles; the time for one turn is unchanged.
    B: |-
      The radius doubles and the time for one turn doubles too.
    C: |-
      The radius doubles; the time for one turn is halved.
    D: |-
      The radius is unchanged; the time for one turn is halved.
  answer: A
  explanation: |-
    $r = \dfrac{mv}{qB}$ is proportional to $v$, so the circle doubles in size. But $T = \dfrac{2\pi m}{qB}$ contains no $v$ at all: the path is twice as long and the electron covers it twice as fast, so the turn takes exactly as long as before.
  misconceptions:
    B: |-
      Assumes a bigger circle must take longer. The circumference does double — but so does the speed, and the two changes cancel exactly.
    C: |-
      Gets the radius right, then applies "faster means quicker" to the period. The path grows in step with the speed, so the time for a turn does not change.
    D: |-
      Swaps the two results. It is the *period* that does not depend on the speed; the radius is directly proportional to it.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming workbench with a bartop arcade cabinet, a cutaway of a pinball flipper coil, a controller with its shell off, a PC case fan, and a phone on a power cable showing a swung compass needle](scenes/gaming/moving_charges_magnetism.svg "The arcade cabinet's CRT paints its picture by steering a beam of electrons with magnetic fields. This lesson is about what such a beam does when you simply let it run.")

Tanvi's team has spent a week arguing about a projectile. In their game a bolt of charged plasma is meant to bend as it crosses a magnetic zone, and nobody can agree what the bend should look like. A banana? A spiral? A full circle?

On a college trip to a science centre she finds the argument settled by a glass bulb in a dark corner. Inside it a beam of electrons traces a glowing ring — thin, bright and perfectly closed, hanging in mid-air with nothing holding it.

The demonstrator turns one knob and the ring shrinks to half the size. He turns another and it grows again. Then he tilts the little electron gun, and the ring opens out into a stretched spring winding away down the bulb.

Tanvi photographs all three. A circle, a smaller circle, a coil — same beam, same bulb. What decides which one you get?

## The physics

Start from the force on a moving charge, $F = qvB\sin\theta$, and add the one fact that makes everything here work: **the magnetic force is always perpendicular to the velocity.**

A force at right angles to the motion can never speed a particle up or slow it down — it does no work, so the kinetic energy and the speed stay exactly as they were. All it can do is turn the velocity. A constant-sized force that is always perpendicular to a constant speed is precisely the recipe for **uniform circular motion**.

![On the left, a positive charge entering a field into the page moves in a circle with the magnetic force always pointing to the centre; on the right, a velocity with a component along the field gives a helix](figures/charge_in_magnetic_field/circular-and-helical-paths.svg "Velocity across the field bends into a circle. Any velocity along the field is untouched — and together they make a helix.")

With $\vec{v}$ perpendicular to $\vec{B}$, the magnetic force supplies the centripetal force:

$$qvB = \frac{mv^{2}}{r} \qquad\Longrightarrow\qquad r = \frac{mv}{qB}$$

Faster particles take wider circles; a stronger field pulls them tighter. Now the time for one turn:

$$T = \frac{2\pi r}{v} = \frac{2\pi m}{qB} \qquad\text{and}\qquad f = \frac{qB}{2\pi m}$$

**The period does not depend on the speed or on the radius.** A slow electron takes a small circle, a fast one a big circle, and both come back round in the same time. Everything in $T$ is fixed by the particle and the field.

And if the velocity is *not* perpendicular to $\vec{B}$? Split it in two. The part along $\vec{B}$ feels no force at all and simply carries on at constant speed. The part across $\vec{B}$ circles as before. Together they give a **helix**, of radius $r = mv_\perp/(qB)$ and pitch (one turn's advance) $p = v_\parallel T$. That is Tanvi's stretched spring — the demonstrator tilted the gun and gave the beam a velocity component along the field.

All of this assumes a **uniform** field, no other forces worth counting, and speeds well below the speed of light.

## Worked example

**Given:** electrons in the bulb travelling at $7.0\times10^{6}\,\text{m/s}$, at right angles to a uniform field of $2.0\,\text{mT} = 2.0\times10^{-3}\,\text{T}$. For an electron, $m = 9.1\times10^{-31}\,\text{kg}$ and $q = 1.6\times10^{-19}\,\text{C}$.
**Find:** the radius of the ring and the time for one turn.

**Step 1 — the radius.**

$$r = \frac{mv}{qB} = \frac{(9.1\times10^{-31})(7.0\times10^{6})}{(1.6\times10^{-19})(2.0\times10^{-3})} = \frac{6.4\times10^{-24}}{3.2\times10^{-22}} = 0.020\,\text{m}$$

Two centimetres across the radius — a ring about the size of a bottle cap, which is exactly the sort of glowing circle you can see from across a room.

**Step 2 — the period.**

$$T = \frac{2\pi m}{qB} = \frac{2\pi(9.1\times10^{-31})}{3.2\times10^{-22}} = 1.8\times10^{-8}\,\text{s}$$

About $18$ nanoseconds per lap.

**Step 3 — put that in something you can picture.** A game running at 60 frames per second holds each frame for about $16.7\,\text{ms}$. In one frame, this electron goes round its little ring roughly **nine hundred thousand times**.

**Sanity check:** a couple of centimetres is a size you can see, and a speed of millions of metres per second has to give a laughably short period — the two answers belong together.

## Where the picture breaks

The ring is visible only because the bulb holds a trace of gas that the beam makes glow. In a proper vacuum the same circle would be there and completely invisible. That gas also nibbles energy from the electrons, so the "circle" is really a very slow inward spiral — beautiful, and not quite what the formula describes.

The field is uniform only near the middle of the apparatus, between its two coils. Push the beam out towards the glass and the field weakens, the radius stretches, and the path stops closing neatly.

The formula also assumes the electron is nowhere near light speed. At $7\times10^{6}\,\text{m/s}$ — about 2% of it — that is safe. Wind the gun up far enough and the turns start taking longer than $2\pi m/(qB)$ says, which is a problem the next lesson has to design around.

And for Tanvi's game: a magnetic field bends a charged bolt without ever changing its speed. If the projectile on screen is speeding up as it curls inwards, whatever is doing that is not magnetism.

## Key takeaway

A charge moving across a uniform magnetic field goes in a circle of radius $r = \dfrac{mv}{qB}$, at constant speed, because the magnetic force is always perpendicular to the motion and so does no work. The time for a turn, $T = \dfrac{2\pi m}{qB}$, is the same however fast it goes. Any velocity **along** the field is left untouched, turning the circle into a helix.
