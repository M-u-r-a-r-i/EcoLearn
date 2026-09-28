---
concept_id: cells_combination
interest: smartphones
format: explain
title: Why a power bank joins its cells side by side
check:
  question: |-
    Inside a power bank, two identical lithium cells, each of emf $3.7\,\text{V}$ and internal resistance $0.1\,\Omega$, are connected in **parallel**. The emf and internal resistance of the combination are:
  options:
    A: |-
      $3.7\,\text{V}$ and $0.05\,\Omega$
    B: |-
      $7.4\,\text{V}$ and $0.2\,\Omega$
    C: |-
      $3.7\,\text{V}$ and $0.2\,\Omega$
    D: |-
      $7.4\,\text{V}$ and $0.05\,\Omega$
  answer: A
  explanation: |-
    Identical cells in parallel keep the emf of one cell, $3.7\,\text{V}$, while their internal resistances combine like parallel resistors: $\dfrac{0.1 \times 0.1}{0.1 + 0.1} = 0.05\,\Omega$.
  misconceptions:
    B: |-
      Uses the series rules. Emfs and internal resistances add only when the cells are joined end to end, one after the other.
    C: |-
      Keeps the emf correctly but adds the internal resistances. Side by side, the cells offer two paths for the current, so their internal resistances combine like parallel resistors and the total falls.
    D: |-
      Adds the emfs as if more cells always meant more voltage. In parallel, every cell sits across the same two terminals, so the combination can only push as hard as one of them.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A charging corner: a phone on a wall charger, a power bank charging an earbuds case through a small USB meter, and a smartwatch on its charging puck, with current arrows on the cables](scenes/smartphones/current_electricity.svg "A power bank's printed voltage stays the same whether it holds one cell or several; something else changes.")

At the repair shop where Siddharth helps his aunt on Saturdays, a customer has brought in a swollen, dead power bank for safe disposal. His aunt, wearing gloves, eases the case open on the fire-proof mat.

Inside are two identical cylindrical lithium cells, lying side by side, their positive ends joined by one metal strip and their negative ends by another.

Siddharth is puzzled. On the bench is a laptop battery pack from last week, and in *that* one the cells were joined in a chain, the positive end of one welded to the negative end of the next.

"Same kind of cell," he says. "Two different ways of joining them. Why doesn't the power bank chain them too? Wouldn't that give it more volts?"

His aunt says the power bank wants something else from its second cell. What does joining cells side by side give you that chaining them does not?

## The physics

Each cell is an emf $\varepsilon$ with an internal resistance $r$ in series.

![A single cell drawn as an emf in series with its internal resistance](figures/emf_internal_resistance/cell-with-internal-resistance.svg "Before combining cells, remember what one cell is: an emf with a resistance built in.")

**Cells in series** (the laptop pack): the positive terminal of one is joined to the negative of the next. Going through the chain, the emfs add, and so do the internal resistances, because the current has to cross every one:

$$\varepsilon_\text{eq} = \varepsilon_1 + \varepsilon_2, \qquad r_\text{eq} = r_1 + r_2$$

If one cell is connected the wrong way round, its emf subtracts: $\varepsilon_\text{eq} = \varepsilon_1 - \varepsilon_2$, while the internal resistances still add.

**Cells in parallel** (the power bank): all the positive terminals are joined together, and all the negatives. For two cells,

$$\varepsilon_\text{eq} = \frac{\varepsilon_1 r_2 + \varepsilon_2 r_1}{r_1 + r_2}, \qquad \frac{1}{r_\text{eq}} = \frac{1}{r_1} + \frac{1}{r_2}$$

For $n$ **identical** cells in parallel this simplifies neatly: the emf stays $\varepsilon$, and the internal resistance falls to $r/n$.

![Two cells joined in series, end to end, and two cells joined in parallel, side by side](figures/cells_combination/cells-series-and-parallel.svg "Series adds the push and the internal resistance together; parallel keeps the push and divides the internal resistance.")

So there is the answer: the power bank does not want more volts — its electronics convert whatever it has to the USB output anyway. It wants to deliver a large current without losing much inside the cells, and to last longer. Parallel cells share the current, so each carries only part of it.

## Worked example

**Given:** two identical cells, each $\varepsilon = 3.7\,\text{V}$ and $r = 0.1\,\Omega$, and a load that draws $2.0\,\text{A}$.
**Find:** the combination's emf and internal resistance in series and in parallel, and the voltage lost inside in the parallel case.

In series: $\varepsilon_\text{eq} = 3.7 + 3.7 = 7.4\,\text{V}$ and $r_\text{eq} = 0.1 + 0.1 = 0.2\,\Omega$ — twice the push, twice the internal resistance.

In parallel: $\varepsilon_\text{eq} = 3.7\,\text{V}$ and $r_\text{eq} = \dfrac{0.1}{2} = 0.05\,\Omega$ — the same push, half the internal resistance.

At $2.0\,\text{A}$, the parallel pair loses inside

$$Ir_\text{eq} = 2.0 \times 0.05 = 0.1\,\text{V}$$

A single cell delivering the same $2.0\,\text{A}$ would lose $2.0 \times 0.1 = 0.2\,\text{V}$ — twice as much.

**Sanity check:** in parallel each cell carries half the current, $1.0\,\text{A}$, and loses $1.0 \times 0.1 = 0.1\,\text{V}$ — the same answer found a second way.

## Where the picture breaks

The formulas assume ideal cells with fixed emfs and internal resistances. Real lithium cells are only joined in parallel when they are closely matched: if one had a noticeably higher emf, it would drive a current backwards through the other — the unequal-cells formula hides a circulating current you will meet with Kirchhoff's rules.

A real power bank also has protection and conversion circuits between the cells and the USB port, so its output voltage is not simply the cells' terminal pd.

And one safety point that is not an analogy at all: a swollen or damaged lithium cell can catch fire. Siddharth's aunt opens packs only for disposal, with protection, and nobody should try it at home.

## Key takeaway

In series, emfs and internal resistances both add: more push, more internal loss. In parallel, identical cells keep the emf of one cell and divide the internal resistance, $r/n$, so they deliver large currents with less loss — which is why power banks join their cells side by side.
