---
concept_id: biot_savart_law
interest: gaming
format: explain
title: The trace that bends around a mounting hole
check:
  question: |-
    A short current element on a circuit board carries current towards the **east**. At which of these points, all $1\,\text{cm}$ from the element, does this element produce **no** magnetic field at all?
  options:
    A: |-
      Directly north of it, in the plane of the board.
    B: |-
      Directly above it, out of the plane of the board.
    C: |-
      Directly east of it, straight ahead along the line of the current.
    D: |-
      Nowhere — the element's field is non-zero in every direction, just weaker further away.
  answer: C
  explanation: |-
    The Biot–Savart law gives $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl\sin\theta}{r^{2}}$, where $\theta$ is the angle between the element and the line to the point. Straight ahead along the current, $\theta = 0°$ and $\sin\theta = 0$, so the contribution vanishes.
  misconceptions:
    A: |-
      Picks a point at right angles to the element — where $\sin\theta = 1$ and the element's field is at its *strongest*, not its weakest.
    B: |-
      The same error as A in a different direction. Directly above the element the angle is still $90°$, so this is another point of maximum contribution.
    D: |-
      Remembers the $1/r^{2}$ and forgets the $\sin\theta$. The Biot–Savart law has an angle in it, and along the element's own line that angle switches the contribution off completely.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming workbench with a bartop arcade cabinet, a cutaway of a pinball flipper coil, a controller with its shell off showing a magnet above a sensor chip, a PC case fan, and a phone on a power cable](scenes/gaming/moving_charges_magnetism.svg "The controller's stick uses a magnet over a sensor chip. A keyboard can be built the same way — one magnet per key — which is where this story starts.")

Aditi is laying out the circuit board for a custom keyboard, and she has chosen magnetic switches: a tiny magnet in every key stem, a sensor in the board underneath. It is her first board, so she has sent the layout to a friend who has made a dozen.

The reply is one line. *Move your LED power trace away from the sensors. At least a centimetre.*

Aditi is annoyed, because the trace is on the opposite side of the board and touches nothing. She is more annoyed because she cannot argue back. She has no idea how big the trace's magnetic field actually is — and the trace is not a straight line. It leaves the connector, turns a corner, runs a while, curves around a mounting hole and carries on.

Every formula she has ever met is for a long straight wire. Hers is a squiggle. How do you get a field out of a shape like that?

## The physics

The same way you get the area of an odd shape: cut it into pieces small enough to be simple, work out each piece, and add them up. The rule for one piece is the **Biot–Savart law**.

Take a tiny length $d\vec{l}$ of wire, pointing along the conventional current $I$. Let $\vec{r}$ run from that element to the point P where you want the field, with $\hat{r}$ the unit vector along it. Then the element's contribution is

$$d\vec{B} = \frac{\mu_0}{4\pi}\,\frac{I\,d\vec{l}\times\hat{r}}{r^{2}} \qquad\text{with size}\qquad dB = \frac{\mu_0}{4\pi}\,\frac{I\,dl\,\sin\theta}{r^{2}}$$

Here $\theta$ is the angle between $d\vec{l}$ and $\vec{r}$, and $\mu_0 = 4\pi\times10^{-7}\,\text{T}\,\text{m}/\text{A}$ is the **permeability of free space**, which makes the constant $\mu_0/4\pi = 10^{-7}$ in SI units — a number worth memorising, because it turns most of these calculations into one line.

![A short current element dl on a curved wire, the vector r to a point P, the angle theta between them, and the small field dB at P pointing into the page](figures/biot_savart_law/current-element-dB.svg "The contribution is perpendicular to both the element and the line to P — so it points into or out of the plane they define.")

Read the four pieces of the formula separately:

- $dB \propto I$ and $dB \propto dl$ — more current, or more wire, gives more field.
- $dB \propto 1/r^{2}$ — an inverse-square law, like Coulomb's.
- $dB \propto \sin\theta$ — and this is the part with no electrical cousin. An element sends out **nothing at all** along its own line, and the most it can give at right angles.
- The **direction** comes from $d\vec{l}\times\hat{r}$: perpendicular to both, by the right-hand rule. Wrap your right hand round the element with the thumb along $I$, and $d\vec{B}$ follows your fingers, just as Oersted's grip rule said.

To get the field of Aditi's whole squiggle you add every element's $d\vec{B}$ **as vectors**. Along a straight run they all happen to point the same way and only differ in size; once the trace bends around the mounting hole, even their directions differ, and nothing but a proper vector sum will do. The next two lessons do that sum for the two shapes that matter most: a circular loop and a long straight wire.

## Worked example

**Given:** a $1.0\,\text{mm}$ length of trace carrying $2.0\,\text{A}$, and a sensor $1.0\,\text{cm}$ away in the direction at right angles to the trace.
**Find:** the field that this one small piece of trace contributes at the sensor.

**Step 1 — the size.** At right angles, $\sin\theta = 1$:

$$dB = \frac{\mu_0}{4\pi}\frac{I\,dl}{r^{2}} = 10^{-7}\times\frac{(2.0)(1.0\times10^{-3})}{(1.0\times10^{-2})^{2}} = 10^{-7}\times 20 = 2.0\times10^{-6}\,\text{T}$$

**Step 2 — picture it.** Two microtesla is roughly a twenty-fifth of the Earth's own magnetic field: small, but not nothing, and a magnetic sensor is built to notice far less than the Earth's field.

**Step 3 — and the rest of the trace?** A three-centimetre run holds about thirty pieces like this one. You cannot simply multiply by thirty: the far ones sit at larger $r$ and smaller $\sin\theta$, so each gives less, and past the bend they push in a different direction as well.

**Sanity check:** one millimetre of wire producing a few per cent of the Earth's field a centimetre away sounds about right — which is exactly why Aditi's friend wanted that centimetre.

## Where the picture breaks

The honest catch first: **a current element cannot exist on its own.** Current must flow round a closed circuit, so you can never isolate one $d\vec{l}$ and measure its $d\vec{B}$. The Biot–Savart law is a bookkeeping rule that gives the right answer once you have added up a complete loop; the individual contributions are not separately measurable.

That matters for Aditi's board. The LED current does not vanish at the end of the trace — it returns, usually through a ground plane lying directly underneath. Two nearly-coincident opposite currents almost cancel a millimetre away, so the real field near her sensors is much smaller than the worked example suggests, and the "at least a centimetre" rule is a comfortable margin rather than a calculation.

Finally, the law as stated is for **steady** currents. The LED trace in a keyboard is switched thousands of times a second, and switching currents do things this chapter does not cover.

## Key takeaway

The **Biot–Savart law** says every little piece of a current-carrying wire makes its own small field, $d\vec{B} = \dfrac{\mu_0}{4\pi}\dfrac{I\,d\vec{l}\times\hat{r}}{r^{2}}$ — falling off as $1/r^{2}$, strongest at right angles to the element, zero straight ahead of it, and directed perpendicular to both the element and the line to the point. The field of any shape of wire is the vector sum of all of them.
