---
concept_id: charge_in_magnetic_field
interest: cricket
format: explain
title: Why the canteen microwave has magnets in it
check:
  question: |-
    A charged particle is moving in a circle in a uniform magnetic field. It is then sent in again at **twice** the speed, into the same field, still at right angles to it. What happens to the radius of its path and to the time it takes to go once round?
  options:
    A: |-
      The radius doubles and the time for one turn doubles.
    B: |-
      The radius stays the same and the time for one turn halves.
    C: |-
      The radius doubles and the time for one turn is unchanged.
    D: |-
      The radius becomes four times bigger and the time for one turn is unchanged.
  answer: C
  explanation: |-
    $r = mv/(qB)$ is proportional to $v$, so the radius doubles; but $T = 2\pi m/(qB)$ contains no $v$ at all, so the particle goes twice as fast around a circle twice as big and takes exactly the same time.
  misconceptions:
    A: |-
      Assumes a bigger circle must take longer. The circumference doubles, but so does the speed, and the two changes cancel exactly.
    B: |-
      Thinks the field alone fixes the size of the circle. The field fixes the *period*; the radius depends on the particle's momentum $mv$.
    D: |-
      Carries over a $v^2$ from $F = mv^2/r$ and forgets that the magnetic force $qvB$ grows with $v$ as well. One power of $v$ cancels, leaving $r \propto v$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground with an electric roller, a compass lying on a thick power cable, a bowling machine and a loudspeaker on a pole](scenes/cricket/moving_charges_magnetism.svg "Machines all over a ground rely on magnetic fields steering moving charges.")

The tea interval, and the canteen microwave gives up halfway through a tray of samosas. Nothing. No hum, no light.

Imran, who is meant to be padding up, watches the club electrician unscrew the case on the back steps. Out come the usual things — a fan, a transformer, a fuse — and then something Imran was not expecting: a squat metal cylinder with two heavy black rings clamped around it. Ring magnets, strong enough to snap onto the spanner from a hand's width away.

"That's the magnetron," the electrician says. "It's what makes the waves."

Imran turns it over. A microwave oven cooks with electricity. There is no moving part in this cylinder at all. So why on earth does it need a pair of magnets?

## The physics

Inside that cylinder, electrons boil off a hot wire down the middle and head outwards. The magnets fill the space with a magnetic field, and a field does one thing to a moving charge: it pushes it **sideways**, with a force $F = qvB$ that is always perpendicular to the velocity.

A sideways push of constant size, always at right angles to the motion, is exactly the recipe for **uniform circular motion**. The magnetic force becomes the centripetal force:

$$qvB = \frac{mv^{2}}{r}$$

Cancel one $v$ and rearrange:

$$r = \frac{mv}{qB}$$

The radius grows with the particle's momentum and shrinks as the field gets stronger. Now the time for one full turn, from $v = 2\pi r / T$:

$$T = \frac{2\pi m}{qB} \qquad\text{and}\qquad f = \frac{qB}{2\pi m}$$

![On the left, a positive charge in a field into the page following a circle with the force always pointing to the centre; on the right, a charge entering at an angle to B and spiralling along it in a helix](figures/charge_in_magnetic_field/circular-and-helical-paths.svg "Velocity across the field makes the circle; velocity along the field is untouched, and turns the circle into a helix.")

Look hard at that period. **There is no $v$ and no $r$ in it.** A fast particle takes a big circle, a slow one a small circle, and both come round in the same time. That is the fact the magnetron is built on: the electrons circle at a steady rate, and that rate sets the frequency of the microwaves the oven cooks with.

What if the charge does not enter at right angles? Split the velocity into a part **across** $\vec{B}$, which makes the circle, and a part **along** $\vec{B}$, which feels no force at all and just carries on. Together they give a **helix** — a circle drifting steadily along the field lines, like the spring in a ballpoint pen.

All of this assumes the field is uniform and the only force acting is the magnetic one, with the speed well below the speed of light.

## Worked example

**Given:** in a school demonstration tube, electrons move at $2.0 \times 10^{6}\,\text{m/s}$ straight across a uniform field of $1.0 \times 10^{-4}\,\text{T}$.
**Find:** the radius of the circle, and the time for one turn.

**Step 1 — the radius.**

$$r = \frac{mv}{qB} = \frac{(9.1 \times 10^{-31})(2.0 \times 10^{6})}{(1.6 \times 10^{-19})(1.0 \times 10^{-4})} = \frac{1.82 \times 10^{-24}}{1.6 \times 10^{-23}} \approx 0.11\,\text{m}$$

So the electrons loop round a circle about $11\,\text{cm}$ across the radius — roughly the width of your palm, and easy to see glowing in a darkened lab.

**Step 2 — the time for one turn.**

$$T = \frac{2\pi m}{qB} = \frac{2\pi \times 9.1 \times 10^{-31}}{1.6 \times 10^{-23}} \approx 3.6 \times 10^{-7}\,\text{s}$$

That is about a third of a microsecond — roughly three million laps every second.

**Sanity check:** the same period comes out of $T = 2\pi r/v$ with the radius from Step 1, which is the reassurance that the two answers belong to the same circle.

## Where the picture breaks

The magnetron is a much harsher place than a clean circle in a uniform field. Its magnets give something like a thousand times the field used above, so the electrons curve in a fraction of a millimetre; and there is a strong electric field pulling them outwards at the same time, so the real paths are looping curves, not circles. You will not be asked for those.

The clean result also assumes nothing else acts on the charge — no gravity worth mentioning (it is utterly swamped here), no collisions, and speeds far below light speed. Push a particle close to light speed and $T$ stops being constant, which is a problem the next lesson runs straight into.

## Key takeaway

In a uniform magnetic field, a charge moving across the field goes in a circle of radius $r = mv/(qB)$, because the magnetic force is always perpendicular to the velocity. The period $T = 2\pi m/(qB)$ does **not** depend on the speed or the radius. Any velocity along the field survives untouched, turning the circle into a helix.
