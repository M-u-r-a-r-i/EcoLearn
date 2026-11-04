---
concept_id: satellite_energy
interest: smartphones
format: explain
title: The satellite that speeds up as air drag slows it
check:
  question: |-
    A weather satellite in a circular orbit has total mechanical energy $-3.0 \times 10^{9}\,\text{J}$, with potential energy taken as zero at infinity. What is its gravitational potential energy?
  options:
    A: |-
      $-3.0 \times 10^{9}\,\text{J}$
    B: |-
      $-6.0 \times 10^{9}\,\text{J}$
    C: |-
      $+3.0 \times 10^{9}\,\text{J}$
    D: |-
      $-1.5 \times 10^{9}\,\text{J}$
  answer: B
  explanation: |-
    In a circular orbit $E = -GMm/2r$ and $U = -GMm/r$, so $U = 2E = -6.0 \times 10^{9}\,\text{J}$. The kinetic energy is $K = -E = +3.0 \times 10^{9}\,\text{J}$, and $K + U = E$ checks.
  misconceptions:
    A: |-
      Treats the total energy as if it were all potential energy, forgetting the satellite's kinetic energy; $E = K + U$, and $K$ is positive.
    C: |-
      Gives the kinetic energy $K = -E$ instead of the potential energy; the potential energy is negative, twice the total.
    D: |-
      Halves the total instead of doubling it; since $K = -E$ is positive, $U$ must be more negative than $E$ for the two to add up to $E$.
author: claude-code/opus-5
written: 2026-09-28
---
## The story

![A city rooftop at night: a fixed satellite dish, moving navigation satellites, a weather balloon rising with a phone, and a phone and tablet on a table showing a sky plot and a weather image](scenes/smartphones/gravitation.svg "Each satellite over the rooftop is bound to the Earth. Its energy, counted properly, is negative.")

Ishita's phone buzzes with a notification from her space-news app: an old satellite in a low orbit is being slowly dragged down by the thin traces of air that still exist hundreds of kilometres up. It will burn up on re-entry within a few years.

She reads the next line aloud to Yash. "As the orbit shrinks, the satellite actually **speeds up**."

Yash laughs. "That's a typo. Drag *slows* things down. That's the whole point of drag. Put your hand out of a bus window and see."

"The article says it twice."

"Then the article's wrong twice."

Ishita isn't sure. Drag is definitely taking energy away from the satellite; that's why it's sinking. But how can taking energy away make something go **faster**?

## The physics

Take a satellite of mass $m$ in a circular orbit of radius $r$ around the Earth (mass $M$), with potential energy zero at infinity.

**Kinetic energy.** Gravity supplies the centripetal force: $GMm/r^2 = mv^2/r$, so $mv^2 = GMm/r$ and

$$K = \frac{1}{2}mv^2 = \frac{GMm}{2r}$$

**Potential energy.**

$$U = -\frac{GMm}{r}$$

**Total mechanical energy.**

$$E = K + U = -\frac{GMm}{2r}$$

So in every circular orbit, $K = -E$ and $U = 2E$.

**Why $E$ is negative.** At infinity $U = 0$ and $K$ can't be negative, so a body with $E < 0$ can never get there. It is **bound** to the Earth. The size of $E$ is the **binding energy**: the energy you'd have to supply to set the satellite completely free.

![A graph of energy against orbit radius: a blue kinetic energy curve above zero, a red potential energy curve below, and a green dashed total energy curve halfway between the red curve and zero](figures/satellite_energy/energy-vs-orbit-radius.svg "At every radius, K = −E and U = 2E. Moving to a smaller orbit lowers E and U but raises K.")

**Ishita's puzzle.** Drag removes energy, so $E$ becomes **more negative**, and $E = -GMm/2r$ says $r$ must shrink. But at a smaller $r$, $K = -E$ is **bigger**. The satellite falls inward, and gravity's pull along that fall does work on it. Potential energy drops by twice as much as the total, so half of that drop is lost to drag as heat and the other half goes into extra kinetic energy.

## Worked example

**Given:** a $1000\,\text{kg}$ satellite; $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$. Its orbit shrinks from $r_1 = 1.0 \times 10^{7}\,\text{m}$ to $r_2 = 8.0 \times 10^{6}\,\text{m}$ (round, illustrative radii).
**Find:** $K$, $U$ and $E$ before and after.

**Step 1 — the common factor.** $GMm = 4.0 \times 10^{14} \times 1000 = 4.0 \times 10^{17}\,\text{J m}$.

**Step 2 — first orbit.** $K_1 = 4.0 \times 10^{17} / (2 \times 1.0 \times 10^{7}) = 2.0 \times 10^{10}\,\text{J}$, so $U_1 = -4.0 \times 10^{10}\,\text{J}$ and $E_1 = -2.0 \times 10^{10}\,\text{J}$.

**Step 3 — second orbit.** $K_2 = 4.0 \times 10^{17} / (2 \times 8.0 \times 10^{6}) = 2.5 \times 10^{10}\,\text{J}$, so $U_2 = -5.0 \times 10^{10}\,\text{J}$ and $E_2 = -2.5 \times 10^{10}\,\text{J}$.

**Step 4 — what changed.** The total fell by $0.5 \times 10^{10}\,\text{J}$: that is what drag took away as heat. The kinetic energy **rose** by the same $0.5 \times 10^{10}\,\text{J}$, and the potential energy fell by twice that.

So the article was right: losing energy made the satellite faster.

**Sanity check:** $\Delta K + \Delta U = +0.5 \times 10^{10} - 1.0 \times 10^{10} = -0.5 \times 10^{10}\,\text{J}$, exactly the change in $E$.

## Where the picture breaks

The phone notification is only the way the news arrived; the physics is the satellite. Yash's hand out of a bus window is also a fair picture of drag, but on a bus nothing is pulling you inward to give you speed back. For the satellite, gravity does.

Our numbers are simplified. Real drag decay happens at a few hundred kilometres, much lower than the round radii we used, and the orbit shrinks slowly over many laps, so treating each moment as a circular orbit is a good approximation but not exact. The satellite's energy formulas also assume a spherical Earth and ignore the pulls of the Moon and Sun.

## Key takeaway

For a circular orbit, $K = GMm/2r$, $U = -GMm/r$ and $E = -GMm/2r$, so $K = -E$ and $U = 2E$. The total energy is negative because the satellite is bound. Lowering the orbit makes $E$ more negative but $K$ larger, which is why a satellite losing energy to drag speeds up.
