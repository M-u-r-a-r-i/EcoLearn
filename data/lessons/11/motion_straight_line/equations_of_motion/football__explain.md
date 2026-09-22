---
concept_id: equations_of_motion
interest: football
format: explain
title: Will the through ball die before the goal line
check:
  question: |-
    A pass leaves a midfielder's boot along the grass at $10\,\text{m/s}$ and slows uniformly to $4.0\,\text{m/s}$ over $21\,\text{m}$. Taking the direction of the pass as positive, what is the ball's acceleration?
  options:
    A: |-
      $-4.0\,\text{m/s}^2$
    B: |-
      $-2.0\,\text{m/s}^2$
    C: |-
      $+2.0\,\text{m/s}^2$
    D: |-
      $-0.29\,\text{m/s}^2$
  answer: B
  explanation: |-
    No time is given, so use $v^2 = u^2 + 2as$: $4.0^2 = 10^2 + 2a(21)$, so $a = (16 - 100)/42 = -2.0\,\text{m/s}^2$. It is negative because it points opposite to the ball's motion.
  misconceptions:
    A: |-
      Drops the factor of 2 in $v^2 = u^2 + 2as$ and computes $-84/21$.
    C: |-
      Gets the right size but ignores the sign convention. A ball slowing down while moving in the positive direction has a negative acceleration.
    D: |-
      Divides the change in speed by the distance, $(4.0 - 10)/21$, treating it like $a = \Delta v/\Delta t$ with a distance in place of the time. The units come out as $\text{s}^{-1}$, not $\text{m/s}^2$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A winger dribbles along the touchline towards goal, chased by a defender, while the goalkeeper comes off the line; a number line with origin O and +x runs beneath](scenes/football/motion_straight_line.svg "A ball rolling along the grass slows steadily — and the whole pitch is waiting to see where it stops.")

Last minute, one goal down. Tara, the team's playmaker, spots her striker Manav making a run and slides a through ball along the grass, about $45\,\text{m}$ from the opponents' goal line.

The opposition keeper, Hamza, takes one look and stays on his line. "Leave it! It's too heavy — it'll run out for a goal kick!"

Manav thinks the opposite. "It's slowing down, it'll hold up for me!"

On the bench, Tara's friend Pooja is doing sums. The pass left Tara's boot at about $12\,\text{m/s}$, and on this dry grass a rolling ball loses speed at a fairly steady rate — about $1.5\,\text{m/s}$ every second (illustrative). If that's true, the whole future of the ball is fixed the instant it's kicked.

Does it reach the goal line, or stop short? If it gets there, how fast will it be going — and how many seconds does Manav have?

## The physics

When an object moves along a straight line with **constant acceleration** $a$, three equations connect the initial velocity $u$, final velocity $v$, displacement $s$ and time $t$:

$$v = u + at$$
$$s = ut + \tfrac{1}{2}at^2$$
$$v^2 = u^2 + 2as$$

Each equation leaves out one quantity: the first has no $s$, the second no $v$, the third no $t$. Pick the one that contains the three quantities you know and the one you want.

Where they come from:

- **$v = u + at$** is the definition of acceleration, $a = (v - u)/t$, rearranged — valid only if $a$ is constant.
- **$s = ut + \tfrac{1}{2}at^2$** is the area under the straight $v$–$t$ line: a rectangle $ut$ plus a triangle $\tfrac{1}{2}t(at)$.
- **$v^2 = u^2 + 2as$** comes from eliminating $t$ between the first two.

![A velocity–time graph rising in a straight line from 2 m/s to 8 m/s over 4 s, with the area below split into a rectangle of area ut = 8 m and a triangle of area ½at² = 12 m](figures/equations_of_motion/vt-area-derivation.svg "The displacement is the area under the line: rectangle plus triangle, 8 m + 12 m = 20 m.")

**Signs matter.** Choose a positive direction and give every vector — $u$, $v$, $a$, $s$ — its sign. For Tara's pass, take the direction of the pass as positive: $u = +12\,\text{m/s}$, and because the ball slows, $a = -1.5\,\text{m/s}^2$.

## Worked example

**Given:** $u = +12\,\text{m/s}$, $a = -1.5\,\text{m/s}^2$ (constant), goal line $45\,\text{m}$ ahead.
**Find:** where the ball would stop, its speed at the goal line, and the time to get there.

**Stopping distance.** At a stop $v = 0$; no time is known, so use $v^2 = u^2 + 2as$:

$$0 = 12^2 + 2(-1.5)s \;\Rightarrow\; s = \frac{144}{3.0} = 48\,\text{m}$$

That is beyond $45\,\text{m}$, so the ball does reach the goal line. Hamza was right.

**Speed at the goal line.** Again $v^2 = u^2 + 2as$, with $s = 45\,\text{m}$:

$$v^2 = 144 - 2(1.5)(45) = 144 - 135 = 9 \;\Rightarrow\; v = 3.0\,\text{m/s}$$

**Time to the line.** Now use $v = u + at$:

$$3.0 = 12 - 1.5t \;\Rightarrow\; t = \frac{9.0}{1.5} = 6.0\,\text{s}$$

Manav has $6.0\,\text{s}$ to catch a ball that is creeping along at the end.

**Sanity check:** the second equation, which we haven't used yet, must agree: $s = 12(6.0) - \tfrac{1}{2}(1.5)(6.0)^2 = 72 - 27 = 45\,\text{m}$. It does.

## Where the picture breaks

The equations need a **constant** acceleration, and a rolling ball's slowing is only roughly constant: it depends on the grass length, dampness and any bounce or spin, and at higher speeds air drag adds to it. So $48\,\text{m}$ is an estimate, not a promise. The maths also doesn't know that a ball can't roll backwards on its own: $s = ut + \tfrac{1}{2}at^2$ says the ball returns towards Tara after $t = 8\,\text{s}$ ($u/|a|$), but in reality it simply stops then. Always check that an answer lies in the time range where your constant-acceleration model holds.

## Key takeaway

For constant acceleration in a straight line, $v = u + at$, $s = ut + \tfrac{1}{2}at^2$ and $v^2 = u^2 + 2as$. Choose a positive direction, sign every vector, and pick the equation that contains what you know and what you want. Tara's $12\,\text{m/s}$ pass would roll $48\,\text{m}$ — just enough to cross the line at $45$.
