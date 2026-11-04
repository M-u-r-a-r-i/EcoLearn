---
concept_id: emf_internal_resistance
interest: smartphones
format: explain
title: The phone that dies in the snow with a quarter of its battery left
check:
  question: |-
    A phone's lithium cell has emf $3.8\,\text{V}$ and internal resistance $0.2\,\Omega$. While it is being **charged** with a current of $1.0\,\text{A}$ flowing into it, the potential difference across its terminals is:
  options:
    A: |-
      $3.6\,\text{V}$
    B: |-
      $3.8\,\text{V}$
    C: |-
      $4.0\,\text{V}$
    D: |-
      $0.2\,\text{V}$
  answer: C
  explanation: |-
    When charging, the charger must push current backwards through the cell, against its emf *and* through its internal resistance, so $V = \varepsilon + Ir = 3.8 + 1.0 \times 0.2 = 4.0\,\text{V}$.
  misconceptions:
    A: |-
      Uses $V = \varepsilon - Ir$, which is for a cell *delivering* current. When current is driven into the cell, the drop across $r$ adds to the emf instead.
    B: |-
      Assumes the terminal pd always equals the emf. That is true only when no current flows; any current, either way, shifts the terminal pd by $Ir$.
    D: |-
      Calculates only the drop across the internal resistance, $Ir$, and stops. The terminal pd is the emf plus or minus that drop, not the drop alone.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A charging corner: a phone on a wall charger, a power bank charging an earbuds case through a small USB meter, and a smartwatch on its charging puck, with current arrows on the cables](scenes/smartphones/current_electricity.svg "The percentage on the screen is a guess about charge; it says nothing about how hard the cell can push when something suddenly demands current.")

Neha has waited all morning for the clouds to lift over the pass above Manali. At last the peaks appear, snow blazing in the sun. She pulls off a glove, opens the camera, taps for a burst of photos with the flash — and the phone switches itself off. The battery was showing $25\%$.

It will not turn back on up there. An hour later, in the warm café at the bottom of the trail, it starts perfectly well, and reports $24\%$.

Her brother Dev is baffled. "It didn't lose any charge. Twenty-five, then twenty-four. So why did it die?"

The battery clearly still had its energy. Somehow, in the cold, and at the exact moment the camera asked for a burst of current, it could not deliver it. What changed — and what is a battery's voltage, if it depends on what you ask of it?

## The physics

A cell does two things at once, and the puzzle comes from noticing only the first.

The **electromotive force**, $\varepsilon$, is the energy the cell gives to each coulomb of charge driven round the circuit — joules per coulomb, so volts. Despite its name it is not a force. It equals the pd across the terminals when **no current flows**.

But the charge must also pass *through* the cell — its electrolyte and electrodes — and that path has resistance: the **internal resistance** $r$. It sits inside the cell, in series with the emf, and cannot be switched off.

![A cell drawn as an emf in series with a small internal resistance r, connected to an external resistance R](figures/emf_internal_resistance/cell-with-internal-resistance.svg "Every real cell is an ideal source plus a resistance you cannot get at — and the current has to cross both.")

With an external load $R$, the emf drives current through $R$ and $r$ in series:

$$I = \frac{\varepsilon}{R + r}$$

A part $Ir$ of the push is lost inside the cell, so the circuit outside receives only the **terminal potential difference**:

$$V = \varepsilon - Ir$$

- With $I = 0$, $V = \varepsilon$: an open-circuit reading gives the emf.
- The bigger the current, the further $V$ falls below $\varepsilon$ — a straight line of slope $-r$.
- While the cell is being **charged**, current is forced backwards through it, and the terminal pd rises *above* the emf: $V = \varepsilon + Ir$.

![A graph of terminal potential difference against current: a straight line starting at the emf and falling with slope minus r](figures/emf_internal_resistance/terminal-pd-vs-current.svg "The intercept at zero current is the emf; the steepness of the fall is the internal resistance.")

A lithium cell's internal resistance rises sharply in the cold, because the chemistry inside slows down. That is the missing piece in Neha's story.

## Worked example

**Given:** Neha's cell has emf $\varepsilon = 3.8\,\text{V}$, and the camera burst draws $I = 2.0\,\text{A}$. Its internal resistance is about $0.1\,\Omega$ when warm and $0.3\,\Omega$ in the snow (illustrative values).
**Find:** the terminal pd in each case.

Warm, the volts lost inside are $Ir = 2.0 \times 0.1 = 0.2\,\text{V}$, so

$$V = \varepsilon - Ir = 3.8 - 0.2 = 3.6\,\text{V}$$

The phone's electronics receive a comfortable $3.6\,\text{V}$.

Cold, the loss triples to $Ir = 2.0 \times 0.3 = 0.6\,\text{V}$, so

$$V = 3.8 - 0.6 = 3.2\,\text{V}$$

Same cell, same charge, same current — but the terminal pd has sagged by $0.4\,\text{V}$, low enough that a phone's protection circuit may decide the battery is empty and shut down to protect it.

**Sanity check:** each time, what is delivered plus what is lost inside adds back to the emf: $3.6 + 0.2$ and $3.2 + 0.6$ are both $3.8\,\text{V}$.

## Where the picture breaks

The numbers are illustrative, and the model is tidier than a real cell. A lithium cell's internal resistance is not one fixed number: it depends on temperature, on how full the cell is and on its age, and its emf itself drifts slightly as it discharges. The straight-line graph assumes $r$ is constant, which is an approximation over a modest range of current.

The camera's current is also not a steady $2.0\,\text{A}$: a flash burst is a series of sharp spikes, and it is the brief peaks that pull the terminal pd down to the cut-off.

And the percentage on screen is an estimate of remaining charge made by the phone's software. It was probably right. The failure was never about charge — it was about the voltage the cell could hold up under load.

## Key takeaway

A real cell is an emf $\varepsilon$ in series with an internal resistance $r$. It drives $I = \varepsilon/(R + r)$, and the outside circuit receives only $V = \varepsilon - Ir$ — or $\varepsilon + Ir$ while the cell is being charged. The emf is the no-current reading; the gap between it and the terminal pd grows with the current and with the internal resistance.
