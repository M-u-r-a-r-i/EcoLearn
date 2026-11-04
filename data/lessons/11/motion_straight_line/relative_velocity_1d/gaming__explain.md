---
concept_id: relative_velocity_1d
interest: gaming
format: explain
title: Faster on the final straight, and still second
check:
  question: |-
    In a street-racing game, take the positive direction along your car's motion. Your car moves at $+40\,\text{m/s}$, and a bus in the opposite lane comes towards you at $-15\,\text{m/s}$. What is the velocity of the bus relative to your car, $v_\text{BC}$?
  options:
    A: |-
      $+55\,\text{m/s}$
    B: |-
      $+25\,\text{m/s}$
    C: |-
      $-55\,\text{m/s}$
    D: |-
      $-15\,\text{m/s}$
  answer: C
  explanation: |-
    $v_\text{BC} = v_\text{B} - v_\text{C} = (-15) - (+40) = -55\,\text{m/s}$. Seen from your car, the bus rushes towards you at $55\,\text{m/s}$, in the negative direction.
  misconceptions:
    A: |-
      Computes $v_\text{C} - v_\text{B}$, which is your car's velocity relative to the bus. The order of the subscripts matters: swapping it flips the sign.
    B: |-
      Adds the signed velocities, $40 + (-15)$, or subtracts the speeds as if it were a chase. Head-on, the speeds add.
    D: |-
      Gives the bus's velocity relative to the road and forgets that the observer (your car) is moving too.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A gaming desk at night: a monitor shows a side-scrolling game whose runner moves along a straight track marked like a number line, with a position and velocity readout; a tablet replays a velocity-time graph](scenes/gaming/motion_straight_line.svg "Every velocity on a HUD is measured from the track. What you see through the windscreen depends on your own motion too.")

Last lap of the online league final. Arjun comes out of the final corner onto the long straight in second place, and his car is quicker: the HUD shows $288\,\text{km/h}$, and the leader's telemetry shows $270\,\text{km/h}$ (illustrative numbers).

His friend Sneha is watching the stream. "He's got him. He's eighteen km/h faster."

But through Arjun's windscreen, the leader's car isn't rushing towards him at all. It is creeping back towards his bonnet, painfully slowly. The gap is $60\,\text{m}$, and the finish line is $600\,\text{m}$ beyond the leader.

The chat is spamming "SEND IT". Arjun holds the throttle flat. The leader's rear wing grows, and grows, and crosses the line still clearly ahead.

"He was faster," Sneha says. "How does the slower car win?"

What she needs is the view from inside Arjun's car — the view the camera was showing all along.

## The physics

The **relative velocity** of object A with respect to object B is the velocity A appears to have to an observer moving along with B:

$$v_\text{AB} = v_\text{A} - v_\text{B}$$

Here $v_\text{A}$ and $v_\text{B}$ are both measured from the ground (the track), along the same line, with the **same** positive direction, and substituted **with their signs**. Order matters: $v_\text{BA} = v_\text{B} - v_\text{A} = -v_\text{AB}$.

Two cases come up all the time:

- **Same direction (a chase):** the relative velocity is the *difference* of the speeds. The gap closes slowly.
- **Opposite directions (head-on):** subtracting a negative velocity adds the speeds. The gap closes fast.

![Two diagrams on a line. A chase: A at +8 m/s behind B at +6 m/s, relative velocity +2 m/s. Head-on: A at +5 m/s and B at −6 m/s, relative velocity +11 m/s](figures/relative_velocity_1d/chase-and-head-on.svg "Subtract with signs. In a chase the speeds partly cancel; head-on, they add.")

That slowly creeping rear wing *is* the relative velocity. The chase camera rides along with Arjun's car, so it shows the leader moving at $v_\text{leader} - v_\text{Arjun}$: a small number, pointing backwards.

## Worked example

**Given:** positive direction along the straight. Arjun (A): $288\,\text{km/h} = 288/3.6 = 80\,\text{m/s}$. Leader (L): $270\,\text{km/h} = 75\,\text{m/s}$. Gap $60\,\text{m}$; the line is $600\,\text{m}$ ahead of the leader. Take both speeds as constant.
**Find:** whether Arjun catches the leader before the line.

Arjun's velocity relative to the leader:

$$v_\text{AL} = v_\text{A} - v_\text{L} = 80 - 75 = +5.0\,\text{m/s}$$

Time to close the $60\,\text{m}$ gap: $t = 60/5.0 = 12\,\text{s}$.

Time for the leader to reach the line: $t = 600/75 = 8.0\,\text{s}$.

The leader gets there first. In $8.0\,\text{s}$ Arjun closes only $5.0 \times 8.0 = 40\,\text{m}$ of the gap, and crosses the line $20\,\text{m}$ behind.

**Second case — head-on:** in a street-racing mode, a car in the opposite lane comes towards Arjun at $-20\,\text{m/s}$ while he does $+80\,\text{m/s}$. Its velocity relative to him is $-20 - 80 = -100\,\text{m/s}$: it seems to rush at him at $360\,\text{km/h}$, faster than either car is actually going.

**Sanity check:** had Arjun matched the leader's speed, $v_\text{AL} = 0$ and the gap would never close — the right limit. Had the leader been parked, $v_\text{AL}$ would be Arjun's full $80\,\text{m/s}$. And the leader's velocity relative to Arjun is $v_\text{LA} = 75 - 80 = -5.0\,\text{m/s}$: the slow backward creep on screen.

## Where the picture breaks

We assumed constant speeds; in a real race both cars are still accelerating on the straight, and slipstreaming changes Arjun's speed as he closes in, so the relative velocity changes from moment to moment. The rule $v_\text{AB} = v_\text{A} - v_\text{B}$ still holds at every instant. Online games add their own wrinkle: each player's screen shows the other car's position a fraction of a second late, and the game has to reconcile the two views. And the simple subtraction is an excellent approximation at everyday speeds, but not near the speed of light, where it needs correcting.

## Key takeaway

The velocity of A relative to B is $v_\text{AB} = v_\text{A} - v_\text{B}$, with both velocities signed along the same line. In a chase the speeds partly cancel, so being faster may not be enough in the distance left; head-on, they add. Subtract in the right order — swapping A and B flips the sign.
