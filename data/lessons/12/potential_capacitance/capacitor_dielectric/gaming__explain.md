---
concept_id: capacitor_dielectric
interest: gaming
format: explain
title: How a speck of ceramic beats a cylinder of air
check:
  question: |-
    A parallel-plate capacitor is charged by a battery and then **disconnected** from it. A dielectric slab with $K = 3$ is now pushed in until it fills the gap. What happens to the charge, the voltage and the stored energy?
  options:
    A: |-
      Charge unchanged; voltage falls to one third; stored energy falls to one third.
    B: |-
      Charge unchanged; voltage unchanged; stored energy triples.
    C: |-
      Charge triples; voltage unchanged; stored energy triples.
    D: |-
      Charge unchanged; voltage falls to one third; stored energy triples.
  answer: A
  explanation: |-
    Disconnected means $Q$ is fixed. Inserting the slab makes $C' = 3C$, so $V' = Q/C' = V/3$, and $U' = Q^2/2C' = U/3$ — the slab is pulled in, and the energy lost is the work it does on the way.
  misconceptions:
    B: |-
      Keeps the voltage fixed because "the battery set it to that value". Once the battery is disconnected nothing holds $V$ constant; it is the charge that is now trapped, and $V$ must fall as $C$ rises.
    C: |-
      Applies the battery-*connected* result to a disconnected capacitor. With a battery still attached $V$ is fixed and $Q$ rises to $3Q$; with it removed $Q$ is fixed instead. Deciding which one is held constant is the whole question.
    D: |-
      Gets $V' = V/3$ right but then uses $U = \tfrac{1}{2}CV^2$ with the *old* $V$, or simply assumes more capacitance must mean more energy. With $Q$ fixed, $U = Q^2/2C$ and a larger $C$ means less stored energy.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk with a monitor showing rings of equal potential around a charge, a phone with a fingertip on its screen, an old picture tube on the bench and an opened power supply with two big capacitors](scenes/gaming/potential_capacitance.svg "Two capacitors the size of thumbs in the power supply. On the board beside it, parts a thousand times smaller hold more.")

Ishaan has two dead boards on the table: a chunky old sound card from the 1990s and the controller board out of a modern headset. He is comparing them for a school project, and something on them doesn't add up.

The old board has a capacitor the size of a AA cell, printed **10 µF**. The new board has a speck of tan ceramic about as big as a full stop, printed **10 µF** as well.

Ananya, who does the soldering for their robotics club, checks the markings twice. Same value. A volume difference of maybe a thousand times.

Ishaan already knows $C = \varepsilon_0 A/d$: capacitance comes from plate area and gap. The speck cannot have a thousand times the plate area, and its gap cannot be a thousandth as wide without falling apart. So the formula, as written, can't be the whole story. What else is inside that speck?

## The physics

Fill the gap of a capacitor with a dielectric of constant $K$ instead of air. The bound charges on the slab's faces oppose the applied field, so for the same charge $Q$ on the plates the field between them drops from $E_0$ to $E_0/K$. The voltage $V = Ed$ drops by the same factor — and since $C = Q/V$, the capacitance **rises**:

$$C = K\,C_0 = \frac{K\varepsilon_0 A}{d}$$

That is Ishaan's missing factor. A ceramic with a large $K$ does what a thousand-fold increase in area would do, in the same space. (Real ceramic capacitors also stack many thin layers, which multiplies the area as well.)

**A slab that only partly fills the gap.** If a slab of thickness $t$ sits inside a gap $d$, the field is $E_0$ in the air and $E_0/K$ inside the slab, so the voltage adds up as

$$V = E_0(d - t) + \frac{E_0}{K}\,t$$

which gives

$$C = \frac{\varepsilon_0 A}{(d-t) + \dfrac{t}{K}}$$

In words: **a thickness $t$ of dielectric counts as only $t/K$ of air.**

![A capacitor with plates 4.0 mm apart and a 2.0 mm slab with K = 4 in the middle; the field is E-nought in the air gaps and E-nought over K in the slab](figures/capacitor_dielectric/slab-partial.svg "The slab weakens the field inside it, so it counts as only t/K of air. Here the effective gap drops from 4.0 mm to 2.5 mm.")

**Two very different situations.** Before saying what happens when the slab goes in, ask what is being held fixed.

- **Battery still connected** — $V$ is fixed. Then $C$ rises to $KC$, so $Q = CV$ rises to $KQ$: the battery pushes more charge in. The energy $U = \tfrac{1}{2}CV^2$ rises to $KU$.
- **Battery disconnected** — $Q$ is fixed. Then $V = Q/C$ falls to $V/K$, and $U = Q^2/2C$ falls to $U/K$.

In both cases the slab is **pulled in** by the fringing field at the edges. In the disconnected case the lost energy is the work the capacitor does on the slab as it is drawn in.

## Worked example

A parallel-plate capacitor with an air gap of $d = 4.0\,\text{mm}$ has capacitance $C_0 = 20\,\text{pF}$.

**Find:** the capacitance (a) with a slab of $K = 4$ filling the gap, and (b) with a $2.0\,\text{mm}$ slab of the same material halfway across, as in the figure.

**Step 1 — the slab fills the gap.**

$$C = K C_0 = 4 \times 20 = 80\,\text{pF}$$

Four times the value, from the same two plates in the same place.

**Step 2 — the effective gap for the $2.0\,\text{mm}$ slab.** The $2.0\,\text{mm}$ of air stays as it is, and the $2.0\,\text{mm}$ of dielectric counts as $t/K = 2.0/4 = 0.5\,\text{mm}$:

$$d_\text{eff} = 2.0 + 0.5 = 2.5\,\text{mm}$$

**Step 3 — the new capacitance.** Capacitance goes as $1/d$, so

$$C = C_0 \times \frac{4.0}{2.5} = 20 \times 1.6 = 32\,\text{pF}$$

**Sanity check:** $32\,\text{pF}$ lies between $20\,\text{pF}$ (no slab) and $80\,\text{pF}$ (a full slab), which is where a half-filled gap has to land.

## Where the picture breaks

The tan speck is not two plates with one slab between them: it is dozens of metal layers interleaved with ceramic, so its area advantage and its $K$ advantage multiply. Its $K$ is also not a constant — the high-$K$ ceramics change value with temperature and with the voltage across them, sometimes losing half their capacitance in use, which is why the marking is a nominal figure. The formulas here assume a **linear** dielectric filling the gap uniformly with its faces square-on to the plates; a slab set at an angle, or pushed in only part-way across the *area* rather than the gap, is a different calculation. And every dielectric has a breakdown field: raise the voltage far enough and the insulator conducts, which destroys the capacitor rather than storing more.

## Key takeaway

Filling a capacitor's gap with a dielectric multiplies its capacitance by $K$: $C = K\varepsilon_0 A/d$, because the polarised slab weakens the field and so lowers the voltage for the same charge. A partial slab of thickness $t$ counts as only $t/K$ of air. Whether $Q$ or $V$ stays fixed when the slab goes in depends entirely on whether the battery is still connected — decide that first.
