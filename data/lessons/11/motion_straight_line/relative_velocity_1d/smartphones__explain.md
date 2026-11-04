---
concept_id: relative_velocity_1d
interest: smartphones
format: explain
title: Sharing a file between two moving trains
check:
  question: |-
    You walk along a straight street towards a cab you've booked. Taking the positive direction as the way the cab is driving, the cab moves at $+8.0\,\text{m/s}$ and you walk at $-1.5\,\text{m/s}$. What is the cab's velocity relative to you, $v_\text{CY}$?
  options:
    A: |-
      $+6.5\,\text{m/s}$
    B: |-
      $+9.5\,\text{m/s}$
    C: |-
      $-9.5\,\text{m/s}$
    D: |-
      $+8.0\,\text{m/s}$
  answer: B
  explanation: |-
    $v_\text{CY} = v_\text{C} - v_\text{Y} = (+8.0) - (-1.5) = +9.5\,\text{m/s}$. Walking towards the cab makes it close in on you faster than its own speed.
  misconceptions:
    A: |-
      Adds the signed velocities, $8.0 + (-1.5)$, instead of subtracting your velocity from the cab's.
    C: |-
      Computes $v_\text{Y} - v_\text{C}$, which is your velocity relative to the cab. The order of the subscripts matters: it flips the sign.
    D: |-
      Ignores the observer's own motion, as if velocities looked the same from every frame. Your walking changes how fast the cab approaches you.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![An evening street: a phone shows a live-tracking map of a straight road, while a delivery scooter rides past kilometre markers](scenes/smartphones/motion_straight_line.svg "Everything on this road is moving. How fast something seems to move depends on who is watching.")

Neha and her cousin Aryan are going home from the same city on the same evening — on two different trains that leave the station together on parallel tracks.

For a few minutes the trains run almost side by side, windows nearly level. Neha opens her phone's nearby-sharing feature, spots Aryan's phone, and sends him a whole wedding video. It goes through without a hitch. Their phones' short-range link only reaches about ten metres (illustrative), but it didn't matter.

A week later they travel back, and this time their trains pass each other in opposite directions on the same stretch of track. Neha is ready, phone in hand, sharing screen open. Aryan's phone appears for a moment — and vanishes. Nothing is sent.

"Same trains, same speeds, same tracks, same phones," Aryan texts afterwards. "Why did it work perfectly once and fail completely the next time?"

What changed isn't how fast either train was going. It's how fast each looked *from the other*.

## The physics

The **relative velocity** of object A with respect to object B is the velocity A appears to have to an observer moving along with B:

$$v_\text{AB} = v_\text{A} - v_\text{B}$$

Both $v_\text{A}$ and $v_\text{B}$ are measured from the ground, along the same line, with the **same** positive direction, and substituted **with their signs**. Order matters: $v_\text{BA} = v_\text{B} - v_\text{A} = -v_\text{AB}$.

Two cases show up all the time:

- **Same direction:** the relative velocity is the *difference* of the speeds. Two objects at similar speeds hardly move relative to each other.
- **Opposite directions (head-on):** subtracting a negative velocity adds the speeds. They rush past each other.

![Two diagrams on a line. A chase: A at +8 m/s behind B at +6 m/s, relative velocity +2 m/s. Head-on: A at +5 m/s and B at −6 m/s, relative velocity +11 m/s](figures/relative_velocity_1d/chase-and-head-on.svg "Subtract with signs. Moving the same way, the speeds partly cancel; head-on, they add.")

For the phones, what matters is not the trains' speeds over the ground but how quickly the gap between the two phones changes — the relative velocity. On the first trip it was small, so the phones stayed within range for a long time. On the second, it was huge.

## Worked example

**Given:** positive in the direction of Neha's train. Neha's train: $v_\text{N} = +22\,\text{m/s}$. Aryan's train: $+20\,\text{m/s}$ on the first trip, $-20\,\text{m/s}$ on the second (illustrative). The link works while the phones are within $10\,\text{m}$ of each other along the track — from $10\,\text{m}$ behind to $10\,\text{m}$ ahead, a window $20\,\text{m}$ long. Treat the speeds as constant.
**Find:** how long the phones stay in range each time.

**Same direction:**

$$v_\text{NA} = v_\text{N} - v_\text{A} = 22 - 20 = +2\,\text{m/s}$$

Time in range: $t = 20\,\text{m} / 2\,\text{m/s} = 10\,\text{s}$ — long enough to connect and send a video. (To stay side by side for minutes, as in the story, the trains' speeds must have matched even more closely than this.)

**Opposite directions:**

$$v_\text{NA} = 22 - (-20) = +42\,\text{m/s}$$

Time in range: $t = 20/42 \approx 0.48\,\text{s}$ — less than half a second. The phones barely find each other before they're apart.

**Sanity check:** had the trains run at exactly equal speeds in the same direction, $v_\text{NA} = 0$ and the phones would stay in range indefinitely — the right limit. And from Aryan's seat the answers are the same, with the sign flipped: $v_\text{AN} = -2\,\text{m/s}$ and $-42\,\text{m/s}$.

## Where the picture breaks

Real trains don't hold constant speeds, and they sit a few metres apart sideways, so the true gap between the phones never quite reaches zero — we have kept only the motion along the track. The ten-metre range is not a sharp edge either: signal strength fades gradually, and a train's metal body blocks a lot of it. So the numbers here are rough, and the phone is only the setting. The physics is solid, though: $v_\text{AB} = v_\text{A} - v_\text{B}$ holds at every instant, and it is an excellent approximation at everyday speeds; only near the speed of light does this simple subtraction need correcting.

## Key takeaway

The velocity of A relative to B is $v_\text{AB} = v_\text{A} - v_\text{B}$, with both velocities signed along the same line. Moving the same way, the speeds partly cancel and objects stay near each other; head-on, the speeds add and they flash past. Swap A and B and the sign flips.
