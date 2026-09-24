---
concept_id: relative_velocity_1d
interest: motorsport
format: explain
title: He is faster and still cannot get past
check:
  question: |-
    Take the positive direction as the way the cars travel down the straight. Car P is running at $+55\,\text{m/s}$ and catches car Q, which is being lapped and is running at $+35\,\text{m/s}$. What is the velocity of P relative to Q, $v_\text{PQ}$?
  options:
    A: |-
      $+90\,\text{m/s}$
    B: |-
      $+20\,\text{m/s}$
    C: |-
      $-20\,\text{m/s}$
    D: |-
      $+1.6\,\text{m/s}$
  answer: B
  explanation: |-
    $v_\text{PQ} = v_\text{P} - v_\text{Q} = 55 - 35 = +20\,\text{m/s}$. To someone sitting in Q, P is closing at $20\,\text{m/s}$, not at its full track speed.
  misconceptions:
    A: |-
      Adds the two velocities. Adding is what the subtraction does automatically when the cars move in *opposite* directions; in a chase, both are positive and they partly cancel.
    C: |-
      Computes $v_\text{Q} - v_\text{P}$, which is Q's velocity relative to P. The order of the subscripts matters — swapping them flips the sign.
    D: |-
      Divides one speed by the other ($55/35$). Relative velocity is a difference of velocities, not a ratio, and a ratio has no units of m/s at all.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A long straight at a race circuit with a car accelerating away from the timing beam at the start line, distance boards reading 0, 100 and 200 along the verge, and an arrow marking the positive direction](scenes/motorsport/motion_straight_line.svg "Two cars, one straight. What decides the overtake is not either speed — it is the gap between them.")

Vivek and Kavya have the best seats in the grandstand, right where the long back straight begins, and the two cars fighting for third have just come out of the last corner nose to tail.

"He's got him," says Kavya. The chasing car is visibly quicker — you can hear it and you can see the gap shrinking every second.

"Not down here he hasn't," says Vivek.

The gap closes, and closes, and then the braking boards come up and both drivers stand on the brakes, still in the same order they started.

Kavya is indignant. The chasing car was faster. It was catching up the whole way. And yet the straight simply ran out.

What she needs is to stop watching from the grandstand and start watching from the car in front. Seen from there, how quickly is the chaser actually arriving?

## The physics

The **relative velocity** of object A with respect to object B is the velocity A appears to have to an observer travelling along with B:

$$v_\text{AB} = v_\text{A} - v_\text{B}$$

Both $v_\text{A}$ and $v_\text{B}$ are measured from the ground, along the same line, using the **same** positive direction, and are substituted **with their signs**. The order matters: $v_\text{BA} = v_\text{B} - v_\text{A} = -v_\text{AB}$.

Two cases cover almost everything:

- **Same direction (a chase):** the relative velocity is the *difference* of the speeds, and the gap closes slowly.
- **Opposite directions (head-on):** subtracting a negative velocity adds the speeds, and the gap closes alarmingly fast.

![Two diagrams on a line. A chase: A behind B, both moving the same way, with a small relative velocity. Head-on: A and B moving towards each other, with a large relative velocity](figures/relative_velocity_1d/chase-and-head-on.svg "Subtract with signs. In a chase the speeds partly cancel; head-on, they add.")

That is the answer to the grandstand argument. Being faster is not the question. The question is whether the *closing speed* — a much smaller number than either car's speed — can eat the gap before the straight runs out.

## Worked example

**Given:** positive down the straight. Chasing car A: $v_\text{A} = +60\,\text{m/s}$. Leading car B: $v_\text{B} = +50\,\text{m/s}$. The gap is $50\,\text{m}$, and B's braking point is $200\,\text{m}$ ahead of it. Treat both speeds as constant along the straight (illustrative).
**Find:** whether A draws level with B before the braking point.

A's velocity relative to B:

$$v_\text{AB} = v_\text{A} - v_\text{B} = 60 - 50 = +10\,\text{m/s}$$

At that closing speed, wiping out the $50\,\text{m}$ gap takes

$$t = \frac{50\,\text{m}}{10\,\text{m/s}} = 5.0\,\text{s}$$

But B reaches its braking point in

$$t = \frac{200\,\text{m}}{50\,\text{m/s}} = 4.0\,\text{s}$$

The straight runs out first. In those $4.0\,\text{s}$, A closes only $10 \times 4.0 = 40\,\text{m}$ of the gap and arrives at the braking zone still $10\,\text{m}$ behind — close enough to be loud, not close enough to pass.

**A second case.** Suppose B had spun and stopped on the straight: $v_\text{B} = 0$, so $v_\text{AB} = 60 - 0 = +60\,\text{m/s}$. The closing speed jumps from $10$ to $60\,\text{m/s}$, which is why a stationary car on a fast straight is the most dangerous thing on a circuit, and why marshals wave flags long before anyone can see it.

**Sanity check:** if A had been doing exactly B's $50\,\text{m/s}$, then $v_\text{AB} = 0$ and the gap would never close at all — the right answer in that limit.

## Where the picture breaks

Neither car holds a constant speed down a real straight: both are still accelerating, and the chasing car usually gains extra speed in the leader's slipstream, so the closing speed grows as the chase goes on. That is why a pass that "shouldn't" happen sometimes does. The rule itself survives all of this — $v_\text{AB} = v_\text{A} - v_\text{B}$ holds at every instant, whatever the cars are doing — but you must use the velocities at that instant, not averages. And simple subtraction is an excellent approximation for anything on wheels; only at speeds approaching the speed of light does it need correcting.

## Key takeaway

The velocity of A relative to B is $v_\text{AB} = v_\text{A} - v_\text{B}$, with both velocities signed along the same line. In a chase the speeds partly cancel, so being faster may not be enough; head-on, they add. Get the order of the subscripts right — swapping A and B flips the sign, and turns "catching" into "being caught".
