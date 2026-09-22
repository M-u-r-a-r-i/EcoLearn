---
concept_id: equations_of_motion
interest: smartphones
format: explain
title: Could he have caught the falling phone
check:
  question: |-
    Om tosses his phone straight up to catch it again, releasing it at $4.2\,\text{m/s}$. Taking upwards as positive, $g = 9.8\,\text{m/s}^2$ and ignoring air resistance, how high does the phone rise above his hand?
  options:
    A: |-
      $1.8\,\text{m}$
    B: |-
      $0.43\,\text{m}$
    C: |-
      $0.90\,\text{m}$
    D: |-
      $-0.90\,\text{m}$
  answer: C
  explanation: |-
    At the top $v = 0$, and no time is given, so use $v^2 = u^2 + 2as$: $0 = 4.2^2 + 2(-9.8)s$, giving $s = 17.64/19.6 = 0.90\,\text{m}$ upwards.
  misconceptions:
    A: |-
      Drops the factor of 2 in $v^2 = u^2 + 2as$ and computes $17.64/9.8$.
    B: |-
      Computes $u/g = 0.43$ — which is the time to the top, in seconds — and reports it as a height.
    D: |-
      Takes $a = +9.8\,\text{m/s}^2$ while also taking upwards as positive, so gravity appears to point up and the height comes out negative. With upwards positive, $a = -g$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![An evening street: a phone shows a live-tracking map of a straight road, a delivery scooter rides past, and a phone slides off a café table and falls, with a green arrow for g](scenes/smartphones/motion_straight_line.svg "On the right, by a café table, a phone is on its way to the ground. Once it's let go, gravity is the only thing that matters.")

Pallavi is taking a group selfie at a café, arm stretched up, phone about $1.6\,\text{m}$ above the floor (illustrative). A waiter brushes past, her elbow jerks, and the phone slips out of her fingers.

It lands flat on the tiles with a crack. The screen protector is shattered; the screen underneath, luckily, is fine.

Her friend Jatin, standing right next to her, shakes his head. "I should have caught that. I saw it go — I had loads of time."

"Loads of time?" Pallavi says. "It was gone in a blink."

They argue about it all the way home. Jatin reckons it took a full second to fall. Pallavi thinks it was much less. Neither of them had a stopwatch running.

The only thing pulling the phone down was gravity, and gravity doesn't change over a metre and a half. So surely the fall is perfectly predictable: how long did it take, how fast was the phone going when it hit — and did Jatin really have time?

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

**Signs matter.** Choose a positive direction and give every vector — $u$, $v$, $a$, $s$ — its sign. For the falling phone, take **downwards** as positive: then $a = +g = +9.8\,\text{m/s}^2$ and $s = +1.6\,\text{m}$. The phone was let go, not thrown, so $u = 0$.

## Worked example

**Given:** $u = 0$, $a = +9.8\,\text{m/s}^2$, $s = +1.6\,\text{m}$ (downwards positive). Ignore air resistance.
**Find:** the fall time, the speed at impact, and how far the phone had fallen by the time Jatin could react, taking his reaction time as $0.25\,\text{s}$ (illustrative).

**Fall time.** Use $s = ut + \tfrac{1}{2}at^2$ with $u = 0$:

$$1.6 = \tfrac{1}{2}(9.8)t^2 \;\Rightarrow\; t = \sqrt{\frac{2(1.6)}{9.8}} = \sqrt{0.327} \approx 0.57\,\text{s}$$

**Impact speed.** Use $v^2 = u^2 + 2as$:

$$v^2 = 0 + 2(9.8)(1.6) = 31.36 \;\Rightarrow\; v = 5.6\,\text{m/s} \approx 20\,\text{km/h}$$

**After Jatin's reaction time.** $s = \tfrac{1}{2}(9.8)(0.25)^2 \approx 0.31\,\text{m}$, and $v = 9.8 \times 0.25 = 2.45\,\text{m/s}$.

So by the time Jatin's brain had said "catch it", the phone had dropped about $30\,\text{cm}$ and was moving fast, and only about $0.57 - 0.25 = 0.32\,\text{s}$ remained before it hit the tiles. Not a full second — barely a third of one. Pallavi wins.

**Sanity check:** $v = u + at = 9.8 \times 0.571 = 5.6\,\text{m/s}$, matching the third equation. And the average velocity, $1.6/0.571 = 2.8\,\text{m/s}$, is exactly half of $5.6\,\text{m/s}$ — as it must be for constant acceleration from rest.

## Where the picture breaks

The equations need a **constant** acceleration. Over a $1.6\,\text{m}$ fall, gravity is constant and air resistance on a compact, fairly heavy phone is tiny, so "ignore air" is a good approximation here — but it would not be for a sheet of paper, or for a phone falling from a tall building, where drag grows with speed. The phone also tumbles as it falls, which doesn't change the motion of its centre much but decides which face hits first. And the equations stop at the moment of impact: the few milliseconds of crashing to a halt on the tiles involve a huge, rapidly changing acceleration that no constant-$a$ equation describes.

## Key takeaway

For constant acceleration in a straight line, $v = u + at$, $s = ut + \tfrac{1}{2}at^2$ and $v^2 = u^2 + 2as$. Choose a positive direction, sign every vector, and pick the equation that contains what you know and what you want. A phone dropped from $1.6\,\text{m}$ hits the floor in under $0.6\,\text{s}$, at about $5.6\,\text{m/s}$.
