---
concept_id: cells_combination
interest: cricket
format: explain
title: Four cells, two ways to wire them, one bright bail light
check:
  question: |-
    Two identical cells, each of emf $1.5\,\text{V}$ and internal resistance $0.50\,\Omega$, are joined in parallel (positive to positive, negative to negative). The combination behaves as a single cell of:
  options:
    A: |-
      emf $1.5\,\text{V}$, internal resistance $0.25\,\Omega$
    B: |-
      emf $3.0\,\text{V}$, internal resistance $1.0\,\Omega$
    C: |-
      emf $3.0\,\text{V}$, internal resistance $0.25\,\Omega$
    D: |-
      emf $0.75\,\text{V}$, internal resistance $0.25\,\Omega$
  answer: A
  explanation: |-
    Identical cells in parallel keep the emf of one cell, while the two internal resistances are in parallel: $r_\text{eq} = r/2 = 0.25\,\Omega$.
  misconceptions:
    B: |-
      Applies the series rules. Emfs add only when the cells are one after another, so that the same charge passes through both.
    C: |-
      Adds the emfs but treats the internal resistances as parallel — mixing the two arrangements. One connection decides both answers.
    D: |-
      Assumes the emf is shared out, as if two cells each gave half. In parallel each cell drives the same two points to the same potential difference.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A cricket ground at dusk with floodlights, an electronic scoreboard, glowing stumps and an umpire holding a light meter](scenes/cricket/current_electricity.svg "Lit bails, a lit scoreboard — and a box of ordinary cells behind both.")

The under-15s want lit bails for their evening tournament, so Harsh and Neha build a set in the school workshop: an LED in each bail, a tiny switch, and a holder for four identical cells.

Harsh wires all four in a line, nose to tail, the way a torch does. The LEDs come up blindingly bright — and are noticeably dimmer by the end of the second innings.

Neha rebuilds the holder as two pairs side by side. Her set is not as bright, but it is still going at stumps, hours later.

They argue about it all the way home. Same four cells, same LEDs, same evening. Harsh says his wiring is "stronger". Neha says hers is "bigger". Neither can say what changed electrically — or, more usefully, which wiring they should use for the umpire's light meter, which needs only a whisper of current but must never fade.

## The physics

Every real cell has an emf $\varepsilon$ and an internal resistance $r$. Combining cells combines both.

**In series**, cells are joined nose to tail — the positive terminal of one to the negative of the next — so the same charge passes through every cell in turn, picking up energy from each. The emfs add, and so do the internal resistances:

$$\varepsilon_\text{series} = \varepsilon_1 + \varepsilon_2, \qquad r_\text{series} = r_1 + r_2$$

If a cell is put in backwards, its emf *subtracts* — the rest of the battery drives current backwards through it.

**In parallel**, like terminals are joined together, so each cell is connected across the same two points. For $n$ **identical** cells the combination has the emf of one cell, but the internal resistances are in parallel:

$$\varepsilon_\text{parallel} = \varepsilon, \qquad r_\text{parallel} = \frac{r}{n}$$

![Two identical cells in series, giving twice the emf and twice the internal resistance, and the same two in parallel, giving the same emf and half the internal resistance](figures/cells_combination/cells-series-and-parallel.svg "Series buys voltage at the cost of internal resistance; parallel buys low internal resistance at no gain in voltage.")

For two *unequal* cells in parallel, the combination is

$$\varepsilon_\text{eq} = \frac{\varepsilon_1 r_2 + \varepsilon_2 r_1}{r_1 + r_2}, \qquad r_\text{eq} = \frac{r_1 r_2}{r_1 + r_2}$$

Which is better depends on the load. Since $I = \varepsilon_\text{eq}/(R + r_\text{eq})$, series wins when the external resistance $R$ is **large** compared with $r$ (the extra internal resistance hardly matters, and you gain voltage), while parallel wins when $R$ is **small** compared with $r$ (the cells share the heavy current instead of each fighting its own internal resistance).

## Worked example

**Given:** two identical cells, each $\varepsilon = 1.5\,\text{V}$ with $r = 0.5\,\Omega$, driving a bail light that behaves as $R = 2\,\Omega$.
**Find:** the current in series, and in parallel.

**Series.** The emfs add to $3\,\text{V}$, and the internal resistances add to $1\,\Omega$. So the circuit has $2 + 1 = 3\,\Omega$ in all:

$$I = \frac{3}{3} = 1\,\text{A}$$

**Parallel.** The emf stays at $1.5\,\text{V}$, and the internal resistance halves to $0.25\,\Omega$. The circuit now has $2 + 0.25 = 2.25\,\Omega$:

$$I = \frac{1.5}{2.25} \approx 0.67\,\text{A}$$

Series gives about half as much current again — which is Harsh's bright bails. Each of his cells is carrying the full $1\,\text{A}$, so they empty fast. In Neha's pair, each cell supplies only half of $0.67\,\text{A}$, so the set runs far longer on the same chemistry.

**Sanity check:** the load here ($2\,\Omega$) is much bigger than $r$, so theory says series should win on current — and it does.

## Where the picture breaks

The bail lights are a real circuit; there is no cricketing analogy being stretched here, and inventing one (cells as batting partners "adding runs") would suggest that cells cooperate in ways they don't. The genuine simplifications: the formula $r_\text{parallel} = r/n$ needs the cells to be truly identical, and two shop-bought cells never are — connect a fresh cell in parallel with a tired one and the fresh one quietly drives current *into* the tired one. An LED is also not a resistor; treating the bail light as $2\,\Omega$ is a stand-in so the arithmetic stays visible. And nothing here predicts *how long* a set lasts, since that depends on the charge each cell stores.

## Key takeaway

Cells in series add their emfs and their internal resistances; identical cells in parallel keep one cell's emf and divide the internal resistance by $n$. Use $I = \varepsilon_\text{eq}/(R + r_\text{eq})$ to compare arrangements: series for a high-resistance load, parallel for a low-resistance one that draws heavy current.
