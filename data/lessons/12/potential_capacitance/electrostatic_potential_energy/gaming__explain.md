---
concept_id: electrostatic_potential_energy
interest: gaming
format: explain
title: What it costs to put a charge where you want it
check:
  question: |-
    A dipole of moment $p = 5.0 \times 10^{-9}\,\text{C}\,\text{m}$ sits in a uniform external field $E = 2.0 \times 10^{4}\,\text{N/C}$, lined up with the field. How much work must an outside agent do to turn it right round, to $180°$?
  options:
    A: |-
      $1.0 \times 10^{-4}\,\text{J}$
    B: |-
      Zero, because the dipole ends up lying along the same line it started on.
    C: |-
      $-2.0 \times 10^{-4}\,\text{J}$
    D: |-
      $2.0 \times 10^{-4}\,\text{J}$
  answer: D
  explanation: |-
    $U = -pE\cos\theta$, so $U_\text{initial} = -pE$ and $U_\text{final} = +pE$. The work is $U_\text{final} - U_\text{initial} = 2pE = 2 \times 5.0 \times 10^{-9} \times 2.0 \times 10^{4} = 2.0 \times 10^{-4}\,\text{J}$.
  misconceptions:
    A: |-
      Takes the aligned position as zero energy and computes only $pE$. The aligned position is the *minimum*, $U = -pE$, so the climb to $+pE$ is twice as big.
    B: |-
      Assumes $\theta = 180°$ is equivalent to $\theta = 0°$ because the dipole lies on the same line. A dipole has a direction, from $-q$ to $+q$; reversed means the $+q$ end now faces the wrong way, which is the highest-energy orientation, not the lowest.
    C: |-
      Subtracts the wrong way round, $U_\text{initial} - U_\text{final}$. Work done *by the external agent* is the increase in potential energy, $U_\text{final} - U_\text{initial}$, and here the energy goes up.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A gaming desk with a monitor showing rings of equal potential around a charge, a phone with a fingertip on its screen, an old picture tube on the bench and an opened power supply with two big capacitors](scenes/gaming/potential_capacitance.svg "The rings on the monitor are a map of potential. This lesson is about what it costs to drag something across that map.")

Ritika is two months into building a puzzle game. The player drags glowing charged orbs onto a board to build a shield, and the game charges them an energy budget for every orb placed.

Her first version charged a flat price per orb. It was boring — position didn't matter. So she rewrote it: the price of an orb now depends on what is already on the board. Drop a positive orb next to another positive one and it costs a fortune. Drop it next to a negative one and the game *refunds* you.

Sameer, playtesting, finds the exploit in about four minutes. He places a positive and a negative orb touching, banks the huge refund, then spends it on the far side of the board.

"That's a bug," he says.

Ritika isn't so sure it is. The refund felt like the right call when she wrote it. Is there a real quantity that behaves this way — one that goes up when you force like charges together and genuinely goes down when you let unlike ones approach?

## The physics

**Two charges.** The **electrostatic potential energy** of a system is the work an external agent must do to assemble it, bringing the charges slowly from infinity to their places. For two point charges $q_1$ and $q_2$ a distance $r_{12}$ apart,

$$U = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r_{12}} = \frac{k\,q_1 q_2}{r_{12}}$$

with $U = 0$ taken when the charges are infinitely far apart. The signs are Ritika's refund made exact: two like charges give $U > 0$ (you paid to push them together), a like–unlike pair gives $U < 0$ (the system did the work for you, so you got energy back).

**More than two.** Add **one term per pair**, with signs. For three charges,

$$U = k\left(\frac{q_1q_2}{r_{12}} + \frac{q_1q_3}{r_{13}} + \frac{q_2q_3}{r_{23}}\right)$$

Because potential is a scalar, this is plain addition — no directions. Note that the assembly order doesn't change the total, which is what makes $U$ a property of the arrangement rather than of the route to it.

![Three charges of +2, +2 and −2 microcoulombs on a triangle with sides of 10 cm; the pair energies are +0.36 J, −0.36 J and −0.36 J, and the total is −0.36 J](figures/electrostatic_potential_energy/three-charges.svg "One term per pair, with signs. The like pair adds energy; the two unlike pairs take it away.")

**A dipole in an external field.** Now the field is supplied from outside and the dipole only turns in it. Its energy depends on the angle $\theta$ between the dipole moment $\vec{p}$ and the field $\vec{E}$:

$$U = -pE\cos\theta = -\vec{p}\cdot\vec{E}$$

with $U = 0$ chosen at $\theta = 90°$. Aligned ($\theta = 0$) gives the minimum $-pE$, which is why a free dipole settles there; reversed ($\theta = 180°$) gives the maximum $+pE$, a balance point that the slightest nudge destroys.

![A dipole in a field pointing right: aligned, U = −pE and stable; at 90 degrees, U = 0; reversed, U = +pE and unstable](figures/electrostatic_potential_energy/dipole-orientation-energy.svg "Aligned with the field is the lowest energy, so the dipole settles there. Reversed is the highest, and the slightest nudge tips it over.")

## Worked example

Two small charged beads, $q_1 = +2.0\,\mu\text{C}$ and $q_2 = +3.0\,\mu\text{C}$, are held $0.60\,\text{m}$ apart on an insulating rod.

**Find:** the energy stored in the pair, and the extra work needed to push them to half that separation.

**Step 1 — the energy at $0.60\,\text{m}$.**

$$U = \frac{k q_1 q_2}{r} = \frac{9.0 \times 10^{9} \times 2.0\times10^{-6} \times 3.0\times10^{-6}}{0.60} = \frac{0.054}{0.60} = 0.090\,\text{J}$$

Positive, as it must be for two positive charges: somebody had to push them together.

**Step 2 — the energy at $0.30\,\text{m}$.** Since $U \propto 1/r$, halving $r$ doubles $U$:

$$U' = 2 \times 0.090 = 0.18\,\text{J}$$

**Step 3 — the extra work.** $W = U' - U = 0.18 - 0.090 = 0.090\,\text{J}$.

So closing the last $30\,\text{cm}$ costs as much as the whole journey in from infinity did. About a tenth of a joule is roughly the work of lifting a $10\,\text{g}$ coin one metre — small, but easily felt in a spring.

**Sanity check:** pushing like charges closer should always cost energy, and the answer came out positive.

## Where the picture breaks

Ritika's refund is honest physics, but her board is not. In a real system nothing stays put unless something holds it: those beads are on a rod, and without it the pair would fly apart and turn all $0.090\,\text{J}$ into kinetic energy. Her orbs also have a size and a price cap, while $U = kq_1q_2/r$ blows up without limit as $r \to 0$ — point charges are an idealisation, and real charges have structure long before they touch. Finally, her budget is a single running total, whereas the two formulas here answer different questions: $kq_1q_2/r$ is the energy of charges that all belong to the system, while $-\vec{p}\cdot\vec{E}$ leaves out the energy of whatever makes the external field, because that part never changes as the dipole turns.

## Key takeaway

The potential energy of a set of charges is the work needed to assemble them from infinity: one term $kq_iq_j/r_{ij}$ per pair, added as signed numbers. Like pairs store positive energy, unlike pairs negative. A dipole in an external field has $U = -pE\cos\theta$ — lowest when aligned, highest when reversed.
