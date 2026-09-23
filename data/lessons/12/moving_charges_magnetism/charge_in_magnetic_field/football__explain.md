---
concept_id: charge_in_magnetic_field
interest: football
format: explain
title: How a sample bottle gives a molecule away
check:
  question: |-
    Two singly charged ions are fired into the same uniform magnetic field at the same speed, at right angles to the field. One ion is twice as heavy as the other. Compared with the lighter ion, the heavier one moves on a circle with
  options:
    A: |-
      twice the radius, and takes twice as long to go round.
    B: |-
      twice the radius, but takes the same time to go round.
    C: |-
      half the radius, and takes half as long to go round.
    D: |-
      twice the radius, but takes half as long to go round.
  answer: A
  explanation: |-
    With $q$, $v$ and $B$ fixed, $r = mv/(qB)$ is proportional to $m$, and so is the period $T = 2\pi m/(qB)$. Doubling the mass doubles both.
  misconceptions:
    B: |-
      Remembers correctly that the period does not depend on the *speed*, and over-generalises it to "the period never changes". It does not depend on $v$, but it is directly proportional to $m$.
    C: |-
      Puts the mass in the denominator, thinking a heavier particle is harder to move and so must be held in a tighter circle. Heavier means harder to *turn*, so the circle is wider.
    D: |-
      Thinks a bigger circle must be covered faster, or confuses the period with the frequency. The heavier ion travels at the same speed around a longer path, so it takes longer.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground with a coil traced around the goal frame, a pop-up sprinkler on a solenoid valve, an electric line-marking machine and a horn speaker on a pole with a compass lying on its supply cable](scenes/football/moving_charges_magnetism.svg "The same physics that runs the machines on this ground also runs the laboratory that tests the players on it.")

Arjun's team has just lost a state semi-final, and the last thing he expected was to be handed a numbered envelope on the way off the pitch. Two players from each side, chosen at random, report to doping control.

He sits in a small room with a bottle of water and a chaperone who will not leave him alone even for a minute, and asks the obvious question: what can anyone actually tell from this?

Everything, the doctor says. That sample goes to a laboratory where a machine can pick out a single banned molecule mixed into it — not "something suspicious", but which molecule, by name, at a few parts in a billion.

Arjun tries to imagine any sieve fine enough to do that. Nothing in a chemistry lab sorts things by molecule. So how do you sort a liquid into the substances it was made of?

## The physics

You do it by making the molecules into ions, firing them into a magnetic field, and letting the field sort them.

A charge moving *across* a magnetic field feels a force $F = qvB$ at right angles to its motion. A force that is always perpendicular to the velocity never changes the speed — it only turns the charge, constantly, by the same amount. That is the definition of **uniform circular motion**, and the magnetic force is the centripetal force:

$$qvB = \frac{mv^{2}}{r} \qquad \Longrightarrow \qquad r = \frac{mv}{qB}$$

![On the left, a positive charge in a field into the page following a circle with the force always pointing to the centre; on the right, a charge entering at an angle to B and spiralling along it in a helix](figures/charge_in_magnetic_field/circular-and-helical-paths.svg "Velocity across the field makes the circle; velocity along the field is untouched, which turns the circle into a helix.")

The radius grows with momentum $mv$ and shrinks with the field: a heavy ion sweeps a wide arc, a light one a tight arc, and **that difference in radius is the sorting**. Fire ions of one speed into the field, put a detector at a fixed place, and only one mass lands on it.

Now go once round the circle. The time taken is the circumference divided by the speed:

$$T = \frac{2\pi r}{v} = \frac{2\pi m}{qB}$$

Look at what has dropped out: $v$ has cancelled. **The time for one turn does not depend on how fast the particle is going**, or on how big its circle is — only on $m$, $q$ and $B$. A faster ion takes a wider circle at exactly the rate that keeps the lap time the same. The next lesson, on the cyclotron, is built entirely on that fact.

One condition matters: all of this assumes $\vec{v}$ is **perpendicular** to $\vec{B}$. If the ion enters at an angle, split its velocity in two. The part across $\vec{B}$ still makes a circle; the part along $\vec{B}$ feels no force at all and carries on unchanged. A circle plus a steady drift along the axis is a **helix**, like the thread of a screw, and the distance it advances in one turn is called the pitch.

## Worked example

**Given:** a singly charged fragment of mass $2.0 \times 10^{-25}\,\text{kg}$ ($q = 1.6 \times 10^{-19}\,\text{C}$) enters a field of $0.50\,\text{T}$ at $2.0 \times 10^{5}\,\text{m/s}$, at right angles to the field.
**Find:** the radius of its path, and how a molecule twice as heavy would be separated from it.

**Step 1 — the radius.**

$$r = \frac{mv}{qB} = \frac{(2.0 \times 10^{-25})(2.0 \times 10^{5})}{(1.6 \times 10^{-19})(0.50)} = \frac{4.0 \times 10^{-20}}{8.0 \times 10^{-20}} = 0.50\,\text{m}$$

Half a metre. The ion turns through a half-circle about a metre across — the size of a small table, which is roughly the size of the real instrument.

**Step 2 — the heavier molecule.** Same charge, same speed, same field, but $m$ doubled: $r$ doubles to $1.0\,\text{m}$. The two ions land half a metre apart.

**Sanity check:** half a metre of separation is something you could measure with a ruler, which is why an instrument this size can tell two molecules apart at all.

## Where the picture breaks

The machine does not weigh a molecule. It sorts by $r = mv/(qB)$, which fixes the **charge-to-mass ratio**, not the mass: a doubly charged ion of twice the mass bends on exactly the same circle. Real instruments get around that by also fixing the speed of the ions before they enter the field, and by breaking each molecule into a pattern of fragments that acts like a fingerprint.

Two idealisations hide in the calculation. The field is treated as perfectly uniform over the whole path, which is only true near the middle of the magnet; and the ion must travel in a good vacuum, because one collision with an air molecule ends the neat circle.

## Key takeaway

A charge moving across a magnetic field goes in a circle of radius $r = \dfrac{mv}{qB}$, because the magnetic force is always perpendicular to the velocity. The period $T = \dfrac{2\pi m}{qB}$ is independent of the speed and of the radius. Add a velocity component along $\vec{B}$, which feels no force, and the circle stretches into a helix.
