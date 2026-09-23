---
concept_id: circular_loop_field
interest: football
format: explain
title: Why the guard has to hold the wand so close
check:
  question: |-
    A flat circular coil of $N$ turns and radius $R$ carries a current $I$. Which single change would **double** the magnetic field at the centre of the coil?
  options:
    A: |-
      Doubling the radius, keeping the current and the number of turns the same.
    B: |-
      Doubling the number of turns and the radius together, keeping the current the same.
    C: |-
      Doubling the current and the radius together, keeping the number of turns the same.
    D: |-
      Doubling the number of turns, keeping the current and the radius the same.
  answer: D
  explanation: |-
    At the centre, $B = \dfrac{\mu_0 N I}{2R}$. Only $N$ changes in option D, and $B$ is directly proportional to it, so the field doubles.
  misconceptions:
    A: |-
      Thinks a bigger loop gives a bigger field because it holds more wire. The radius is in the denominator: the extra wire is also further from the centre, and the field at the centre *halves*.
    B: |-
      Counts the extra turns but forgets that the radius sits underneath them. Doubling both leaves $N/R$ exactly as it was.
    C: |-
      Sees the current double and stops reading. Doubling the radius at the same time halves the result straight back to its original value.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground with a coil traced around the goal frame, a pop-up sprinkler on a solenoid valve, an electric line-marking machine and a horn speaker on a pole with a compass lying on its supply cable](scenes/football/moving_charges_magnetism.svg "Coils like the one traced around this goal frame are the same physics as the coil inside a security wand.")

Tanvi has queued forty minutes for a final, and the last obstacle is the security check. The guard runs a flat plastic wand over her: down the arms, down the sides, round the bag.

She notices the guard is fussy about one thing only — distance. The wand never leaves her clothes by more than a few centimetres, and when the man ahead of her holds his bag out at arm's length he is told, twice, to bring it closer.

Then the wand shrieks at a steel hairpin the size of a paperclip, hidden in Tanvi's hair, and ignores the large plastic bottle in her hand entirely.

A flat paddle with nothing inside it but a coil of wire. It can find a paperclip through hair — but only if it is almost touching. Why should a few centimetres matter so much?

## The physics

Inside the wand is a **circular coil**, and the field it makes is the answer to both halves of Tanvi's puzzle.

Add up the Biot–Savart contributions of every element of a circular loop of radius $R$ carrying current $I$, and at the **centre** each piece contributes in the same direction, along the axis. The sum is simple:

$$B_\text{centre} = \frac{\mu_0 I}{2R}, \qquad \text{and for } N \text{ closely wound turns} \quad B = \frac{\mu_0 N I}{2R}$$

![On the left, a loop seen face on with the field coming out of the page at its centre; on the right, the same loop seen edge on with the field along the axis at a point P a distance x away](figures/circular_loop_field/loop-centre-and-axis.svg "At the centre the field is μ₀NI/2R. Move along the axis and the denominator grows as (R² + x²) to the power 3/2 — quickly.")

The **direction** comes from a right-hand rule of its own: curl the fingers of your right hand the way the current goes round the loop, and your thumb points along the field on the axis. Seen from the side the thumb points towards, the current runs anticlockwise.

Step off the centre, along the axis, a distance $x$, and the pieces of the loop no longer contribute quite parallel to each other. The components across the axis cancel in pairs and only the axial parts survive:

$$B_\text{axis} = \frac{\mu_0 N I R^{2}}{2\,(R^{2} + x^{2})^{3/2}}$$

Set $x = 0$ and it collapses back to $\mu_0 N I/2R$, as it must. Go far out, $x \gg R$, and the $R^2$ under the bracket stops mattering: $B \approx \dfrac{\mu_0 N I R^{2}}{2x^{3}}$, falling as $1/x^{3}$.

That cube is the guard's problem. The field of a small loop collapses *much* faster than the $1/r^2$ of a point charge, so a coil that is powerful against your sleeve is feeble at arm's length. Both formulas hold for a flat, closely wound coil, and the axial one is only valid **on the axis**.

## Worked example

**Given:** a wand coil of $N = 100$ turns, radius $R = 0.050\,\text{m}$, carrying $I = 0.20\,\text{A}$.
**Find:** the field at its centre, and how much of it survives at $5\,\text{cm}$ and at $15\,\text{cm}$ out along the axis.

**Step 1 — at the centre.**

$$B = \frac{\mu_0 N I}{2R} = \frac{(4\pi \times 10^{-7})(100)(0.20)}{2(0.050)} \approx 2.5 \times 10^{-4}\,\text{T}$$

That is about five times the Earth's magnetic field — strong, right at the paddle.

**Step 2 — one radius out ($x = R = 0.050\,\text{m}$).** Put $x = R$ in the axial formula and the bracket becomes $(2R^{2})^{3/2} = 2\sqrt{2}\,R^{3}$, so the field is the centre value divided by $2\sqrt{2}$:

$$B \approx \frac{2.5 \times 10^{-4}}{2.83} \approx 0.9 \times 10^{-4}\,\text{T}$$

Five centimetres away, roughly a third is left.

**Step 3 — three radii out ($x = 15\,\text{cm}$).** Now the bracket is $(10R^{2})^{3/2} \approx 31.6\,R^{3}$, leaving about **3 %** of the centre field. At the length of a hand, the wand has almost nothing to offer.

**Sanity check:** a field that drops to a third in five centimetres and to a thirtieth in fifteen is exactly the behaviour of a guard who insists on holding the wand against your clothes.

## Where the picture breaks

The wand does not detect steel with this field on its own. The coil's field induces swirling currents in nearby metal, and those currents are what the wand senses — which belongs to the next chapter, on induction. What the loop formula explains is the *reach*, not the detecting.

Both equations assume a **flat, closely wound** coil, every turn at the same radius $R$. A real coil is wound over some width and thickness, so $R$ is an average and the field near the wire itself is much stronger than the formula suggests.

And the axial formula describes only points on the axis. Tanvi's hairpin was somewhere off to the side, where the field is weaker and tilted, and no formula in this chapter gives it neatly.

## Key takeaway

A circular coil of $N$ turns makes a field $\dfrac{\mu_0 N I}{2R}$ at its centre, directed along the axis by the right-hand curl rule. Along the axis it falls as $\dfrac{\mu_0 N I R^{2}}{2(R^{2}+x^{2})^{3/2}}$ — eventually as $1/x^{3}$, which is why a coil's field is a short-range thing.
