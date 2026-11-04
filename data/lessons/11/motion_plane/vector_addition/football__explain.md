---
concept_id: vector_addition
interest: football
format: explain
title: Why a 40-metre run plus a 30-metre run isn't 70 metres from home
check:
  question: |-
    A full-back runs $30\,\text{m}$ up the touchline, then turns $60^\circ$ towards the middle of the pitch and runs another $20\,\text{m}$ in a straight line. How far is she from where she started?
  options:
    A: |-
      $50\,\text{m}$
    B: |-
      About $43.6\,\text{m}$
    C: |-
      About $36.1\,\text{m}$
    D: |-
      $10\,\text{m}$
  answer: B
  explanation: |-
    The angle between the two displacements is $60^\circ$, so $R = \sqrt{30^2 + 20^2 + 2(30)(20)\cos 60^\circ} = \sqrt{900 + 400 + 600} = \sqrt{1900} \approx 43.6\,\text{m}$.
  misconceptions:
    A: |-
      Adds the two lengths as plain numbers, as if both runs were in the same direction. That is true only when the angle between them is zero.
    C: |-
      Uses Pythagoras, $\sqrt{A^2 + B^2}$, whatever the angle. That shortcut works only when the two displacements are at right angles.
    D: |-
      Subtracts the lengths, which is correct only when the second run goes straight back the way the first one came.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A player lofts the ball in an arc over the goalkeeper while a teammate jogs round the centre circle](scenes/football/motion_plane.svg "Players rarely run in one straight line for long. Every change of direction changes where they end up.")

Kavya plays on the left wing for her district under-17 side. In the second half she makes the run of the match: $40$ metres flat out up the touchline, then a sharp cut inside, another $30$ metres towards the penalty area, and a shot that hits the post.

In the dressing room she is still breathing hard. "Seventy metres at full sprint," she tells her coach, Mr Fernandes. "That's why I snatched at the shot."

"You certainly ran seventy," he says, looking at the tracking sheet. "But you finished only fifty metres from where you started the run."

"That can't be right," says Kavya. "Forty and thirty is seventy."

For lengths of running, it is. So why isn't it for where she ended up, and what decides the fifty?

## The physics

Displacements, velocities and forces are vectors, so they don't add like plain numbers: the direction matters. Two rules give the sum, called the **resultant** $\vec{R} = \vec{A} + \vec{B}$:

- **Triangle rule:** draw $\vec{A}$, then draw $\vec{B}$ starting from the head of $\vec{A}$. The resultant runs from the tail of $\vec{A}$ to the head of $\vec{B}$.
- **Parallelogram rule:** draw $\vec{A}$ and $\vec{B}$ from the same point, complete the parallelogram, and $\vec{R}$ is the diagonal from that point.

Both rules give the same arrow, and the order doesn't matter: $\vec{A} + \vec{B} = \vec{B} + \vec{A}$.

![Left: A and B drawn head to tail with R closing the triangle. Right: A and B drawn from one point, with R as the parallelogram's diagonal](figures/vector_addition/triangle-and-parallelogram.svg "Two ways to draw the same sum. The resultant starts where A starts and ends where the chain of arrows ends.")

Kavya's run is the triangle rule acted out on grass. Her first leg is $\vec{A}$ ($40\,\text{m}$ up the line), her second is $\vec{B}$ ($30\,\text{m}$ infield), drawn head to tail, and her final displacement is the third side of the triangle.

For two vectors of sizes $A$ and $B$ with an angle $\theta$ between their directions, the law of cosines gives

$$R = \sqrt{A^2 + B^2 + 2AB\cos\theta}$$

and $\vec{R}$ makes an angle $\alpha$ with $\vec{A}$, where

$$\tan\alpha = \frac{B\sin\theta}{A + B\cos\theta}$$

Here $\theta$ is the angle she turns through at the corner. The resultant depends on it:

- $\theta = 0^\circ$ (no turn): $R = A + B$, the largest possible.
- $\theta = 90^\circ$ (a right-angle cut): $R = \sqrt{A^2 + B^2}$.
- $\theta = 180^\circ$ (straight back): $R = |A - B|$, the smallest possible.

![A graph of the resultant of vectors of sizes 3 and 4 against the angle between them, falling from 7 at 0 degrees through 5 at 90 degrees to 1 at 180 degrees](figures/vector_addition/resultant-vs-angle.svg "The same two vectors can give any resultant from their difference to their sum. Only the angle between them decides which.")

## Worked example

**Given (illustrative):** $A = 40\,\text{m}$ up the touchline, then $B = 30\,\text{m}$ after a cut of $\theta = 90^\circ$ towards the middle.
**Find:** the size and direction of Kavya's displacement.

With $\cos 90^\circ = 0$:
$$R = \sqrt{40^2 + 30^2} = \sqrt{1600 + 900} = \sqrt{2500} = 50\,\text{m}$$

Direction, with $\sin 90^\circ = 1$:
$$\tan\alpha = \frac{30 \times 1}{40 + 0} = 0.75 \quad\Rightarrow\quad \alpha \approx 37^\circ$$

She ends $50\,\text{m}$ from her starting spot, along a line $37^\circ$ infield from the touchline.

**Sanity check:** $50\,\text{m}$ lies between $|40 - 30| = 10\,\text{m}$ and $40 + 30 = 70\,\text{m}$. The direction leans towards the longer leg (the touchline), since $37^\circ < 45^\circ$.

## Where the picture breaks

A real cut inside is a curve, not a sharp corner, so Kavya's path is slightly shorter than $70\,\text{m}$. Her displacement, though, depends only on her start and end points, so the triangle still gives it exactly. The formula needs $\theta$ to be the angle between the two arrows when they are drawn *tail to tail*, which here equals the turn at the corner. Using the inside angle of the triangle instead (here also $90^\circ$, but not in general) is a common slip.

## Key takeaway

Vectors add by the triangle or parallelogram rule, not by adding their sizes. For two vectors at angle $\theta$, $R = \sqrt{A^2 + B^2 + 2AB\cos\theta}$. The result can be anything from $|A - B|$ to $A + B$, so $40\,\text{m}$ plus $30\,\text{m}$ makes $70\,\text{m}$ only when both point the same way.
