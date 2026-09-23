---
concept_id: kirchhoffs_rules
interest: football
format: explain
title: The pump, the panel and a current that came out negative
check:
  question: |-
    You solve a two-loop circuit with Kirchhoff's rules and one of the branch currents comes out as $-2\,\text{A}$. This means:
  options:
    A: |-
      there is an arithmetic mistake, because a current cannot be negative
    B: |-
      a current of $2\,\text{A}$ flows in that branch, opposite to the direction you assumed
    C: |-
      a current of $2\,\text{A}$ flows, and the cell in that branch has reversed its polarity
    D: |-
      no current flows in that branch
  answer: B
  explanation: |-
    The direction of each branch current is a guess you make before writing the equations. A negative answer is the algebra telling you the guess was backwards; the magnitude is still correct.
  misconceptions:
    A: |-
      Treats a minus sign as an error. Currents are given signed values *relative to an assumed direction*, so a negative result is a valid answer, not a failed one.
    C: |-
      Confuses the direction of the current with the polarity of the source. Nothing about the cell changes — only the arrow you drew was wrong, and a cell can perfectly well be driven backwards by a stronger source.
    D: |-
      Reads the minus sign as "nothing there". The size of the current is $2\,\text{A}$; only its direction is the opposite of what was assumed.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night with two lit pylons, an electronic scoreboard, a fourth official holding a glowing LED substitution board, and a pitch-side distribution box with cables running to the lights](scenes/football/current_electricity.svg "By day the same distribution box carries the irrigation pump — and, since last month, a solar panel too.")

The pitch needs watering every morning in summer, and the pump that does it used to run off a battery that somebody had to remember to charge. In June the club bolted a solar panel to the clubhouse roof and wired it to the same two terminals as the battery, so that the pump would run off sunlight and the battery would cover the cloudy days.

Vikram, the groundsman, switches it on at eleven and stands there with a clamp meter because the numbers make no sense to him. The panel's cable reads 4. The pump's cable reads 2. And the battery's cable, which he expected to read 2 as well, reads 2 in the wrong direction — the meter's arrow points *into* the battery.

His nephew Sameer, who is in Class 12, tries to work it out with the rules he knows. Resistances in series add; in parallel take reciprocals. He gets nowhere in about a minute, because there is no pair of components here that is purely in series or purely in parallel — each branch has a source of its own, pushing against the other.

Is the battery helping the pump, or is something else going on entirely?

## The physics

Two rules, published by Gustav Kirchhoff in 1845, handle any network however tangled.

**The junction rule.** At any junction, the total current arriving equals the total current leaving:

$$\sum I_\text{in} = \sum I_\text{out}$$

This is **conservation of charge** — in a steady current, charge cannot pile up at a point.

**The loop rule.** Round any closed loop, the algebraic sum of the changes in potential is zero:

$$\sum \Delta V = 0$$

This is **conservation of energy** — walk all the way round and you must arrive back at the potential you started from.

![The junction rule, with currents in equalling currents out, and the loop rule, with the sign convention for crossing a resistor and a cell](figures/kirchhoffs_rules/junction-and-loop-rules.svg "Signs are the whole battle: fix the directions first, then apply the same convention at every component.")

The signs are where marks are lost, so settle them before writing anything down:

- choose a direction for the current in each branch — **guess freely**, because a wrong guess simply comes out negative;
- choose a direction in which to walk round each loop;
- crossing a resistor **with** the current, the potential drops: $-IR$; against the current: $+IR$;
- crossing a cell from its $-$ plate to its $+$ plate: $+\varepsilon$; the other way: $-\varepsilon$.

Write one junction equation per junction (one fewer than the number of junctions is always enough) and one loop equation per independent loop, until you have as many equations as unknown currents. Then solve.

## Worked example

**Given:** the panel behaves as an $18\,\text{V}$ source with $1\,\Omega$ in its branch, the battery as a $12\,\text{V}$ source with $1\,\Omega$ in its branch, and the pump as a $7\,\Omega$ resistor. (Illustrative values; the resistances stand for internal resistance plus cable.)
**Find:** the current in each branch.

**Step 1 — guess and apply the junction rule.** Assume both sources push current *into* the top junction: $I_1$ from the panel, $I_2$ from the battery. Then the pump must carry $I_1 + I_2$ away from it.

**Step 2 — the loop through the panel and the pump.** The panel's emf is used up by its own $1\,\Omega$ and by the pump:

$$18 = I_1 + 7(I_1 + I_2)$$

**Step 3 — the loop through the battery and the pump.**

$$12 = I_2 + 7(I_1 + I_2)$$

**Step 4 — solve.** Tidying gives $8I_1 + 7I_2 = 18$ and $7I_1 + 8I_2 = 12$, and these are satisfied by

$$I_1 = 4\,\text{A}, \qquad I_2 = -2\,\text{A}$$

The minus sign is the answer to Vikram's puzzle. The battery is not helping the pump at all: $2\,\text{A}$ is flowing *into* it. The panel is supplying $4\,\text{A}$, sending $2\,\text{A}$ to the pump and charging the battery with the other $2\,\text{A}$.

**Sanity check:** the junction should sit at one definite potential, and every branch agrees on it — the pump has $7 \times 2 = 14\,\text{V}$ across it, the panel gives $18 - 4 = 14\,\text{V}$, and the battery, being charged, sits at $12 + 2 = 14\,\text{V}$.

## Where the picture breaks

The pump house is a real circuit, not an analogy for anything in football. What is idealised is the tidiness: connecting cables are treated as resistanceless, and each source's "$1\,\Omega$" bundles together internal resistance and wiring that are really separate. A solar panel is also not honestly a fixed emf with a fixed internal resistance — its output swings with the sunlight, and a real installation puts a charge controller between the panel and the battery precisely so that the charging current is regulated rather than left to whatever the algebra above produces. Both of Kirchhoff's rules also assume a **steady** current; with rapidly changing currents the loop rule needs a correction from changing magnetic fields, which you meet later in electromagnetism.

## Key takeaway

Kirchhoff's junction rule says the currents arriving at a junction equal those leaving (charge is conserved); the loop rule says the potential changes round a closed loop sum to zero (energy is conserved). Together they solve any network, including ones with several sources where the series and parallel rules fail. Guess the current directions freely — a negative answer just means that arrow points the other way.
