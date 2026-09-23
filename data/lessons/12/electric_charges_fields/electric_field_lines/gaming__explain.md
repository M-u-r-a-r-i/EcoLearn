---
concept_id: electric_field_lines
interest: gaming
format: explain
title: The glowing threads that never cross
check:
  question: |-
    In one diagram, 12 field lines are drawn leaving charge X. Four of them end on a nearby charge Y, and the other eight run off to infinity. What can you conclude about Y?
  options:
    A: |-
      Y is negative, with a magnitude one third of X's.
    B: |-
      Y is negative, with the same magnitude as X.
    C: |-
      Y is positive, because lines are always drawn running from one charge to another.
    D: |-
      Nothing about Y's size can be worked out, because the number of lines drawn is a free choice.
  answer: A
  explanation: |-
    Lines end on negative charges, so Y is negative, and the number of lines is drawn proportional to the magnitude of the charge: $4/12 = 1/3$, so $|q_Y| = |q_X|/3$.
  misconceptions:
    B: |-
      Assumes any pair of charges joined by lines must be equal and opposite. Only a charge that catches *all* of X's lines matches it in magnitude.
    C: |-
      Reverses the convention. Lines leave positive charges and end on negative ones, and eight of X's lines here end nowhere at all.
    D: |-
      Confuses the free choice of how many lines to draw in total with the rule that fixes their ratio. Within one diagram the scale is the same for every charge.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night during a PC build: a monitor running a field sandbox with two charges, a plasma globe, an antistatic bag sparking to a fingertip, and an open PC case with a graphics card going in](scenes/gaming/electric_charges_fields.svg "The plasma globe on the desk is the only thing here that draws its own field.")

The plasma globe was a birthday present, bought for the desk because it looked good next to the RGB strip. Nandini has kept it because of what it does when you touch it.

Left alone, it throws a dozen violet threads out from the ball at its centre to the glass, all trembling slightly. Put a fingertip on the glass and one thread swings across and fastens onto the spot under her finger, brighter than the rest.

Her cousin, who plays on the same team, leans in and starts counting. "Look — they bend round each other. They get squashed together near the middle and spread out near the glass. And not one of them ever crosses another."

Nandini looks properly for the first time. Something in that sealed glass ball is being drawn in the air, and it obeys rules. What are those threads a picture of — and why should two of them never cross?

## The physics

The threads are the globe's own rough sketch of **electric field lines**.

An **electric field line** is a curve drawn so that the **tangent at every point gives the direction of $\vec{E}$** there. Lines are a map of the field, and they obey a short list of rules.

1. **They start on positive charges and end on negative charges.** For a lone charge, they start or end at infinity.
2. **In charge-free space they are continuous curves**, with no breaks.
3. **Two field lines never cross.** At any point the field has exactly one direction; at a crossing it would have two.
4. **Electrostatic field lines never close into loops.** They run from positive to negative, never round in a circle.
5. **Their crowding shows the field's strength.** The number of lines per unit area, through a surface held at right angles to them, is proportional to $E$: crowded lines mean a strong field.

The number of lines drawn leaving or entering a charge is made **proportional to the size of that charge** — twice the charge, twice the lines.

![Three field-line patterns: a single positive charge with radial lines, a dipole whose lines leave the positive charge and curve into the negative one, and two equal positive charges whose lines turn away from each other with a neutral point between them](figures/electric_field_lines/field-line-patterns.svg "Three patterns worth knowing. In (c) the two sets of lines never meet, and midway between the charges the field is exactly zero.")

Rule 5 also explains the inverse-square law in one line. For an isolated charge, $N$ lines spread over a sphere of area $4\pi r^2$, so their density is $N/(4\pi r^2)$ — falling as $1/r^2$, exactly like $E$.

Pattern (c) is worth a second look: between two like charges there is a **neutral point**, a place where the two fields cancel exactly and no line passes.

## Worked example

**Given (illustrative):** two positive charges on a line, $q_1 = +4.0\,\text{nC}$ and $q_2 = +1.0\,\text{nC}$, held $0.30\,\text{m}$ apart.
**Find:** where between them the field is zero — the neutral point in pattern (c).

Let the point be a distance $x$ from $q_1$, so it is $(0.30 - x)$ from $q_2$. The two fields point in opposite directions there, so they cancel when their magnitudes are equal:

$$\frac{k q_1}{x^2} = \frac{k q_2}{(0.30 - x)^2}$$

**Step 1 — take the ratio.** Cancelling $k$ and taking the square root of both sides:

$$\frac{x}{0.30 - x} = \sqrt{\frac{q_1}{q_2}} = \sqrt{4} = 2$$

The distances are in the ratio $2:1$ — the neutral point sits further from the *bigger* charge, because a bigger charge needs more distance to be brought down to the same strength.

**Step 2 — solve.** $x = 2(0.30 - x)$, so $3x = 0.60$ and

$$x = 0.20\,\text{m}$$

The field vanishes $0.20\,\text{m}$ from the $4.0\,\text{nC}$ charge and $0.10\,\text{m}$ from the $1.0\,\text{nC}$ one.

**Sanity check:** a quarter of the charge at half the distance gives the same field, since halving the distance quadruples it — so the point is in exactly the right place.

## Where the picture breaks

A plasma globe is a beautiful hook and a poor diagram. Those threads are channels of glowing ionised gas, not field lines: they carry a current, they wander, and the globe drives them with a voltage that reverses millions of times a second, so nothing in it is electrostatic. A finger changes the pattern because a hand is a conductor connected to the room, not because field lines like fingers.

Even a proper line diagram is a convention. The total number of lines is your choice — only ratios and crowding mean anything — and a flat drawing shows one slice of a three-dimensional pattern. And a field line is **not** a path: a charge released on a curved line starts off along it, but inertia carries it away from the line at once.

## Key takeaway

A field line's tangent gives the direction of $\vec{E}$. Lines start on positive charges and end on negative ones, never cross, never form closed loops in electrostatics, and crowd together where the field is strong. The number of lines is proportional to the charge, and between two like charges there is a neutral point where the field is zero.
