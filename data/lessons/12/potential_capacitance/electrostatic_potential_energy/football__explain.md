---
concept_id: electrostatic_potential_energy
interest: football
format: explain
title: The tactics board discs that refused to sit together
check:
  question: |-
    A charge of $+4.0\,\mu\text{C}$ and a charge of $-1.0\,\mu\text{C}$ are held $0.30\,\text{m}$ apart. How much work must you do to pull them slowly infinitely far apart? (Take $k = 9.0 \times 10^{9}\,\text{N m}^2/\text{C}^2$.)
  options:
    A: |-
      $0.40\,\text{J}$
    B: |-
      $-0.12\,\text{J}$
    C: |-
      $0.060\,\text{J}$
    D: |-
      $0.12\,\text{J}$
  answer: D
  explanation: |-
    The pair's energy is $U = kq_1q_2/r = 9.0 \times 10^{9} \times (-4.0 \times 10^{-12})/0.30 = -0.12\,\text{J}$. At infinite separation $U = 0$, so you must supply $+0.12\,\text{J}$.
  misconceptions:
    A: |-
      Divides by $r^2$, as in Coulomb's force law. Potential energy falls as $1/r$, not $1/r^2$.
    B: |-
      Gives the system's potential energy instead of the work needed. The energy is $-0.12\,\text{J}$, so raising it to zero costs $+0.12\,\text{J}$ of work.
    C: |-
      Halves the answer, borrowing the $\tfrac{1}{2}$ from the energy stored in a capacitor. There is no factor of a half in $U = kq_1q_2/r$ for a pair of point charges.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A training ground at dusk with a floodlight pylon, an electric fence and its energiser box along the far side, a coach holding a touchscreen tablet, a water bowser and an AED cabinet](scenes/football/potential_capacitance.svg "Before anyone steps onto the grass, the shape of the game is set out on a steel board with magnetic discs.")

Coach Zubin sets up the week's shape on his steel tactics board, eleven red discs against eleven blue. Ipsita, who is injured and bored on the bench, notices that two of his red discs have been dropped in the bag the wrong way up.

She slides one of them towards another. A hand's width apart, it stops dead and skews sideways. She pushes it in anyway, holds it, and lets go — and it shoots off the edge of the board.

Then she flips it over. Now the same two discs snap together from a centimetre away with a click.

"Where did that shove come from?" she asks. "I was holding it. So was the board. Which disc had the energy in it — the one I pushed, or the one it hit?"

Zubin shrugs and redraws his midfield. Ipsita opens her physics notes at *Potential energy of a system of charges* and finds something stranger still: for two charges that attract, the book writes the energy as a **negative** number.

Whose energy is it, and how can there be less than none of it?

## The physics

**Two charges.** Hold $q_1$ fixed and bring $q_2$ slowly in from infinity to a distance $r$. The work you do against the field is stored as the **electrostatic potential energy** of the pair:

$$U = \frac{1}{4\pi\varepsilon_0}\,\frac{q_1 q_2}{r} = \frac{k q_1 q_2}{r}$$

Ipsita's question has a clean answer: $U$ belongs to the **system**, not to either charge. Neither one has an energy of its own; the energy is in the arrangement. The zero is chosen at infinite separation.

- **Like charges** ($q_1q_2 > 0$) give $U > 0$. You had to push them together, and they fly apart when released — her flipped disc.
- **Unlike charges** ($q_1q_2 < 0$) give $U < 0$. A negative energy means a **bound** pair: you must supply $|U|$ to pull them apart. Less than none, relative to the far-apart state you called zero.

**Three or more charges.** Assemble them one at a time and add up the work. The result is one term per **pair**, each counted once:

$$U = k\left(\frac{q_1q_2}{r_{12}} + \frac{q_1q_3}{r_{13}} + \frac{q_2q_3}{r_{23}}\right)$$

$N$ charges give $N(N-1)/2$ pairs. The order you build them in makes no difference, because the electrostatic force is conservative.

![Three charges of +2, +2 and −2 microcoulombs at the corners of a triangle of side 10 cm, with pair energies of +0.36 J, −0.36 J and −0.36 J adding to −0.36 J](figures/electrostatic_potential_energy/three-charges.svg "A worked case: one term per pair, with signs. The like pair stores energy; the two unlike pairs take more of it away.")

**A charge in an external field.** If the field is made by charges you are not counting, a charge $q$ at a point of potential $V$ has $U = qV$.

**A dipole in a uniform external field.** Turning a dipole against the torque takes work. With $\theta$ the angle between $\vec{p}$ and $\vec{E}$, and the zero taken at $\theta = 90^\circ$:

$$U(\theta) = -pE\cos\theta = -\vec{p}\cdot\vec{E}$$

so turning it from $\theta_1$ to $\theta_2$ costs $pE(\cos\theta_1 - \cos\theta_2)$.

![A dipole in a field pointing right, shown aligned with U = −pE and stable, at 90 degrees with U = 0, and reversed with U = +pE and unstable](figures/electrostatic_potential_energy/dipole-orientation-energy.svg "Aligned with the field is the lowest energy, so a free dipole settles there. Reversed is the highest, and the smallest nudge tips it over.")

## Worked example

Put three charges in a straight line on the board's edge: $+2.0\,\mu\text{C}$ at $A$, $+2.0\,\mu\text{C}$ at $B$ one metre along, and $-2.0\,\mu\text{C}$ at $C$ another metre beyond (illustrative values). **Find** the energy of the system.

Every pair here has charges of size $2.0\,\mu\text{C}$, so start with the common factor:

$$k q^2 = 9.0 \times 10^{9} \times (2.0 \times 10^{-6})^2 = 0.036\,\text{J m}$$

Now one term per pair, with its sign and its own separation:

- $A$–$B$, like charges, $1.0\,\text{m}$ apart: $+0.036\,\text{J}$
- $B$–$C$, unlike, $1.0\,\text{m}$ apart: $-0.036\,\text{J}$
- $A$–$C$, unlike, $2.0\,\text{m}$ apart: $-0.018\,\text{J}$

$$U = 0.036 - 0.036 - 0.018 = -0.018\,\text{J}$$

Negative, so the three are bound: scattering them to infinity takes $0.018\,\text{J}$ — roughly the energy of dropping a match ball half a centimetre.

**Sanity check:** the $A$–$C$ pair is twice as far apart as the others and its term is exactly half the size, as $1/r$ demands.

**And a dipole:** one with $p = 2.0 \times 10^{-9}\,\text{C m}$ sitting aligned in a uniform field $E = 1.0 \times 10^{5}\,\text{N/C}$ needs $pE(\cos 0^\circ - \cos 90^\circ) = pE = 2.0 \times 10^{-4}\,\text{J}$ to be turned side-on, and twice that to be turned right round.

## Where the picture breaks

The discs are a loose frame, not an analogy — say so plainly. A magnetic disc is a **dipole** with two poles, not a point charge, and there is no such thing as a single isolated magnetic pole to play the part of $q$. What the board does get right is the part Ipsita asked about: the energy sits in the arrangement of two objects, not inside either one. Two further cautions. Friction on the steel surface quietly eats energy, which a vacuum full of point charges does not. And $U = kq_1q_2/r$ is for point charges; near real, spread-out objects you must add up the contributions of all their parts.

## Key takeaway

Two point charges have potential energy $U = kq_1q_2/r$, belonging to the pair, with zero taken at infinite separation. Positive means you had to push them together; negative means they are bound and you must pay to separate them. For several charges, add one signed term per pair. A dipole in a uniform field has $U = -pE\cos\theta$, lowest when aligned and highest when reversed.
