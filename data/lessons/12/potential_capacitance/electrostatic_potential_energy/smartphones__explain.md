---
concept_id: electrostatic_potential_energy
interest: smartphones
format: explain
title: Why the digits on a fitness band line up to appear
check:
  question: |-
    A dipole of moment $p = 3.0\times10^{-9}\,\text{C m}$ sits in a uniform field $E = 5.0\times10^{4}\,\text{V/m}$, lined up with the field. How much work must an external agent do to turn it slowly until it points exactly opposite to the field?
  options:
    A: |-
      $1.5\times10^{-4}\,\text{J}$
    B: |-
      $3.0\times10^{-4}\,\text{J}$
    C: |-
      Zero, because the dipole ends up on the same line it started on.
    D: |-
      $-3.0\times10^{-4}\,\text{J}$
  answer: B
  explanation: |-
    $U = -pE\cos\theta$ goes from $-pE$ (aligned) to $+pE$ (reversed), so the work is $2pE = 2 \times 3.0\times10^{-9} \times 5.0\times10^{4} = 3.0\times10^{-4}\,\text{J}$.
  misconceptions:
    A: |-
      Takes the work as just $pE$, measuring from zero instead of from the aligned energy $-pE$. The energy climbs from $-pE$ all the way to $+pE$, a rise of $2pE$.
    C: |-
      Thinks work depends on where the dipole ends up in space rather than on its orientation. The energy depends on the angle to the field, and turning it round changes that angle by $180^\circ$.
    D: |-
      Gets the sign wrong. Turning a dipole away from the field is done against the field's torque, so the external agent does positive work and the energy rises.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A desk by a rainy window: a phone with raindrops on its screen being tapped by a finger, a metal biscuit tin with its lid off, a breadboard with two supercapacitor cells wired in a chain, a stylus and a fitness band with a small display](scenes/smartphones/potential_capacitance.svg "The fitness band's grey digits appear only where a small voltage is switched on across the display.")

Riya's budget fitness band has a plain grey display, and one night her cousin Arnav, who wants to study electronics, shows her a trick. He holds the band under the desk lamp and tilts it: the digits show up dark, but only in the thin segments where the band has switched on a small voltage.

"There's a layer of liquid in there," he says. "Long thin molecules. Switch on a voltage across a segment and they swing round to line up with the field. That's what changes how the light gets through."

"Why line up *with* the field?" Riya asks. "Why not across it, or against it? A molecule doesn't know which way is which."

Arnav opens his mouth, then shuts it. He knows the molecules turn. He has never asked why that particular direction is the one they settle into — or what it has to do with energy.

## The physics

**A system of point charges.** The potential energy of a group of charges is the work needed to assemble them, bringing each in from infinity one at a time. For two charges a distance $r$ apart:

$$U = \frac{1}{4\pi\varepsilon_0}\,\frac{q_1 q_2}{r}$$

For more charges, add one such term **for every pair**, with signs. Like charges give a positive term (you had to push them together); unlike charges give a negative one (they pulled together on their own).

![Three charges of +2, +2 and −2 microcoulombs on a triangle with sides of 10 cm; the pair energies are +0.36 J, −0.36 J and −0.36 J, and the total is −0.36 J](figures/electrostatic_potential_energy/three-charges.svg "One term per pair, with signs. The like pair adds energy; the two unlike pairs take it away.")

**A dipole in a uniform external field.** A dipole of moment $\vec{p}$ at angle $\theta$ to a uniform field $\vec{E}$ has potential energy

$$U = -pE\cos\theta = -\vec{p}\cdot\vec{E}$$

- **Aligned** ($\theta = 0$): $U = -pE$, the lowest possible — stable.
- **Across** ($\theta = 90^\circ$): $U = 0$.
- **Reversed** ($\theta = 180^\circ$): $U = +pE$, the highest — unstable.

Anything free to turn settles where its energy is lowest, and the field's torque, $\tau = pE\sin\theta$, turns it that way. Turning it from $\theta_1$ to $\theta_2$ takes external work $pE(\cos\theta_1 - \cos\theta_2)$.

![A dipole in a field pointing right: aligned, U = −pE and stable; at 90 degrees, U = 0; reversed, U = +pE and unstable](figures/electrostatic_potential_energy/dipole-orientation-energy.svg "Aligned with the field is the lowest energy, so the dipole settles there. Reversed is the highest, and the slightest nudge tips it over.")

That is Riya's answer: lined up with the field is the lowest-energy way to point, so that is where the molecules end up.

## Worked example

Use $\dfrac{1}{4\pi\varepsilon_0} = 9.0\times10^9\,\text{N m}^2\text{C}^{-2}$ and illustrative values.

**(a)** Charges $+1.0\,\mu\text{C}$, $+1.0\,\mu\text{C}$ and $-1.0\,\mu\text{C}$ sit at the corners of a triangle with every side $10\,\text{cm}$.

**Step 1 — one pair.** Every pair has the same size of energy:

$$\frac{9.0\times10^9 \times (1.0\times10^{-6})^2}{0.10} = 0.09\,\text{J}$$

**Step 2 — all three pairs.** One like pair ($+0.09\,\text{J}$), two unlike pairs ($-0.09\,\text{J}$ each):

$$U = 0.09 - 0.09 - 0.09 = -0.09\,\text{J}$$

Negative: the group holds together, and you would have to supply $0.09\,\text{J}$ to pull it apart.

**(b)** A dipole with $p = 2.0\times10^{-8}\,\text{C m}$ sits in a field of $1.0\times10^{4}\,\text{V/m}$.

**Step 3 — the two extremes.** $pE = 2.0\times10^{-4}\,\text{J}$, so aligned $U = -2.0\times10^{-4}\,\text{J}$ and reversed $U = +2.0\times10^{-4}\,\text{J}$.

**Step 4 — the cost of flipping it.** $2pE = 4.0\times10^{-4}\,\text{J}$, roughly the energy a one-gram paper clip gains falling $4\,\text{cm}$.

**Sanity check:** turning a dipole from aligned to reversed must cost energy, so the answer is positive and twice the size of either extreme.

## Where the picture breaks

The molecules in a display are not rigid little $\pm q$ dumbbells. Much of their response is **induced**: the field stretches their electron clouds (as the dielectrics lesson describes) and the lengthwise direction is simply easier to stretch. The rule "lowest energy is along the field" survives, but the energy is not exactly $-pE\cos\theta$. The molecules also spring back when the voltage is switched off because of how they are anchored to the display's inner surfaces — a force this chapter doesn't cover.

## Key takeaway

The potential energy of a group of charges is the sum over every pair of $\dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1q_2}{r}$, with signs. A dipole in a uniform field has $U = -pE\cos\theta$: lowest and stable when aligned, highest when reversed, so flipping it costs $2pE$.
