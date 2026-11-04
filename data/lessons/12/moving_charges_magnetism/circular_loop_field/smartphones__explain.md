---
concept_id: circular_loop_field
interest: smartphones
format: explain
title: Why a thick case can stop wireless charging
check:
  question: |-
    A flat circular coil in a charging pad carries a current $I$ and produces a field $B_0$ at its centre. It is replaced by a coil with **twice as many turns** and **twice the radius**, carrying the **same** current. What is the field at the centre of the new coil?
  options:
    A: |-
      $2B_0$
    B: |-
      $B_0/4$
    C: |-
      $B_0/2$
    D: |-
      $B_0$, unchanged
  answer: D
  explanation: |-
    At the centre, $B = \dfrac{\mu_0 N I}{2R}$. Doubling $N$ doubles $B$; doubling $R$ halves it. The two effects cancel, so the field is still $B_0$.
  misconceptions:
    A: |-
      Counts the extra turns but forgets that a bigger loop puts every bit of wire further from the centre. The field at the centre is proportional to $N/R$, not to $N$ alone.
    B: |-
      Treats the centre field as falling off as $1/R^{2}$, like the field of a single current element, and then forgets the extra turns. For the whole loop, the centre field is proportional to $1/R$, and the doubled turns cancel that.
    C: |-
      Accounts for the larger radius but ignores the doubled number of turns. Each turn adds its own field at the centre, so twice the turns gives twice the field.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk with a phone lying on a charging cable showing a swung compass arrow, a wireless charging pad with its coil exposed, a flip-cover case with a small magnet in its flap, and a speaker and a small cylinder-shaped vibration motor taken apart](scenes/smartphones/moving_charges_magnetism.svg "In the middle of the desk: a wireless charging pad with its cover off. Under the plastic is a flat coil of copper wire — a stack of circular loops.")

Neha's wireless charging pad worked perfectly for a year. Then she bought a thick, rugged case for her phone, and the pad stopped working. Put the phone down, and the charging symbol flickers and disappears. Take the case off, and it charges happily again.

Her brother Vikram opens up an old broken pad to see what's inside. There's no clever electronics under the top cover — mostly a flat spiral of thick copper wire, about four centimetres across, sitting on a black magnetic sheet. A matching flat coil, he knows, is glued inside the back of the phone.

The case, with its padded back and built-in stand, lifts the phone by barely two centimetres. Vikram's first guess is that the field from the pad's coil drops only a little over so short a gap, the way a torch beam dims gradually. But the charger gives up completely.

How fast does the field of a coil really fade as you move away from it along its middle?

## The physics

A circular loop of wire is the simplest shape that makes a strong, well-aimed field. Use the Biot–Savart law and add up the contributions of every small element round the loop.

**At the centre.** Every element is the same distance $R$ from the centre and at right angles to the line joining them, and every contribution points the same way — along the axis. They all add. For a coil of $N$ turns carrying current $I$:

$$B_\text{centre} = \frac{\mu_0 N I}{2R}$$

**On the axis**, at a distance $x$ from the centre, each element's field tilts. Their sideways parts cancel in opposite pairs, and only the parts along the axis add:

$$B_\text{axis} = \frac{\mu_0 N I R^{2}}{2\,(R^{2}+x^{2})^{3/2}}$$

At $x = 0$ this reduces to the centre formula. Far away ($x \gg R$) it falls off as $1/x^{3}$ — much faster than the $1/x^{2}$ you might guess.

![On the left, a circular current loop seen face on, with the field at its centre along the axis; on the right, the same loop seen edge on with the field at a point on the axis](figures/circular_loop_field/loop-centre-and-axis.svg "At the centre every element's field points the same way and they all add. Along the axis the sideways parts cancel in pairs — only the parts along the axis survive.")

The direction comes from a right-hand rule: **curl the fingers of your right hand round the loop in the direction of the current; your thumb points along $\vec{B}$ on the axis.** The loop behaves like a flat magnet, with its field coming out of one face and into the other.

## Worked example

**Given:** a pad coil with $N = 10$ turns of radius $R = 2.0\,\text{cm} = 0.020\,\text{m}$, carrying $I = 1.0\,\text{A}$ at one instant (illustrative values).
**Find:** the field at the centre, and on the axis at $x = 2.0\,\text{cm}$, where a phone in a thick case might sit.

**Step 1 — at the centre.**

$$B_\text{centre} = \frac{\mu_0 N I}{2R} = \frac{(4\pi\times10^{-7})(10)(1.0)}{2(0.020)} = \pi\times10^{-4}\,\text{T} \approx 0.31\,\text{mT}$$

About six times the Earth's field — from a coil you could cover with two fingers.

**Step 2 — at $x = R$.** Here $R^{2}+x^{2} = 2R^{2}$, so the axis formula becomes the centre field times $\dfrac{R^{3}}{(2R^{2})^{3/2}} = \dfrac{1}{2^{3/2}} \approx 0.35$:

$$B_\text{axis} \approx 0.35\times0.31\,\text{mT} \approx 0.11\,\text{mT}$$

Lifting the phone by just one coil radius leaves only about a **third** of the field.

**Sanity check:** a gap the size of the coil itself is "far" for that coil — so a big drop over just two centimetres makes sense, and a small, closely matched coil in the phone is exactly why the phone must sit flat on the pad.

## Where the picture breaks

A real charging coil is a flat **spiral**, not ten loops all of the same radius, so the true field is a sum over slightly different sizes. The black magnetic sheet under it also shapes the field upwards. Our formula is a good first estimate, not the design answer.

The pad's current is not steady either: it alternates at roughly 100–200 kHz, because only a *changing* field can drive current in the phone's coil. The formulas give the field at any one instant.

And the charger doesn't just get weaker with distance. How well it transfers energy depends on how much of the pad's field passes through the phone's coil, and the pad also checks that a phone is there. That is why it switches off completely rather than fading gently.

## Key takeaway

A circular coil of $N$ turns carrying current $I$ makes a field $B = \dfrac{\mu_0 N I}{2R}$ at its centre, along its axis, with direction given by curling the right hand's fingers along the current. On the axis at distance $x$, $B = \dfrac{\mu_0 N I R^{2}}{2(R^{2}+x^{2})^{3/2}}$ — it drops to about a third at one radius away, and falls as $1/x^{3}$ far off.
