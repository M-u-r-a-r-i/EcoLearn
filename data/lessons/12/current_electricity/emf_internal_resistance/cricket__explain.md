---
concept_id: emf_internal_resistance
interest: cricket
format: explain
title: The battery that reads full but can't run the scoreboard
check:
  question: |-
    A cell of emf $12\,\text{V}$ and internal resistance $0.50\,\Omega$ is delivering a current of $4.0\,\text{A}$. The potential difference across its terminals is:
  options:
    A: |-
      $12\,\text{V}$
    B: |-
      $14\,\text{V}$
    C: |-
      $10\,\text{V}$
    D: |-
      $2.0\,\text{V}$
  answer: C
  explanation: |-
    $V = \varepsilon - Ir = 12 - (4.0)(0.50) = 12 - 2.0 = 10\,\text{V}$. Two volts are dropped across the cell's own internal resistance.
  misconceptions:
    A: |-
      Treats the emf as the terminal pd whatever the current. They are equal only when the cell delivers no current.
    B: |-
      Adds $Ir$ instead of subtracting it. The internal resistance takes energy from the charge on its way out; it cannot add any.
    D: |-
      Reports the lost volts, $Ir$, instead of what is left for the external circuit.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground at dusk with floodlights, an electronic scoreboard, glowing stumps and an umpire holding a light meter](scenes/cricket/current_electricity.svg "The scoreboard, the lamps and the stump lights all hang off the same battery pack.")

Sunday morning, and the electronic scoreboard won't start. Rupa fetches the school's multimeter, clips it across the battery pack and reads the display: **12.0 V**. Exactly what the label promises.

"Battery's fine," she tells Aniket. "Must be the board."

Aniket isn't convinced. He connects the board anyway, and they both watch the multimeter as he does it. The digits slide down — 11.4, 10.8, 10.3 — and settle around ten and a half. The scoreboard's segments glow a sickly dim orange and the clock resets itself.

Rupa disconnects the board. The meter climbs straight back to 12.0 V.

The battery hasn't changed in those few seconds. The same battery is somehow worth twelve volts when nothing is attached and ten and a half when something is. What is the meter really measuring?

## The physics

The **emf** (electromotive force) $\varepsilon$ of a cell is the energy it gives to each coulomb of charge driven round the circuit, measured in volts. Despite the name it is not a force. It is a property of the cell's chemistry, and it does not change when you connect a load.

But charge has to travel *through* the cell — through its electrolyte and electrodes — and that path has resistance too. This is the cell's **internal resistance** $r$. We model a real cell as an ideal source of emf $\varepsilon$ in series with a resistance $r$ that you cannot get at with a screwdriver.

![A real cell drawn as an ideal source of emf in series with an internal resistance, connected to an external resistor, with a voltmeter across the terminals](figures/emf_internal_resistance/cell-with-internal-resistance.svg "The voltmeter can only reach the terminals — so it never sees the volts already lost inside.")

With an external resistance $R$ connected, the same current flows through $R$ and $r$, so

$$I = \frac{\varepsilon}{R + r}$$

The **terminal potential difference** $V$ is what is left for the outside world:

$$V = \varepsilon - Ir$$

Read that carefully: $V$ is smaller than $\varepsilon$ whenever current flows, and the gap $Ir$ grows with the current. Only in the **open-circuit** case, $I = 0$, do the two coincide — which is exactly what Rupa's first reading was. A good voltmeter draws almost no current, so across a disconnected battery it reports the emf.

![A graph of terminal potential difference against current: a straight line starting at the emf and sloping downwards](figures/emf_internal_resistance/terminal-pd-vs-current.svg "The intercept is the emf and the downward slope is the internal resistance — a tired cell's line slopes more steeply.")

As a cell ages its internal resistance rises. Its emf can still read close to the label on an idle meter while it collapses under any real load — which is why "the battery shows 12 V" proves less than it seems.

## Worked example

**Given:** a battery of emf $\varepsilon = 12\,\text{V}$ and internal resistance $r = 0.5\,\Omega$, connected to a scoreboard behaving as $R = 5.5\,\Omega$.
**Find:** the current, and the terminal potential difference.

The two resistances are in series with the emf, so add them: the circuit's total resistance is $6\,\Omega$.

$$I = \frac{\varepsilon}{R + r} = \frac{12}{6} = 2\,\text{A}$$

Now find how many volts that current loses inside the cell:

$$Ir = 2 \times 0.5 = 1\,\text{V}$$

One volt is spent getting through the battery itself, so the scoreboard receives

$$V = \varepsilon - Ir = 12 - 1 = 11\,\text{V}$$

Just over nine-tenths of what the label promised — dimmer than it should be, but working. If the pack were old, with $r$ several ohms instead of half an ohm, most of the emf would be lost inside and the board would go dark.

**Sanity check:** the numbers must add up: $11\,\text{V}$ across the board plus $1\,\text{V}$ lost inside is the full $12\,\text{V}$ of emf.

## Where the picture breaks

Nothing about cricket is being used as an analogy here — the scoreboard is simply a circuit, and forcing a comparison with, say, a tiring bowler would smuggle in wrong physics (a bowler tires permanently; a cell's terminal pd recovers the instant you disconnect it). The model itself has limits too. Treating $r$ as a fixed resistance is an approximation: it depends on temperature, on how far the cell is discharged, and on how fast the current changes. A real voltmeter draws a tiny current, so even the "open-circuit" reading is a hair below $\varepsilon$. And the scoreboard is not a plain resistor, so its $5.5\,\Omega$ is an illustrative stand-in.

## Key takeaway

Emf is the energy per coulomb a cell supplies; terminal potential difference is what survives the trip through the cell's own internal resistance: $V = \varepsilon - Ir$, with $I = \varepsilon/(R + r)$. The two are equal only on open circuit, so a healthy-looking voltmeter reading on a disconnected battery tells you almost nothing about whether it can drive a load.
