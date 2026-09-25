---
concept_id: vector_addition
interest: smartphones
format: explain
title: Three GPS speeds on one ferry
check:
  question: |-
    A small camera drone flies north at $6\,\text{m/s}$ relative to the air, while a steady wind carries the air east at $8\,\text{m/s}$. How fast does the drone move over the ground?
  options:
    A: |-
      $14\,\text{m/s}$
    B: |-
      $2\,\text{m/s}$
    C: |-
      $10\,\text{m/s}$
    D: |-
      $7\,\text{m/s}$
  answer: C
  explanation: |-
    The two velocities are at right angles, so the resultant is the hypotenuse: $\sqrt{6^2 + 8^2} = \sqrt{100} = 10\,\text{m/s}$, pointing between north and east.
  misconceptions:
    A: |-
      Adds the sizes as if they were scalars. $6 + 8$ is only right when the two vectors point the same way.
    B: |-
      Subtracts the sizes, which is only right when the vectors point in opposite directions.
    D: |-
      Averages the two speeds. Vectors are not averaged when they are added; their resultant comes from the triangle rule.
author: claude-code/opus-5
written: 2026-09-25
---
## The story

![An evening terrace: a phone shows a map route, a drone flies at a slant over the rooftops, and an earbud case skids off a table](scenes/smartphones/motion_plane.svg "Every moving thing in this picture has a velocity with a size and a direction. Combining them takes more than plain adding.")

Neha and her brother Arjun are on the ferry across the harbour, and Arjun has a GPS speed app open on his phone. With the ferry cruising steadily, it reads $2.0\,\text{m/s}$.

Neha takes the phone and walks towards the front of the deck at her usual easy pace. The reading climbs to $3.5$. She turns round and walks towards the back: $0.5$. Then she walks straight across the deck, from one railing to the other.

"Easy," says Arjun, before she looks. "Either $3.5$ or $0.5$, or something in the middle, like $2.0$."

Neha glances at the screen and grins. It says $2.5$.

Her walking speed never changed. The ferry never changed. Why does the phone give three different answers, and where did $2.5$ come from?

## The physics

Neha's velocity over the water is the **vector sum** of two velocities: the ferry's velocity $\vec{A}$ (over the water) and her own velocity $\vec{B}$ (over the deck). Because vectors have direction, the size of the sum depends on the **angle** between them, not just on their sizes.

Vectors add by either of two equivalent rules:

- **Triangle rule (head to tail):** draw $\vec{A}$; draw $\vec{B}$ starting from the head of $\vec{A}$. The resultant $\vec{R} = \vec{A} + \vec{B}$ runs from the tail of $\vec{A}$ to the head of $\vec{B}$.
- **Parallelogram rule (tail to tail):** draw both from one point and complete the parallelogram. $\vec{R}$ is the diagonal from that point.

![Triangle rule: A then B head to tail, with R from A's tail to B's head. Parallelogram rule: A and B from one point, with R as the diagonal](figures/vector_addition/triangle-and-parallelogram.svg "Both rules give the same arrow. The triangle is quicker to draw; the parallelogram shows why the order doesn't matter: A + B = B + A.")

For vectors of sizes $A$ and $B$ at angle $\theta$ between them, the triangle gives (by the cosine rule)

$$R = \sqrt{A^2 + B^2 + 2AB\cos\theta}$$

Three cases to remember:
- **Same direction** ($\theta = 0^\circ$): $R = A + B$, the biggest possible.
- **Opposite** ($\theta = 180^\circ$): $R = |A - B|$, the smallest.
- **At right angles** ($\theta = 90^\circ$): $R = \sqrt{A^2 + B^2}$.

![Graph of resultant size against the angle between vectors of sizes 3 and 4: 7 at zero degrees, 5 at ninety, 1 at one hundred and eighty](figures/vector_addition/resultant-vs-angle.svg "Same two vectors, different angle, different resultant. Neha's speeds, 1.5 and 2.0, are exactly half of 3 and 4, so halve every value on this curve.")

Back on the ferry, walking forward means $\theta = 0^\circ$; walking back, $\theta = 180^\circ$; walking across, $\theta = 90^\circ$. The phone was right all three times.

## Worked example

**Given (illustrative):** ferry $A = 2.0\,\text{m/s}$ forward over the water; Neha walks at $B = 1.5\,\text{m/s}$ relative to the deck, straight across.
**Find:** her speed and direction over the water.

1. The vectors are at right angles, so $R = \sqrt{2.0^2 + 1.5^2} = \sqrt{4.00 + 2.25} = \sqrt{6.25} = 2.5\,\text{m/s}$.
2. Direction: $\tan\alpha = \dfrac{1.5}{2.0} = 0.75$, so $\alpha \approx 37^\circ$ from the ferry's heading, towards the railing she walks to.

So over the water she moves at $2.5\,\text{m/s}$, a brisk jog, along a slanting line even though on the deck she walks straight across.

**Sanity check:** $2.5$ lies between the smallest possible answer, $0.5$, and the biggest, $3.5$, as every angle in between must.

## Where the picture breaks

A phone's GPS measures speed over the **ground**, while the ferry's $2.0\,\text{m/s}$ here is over the **water**. That's the same thing only on still water; a tidal current would be a third vector to add. GPS speed readings also jitter by a few tenths of a metre per second, so a real phone wouldn't show such clean numbers. And the ferry's heading drifts a little, so the angle is never exactly $90^\circ$.

## Key takeaway

Vectors add head to tail (triangle rule) or as the diagonal of a parallelogram, and the size of the resultant depends on the angle between them: $R = \sqrt{A^2 + B^2 + 2AB\cos\theta}$. It ranges from $A + B$ (same direction) down to $|A - B|$ (opposite), with $\sqrt{A^2 + B^2}$ at right angles.
