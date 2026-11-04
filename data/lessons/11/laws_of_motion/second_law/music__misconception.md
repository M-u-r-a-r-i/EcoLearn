---
concept_id: second_law
interest: music
format: misconception
title: Does a bass drum fall faster than a drumstick
check:
  question: |-
    A $10\,\text{kg}$ amplifier and a $0.5\,\text{kg}$ microphone are dropped together from the edge of a stage. Ignoring air resistance, which statement is correct?
  options:
    A: |-
      They land together, because both accelerate at $g$: the amplifier's larger weight is exactly matched by its larger mass.
    B: |-
      The amplifier lands first, because it is $20$ times heavier.
    C: |-
      They land together, because gravity pulls on both with the same force.
    D: |-
      The microphone lands first, because lighter things are easier to move.
  answer: A
  explanation: |-
    The amplifier's weight is $20$ times larger, but so is its mass, so $a = mg/m = g$ for both. Equal accelerations from rest mean they land together.
  misconceptions:
    B: |-
      Believes heavier objects fall faster — true in everyday air for feathers and paper, but not caused by weight itself.
    C: |-
      Right result, wrong reason: gravity pulls $20$ times harder on the amplifier. They land together because the force and the mass grow in the same proportion.
    D: |-
      Uses "lighter is easier to accelerate" but forgets that the lighter object also has a smaller force pulling on it.
author: claude-code/opus-5
written: 2026-09-21
---
## The story

![A concert stage with a drum kit near the edge of the stage](scenes/music/laws_of_motion.svg "Two things are about to go over the edge of this stage.")

The encore ends in chaos. As the band takes a bow, the drummer's elbow knocks a drumstick off the edge of the stage — and at the very same moment the loose bass drum rolls off beside it. Both drop towards the floor, one metre below.

Everyone in the front row has a split second to guess which will land first. The guitarist, Kunal, doesn't hesitate: "The drum, obviously. It's a hundred times heavier."

The keyboard player, Sana, isn't so sure. She remembers a story about someone dropping two balls from the Leaning Tower of Pisa. Which of them is right — and why?

## The common belief

At the end of a show, a drumstick and a heavy bass drum fall off the stage together. "The drum will obviously hit the floor first," says the guitarist. "It's a hundred times heavier."

It sounds like common sense: heavy things fall faster.

## Why it feels right

Everyday experience seems to back it up. Drop a cymbal-cleaning cloth and a tuning fork and the fork lands first; a sheet of set-list paper flutters down while a phone drops like a stone. And part of the belief is genuinely true: gravity really does pull harder on the heavier object. The bass drum's weight is far larger than the drumstick's.

So if the pull is bigger, surely the fall is faster?

## What actually happens

Ignoring air resistance, the drum and the stick hit the floor **at the same moment**.

Gravity pulls harder on the drum — but the drum is also harder to accelerate, because it has more mass. The two effects cancel exactly. Newton's second law shows how: the drum's weight is many times larger than the stick's, but its mass is larger by exactly the same factor, so the acceleration — force divided by mass — comes out the same for both.

The cloth and the paper fall slowly for a different reason: **air resistance**. They are light and spread out, so the air's drag is large compared with their weight. Crumple the paper into a tight ball and it falls almost as fast as the phone. It is shape and air, not weight itself, that make the difference.

## The physics

For a falling body, the only force (ignoring air) is its weight, $W = mg$. Newton's second law, $F_\text{net} = ma$, then gives

$$a = \frac{F_\text{net}}{m} = \frac{mg}{m} = g$$

The mass cancels. Every object falling freely near the Earth's surface has the same acceleration, $g \approx 9.8\,\text{m/s}^2$, downwards.

![Two graphs: at fixed mass, acceleration rises in a straight line with force; at fixed force, acceleration falls along a curve as mass increases](figures/second_law/force-mass-acceleration.svg "The two halves of the second law. Falling objects use both at once: a heavier object has a proportionally larger force (left) and a proportionally larger mass (right), so its acceleration is unchanged.")

The misconception keeps only half of the second law — "more force, more acceleration" — and forgets the other half: "more mass, less acceleration". Here both change together.

## Worked example

A bass drum of mass $8.0\,\text{kg}$ and a drumstick of mass $0.050\,\text{kg}$ fall from a stage. Find the weight and the acceleration of each (ignore air resistance).

$$W_\text{drum} = mg = 8.0 \times 9.8 = 78.4\,\text{N}, \qquad W_\text{stick} = 0.050 \times 9.8 = 0.49\,\text{N}$$

$$a_\text{drum} = \frac{78.4}{8.0} = 9.8\,\text{m/s}^2, \qquad a_\text{stick} = \frac{0.49}{0.050} = 9.8\,\text{m/s}^2$$

The drum's weight is $160$ times larger, and so is its mass. The accelerations are identical, so released together from the same height, they land together.

## Key takeaway

Heavier objects are pulled harder by gravity, but they are also harder to accelerate — by exactly the same factor. From $F_\text{net} = ma$ with $F = mg$, every freely falling object has acceleration $g$. Differences you see in everyday falls come from air resistance, not from weight.
