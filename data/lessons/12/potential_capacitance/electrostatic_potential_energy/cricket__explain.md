---
concept_id: electrostatic_potential_energy
interest: cricket
format: explain
title: Whose energy is it when the ball is at the top of a toss
check:
  question: |-
    Charges of $+3.0\,\mu\text{C}$ and $-3.0\,\mu\text{C}$ are held $0.30\,\text{m}$ apart. How much work must you do to pull them slowly until they are infinitely far apart? (Take $k = 9.0 \times 10^9\,\text{N m}^2/\text{C}^2$.)
  options:
    A: |-
      $+0.27\,\text{J}$
    B: |-
      $-0.27\,\text{J}$
    C: |-
      $+0.90\,\text{J}$
    D: |-
      $0\,\text{J}$, because the pair's total charge is zero
  answer: A
  explanation: |-
    The pair's energy is $U = kq_1q_2/r = 9.0 \times 10^9 \times (-9.0 \times 10^{-12})/0.30 = -0.27\,\text{J}$. At infinity $U = 0$, so you must supply $+0.27\,\text{J}$.
  misconceptions:
    B: |-
      Gives the system's potential energy instead of the work needed. The energy is $-0.27\,\text{J}$, so raising it to zero takes $+0.27\,\text{J}$ of work.
    C: |-
      Divides by $r^2$ as in Coulomb's force law. Potential energy goes as $1/r$, not $1/r^2$.
    D: |-
      Thinks a pair with zero net charge has no electrostatic energy. The energy depends on each pair of charges and the distance between them, not on the total charge.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A cricket ground under a storm cloud with lightning in the distance, a floodlight tower, a curator on the pitch, a car by the boundary and a photographer's flash](scenes/cricket/potential_capacitance.svg "Waiting out a rain delay: plenty of time to argue about physics.")

Rain delay again. Under the dressing-room awning, Tanvi, the team's wicketkeeper, tosses a ball straight up and catches it, over and over. Sameer sits beside her with his physics notes open.

"At the top," he says, watching the ball hang for an instant, "the ball has potential energy."

"The ball has it?" Tanvi catches it and holds it up. "Suppose the Earth vanished. Would this ball still have energy for being 'high'? High above what?"

Sameer frowns. The energy exists only because the Earth pulls the ball and the ball pulls the Earth. It seems to belong to the two of them together.

He turns the page. The next heading reads *Potential energy of a system of charges*. Two charges, three charges, a dipole sitting in a field. If energy belongs to pairs, how do you add it up for three charges, or thirty? And what does a *negative* energy even mean?

## The physics

**Two charges.** Start with $q_1$ fixed. Bring $q_2$ slowly from infinity to a distance $r$. The work you do against the field is stored as the **electrostatic potential energy** of the pair:

$$U = \frac{1}{4\pi\varepsilon_0}\,\frac{q_1 q_2}{r} = \frac{k q_1 q_2}{r}$$

Tanvi was right. $U$ belongs to the **system**, not to either charge alone. The zero is when the charges are infinitely far apart.

- **Like charges** ($q_1q_2 > 0$): $U > 0$. You had to push them together, and they will fly apart if released.
- **Unlike charges** ($q_1q_2 < 0$): $U < 0$. They pull together, so you must supply $|U|$ to separate them. A negative energy means a **bound** pair.

**Three or more charges.** Assemble them one at a time and add the work at each step. The result is one term for every pair, each counted once:

$$U = k\left(\frac{q_1q_2}{r_{12}} + \frac{q_1q_3}{r_{13}} + \frac{q_2q_3}{r_{23}}\right)$$

$N$ charges give $N(N-1)/2$ pairs. Order doesn't matter, because the electrostatic force is conservative.

![Three charges of +2, +2 and −2 microcoulombs on a triangle with sides of 10 cm; the pair energies are +0.36 J, −0.36 J and −0.36 J, and the total is −0.36 J](figures/electrostatic_potential_energy/three-charges.svg "One term per pair, with signs. The like pair adds energy; the two unlike pairs take it away.")

**A charge in an external field.** If the field comes from charges you are not counting, the energy of a charge $q$ at a point of potential $V$ is $U = qV$.

**A dipole in a uniform external field.** Turning a dipole against the torque takes work. With $\theta$ the angle between $\vec{p}$ and $\vec{E}$, and zero energy chosen at $\theta = 90^\circ$:

$$U(\theta) = -pE\cos\theta = -\vec{p}\cdot\vec{E}$$

The work needed to turn it from $\theta_1$ to $\theta_2$ is $pE(\cos\theta_1 - \cos\theta_2)$.

![A dipole in a field pointing right: aligned, U = −pE and stable; at 90 degrees, U = 0; reversed, U = +pE and unstable](figures/electrostatic_potential_energy/dipole-orientation-energy.svg "Aligned with the field is the lowest energy, so the dipole settles there. Reversed is the highest, and the slightest nudge tips it over.")

## Worked example

**Given:** $q_1 = q_2 = +2.0\,\mu\text{C}$ and $q_3 = -2.0\,\mu\text{C}$ at the corners of an equilateral triangle of side $0.10\,\text{m}$ (illustrative values).
**Find:** the potential energy of the system.

Each pair has the same size of term:

$$\frac{k\,(2.0 \times 10^{-6})^2}{0.10} = \frac{9.0 \times 10^9 \times 4.0 \times 10^{-12}}{0.10} = 0.36\,\text{J}$$

Now add the signs: pair 1–2 is like ($+0.36\,\text{J}$), while pairs 1–3 and 2–3 are unlike ($-0.36\,\text{J}$ each).

$$U = 0.36 - 0.36 - 0.36 = -0.36\,\text{J}$$

So $0.36\,\text{J}$ of work is needed to pull all three charges infinitely far apart.

**Add a dipole:** a dipole with $p = 4.0 \times 10^{-9}\,\text{C m}$ sits aligned with a uniform field $E = 2.0 \times 10^4\,\text{N/C}$. To turn it round to $\theta = 180^\circ$ takes $pE(\cos 0^\circ - \cos 180^\circ) = 2pE = 2 \times 4.0 \times 10^{-9} \times 2.0 \times 10^4 = 1.6 \times 10^{-4}\,\text{J}$.

**Sanity check:** the units work out as $\text{N m}^2\,\text{C}^{-2} \times \text{C}^2 / \text{m} = \text{N m} = \text{J}$. Limiting case: as $r \to \infty$ every term goes to zero, which is the reference we chose.

## Where the picture breaks

The tossed ball makes the key point: potential energy belongs to a system of interacting bodies. But gravity and electricity differ. Gravity only attracts, so the gravitational energy of a pair (with zero at infinity) is always negative. Electric pair energies can be either sign. The familiar $mgh$ also uses a different zero, at the ground rather than at infinity. That is fine, because only *changes* in energy are ever measured. Finally, "where" the energy sits can't be pinned to either charge. In the next lessons you'll see it can be described as stored in the field itself.

## Key takeaway

The potential energy of two charges is $U = kq_1q_2/r$. It belongs to the pair, and its zero is at infinite separation. For several charges, add one signed term per pair. A dipole in a uniform field has $U = -pE\cos\theta$: lowest when aligned, highest when reversed.
