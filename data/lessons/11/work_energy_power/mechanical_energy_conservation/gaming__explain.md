---
concept_id: mechanical_energy_conservation
interest: gaming
format: explain
title: The jump pad you can tune without testing it
check:
  question: |-
    A crate is launched straight up at $10\,\text{m/s}$ in a game with Earth gravity and no air resistance. How fast is it moving when it has risen to **half** of its maximum height?
  options:
    A: |-
      $5\,\text{m/s}$
    B: |-
      $10\,\text{m/s}$
    C: |-
      $8.7\,\text{m/s}$
    D: |-
      $7.1\,\text{m/s}$
  answer: D
  explanation: |-
    At half the maximum height, half of the starting kinetic energy has become potential energy, so $K$ is halved. Since $K \propto v^2$, the speed falls by a factor $\sqrt{2}$: $v = 10/\sqrt{2} \approx 7.1\,\text{m/s}$.
  misconceptions:
    A: |-
      Halves the speed because half the height has been climbed; it is the *energy* that halves, and speed is proportional to the square root of the energy, not to the height.
    B: |-
      Reads "mechanical energy is conserved" as "speed is conserved"; the total stays fixed, but it moves from kinetic to potential, so the crate must slow down as it rises.
    C: |-
      Uses $v^2 = u^2 - gh$ instead of $v^2 = u^2 - 2gh$, losing the factor of 2 that comes from the $\tfrac{1}{2}$ in the kinetic energy.
author: claude-code/opus-5
written: 2026-09-23
---
## The story

![A gaming desk at night: a monitor shows a physics sandbox with a spring launcher, a kart at the top of a loop and a crate being dragged by a rope, beside a force-feedback racing wheel and a controller](scenes/gaming/work_energy_power.svg "A launched object trades speed for height on the way up, and takes it back on the way down.")

Meher's level has one job: a jump pad on the floor has to throw a supply crate onto a balcony, and the crate must land gently enough not to shatter. Her teammate Yash has been tuning it the way he always does — nudge the launch speed, hit play, watch, repeat. Forty attempts in, the crate either smashes through the railing or thumps down short.

"It's fine," Yash says. "I'll find the number."

Meher stops him. The engine's own numbers are right there in the debug overlay: the crate's speed, updated every frame, and its height. Between launch and the balcony, nothing touches the crate except gravity — no wind, no drag, and her level has air resistance switched off.

She thinks there is one equation that gives the landing speed and the exact launch speed needed, without a single test run. What links a height to a speed when gravity is the only thing acting?

## The physics

The **mechanical energy** of a body is its kinetic energy plus its potential energy:

$$E = K + U = \tfrac{1}{2}mv^2 + mgh$$

If only conservative forces (here, gravity) do work on it, $E$ does not change:

$$\tfrac{1}{2}mv_i^2 + mgh_i = \tfrac{1}{2}mv_f^2 + mgh_f$$

This follows straight from the work–energy theorem. The net work is the work done by gravity, which is $-\Delta U$, so $\Delta K = -\Delta U$, meaning $\Delta(K + U) = 0$: whatever one gains, the other loses, joule for joule.

![Energy against height for an object launched straight up: kinetic energy falls in a straight line to zero at the top, potential energy rises to meet it, and the dashed total stays flat](figures/mechanical_energy_conservation/ke-pe-vs-height.svg "Plotted for one particular launch, but the shape is universal: the two energies trade one for one, and the dashed total never moves.")

Three things make this useful:

- **Mass often cancels.** Divide through by $m$ and you get $\tfrac{1}{2}v_i^2 + gh_i = \tfrac{1}{2}v_f^2 + gh_f$ — the crate's mass never enters the answer.
- **The path does not matter.** Straight up, along a ramp or through a loop, only the height change counts, because gravity is conservative.
- **It only holds while no non-conservative force does work.** Switch air resistance on, or let the crate scrape a wall, and mechanical energy leaks away as heat.

## Worked example

**Given** (illustrative level values): a crate leaves the jump pad straight up at $u = 20\,\text{m/s}$, with $g = 9.8\,\text{m/s}^2$ and no air resistance.
**Find:** how high it rises, and how fast it is moving halfway up.

**Step 1 — the top.** At the highest point the crate is momentarily at rest, so all the kinetic energy has become potential energy: $\tfrac{1}{2}mu^2 = mgh$, and the mass cancels:

$$h = \frac{u^2}{2g} = \frac{400}{19.6} \approx 20\,\text{m}$$

About the height of a six-storey building — that is where the balcony has to be.

**Step 2 — halfway up.** At $h/2$, exactly half the energy is stored as potential energy, so the kinetic energy is half of what it was:

$$\tfrac{1}{2}mv^2 = \tfrac{1}{2}\left(\tfrac{1}{2}mu^2\right) \quad\Rightarrow\quad v = \frac{u}{\sqrt{2}} = \frac{20}{1.414} \approx 14\,\text{m/s}$$

Halfway up in *height*, the crate still has $70\%$ of its speed. Most of the slowing happens near the top.

**Sanity check:** the crate loses half its energy but only $30\%$ of its speed, which is what a square-root relationship should do.

## Where the picture breaks

Meher's answer is exact only because she switched air resistance off. With drag on, mechanical energy is no longer conserved: the crate rises lower than $20\,\text{m}$ and returns slower than it left, and the energy lost depends on the whole path, not just the height. Engines also step time forward in small jumps — typically $1/60\,\text{s}$ — and simple stepping methods quietly gain or lose a little energy each frame, which is why a bouncing object in a badly-built game can creep higher and higher. Real crates are not points, either: a tumbling crate carries rotational energy this equation ignores.

## Key takeaway

When only conservative forces do work, $K + U$ stays constant: $\tfrac{1}{2}mv_i^2 + mgh_i = \tfrac{1}{2}mv_f^2 + mgh_f$. Speed and height trade one for the other, the mass usually cancels, and the path taken never matters — only the change in height.
