---
concept_id: wheatstone_bridge
interest: football
format: explain
title: The instrument whose whole job is to read nothing
check:
  question: |-
    A Wheatstone bridge is balanced with $P = 10\,\Omega$, $Q = 20\,\Omega$ and $R = 15\,\Omega$. The fourth arm $S$ is:
  options:
    A: |-
      $30\,\Omega$
    B: |-
      $7.5\,\Omega$
    C: |-
      $45\,\Omega$
    D: |-
      $15\,\Omega$
  answer: A
  explanation: |-
    The balance condition is $\dfrac{P}{Q} = \dfrac{R}{S}$, so $S = \dfrac{QR}{P} = \dfrac{20 \times 15}{10} = 30\,\Omega$.
  misconceptions:
    B: |-
      Turns the ratio upside down, computing $PR/Q$. $P$ and $R$ are on *different* sides of the bridge, so they cannot both end up on top.
    C: |-
      Adds the three known arms. Balance is a condition on a ratio, not on a total — doubling every arm leaves a bridge just as balanced.
    D: |-
      Assumes balance means the two branches have the same total resistance, $P + Q = R + S$, giving $S = 30 - 15$. It is the *ratio* of the two arms within each branch that must match, so that the two midpoints sit at the same potential.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night with two lit pylons, an electronic scoreboard, a fourth official holding a glowing LED substitution board, and a pitch-side distribution box with cables running to the lights](scenes/football/current_electricity.svg "The equipment room behind the stand is quieter than the floodlights, and considerably stranger.")

At the district trials camp, every player does a standing jump on a force plate — a flat steel platform wired to a laptop, which turns the push of their legs into a number.

Anaya has jumped, landed, and is now standing to one side watching the readout between attempts. What she notices is the *zero*. With nobody on the plate the display says 0.0 and stays there, absolutely still. The cheap bathroom scale in the physio's room, two metres away, cannot manage that; left alone it wanders between 0.1 and 0.3 all morning.

The coach lets her open the plate's junction box at lunchtime. Inside there is no chip doing anything clever — just four resistors wired into a diamond, a cell across one diagonal and a sensitive meter across the other, and that meter is reading zero.

Which seems mad. Somebody has built a measuring instrument whose entire purpose, when it is working properly, is to tell you nothing at all. Why would that be *more* accurate than a meter with a number on it?

## The physics

A **Wheatstone bridge** is four resistances $P$, $Q$, $R$ and $S$ arranged in a diamond. A cell with a key sits across one diagonal, and a sensitive galvanometer across the other.

![A Wheatstone bridge drawn as a diamond: four resistors P, Q, R and S, a galvanometer across the middle reading zero, and a cell with a key across the other diagonal](figures/wheatstone_bridge/wheatstone-bridge-balanced.svg "Adjust one arm until the galvanometer reads exactly zero; that null is what you are really measuring.")

Call the corners A, B, C and D, with the cell across A and C, the galvanometer across B and D, $P$ and $Q$ in the branch A–B–C, and $R$ and $S$ in the branch A–D–C.

The bridge is **balanced** when the galvanometer reads zero. That happens when B and D are at the same potential, and the condition follows in three lines.

If no current passes through the galvanometer, then the same current $I_1$ flows through $P$ and on through $Q$, and the same current $I_2$ flows through $R$ and on through $S$. Since B and D are at the same potential, the drop from A to B equals the drop from A to D, and the drop from B to C equals the drop from D to C:

$$I_1P = I_2R \qquad \text{and} \qquad I_1Q = I_2S$$

Divide the first by the second, and both currents cancel:

$$\frac{P}{Q} = \frac{R}{S}$$

That is the **balance condition**. Notice what has vanished: the currents, the emf of the cell and its internal resistance, and the resistance of the galvanometer. None of them appears. So the measurement does not depend on the cell staying steady or on the meter being calibrated — the galvanometer only ever has to answer one question, and it is a yes-or-no question: *is this zero?*

That is Anaya's answer. A meter that must report a number has to be calibrated, and its calibration drifts. A meter that only has to detect a null does not, and a sensitive one can spot a very small imbalance, so three known resistances hand you the fourth to high accuracy. Change one arm slightly — because a strain gauge on a steel plate stretches when somebody stands on it — and the galvanometer swings off zero by an amount that measures the change.

## Worked example

**Given:** a balanced bridge with $P = 4\,\Omega$ and $Q = 6\,\Omega$ in one branch, and an adjustable standard $R = 12\,\Omega$ in the other.
**Find:** the unknown resistance $S$.

The two arms of the first branch are in the ratio $P : Q = 4 : 6$, that is $2 : 3$. At balance the second branch must be split in exactly the same ratio, so $S$ has to be one and a half times $R$.

Putting that through the condition:

$$S = R\,\frac{Q}{P} = 12 \times \frac{6}{4} = 18\,\Omega$$

**Sanity check:** $12$ and $18$ are in the ratio $2 : 3$, matching $4$ and $6$ — and the answer came out bigger than $R$, which is what a $Q$ larger than $P$ demands.

## Where the picture breaks

The camp is the setting; there is no analogy between a bridge circuit and anything on a pitch, and the physics belongs to the apparatus. The idealisations are worth naming. Connecting wires and contacts are taken as resistanceless, which matters when the arms themselves are small — a fraction of an ohm in a lead is invisible next to $1000\,\Omega$ and fatal next to $1\,\Omega$. The bridge is also least sensitive when the four arms are wildly different, so a good measurement keeps them within about a factor of ten of each other. And the balance condition says nothing about how *fast* the galvanometer settles: tapping the key briefly, rather than leaving it closed, is what stops the arms heating up and shifting their own resistances while you work.

## Key takeaway

A Wheatstone bridge is four resistances in a diamond, with a cell across one diagonal and a galvanometer across the other. At balance the galvanometer reads zero and $P/Q = R/S$, so three known arms give the fourth. Because the balance condition contains neither the cell's emf nor the galvanometer's resistance, a null measurement is far more trustworthy than reading a number off a meter.
