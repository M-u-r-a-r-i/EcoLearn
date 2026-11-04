---
concept_id: capacitors_combination
interest: cricket
format: explain
title: Rebuilding a bowling machine's capacitor from a drawer of spares
check:
  question: |-
    Three $6.0\,\mu\text{F}$ capacitors are connected in series. What is their equivalent capacitance?
  options:
    A: |-
      $18\,\mu\text{F}$
    B: |-
      $0.50\,\mu\text{F}$
    C: |-
      $2.0\,\mu\text{F}$
    D: |-
      $6.0\,\mu\text{F}$
  answer: C
  explanation: |-
    In series, $\dfrac{1}{C} = \dfrac{1}{6.0} + \dfrac{1}{6.0} + \dfrac{1}{6.0} = \dfrac{3}{6.0} = 0.50\,\mu\text{F}^{-1}$, so $C = 2.0\,\mu\text{F}$.
  misconceptions:
    A: |-
      Adds the capacitances directly, which is the rule for parallel. Capacitors in series combine like resistors in parallel.
    B: |-
      Adds the reciprocals correctly but forgets to take the reciprocal of the sum at the end; $0.50$ is $1/C$, not $C$.
    D: |-
      Thinks that because every capacitor in series carries the same charge, the chain behaves like one capacitor. The voltages add, so the chain stores less charge per volt.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground under a storm cloud with lightning in the distance, a floodlight tower, a curator on the pitch, a car by the boundary and a photographer's flash](scenes/cricket/potential_capacitance.svg "Behind every net session is equipment that somebody has to keep running.")

It's Saturday evening at the academy, and the bowling machine has just died mid-session. Irfan, eighteen, helps the coaches and is the only one who is any good with electronics. With the machine unplugged, he opens the control box and finds it straight away: a capacitor with a bulging top. The service sheet says to replace it with **20 μF, rated for at least 50 V**.

The shop is shut until Monday. Twenty under-16 batters are booked for tomorrow morning.

In the workshop drawer: a strip of identical capacitors, each **10 μF, rated 25 V**, and a single 30 μF one.

"Two tens side by side make twenty," says his friend Kunal. "Done."

Irfan isn't so sure. What does "side by side" do to the voltage each capacitor has to survive? And if he chains them end to end instead, does the capacitance add up, or does something stranger happen?

## The physics

**Parallel.** Connect capacitors side by side between the same two points. Each has the **same potential difference** $V$ across it, and each takes its own charge: $Q_1 = C_1V$, $Q_2 = C_2V$, and so on. The total charge drawn is

$$Q = Q_1 + Q_2 + Q_3 = (C_1 + C_2 + C_3)V$$

$$C_\text{parallel} = C_1 + C_2 + C_3$$

Parallel is like adding plate area, so the result is **larger than the largest**.

**Series.** Connect capacitors end to end. Charge $+Q$ on the first plate induces $-Q$ on the facing plate, which pushes $+Q$ onto the next capacitor's plate, and so on. Every capacitor carries the **same charge** $Q$. The voltages add:

$$V = \frac{Q}{C_1} + \frac{Q}{C_2} + \frac{Q}{C_3}$$

$$\frac{1}{C_\text{series}} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3}$$

Series is like widening the gap, so the result is **smaller than the smallest**. It also shares out the voltage. That is the key to Irfan's problem.

![Series: three capacitors in a chain with the same charge on each and voltages adding. Parallel: three side by side with the same voltage across each and charges adding.](figures/capacitors_combination/series-and-parallel.svg "Series: same Q, voltages add. Parallel: same V, charges add. The rules are the reverse of those for resistors.")

## Worked example

**Given:** two $10\,\mu\text{F}$ capacitors in parallel, and this pair in series with the $30\,\mu\text{F}$ capacitor, across $12\,\text{V}$.
**Find:** the equivalent capacitance, the total charge, and the voltage and charge for each capacitor.

Parallel pair: $10 + 10 = 20\,\mu\text{F}$.

Pair in series with $30\,\mu\text{F}$:

$$\frac{1}{C} = \frac{1}{20} + \frac{1}{30} = \frac{3 + 2}{60} = \frac{5}{60} \quad\Rightarrow\quad C = 12\,\mu\text{F}$$

Total charge: $Q = CV = 12\,\mu\text{F} \times 12\,\text{V} = 144\,\mu\text{C}$. The $30\,\mu\text{F}$ capacitor and the pair, being in series, each carry this $144\,\mu\text{C}$.

- Across the $30\,\mu\text{F}$: $V = 144/30 = 4.8\,\text{V}$.
- Across the pair: $V = 144/20 = 7.2\,\text{V}$. Each $10\,\mu\text{F}$ holds $10 \times 7.2 = 72\,\mu\text{C}$.

**Sanity check:** $4.8 + 7.2 = 12\,\text{V}$ ✓ and $72 + 72 = 144\,\mu\text{C}$ ✓. And $12\,\mu\text{F}$ is smaller than both $20$ and $30\,\mu\text{F}$, as a series combination must be.

**Irfan's fix.** Kunal's parallel pair gives $20\,\mu\text{F}$, but each capacitor would face the full $50\,\text{V}$, twice its $25\,\text{V}$ rating. Two in series share the voltage, $25\,\text{V}$ each, but give only $5\,\mu\text{F}$. So Irfan builds **four** such series pairs and puts them in parallel: $4 \times 5 = 20\,\mu\text{F}$, with each capacitor seeing at most $25\,\text{V}$. That uses eight capacitors in total.

## Where the picture breaks

The numbers here are illustrative, not taken from any real machine's manual. The series rule assumes ideal capacitors. Real ones leak a little, and unequal leakage makes the voltage split unevenly over time, so engineers add resistors to balance them or leave a safety margin. Rather than run components at exactly their rated voltage, a technician would choose parts rated well above it. And any repair on mains-powered equipment should be done with the machine unplugged, and its large capacitors discharged, by someone trained to do it.

## Key takeaway

In parallel, the voltage is shared and the charges add: $C = C_1 + C_2 + \dots$. In series, the charge is shared and the voltages add: $1/C = 1/C_1 + 1/C_2 + \dots$. Series combinations have less capacitance but can withstand a higher total voltage.
