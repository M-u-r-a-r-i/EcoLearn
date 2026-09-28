---
concept_id: resistors_combination
interest: smartphones
format: explain
title: Making the resistor you need from a bag of ones you have
check:
  question: |-
    A USB gadget kit has three identical $30\,\Omega$ resistors. One is connected in series with the other two, which are in parallel with each other. What is the equivalent resistance?
  options:
    A: |-
      $90\,\Omega$
    B: |-
      $10\,\Omega$
    C: |-
      $15\,\Omega$
    D: |-
      $45\,\Omega$
  answer: D
  explanation: |-
    The parallel pair gives $\dfrac{1}{R_p} = \dfrac{1}{30} + \dfrac{1}{30}$, so $R_p = 15\,\Omega$. That is in series with the third resistor: $15 + 30 = 45\,\Omega$.
  misconceptions:
    A: |-
      Adds all three as if they were in series. The parallel pair offers two paths side by side, which lowers their combined resistance rather than adding to it.
    B: |-
      Treats all three as if they were in parallel. Only two of them share the same pair of points; the third carries the whole current on its own.
    C: |-
      Correctly finds the parallel pair's $15\,\Omega$ but forgets the series resistor. The whole current must still pass through the third $30\,\Omega$ as well.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A charging corner: a phone on a wall charger, a power bank charging an earbuds case through a small USB meter, and a smartwatch on its charging puck, with current arrows on the cables](scenes/smartphones/current_electricity.svg "One charger, several devices: some share a current, some share a voltage, and the difference decides everything.")

The electronics club is building USB-powered charging-status lights, and Tanvi's circuit needs a $50\,\Omega$ resistor. The club's parts box has hundreds of resistors — every single one of them $100\,\Omega$.

"Cut one in half?" suggests Joseph, not entirely joking.

Tanvi has a better instinct. Two resistors joined end to end must make something bigger, she reasons — so joined some *other* way, might they make something smaller? It feels like cheating: how can adding a second resistor to a circuit make the total resistance go *down*?

Meanwhile Joseph has spotted something on the club's power strip. The phone charger and the club's laptop are plugged in side by side, and switching one off does not dim the other.

Two ways of joining things. What does each do to the resistance — and to the current?

## The physics

**In series**, components are joined end to end, so there is only one path: the **same current** $I$ passes through each. The voltages across them add up to the total, $V = IR_1 + IR_2 + \dots$, so the equivalent resistance is

$$R_s = R_1 + R_2 + R_3 + \dots$$

Series resistance is always larger than the largest single resistor — more obstacles along one path.

**In parallel**, components are connected across the same two points, so each has the **same voltage** $V$. The currents in the branches add up to the total, $I = V/R_1 + V/R_2 + \dots$, so

$$\frac{1}{R_p} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots$$

Parallel resistance is always smaller than the smallest single resistor — each extra branch is an extra path, and more paths let more current through for the same voltage. For two resistors, $R_p = \dfrac{R_1 R_2}{R_1 + R_2}$; for $n$ identical resistors $R$, $R_p = R/n$.

![Resistors in series along one path, and resistors in parallel across the same two points](figures/resistors_combination/series-and-parallel.svg "Series shares the current and splits the voltage; parallel shares the voltage and splits the current.")

That answers Joseph's power strip, too: the sockets are in parallel, so each device gets the full mains voltage and switching one off leaves the others untouched.

For a mixed network, reduce it step by step: replace each clear series or parallel group by its equivalent, and repeat.

## Worked example

**Given:** two of the club's $100\,\Omega$ resistors and a USB port supplying $5.0\,\text{V}$.
**Find:** the equivalent resistance and the current from the port, with the pair (a) in series and (b) in parallel.

(a) In series, $R_s = 100 + 100 = 200\,\Omega$, so the current is

$$I = \frac{V}{R_s} = \frac{5.0}{200} = 0.025\,\text{A} = 25\,\text{mA}$$

One path, twice the obstacle, half the current one resistor would take.

(b) In parallel, $R_p = \dfrac{100}{2} = 50\,\Omega$ — exactly Tanvi's missing value. The current is

$$I = \frac{5.0}{50} = 0.10\,\text{A} = 100\,\text{mA}$$

Each branch has the full $5.0\,\text{V}$ across it and takes $5.0/100 = 50\,\text{mA}$; the two branches add to $100\,\text{mA}$.

**Sanity check:** $50\,\Omega$ is below the smallest resistor, $100\,\Omega$, as any parallel combination must be — adding a path can only make it easier for charge to get through.

## Where the picture breaks

The resistor box is real, but "resistance goes down when you add a resistor" needs care: it goes down only when the new one is added *in parallel*. Added in series, it goes up.

The idealisation is the wiring. We treat the connecting wires as having zero resistance, which is fine for a breadboard but not for a long, thin charging cable, which is itself a resistance in series with everything.

And a real power strip is parallel for a good reason and with a real limit: every device added draws extra current through the strip's single supply cable, so too many heavy devices can overload it even though each socket is fine.

## Key takeaway

In series the same current flows through every resistor and $R_s = R_1 + R_2 + \dots$; in parallel every resistor has the same voltage and $1/R_p = 1/R_1 + 1/R_2 + \dots$. Series totals are larger than any part, parallel totals are smaller than any part, and mixed networks are reduced one group at a time.
