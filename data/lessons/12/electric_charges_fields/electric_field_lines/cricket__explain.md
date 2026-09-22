---
concept_id: electric_field_lines
interest: cricket
format: explain
title: Grass seed that draws the invisible
check:
  question: |-
    In Tanvi's exhibition dish, the grass seeds trace out the field lines around two electrodes. Which statement about electric field lines is correct?
  options:
    A: |-
      Two field lines can cross at a point where the fields of two charges meet.
    B: |-
      A field line is always the path a positive charge follows when released from rest.
    C: |-
      Where the field lines are closer together, the electric field is stronger.
    D: |-
      Field lines start on negative charges and end on positive charges.
  answer: C
  explanation: |-
    The number of lines per unit area crossing a surface at right angles is proportional to the field strength, so crowded lines mean a strong field and spread-out lines a weak one.
  misconceptions:
    A: |-
      Forgets that the field at any point has exactly one direction. If two lines crossed, the field there would point two ways at once, so lines never cross.
    B: |-
      Confuses the direction of the force with the path of motion. A released charge starts along the line, but once it is moving it has inertia and generally leaves a curved line.
    D: |-
      Reverses the convention. Field lines point the way a positive charge would be pushed, so they leave positive charges and end on negative ones.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A storm over a cricket ground: dark clouds, distant lightning, players walking off, groundstaff dragging a plastic cover and a team bus waiting](scenes/cricket/electric_charges_fields.svg "Around every charge in this picture there is a field. Can you draw it?")

Tanvi's school is holding a science exhibition on "the physics of the cricket ground", and she wants a stall nobody will forget. Her idea comes from an unlikely place: the bag of grass seed that Bala, the groundsman, uses to repair worn patches on the outfield.

She scatters a pinch of the fine seed on a shallow dish of castor oil. Her physics teacher clamps two metal electrodes into the oil and connects them to the lab's high-voltage supply, one charged positive and one negative, carefully keeping the students' hands clear.

As the supply is switched on, the seeds twitch, then swing round. Within seconds they have lined up nose to tail into chains: curves that leave one electrode, bulge outwards and bend round to meet the other. Near the electrodes the chains crowd together; far away they spread out.

The seeds have drawn a picture of something invisible. But what exactly are those curves, and why does no chain ever cross another?

## The physics

The seeds are tracing **electric field lines**. Each seed becomes slightly polarised in the field (one end a little positive, the other a little negative) and the field turns it to point along the local field direction, like a compass needle.

An **electric field line** is a curve drawn so that the **tangent at every point gives the direction of $\vec{E}$** at that point. Field lines are a map of the field. They obey these rules:

1. **They start on positive charges and end on negative charges.** With a single charge, they start or end at infinity.
2. **In a region with no charge, they are continuous curves** with no breaks.
3. **Two field lines never cross.** At any point the field has one direction; at a crossing it would have two.
4. **Electrostatic field lines never form closed loops.** They always run from positive to negative.
5. **Their density shows the field strength.** The number of lines per unit area, through a surface at right angles to them, is proportional to $E$: crowded lines mean a strong field.

The number of lines leaving or entering a charge is drawn **proportional to the size of the charge**.

![Field lines for a single positive charge (radial, outwards), a dipole (lines leave the positive charge and curve round to the negative one) and two equal positive charges (lines push apart, with a neutral point midway)](figures/electric_field_lines/field-line-patterns.svg "Three patterns to know. In (c) the two sets of lines never meet; midway between the charges the field is zero.")

The dipole pattern in (b) is exactly what Tanvi's seeds drew between a positive and a negative electrode. Two like electrodes would give pattern (c) instead, with the lines turning away from each other and an empty gap between them: the **neutral point**, where the two fields cancel.

The density rule also explains the inverse-square law. For an isolated charge, $N$ lines spread out over a sphere of area $4\pi r^2$, so the density is $N/(4\pi r^2)$, which falls as $1/r^2$, just like $E$.

## Worked example

**Given:** a sketch shows 16 lines leaving charge A, which is $+8.0\,\text{nC}$. Of these, 8 lines end on charge B and the other 8 go off to infinity. No lines leave B.
**Find:** (a) the charge on B; (b) how the line density around an isolated A compares at $0.10\,\text{m}$ and $0.20\,\text{m}$.

(a) Lines end on B, so B is negative. The number of lines is proportional to charge magnitude: $8/16 = 1/2$, so $|q_B| = 4.0\,\text{nC}$, giving $q_B = -4.0\,\text{nC}$. The 8 lines that escape to infinity show that A's charge is bigger in size.

(b) Line density $= N/(4\pi r^2)$:

$$\text{at } 0.10\,\text{m}: \frac{16}{4\pi(0.10)^2} = \frac{16}{0.126} \approx 127\,\text{lines/m}^2 \qquad \text{at } 0.20\,\text{m}: \frac{16}{4\pi(0.20)^2} = \frac{16}{0.503} \approx 31.8\,\text{lines/m}^2$$

The ratio is $127/31.8 \approx 4$, matching $E \propto 1/r^2$.

**Sanity check:** the total charge is $+8.0 - 4.0 = +4.0\,\text{nC}$, positive, so far away the pattern should look like a single positive charge with lines going outwards to infinity, just as the 8 escaping lines show.

## Where the picture breaks

The number of lines is a choice: the rule is only that it's *proportional* to the charge, so "16 lines" has no absolute meaning. Field lines also exist in three dimensions, and a flat drawing (or a flat dish) shows only one slice. The seeds line up because they're polarised, and in a real dish the oil and seeds slightly distort the field they're mapping. Finally, a field line is not a path: a charge released on one generally won't follow it.

## Key takeaway

A field line's tangent gives the direction of $\vec{E}$. Lines start on positive charges and end on negative ones, never cross, never form closed loops in electrostatics, and crowd together where the field is strong. The number of lines is proportional to the charge.
