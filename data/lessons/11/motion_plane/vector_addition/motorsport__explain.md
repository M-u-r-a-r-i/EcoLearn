---
concept_id: vector_addition
interest: motorsport
format: explain
title: Why two marshals pushing 350 newtons don't make 350
check:
  question: |-
    Two marshals push on the same point of a stalled car with forces of $60\,\text{N}$ and $80\,\text{N}$. The angle between the two pushes is $60^\circ$. What is the size of the resultant push? ($\cos 60^\circ = 0.50$)
  options:
    A: |-
      $140\,\text{N}$
    B: |-
      About $122\,\text{N}$
    C: |-
      $100\,\text{N}$
    D: |-
      $20\,\text{N}$
  answer: B
  explanation: |-
    $R = \sqrt{A^2 + B^2 + 2AB\cos\theta} = \sqrt{60^2 + 80^2 + 2(60)(80)(0.50)} = \sqrt{14\,800} \approx 122\,\text{N}$.
  misconceptions:
    A: |-
      Adds the magnitudes, as if both marshals pushed in exactly the same direction. That is the answer only when the angle between them is zero.
    C: |-
      Uses Pythagoras, $\sqrt{A^2 + B^2}$, whatever the angle. That shortcut is correct only for vectors at right angles.
    D: |-
      Subtracts the magnitudes, which is correct only when the two pushes are exactly opposite.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A race circuit seen from above: cars on the straights, one car sweeping through a curved corner, and a trackside replay screen showing a car arcing over a crest](scenes/motorsport/motion_plane.svg "When a car stops on track, marshals have to move it — and the direction each of them pushes matters as much as how hard.")

Halfway through the second session of a club track day, a hatchback coughs and dies on the exit of the last corner. Yellow flags come out. Two marshals, Rehan and Ayesha, sprint across the grass to push it behind the barrier before the next group comes round.

Rehan gets behind the rear bumper and shoves straight along the track. Ayesha can't fit beside him, so she braces against the rear corner and pushes across the track, square to Rehan's push, to swing the car towards the gap in the barrier.

"I'm giving it two hundred newtons," Rehan grunts. "You?"

"About a hundred and fifty."

"Three hundred and fifty newtons on this car, then. It should be moving."

It is moving — but not the way either of them expected. So what is the combined push really worth, and which way does the car actually go?

## The physics

Forces, velocities and displacements are vectors, so you cannot add them like ordinary numbers. Direction is part of the quantity. Two equivalent rules give the sum, the **resultant** $\vec{R} = \vec{A} + \vec{B}$:

- **Triangle rule:** draw $\vec{A}$, then draw $\vec{B}$ starting from the head of $\vec{A}$. The resultant runs from the tail of $\vec{A}$ to the head of $\vec{B}$.
- **Parallelogram rule:** draw $\vec{A}$ and $\vec{B}$ from the same point, complete the parallelogram, and the diagonal from that point is $\vec{R}$.

Both give the same arrow, and the order does not matter: $\vec{A} + \vec{B} = \vec{B} + \vec{A}$.

![Left: vectors A and B drawn head to tail with R closing the triangle. Right: A and B drawn from one point, with R as the diagonal of the parallelogram](figures/vector_addition/triangle-and-parallelogram.svg "Two ways of drawing the same sum. In both, the resultant starts where A starts and ends where the chain of arrows ends.")

For two vectors of sizes $A$ and $B$ with an angle $\theta$ between them, the triangle gives (by the law of cosines)

$$R = \sqrt{A^2 + B^2 + 2AB\cos\theta}$$

and the resultant makes an angle $\alpha$ with $\vec{A}$, where

$$\tan\alpha = \frac{B\sin\theta}{A + B\cos\theta}$$

So the answer depends entirely on the angle:

- $\theta = 0^\circ$ (same direction): $R = A + B$, the largest it can ever be.
- $\theta = 90^\circ$: $R = \sqrt{A^2 + B^2}$.
- $\theta = 180^\circ$ (opposite): $R = |A - B|$, the smallest it can ever be.

![A graph of the resultant of two vectors against the angle between them, falling smoothly from their sum at 0 degrees, through the Pythagorean value at 90 degrees, to their difference at 180 degrees](figures/vector_addition/resultant-vs-angle.svg "The same two vectors can give any resultant between their difference and their sum. Only the angle decides which one you get.")

Rehan's push is $\vec{A}$ and Ayesha's is $\vec{B}$. Because she is pushing across the car, none of her effort goes along the track — which is exactly why $350\,\text{N}$ was never the right answer.

## Worked example

**Given:** Rehan pushes with $A = 200\,\text{N}$ along the track; Ayesha pushes with $B = 150\,\text{N}$ at $\theta = 90^\circ$ to his push (illustrative numbers).
**Find:** the size and direction of the combined push.

With $\cos 90^\circ = 0$, the middle term vanishes:

$$R = \sqrt{200^2 + 150^2} = \sqrt{40\,000 + 22\,500} = \sqrt{62\,500} = 250\,\text{N}$$

Direction, with $\sin 90^\circ = 1$:

$$\tan\alpha = \frac{150 \times 1}{200 + 0} = 0.75 \quad\Rightarrow\quad \alpha \approx 37^\circ$$

So the car feels a single $250\,\text{N}$ push, angled about $37^\circ$ off the track, towards Ayesha's side. Not $350\,\text{N}$, and not straight down the track either.

**Sanity check:** $250\,\text{N}$ sits between $|200 - 150| = 50\,\text{N}$ and $200 + 150 = 350\,\text{N}$, as every resultant must. The direction leans towards the bigger push, Rehan's, since $37^\circ$ is less than $45^\circ$.

## Where the picture breaks

The $250\,\text{N}$ is only the sum of the two pushes. The car also has rolling resistance, and its front wheels point somewhere, so it moves according to the *net* force and may not travel along $\vec{R}$ at all. A car is not a point either: two pushes applied at different places make it turn as well as move, which these arrows cannot show. And nobody pushes at a perfectly steady force — the formula gives the resultant at one instant.

## Key takeaway

Vectors add by the triangle (or parallelogram) rule, not by adding their sizes. For two vectors at angle $\theta$, $R = \sqrt{A^2 + B^2 + 2AB\cos\theta}$. The resultant can be anything from $|A - B|$ to $A + B$, so a $200\,\text{N}$ push and a $150\,\text{N}$ push make $350\,\text{N}$ only when both point the same way.
