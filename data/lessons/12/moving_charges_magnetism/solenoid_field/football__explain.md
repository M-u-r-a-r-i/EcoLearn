---
concept_id: solenoid_field
interest: football
format: explain
title: The valve nobody turns
check:
  question: |-
    A long solenoid carries a current $I$ and produces a field $B$ inside it. A second long solenoid has the **same number of turns per metre** and carries the **same current**, but is wound on a tube of twice the diameter. The field inside the second solenoid is
  options:
    A: |-
      $B/2$
    B: |-
      $2B$
    C: |-
      $B$ — the same as the first
    D: |-
      $B/4$
  answer: C
  explanation: |-
    Ampère's law gives $B = \mu_0 n I$ inside a long solenoid. Only the turns per unit length $n$ and the current appear — the radius does not, as long as the solenoid is much longer than it is wide.
  misconceptions:
    A: |-
      Thinks the same "amount of field" has to spread over a bigger cross-section, so it must thin out. A wider solenoid does carry more total flux, but the field *strength* inside is unchanged.
    B: |-
      Assumes a bigger coil is a stronger coil because each turn is longer and holds more wire. The extra wire is also further from the axis, and the two effects cancel exactly.
    D: |-
      Scales the field by the cross-sectional area, which grows four times. The field inside a long solenoid does not depend on the area at all.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A football ground with a coil traced around the goal frame, a pop-up sprinkler on a solenoid valve, an electric line-marking machine and a horn speaker on a pole with a compass lying on its supply cable](scenes/football/moving_charges_magnetism.svg "Look at the buried box beside the sprinkler: that is where the water is switched on and off.")

Dev stays behind after training twice a week to practise free kicks against an empty goal, and he has learned to be off the grass by nine.

At nine exactly, something under the pitch goes *click*. A row of sprinkler heads rises out of the turf near the far post and starts turning. Ninety seconds later they sink back, there is another click, and the next row comes up.

The first time it happened he looked for the groundsman. Nobody was there. There is no tap at the side of the pitch, no wheel, no handle — only a buried plastic box with two thin wires going into it, and mains water pressure sitting behind it all day doing nothing.

Something in that box holds back the water all day and lets it through at nine. Two thin wires, no moving handle. What is inside?

## The physics

A coil — and the field a coil makes inside itself is one of the tidiest results in this chapter.

A **solenoid** is a long cylinder of closely wound turns. Each turn makes a field like the circular loop of an earlier lesson; stack them up and, in the middle, the fields reinforce along the axis while the parts pointing across the axis cancel between neighbours. The result is a field that is **uniform inside and almost zero outside** — a bar magnet's field, made to order and switchable.

![A long solenoid cut along its axis, with current out of the page on top and into the page below, a uniform field inside, almost nothing outside, and a rectangular Amperian loop of length L](figures/solenoid_field/solenoid-field-and-amperian-rectangle.svg "Only the inside arm of the rectangle contributes: the outside arm sits where B ≈ 0, and the two short arms are perpendicular to B.")

To find its size, use Ampère's law with a rectangular loop that has one arm along the axis inside, one arm outside, and two short arms crossing the windings. Walk around it:

- the **inside arm**, of length $L$, runs along $\vec{B}$: it contributes $BL$;
- the **outside arm** sits where $B \approx 0$: it contributes nothing;
- the **two short arms** cross the field at right angles, so $\vec{B} \cdot d\vec{l} = 0$ on each.

So $\oint \vec{B}\cdot d\vec{l} = BL$. If the winding has $n$ turns per unit length, the rectangle is threaded by $nL$ turns, each carrying $I$, so $I_\text{enc} = nLI$ and

$$BL = \mu_0 n L I \qquad \Longrightarrow \qquad \boxed{B = \mu_0 n I}$$

Read what is *missing* from that result: the radius, the length of the solenoid, and where inside you measure. A long solenoid makes the same field everywhere in its middle, no matter how wide it is. The direction is the right-hand curl rule again — fingers the way the current circles, thumb along the field.

This holds for an **ideal** solenoid: much longer than it is wide, closely and evenly wound, and measured near the middle. Slide a soft iron rod inside and the field becomes hundreds of times stronger, which is the trick every real valve uses.

## Worked example

**Given:** the valve coil has $N = 500$ turns wound over a length of $0.10\,\text{m}$, carrying $I = 0.40\,\text{A}$.
**Find:** the field inside it.

**Step 1 — the turns per metre.**

$$n = \frac{N}{L} = \frac{500}{0.10} = 5000\ \text{turns per metre}$$

**Step 2 — the field.**

$$B = \mu_0 n I = (4\pi \times 10^{-7})(5000)(0.40) \approx 2.5 \times 10^{-3}\,\text{T}$$

About $2.5\,\text{mT}$ — some fifty times the Earth's field, inside a coil you could hide in your fist. That field pulls an iron plunger up the middle of the coil, and the plunger is what lifts off the valve seat and lets the water through.

**Sanity check:** the only ways to strengthen it are more turns per centimetre or more current — not a fatter coil. That is why a valve coil is wound thin and tall rather than wide.

## Where the picture breaks

"Almost zero outside" and "uniform inside" are both idealisations that fail at the ends. At the very mouth of a real solenoid the field is roughly **half** its middle value, and it spills out into the familiar bar-magnet shape. The rectangle trick works because it is drawn in the middle of a long coil.

The valve also does something this lesson cannot finish explaining. The field does not push the water; it pulls an iron plunger, and *why* iron is dragged into a field belongs to the chapter on magnetism and matter. Without that iron, $2.5\,\text{mT}$ would move nothing.

And a solenoid left on gets hot. Some valves hold themselves open with a much smaller current after the initial pull, precisely to keep that heat down.

## Key takeaway

Inside a long solenoid the field is uniform, along the axis, and given by $B = \mu_0 n I$, where $n$ is the turns per unit length. It depends on the winding density and the current only — not on the radius, and not on where in the middle you measure — and outside the coil it is very nearly zero.
