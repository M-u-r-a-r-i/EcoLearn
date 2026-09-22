---
concept_id: vector_addition
interest: cricket
format: explain
title: Why two groundstaff pulling 700 newtons don't make 700
check:
  question: |-
    Two groundstaff pull on the same corner of a rain cover with forces of $400\,\text{N}$ and $300\,\text{N}$. The angle between their ropes is $60^\circ$. What is the size of their combined pull?
  options:
    A: |-
      About $608\,\text{N}$
    B: |-
      $700\,\text{N}$
    C: |-
      $100\,\text{N}$
    D: |-
      $500\,\text{N}$
  answer: A
  explanation: |-
    $R = \sqrt{A^2 + B^2 + 2AB\cos\theta} = \sqrt{400^2 + 300^2 + 2(400)(300)\cos 60^\circ} = \sqrt{370\,000} \approx 608\,\text{N}$.
  misconceptions:
    B: |-
      Adds the magnitudes as if both ropes pointed the same way. That is true only when the angle between them is zero.
    C: |-
      Subtracts the magnitudes, which is correct only when the ropes pull in exactly opposite directions.
    D: |-
      Uses Pythagoras, $\sqrt{A^2 + B^2}$, whatever the angle. That shortcut works only when the vectors are at right angles.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A day match: a batter lofts the ball towards the boundary as a fielder races along the rope](scenes/cricket/motion_plane.svg "The sky can change fast at a cricket ground, and so can the groundstaff's job.")

The sky over the ground turns grey in minutes. The umpires take the players off, and the groundstaff sprint out with the big rain cover for the pitch.

Mahesh, the head groundsman, grabs one rope tied to the front corner. Young Sunil grabs another rope tied to the same corner. Mahesh pulls straight towards the far end of the pitch; Sunil has to stand off to one side so they don't trip over each other.

"Pull harder, Sunil!" Mahesh shouts.

"I'm pulling 300 newtons, you're pulling 400," Sunil gasps. "That's 700 newtons on that corner!"

"Only if we both pull the same way," says Mahesh. "We don't."

So what *is* the combined pull on that corner, and which way does the cover actually slide?

## The physics

Forces, velocities and displacements are vectors, so you can't add them like ordinary numbers. The direction matters. Two rules give the sum, the **resultant** $\vec{R} = \vec{A} + \vec{B}$:

- **Triangle rule:** draw $\vec{A}$, then draw $\vec{B}$ starting from the head of $\vec{A}$. The resultant runs from the tail of $\vec{A}$ to the head of $\vec{B}$.
- **Parallelogram rule:** draw $\vec{A}$ and $\vec{B}$ from the same point, complete the parallelogram, and the diagonal from that point is $\vec{R}$.

Both rules give the same answer, and the order doesn't matter: $\vec{A} + \vec{B} = \vec{B} + \vec{A}$.

![Left: A and B drawn head to tail with R closing the triangle. Right: A and B drawn from one point, with R as the parallelogram's diagonal](figures/vector_addition/triangle-and-parallelogram.svg "Two ways to draw the same sum. In both, the resultant starts where A starts and ends where the chain of arrows ends.")

For two vectors of sizes $A$ and $B$ with angle $\theta$ between them, the triangle gives (by the law of cosines):

$$R = \sqrt{A^2 + B^2 + 2AB\cos\theta}$$

and the resultant makes an angle $\alpha$ with $\vec{A}$, where

$$\tan\alpha = \frac{B\sin\theta}{A + B\cos\theta}$$

That formula explains Mahesh's point. The resultant depends on the angle:

- $\theta = 0^\circ$ (same direction): $R = A + B$, the largest possible.
- $\theta = 90^\circ$: $R = \sqrt{A^2 + B^2}$.
- $\theta = 180^\circ$ (opposite): $R = |A - B|$, the smallest possible.

![A graph of the resultant of vectors of sizes 3 and 4 against the angle between them, falling from 7 at 0 degrees through 5 at 90 degrees to 1 at 180 degrees](figures/vector_addition/resultant-vs-angle.svg "The same two vectors can give any resultant from their difference to their sum. Only the angle decides which.")

In the story, Mahesh's rope is $\vec{A}$ and Sunil's is $\vec{B}$. Because Sunil stands off to the side, some of his pull goes sideways, not along the pitch.

## Worked example

**Given:** Mahesh pulls with $A = 400\,\text{N}$ along the pitch; Sunil pulls with $B = 300\,\text{N}$ at $\theta = 90^\circ$ to Mahesh's rope (illustrative numbers).
**Find:** the size and direction of the combined pull.

With $\cos 90^\circ = 0$:
$$R = \sqrt{400^2 + 300^2} = \sqrt{160\,000 + 90\,000} = \sqrt{250\,000} = 500\,\text{N}$$

Direction, with $\sin 90^\circ = 1$:
$$\tan\alpha = \frac{300 \times 1}{400 + 0} = 0.75 \quad\Rightarrow\quad \alpha \approx 37^\circ$$

The corner is pulled with $500\,\text{N}$, at about $37^\circ$ from Mahesh's rope, towards Sunil's side. Not $700\,\text{N}$.

**Sanity check:** $500\,\text{N}$ lies between $|400 - 300| = 100\,\text{N}$ and $400 + 300 = 700\,\text{N}$, and the direction leans towards the bigger pull, Mahesh's, since $37^\circ < 45^\circ$.

## Where the picture breaks

The resultant here is only the pull of the two ropes. The cover also feels friction from the wet grass, and it slides according to the *net* force, so it may not move in exactly the direction of $\vec{R}$. A cover is also not a point: pulling one corner makes it twist and bunch up, which our arrows ignore. And the forces themselves wobble as the two men walk; the formula gives the sum at one instant.

## Key takeaway

Vectors add by the triangle (or parallelogram) rule, not by adding their sizes. For two vectors at angle $\theta$, $R = \sqrt{A^2 + B^2 + 2AB\cos\theta}$. The resultant can be anything from $|A - B|$ (opposite directions) to $A + B$ (same direction), so two pulls of $400\,\text{N}$ and $300\,\text{N}$ make $700\,\text{N}$ only when they point the same way.
