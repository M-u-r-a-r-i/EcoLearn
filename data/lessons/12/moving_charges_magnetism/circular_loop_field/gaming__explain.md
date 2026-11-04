---
concept_id: circular_loop_field
interest: gaming
format: explain
title: The hidden coil under the escape-room table
check:
  question: |-
    A flat circular coil of $N$ turns and radius $R$ carries a steady current $I$. Which change, on its own, would **double** the magnetic field at the centre of the coil without changing the current?
  options:
    A: |-
      Doubling the number of turns.
    B: |-
      Doubling the radius of the coil.
    C: |-
      Doubling the number of turns and the radius together.
    D: |-
      Halving the number of turns and halving the radius.
  answer: A
  explanation: |-
    At the centre, $B = \dfrac{\mu_0 N I}{2R}$. The field is directly proportional to $N$, so twice the turns gives twice the field — every extra turn adds its own contribution in the same direction.
  misconceptions:
    B: |-
      Assumes a bigger coil must make a bigger field. $R$ sits in the denominator: widening the loop moves every part of the wire further from the centre, and the field *halves*.
    C: |-
      Gets the effect of the turns right but changes the radius at the same time. Doubling $N$ doubles $B$, doubling $R$ halves it, and the two cancel exactly.
    D: |-
      Notices correctly that halving the radius doubles the field, and forgets that halving the turns halves it again. Both factors have to be counted.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming workbench with a bartop arcade cabinet, a cutaway of a pinball flipper coil, a controller with its shell off, a PC case fan, and a phone on a power cable showing a swung compass needle](scenes/gaming/moving_charges_magnetism.svg "A coil of wire with current in it is a magnet you can switch — which is why it turns up in a pinball flipper, a fan and, in this story, a puzzle.")

The game-dev club's stall at the college fest is a physical escape room, and Nidhi built the puzzle everyone talks about. A compass sits on a small plinth in the middle of a table. Press the correct button and the needle swings round to a new heading; the number it lands on is the code for the next lock.

Under the table, out of sight, is a flat coil she wound herself around a jam jar — twenty turns of wire, taped down, fed from a cell through the button.

It works perfectly in testing, with the compass sitting right above the middle of the coil. On the first morning of the fest a volunteer swaps the plinth for a taller one so the crowd can see the dial, lifting the compass five centimetres — and every player starts getting the wrong code. The needle still swings. It just swings to a different number.

Five centimetres. How quickly does a coil's field fade as you move off it?

## The physics

Start at the easiest point: the **centre** of a single loop of radius $R$ carrying current $I$. Biot–Savart is unusually kind there. Every element of the wire is the same distance $R$ from the centre; every element is at right angles to the line joining it to the centre, so $\sin\theta = 1$; and by symmetry every element's $d\vec{B}$ points the same way, straight along the axis. So you can simply add the lengths:

$$B = \frac{\mu_0}{4\pi}\frac{I}{R^{2}}\times(2\pi R) = \frac{\mu_0 I}{2R} \qquad\text{and for } N \text{ turns}\qquad B = \frac{\mu_0 N I}{2R}$$

![On the left, a circular current loop seen face on, with the field at its centre along the axis; on the right, the same loop seen edge on with the field at a point on the axis](figures/circular_loop_field/loop-centre-and-axis.svg "At the centre every element pushes the same way. Move along the axis and the contributions start to tilt, so only part of each one survives.")

Which face is the north pole? Curl the fingers of your **right hand** the way the current runs round the loop; your thumb points the way $\vec{B}$ leaves the coil along the axis.

Now step off the centre, along the axis, a distance $x$. Each element still contributes the same amount, but the contributions now tilt outwards; the sideways parts cancel in pairs around the ring and only the axial parts survive. Adding those up gives

$$B = \frac{\mu_0 N I R^{2}}{2\left(R^{2}+x^{2}\right)^{3/2}}$$

Two checks on that formula. Put $x = 0$ and it collapses to $\mu_0 N I/(2R)$, as it must. Go far away, $x \gg R$, and it becomes $B \approx \mu_0 N I R^{2}/(2x^{3})$ — the field of a coil dies as $1/x^{3}$, much faster than the $1/r^{2}$ of a single element or the $1/r$ of a long wire you will meet next.

It is that cube that ruined Nidhi's puzzle. This expression holds **on the axis only**, for a flat, tightly wound coil carrying a steady current.

## Worked example

**Given:** Nidhi's coil has $N = 20$ turns of radius $R = 5.0\,\text{cm} = 0.050\,\text{m}$ and carries $I = 0.40\,\text{A}$.
**Find:** the field at the centre, and the field on the axis $5.0\,\text{cm}$ away — the height the taller plinth added.

**Step 1 — at the centre.**

$$B = \frac{\mu_0 N I}{2R} = \frac{(4\pi\times10^{-7})(20)(0.40)}{2(0.050)} = \frac{1.0\times10^{-5}}{0.10} = 1.0\times10^{-4}\,\text{T}$$

That is $100\,\text{microtesla}$ — roughly twice the Earth's own field, so on the plinth the needle was mostly obeying the coil.

**Step 2 — on the axis, at $x = R$.** When $x$ equals $R$, the bracket becomes $(2R^{2})^{3/2} = 2\sqrt{2}\,R^{3}$, so the field is just the centre value divided by $2\sqrt{2} \approx 2.8$:

$$B = \frac{1.0\times10^{-4}}{2.8} \approx 3.6\times10^{-5}\,\text{T}$$

**Step 3 — what the compass now sees.** The coil's field has dropped to about a third, to roughly the size of the Earth's field instead of double it. The needle is no longer being dominated by the coil; it settles part-way between the two — at a different number on the dial.

**Sanity check:** one coil radius off the centre and the field is already down by two-thirds. A coil is a strong magnet in the middle of itself and a weak one anywhere else, which is exactly why Nidhi's puzzle was so fussy about height.

## Where the picture breaks

The axis formula is for the **axis**. The volunteer happened to lift the compass straight up, which is the one direction the formula covers. Had the plinth been slid sideways instead, the field there would not even point along the axis, and no tidy expression describes it — off-axis fields are worked out numerically.

A hand-wound coil is also not $N$ identical circles stacked in one plane. The turns sit at slightly different radii and spread along a short length. Treating them as $N$ coplanar loops of radius $R$ is a good approximation only while the winding is small compared with $R$ — which is why a jam jar and neat taping matter more than they look.

And the compass reads the **sum** of the coil's field and the Earth's, so the heading depends on which way the table faces as well as on the current. Reverse the cell and the needle swings the other way entirely: the same coil, with its north face now pointing down.

## Key takeaway

At the centre of a flat coil of $N$ turns, $B = \dfrac{\mu_0 N I}{2R}$, pointing along the axis — right-hand fingers along the current, thumb along $\vec{B}$. On the axis at distance $x$ the field is $\dfrac{\mu_0 N I R^{2}}{2(R^{2}+x^{2})^{3/2}}$, which falls away as $1/x^{3}$ once you are well clear of the coil.
