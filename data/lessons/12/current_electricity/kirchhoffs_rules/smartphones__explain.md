---
concept_id: kirchhoffs_rules
interest: smartphones
format: explain
title: The fresh cell that quietly charged the old one
check:
  question: |-
    A fully charged lithium cell ($4.2\,\text{V}$, internal resistance $0.1\,\Omega$) is wired in parallel with a half-empty one ($3.8\,\text{V}$, $0.1\,\Omega$), positive to positive, with nothing else connected. What current circulates between them?
  options:
    A: |-
      $40\,\text{A}$
    B: |-
      $0\,\text{A}$
    C: |-
      $4\,\text{A}$
    D: |-
      $2\,\text{A}$
  answer: D
  explanation: |-
    Walking round the single loop, you cross one cell from $-$ to $+$ ($+4.2\,\text{V}$) and the other from $+$ to $-$ ($-3.8\,\text{V}$), and both internal resistances: $4.2 - 3.8 - I(0.1 + 0.1) = 0$, so $I = 0.4/0.2 = 2\,\text{A}$.
  misconceptions:
    A: |-
      Adds the two emfs, $8.0/0.2$. Joined positive to positive, the cells face each other round the loop, so the loop rule gives their *difference*, not their sum.
    B: |-
      Thinks cells in parallel simply share a voltage and so nothing flows between them. That is true only when their emfs are equal; any difference drives a current round the loop.
    C: |-
      Divides the emf difference by only one internal resistance, $0.4/0.1$. The loop passes through both cells, so both internal resistances are in its path.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A charging corner: a phone on a wall charger, a power bank charging an earbuds case through a small USB meter, and a smartwatch on its charging puck, with current arrows on the cables](scenes/smartphones/current_electricity.svg "Where cables and cells branch and rejoin, the current has choices — and two sources can end up pushing against each other.")

For the school science fair, Varun is building a portable speaker in a wooden box. To make it last longer, he wires in two lithium cells side by side: a new one, fully charged, and an older one salvaged from a retired phone, about half empty.

The speaker plays nicely. But after a few minutes Varun puts his hand on the pack and frowns. The *old* cell is warm — warmer than the new one — and yet it can hardly be doing much work. The new cell is the strong one.

His teacher, Ms. Kulkarni, looks at the wiring and asks him a question instead of giving an answer. "Where do you think the new cell's current is going? All of it into the speaker?"

Two cells, one speaker, three branches of wire. How do you even work out which way the currents go in a circuit like that?

## The physics

Series and parallel rules cannot untangle a circuit with several sources in different branches. **Kirchhoff's rules** can — and they are nothing more than two conservation laws.

**Junction rule** (conservation of charge): at any junction, the total current flowing in equals the total current flowing out. Charge cannot pile up at a point.

**Loop rule** (conservation of energy): round any closed loop, the algebraic sum of the changes in potential is zero. Walk round a loop and you arrive back at the same potential.

![A junction with one current in and two out, and a loop containing a cell and a resistor, with the sign rules](figures/kirchhoffs_rules/junction-and-loop-rules.svg "The rules are easy; the signs are the whole battle. Fix every direction before you write a single equation.")

Signs, walking round a loop in a chosen direction:

- across a resistor **with** the current: $-IR$; **against** it: $+IR$;
- through a cell from $-$ to $+$: $+\varepsilon$; from $+$ to $-$: $-\varepsilon$.

The method: mark a current in every branch, guessing a direction for each. Write the junction rule at the junctions and the loop rule for enough independent loops. Solve. If a current comes out negative, it simply flows the other way.

## Worked example

**Given:** Varun's new cell, $\varepsilon_1 = 4.2\,\text{V}$, $r_1 = 0.1\,\Omega$; the old cell, $\varepsilon_2 = 3.8\,\text{V}$, $r_2 = 0.2\,\Omega$; both positive terminals joined to the speaker, which acts as $R = 4.0\,\Omega$ (illustrative values).
**Find:** the current in each branch.

Label $I_1$ out of the new cell's $+$ terminal, $I$ down through the speaker, and $I_2$ *into* the old cell's $+$ terminal.

1. Junction: $I_1 = I + I_2$.
2. Loop through the new cell and the speaker: $4.2 - 0.1\,I_1 - 4.0\,I = 0$.
3. Loop through the two cells: $4.2 - 0.1\,I_1 - 0.2\,I_2 - 3.8 = 0$, so $0.1\,I_1 + 0.2\,I_2 = 0.4$.
4. Solving the three together gives $I_1 = 2.0\,\text{A}$, $I = 1.0\,\text{A}$, $I_2 = 1.0\,\text{A}$.

So the new cell supplies $2.0\,\text{A}$, but only half goes to the speaker. The other $1.0\,\text{A}$ is driven backwards into the old cell — the new cell is charging it, uncontrolled, and that is the warmth Varun felt.

**Sanity check:** the speaker's pd is $4.0 \times 1.0 = 4.0\,\text{V}$; the new cell gives $4.2 - 2.0 \times 0.1 = 4.0\,\text{V}$ and the old one, being charged, takes $3.8 + 1.0 \times 0.2 = 4.0\,\text{V}$. All three branches agree, as they must between the same two points.

## Where the picture breaks

The values are illustrative, and the model treats each cell as a fixed emf and a fixed resistance. A real lithium cell's emf changes as it charges, so the backward current would shrink over time rather than stay at $1.0\,\text{A}$, and the speaker is not really a steady resistor.

The practical lesson is real, though: mismatched lithium cells should never be wired in parallel without a protection circuit. Real battery packs use matched cells and dedicated electronics precisely to prevent this uncontrolled charging.

## Key takeaway

Kirchhoff's junction rule (current in = current out) expresses conservation of charge; the loop rule (potential changes round any loop sum to zero) expresses conservation of energy. Mark each branch current, apply the sign rules consistently, and solve — a negative answer just means the current flows the other way.
