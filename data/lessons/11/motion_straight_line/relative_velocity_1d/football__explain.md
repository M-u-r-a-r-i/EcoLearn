---
concept_id: relative_velocity_1d
interest: football
format: explain
title: The faster defender who never caught up
check:
  question: |-
    Two players run towards each other to contest a header. Taking the positive direction towards the opponents' goal, player A runs at $+6.0\,\text{m/s}$ and player B runs at $-4.0\,\text{m/s}$. What is the velocity of B relative to A, $v_\text{BA}$?
  options:
    A: |-
      $+10\,\text{m/s}$
    B: |-
      $+2.0\,\text{m/s}$
    C: |-
      $-10\,\text{m/s}$
    D: |-
      $-4.0\,\text{m/s}$
  answer: C
  explanation: |-
    $v_\text{BA} = v_\text{B} - v_\text{A} = (-4.0) - (+6.0) = -10\,\text{m/s}$. Seen from A, B rushes towards her at $10\,\text{m/s}$ in the negative direction — the speeds add because they run head-on.
  misconceptions:
    A: |-
      Computes $v_\text{A} - v_\text{B}$, which is A's velocity relative to B. The order of the subscripts matters: swapping it flips the sign.
    B: |-
      Adds the signed velocities, $6.0 + (-4.0)$, instead of subtracting A's velocity from B's.
    D: |-
      Reports B's velocity relative to the ground, forgetting that the question asks how B moves as seen by A, who is moving too.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A winger dribbles along the touchline towards goal, chased by a defender, while the goalkeeper comes off the line; a number line with origin O and +x runs beneath](scenes/football/motion_straight_line.svg "The defender's arrow is longer than the winger's. Only the gap between them decides the chase.")

A corner is cleared, and the counter-attack is on. Aarav picks up the ball near halfway and races towards goal, the ball at his feet. Jomon, the other team's fastest defender, sets off after him from a few metres behind.

In the stands, Divya grabs her father's arm. "Jomon will catch him — he's much quicker!" She's right that he's quicker: with the ball at his feet Aarav manages about $7.5\,\text{m/s}$, while Jomon is flat out at about $8.5\,\text{m/s}$ (illustrative numbers).

"He's six metres behind, though," her father says. "And Aarav only needs to get twenty metres further before he shoots."

Jomon closes, stretches for a tackle — and the shot is already away. Goal.

Divya can't believe it. The faster player lost the race. How can being quicker not be enough?

To see it, she needs to watch the chase from Aarav's point of view.

## The physics

The **relative velocity** of object A with respect to object B is the velocity A appears to have to an observer moving along with B:

$$v_\text{AB} = v_\text{A} - v_\text{B}$$

Here $v_\text{A}$ and $v_\text{B}$ are both measured from the ground, along the same line, with the **same** positive direction, and substituted **with their signs**. Order matters: $v_\text{BA} = v_\text{B} - v_\text{A} = -v_\text{AB}$.

Two cases show up constantly on a football pitch:

- **Same direction (a chase):** the relative velocity is the *difference* of the speeds. The gap closes slowly.
- **Opposite directions (head-on):** subtracting a negative velocity adds the speeds. The gap closes fast.

![Two diagrams on a line. A chase: A at +8 m/s behind B at +6 m/s, relative velocity +2 m/s. Head-on: A at +5 m/s and B at −6 m/s, relative velocity +11 m/s](figures/relative_velocity_1d/chase-and-head-on.svg "Subtract with signs. In a chase the speeds partly cancel; head-on, they add.")

From Aarav's point of view, Jomon isn't approaching at $8.5\,\text{m/s}$ — only at the *difference* of their speeds. That small closing speed has to eat up the gap before Aarav reaches his shooting spot.

## Worked example

**Given:** positive towards the goal Aarav is attacking. Jomon (J): $v_\text{J} = +8.5\,\text{m/s}$. Aarav (A): $v_\text{A} = +7.5\,\text{m/s}$. Gap $= 6.0\,\text{m}$; Aarav shoots after running another $20\,\text{m}$. Take both speeds as constant.
**Find:** whether Jomon catches him before the shot.

Jomon's velocity relative to Aarav:

$$v_\text{JA} = v_\text{J} - v_\text{A} = 8.5 - 7.5 = +1.0\,\text{m/s}$$

Time to close the $6.0\,\text{m}$ gap: $t = 6.0/1.0 = 6.0\,\text{s}$.

Time for Aarav to reach his shooting spot: $t = 20/7.5 \approx 2.7\,\text{s}$.

In $2.7\,\text{s}$ Jomon closes only $1.0 \times 2.7 \approx 2.7\,\text{m}$ of the gap — still about $3.3\,\text{m}$ behind when the shot goes in.

**Second case — the keeper comes out:** the goalkeeper rushes at Aarav at $-5.0\,\text{m/s}$. Then $v_\text{AK} = 7.5 - (-5.0) = +12.5\,\text{m/s}$: a $25\,\text{m}$ gap vanishes in just $25/12.5 = 2.0\,\text{s}$. That is why a keeper coming off the line gives a striker so little time.

**Sanity check:** had Jomon been exactly as fast as Aarav, $v_\text{JA} = 0$ and the gap would never close — the right limit. Had Aarav stood still, $v_\text{JA}$ would be Jomon's full $8.5\,\text{m/s}$.

## Where the picture breaks

Neither player keeps a constant speed: Jomon needs a second or two to reach top speed, and Aarav slows each time he touches the ball, so the relative velocity changes during the chase. For those details you'd need accelerations — but $v_\text{AB} = v_\text{A} - v_\text{B}$ still holds at every instant. Real chases are also rarely along one straight line; a defender angles his run to cut off the shot, which needs vectors in two dimensions. And this simple subtraction is an excellent approximation at everyday speeds; only near the speed of light does it need correcting.

## Key takeaway

The velocity of A relative to B is $v_\text{AB} = v_\text{A} - v_\text{B}$, with both velocities signed along the same line. In a chase the speeds partly cancel, so being faster may not be enough; head-on, they add. Subtract in the right order — swapping A and B flips the sign.
