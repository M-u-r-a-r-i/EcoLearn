---
concept_id: wheatstone_bridge
interest: smartphones
format: explain
title: Weighing a battery's temperature sensor with a zero
check:
  question: |-
    In a Wheatstone bridge the ratio arms are $P = 100\,\Omega$ and $Q = 500\,\Omega$. The galvanometer reads zero when the known arm is set to $R = 300\,\Omega$. The unknown resistance $S$ is:
  options:
    A: |-
      $60\,\Omega$
    B: |-
      $1500\,\Omega$
    C: |-
      $700\,\Omega$
    D: |-
      $300\,\Omega$
  answer: B
  explanation: |-
    At balance $\dfrac{P}{Q} = \dfrac{R}{S}$, so $S = \dfrac{QR}{P} = \dfrac{500 \times 300}{100} = 1500\,\Omega$.
  misconceptions:
    A: |-
      Inverts the ratio, $S = RP/Q$. Since $Q$ is five times $P$, $S$ must be five times $R$, not a fifth of it.
    C: |-
      Thinks balance means the two paths have equal total resistance, $P + S = Q + R$. Balance means the *ratios* match, so that the two middle points sit at the same potential.
    D: |-
      Assumes that at balance the known and unknown arms must be equal. That is only true when the ratio arms are equal; here $P$ and $Q$ differ.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A charging corner: a phone on a wall charger, a power bank charging an earbuds case through a small USB meter, and a smartwatch on its charging puck, with current arrows on the cables](scenes/smartphones/current_electricity.svg "Somewhere inside each of these batteries is a tiny resistor whose only job is to report the temperature.")

Pooja's phone slows its charging whenever the battery gets hot. When her physics teacher, Mr. Das, brings a dismantled battery pack to class, she finally sees how it knows: next to the cell is a speck of a component with two thin leads — a **thermistor**, a resistor whose resistance falls sharply as it warms.

Mr. Das wants the class to measure its resistance precisely, at room temperature and then warmed between two fingers. Pooja reaches for the digital multimeter.

"Not today," he says, and hands her a diamond of four resistors, a cell and a galvanometer. "This one doesn't read a number off a dial. You find the answer when the needle does *nothing at all*."

Pooja is unconvinced. How can a meter that reads zero tell you anything — let alone a resistance?

## The physics

Four resistances $P$, $Q$, $R$ and $S$ are joined in a diamond ABCD. A cell drives current in at A and out at C. A sensitive **galvanometer** bridges the other two corners, B and D. $P$ and $Q$ are the **ratio arms**, $R$ is a known adjustable resistance, and $S$ is the unknown.

![A Wheatstone bridge drawn as a diamond of four resistors with a galvanometer across the middle reading zero and a cell across the other diagonal](figures/wheatstone_bridge/wheatstone-bridge-balanced.svg "Adjust the known arm until the galvanometer reads exactly zero; that null, not a dial reading, is what you are measuring.")

Adjust $R$ until the galvanometer reads **zero**. The bridge is then **balanced**, and two things follow:

- no current passes through the galvanometer, so the same current $I_1$ flows through $P$ and then $R$, and the same current $I_2$ through $Q$ and then $S$;
- no current through the galvanometer means no potential difference across it, so B and D are at the **same potential**.

Equal potentials at B and D mean the drops from A are equal, and so are the drops on to C:

$$I_1 P = I_2 Q \qquad \text{and} \qquad I_1 R = I_2 S$$

Dividing the first by the second, the currents cancel:

$$\frac{P}{Q} = \frac{R}{S} \qquad \Longrightarrow \qquad S = \frac{QR}{P}$$

That is the **balance condition**. The cell's emf, its internal resistance and the galvanometer's resistance appear nowhere in it. A **null method** only needs a detector that can tell zero from not-zero, which is why it is more precise than reading a pointer against a scale.

## Worked example

**Given:** Pooja sets the ratio arms to $P = 100\,\Omega$ and $Q = 1000\,\Omega$. At room temperature the galvanometer reads zero with $R = 1000\,\Omega$.
**Find:** the thermistor's resistance $S$.

The ratio arms are in the ratio $1 : 10$, so the unknown must be ten times the known arm:

$$S = \frac{QR}{P} = \frac{1000 \times 1000}{100} = 10\,000\,\Omega = 10\,\text{k}\Omega$$

Ten kilo-ohms — a typical size for this kind of sensor at room temperature.

Then she holds the thermistor between her fingers, and the bridge swings off balance. It balances again at $R = 700\,\Omega$, so now $S = 10 \times 700 = 7\,\text{k}\Omega$. The warmth of her fingers has cut its resistance by nearly a third — exactly what a semiconductor thermistor should do.

**Sanity check:** with $Q$ ten times $P$, the unknown arm must be ten times the known arm, and $10\,\text{k}\Omega$ is ten times $1000\,\Omega$.

## Where the picture breaks

The resistances here are illustrative. The bridge is the physics; the phone battery is only the reason to measure. Inside a real phone the thermistor is usually read by a simpler divider circuit and a chip that converts voltage to a number, not by someone balancing a bridge — but the bridge's null idea is used widely in precise sensors.

The balance condition assumes the bridge's resistances stay put while you measure. Here the current through the thermistor itself warms it slightly, so a careful measurement keeps the cell's current small.

And "zero" is only as good as the galvanometer: near balance, a small mismatch gives a deflection too small to see, which sets the precision.

## Key takeaway

A Wheatstone bridge is balanced when the galvanometer reads zero, which means its two middle points are at the same potential; then $P/Q = R/S$, so an unknown resistance is $S = QR/P$. Because it measures a null, the result does not depend on the cell's emf or the galvanometer's calibration.
