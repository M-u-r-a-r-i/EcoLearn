---
concept_id: cells_combination
interest: football
format: explain
title: End to end or side by side, and who wins the argument
check:
  question: |-
    Two identical cells, each of emf $1.5\,\text{V}$ and internal resistance $0.5\,\Omega$, are connected **in parallel**. The equivalent emf and internal resistance of the combination are:
  options:
    A: |-
      $3.0\,\text{V}$ and $1.0\,\Omega$
    B: |-
      $3.0\,\text{V}$ and $0.25\,\Omega$
    C: |-
      $1.5\,\text{V}$ and $0.25\,\Omega$
    D: |-
      $1.5\,\text{V}$ and $1.0\,\Omega$
  answer: C
  explanation: |-
    Identical cells in parallel keep the emf of a single cell, $1.5\,\text{V}$, while their internal resistances combine like resistors in parallel: $r_\text{eq} = 0.5/2 = 0.25\,\Omega$.
  misconceptions:
    A: |-
      Gives the **series** result. Cells end-to-end add their emfs and their internal resistances; side-by-side cells do neither.
    B: |-
      Assumes parallel gives the best of both — double the emf *and* half the internal resistance. Each connection buys one thing only; you never get the voltage for free.
    D: |-
      Gets the emf right but adds the internal resistances. In parallel they are two routes for the current, so they combine as a parallel pair and the total comes out smaller, not larger.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A floodlit football ground at night with two lit pylons, an electronic scoreboard, a fourth official holding a glowing LED substitution board, and a pitch-side distribution box with cables running to the lights](scenes/football/current_electricity.svg "The stadium has pylons; a terrace kickabout has whatever cells are left in the drawer.")

The ground closes at eight, so Ishita and Deep play their five-a-side on the terrace of Deep's building, with two jumpers for goalposts and one battered lamp for light. The lamp is homemade: a bulb, a switch, and a holder that takes two cells.

Tonight it takes them a while, because the cells in the drawer are old and the bulb is barely orange.

Deep clips them end to end, positive to negative. "Twice the voltage," he says. "Twice the push."

Ishita takes the holder off him and wires them side by side instead, both positive terminals together. "These cells are half dead," she says. "Stacking them just stacks up whatever is wrong inside them too."

The bulb glows in both arrangements. Neither of them can honestly say which is brighter by eye. And Deep's claim has a hole in it that he has not noticed: even if the voltage really doubles, does the current?

## The physics

Every real cell is an emf $\varepsilon$ in series with an internal resistance $r$. When you combine cells, you are combining both.

**In series**, cells are joined positive-to-negative in a chain, so the same current passes through every one and their pushes add. For $n$ identical cells,

$$\varepsilon_\text{eq} = n\varepsilon, \qquad r_\text{eq} = nr$$

You gain voltage, but you also stack up the internal resistance, which is the part Deep has not accounted for.

**In parallel**, all the positive terminals are joined together and all the negatives together. Each cell provides its own route for the current, so the emf stays that of a single cell while the internal resistances combine like resistors in parallel. For $n$ identical cells,

$$\varepsilon_\text{eq} = \varepsilon, \qquad r_\text{eq} = \frac{r}{n}$$

![Two identical cells in series, giving twice the emf and twice the internal resistance, and the same two in parallel, giving the same emf and half the internal resistance](figures/cells_combination/cells-series-and-parallel.svg "Series buys voltage at the price of internal resistance; parallel buys low internal resistance and no extra voltage.")

Only connect cells in parallel if their emfs are equal — otherwise the stronger one drives current backwards through the weaker one, wasting energy and heating it. For two cells that are *not* identical, the general results are

$$\varepsilon_\text{eq} = \frac{\varepsilon_1 r_2 + \varepsilon_2 r_1}{r_1 + r_2}, \qquad r_\text{eq} = \frac{r_1 r_2}{r_1 + r_2}$$

Either way, the current the combination drives through an external resistance $R$ is found the same way as for a single cell:

$$I = \frac{\varepsilon_\text{eq}}{R + r_\text{eq}}$$

and that formula is where the argument gets settled — because which arrangement wins depends on how $R$ compares with $r$.

## Worked example

**Given:** two tired cells, each of emf $1.5\,\text{V}$ and internal resistance $1.0\,\Omega$ (illustrative, but the right size for a cell near the end of its life), lighting a bulb of resistance $2.0\,\Omega$.
**Find:** the current in each arrangement.

**Step 1 — series.** The emfs add and so do the internal resistances: $\varepsilon_\text{eq} = 3.0\,\text{V}$ and $r_\text{eq} = 2.0\,\Omega$. So

$$I_\text{series} = \frac{3.0}{2.0 + 2.0} = 0.75\,\text{A}$$

Deep doubled the voltage, but he also doubled the resistance inside — so the current is nowhere near double.

**Step 2 — parallel.** The emf stays $1.5\,\text{V}$ and the internal resistance halves to $0.5\,\Omega$:

$$I_\text{parallel} = \frac{1.5}{2.0 + 0.5} = 0.6\,\text{A}$$

So Deep wins this one, but only just: $0.75\,\text{A}$ against $0.6\,\text{A}$, not the two-to-one he promised.

**Sanity check:** swap the bulb for a low-resistance one, say $0.5\,\Omega$, and the answer flips — series gives $1.2\,\text{A}$ while parallel gives $1.5\,\text{A}$. Series wins when the external resistance is large compared with $r$; parallel wins when it is small.

## Where the picture breaks

Football is only the setting — a cell is not like a player and a battery is not like a team, and pushing that comparison would teach you nothing true. Inside the physics, the honest limits are these. Treating $\varepsilon$ and $r$ as fixed numbers is an approximation: both drift as a cell discharges and as it warms. "Two identical cells" is also an idealisation — two cells out of the same drawer never match exactly, and in parallel that mismatch means a small current circulates between them even with the lamp switched off. And nothing here says anything about how *long* the lamp will run; that depends on the charge stored, which is a separate question from the current it can push right now.

## Key takeaway

Cells in series give $\varepsilon_\text{eq} = n\varepsilon$ and $r_\text{eq} = nr$; cells in parallel give $\varepsilon_\text{eq} = \varepsilon$ and $r_\text{eq} = r/n$. Either way the current is $I = \varepsilon_\text{eq}/(R + r_\text{eq})$. Series is better for a large external resistance, parallel for a small one — doubling the voltage never simply doubles the current, because the internal resistance comes along with it.
