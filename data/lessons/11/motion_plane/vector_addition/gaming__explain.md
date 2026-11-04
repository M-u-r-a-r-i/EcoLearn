---
concept_id: vector_addition
interest: gaming
format: explain
title: Two ropes, one stone block and a co-op puzzle
check:
  question: |-
    In a co-op game, two characters pull a block along the floor with ropes: one with $300\,\text{N}$ due east, the other with $400\,\text{N}$ due north. Ignoring every other force, what is the size of their combined pull?
  options:
    A: |-
      $700\,\text{N}$
    B: |-
      $100\,\text{N}$
    C: |-
      $2.5 \times 10^5\,\text{N}$
    D: |-
      $500\,\text{N}$
  answer: D
  explanation: |-
    The pulls are at right angles, so the triangle of forces is right-angled and $R = \sqrt{300^2 + 400^2} = \sqrt{250\,000} = 500\,\text{N}$, pointing between east and north.
  misconceptions:
    A: |-
      Adds the magnitudes as if they were scalars. That is only right when both pulls point the same way; at right angles part of each pull is "spent" in a different direction.
    B: |-
      Subtracts the magnitudes. That gives the resultant only when the pulls point in opposite directions, not at right angles.
    C: |-
      Uses Pythagoras but forgets the square root, so gets $R^2$ instead of $R$. The units ($\text{N}^2$) would show the slip.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: the monitor shows an artillery game with a shell flying along a curved arc; a tablet shows a top-down minimap of a circular kart track](scenes/gaming/motion_plane.svg "In a game world, pushes, pulls and velocities all come with directions, and the engine has to combine them.")

Arjun and Sneha are stuck on level 7 of a co-op puzzle game. A huge stone block has to be dragged onto a pressure plate, and each of their characters can grab a rope tied to it. The game shows each pull on screen: Arjun's character hauls with $400$ units, Sneha's with $300$.

The pressure plate is in a corner, so Arjun pulls towards the far wall and Sneha pulls along the side wall. The block slides diagonally, and much more slowly than they expected.

"That's 700 units of pull," says Arjun. "It should fly."

Sneha tries something else: she walks round until her rope lines up with his. Now the block shoots off, straight at the wall. Then, messing about, she pulls the opposite way to him, and the block barely creeps.

Same two characters, same two pulls. So how strong is their combined pull, and why does it keep changing?

## The physics

Scalars add like numbers. Vectors don't: when you add two vectors, their **directions** matter as much as their sizes. The single vector that has the same effect as both together is the **resultant**, $\vec{R} = \vec{A} + \vec{B}$.

**Triangle law.** Draw $\vec{A}$. Put the tail of $\vec{B}$ at the head of $\vec{A}$. The resultant runs from the tail of $\vec{A}$ to the head of $\vec{B}$, closing the triangle.

**Parallelogram law.** Draw $\vec{A}$ and $\vec{B}$ from the same point and complete the parallelogram. The resultant is the diagonal from that point. It is the same arrow as the triangle law gives.

![Left: A and B drawn head to tail with R closing the triangle. Right: A and B drawn from one point, with R as the parallelogram's diagonal](figures/vector_addition/triangle-and-parallelogram.svg "Two ways to draw the same sum. In both, the resultant starts where A starts and ends where the chain of arrows ends.")

For vectors of sizes $A$ and $B$ with an angle $\theta$ between them (drawn tail to tail), the geometry of the parallelogram gives

$$R = \sqrt{A^2 + B^2 + 2AB\cos\theta}, \qquad \tan\beta = \frac{B\sin\theta}{A + B\cos\theta}$$

where $\beta$ is the angle between $\vec{R}$ and $\vec{A}$. Vector addition is commutative, $\vec{A} + \vec{B} = \vec{B} + \vec{A}$.

Now Arjun and Sneha's puzzle is clear. Pulling the same way ($\theta = 0$), $\cos\theta = 1$ and $R = A + B = 700$. Pulling at right angles ($\theta = 90^\circ$), $R = \sqrt{300^2 + 400^2} = 500$. Pulling in opposite directions ($\theta = 180^\circ$), $R = A - B$ in size, just $100$.

![A graph of the resultant of vectors of sizes 3 and 4 against the angle between them, falling from 7 at 0 degrees through 5 at 90 degrees to 1 at 180 degrees](figures/vector_addition/resultant-vs-angle.svg "Multiply every number by 100 and this is the block puzzle. The same two pulls give anything from their difference to their sum; only the angle decides which.")

## Worked example

**Given (illustrative):** Arjun pulls with $A = 400\,\text{N}$ and Sneha with $B = 300\,\text{N}$, with $\theta = 60^\circ$ between the ropes.
**Find:** the size and direction of the resultant pull.

Use the parallelogram formula, since the ropes are neither parallel nor at right angles:
$$R = \sqrt{400^2 + 300^2 + 2(400)(300)\cos 60^\circ} = \sqrt{160\,000 + 90\,000 + 120\,000} = \sqrt{370\,000} \approx 608\,\text{N}$$

Direction, measured from Arjun's rope:
$$\tan\beta = \frac{300\sin 60^\circ}{400 + 300\cos 60^\circ} = \frac{259.8}{550} = 0.472 \;\Rightarrow\; \beta \approx 25^\circ$$

So the block is pulled with about $610\,\text{N}$, $25^\circ$ from Arjun's rope towards Sneha's.

**Sanity check:** $608\,\text{N}$ lies between $500\,\text{N}$ (at $90^\circ$) and $700\,\text{N}$ (at $0^\circ$), as it should for $60^\circ$. The resultant leans towards the larger pull: $25^\circ$ is less than half of $60^\circ$.

## Where the picture breaks

A real block on a stone floor also feels friction, its weight and the floor's push, so how fast it moves depends on all of those, not just the rope pulls. Game engines often simplify friction or tune it for fun, so a block's speed is a poor measure of the net force. The game's "units" of pull may not be newtons at all. And we treated both ropes as horizontal; a rope angled upwards would also lift slightly on the block. What does carry over exactly is the rule the engine itself uses: forces are added as vectors, head to tail.

## Key takeaway

Vectors add by the triangle (or parallelogram) law, not like ordinary numbers: $R = \sqrt{A^2 + B^2 + 2AB\cos\theta}$. The resultant can be anything from $|A - B|$ (opposite directions) to $A + B$ (same direction), and at right angles it is $\sqrt{A^2 + B^2}$. The angle between the vectors decides where in that range it falls.
