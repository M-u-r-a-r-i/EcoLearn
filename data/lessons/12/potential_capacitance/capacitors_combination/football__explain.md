---
concept_id: capacitors_combination
interest: football
format: explain
title: Building an eight-microfarad capacitor out of a drawer of spares
check:
  question: |-
    A $6.0\,\mu\text{F}$ and a $3.0\,\mu\text{F}$ capacitor are connected in series across a battery. Which statement is correct?
  options:
    A: |-
      The equivalent capacitance is $2.0\,\mu\text{F}$, and the larger voltage sits across the $3.0\,\mu\text{F}$ capacitor.
    B: |-
      The equivalent capacitance is $9.0\,\mu\text{F}$, and both capacitors have the same voltage across them.
    C: |-
      The equivalent capacitance is $2.0\,\mu\text{F}$, and the larger voltage sits across the $6.0\,\mu\text{F}$ capacitor.
    D: |-
      The equivalent capacitance is $4.5\,\mu\text{F}$, and both capacitors carry the same charge.
  answer: A
  explanation: |-
    In series $\dfrac{1}{C} = \dfrac{1}{6.0} + \dfrac{1}{3.0} = \dfrac{3}{6.0}$, so $C = 2.0\,\mu\text{F}$. Both carry the same charge, and since $V = Q/C$, the smaller capacitance takes the bigger share of the voltage.
  misconceptions:
    B: |-
      Applies the parallel rules to a series chain — adding the capacitances and assuming equal voltages. In series the *charge* is shared and the voltages add.
    C: |-
      Gets the equivalent capacitance right but assumes the bigger capacitor takes the bigger voltage. With equal charges, $V = Q/C$ is largest across the smallest capacitance.
    D: |-
      Averages the two values instead of adding reciprocals. The equal-charge part is right, but a series combination is always smaller than the smallest capacitor in it.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground at dusk with a floodlight pylon, an electric fence and its energiser box along the far side, a coach holding a touchscreen tablet, a water bowser and an AED cabinet](scenes/football/potential_capacitance.svg "Behind every match morning is a store room of equipment somebody has to keep alive.")

The compressor in the store room is what inflates the match balls, and on Friday evening it stops starting. The motor hums, strains, and trips out.

Salim, who fixes everything at the club and is studying electronics at the polytechnic, unplugs it, waits, discharges the big capacitor with an insulated screwdriver and opens the cover. There it is: a small can with a domed top and a crust of dried paste. The label reads **8 μF**.

Rhea, the team's under-17 captain, counts the ball bag. Twenty balls, flat, for a district tournament that kicks off at nine.

The electrical shop opens Monday. The workshop drawer holds a $12\,\mu\text{F}$ can, a $4\,\mu\text{F}$ can and a $5\,\mu\text{F}$ can, all in good condition, and nothing that says $8$.

"Wire the twelve and the four so they take away from each other," Rhea suggests. "Twelve minus four."

Salim laughs, then stops, because he has two ways of joining capacitors and he suddenly wants to know exactly what each one does.

## The physics

**Parallel.** Connect capacitors side by side between the same two points. Each one then has the **same potential difference** $V$ across it, and each takes its own charge, $Q_1 = C_1V$, $Q_2 = C_2V$ and so on. The total charge drawn from the supply is

$$Q = Q_1 + Q_2 + Q_3 = (C_1 + C_2 + C_3)V$$

$$C_\text{parallel} = C_1 + C_2 + C_3$$

Connecting in parallel is like adding plate area, so the result is **bigger than the biggest** of them.

**Series.** Connect them end to end in a chain. Charge $+Q$ on the first plate induces $-Q$ on the plate facing it, which pushes $+Q$ onto the next capacitor, and so on down the line, so every capacitor in the chain carries the **same charge** $Q$. Their voltages add up to the supply voltage:

$$V = \frac{Q}{C_1} + \frac{Q}{C_2} + \frac{Q}{C_3}$$

$$\frac{1}{C_\text{series}} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3}$$

Connecting in series is like widening the gap, so the result is **smaller than the smallest**. These two rules are the reverse of the ones for resistors, which is exactly the trap most students fall into.

So Rhea's instinct was half right. There is no way to make capacitors subtract — but series *does* give you something smaller than either one.

![On the left, three capacitors in a series chain carrying the same charge with their voltages adding; on the right, three in parallel with the same voltage across each and their charges adding](figures/capacitors_combination/series-and-parallel.svg "Series: same charge, voltages add. Parallel: same voltage, charges add. Note that these are the opposite of the rules for resistors.")

## Worked example

Salim wires the $12\,\mu\text{F}$ and the $4\,\mu\text{F}$ in series, then puts the $5\,\mu\text{F}$ in parallel across that pair, and tests the lot on a $24\,\text{V}$ bench supply.

**Find** the equivalent capacitance, then the voltage across each capacitor.

**Step 1 — the series pair.** Add the reciprocals, then invert at the end:

$$\frac{1}{C} = \frac{1}{12} + \frac{1}{4} = \frac{1 + 3}{12} = \frac{4}{12} \quad\Rightarrow\quad C = 3\,\mu\text{F}$$

Smaller than either — as a series combination must be.

**Step 2 — add the parallel branch.** Now the capacitances simply add:

$$C_\text{eq} = 3 + 5 = 8\,\mu\text{F}$$

Which is exactly the value on the dead can. The compressor can run tomorrow.

**Step 3 — share out the voltage.** The series pair, as a $3\,\mu\text{F}$ unit across $24\,\text{V}$, carries $Q = CV = 3 \times 24 = 72\,\mu\text{C}$, and both capacitors in the chain carry that same $72\,\mu\text{C}$:

$$V_{12} = \frac{72}{12} = 6\,\text{V}, \qquad V_{4} = \frac{72}{4} = 18\,\text{V}$$

The small capacitor takes three quarters of the voltage. That is worth knowing before you pick parts: the $4\,\mu\text{F}$ can must be rated for $18\,\text{V}$, not for a quarter of the supply.

**Sanity check:** $6 + 18 = 24\,\text{V}$ across the chain, as it should be, and the $5\,\mu\text{F}$ branch sees the full $24\,\text{V}$ because it is straight across the supply.

## Where the picture breaks

The values here are illustrative, not from any real machine's manual. The rules assume ideal capacitors, and real ones leak: over minutes, unequal leakage pulls a series chain's voltages away from the neat split above, which is why engineers add balancing resistors or leave a wide margin. A motor capacitor also has to survive a mains-frequency alternating voltage and a rated current, so matching the microfarads alone is not enough — the voltage rating and the type matter too. And the first thing Salim did is the part to copy: unplug the machine and discharge the capacitor before touching anything. A charged capacitor can hold its charge long after the plug is out.

## Key takeaway

In parallel, the voltage is shared equally and the charges add: $C = C_1 + C_2 + \dots$, larger than the largest. In series, the charge is the same in every capacitor and the voltages add: $1/C = 1/C_1 + 1/C_2 + \dots$, smaller than the smallest. In a series chain the smallest capacitance always takes the largest share of the voltage.
