---
concept_id: free_body_diagrams
interest: gaming
format: explain
title: Why the crane cable snapped in the puzzle level
check:
  question: |-
    In a puzzle game with realistic physics, a $20\,\text{kg}$ lantern hangs at rest from a cable that makes $30^\circ$ with the vertical, held aside by a horizontal rope. Taking $g = 9.8\,\text{m/s}^2$, what is the tension in the angled cable?
  options:
    A: |-
      $196\,\text{N}$
    B: |-
      $113\,\text{N}$
    C: |-
      $98\,\text{N}$
    D: |-
      $226\,\text{N}$
  answer: D
  explanation: |-
    Vertically, only the cable's vertical component holds up the weight: $T\cos 30^\circ = mg = 196\,\text{N}$, so $T = \dfrac{196}{0.866} \approx 226\,\text{N}$.
  misconceptions:
    A: |-
      Assumes the supporting cable carries exactly the weight. Only its vertical component balances the weight; the full tension must be larger when the cable is slanted.
    B: |-
      Finds the horizontal rope's tension, $mg\tan 30^\circ \approx 113\,\text{N}$, instead of the angled cable's.
    C: |-
      Uses $mg\sin 30^\circ$, mixing up which component of the tension is vertical. With the angle measured from the vertical, the vertical component is $T\cos 30^\circ$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a racing game on the monitor and a zero-gravity game on a tablet](scenes/gaming/laws_of_motion.svg "Physics puzzle games live or die by getting forces right, and so do the levels players build in them.")

Nisha is building her first level in a physics-puzzle game. The centrepiece is a wrecking ball hanging from a crane by a steel cable. A second cable, horizontal, pulls the ball aside and ties it to a peg, so that the cable from the crane hangs at an angle. When the player cuts the horizontal cable, the ball swings and smashes the wall.

Every cable in the game has a strength. Nisha checks the ball's weight in the editor, then picks a crane cable rated a little above it. "Easy," she tells her friend Yash. "The crane cable holds the ball up, so it carries the ball's weight. Anything stronger than that is safe."

She presses *Play*. Before the player has touched anything, before the ball has moved a centimetre, the crane cable snaps and the ball crashes to the floor.

"Your game's broken," says Yash.

Nisha doesn't think so. Something in her numbers is wrong. But the ball was just hanging there. Where did the extra force come from?

## The physics

To find forces on a body at rest, draw a **free-body diagram**: a sketch of **one** body, on its own, with an arrow for every force acting **on** it.

1. **Isolate the body.** Draw the wrecking ball alone, as a dot or a simple shape.
2. **Add every force on it, from other bodies:** its weight $W = mg$ (by the Earth), the tension $T$ along the crane cable, the pull $F$ along the horizontal cable. Nothing else touches it.
3. **Leave out** forces the ball exerts on other things (its pull on the cables) and anything that isn't a force, like velocity. Those belong on other diagrams, or on none.
4. **Choose axes and resolve** any slanted force into components.

A body stays at rest only if the net force on it is zero. For forces that all act at one point (**concurrent forces**), that means the components balance separately:

$$\sum F_x = 0 \qquad \sum F_y = 0$$

![Left: a ball hanging from a beam on a cord at 30 degrees to the vertical, held aside by a horizontal string to a spring balance. Right: its free-body diagram with tension T up and to the left along the cord, weight W down and pull F to the right, with T's components T cos 30 degrees and T sin 30 degrees dashed](figures/free_body_diagrams/ball-held-aside-fbd.svg "Nisha's level in miniature: the cord is the crane cable, the horizontal string is the tie to the peg. The dashed parts of T are what balance W and F.")

With the crane cable at angle $\theta$ to the vertical, its tension has a vertical component $T\cos\theta$ and a horizontal component $T\sin\theta$. Only the **vertical** component holds the ball up:

$$T\cos\theta = W \quad\Rightarrow\quad T = \frac{W}{\cos\theta}$$

Since $\cos\theta < 1$ for any slant, $T$ is **bigger** than the weight. The rest of the tension is spent pulling sideways against the horizontal cable. That was Nisha's missing force.

## Worked example

**Given (illustrative values):** wrecking ball $m = 50\,\text{kg}$; crane cable at $30^\circ$ to the vertical; horizontal tie cable; $g = 9.8\,\text{m/s}^2$. Nisha's crane cable is rated at $550\,\text{N}$.
**Find:** the tension in each cable, and whether the crane cable survives.

*Weight:* $W = mg = 50 \times 9.8 = 490\,\text{N}$, downwards.

*Vertical balance:* $T\cos 30^\circ = 490$, so

$$T = \frac{490}{0.866} \approx 566\,\text{N}$$

*Horizontal balance:* $F = T\sin 30^\circ = 566 \times 0.5 \approx 283\,\text{N}$.

The crane cable needs $566\,\text{N}$, more than its $550\,\text{N}$ rating, so it snaps, exactly as in the game.

**Sanity check:** dividing the two balance equations gives $F = W\tan 30^\circ = 490 \times 0.577 \approx 283\,\text{N}$ ✓. Limiting cases: at $\theta = 0$ the cable hangs straight, $T = W$ and $F = 0$; as $\theta$ approaches $90^\circ$, $\cos\theta \to 0$ and $T$ grows without limit, which is why no cable can hold a weight perfectly sideways.

## Where the picture breaks

We treated the ball as a point, so all three forces meet at one place; for a real extended body, you'd also need the forces not to twist it, which is rotational equilibrium, coming later. Real cables have mass and sag, so their tension isn't quite the same everywhere, and they stretch a little under load. A game may also have its own rules for breaking cables, such as a safety margin or a random factor. The method, one body, all forces on it, balance the components, doesn't change.

## Key takeaway

A free-body diagram shows one body and every force acting on it, nothing else. For a body in equilibrium under concurrent forces, the components balance separately: $\sum F_x = 0$ and $\sum F_y = 0$. A slanted support carries more than the weight it holds up, $T = W/\cos\theta$, because only part of its pull is vertical.
