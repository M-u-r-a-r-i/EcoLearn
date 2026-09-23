---
concept_id: solenoid_field
interest: cricket
format: explain
title: The click before the sprinklers
check:
  question: |-
    A long solenoid is stretched to twice its original length, keeping the same total number of turns and carrying the same current. The magnetic field inside it becomes
  options:
    A: |-
      half as strong.
    B: |-
      unchanged, because the number of turns and the current are the same.
    C: |-
      twice as strong.
    D: |-
      a quarter as strong.
  answer: A
  explanation: |-
    $B = \mu_0 n I$, where $n = N/L$ is the number of turns **per unit length**. Doubling $L$ with $N$ fixed halves $n$, so it halves $B$.
  misconceptions:
    B: |-
      Thinks the field depends on the total number of turns $N$. It depends on how tightly those turns are packed: the same $N$ spread over twice the length gives half the field.
    C: |-
      Reasons that a longer solenoid is "more solenoid", so stronger. Length is in the denominator of $n$ — spreading the turns out weakens the field.
    D: |-
      Applies the length change twice, as if $B \propto 1/L^{2}$. Only one power of the length appears, through $n = N/L$.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground with an electric roller, a compass lying on a thick power cable, a bowling machine and a loudspeaker on a pole](scenes/cricket/moving_charges_magnetism.svg "Nearly every switch, valve and motor on a ground has a coil hidden inside it.")

Half past five, nets finished, and the outfield sprinklers are due. Ishita is helping the groundsman wind up the hosepipes when a small, flat *click* comes from the box beside the sightscreen — and a second later every sprinkler on the square hisses into life.

She opens the box. Inside is a brass valve with a fat coil of wire wound around a tube on top, its two wires running back to the timer. No motor. No lever. No handle for anyone to turn.

The groundsman shrugs: "Timer sends current, valve opens."

Ishita takes the top off the tube. There is a little iron plug inside it, free to slide — and it is not touching the coil anywhere. The coil is outside the tube, the plug is sealed inside with the water. Nothing mechanical connects them. So how does switching on a current haul an iron plug up a pipe?

## The physics

A **solenoid** is a long coil: many turns of wire wound close together in a cylinder. Each turn makes a field like the loop in the last lesson, and stacked together their fields add along the axis and largely cancel outside.

For an ideal long solenoid the result is strikingly simple. Inside, the field is **uniform**: same size, same direction, parallel to the axis, everywhere in the middle of the coil. Outside, it is very nearly zero.

![A long solenoid cut along its axis, with current out of the page on top and into the page below, a uniform field inside, almost nothing outside, and a rectangular Amperian loop of length L](figures/solenoid_field/solenoid-field-and-amperian-rectangle.svg "Only the inside arm of the rectangle contributes: the outside arm sits where B ≈ 0, and the two short arms are perpendicular to B.")

Ampère's law gets us there in four lines. Take a rectangular loop with one long side of length $L$ inside the solenoid, along the axis, and the opposite side outside.

- Along the **inside** arm, $\vec{B}$ is parallel to the path and constant: this contributes $BL$.
- Along the **outside** arm, $B \approx 0$: contributes nothing.
- Along the **two short arms**, $\vec{B}$ is perpendicular to the path: $\vec{B}\cdot d\vec{l} = 0$.

So $\oint \vec{B}\cdot d\vec{l} = BL$. If the coil has $n$ turns per unit length, the loop encloses $nL$ turns, each carrying $I$, so $I_\text{enclosed} = nLI$. Ampère's law then gives $BL = \mu_0 nLI$, and the $L$ cancels:

$$B = \mu_0 n I \qquad\text{with}\qquad n = \frac{N}{L}$$

Read what is *not* in that formula: no radius, and no position inside the coil. A wide solenoid and a narrow one with the same turns per metre and the same current have the same internal field.

**Direction:** curl your right fingers along the current in the turns; your thumb points along $\vec{B}$ inside, which is the solenoid's north end. A current-carrying solenoid is, from outside, essentially a bar magnet — which is what grabs Ishita's iron plug and drags it in.

This result is exact only for an ideal, infinitely long solenoid; near the ends the field weakens to about half its central value.

## Worked example

**Given:** a valve coil of $500$ turns wound over a length of $20\,\text{cm}$, carrying $2.0\,\text{A}$.
**Find:** the magnetic field inside it.

**Step 1 — the turns per unit length.**

$$n = \frac{N}{L} = \frac{500}{0.20} = 2500\ \text{turns per metre}$$

**Step 2 — the field.**

$$B = \mu_0 n I = (4\pi \times 10^{-7})(2500)(2.0) \approx 6.3 \times 10^{-3}\,\text{T}$$

About $6\,\text{mT}$: over a hundred times the Earth's magnetic field, though still well short of the few tens of millitesla at the face of a fridge magnet.

**Sanity check:** a current-carrying coil that is stronger than the Earth but weaker than a small permanent magnet is exactly the right size for something that has to tug a plug a few millimetres and no further.

## Where the picture breaks

"Outside the solenoid, $B = 0$" is the useful lie in this derivation. The field lines have to close on themselves, so they do return outside — spread thinly over a huge area, which is why the outside field is weak enough to ignore for a long coil. Near a short coil, or near either end, it is not.

The valve also cheats, in a way this chapter cannot yet explain. That iron plug does not merely sit in the coil's field; iron concentrates field lines enormously, so the real field in the gap is many times $\mu_0 n I$. Soft iron is used precisely because it lets go again the instant the current stops — which is why the sprinklers shut off with a second click. Why iron does that is the subject of the next chapter.

## Key takeaway

Inside a long solenoid the magnetic field is uniform and parallel to the axis, with $B = \mu_0 n I$, where $n$ is the number of turns **per unit length**; outside, it is nearly zero. Ampère's law gives this in a few lines by choosing a rectangular loop with one side inside the coil and one outside.
