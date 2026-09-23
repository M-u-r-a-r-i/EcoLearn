---
concept_id: wheatstone_bridge
interest: cricket
format: explain
title: How the scales in the kit room weigh a ball to the gram
check:
  question: |-
    A Wheatstone bridge is balanced with $P = 10\,\Omega$ and $Q = 20\,\Omega$ in the ratio arms, and the known resistance $R = 15\,\Omega$. The unknown resistance $S$ is:
  options:
    A: |-
      $7.5\,\Omega$
    B: |-
      $30\,\Omega$
    C: |-
      $15\,\Omega$
    D: |-
      $45\,\Omega$
  answer: B
  explanation: |-
    At balance $\dfrac{P}{Q} = \dfrac{R}{S}$, so $S = \dfrac{QR}{P} = \dfrac{20 \times 15}{10} = 30\,\Omega$.
  misconceptions:
    A: |-
      Uses the ratio upside down, calculating $PR/Q$. Keep $P$ and $R$ on the same side of the bridge: $S$ is on $Q$'s side, so $Q$ multiplies.
    C: |-
      Thinks a zero galvanometer reading means the opposite arms are equal. Balance needs equal *ratios*, not equal resistances — equal arms are just the special case $P = Q$.
    D: |-
      Adds the three known resistances instead of using the ratio. The balance condition is multiplicative, not additive.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground at dusk with floodlights, an electronic scoreboard, glowing stumps and an umpire holding a light meter](scenes/cricket/current_electricity.svg "The electronics in the kit room are quieter than the floodlights, but stranger.")

Before a tournament, every match ball has to be checked: the Laws put a men's ball between $155.9\,\text{g}$ and $163\,\text{g}$. The club's kit room has a small digital scale for the job, and Meera notices it can tell a $159\,\text{g}$ ball from a $160\,\text{g}$ one without hesitating.

Pranav, who has taken the lid off an old one, tells her what is inside: no springs and no weights. Just a slim metal bar with four tiny foil patterns glued to it, wired into a diamond. When the ball presses down, the bar bends by a fraction of a millimetre, and the foils' resistance changes by about a **tenth of one per cent**.

Meera can't see how that helps. Their school ohmmeter cannot reliably tell $120\,\Omega$ from $120.1\,\Omega$ — its own reading wanders more than that when the battery warms up.

So how does a cheap circuit measure a change a good meter cannot even see?

## The physics

The trick is to stop measuring a resistance and start detecting a **zero**. That is what a **Wheatstone bridge** does.

Four resistances $P$, $Q$, $R$ and $S$ are connected in a diamond. A cell drives current in at one corner (A) and out at the opposite corner (C). A sensitive **galvanometer** bridges the other two corners, B and D.

![A Wheatstone bridge drawn as a diamond of four resistors with a galvanometer across the middle reading zero and a cell across the other diagonal](figures/wheatstone_bridge/wheatstone-bridge-balanced.svg "Adjust one arm until the galvanometer reads exactly zero; that null is what you are really measuring.")

Adjust one arm until the galvanometer reads **zero**. The bridge is then **balanced**, and at balance:

- no current flows through the galvanometer, so the same current $I_1$ flows through $P$ and then $R$, and the same current $I_2$ flows through $Q$ and then $S$;
- zero current through the galvanometer also means **no potential difference** across it, so B and D are at the same potential.

Equal potentials at B and D means the drops from A are equal, and so are the drops to C:

$$I_1 P = I_2 Q \qquad \text{and} \qquad I_1 R = I_2 S$$

Divide the first by the second, and the currents cancel:

$$\frac{P}{Q} = \frac{R}{S} \qquad \Longrightarrow \qquad S = \frac{QR}{P}$$

That is the **balance condition**, and notice what has vanished from it: the cell's emf, the cell's internal resistance and the galvanometer's resistance appear nowhere. A null method doesn't care how strong the battery is or how well the meter is calibrated — only that it can tell zero from not-zero. That is why the bridge beats a direct measurement, and why the smallest changes show up as the bridge going *off* balance.

## Worked example

**Given:** a bridge with ratio arms $P = 10\,\Omega$ and $Q = 20\,\Omega$, and a variable known resistance $R$. The galvanometer reads zero when $R$ is set to $30\,\Omega$.
**Find:** the unknown resistance $S$.

The ratio arms are in the ratio $P : Q = 1 : 2$ — so whatever $R$ is, $S$ must be twice it.

$$S = \frac{QR}{P} = \frac{20 \times 30}{10} = 60\,\Omega$$

Sixty ohms — about the resistance of a couple of metres of very fine wire, and a perfectly ordinary value for a strain-gauge element.

**Sanity check:** $S$ came out on the same side of the bridge as the larger ratio arm $Q$, and correspondingly larger than $R$ — which is what the ratio $1:2$ demands.

## Where the picture breaks

The scale is a real device, and no part of cricket behaves like a bridge circuit — trying to make the ball or the pitch stand in for a resistor would only mislead. The honest limits are practical. A bridge is precise only when the four arms are of comparable size; if $S$ is a thousand times $R$, the balance point becomes hopelessly insensitive, and very low or very high resistances need other methods. The derivation also assumes steady currents and resistances that hold still — but the gauges' resistance drifts with temperature, which is exactly why a real load cell uses four gauges arranged so that temperature changes affect all the arms together and cancel at the balance point. Finally, a working scale doesn't rebalance for every ball: it measures how far *off* balance the bridge has gone.

## Key takeaway

A Wheatstone bridge balances four resistances so that the galvanometer reads zero; at that null, $\dfrac{P}{Q} = \dfrac{R}{S}$, so an unknown $S = QR/P$. Because the balance condition contains neither the cell's emf nor the galvanometer's resistance, a null measurement is far more precise than reading a meter dial.
