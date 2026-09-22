---
concept_id: relative_velocity_1d
interest: cricket
format: explain
title: He is faster than the ball, so why is it four
check:
  question: |-
    Two batters run a single and pass each other mid-pitch. Taking the positive direction towards the bowler's end, batter A runs at $+4.5\,\text{m/s}$ and batter B runs at $-5.5\,\text{m/s}$. What is the velocity of A relative to B, $v_\text{AB}$?
  options:
    A: |-
      $+10\,\text{m/s}$
    B: |-
      $-1.0\,\text{m/s}$
    C: |-
      $+1.0\,\text{m/s}$
    D: |-
      $-10\,\text{m/s}$
  answer: A
  explanation: |-
    $v_\text{AB} = v_\text{A} - v_\text{B} = (+4.5) - (-5.5) = +10\,\text{m/s}$. Seen from B, A rushes towards the bowler's end at $10\,\text{m/s}$.
  misconceptions:
    B: |-
      Adds the signed velocities, $4.5 + (-5.5)$, instead of subtracting B's velocity from A's.
    C: |-
      Subtracts the speeds and ignores the directions, $5.5 - 4.5$ — the rule for a chase, wrongly used for two people running towards each other.
    D: |-
      Computes $v_\text{B} - v_\text{A}$, which is B's velocity relative to A. The order of the subscripts matters: it flips the sign.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground in sunshine: a fielder chases the ball towards the boundary rope while a batter runs between the wickets](scenes/cricket/motion_straight_line.svg "Fielder and ball both heading for the rope. Only the gap between them matters.")

The ball is pulled hard along the ground towards the long boundary, and Vikram sets off after it from deep mid-wicket.

On the pavilion balcony, Sneha and her brother Arjun lean forward. "He'll get it," Sneha says. "He's running faster than the ball now." She's right about that: by the time Vikram hits top speed, he's doing about $8\,\text{m/s}$, and the ball, slowed by the grass, is rolling at about $6\,\text{m/s}$ (illustrative numbers).

"But look how far behind he is," Arjun says. The ball is $10\,\text{m}$ ahead of Vikram, and the rope is $25\,\text{m}$ beyond the ball.

The crowd roars. Vikram closes in, stretches out a hand — and the ball trickles over the rope a stride ahead of him. Four.

Sneha frowns. He was faster. How can the slower thing win?

What she needs is to see the chase from the ball's point of view.

## The physics

The **relative velocity** of object A with respect to object B is the velocity A appears to have to an observer moving along with B:

$$v_\text{AB} = v_\text{A} - v_\text{B}$$

Here $v_\text{A}$ and $v_\text{B}$ are both measured from the ground, along the same line, with the **same** positive direction, and substituted **with their signs**. Order matters: $v_\text{BA} = v_\text{B} - v_\text{A} = -v_\text{AB}$.

Two cases show up all the time:

- **Same direction (a chase):** the relative velocity is the *difference* of the speeds. The gap closes slowly.
- **Opposite directions (head-on):** subtracting a negative velocity adds the speeds. The gap closes fast.

![Two diagrams on a line. A chase: A at +8 m/s behind B at +6 m/s, relative velocity +2 m/s. Head-on: A at +5 m/s and B at −6 m/s, relative velocity +11 m/s](figures/relative_velocity_1d/chase-and-head-on.svg "Subtract with signs. In a chase the speeds partly cancel; head-on, they add.")

In Vikram's chase, the ball's view is what matters: to the ball, Vikram is approaching at only the *difference* of their speeds. Being faster isn't enough — the question is whether that small closing speed eats up the gap before the rope.

## Worked example

**Given:** positive direction towards the rope. Vikram (F): $v_\text{F} = +8.0\,\text{m/s}$. Ball (B): $v_\text{B} = +6.0\,\text{m/s}$. Gap $= 10\,\text{m}$; the rope is $25\,\text{m}$ ahead of the ball. Take both speeds as constant.
**Find:** whether Vikram reaches the ball before the rope.

Vikram's velocity relative to the ball:

$$v_\text{FB} = v_\text{F} - v_\text{B} = 8.0 - 6.0 = +2.0\,\text{m/s}$$

Time to close the $10\,\text{m}$ gap: $t = 10/2.0 = 5.0\,\text{s}$.

Time for the ball to reach the rope: $t = 25/6.0 \approx 4.17\,\text{s}$.

The ball gets there first. In $4.17\,\text{s}$ Vikram closes only $2.0 \times 4.17 \approx 8.3\,\text{m}$ of the gap — about $1.7\,\text{m}$ short. Four runs.

**Second case — batters crossing:** one runs at $+6.0\,\text{m/s}$, the other at $-6.0\,\text{m/s}$. Then $v_\text{12} = 6.0 - (-6.0) = +12\,\text{m/s}$: each sees the other rush past at twice their own speed.

**Sanity check:** had Vikram been as fast as the ball, $v_\text{FB} = 0$ and he'd never close the gap — the right limit. Had the ball been stopped, $v_\text{FB}$ would be his full $8.0\,\text{m/s}$.

## Where the picture breaks

A ball rolling on grass doesn't keep a constant $6\,\text{m/s}$: friction slows it steadily, so the relative velocity grows as the chase goes on, and a real fielder sometimes catches a ball that "should" have won. Vikram also needs time to reach top speed. For those details you'd need accelerations — but the rule $v_\text{AB} = v_\text{A} - v_\text{B}$ still holds at every instant. It is an excellent approximation at everyday speeds; only near the speed of light does this simple subtraction need correcting.

## Key takeaway

The velocity of A relative to B is $v_\text{AB} = v_\text{A} - v_\text{B}$, with both velocities signed along the same line. In a chase the speeds partly cancel, so being faster may not be enough; head-on, they add. Always subtract in the right order — swapping A and B flips the sign.
