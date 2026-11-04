---
concept_id: emf_internal_resistance
interest: football
format: explain
title: Two packs read nine volts and only one of them works
check:
  question: |-
    A cell of emf $12\,\text{V}$ has an internal resistance of $1\,\Omega$. It is connected to a lamp of resistance $5\,\Omega$. The terminal potential difference is:
  options:
    A: |-
      $12\,\text{V}$
    B: |-
      $2.0\,\text{V}$
    C: |-
      $11\,\text{V}$
    D: |-
      $10\,\text{V}$
  answer: D
  explanation: |-
    The current is $I = \varepsilon/(R + r) = 12/6 = 2\,\text{A}$, so the volts lost inside are $Ir = 2 \times 1 = 2\,\text{V}$ and the terminal pd is $V = 12 - 2 = 10\,\text{V}$.
  misconceptions:
    A: |-
      Assumes the terminal pd always equals the emf. That is true only when the cell delivers no current; as soon as current flows, some potential is dropped inside the cell itself.
    B: |-
      Works out the volts lost inside the cell, $Ir = 2\,\text{V}$, and reports that as the terminal pd. It is what is *missing* from the terminals, not what is left at them.
    C: |-
      Subtracts the internal resistance in ohms from the emf in volts. You cannot subtract ohms from volts — the internal resistance has to be multiplied by the current first.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night with two lit pylons, an electronic scoreboard, a fourth official holding a glowing LED substitution board, and a pitch-side distribution box with cables running to the lights](scenes/football/current_electricity.svg "The substitution board is the only thing on this ground running off a pack small enough to carry.")

Ninety seconds before the first substitution of the school final, the fourth official's LED board goes dim. The orange number is barely readable from the halfway line, and the digits flicker each time the display refreshes.

Farhan, who looks after the club's equipment, has two spare packs in his bag. He pulls out the multimeter and tests the one that is fitted: **9.0 V**, exactly what is printed on the label. Nothing wrong with it, by that reading.

He tests the spare. Also 9.0 V.

He swaps them anyway, because there is nothing else to try. The board comes up bright and steady, and stays that way for the rest of the match.

Two packs, the same number on the meter, and only one of them can run the board. So the meter is clearly not measuring the thing that matters. What is it missing?

## The physics

A real cell is not a pure source of voltage. Inside it, the charge has to move through the electrolyte and the electrode materials, and that path has resistance of its own. We model this by drawing the cell as an **ideal source of emf** $\varepsilon$ in **series with an internal resistance** $r$.

The **emf** $\varepsilon$ is the energy the cell gives to each coulomb of charge it drives round the circuit, in joules per coulomb — that is, in volts. It is a property of the cell's chemistry, not of the circuit.

The **terminal potential difference** $V$ is what is actually available at the two terminals, which is what a voltmeter across them reads.

![A real cell modelled as an ideal source of emf in series with an internal resistance, connected to an external resistor, with a voltmeter reading the terminal potential difference](figures/emf_internal_resistance/cell-with-internal-resistance.svg "The voltmeter can only reach the terminals — so it never sees the volts already lost on the way out.")

When the cell drives a current $I$ through an external resistance $R$, the emf has to cover the drop inside as well as the drop outside:

$$\varepsilon = I(R + r) \qquad \Rightarrow \qquad I = \frac{\varepsilon}{R + r}$$

and the terminal pd is what survives:

$$V = \varepsilon - Ir$$

Look hard at that last equation, because it explains Farhan's whole afternoon. If $I = 0$ — nothing connected, just a meter across the terminals — then $V = \varepsilon$ and both packs read $9.0\,\text{V}$. A voltmeter draws almost no current, so it measures the emf and tells you nothing at all about $r$. Only when the cell is made to *work* does the internal resistance show itself.

![A graph of terminal potential difference against current: a straight line starting at the emf and sloping downwards](figures/emf_internal_resistance/terminal-pd-vs-current.svg "The intercept at zero current is the emf; the downward slope is the internal resistance. A tired cell's line slopes more steeply.")

Plot $V$ against $I$ and you get a straight line: intercept $\varepsilon$, slope $-r$. A fresh cell has a small $r$ and a nearly flat line. As a cell ages, $r$ climbs, the line tips over, and the terminals sag the moment anything demanding is plugged in. This holds while $\varepsilon$ and $r$ are treated as constant, which is a fair approximation over a short measurement.

## Worked example

**Given:** the tired pack reads $9.0\,\text{V}$ with nothing connected. Connected to the board, which behaves as a $4\,\Omega$ resistor, the voltmeter across its terminals reads only $6.0\,\text{V}$.
**Find:** the internal resistance of the pack.

**Step 1 — the volts that went missing.** The open-circuit reading is the emf, so

$$\varepsilon - V = 9.0 - 6.0 = 3.0\,\text{V}$$

Three volts out of nine are being dropped *inside* the pack, before they ever reach the terminals. Only two-thirds of the pack's push is getting out to the board.

**Step 2 — the current.** The $6.0\,\text{V}$ that does reach the terminals is across the board's $4\,\Omega$:

$$I = \frac{V}{R} = \frac{6.0}{4} = 1.5\,\text{A}$$

**Step 3 — the internal resistance.** Those missing volts are $Ir$:

$$r = \frac{\varepsilon - V}{I} = \frac{3.0}{1.5} = 2.0\,\Omega$$

**Sanity check:** $2\,\Omega$ inside a pack whose load is only $4\,\Omega$ is enormous — the pack is fighting itself nearly as hard as it drives the board, which is exactly what a worn-out cell does.

## Where the picture breaks

The ground is the setting, not an analogy — nothing in football behaves like an emf. The model itself is the thing to be careful with. The internal resistance is not a real resistor sitting in a box; it is a way of summarising chemistry that is genuinely more complicated, and $r$ changes with temperature, with how far the cell has discharged, and even with how fast you draw current. Treating $\varepsilon$ and $r$ as constants is a good approximation for a steady measurement and a poor one over a whole match. And a voltmeter is not perfect either: it draws a tiny current, so even the "open-circuit" reading is a hair below the true emf.

## Key takeaway

A real cell is an emf $\varepsilon$ in series with an internal resistance $r$. The current it drives is $I = \varepsilon/(R + r)$, and its terminal pd is $V = \varepsilon - Ir$ — equal to the emf only when no current flows. That is why two packs can read the same on a voltmeter and behave completely differently under load: the meter sees $\varepsilon$, while the load feels $r$.
