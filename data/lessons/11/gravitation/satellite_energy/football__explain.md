---
concept_id: satellite_energy
interest: football
format: explain
title: The satellite that speeds up as the air drags on it
check:
  question: |-
    A satellite in a low circular orbit slowly loses mechanical energy to drag from the thin upper atmosphere, while staying on a nearly circular orbit. What happens to it?
  options:
    A: |-
      It stays at the same height but moves more slowly.
    B: |-
      It sinks to a lower orbit and moves faster.
    C: |-
      It sinks to a lower orbit and moves more slowly.
    D: |-
      It sinks to a lower orbit at the same speed.
  answer: B
  explanation: |-
    The total energy $E = -GMm/2r$ decreases (becomes more negative), so $r$ decreases. The kinetic energy $K = GMm/2r = -E$ then increases: the satellite sinks and speeds up, with the potential energy falling by twice the energy lost.
  misconceptions:
    A: |-
      Thinks drag simply slows the satellite in place; at a fixed radius only one speed, $\sqrt{GM/r}$, keeps a circular orbit, so a slower satellite must fall inward.
    C: |-
      Applies the everyday rule that friction always slows things down; here gravity does work as the satellite sinks, and it adds more kinetic energy than drag removes.
    D: |-
      Thinks orbital speed is the same for every orbit; it depends on radius, $v = \sqrt{GM/r}$, so a lower orbit is faster.
author: claude-code/opus-5
written: 2026-09-22
---
## The story

![A night match: the goalkeeper's long kick at the top of its arc, the Moon and a satellite overhead, and a dish on the stand roof aimed at the satellite](scenes/football/gravitation.svg "The satellite above the stadium is bound to the Earth. Its energy says so, and it holds a surprise.")

Rain has delayed kick-off, and Farah and Om are sheltering under the stand. Farah is reading about low satellites on her phone.

"Listen. Even four hundred kilometres up, there's a trace of air. It drags on low satellites, and they slowly lose height. And here's the strange part: as they sink, they go *faster*."

Om snorts. "Drag makes things slower. That's what drag *does*." He points at the waterlogged pitch. "Roll a ball across that and see how fast it stops."

"I know. But it says the satellite ends up moving faster than before."

"Then where does the extra energy come from? The air is taking energy away, not giving it."

Om is right that drag removes energy. So how can the satellite end up with *more* kinetic energy than before?

## The physics

Take a satellite of mass $m$ in a circular orbit of radius $r$ round a planet of mass $M$, with potential energy zero at infinity.

**Kinetic energy.** Gravity provides the centripetal force: $GMm/r^2 = mv^2/r$, so $mv^2 = GMm/r$ and

$$K = \tfrac{1}{2}mv^2 = \frac{GMm}{2r}$$

**Potential energy.**
$$U = -\frac{GMm}{r}$$

**Total energy.**
$$E = K + U = \frac{GMm}{2r} - \frac{GMm}{r} = -\frac{GMm}{2r}$$

So in every circular orbit $K = -E$ and $U = 2E$.

**Why is $E$ negative?** At infinity $U = 0$, and $K$ can never be negative. A body with total energy below zero can never get there: it is **bound** to the planet. The size of $E$, $GMm/2r$, is the **binding energy**, the least energy that must be supplied to free the satellite completely.

![A graph of energy against orbit radius: a blue kinetic energy curve above zero, a red potential energy curve below, and a green dashed total energy curve halfway between the red curve and zero](figures/satellite_energy/energy-vs-orbit-radius.svg "At every radius K = −E and U = 2E. Move to a smaller orbit and E and U fall while K rises.")

**Om's puzzle.** Drag removes energy, so $E$ becomes more negative and $r$ must get smaller. But since $K = -E$, the kinetic energy *rises* by exactly the energy drag removed. Where does it come from? As the satellite sinks, $U = 2E$ falls by *twice* that amount. Half of the potential energy released pays for the drag losses; the other half becomes kinetic energy. So the satellite sinks and speeds up.

## Worked example

**Given:** a satellite of mass $m = 500\,\text{kg}$ (illustrative), in a circular orbit of radius $r_1 = 6.8 \times 10^{6}\,\text{m}$, which drag lowers to $r_2 = 6.7 \times 10^{6}\,\text{m}$ (illustrative); $GM = 4.0 \times 10^{14}\,\text{m}^3/\text{s}^2$.
**Find:** $K$, $U$ and $E$ in the first orbit; the energy lost to drag; the change in speed.

$GMm = 4.0 \times 10^{14} \times 500 = 2.0 \times 10^{17}\,\text{J m}$.

$$K_1 = \frac{2.0 \times 10^{17}}{2 \times 6.8 \times 10^{6}} \approx 1.47 \times 10^{10}\,\text{J}, \qquad U_1 = -2K_1 \approx -2.94 \times 10^{10}\,\text{J}, \qquad E_1 = -K_1 \approx -1.47 \times 10^{10}\,\text{J}$$

Energy lost to drag:
$$E_1 - E_2 = \frac{GMm}{2}\left(\frac{1}{r_2} - \frac{1}{r_1}\right) = 1.0 \times 10^{17} \times (1.4925 - 1.4706) \times 10^{-7} \approx 2.2 \times 10^{8}\,\text{J}$$

So $K$ rises by about $2.2 \times 10^{8}\,\text{J}$ and $U$ falls by about $4.4 \times 10^{8}\,\text{J}$.

Speeds: $v_1 = \sqrt{GM/r_1} = \sqrt{5.88 \times 10^{7}} \approx 7.67\,\text{km/s}$ and $v_2 = \sqrt{5.97 \times 10^{7}} \approx 7.73\,\text{km/s}$.

**Sanity check:** $\Delta K + \Delta U = +2.2 \times 10^{8} - 4.4 \times 10^{8} = -2.2 \times 10^{8}\,\text{J}$, exactly the energy drag removed. And $\tfrac{1}{2} \times 500 \times (7.67 \times 10^{3})^2 \approx 1.47 \times 10^{10}\,\text{J}$, matching $K_1$.

## Where the picture breaks

Om's ball on a wet pitch really does just slow down: it rolls on flat ground, where gravity does no work on it. The satellite is different because every bit of sinking lets gravity do work. Our calculation also treats each moment as a perfect circular orbit. That's a good approximation only because drag acts gently over many orbits; the real path is a slow inward spiral. And the thin air's density changes with solar activity, so real satellites lose height at an uneven rate. The football here is only the setting.

## Key takeaway

For a circular orbit, $K = GMm/2r$, $U = -GMm/r$ and $E = -GMm/2r$, so $K = -E$ and $U = 2E$. The total energy is negative because the satellite is bound to the planet. When drag removes energy, the satellite sinks and speeds up: the potential energy falls by twice the loss, and half of that becomes kinetic energy.
