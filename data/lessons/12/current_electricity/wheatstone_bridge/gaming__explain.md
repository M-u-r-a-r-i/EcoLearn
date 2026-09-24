---
concept_id: wheatstone_bridge
interest: gaming
format: explain
title: The sim pedal that brakes by itself after an hour
check:
  question: |-
    A Wheatstone bridge is balanced. Which one of these changes would leave the galvanometer still reading exactly zero?
  options:
    A: |-
      doubling the resistance of one of the ratio arms
    B: |-
      replacing the unknown arm with a resistor of a different value
    C: |-
      replacing the driving cell with one of a different emf
    D: |-
      warming one arm alone, so that its resistance rises slightly
  answer: C
  explanation: |-
    The balance condition $\dfrac{P}{Q} = \dfrac{R}{S}$ contains only the four arms — no emf, no internal resistance, no galvanometer resistance. A stronger or weaker cell changes the currents but not the null.
  misconceptions:
    A: |-
      Overlooks that balance is a condition on the *ratio* $P/Q$. Doubling one ratio arm doubles that ratio, so the bridge goes off balance at once.
    B: |-
      Forgets that the unknown is one of the four resistances in the condition. Change it and the bridge has to be rebalanced — that is the whole point of the instrument.
    D: |-
      Misses that a bridge is built to *detect* exactly this. A resistance change in one arm breaks the balance; only a change shared by all four arms cancels out of the ratios.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A night gaming desk with a monitor showing a frame counter, a controller charging over a USB cable, a USB power meter, and an open PC case with a fan and a power supply](scenes/gaming/current_electricity.svg "The PC's exhaust blows warm air across the desk all evening — which turns out to matter.")

Shreyas builds his own brake pedal for his sim-racing rig over three weekends: a steel plate that bends a fraction of a millimetre under his foot, with a **strain gauge** glued to it — a foil zigzag whose resistance changes by a few parts in a thousand as the plate flexes.

For an hour it is perfect. Then, halfway through a long race, the game starts registering a light brake that he is not applying. He lifts his foot off entirely. The brake bar sits at four per cent, and slowly creeps upward.

Nothing is stuck. Nothing is loose. His friend Meghna, who does electronics, asks how many gauges he used.

"One," says Shreyas. "Why would I need four?"

She points at the PC exhaust, blowing warm air straight across his pedal plate all evening, and asks what else — apart from his foot — might be changing a gauge's resistance by a few parts in a thousand.

## The physics

The trick of the **Wheatstone bridge** is to stop measuring a resistance and start detecting a **zero**.

Four resistances $P$, $Q$, $R$ and $S$ are connected in a diamond. A cell drives current in at one corner (A) and out at the opposite corner (C). A sensitive **galvanometer** bridges the other two corners, B and D.

![A Wheatstone bridge drawn as a diamond of four resistors with a galvanometer across the middle reading zero and a cell across the other diagonal](figures/wheatstone_bridge/wheatstone-bridge-balanced.svg "Adjust one arm until the galvanometer reads exactly zero; that null, not a dial reading, is what you are measuring.")

Adjust one arm until the galvanometer reads **zero**. The bridge is then **balanced**, and at balance two things follow:

- no current passes through the galvanometer, so the same current $I_1$ goes through $P$ and then $R$, and the same current $I_2$ through $Q$ and then $S$;
- zero current through the galvanometer also means **no potential difference** across it, so B and D sit at the same potential.

Equal potentials at B and D means the drops from A are equal, and so are the drops on to C:

$$I_1 P = I_2 Q \qquad \text{and} \qquad I_1 R = I_2 S$$

Divide the first by the second and the currents cancel:

$$\frac{P}{Q} = \frac{R}{S} \qquad \Longrightarrow \qquad S = \frac{QR}{P}$$

That is the **balance condition**. Look at what has vanished from it: the cell's emf, the cell's internal resistance and the galvanometer's resistance appear nowhere. A null method does not care how strong the battery is or how well the meter is calibrated — only that it can tell zero from not-zero. That is why the bridge beats reading a dial.

And it answers Meghna's question. Warm *one* arm and its resistance alone changes, the ratio breaks, and the bridge swings off balance — indistinguishable from a brake press. But if all four arms are gauges on the same warm plate, every arm's resistance changes by the same factor, both ratios are untouched, and the temperature cancels exactly. Four gauges are not four times the sensitivity; they are a way of making the bridge blind to everything except the bending.

## Worked example

**Given:** Shreyas measures an unmarked replacement gauge with a lab bridge. The ratio arms are $P = 40\,\Omega$ and $Q = 10\,\Omega$, and the galvanometer reads zero when the variable known arm is set to $R = 480\,\Omega$.
**Find:** the gauge's resistance $S$.

The ratio arms are in the ratio $P : Q = 4 : 1$, so whatever $R$ is, $S$ must be a quarter of it.

$$S = \frac{QR}{P} = \frac{10 \times 480}{40} = 120\,\Omega$$

One hundred and twenty ohms — one of the standard values strain gauges are made in, so the replacement is the right part.

**Sanity check:** $S$ sits on the same side of the bridge as the *smaller* ratio arm $Q$, so it must be the smaller of the pair $R$ and $S$ — and it is, by the same factor of four.

## Where the picture breaks

The pedal is a real device, and nothing in racing itself behaves like a bridge circuit — trying to make the car or the track stand in for a resistor would only mislead.

The honest limits are practical. A bridge is precise only when the four arms are of comparable size; if $S$ were a thousand times $R$, the balance point would become hopelessly insensitive, and very small or very large resistances need other methods. The derivation also assumes steady currents and resistances that hold still while you balance.

And a working pedal never rebalances itself. It sits permanently slightly off balance and measures the small voltage across the galvanometer diagonal, which is *proportional to* the imbalance — the balance condition tells you where the zero is, and the instrument then lives just beside it. Finally, four gauges cancel temperature only if they really do share it: a gauge nearer the warm air still drifts, which is why they are mounted in pairs on opposite faces of the same piece of metal.

## Key takeaway

A Wheatstone bridge balances four resistances until the galvanometer reads zero; at that null, $\dfrac{P}{Q} = \dfrac{R}{S}$, so an unknown $S = QR/P$. Because the condition contains neither the cell's emf nor the galvanometer's resistance, a null measurement is far more precise than reading a meter — and any effect shared equally by all four arms cancels out of it entirely.
