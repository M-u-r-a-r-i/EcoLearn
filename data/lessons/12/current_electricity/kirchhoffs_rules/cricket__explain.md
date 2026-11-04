---
concept_id: kirchhoffs_rules
interest: cricket
format: explain
title: Two battery packs, one scoreboard, and no series-parallel shortcut
check:
  question: |-
    Three wires meet at a junction in a circuit. Along the first, a current of $5.0\,\text{A}$ flows **into** the junction; along the second, $2.0\,\text{A}$ flows **out**. The current in the third wire is:
  options:
    A: |-
      $7.0\,\text{A}$, flowing out
    B: |-
      $3.0\,\text{A}$, flowing in
    C: |-
      $7.0\,\text{A}$, flowing in
    D: |-
      $3.0\,\text{A}$, flowing out
  answer: D
  explanation: |-
    Charge cannot accumulate at a junction, so current in must equal current out: $5.0\,\text{A}$ in must be matched by $5.0\,\text{A}$ out, and $2.0\,\text{A}$ already leaves by the second wire, leaving $3.0\,\text{A}$ out along the third.
  misconceptions:
    A: |-
      Adds the two given currents instead of subtracting. Only the $5.0\,\text{A}$ arrives; the $2.0\,\text{A}$ is part of it leaving, not extra charge coming in.
    B: |-
      Gets the size right but the direction wrong, treating every unknown current as an inflow. If $3.0\,\text{A}$ also flowed in, $8.0\,\text{A}$ would arrive and only $2.0\,\text{A}$ leave.
    C: |-
      Makes both errors at once: adds the currents and calls the result an inflow.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground at dusk with floodlights, an electronic scoreboard, glowing stumps and an umpire holding a light meter](scenes/cricket/current_electricity.svg "One scoreboard, and tonight two different battery packs wired to it at once.")

The scoreboard's battery pack won't last a full day-night match, so the club buys a second one. On the morning of the game the two packs sit on the pavilion floor, cables out, and nobody can agree on the wiring.

"Just connect both to the board," says the captain, Zoya. "Two packs, twice the power."

Her uncle Vikram, who wires houses for a living, connects them and clamps his meter round each cable in turn. The older pack is pushing out about twice as much current as the new one, even though both are wired to the same two terminals.

Zoya tries to work it out with the rules she knows — resistors in series add, resistors in parallel take reciprocals — and gets nowhere. There is no pair of resistors here that is purely in series or purely in parallel; each branch has its own source pushing back against the other.

The series and parallel rules have run out. Something more general is needed.

## The physics

Two rules, stated by Gustav Kirchhoff in 1845, handle any network however tangled.

**The junction rule.** At any junction, the sum of currents entering equals the sum of currents leaving:

$$\sum I_\text{in} = \sum I_\text{out}$$

This is **conservation of charge**: charge cannot pile up at a point in a steady current.

**The loop rule.** Round any closed loop, the algebraic sum of the changes in potential is zero:

$$\sum \Delta V = 0$$

This is **conservation of energy**: come back to where you started and you are back at the same potential.

![The junction rule with currents in equalling currents out, and the loop rule with the sign convention for crossing a resistor and a cell](figures/kirchhoffs_rules/junction-and-loop-rules.svg "Signs are the whole battle: fix a walking direction first, then apply the same rule at every component.")

The signs are where marks are lost, so fix them before you write anything:

- choose a direction for the current in each branch — **guess freely**, because a wrong guess simply comes out negative;
- choose a direction to walk round each loop;
- crossing a resistor **with** the current, the potential drops: $-IR$. Against it: $+IR$;
- crossing a cell from its $-$ terminal to its $+$ terminal: $+\varepsilon$. The other way: $-\varepsilon$.

Write one junction equation per junction (one fewer than the number of junctions is enough) and one loop equation per independent loop, until you have as many equations as unknown currents. Then solve.

## Worked example

**Given:** two packs feeding the scoreboard. Pack 1 has emf $10\,\text{V}$ with $2\,\Omega$ in its branch; pack 2 has $9\,\text{V}$ with $3\,\Omega$ in its branch (the internal resistance and cable, together). Both branches meet at a junction and feed the scoreboard, which behaves as a $2\,\Omega$ resistor. Values are illustrative.
**Find:** the current out of each pack.

**Step 1 — the junction.** Call the currents leaving the packs $I_1$ and $I_2$. Both arrive at the junction, so the scoreboard carries $I_1 + I_2$.

**Step 2 — the loop through pack 1 and the scoreboard.** Walking round it, the $10\,\text{V}$ of emf must be used up by the two resistors:

$$10 = 2I_1 + 2(I_1 + I_2)$$

**Step 3 — the loop through pack 2 and the scoreboard.**

$$9 = 3I_2 + 2(I_1 + I_2)$$

**Step 4 — solve.** Tidying gives $4I_1 + 2I_2 = 10$ and $2I_1 + 5I_2 = 9$. These are satisfied by

$$I_1 = 2\,\text{A}, \qquad I_2 = 1\,\text{A}$$

The older, stronger pack supplies twice as much as the other — exactly what Vikram's meter showed — and the scoreboard receives $3\,\text{A}$.

**Sanity check:** the scoreboard's potential difference is $3 \times 2 = 6\,\text{V}$, and each branch agrees: $10 - 2(2) = 6$ and $9 - 3(1) = 6$.

## Where the picture breaks

The pavilion circuit is real, not an analogy for anything in cricket. What is idealised is the wiring: connecting cables are taken as resistanceless, and each pack's internal resistance is rolled into one branch resistance that is really a mix of chemistry and cable. Both rules also assume a **steady** current — with rapidly changing currents, changing magnetic fields make the loop rule need a correction you will meet in Class 12 electromagnetism. And in real life, connecting two unequal packs across the same terminals is a bad idea: as the stronger one runs down, current can be driven backwards through the other.

## Key takeaway

Kirchhoff's junction rule says current in equals current out at every junction (charge is conserved); his loop rule says the potential changes round any closed loop sum to zero (energy is conserved). Together they solve any network, including ones with several sources where series and parallel rules fail. Guess current directions freely — a negative answer just means the arrow points the other way.
