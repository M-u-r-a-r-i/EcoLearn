---
concept_id: relative_velocity_2d
interest: cricket
format: explain
title: Why straight-down rain hits a running batter in the face
check:
  question: |-
    A fielder runs east along the boundary at $6\,\text{m/s}$. A ball rolls north across the grass towards the rope at $8\,\text{m/s}$. What is the velocity of the ball relative to the fielder?
  options:
    A: |-
      $14\,\text{m/s}$
    B: |-
      $2\,\text{m/s}$
    C: |-
      $10\,\text{m/s}$, pointing $37^\circ$ west of north
    D: |-
      $10\,\text{m/s}$, pointing $37^\circ$ east of north
  answer: C
  explanation: |-
    $\vec{v}_{\text{ball, fielder}} = \vec{v}_\text{ball} - \vec{v}_\text{fielder} = 8\hat{j} - 6\hat{i}$, with $\hat{i}$ east and $\hat{j}$ north. Its size is $\sqrt{6^2 + 8^2} = 10\,\text{m/s}$, at $\tan^{-1}(6/8) \approx 37^\circ$ west of north.
  misconceptions:
    A: |-
      Adds the two speeds as numbers, as if the velocities were in the same line. They are at right angles, so their directions must be included.
    B: |-
      Subtracts the speeds as numbers, as if the ball and fielder moved along the same line. Relative velocity subtracts vectors, not sizes.
    D: |-
      Adds the fielder's velocity instead of subtracting it. The fielder is moving east, so to him the ball drifts west.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A day match: a batter lofts the ball towards the boundary as a fielder races along the rope](scenes/cricket/motion_plane.svg "The same field looks different depending on who is moving across it.")

Dark clouds, then the first heavy drops. The umpires signal, and everyone heads for the pavilion. There is no wind at all; from the dressing-room balcony, the rain is falling straight down like a curtain of lines.

Aditi, who was batting, sprints off to save her gloves and bat from a soaking. Halfway there, she notices something odd. The rain isn't landing on the top of her helmet. It's hitting her face and the front of her shirt, as if it were blowing towards her.

Her batting partner, Rukhsar, walks off slowly behind her and says the rain feels almost straight down to her.

It's the same rain, falling the same way, at the same moment. Why does it come at Aditi on a slant, and why does the slant depend on how fast you move?

## The physics

The velocity you measure depends on who is measuring. The **relative velocity** of A with respect to B is the velocity A seems to have to an observer moving along with B:

$$\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$$

Both $\vec{v}_A$ and $\vec{v}_B$ are measured relative to the ground. In one dimension this was ordinary subtraction. In a plane it is **vector** subtraction: add $-\vec{v}_B$ to $\vec{v}_A$ by the triangle rule, or subtract component by component. Note that $\vec{v}_{BA} = -\vec{v}_{AB}$: each sees the other moving the opposite way.

![Left: A moves straight down and observer B moves right. Right: v_A drawn down, then minus v_B drawn to the left, giving v_AB slanting down and backwards](figures/relative_velocity_2d/subtracting-velocities.svg "To find how A looks to B, add minus v_B to v_A. The result slants back towards B and is faster than either motion alone.")

For Aditi, A is the rain and B is Aditi. Take $\hat{i}$ in the direction she runs and $\hat{j}$ vertically up. The rain falls straight down, $\vec{v}_R = -v_R\,\hat{j}$, and she runs forward, $\vec{v}_A = v\,\hat{i}$. So, relative to her,

$$\vec{v}_{RA} = \vec{v}_R - \vec{v}_A = -v\,\hat{i} - v_R\,\hat{j}$$

The $-v\,\hat{i}$ part means that, to Aditi, the rain also moves *backwards*, towards her, which is why it lands on her front. The angle from the vertical satisfies $\tan\theta = v/v_R$: run faster and the slant gets steeper. Rukhsar, walking slowly, has a small $v$, so the rain looks almost vertical to her.

## Worked example

**Given:** rain falls vertically at $8.0\,\text{m/s}$ (illustrative; raindrops fall at a few metres per second). Aditi runs horizontally at $6.0\,\text{m/s}$; Rukhsar walks at $1.5\,\text{m/s}$.
**Find:** the rain's velocity relative to Aditi, and its angle from the vertical for both players.

$$\vec{v}_{RA} = (0 - 6.0)\hat{i} + (-8.0 - 0)\hat{j} = (-6.0\hat{i} - 8.0\hat{j})\,\text{m/s}$$

$$|\vec{v}_{RA}| = \sqrt{6.0^2 + 8.0^2} = \sqrt{100} = 10\,\text{m/s}$$

$$\tan\theta = \frac{6.0}{8.0} = 0.75 \quad\Rightarrow\quad \theta \approx 37^\circ \text{ from the vertical, coming from in front}$$

For Rukhsar: $\tan\theta = 1.5/8.0 \approx 0.19$, so $\theta \approx 11^\circ$. Nearly straight down, as she said.

**Sanity check:** the relative speed ($10\,\text{m/s}$) is larger than either speed alone, as it should be for velocities at right angles. If Aditi stood still ($v = 0$), $\theta = 0$ and the rain would be vertical again.

## Where the picture breaks

We assumed every drop falls at the same steady speed with no wind. Real drops come in many sizes, and bigger drops fall faster, so the slant is really a spread of angles. Any wind adds its own velocity to the rain. Aditi also doesn't run at a constant speed: she accelerates away from the crease, so the slant she sees changes during the run. The subtraction rule itself is exact for everyday speeds; it needs correcting only near the speed of light.

## Key takeaway

The velocity of A relative to B is $\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$, a vector subtraction. Your own motion adds a backwards part to everything you watch. That is why vertical rain slants into a runner's face at $\tan\theta = v/v_R$, and why the slant grows the faster you run.
