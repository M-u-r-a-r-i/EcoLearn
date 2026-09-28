---
concept_id: capacitors_combination
interest: smartphones
format: explain
title: Two supercapacitors and a five-volt problem
check:
  question: |-
    Two $2\,\mu\text{F}$ capacitors are connected in series, and that pair is then connected in parallel with a $3\,\mu\text{F}$ capacitor. What is the equivalent capacitance?
  options:
    A: |-
      $7\,\mu\text{F}$
    B: |-
      $0.75\,\mu\text{F}$
    C: |-
      $4\,\mu\text{F}$
    D: |-
      $1.7\,\mu\text{F}$
  answer: C
  explanation: |-
    The series pair gives $\dfrac{1}{C} = \dfrac{1}{2} + \dfrac{1}{2}$, so $C = 1\,\mu\text{F}$. In parallel with $3\,\mu\text{F}$, capacitances simply add: $1 + 3 = 4\,\mu\text{F}$.
  misconceptions:
    A: |-
      Adds all three as if they were all in parallel, ignoring that the first two are in series. Capacitors in series have a smaller combined capacitance than either one.
    B: |-
      Treats all three as one series chain, using the reciprocal rule for the $3\,\mu\text{F}$ capacitor too, although it is in parallel with the pair.
    D: |-
      Uses the rules for resistors: adds the series pair to get $4\,\mu\text{F}$, then combines that with $3\,\mu\text{F}$ by reciprocals. For capacitors the rules are the other way round.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a rainy window: a phone with raindrops on its screen being tapped by a finger, a metal biscuit tin with its lid off, a breadboard with two supercapacitor cells wired in a chain, a stylus and a fitness band with a small display](scenes/smartphones/potential_capacitance.svg "The two fat cylinders on the breadboard are supercapacitors, wired one after the other. Whether that was the right choice is this lesson's question.")

Harsh is building a torch for the school science fair that charges in under a minute from a phone's USB port and has no battery at all. The idea is to store the energy in **supercapacitors**: fat little cylinders that can take charge far faster than a battery can.

The electronics shop had exactly what he needed, he thought. He bought two. Each label reads **10 F, 2.7 V**.

At home he realises the problem. A USB port gives $5\,\text{V}$. Each cell must never be charged above $2.7\,\text{V}$. So he wires the two in a chain, one after the other, so the $5\,\text{V}$ is shared between them.

His friend Mansi checks the design and winces. "You know that halves your capacitance? You'll have *five* farads, not twenty."

Harsh frowns at the breadboard. He paid for twenty farads of capacitors. Where did half of them go — and is the chain the mistake, or the only thing that works?

## The physics

![Series: three capacitors in a chain with the same charge on each and voltages adding. Parallel: three side by side with the same voltage across each and charges adding.](figures/capacitors_combination/series-and-parallel.svg "Series: same Q, voltages add. Parallel: same V, charges add. The rules are the reverse of those for resistors.")

**In series.** Capacitors connected end to end carry the **same charge** $Q$: whatever charge the supply pushes onto the first plate induces an equal and opposite charge on the next, all along the chain. The voltages add:

$$V = V_1 + V_2 + \dots = \frac{Q}{C_1} + \frac{Q}{C_2} + \dots$$

Dividing by $Q$ gives

$$\frac{1}{C_\text{series}} = \frac{1}{C_1} + \frac{1}{C_2} + \dots$$

The combination is **smaller** than the smallest one — it behaves like a single capacitor with a wider gap. The payoff is that the voltage is shared between the capacitors.

**In parallel.** Capacitors connected side by side have the **same voltage** $V$. The charges add, $Q = C_1V + C_2V + \dots$, so

$$C_\text{parallel} = C_1 + C_2 + \dots$$

The combination is **larger** — like one capacitor with bigger plates.

These are the opposite of the rules for resistors, which is the commonest trap.

## Worked example

Harsh's two cells, $C_1 = C_2 = 10\,\text{F}$, each rated $2.7\,\text{V}$ (illustrative values), charged from $5.0\,\text{V}$.

**Step 1 — the series capacitance.**

$$\frac{1}{C} = \frac{1}{10} + \frac{1}{10} = \frac{2}{10} \quad\Rightarrow\quad C = 5\,\text{F}$$

**Step 2 — the charge at 5 V.**

$$Q = CV = 5 \times 5.0 = 25\,\text{C}$$

The same $25\,\text{C}$ sits on each cell.

**Step 3 — the voltage on each cell.**

$$V_1 = \frac{Q}{C_1} = \frac{25}{10} = 2.5\,\text{V}$$

Each cell gets $2.5\,\text{V}$, safely under its $2.7\,\text{V}$ limit.

**Step 4 — the parallel alternative.** Side by side the cells make $20\,\text{F}$, but each would then feel the full $5\,\text{V}$ — nearly double its rating. Mansi's twenty farads were never usable from a USB port.

**Sanity check:** in series the two equal cells share the voltage equally, $2.5 + 2.5 = 5.0\,\text{V}$, as they must.

## Where the picture breaks

Real supercapacitors are not identical: their capacitances can differ by several per cent and they leak charge at different rates, so in a series chain one cell can slowly end up with more than its share of the voltage. Real designs add a small **balancing** circuit across each cell for that reason. Also, "charged from 5 V" hides a resistance and a current — how *fast* it charges belongs to the next chapter. And a supercapacitor stores its charge in an ultra-thin layer at the surface of a porous material, not across a neat gap between two plates; the series and parallel rules apply to it all the same.

## Key takeaway

In series, capacitors share the same charge and their voltages add: $\dfrac{1}{C} = \dfrac{1}{C_1} + \dfrac{1}{C_2} + \dots$, giving less capacitance but a higher total voltage rating. In parallel, they share the same voltage and their charges add: $C = C_1 + C_2 + \dots$. These are the reverse of the rules for resistors.
