---
concept_id: kirchhoffs_rules
interest: gaming
format: explain
title: Two supplies, one scoreboard, and a meter that reads 2, 1 and 3
check:
  question: |-
    You are applying Kirchhoff's loop rule and you walk round the loop **in the same direction** as the current $I$ through a resistor $R$. The term you write for that resistor is:
  options:
    A: |-
      $-IR$
    B: |-
      $+IR$
    C: |-
      $-I/R$
    D: |-
      zero, because a resistor contains no source of emf
  answer: A
  explanation: |-
    Current flows from higher to lower potential through a resistor, so travelling with the current means going *downhill* — a potential change of $-IR$. Crossing it against the current gives $+IR$.
  misconceptions:
    B: |-
      Has the sign inverted. $+IR$ is what you write when you cross the resistor *against* the current; going with the current is a drop.
    C: |-
      Uses an upside-down Ohm's law. The potential difference across a resistor is $IR$, not $I/R$; the sign is a separate question from the formula.
    D: |-
      Confuses "supplies no energy" with "changes no potential". Only cells contribute $\varepsilon$ terms, but resistors are precisely where the potential falls.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A night gaming desk with a monitor showing a frame counter, a controller charging over a USB cable with current arrows, a USB power meter, and an open PC case with a power supply](scenes/gaming/current_electricity.svg "When more than one source feeds the same pair of terminals, no amount of series-and-parallel arithmetic will tell you what each one is doing.")

The inter-school LAN final is in a hall with one reliable socket and a long history of power cuts. Priya, who is running the event, refuses to let the scoreboard panel go black in the middle of a decider, so she feeds it from two sources at once: the mains adapter, and a chunky power bank, both landing on the same pair of terminals behind the panel.

It works. Then Zoya, who has borrowed the lab's clamp meter for fun, reads all three cables and calls out the numbers: 2 on the adapter's cable, 1 on the power bank's, 3 on the panel's.

The 3 makes sense — it is the 2 and the 1 arriving together. The other two do not. Both sources land on the same two terminals, through cables of the same thickness. So why does one carry exactly twice as much as the other?

Zoya tries what she knows: resistances in series add, in parallel take reciprocals. Neither applies. Nothing here is purely in series or purely in parallel, because each branch has a source of its own.

## The physics

Two rules, published by Gustav Kirchhoff in 1845, handle any network however tangled.

**The junction rule.** At any junction, the total current arriving equals the total current leaving:

$$\sum I_\text{in} = \sum I_\text{out}$$

This is **conservation of charge**: in a steady current, charge cannot pile up at a point.

**The loop rule.** Around any closed loop, the algebraic sum of the potential changes is zero:

$$\sum \Delta V = 0$$

This is **conservation of energy**: walk all the way round and you must come back to the potential you started at.

![The junction rule with currents in equalling currents out, and the loop rule with the sign convention for crossing a resistor and a cell](figures/kirchhoffs_rules/junction-and-loop-rules.svg "The rules are easy; the signs are the whole battle. Fix every direction before you write a single equation.")

Settle the signs before writing anything:

- pick a direction for the current in each branch — **guess freely**, because a wrong guess simply comes out negative, with the right magnitude;
- pick a direction to walk round each loop;
- crossing a resistor **with** the current: $-IR$; **against** it: $+IR$;
- crossing a cell from its $-$ plate to its $+$ plate: $+\varepsilon$; the other way: $-\varepsilon$.

Then write one junction equation per junction (one fewer than the number of junctions is always enough) and one loop equation per independent loop, until the equations match the unknowns. Both rules assume a **steady** current.

## Worked example

**Given:** the adapter behaves as a $12\,\text{V}$ source with $3\,\Omega$ in its branch, the power bank as a $9\,\text{V}$ source with $3\,\Omega$ in its branch, and the panel as a $2\,\Omega$ resistor. (Illustrative; each $3\,\Omega$ bundles internal resistance and cable together.)
**Find:** the current in each branch.

**Step 1 — junction rule.** Assume both sources push current *into* the top terminal, $I_1$ from the adapter and $I_2$ from the bank. Then the panel carries $I_1 + I_2$ away from it.

**Step 2 — the loop through the adapter and the panel.**

$$12 = 3I_1 + 2(I_1 + I_2) \quad\Longrightarrow\quad 5I_1 + 2I_2 = 12$$

**Step 3 — the loop through the bank and the panel.**

$$9 = 3I_2 + 2(I_1 + I_2) \quad\Longrightarrow\quad 2I_1 + 5I_2 = 9$$

**Step 4 — solve.** Subtracting one from the other gives $3I_1 - 3I_2 = 3$, so $I_1 = I_2 + 1$. Putting that back into the first equation gives $7I_2 + 5 = 12$, and so

$$I_2 = 1\,\text{A}, \qquad I_1 = 2\,\text{A}, \qquad I_1 + I_2 = 3\,\text{A}$$

Exactly Zoya's three readings. The panel sits at $2 \times 3 = 6\,\text{V}$, and that is the answer to Priya's question: the adapter has $12 - 6 = 6\,\text{V}$ left over to push across its $3\,\Omega$, while the bank has only $9 - 6 = 3\,\text{V}$ — half as much spare push through the same resistance, so half the current.

**Sanity check:** every branch must agree on the terminal voltage, and all three do: $12 - 3(2) = 6$, $9 - 3(1) = 6$, and $2 \times 3 = 6\,\text{V}$.

## Where the picture breaks

The circuit is real; the tidiness is not. Lumping each source's internal resistance and its cable into one "$3\,\Omega$" hides two different things, and $3\,\Omega$ is generously large for a real adapter — chosen here to keep the arithmetic visible.

The bigger caution is practical. Tying two sources of different emf straight onto one pair of terminals is something the algebra permits and an engineer avoids. Switch the panel off in this circuit and the $12\,\text{V}$ source will simply drive current backwards into the $9\,\text{V}$ bank, which is why real backup setups put a diode or a proper UPS between the two rather than trusting the load to stay connected. A power bank also regulates its own output rather than behaving as a fixed emf with a fixed resistance.

Finally, both rules assume steady currents. With rapidly changing currents the loop rule needs a correction from changing magnetic fields, which you meet later in electromagnetism.

## Key takeaway

Kirchhoff's junction rule ($\sum I_\text{in} = \sum I_\text{out}$) is conservation of charge; the loop rule ($\sum \Delta V = 0$) is conservation of energy. Together they solve any network, including ones with several sources where series-and-parallel arithmetic simply does not apply. Choose directions first, keep the sign convention identical at every component, and let a negative answer tell you which arrow you drew backwards.
