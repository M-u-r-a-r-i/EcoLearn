---
concept_id: meter_bridge
interest: cricket
format: explain
title: Finding the mystery coil in a bail light with a metre of wire
check:
  question: |-
    In a metre bridge, a known resistance of $6.0\,\Omega$ is in the left gap and the unknown $S$ is in the right gap. The galvanometer reads zero when the jockey is at $30\,\text{cm}$ from the left end. $S$ is:
  options:
    A: |-
      $2.6\,\Omega$
    B: |-
      $6.0\,\Omega$
    C: |-
      $14\,\Omega$
    D: |-
      $20\,\Omega$
  answer: C
  explanation: |-
    $\dfrac{R}{S} = \dfrac{l}{100 - l}$, so $S = R\dfrac{100 - l}{l} = 6.0 \times \dfrac{70}{30} = 14\,\Omega$.
  misconceptions:
    A: |-
      Uses the ratio upside down, calculating $6.0 \times 30/70$. The shorter length sits beside the *smaller* resistance, so an unknown that balances at 30 cm must be the larger one.
    B: |-
      Assumes the balance means the two resistances are equal. They are equal only when the balance point is at the middle, $50\,\text{cm}$.
    D: |-
      Uses the whole $100\,\text{cm}$ instead of the remaining $70\,\text{cm}$: $6.0 \times 100/30$. The right-hand arm is only the wire beyond the jockey.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground at dusk with floodlights, an electronic scoreboard, glowing stumps and an umpire holding a light meter](scenes/cricket/current_electricity.svg "One of these bail lights has stopped working, and nothing on it is labelled.")

One of the club's lit bails has stopped flashing, and Kabir has opened it on the lab bench. Inside, next to the LED, is a small coil of fine wire with no marking of any kind — no colour bands, no printed value. To order a replacement, he needs to know its resistance.

The school's multimeter has been missing since the last inter-house tournament. What the lab does have, on the bench by the window, is a dusty wooden board: a metre of thin wire stretched over a scale, two brass gaps at the top, and a little sliding contact called a jockey.

Sneha, who is doing the ISC practical course, takes the coil from him, clips it into the right-hand gap, sets a known resistance in the left, and slides the jockey along the wire until the galvanometer needle sits dead still on zero. She reads one number off the scale — a length, in centimetres.

"Forty," she says. "So your coil is forty-five ohms." Kabir stares at the board. She measured a *length*. How did that become a resistance?

## The physics

A **metre bridge** (or slide-wire bridge) is a Wheatstone bridge in which two of the four arms are simply two parts of one long wire.

A uniform wire exactly $100\,\text{cm}$ long is stretched along a metre scale. The known resistance $R$ goes in the left gap, the unknown $S$ in the right gap. A cell drives current from one end of the wire to the other, and a galvanometer connects the point between the two gaps to a **jockey** that can touch the wire anywhere along it.

![A metre bridge: a one-metre uniform wire on a scale, a known resistance in the left gap, an unknown in the right gap, and a jockey at the balance point with the galvanometer reading zero](figures/meter_bridge/metre-bridge-setup.svg "The jockey's position splits the wire into the bridge's other two arms — so a length reading replaces a resistance reading.")

Slide the jockey until the galvanometer reads zero. If that happens at a distance $l$ from the left end, the wire's two parts have lengths $l$ and $(100 - l)$ centimetres, and they form the bridge's other two arms. Because the wire is uniform, $R_\text{wire} = \rho L/A$ makes each part's resistance simply proportional to its length — the same $\rho$ and the same $A$ all along. So the Wheatstone balance condition becomes

$$\frac{R}{S} = \frac{l}{100 - l} \qquad \Longrightarrow \qquad S = R\,\frac{100 - l}{l}$$

Everything awkward has cancelled: the wire's resistivity, its thickness, the cell's emf and the galvanometer's resistance all drop out. You are left measuring a length with a millimetre scale — something a school lab can do very well.

Two practical points. Tap the jockey on the wire, never drag it, or you wear the wire thin and spoil its uniformity. And choose $R$ so that the balance point lands near the **middle** of the wire: that is where a small error in $l$ costs you least, because near the ends a millimetre of scale is a large fraction of a short arm.

## Worked example

**Given:** Sneha's known resistance $R = 30\,\Omega$ in the left gap, with the balance point at $l = 40\,\text{cm}$.
**Find:** the coil's resistance $S$.

The wire beyond the jockey is $100 - 40 = 60\,\text{cm}$ long.

So the two parts are in the ratio $40 : 60$, or $2 : 3$ — the right-hand arm is one and a half times the left.

$$S = R\,\frac{100 - l}{l} = 30 \times \frac{60}{40} = 45\,\Omega$$

Forty-five ohms, exactly as Sneha said, from one reading on a ruler.

**Sanity check:** the balance point sits left of centre, so the right-hand arm is the longer one — and $S$ must be the larger resistance. It is.

## Where the picture breaks

The bail light gives the question, not the physics: a metre bridge has nothing to do with cricket, and this is a case where the honest move is to teach the apparatus directly. The idealisations are in the apparatus itself. The wire is assumed perfectly uniform in thickness, which no real wire is; the thick brass strips and the soldered joints are assumed to have no resistance of their own (they do — the **end corrections** your practical asks you to measure); and the wire must not be left carrying current for long, because it warms and its resistance drifts. A metre bridge also works poorly for very small or very large unknowns, since the balance point then crowds into one end of the scale.

## Key takeaway

A metre bridge replaces two arms of a Wheatstone bridge with the two parts of one uniform wire, so resistance is proportional to length. At the null point, $\dfrac{R}{S} = \dfrac{l}{100 - l}$, giving $S = R(100-l)/l$ from a single length reading. Aim for a balance near the middle of the wire, where the measurement is least sensitive to error.
