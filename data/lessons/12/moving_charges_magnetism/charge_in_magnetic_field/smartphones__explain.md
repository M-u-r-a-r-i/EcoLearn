---
concept_id: charge_in_magnetic_field
interest: smartphones
format: explain
title: The red sky in a night-mode photo
check:
  question: |-
    An electron is moving in a circle at right angles to a uniform magnetic field. The field is **doubled**, and the electron's speed stays the same. What happens to the radius of its circle and to the time it takes for one full turn?
  options:
    A: |-
      The radius halves, and the time for one turn halves.
    B: |-
      The radius halves, and the time for one turn is unchanged.
    C: |-
      The radius doubles, and the time for one turn doubles.
    D: |-
      The radius halves, and the time for one turn doubles.
  answer: A
  explanation: |-
    $r = \dfrac{mv}{qB}$, so doubling $B$ halves the radius. $T = \dfrac{2\pi m}{qB}$ also has $B$ underneath, so the period halves too: the electron covers a circle half as long at the same speed.
  misconceptions:
    B: |-
      Remembers that the period does not depend on the *speed* and wrongly extends that to the field. $T = 2\pi m/(qB)$ contains $B$, so a stronger field means a quicker turn.
    C: |-
      Thinks a stronger field makes the circle bigger. A stronger field means a stronger sideways force, which bends the path more sharply — a *smaller* circle.
    D: |-
      Gets the radius right, then assumes a stronger field "holds the electron back" and slows its turning. The speed is unchanged and the circle is shorter, so each turn takes less time, not more.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk with a phone lying on a charging cable showing a swung compass arrow, a wireless charging pad with its coil exposed, a flip-cover case with a small magnet in its flap, and a speaker and a small cylinder-shaped vibration motor taken apart](scenes/smartphones/moving_charges_magnetism.svg "The phone on the cable is sensing the Earth's magnetic field. This lesson follows that same field up into the sky, where it steers particles from the Sun.")

Dorje lives in a village high in Ladakh, where the night sky is so dark that the Milky Way throws shadows. On a cold night he props his phone on a wall, switches to night mode, and takes a long exposure of the northern horizon, just to test the camera.

The photo comes back with the lower sky glowing a deep red that his eyes had barely noticed. He sends it to his cousin Pema in Delhi, who looks it up: an **aurora**, the same kind of light usually seen near the poles, visible this far south only on rare nights when the Sun has hurled out an unusually strong burst of charged particles.

Pema is puzzled. Those particles come from the Sun, which lights up the whole day side of the Earth. So why does their glow gather near the poles instead of lighting the whole sky — and what path did they take to get there?

## The physics

The answer starts with one fact: **the magnetic force on a moving charge is always perpendicular to its velocity.**

A force at right angles to the motion can turn the velocity but can never speed it up or slow it down: it does no work, so the speed stays constant. A force of constant size, always perpendicular to a constant speed, is exactly the recipe for **uniform circular motion**.

![On the left, a positive charge entering a field into the page moves in a circle with the magnetic force always pointing to the centre; on the right, a velocity with a component along the field gives a helix](figures/charge_in_magnetic_field/circular-and-helical-paths.svg "Velocity across the field turns into a circle. Velocity along the field is left alone. Together they make a helix — a coiled path that follows the field line.")

When $\vec{v}$ is perpendicular to $\vec{B}$, the magnetic force $qvB$ provides the centripetal force $mv^2/r$:

$$qvB = \frac{mv^{2}}{r} \qquad\Longrightarrow\qquad r = \frac{mv}{qB}$$

The time for one turn is the circumference divided by the speed:

$$T = \frac{2\pi r}{v} = \frac{2\pi m}{qB}$$

The speed cancels. **Every particle of the same kind, in the same field, takes the same time per turn**, however fast it goes. A faster particle simply runs round a bigger circle.

If the velocity has a component **along** the field as well, split it. The part along $\vec{B}$ feels no force and carries on unchanged; the part across $\vec{B}$, $v_\perp$, goes round in a circle of radius $mv_\perp/(qB)$. Together they make a **helix** — a spring-shaped path wound around a field line, advancing a distance $p = v_\parallel T$ (the **pitch**) each turn.

That is Pema's answer. Charged particles arriving near the Earth get wound onto its magnetic field lines and corkscrew along them. Those field lines dive down into the atmosphere near the magnetic poles — so that is where the particles arrive, and where the air glows.

## Worked example

**Given:** an electron corkscrewing down a field line, with the part of its velocity across the field $v_\perp = 1.0\times10^{7}\,\text{m/s}$ (illustrative). Take the Earth's field there as $B = 5.0\times10^{-5}\,\text{T}$. For an electron, $m = 9.1\times10^{-31}\,\text{kg}$, $q = 1.6\times10^{-19}\,\text{C}$.
**Find:** the radius of its helix and the time for one turn.

**Step 1 — the radius.**

$$r = \frac{mv_\perp}{qB} = \frac{(9.1\times10^{-31})(1.0\times10^{7})}{(1.6\times10^{-19})(5.0\times10^{-5})} = \frac{9.1\times10^{-24}}{8.0\times10^{-24}} \approx 1.1\,\text{m}$$

The electron's corkscrew is only about a metre across — about the width of a doorway — wound around a field line thousands of kilometres long.

**Step 2 — the time for one turn.**

$$T = \frac{2\pi m}{qB} = \frac{2\pi(9.1\times10^{-31})}{8.0\times10^{-24}} \approx 7.1\times10^{-7}\,\text{s}$$

Less than a millionth of a second. During a three-second night-mode exposure, such an electron would go round about four million times.

**Sanity check:** the Earth's field is very weak, so the circles should be fairly loose for such a fast particle — a metre, not a micrometre, fits that.

## Where the picture breaks

The formulas assume a **uniform** field. The Earth's field is not: it gets stronger closer to the poles, and that squeezes the helix tighter as the particle goes down. Some particles are even turned back by it, which the simple circle does not describe.

The particles also do not reach the ground. They collide with gas high in the atmosphere, hundreds of kilometres up, and give up their energy; the red colour comes from oxygen atoms up there. Dorje's phone photographed the light from those collisions, not the particles.

And an aurora as far south as Ladakh needs an unusually strong solar storm. On a normal night the glow stays near the poles — where the field lines bring the particles down.

## Key takeaway

A charge moving at right angles to a uniform magnetic field moves in a circle of radius $r = \dfrac{mv}{qB}$ at constant speed, because the magnetic force is always perpendicular to its motion and does no work. The time for one turn, $T = \dfrac{2\pi m}{qB}$, does not depend on the speed. Any velocity along the field is untouched, turning the circle into a helix that follows the field line.
