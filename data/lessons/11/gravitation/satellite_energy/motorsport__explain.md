---
concept_id: satellite_energy
interest: motorsport
format: explain
title: The drag that makes a satellite faster
check:
  question: |-
    Over many months, the thin upper atmosphere slowly drags a satellite from one circular orbit down into a lower circular orbit. Which statement is correct?
  options:
    A: |-
      Its kinetic energy decreases and its total energy decreases.
    B: |-
      Its kinetic energy increases and its total energy increases.
    C: |-
      Its kinetic energy increases and its total energy decreases.
    D: |-
      Both stay the same, because gravity does no net work on a satellite in a circular orbit.
  answer: C
  explanation: |-
    Drag removes energy, so $E = -GMm/2r$ becomes more negative and $r$ shrinks. But $K = GMm/2r$ grows as $r$ shrinks, so the satellite ends up moving faster while holding less total energy.
  misconceptions:
    A: |-
      Assumes drag must slow a satellite as it slows a car. Drag does remove energy, but the satellite responds by falling to a smaller $r$, where the orbital speed is higher.
    B: |-
      Sees the satellite speed up and concludes it has gained energy. The extra kinetic energy is paid for by a fall in potential energy twice as large, so the total goes down.
    D: |-
      True for a perfectly circular orbit with no drag — gravity is always perpendicular to the velocity there. With drag the orbit is shrinking, so the satellite never returns to the same radius.
author: claude-code/opus-5
written: 2026-09-24
---
## The story

![A pit lane at a hill-climb event: a car on a weighbridge, a team truck with a satellite dish on its roof, a GPS aerial on the car's engine cover and a drop-test rig beside the scrutineering bay](scenes/motorsport/gravitation.svg "Drag is the enemy of everything in this pit lane. A few hundred kilometres up, it behaves very strangely indeed.")

Kunal has spent the whole winter on drag. He has taped tufts of wool to the bodywork, filmed them, moved the mirrors, and shaved a genuine few km/h off the top speed loss. Drag, to him, is simple: it takes energy out, and the car goes slower.

Shalini is waiting for the session to start, reading about a small research satellite in a low orbit. She reads a line out to annoy him.

"It says here the satellite is being slowed by the last traces of the atmosphere. It's been up two years, and it's now going about a hundred metres per second **faster** than when it was launched."

"Read it again."

"I've read it four times."

Kunal puts down the wool. Drag can only take energy away — that is the one thing he is certain of after a whole winter. So how does something lose energy and end up faster?

## The physics

Take a satellite of mass $m$ in a circular orbit of radius $r$ around a planet of mass $M$, with potential energy measured as zero at infinity.

**Kinetic energy.** Gravity supplies the centripetal force, so $GMm/r^2 = mv^2/r$, giving $mv^2 = GMm/r$ and

$$K = \tfrac{1}{2}mv^2 = \frac{GMm}{2r}$$

**Potential energy.** $$U = -\frac{GMm}{r}$$

**Total energy.** $$E = K + U = \frac{GMm}{2r} - \frac{GMm}{r} = -\frac{GMm}{2r}$$

So in any circular orbit $K = -E$ and $U = 2E$. The potential energy is negative and always twice as big as the kinetic energy is positive.

**Why is $E$ negative?** At infinity $U = 0$ and $K$ cannot be less than zero, so anything with $E < 0$ can never get there. It is **bound**. The size of $E$, namely $GMm/2r$, is the **binding energy**: the smallest amount of energy you would have to add to set the satellite completely free.

![A graph of kinetic, potential and total energy against orbit radius: kinetic positive and falling, potential negative, and total energy halfway between the potential curve and zero](figures/satellite_energy/energy-vs-orbit-radius.svg "At every radius, K = −E and U = 2E. Shrinking the orbit pushes E and U down but pushes K up.")

**And Shalini's satellite.** Drag removes energy, so $E$ falls — becomes more negative. Since $E = -GMm/2r$, a lower $E$ means a smaller $r$: the orbit shrinks. But $K = GMm/2r$ grows as $r$ shrinks. The potential energy falls by *twice* as much as the total does, and that surplus pays both the drag and the extra kinetic energy. The satellite loses energy and speeds up, and there is no contradiction anywhere.

## Worked example

**Given:** a satellite of mass $m = 1000\,\text{kg}$ (illustrative), first at $r_1 = 1.0 \times 10^{7}\,\text{m}$, later dragged down to $r_2 = 8.0 \times 10^{6}\,\text{m}$; $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$, so $GMm = 4.0 \times 10^{17}\,\text{J}\,\text{m}$.
**Find:** the three energies in each orbit, and how much energy drag removed.

**Step 1 — the higher orbit.** $K_1 = GMm/2r_1 = 4.0 \times 10^{17}/(2.0 \times 10^{7}) = 2.0 \times 10^{10}\,\text{J}$, so $U_1 = -4.0 \times 10^{10}\,\text{J}$ and $E_1 = -2.0 \times 10^{10}\,\text{J}$.

**Step 2 — the lower orbit.** $K_2 = 4.0 \times 10^{17}/(1.6 \times 10^{7}) = 2.5 \times 10^{10}\,\text{J}$, so $E_2 = -2.5 \times 10^{10}\,\text{J}$.

**Step 3 — the bookkeeping.** Drag has taken away $E_1 - E_2 = 5.0 \times 10^{9}\,\text{J}$. Over the same time, kinetic energy went **up** by $5.0 \times 10^{9}\,\text{J}$, while potential energy fell by $1.0 \times 10^{10}\,\text{J}$ — exactly twice as much, which covers both.

**Sanity check:** the orbital speeds are $\sqrt{GM/r}$, so $6.3\,\text{km/s}$ before and $7.1\,\text{km/s}$ after. The satellite is measurably faster and measurably poorer, which is precisely what Shalini read out.

## Where the picture breaks

Motorsport is the setting here, not the analogy — and this is one place where the setting actively misleads, which is why it is worth using. On the car, drag and speed are locked together: remove energy and the car slows. A satellite has somewhere to put the loss, namely height, and height is worth twice as much as speed in the energy books. Kunal's intuition is correct for a car and wrong for an orbit.

The worked example also compares two neat circular orbits. A real decaying orbit is a long slow spiral that is never exactly circular, and the energy removed by drag becomes heat in the thin gas and on the satellite's skin. Near the end the air thickens quickly, the spiral steepens, and the satellite burns up — the point at which the tidy circular-orbit formulae stop applying altogether.

## Key takeaway

For a circular orbit, $K = GMm/2r$, $U = -GMm/r$ and $E = -GMm/2r$, so $K = -E$ and $U = 2E$. The total energy is negative because the satellite is bound, and its size is the binding energy. Take energy away and the orbit shrinks — which makes the satellite go faster, not slower.
