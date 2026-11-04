---
concept_id: meter_bridge
interest: football
format: explain
title: A ruler that beats the lab's digital meter
check:
  question: |-
    In a metre bridge a known resistance of $4\,\Omega$ is in the left gap and an unknown $X$ in the right gap. The galvanometer reads zero when the jockey is $40\,\text{cm}$ from the left end. $X$ is:
  options:
    A: |-
      $2.7\,\Omega$
    B: |-
      $1.6\,\Omega$
    C: |-
      $10\,\Omega$
    D: |-
      $6\,\Omega$
  answer: D
  explanation: |-
    The balance point splits the wire into $40\,\text{cm}$ on the known side and $60\,\text{cm}$ on the unknown side, so $X = R\dfrac{100 - l}{l} = 4 \times \dfrac{60}{40} = 6\,\Omega$.
  misconceptions:
    A: |-
      Inverts the length ratio, using $l/(100-l)$. Each resistance is paired with the length of wire on *its own* side of the balance point, and the unknown's side is $60\,\text{cm}$.
    B: |-
      Multiplies the known resistance by the balance length as a fraction of the whole wire, $4 \times 0.40$. The bridge compares the two *parts* of the wire with each other, not one part with the whole.
    C: |-
      Uses the full $100\,\text{cm}$ instead of the $60\,\text{cm}$ on the unknown's side. The wire beyond the jockey is a separate arm of the bridge, not part of the same one.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night with two lit pylons, an electronic scoreboard, a fourth official holding a glowing LED substitution board, and a pitch-side distribution box with cables running to the lights](scenes/football/current_electricity.svg "When the old scoreboard was replaced, its insides went into a box in the school lab.")

When the club put up the new scoreboard, the old one was stripped and the interesting-looking pieces ended up in a cardboard box in the school physics lab. On practical day, Kavya's group is handed a small coil from that box. No markings, no colour code, nothing. Find its resistance.

They start with the digital multimeter from the drawer. First reading: $3.9\,\Omega$. They press the probes on again: $4.6\,\Omega$. Again: $4.1\,\Omega$. Kavya touches the two probes to each other, with no coil at all in between, and the meter still insists on $0.7\,\Omega$.

Their teacher, Mr Dinesh, does not seem remotely concerned. He puts a wooden board on the bench: a metre of thin wire stretched along a metre scale, two gaps with screw terminals, a cell, and a small sliding contact with a wire trailing to a galvanometer.

"Use this," he says, "and a ruler."

The multimeter cost several thousand rupees and has a screen. The board is a piece of wire and a ruler. Kavya cannot see how the ruler is supposed to win.

## The physics

A **metre bridge** is a Wheatstone bridge in which two of the four arms are simply two parts of one wire.

![A metre bridge: a one metre uniform wire with a metre scale, a known resistance in the left gap, an unknown in the right gap, a jockey touching the wire at the balance point and a galvanometer reading zero](figures/meter_bridge/metre-bridge-setup.svg "The jockey's position splits the wire into the bridge's other two arms — so a length reading replaces a resistance reading.")

A known resistance $R$ goes in the left gap and the unknown $X$ in the right gap; those are two arms of the diamond. The other two are the stretch of wire to the left of the sliding **jockey** and the stretch to its right. A cell drives current from one end of the wire to the other, and the galvanometer connects the point between $R$ and $X$ to the jockey.

Because the wire is **uniform**, $R = \rho L/A$ says its resistance is proportional to its length: $\rho$ and $A$ are the same all along it. So if the jockey balances at a distance $l$ (in centimetres) from the left-hand end, the two wire arms have resistances in the ratio $l : (100 - l)$.

Now apply the Wheatstone balance condition, which says the two branches must be split in the same ratio:

$$\frac{R}{X} = \frac{l}{100 - l} \qquad \Rightarrow \qquad X = R\,\frac{100 - l}{l}$$

Everything awkward has cancelled: the resistivity of the wire, its thickness, the emf of the cell, and the galvanometer's own resistance. The unknown depends on one resistance you trust and one length you can read off a scale.

That is why the ruler wins. The multimeter has to push a current through the coil *and through the probes and their contacts*, and it reports the lot — Kavya's $0.7\,\Omega$ of nothing at all. The bridge never asks the galvanometer to report a number. It asks only "is this zero?", and the jockey's position carries the answer.

## Worked example

**Given:** a known resistance $R = 6\,\Omega$ in the left gap, and the galvanometer reading zero with the jockey at $l = 60\,\text{cm}$.
**Find:** the unknown resistance $X$ in the right gap.

First read the wire. The jockey at $60\,\text{cm}$ leaves $100 - 60 = 40\,\text{cm}$ on the unknown's side, so the two wire arms are in the ratio $60 : 40$, which is $3 : 2$.

The unknown's arm is the *shorter* one, so $X$ must be the smaller resistance — smaller than $6\,\Omega$ by the same factor of $3:2$:

$$X = R\,\frac{100 - l}{l} = 6 \times \frac{40}{60} = 4\,\Omega$$

**Sanity check:** the balance point sat past the middle, on the known side, which is exactly where it should sit when the known resistance is the bigger of the two.

## Where the picture breaks

The scoreboard is only how the coil got into the lab; nothing here is a football analogy. The real limits are in the apparatus. The wire is assumed perfectly uniform, and it is not quite — a good practical repeats the reading with $R$ and $X$ swapped between the gaps and averages, which cancels most of that error. The screw terminals and the jockey contact add **end resistances** that the theory ignores. The bridge is also least accurate when the balance point crowds towards either end, so you choose $R$ to bring the null near the middle of the wire, where a millimetre of misjudgement costs the least. And the jockey should be tapped, not dragged: dragging scrapes the wire thinner in places, which quietly destroys the uniformity everything depends on.

## Key takeaway

A metre bridge is a Wheatstone bridge whose two lower arms are the two parts of a uniform metre wire, so their resistances are in the ratio of their lengths. At balance, $X = R(100 - l)/l$, with $l$ in centimetres from the end next to $R$. The cell's emf, the wire's material and the galvanometer's resistance all cancel — which is why a known resistance and a ruler beat a cheap meter that has to include its own contacts in the reading.
