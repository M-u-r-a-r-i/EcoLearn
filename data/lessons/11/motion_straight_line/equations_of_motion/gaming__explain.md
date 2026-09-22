---
concept_id: equations_of_motion
interest: gaming
format: explain
title: Can the hero reach the ledge with real gravity
check:
  question: |-
    In a racing game, a kart moving at $20\,\text{m/s}$ brakes uniformly and stops in $25\,\text{m}$. Taking its direction of motion as positive, what is its acceleration?
  options:
    A: |-
      $-16\,\text{m/s}^2$
    B: |-
      $-8.0\,\text{m/s}^2$
    C: |-
      $+8.0\,\text{m/s}^2$
    D: |-
      $-0.80\,\text{m/s}^2$
  answer: B
  explanation: |-
    No time is given, so use $v^2 = u^2 + 2as$: $0 = 20^2 + 2a(25)$, so $a = -400/50 = -8.0\,\text{m/s}^2$. It is negative because it points opposite to the kart's motion.
  misconceptions:
    A: |-
      Drops the factor of 2 in $v^2 = u^2 + 2as$ and computes $400/25$.
    C: |-
      Gets the right size but ignores the sign convention. Slowing down while moving in the positive direction needs a negative acceleration.
    D: |-
      Divides the speed by the stopping distance ($20/25$), treating it like $a = \Delta v/\Delta t$ with a distance in place of the time. The units come out as $\text{s}^{-1}$, not $\text{m/s}^2$.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a monitor shows a side-scrolling game whose runner moves along a straight track marked like a number line, with a position and velocity readout; a tablet replays a velocity-time graph](scenes/gaming/motion_straight_line.svg "Side-scrollers run along one line. A jump runs along the other one: straight up and down.")

Ishaan and his cousin Rhea are building a platformer together over the holidays. Ishaan insists on "real physics": gravity in their engine is set to $9.8\,\text{m/s}^2$, and the hero's jump launches him straight up at $4.9\,\text{m/s}$ (their chosen number).

Rhea is designing the first level. She has placed a ledge $1.3\,\text{m}$ above the ground — about the height of a kitchen counter — and she wants the hero to be able to jump onto it.

"He'll make it easily," she says. "Four point nine metres per second is fast. That's nearly eighteen km/h, straight up."

Ishaan isn't so sure. He also wants to know how long each jump lasts, because the level has a spike trap that fires once a second, and the hero needs to be back on the ground before it does.

Gravity in their engine never changes during a jump. Surely that makes the whole jump predictable, on paper, before anyone presses play?

## The physics

When an object moves along a straight line with **constant acceleration** $a$, three equations connect the initial velocity $u$, final velocity $v$, displacement $s$ and time $t$:

$$v = u + at$$
$$s = ut + \tfrac{1}{2}at^2$$
$$v^2 = u^2 + 2as$$

Each equation leaves one quantity out: the first has no $s$, the second no $v$, the third no $t$. Pick the one that contains the three quantities you know and the one you want.

Where they come from:

- **$v = u + at$** is the definition of acceleration, $a = (v - u)/t$, rearranged — valid only when $a$ is constant.
- **$s = ut + \tfrac{1}{2}at^2$** is the area under the straight $v$–$t$ line: a rectangle $ut$ plus a triangle $\tfrac{1}{2}t(at)$.
- **$v^2 = u^2 + 2as$** comes from eliminating $t$ between the first two.

![A velocity–time graph rising in a straight line from 2 m/s to 8 m/s over 4 s, with the area below split into a rectangle of area ut = 8 m and a triangle of area ½at² = 12 m](figures/equations_of_motion/vt-area-derivation.svg "The displacement is the area under the line: rectangle plus triangle, 8 m + 12 m = 20 m. That is where s = ut + ½at² comes from.")

**Signs matter.** Choose a positive direction and give every vector — $u$, $v$, $a$, $s$ — its sign. For a jump, take upward as positive: gravity then gives $a = -g = -9.8\,\text{m/s}^2$, all the way up *and* all the way down.

## Worked example

**Given:** $u = +4.9\,\text{m/s}$ (upward positive), $a = -9.8\,\text{m/s}^2$, no air resistance (the engine has none).
**Find:** the time to the top, the jump height, and the time until the hero lands back on the ground.

**Time to the top.** At the top, $v = 0$. Use $v = u + at$:

$$0 = 4.9 - 9.8t \;\Rightarrow\; t = \frac{4.9}{9.8} = 0.50\,\text{s}$$

**Jump height.** Use $v^2 = u^2 + 2as$ with $v = 0$:

$$0 = 4.9^2 - 2(9.8)s \;\Rightarrow\; s = \frac{24.01}{19.6} \approx 1.23\,\text{m}$$

**Back on the ground.** Now $s = 0$. Use $s = ut + \tfrac{1}{2}at^2$:

$$0 = 4.9t - 4.9t^2 = 4.9t(1 - t) \;\Rightarrow\; t = 0 \text{ or } t = 1.0\,\text{s}$$

So the hero is airborne for exactly one second — no margin at all against a trap that fires every second — and tops out at about $1.23\,\text{m}$, short of Rhea's $1.3\,\text{m}$ ledge. To reach it, $u^2 = 2(9.8)(1.3) = 25.48$, so the launch speed must be at least $u \approx 5.05\,\text{m/s}$.

**Sanity check:** the flight is symmetric, so $1.0\,\text{s}$ is twice the $0.50\,\text{s}$ to the top. And $s = 4.9(0.50) - 4.9(0.50)^2 = 2.45 - 1.225 \approx 1.23\,\text{m}$ agrees with the third equation.

## Where the picture breaks

The equations need a **constant** acceleration, which a game gives exactly; real life adds air resistance, which is small for a jumping person but grows with speed. A game engine also doesn't move the hero continuously: it updates position and velocity in steps, commonly $\tfrac{1}{60}\,\text{s}$, and depending on how it does that update, the simulated jump can be a little higher or lower than the exact formula says — a real headache for level designers. Many games also deliberately use gravity far stronger than $9.8\,\text{m/s}^2$, or stronger on the way down, because real gravity feels "floaty" on screen. The equations still hold for any constant value you choose.

## Key takeaway

For constant acceleration in a straight line, $v = u + at$, $s = ut + \tfrac{1}{2}at^2$ and $v^2 = u^2 + 2as$. Choose a positive direction, sign every vector, and pick the equation that contains what you know and what you want. With real gravity, a $4.9\,\text{m/s}$ jump lasts one second and peaks at about $1.23\,\text{m}$.
