---
concept_id: equations_of_motion
interest: cricket
format: explain
title: How long does a skied catch give you
check:
  question: |-
    A fielder sprinting at $6.0\,\text{m/s}$ slows down uniformly and stops in $3.0\,\text{m}$ just inside the rope. Taking her direction of motion as positive, what is her acceleration?
  options:
    A: |-
      $-12\,\text{m/s}^2$
    B: |-
      $-2.0\,\text{m/s}^2$
    C: |-
      $+6.0\,\text{m/s}^2$
    D: |-
      $-6.0\,\text{m/s}^2$
  answer: D
  explanation: |-
    No time is given, so use $v^2 = u^2 + 2as$: $0 = 6.0^2 + 2a(3.0)$, so $a = -36/6.0 = -6.0\,\text{m/s}^2$. It is negative because it points opposite to her motion.
  misconceptions:
    A: |-
      Drops the factor of 2 in $v^2 = u^2 + 2as$ and computes $36/3.0$.
    B: |-
      Divides the speed by the stopping distance ($6.0/3.0$), treating it like $a = \Delta v/\Delta t$ with a distance in place of the time. The units come out as $\text{s}^{-1}$, not $\text{m/s}^2$.
    C: |-
      Gets the right size but ignores the sign convention. Slowing down while moving in the positive direction needs a negative acceleration.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground in sunshine: a batter runs between the wickets on a 22-yard pitch while a fielder chases the ball towards the boundary rope](scenes/cricket/motion_straight_line.svg "Most of cricket's motion runs along the ground. A skier goes straight up the other line: the vertical.")

Final over, six runs needed, and the batter goes for a huge hit. He gets a thick top edge and the ball climbs almost straight up into the evening sky.

"Harpreet! Yours!" shouts the whole team.

Harpreet, the captain, is at mid-on — about $20\,\text{m}$ from where the ball will come down. She has a split second to decide: sprint in and try to take it herself, or call the wicketkeeper, who is closer but has pads and gloves on and may struggle to run.

From the dugout, her younger brother Gurpreet is doing sums in his head. The edge sent the ball up at maybe $24.5\,\text{m/s}$ (illustrative — a speed gun wouldn't be pointed at a skier). How high will it go? How long before it comes back down? Is that long enough to run $20\,\text{m}$?

The only force that matters is gravity, and it never changes. Surely that makes this predictable?

## The physics

When an object moves along a straight line with **constant acceleration** $a$, three equations connect the initial velocity $u$, final velocity $v$, displacement $s$, and time $t$:

$$v = u + at$$
$$s = ut + \tfrac{1}{2}at^2$$
$$v^2 = u^2 + 2as$$

Each equation leaves out one quantity: the first has no $s$, the second no $v$, the third no $t$. Pick the one that contains the three quantities you know and the one you want.

Where they come from:

- **$v = u + at$** is the definition of acceleration, $a = (v - u)/t$, rearranged — valid only if $a$ is constant.
- **$s = ut + \tfrac{1}{2}at^2$** is the area under the straight $v$–$t$ line: a rectangle $ut$ plus a triangle $\tfrac{1}{2}t(at)$.
- **$v^2 = u^2 + 2as$** comes from eliminating $t$ between the first two.

![A velocity–time graph rising in a straight line from 2 m/s to 8 m/s over 4 s, with the area below split into a rectangle of area ut = 8 m and a triangle of area ½at² = 12 m](figures/equations_of_motion/vt-area-derivation.svg "The displacement is the area under the line: rectangle plus triangle, 8 m + 12 m = 20 m.")

**Signs matter.** Choose a positive direction and give every vector — $u$, $v$, $a$, $s$ — its sign. For a ball thrown straight up, take upward as positive: gravity then gives $a = -g = -9.8\,\text{m/s}^2$, all the way up *and* all the way down.

## Worked example

**Given:** $u = +24.5\,\text{m/s}$ (upward positive), $a = -9.8\,\text{m/s}^2$. Ignore air resistance.
**Find:** the time to the top, the maximum height, and the time until it's back at the height it was hit from.

**Time to the top.** At the top, $v = 0$. Use $v = u + at$:

$$0 = 24.5 - 9.8t \;\Rightarrow\; t = \frac{24.5}{9.8} = 2.5\,\text{s}$$

**Maximum height.** Use $v^2 = u^2 + 2as$ with $v = 0$:

$$0 = 24.5^2 - 2(9.8)s \;\Rightarrow\; s = \frac{600.25}{19.6} \approx 30.6\,\text{m}$$

**Back down to launch height.** Now $s = 0$. Use $s = ut + \tfrac{1}{2}at^2$:

$$0 = 24.5t - 4.9t^2 = t(24.5 - 4.9t) \;\Rightarrow\; t = 0 \text{ or } t = 5.0\,\text{s}$$

Harpreet has about $5\,\text{s}$ to cover $20\,\text{m}$ — an average of just $4\,\text{m/s}$. She should take it.

**Sanity check:** the flight is symmetric, so $5.0\,\text{s}$ is twice the $2.5\,\text{s}$ to the top. And $s = 24.5(2.5) - 4.9(2.5)^2 = 61.25 - 30.625 \approx 30.6\,\text{m}$ agrees with the height from the third equation.

## Where the picture breaks

The equations need a **constant** acceleration. Gravity near the ground is constant, but air resistance isn't zero: at $24.5\,\text{m/s}$ a cricket ball feels a noticeable drag, which grows with speed. A real skier therefore climbs less than $30.6\,\text{m}$ and spends a little less time in the air, and its fall is slightly slower than its rise. A top-edged ball also spins and rarely goes exactly vertical, so it drifts sideways — which is exactly what makes skiers hard to judge. And a catch is taken at hand height, which is not exactly the height the ball left the bat, so the true time differs slightly from $5.0\,\text{s}$.

## Key takeaway

For constant acceleration in a straight line, $v = u + at$, $s = ut + \tfrac{1}{2}at^2$ and $v^2 = u^2 + 2as$. Choose a positive direction, sign every vector, and pick the equation that contains what you know and what you want. A skier hit up at $24.5\,\text{m/s}$ gives a fielder about $5$ seconds.
