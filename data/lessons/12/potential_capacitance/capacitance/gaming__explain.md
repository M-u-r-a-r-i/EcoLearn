---
concept_id: capacitance
interest: gaming
format: explain
title: Counting the tiny reservoirs around a processor
check:
  question: |-
    A parallel-plate capacitor with air between its plates has a capacitance of $40\,\text{pF}$. The plate separation is halved and the plate area is doubled. What is the new capacitance?
  options:
    A: |-
      $40\,\text{pF}$ — the two changes cancel each other out.
    B: |-
      $160\,\text{pF}$
    C: |-
      $80\,\text{pF}$
    D: |-
      $10\,\text{pF}$
  answer: B
  explanation: |-
    $C = \varepsilon_0 A/d$. Doubling $A$ doubles $C$; halving $d$ doubles it again. Together that is a factor of four, so $C = 4 \times 40 = 160\,\text{pF}$.
  misconceptions:
    A: |-
      Thinks "doubling one and halving the other" must cancel. It would if $C$ depended on the *product* $Ad$, but $A$ is on top and $d$ is underneath, so the two changes push the same way and multiply.
    C: |-
      Applies only one of the two changes and forgets the other, doubling once instead of twice.
    D: |-
      Inverts the formula, treating $C$ as proportional to $d/A$. Bigger plates hold more charge for the same voltage and a smaller gap means a smaller voltage for the same charge — both raise $C$.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk with a monitor showing rings of equal potential around a charge, a phone with a fingertip on its screen, an old picture tube on the bench and an opened power supply with two big capacitors](scenes/gaming/potential_capacitance.svg "The two fat cylinders in that opened power supply are capacitors. So are dozens of specks too small to see on the board next to it.")

Priya has an old graphics card that died, and she is taking it apart on a newspaper because she has never seen the inside of one. Under the heatsink is the processor itself, and packed around it, in tight rows, are dozens of tiny black rectangles no bigger than a grain of rice.

Vivek counts them. "Fifty-one. Why fifty-one of anything?"

They look them up: capacitors. And more of them are on the underside of the board, directly beneath the chip.

That is the odd part. The card gets its power through a fat cable from the power supply, which already has two capacitors the size of thumbs. If the big ones are doing the job, why crowd fifty-one specks as close to the processor as physically possible — and what does a single one of them actually hold?

## The physics

Put charge $+Q$ on one conductor and $-Q$ on another nearby, and a potential difference $V$ appears between them. Double the charge and you double the potential difference; the **ratio** does not change. That ratio is the **capacitance**:

$$C = \frac{Q}{V}$$

It depends only on the geometry of the two conductors and what is between them — not on how much charge you happen to have put on. Its SI unit is the **farad**: $1\,\text{F} = 1\,\text{C/V}$. A farad is enormous, so practical values run in microfarads ($10^{-6}\,\text{F}$), nanofarads and picofarads ($10^{-12}\,\text{F}$).

**Deriving the parallel-plate result.** Take two flat plates of area $A$ a distance $d$ apart, with $d$ much smaller than the plates' width, and vacuum (or air) between them.

![A parallel-plate capacitor with plates of area A a distance d apart, carrying +Q and −Q, a uniform field between them and slight fringing at the edges](figures/capacitance/parallel-plate-capacitor.svg "Uniform field between the plates, almost none outside. The derivation ignores the slight fringing at the edges.")

1. The surface charge density is $\sigma = Q/A$. Gauss's law for the pair of sheets gives a uniform field between them,

$$E = \frac{\sigma}{\varepsilon_0} = \frac{Q}{\varepsilon_0 A}$$

2. The field is uniform, so the potential difference is $V = Ed = \dfrac{Qd}{\varepsilon_0 A}$.

3. Therefore

$$C = \frac{Q}{V} = \frac{\varepsilon_0 A}{d}$$

Read it off: **bigger plates** store more charge at the same voltage, and a **smaller gap** means less voltage for the same charge. Both raise $C$. The result assumes the field is uniform right to the edges, which is only approximately true — real plates have a little **fringing** field curving out at the rim, as the figure shows.

## Worked example

Take two square plates of area $A = 100\,\text{cm}^2 = 1.0\times10^{-2}\,\text{m}^2$, separated by an air gap of $d = 1.0\,\text{mm}$. Use $\varepsilon_0 = 8.85\times10^{-12}\,\text{C}^2\text{N}^{-1}\text{m}^{-2}$.

**Find:** the capacitance, and the charge it holds at the $5\,\text{V}$ a USB port supplies.

**Step 1 — the capacitance.**

$$C = \frac{\varepsilon_0 A}{d} = \frac{8.85\times10^{-12} \times 1.0\times10^{-2}}{1.0\times10^{-3}} = 8.85\times10^{-11}\,\text{F} \approx 89\,\text{pF}$$

Two plates the size of a postcard, and the answer is under a tenth of a nanofarad.

**Step 2 — the charge at $5\,\text{V}$.**

$$Q = CV = 8.85\times10^{-11} \times 5.0 = 4.4\times10^{-10}\,\text{C}$$

Less than a nanocoulomb. That is why a one-farad capacitor is not made this way: at a $1\,\text{mm}$ gap it would need plates of about $10^{8}\,\text{m}^2$, a square roughly $10\,\text{km}$ on a side.

**Sanity check:** the farad is defined as a coulomb per volt, and a coulomb is a huge amount of static charge — so picofarads for hand-sized plates is exactly the size of answer to expect.

## Where the picture breaks

The specks on Priya's card are not two flat plates in air. They are stacks of many thin metal layers interleaved with a ceramic that has a large dielectric constant, which is how a grain-of-rice package reaches microfarads instead of the picofarads the bare formula gives — the next lessons are about exactly that. Their placement is a different story again: they sit close to the chip because the wires in between have **inductance**, which resists a sudden change of current, and that is a Class 12 topic from a later chapter. And $C = \varepsilon_0 A/d$ is a limiting result for $d \ll \sqrt{A}$; pull the plates apart until the gap is comparable to their width and the fringing stops being a small correction.

## Key takeaway

Capacitance is the charge a pair of conductors holds per volt between them, $C = Q/V$, measured in farads. It is fixed by geometry, not by the charge. For parallel plates in vacuum, $C = \varepsilon_0 A/d$ — more area or a smaller gap means more capacitance — valid while the gap is small enough for the field between the plates to count as uniform.
