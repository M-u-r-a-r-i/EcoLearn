---
concept_id: distance
interest: football
format: explain
title: Eighty metres of running for ten metres of ground
check:
  question: |-
    A winger sprints $30\,\text{m}$ up the touchline for a through ball. It is overhit and goes out, so she jogs $12\,\text{m}$ back down the same touchline to take up position for the goal kick. What distance has she covered?
  options:
    A: |-
      $18\,\text{m}$
    B: |-
      $42\,\text{m}$
    C: |-
      $-42\,\text{m}$
    D: |-
      $30\,\text{m}$
  answer: B
  explanation: |-
    Distance is the total length of the path, whatever the direction of each leg: $30\,\text{m} + 12\,\text{m} = 42\,\text{m}$.
  misconceptions:
    A: |-
      Subtracts the backward leg, $30 - 12 = 18\,\text{m}$ — that is how far she ended up from her start (the size of her displacement), not the distance she ran.
    C: |-
      Gives distance a sign because part of the path went back down the pitch. Distance is a scalar and can never be negative.
    D: |-
      Takes the distance to be the farthest point she reached from her start, ignoring the path she ran on the way back.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A winger dribbles along the touchline towards goal, chased by a defender, while the goalkeeper comes off the line; a number line with origin O and +x runs beneath](scenes/football/motion_straight_line.svg "Full-backs and wingers spend the whole match running up and down this one line.")

Seventieth minute of a school league match. Kavya, the left-back, sees space and makes a lung-bursting overlapping run up the touchline — about $35\,\text{m}$ (illustrative). The cross never comes: her winger loses the ball, and the other team breaks. Kavya turns and sprints $45\,\text{m}$ back down the same line, sliding in to block the shot at the last moment.

At the break for drinks, her fitness tracker shows the spell: *80 m*.

Her classmate Tushar, filming from the touchline, is sceptical. "Eighty? You finished ten metres behind where you started. You basically went backwards. That's ten metres."

"Tell that to my legs," Kavya gasps.

Tushar isn't joking, though. He really thinks the answer is ten — she ended only ten metres from her starting spot. The tracker really thinks it's eighty.

Which number answers "how far did she run" — and why do they disagree?

## The physics

**Distance** is the total length of the path an object actually travels. It has three defining properties:

- It adds up **every** part of the path, whichever way that part goes.
- It is a **scalar**: a size with a unit, but no direction.
- It can never be negative, and it never decreases as time goes on. The best it can do is stay the same, when the object stops.

Kavya's spell had two legs along the touchline:

$$\text{distance} = 35\,\text{m} + 45\,\text{m} = 80\,\text{m}$$

The second leg went back down the pitch, but it still counts in full: her legs did the work either way. That's why the tracker says $80\,\text{m}$.

Tushar's $10\,\text{m}$ is a different quantity: how far she ended up from where she started, in a straight line. That is (the size of) her **displacement**, which you'll meet in the next lesson. For a trip that never turns around, the two are equal; as soon as the path doubles back, distance becomes larger.

![A path in three legs on a number line — 5 m forward, 5 m back, 3 m forward — with distance 13 m and displacement +3 m](figures/distance/path-legs-total.svg "Distance adds every leg as a positive length: 5 + 5 + 3 = 13 m. The start-to-end gap is only 3 m.")

In symbols, if a path is made of straight legs of lengths $d_1, d_2, d_3, \ldots$ then the distance is $d = d_1 + d_2 + d_3 + \cdots$, with every $d_i \ge 0$. Its SI unit is the metre.

## Worked example

**Given:** a goalkeeper sets up on his line for a corner. He comes off his line $6\,\text{m}$ to claim the cross, misses it and backpedals $6\,\text{m}$ to his line, then comes $4\,\text{m}$ out again to close down the rebound (illustrative).
**Find:** the distance he covered, and how far he finished from where he started.

Distance adds every leg:

$$d = 6 + 6 + 4 = 16\,\text{m}$$

Where did he finish? Out $6$, back $6$ puts him on his line again; then $4\,\text{m}$ out. So he finished $4\,\text{m}$ from where he started.

**Sanity check:** the distance ($16\,\text{m}$) is at least as large as the start-to-finish gap ($4\,\text{m}$), as it must be — and the extra $12\,\text{m}$ is exactly the out-and-back that got him nowhere, $6 + 6$.

## Where the picture breaks

Real players never run a perfectly straight line: Kavya would curve infield to cut off the attacker, so her true path is a little longer than $80\,\text{m}$, and in two dimensions distance is measured along the curve. A fitness tracker also *estimates* distance, from GPS fixes or step counts, and can be off by several per cent. And in a full match a midfielder covers many kilometres on a pitch only about $100\,\text{m}$ long — the same idea on a bigger scale: distance keeps adding, while the pitch stays the same size.

## Key takeaway

Distance is the total length of the path travelled: add every leg as a positive number, whatever its direction. It is a scalar, never negative, and it never goes down. Kavya's run up and back was $80\,\text{m}$ of distance, even though she finished just $10\,\text{m}$ from where she began.
