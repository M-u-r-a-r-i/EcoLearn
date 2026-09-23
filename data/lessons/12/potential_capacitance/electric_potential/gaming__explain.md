---
concept_id: electric_potential
interest: gaming
format: explain
title: Why a hundredth of a volt matters to a chip
check:
  question: |-
    An insulating layer inside a chip is $4.0\,\text{nm}$ thick, with a potential difference of $1.2\,\text{V}$ across it. Taking the field inside the layer as uniform, how big is it?
  options:
    A: |-
      $4.8 \times 10^{-9}\,\text{V/m}$
    B: |-
      $3.0 \times 10^{5}\,\text{V/m}$
    C: |-
      $3.0 \times 10^{8}\,\text{V/m}$
    D: |-
      Zero, because the layer is an insulator and no current flows through it.
  answer: C
  explanation: |-
    In a uniform field $E = \Delta V/d = 1.2\,\text{V} / (4.0 \times 10^{-9}\,\text{m}) = 3.0 \times 10^{8}\,\text{V/m}$.
  misconceptions:
    A: |-
      Multiplies the voltage by the thickness instead of dividing. $\Delta V = Ed$, so $E = \Delta V/d$ — the thickness goes on the bottom.
    B: |-
      Slips a unit prefix and treats $4.0\,\text{nm}$ as $4.0\,\mu\text{m}$. A nanometre is $10^{-9}\,\text{m}$, a thousand times smaller than a micrometre.
    D: |-
      Thinks a field or a potential difference exists only where a current flows. A field is there whenever charges are separated; an insulator is exactly where you expect a large one.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk with a monitor showing rings of equal potential around a charge, a phone with a fingertip on its screen, an old picture tube on the bench and an opened power supply with two big capacitors](scenes/gaming/potential_capacitance.svg "One word, volts, turns up on everything on this desk — the phone, the tube, the power supply. The rings on the monitor are the first hint of what it counts.")

Devika's first build has been running for a week, and tonight she is finally overclocking it. Her cousin Imran, who has done this before, points at a slider in the tuning tool labelled **core voltage, 1.10 V**.

"Nudge it," he says. "Small steps."

She drags it to 1.15 V. Five hundredths of a volt. Within seconds the temperature readout climbs several degrees and the fans get loud.

"That's it," Imran says. "Go much further and you'll cook it."

Devika stares at the number. Her controller's cell says 3.7 V. The USB port on the case says 5 V. The sticker on the power supply warns about hundreds. And a change of **0.05** — a number smaller than one — just made a chip noticeably hotter.

So what is a volt actually counting, that a hundredth of one is worth anything at all?

## The physics

Take a small positive **test charge** $q$ and move it slowly — no acceleration — through a region where other charges are sitting. The electric field pushes on it, so moving it takes work. The **electrostatic potential** $V$ at a point is the work an external force must do to bring a unit positive charge from infinity to that point:

$$V = \frac{W}{q}$$

Potential is a **scalar**, and its SI unit is the **volt**: $1\,\text{V} = 1\,\text{J/C}$. So a volt is not an amount of electricity. It is **energy per unit charge** — joules handed over per coulomb carried.

In practice what matters is the **potential difference** between two points. Carrying a charge $q$ slowly from $B$ to $A$ needs work

$$W_{BA} = q\,(V_A - V_B)$$

Because the electrostatic force is conservative, this work does not depend on the path taken — which is what lets a single number be attached to each point.

That answers Devika's question. At 1.10 V, every coulomb crossing the chip's core delivers 1.10 joules. At 1.15 V it delivers 1.15 joules — about 5% more energy, from the same charge. The energy has to go somewhere, and it goes into heat.

**Potential and field.** The field tells you how fast the potential changes with distance:

$$E = -\frac{dV}{dr}$$

The minus sign says the field points the way the potential *falls*. Where the field is uniform this becomes $E = \Delta V/d$, with $d$ measured along the field. That gives a second unit for the field: $1\,\text{V/m} = 1\,\text{N/C}$.

![A uniform field between plates at 300 V and 0 V, with lines at 200 V and 100 V one centimetre apart, and a positive charge being pushed from 100 V up to 200 V](figures/electric_potential/uniform-field-potential.svg "Potential falls steadily along the field. Pushing a positive charge against the field, from 100 V to 200 V, costs q × 100 V of work.")

In the figure the field runs from the $300\,\text{V}$ plate to the $0\,\text{V}$ plate. The marked lines are $1.0\,\text{cm}$ apart and $100\,\text{V}$ apart, so $E = 100\,\text{V} / 0.010\,\text{m} = 1.0 \times 10^4\,\text{V/m}$.

## Worked example

Inside a chip, the gate of a transistor is separated from the rest of it by an insulating layer only a few nanometres thick. Take the thickness as $d = 2.0\,\text{nm}$ (illustrative) and the potential difference across it as $V = 1.0\,\text{V}$, and treat the field in the layer as uniform.

**Find:** the field in the layer, and the work done on one electron crossing it.

**Step 1 — the field.**

$$E = \frac{V}{d} = \frac{1.0\,\text{V}}{2.0 \times 10^{-9}\,\text{m}} = 5.0 \times 10^{8}\,\text{V/m}$$

That is the same field you would get by putting half a million volts across a single millimetre. One volt is a small number only because the gap is fantastically small.

**Step 2 — the work on one electron.** An electron carries $e = 1.6 \times 10^{-19}\,\text{C}$, so

$$W = eV = 1.6 \times 10^{-19} \times 1.0 = 1.6 \times 10^{-19}\,\text{J}$$

**Sanity check:** dry air breaks down and sparks at about $3 \times 10^{6}\,\text{V/m}$, so the layer is holding off a field over a hundred times stronger than air could — which is exactly why it has to be a solid insulator, and why pushing the voltage higher is risky.

## Where the picture breaks

The chip is a real place where potential difference matters, but this chapter is **electrostatics** — charges at rest. A running chip has charges moving, fields changing billions of times a second, and heating that depends on current as well as voltage; that is the next chapter's story. The tidy result "5% more volts, 5% more energy per coulomb" is true for the energy each charge carries, but the heat a chip actually makes climbs faster than that, because a higher voltage also pushes more charge through per switch. The $2\,\text{nm}$ figure is illustrative, and a real transistor is nothing like two flat plates, so $E = V/d$ is an estimate of the order of magnitude, not a design calculation.

## Key takeaway

Potential is work per unit charge, $V = W/q$, measured in volts, where $1\,\text{V} = 1\,\text{J/C}$. Moving a charge $q$ between two points takes work $q(V_A - V_B)$, whatever path it follows. The field points the way potential falls, $E = -dV/dr$, which in a uniform field is just $E = \Delta V/d$ — so a tiny voltage across a tiny gap can still mean an enormous field.
