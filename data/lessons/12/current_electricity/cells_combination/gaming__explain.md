---
concept_id: cells_combination
interest: gaming
format: explain
title: Half the voltage, twice the buzz in a home-made rumble pack
check:
  question: |-
    Two identical cells, each of emf $1.5\,\text{V}$ and internal resistance $2.0\,\Omega$, are connected **in parallel**. The combination is equivalent to a single cell of:
  options:
    A: |-
      emf $3.0\,\text{V}$, internal resistance $1.0\,\Omega$
    B: |-
      emf $1.5\,\text{V}$, internal resistance $1.0\,\Omega$
    C: |-
      emf $1.5\,\text{V}$, internal resistance $4.0\,\Omega$
    D: |-
      emf $3.0\,\text{V}$, internal resistance $4.0\,\Omega$
  answer: B
  explanation: |-
    Identical cells in parallel are all connected across the same two points, so the emf stays $1.5\,\text{V}$; their internal resistances are in parallel too, giving $r/2 = 1.0\,\Omega$.
  misconceptions:
    A: |-
      Adds the emfs, which only happens in series. In parallel every cell shares the same pair of terminals, so the combination pushes with one cell's emf.
    C: |-
      Adds the internal resistances. They are side by side, not end to end, so they combine like parallel resistors and the total comes out *smaller* than one of them.
    D: |-
      Applies the series rules to a parallel arrangement throughout — right formulas, wrong circuit.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A night gaming desk with a monitor showing a frame counter, a controller with a lithium cell inside charging over USB, a USB power meter, and an open PC case](scenes/gaming/current_electricity.svg "A controller's rumble is a small motor drawing a surprisingly heavy current from a small cell.")

Rehan builds an arcade button box for his fighting game and decides it needs a rumble: a small vibration motor glued inside, run from two AA cells he finds in a drawer.

Wired the obvious way — the two cells nose to tail, the way every remote control in the house does it — the motor buzzes, but feebly. Divya, who lent him the soldering iron, suggests the other arrangement: both cells side by side, positives joined to positives, negatives to negatives.

Rehan tells her that is obviously worse. Side by side gives $1.5\,\text{V}$ instead of $3\,\text{V}$. Half the push must mean less of everything.

They try it anyway. The motor buzzes distinctly harder.

Divya points out that these are old cells, pulled out of a TV remote, and thinks that matters. Rehan cannot see why the *age* of a cell should decide which wiring wins.

## The physics

Every cell carries its internal resistance around with it, so a combination of cells is a combination of emfs **and** of resistances.

![A cell drawn as an emf in series with a small internal resistance r](figures/emf_internal_resistance/cell-with-internal-resistance.svg "Before combining cells, remember what one cell is: an emf with a resistance built in.")

**In series**, cells are joined nose to tail, so the same current passes through all of them and their pushes add:

$$\varepsilon_\text{eq} = \varepsilon_1 + \varepsilon_2 + \dots, \qquad r_\text{eq} = r_1 + r_2 + \dots$$

For $n$ identical cells, $\varepsilon_\text{eq} = n\varepsilon$ and $r_\text{eq} = nr$. (If one cell is put in backwards its emf *subtracts*, while its internal resistance still adds — a good way to ruin a torch.)

**In parallel**, identical cells are all connected across the same two points, so the emf is unchanged and the internal resistances combine like parallel resistors:

$$\varepsilon_\text{eq} = \varepsilon, \qquad r_\text{eq} = \frac{r}{n}$$

![Cells drawn connected in series and in parallel, with the equivalent emf and internal resistance marked for each](figures/cells_combination/cells-series-and-parallel.svg "Series multiplies the push and the internal resistance together; parallel keeps the push and divides the internal resistance.")

Now the question Rehan and Divya stumbled into. With $n$ identical cells driving an external resistance $R$:

$$I_\text{series} = \frac{n\varepsilon}{R + nr}, \qquad I_\text{parallel} = \frac{n\varepsilon}{nR + r}$$

Compare the two denominators and a clean rule falls out: **series wins when $R > r$; parallel wins when $R < r$.** Fresh cells have a small $r$, and most loads are far larger, which is why almost every device stacks its cells in series. Divya's tired cells have a large $r$, and a little motor is a low-resistance load — so this is the other case.

## Worked example

**Given:** two well-used cells, each $\varepsilon = 1.5\,\text{V}$ with $r = 2.0\,\Omega$, driving a vibration motor that behaves as $R = 1.0\,\Omega$ (illustrative values).
**Find:** the current in series, and in parallel.

**Series.** The emfs add to $3.0\,\text{V}$ and the internal resistances add to $4.0\,\Omega$. With the motor, the circuit totals $1.0 + 4.0 = 5.0\,\Omega$:

$$I = \frac{3.0}{5.0} = 0.6\,\text{A}$$

**Parallel.** The emf stays at $1.5\,\text{V}$ and the internal resistance halves to $1.0\,\Omega$. The circuit now totals $1.0 + 1.0 = 2.0\,\Omega$:

$$I = \frac{1.5}{2.0} = 0.75\,\text{A}$$

A quarter more current, from half the voltage — Rehan's surprise, and the reason is visible in the working: in series, four of the five ohms in the circuit were *inside the cells*, so most of the doubled emf was wasted before it ever reached the motor.

**Sanity check:** here $R = 1\,\Omega$ is smaller than $r = 2\,\Omega$, and the rule says parallel should win in that case — and it does.

## Where the picture breaks

Treating the motor as a fixed $1.0\,\Omega$ resistor is the usual motor idealisation: once it spins it generates a back-emf, so its current falls below what Ohm's law alone predicts, and the two arrangements will not differ by exactly the ratio above.

The parallel wiring carries a real warning that the formulas hide. The rule $r_\text{eq} = r/n$ assumes the cells are **identical**. Connect two cells of different emf, or different charge, in parallel and the stronger one immediately drives a current backwards through the weaker one — wasted energy at best, a hot, leaking cell at worst. Cells in series can differ safely; cells in parallel should not.

And $r$ itself is not a constant. It climbs as a cell empties and as it ages, so the "best" wiring for a given pack can change over the pack's life — which is more or less Divya's point about the drawer.

## Key takeaway

Cells in series add both emf and internal resistance: $\varepsilon_\text{eq} = n\varepsilon$, $r_\text{eq} = nr$. Identical cells in parallel keep one cell's emf and divide the internal resistance: $\varepsilon_\text{eq} = \varepsilon$, $r_\text{eq} = r/n$. Series delivers more current when the external resistance is the larger one, parallel when the internal resistance is — and only identical cells should ever be paralleled.
