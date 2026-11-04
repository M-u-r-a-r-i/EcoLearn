---
concept_id: circular_loop_field
interest: cricket
format: explain
title: Why the charging pad is so fussy
check:
  question: |-
    A circular coil has $N$ turns of radius $R$ and carries a current $I$. A second coil is wound with **twice** as many turns and **twice** the radius, and carries the same current. Compared with the first, the magnetic field at the centre of the second coil is
  options:
    A: |-
      twice as large.
    B: |-
      half as large.
    C: |-
      the same.
    D: |-
      four times smaller.
  answer: C
  explanation: |-
    At the centre, $B = \mu_0 N I/(2R)$. Doubling $N$ doubles the field and doubling $R$ halves it, so the two changes cancel exactly.
  misconceptions:
    A: |-
      Applies the doubling of $N$ but forgets that the radius doubled too. Both appear in the formula, on opposite sides of the fraction.
    B: |-
      Applies the doubling of $R$ but forgets the extra turns. Each change alone would have this size of effect; together they cancel.
    D: |-
      Uses an inverse square in $R$, carried over from the $1/r^{2}$ of a single current element. Adding up the whole loop cancels one power of $R$, leaving $B \propto 1/R$ at the centre.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground with an electric roller, a compass lying on a thick power cable, a bowling machine and a loudspeaker on a pole](scenes/cricket/moving_charges_magnetism.svg "Coils like the one in a charging pad are the same physics as the coils in the machines around this ground.")

Tejas is twelfth man, which on a hot Sunday means carrying drinks and guarding everyone's phones. His own is down to four percent, so he drops it onto the wireless charging pad someone has left plugged in by the dressing-room window.

Nothing. He nudges it. Still nothing. He slides it about, and then — a small green light. Charging.

Ten minutes later a fielder comes in, knocks the table, and the phone shifts by about the width of two fingers. The light goes out.

Tejas is unimpressed. There are no contacts to miss and no plug to line up; the phone is still flat on the pad, and it has only moved a few centimetres. Why should a couple of centimetres matter so much?

## The physics

Under that pad is a flat coil of wire. Under the back of the phone is another. Energy crosses between them through the **magnetic field** of the coil — so the question "why does a few centimetres matter?" is really the question "how does a coil's field change as you move away from it?"

Start with the field at the very centre of one circular turn of radius $R$ carrying current $I$. Use the Biot–Savart law: every element of the loop is the same distance $R$ from the centre, and every element is square-on to it ($\theta = 90°$), so all the contributions point the same way and simply add. The total length of wire is the circumference $2\pi R$, so

$$B = \frac{\mu_0}{4\pi}\cdot\frac{I\,(2\pi R)}{R^{2}} = \frac{\mu_0 I}{2R}$$

and for a coil of $N$ closely wound turns, $B = \dfrac{\mu_0 N I}{2R}$.

![On the left, a loop seen face on with the field coming out of the page at its centre; on the right, the same loop seen edge on with the field along the axis at a point P a distance x away](figures/circular_loop_field/loop-centre-and-axis.svg "At the centre the field is μ₀I/2R. Move along the axis and the denominator grows as (R² + x²) to the power 3/2 — quickly.")

**Direction:** curl the fingers of your right hand along the current around the loop; your thumb points the way $\vec{B}$ goes through it. Seen from the side the current appears anticlockwise, the field comes out at you.

Now move a distance $x$ along the **axis** of the loop. Adding up the elements again (the sideways parts cancel by symmetry, the axial parts survive):

$$B = \frac{\mu_0 N I R^{2}}{2\,(R^{2} + x^{2})^{3/2}}$$

Two checks that this is the right formula. Put $x = 0$ and it collapses back to $\mu_0NI/2R$, the centre value. Push $x$ much larger than $R$ and it falls off as $1/x^{3}$ — far faster than the $1/r^{2}$ of a point charge, because the two sides of the loop are sending their fields in nearly opposite directions and almost cancel.

Both results apply on the axis only, for a steady current in a circular loop.

## Worked example

**Given:** a charging coil of $100$ turns, radius $5.0\,\text{cm}$, carrying $0.50\,\text{A}$.
**Find:** the field at the centre of the coil, and the field one radius away along the axis.

**Step 1 — at the centre.**

$$B = \frac{\mu_0 N I}{2R} = \frac{(4\pi \times 10^{-7})(100)(0.50)}{2(0.050)} \approx 6.3 \times 10^{-4}\,\text{T}$$

Roughly ten times the Earth's magnetic field, concentrated in a coil the size of a jar lid.

**Step 2 — at $x = R = 5.0\,\text{cm}$.** Here $(R^{2} + x^{2})^{3/2} = (2R^{2})^{3/2} = 2\sqrt{2}\,R^{3}$, so the formula becomes the centre value multiplied by $1/(2\sqrt{2}) \approx 0.35$:

$$B \approx 0.35 \times 6.3 \times 10^{-4} \approx 2.2 \times 10^{-4}\,\text{T}$$

Move one coil-radius away and roughly two-thirds of the field is already gone. That is Tejas's answer: the pad is not fussy, the field simply is.

**Sanity check:** the field must be weaker off-centre and must match the centre formula at $x = 0$, and this does both.

## Where the picture breaks

A real charging coil is a flat spiral of many different radii, not one clean circle, so the formula gives the shape of the behaviour rather than an exact number for that pad.

The axis formula is also only good **on the axis**. Tejas slid his phone *sideways*, off the axis altogether, where the field is neither along the axis nor given by this expression — working it out there needs more than this chapter.

And strictly, charging needs a *changing* field, not just a strong one; the pad's current alternates, and the receiving coil responds to the change. That is electromagnetic induction, which you will meet in the next chapter. What this lesson settles is the part that matters for aiming: how fast a coil's field fades as you move away.

## Key takeaway

At the centre of a circular coil, $B = \dfrac{\mu_0 N I}{2R}$ — stronger with more turns or more current, weaker for a bigger loop. Along the axis, $B = \dfrac{\mu_0 N I R^{2}}{2(R^{2}+x^{2})^{3/2}}$, which returns the centre value at $x = 0$ and dies off as $1/x^{3}$ far away. The direction comes from curling the right hand along the current.
